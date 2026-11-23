#!/usr/bin/env python3
"""
validate.py — Integrity gate for the Atlas (run in CI).

Checks, in order:
  1. Registry parses and every entry satisfies schema/problem.schema.json
  2. Slugs are unique
  3. VERSION single-source parity across VERSION, data/problems.yaml, CITATION.cff, pyproject.toml
  4. Generated views are current (zero drift in data/problems.json, RANKING.md, README.md,
     problems/<slug>/metadata.json, and problems/<slug>/README.md rank headers)
  5. Every problems/<slug>/papers.md table row carries a valid verification flag
  6. Every 'recently-resolved' problem cites a resolving DOI or arXiv ID in status.md
  7. problems/ root contains only slug directories (zero stray files)
  8. rag/corpus.jsonl has globally unique chunk IDs (regression gate for Bug #1)
  9. Zero broken relative markdown links across top-level docs, docs/, and problems/<slug>/*.md

Exit code 0 = clean, 1 = violations. Warnings do not fail the build.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[union-attr]
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
CORPUS_PATH = ROOT / "rag" / "corpus.jsonl"
VALID_FLAGS = {"verified", "high-confidence", "needs-verification", "ai-suggested"}

PSEUDOPROOF_RE = re.compile(
    r"(THE-PROMPT-IS-THE-PROOF|P-.*-RESOLUTION|THIS-.*-(RESOLUTION|COLIMIT|FIXEDPOINT)"
    r"|11\.8_MASTER|defect_algebra|DEFECT_ALGEBRA|-CLOSURE\.md$|SIMULATION-BREAKING"
    r"|ONTOLOGICAL|TRANSFINITE|^p_map\.py$|P-COLLATZ-MAP|ensemble_fixedpoint"
    r"|ontological_breaker|transfinite_repulsion|prompt_collatz)",
    re.IGNORECASE,
)

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")
FENCE_RE = re.compile(r"```.*?```", re.S)


def check_registry_and_freshness() -> list[str]:
    sys.path.insert(0, str(ROOT / "scripts"))
    import generate  # noqa: E402

    data = generate.yaml.safe_load(generate.REGISTRY_YAML.read_text(encoding="utf-8"))
    errs = [e for e in generate.validate(data["problems"]) if not e.startswith("WARN")]
    if errs:
        return errs
    ranked = generate.rank_problems(data["problems"])
    return generate.check_freshness(ranked, data["meta"])


def check_version_parity() -> list[str]:
    version_file = ROOT / "VERSION"
    if not version_file.exists():
        return ["VERSION file is missing"]
    ver = version_file.read_text(encoding="utf-8").strip()
    issues: list[str] = []

    sys.path.insert(0, str(ROOT / "scripts"))
    import generate  # noqa: E402

    reg = generate.yaml.safe_load(generate.REGISTRY_YAML.read_text(encoding="utf-8"))
    reg_ver = str(reg.get("meta", {}).get("version", ""))
    if reg_ver != ver:
        issues.append(f"data/problems.yaml meta.version ({reg_ver}) != VERSION ({ver})")

    cff = ROOT / "CITATION.cff"
    if cff.exists():
        cff_data = generate.yaml.safe_load(cff.read_text(encoding="utf-8"))
        cff_ver = str(cff_data.get("version", ""))
        if cff_ver != ver:
            issues.append(f"CITATION.cff version ({cff_ver}) != VERSION ({ver})")

    pyproj = ROOT / "pyproject.toml"
    if pyproj.exists():
        m = re.search(r'^version\s*=\s*"([^"]+)"', pyproj.read_text(encoding="utf-8"), re.M)
        if m and m.group(1) != ver:
            issues.append(f"pyproject.toml version ({m.group(1)}) != VERSION ({ver})")
    return issues


def check_papers_flags() -> list[str]:
    """Each markdown table row in papers.md listing a paper must carry a valid flag."""
    if not PROBLEMS_DIR.exists():
        return ["problems/ directory missing — run scripts/generate.py"]
    issues: list[str] = []
    for papers in sorted(PROBLEMS_DIR.glob("*/papers.md")):
        text = papers.read_text(encoding="utf-8")
        if "<!-- DOSSIER:papers -->" in text:
            continue
        for line in text.splitlines():
            if not line.strip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            last = cells[-1].lower()
            if set(last) <= set("-: ") or last in {"verify", "verification", ""}:
                continue
            if last not in VALID_FLAGS:
                if any(re.search(r"\b(1[0-9]{3}|20[0-2][0-9])\b", c) for c in cells):
                    issues.append(
                        f"{papers.relative_to(ROOT)}: row missing/invalid verification flag: '{last}'"
                    )
    return issues


def check_resolved_have_citation() -> list[str]:
    issues: list[str] = []
    for meta in sorted(PROBLEMS_DIR.glob("*/metadata.json")):
        m = json.loads(meta.read_text(encoding="utf-8"))
        if m.get("status") == "recently-resolved":
            status = meta.parent / "status.md"
            txt = status.read_text(encoding="utf-8") if status.exists() else ""
            if "<!-- DOSSIER:status -->" in txt:
                continue
            if not re.search(r"(arXiv|doi|10\.\d{4,})", txt, re.I):
                issues.append(
                    f"{meta.parent.name}: status 'recently-resolved' but status.md lacks a resolving citation"
                )
    return issues


def check_problems_root_clean() -> list[str]:
    """problems/ must contain only slug directories — never stray files."""
    if not PROBLEMS_DIR.exists():
        return []
    return [
        f"problems/ contains a stray file (only slug directories allowed): {p.name}"
        for p in sorted(PROBLEMS_DIR.iterdir())
        if p.is_file()
    ]


def check_corpus_ids() -> list[str]:
    """Ensure rag/corpus.jsonl (if present) has strictly unique chunk IDs."""
    if not CORPUS_PATH.exists():
        return []
    seen: set[str] = set()
    dups = 0
    for line in CORPUS_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        cid = rec.get("id")
        if not isinstance(cid, str) or not cid:
            return ["rag/corpus.jsonl contains a record without a string id"]
        if cid in seen:
            dups += 1
        seen.add(cid)
    if dups:
        return [f"rag/corpus.jsonl contains {dups} duplicate chunk id(s) — run python rag/build_corpus.py"]
    return []


def check_relative_links() -> list[str]:
    """Ensure core markdown files and problem dossiers have no broken relative links."""
    issues: list[str] = []
    targets = (
        list(ROOT.glob("*.md"))
        + list((ROOT / "docs").rglob("*.md"))
        + list(PROBLEMS_DIR.glob("*/*.md"))
    )
    for f in sorted(targets):
        txt = FENCE_RE.sub("", f.read_text(encoding="utf-8", errors="replace"))
        for m in LINK_RE.finditer(txt):
            tgt = m.group(1).strip()
            if not tgt or tgt.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if not ("/" in tgt or "." in tgt):
                continue
            if not (f.parent / tgt).resolve().exists():
                issues.append(f"broken link in {f.relative_to(ROOT)} -> {tgt}")
    return issues


def check_pseudoproof_leak() -> None:
    """Warn (never fail) when numerology artifacts live outside a _quarantine/ dir."""
    if not PROBLEMS_DIR.exists():
        return
    leaks = [
        str(f.relative_to(ROOT))
        for f in PROBLEMS_DIR.rglob("*")
        if f.is_file()
        and "_quarantine" not in f.parts
        and PSEUDOPROOF_RE.search(f.name)
    ]
    if leaks:
        print(
            f"\n⚠ {len(leaks)} pseudo-proof/numerology file(s) live outside _quarantine/ "
            f"(sweep them in; see docs/review/REPO-AUDIT-2026-07.md):"
        )
        for leak in sorted(leaks)[:25]:
            print(f"    - {leak}")
        if len(leaks) > 25:
            print(f"    … and {len(leaks) - 25} more")


def main() -> int:
    all_issues: list[str] = []
    all_issues += check_registry_and_freshness()
    all_issues += check_version_parity()
    all_issues += check_papers_flags()
    all_issues += check_resolved_have_citation()
    all_issues += check_problems_root_clean()
    all_issues += check_corpus_ids()
    all_issues += check_relative_links()

    check_pseudoproof_leak()  # warnings only

    if all_issues:
        print("VALIDATION FAILED:\n")
        for i in all_issues:
            print(f"  ✗ {i}")
        return 1
    print("✓ Atlas validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
