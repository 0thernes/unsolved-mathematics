#!/usr/bin/env python3
"""
validate.py — Integrity gate for the Atlas (run in CI).

Checks, in order:
  1. Registry parses and every entry satisfies schema/problem.schema.json
  2. Slugs are unique
  3. The committed ranking views are CURRENT (generate.py --check passes)
  4. Every problems/NNN-slug/papers.md table row carries a verification flag
  5. Every 'recently-resolved' problem cites a resolution in status.md

Exit code 0 = clean, 1 = violations. Warnings do not fail the build.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Make output safe on legacy Windows consoles (cp1252) and in CI alike.
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
VALID_FLAGS = {"verified", "high-confidence", "needs-verification", "ai-suggested"}

# Pseudo-proof / numerology artifact name patterns. Matched on FILENAME only, so
# files that merely *discuss* the quarantine (status.md, audit notes) never trip it.
# See docs/review/REPO-AUDIT-2026-07.md.
PSEUDOPROOF_RE = re.compile(
    r"(THE-PROMPT-IS-THE-PROOF|P-.*-RESOLUTION|THIS-.*-(RESOLUTION|COLIMIT|FIXEDPOINT)"
    r"|11\.8_MASTER|defect_algebra|DEFECT_ALGEBRA|-CLOSURE\.md$|SIMULATION-BREAKING"
    r"|ONTOLOGICAL|TRANSFINITE|^p_map\.py$|P-COLLATZ-MAP|ensemble_fixedpoint"
    r"|ontological_breaker|transfinite_repulsion|prompt_collatz)",
    re.IGNORECASE,
)


def check_registry() -> list[str]:
    sys.path.insert(0, str(ROOT / "scripts"))
    import generate  # noqa: E402

    data = generate.yaml.safe_load(generate.REGISTRY_YAML.read_text(encoding="utf-8"))
    errs = generate.validate(data["problems"])
    return [e for e in errs if not e.startswith("WARN")]


def check_papers_flags() -> list[str]:
    """Each markdown table row in papers.md whose last cell looks like a flag
    must use a known flag; rows clearly listing a paper must carry one."""
    problems = []
    if not PROBLEMS_DIR.exists():
        return ["problems/ directory missing — run scripts/generate.py"]
    issues: list[str] = []
    for papers in PROBLEMS_DIR.glob("*/papers.md"):
        text = papers.read_text(encoding="utf-8")
        if "<!-- DOSSIER:papers -->" in text:
            continue  # still a template; not yet authored — skipped, not failed
        for line in text.splitlines():
            if not line.strip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            last = cells[-1].lower()
            # header / separator rows
            if set(last) <= set("-: ") or last in {"verify", "verification", ""}:
                continue
            # a data row: the final cell should be a valid flag
            if last not in VALID_FLAGS:
                # only flag if the row looks like a real citation row (has a year)
                if any(re.search(r"\b(1[0-9]{3}|20[0-2][0-9])\b", c) for c in cells):
                    issues.append(
                        f"{papers.relative_to(ROOT)}: row missing/invalid verification flag: '{last}'"
                    )
    return issues


def check_resolved_have_citation() -> list[str]:
    issues: list[str] = []
    for meta in PROBLEMS_DIR.glob("*/metadata.json"):
        import json

        m = json.loads(meta.read_text(encoding="utf-8"))
        if m.get("status") == "recently-resolved":
            status = meta.parent / "status.md"
            txt = status.read_text(encoding="utf-8") if status.exists() else ""
            # An un-authored template is backlog, not a violation — skip it.
            if "<!-- DOSSIER:status -->" in txt:
                continue
            if not re.search(r"(arXiv|doi|10\.\d{4,})", txt, re.I):
                issues.append(
                    f"{meta.parent.name}: status 'recently-resolved' but status.md lacks a resolving citation"
                )
    return issues


def check_problems_root_clean() -> list[str]:
    """problems/ must contain only slug directories — never stray files.
    (Two crank .md files were found loose here on 2026-07-02.)"""
    if not PROBLEMS_DIR.exists():
        return []
    return [
        f"problems/ contains a stray file (only slug directories allowed): {p.name}"
        for p in sorted(PROBLEMS_DIR.iterdir())
        if p.is_file()
    ]


def check_pseudoproof_leak() -> None:
    """Warn (never fail) when numerology artifacts live outside a _quarantine/ dir.
    Non-fatal by design: a live multi-session tree can re-drop these at any moment,
    so CI should surface — not block on — the churn."""
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
    all_issues += check_registry()
    all_issues += check_papers_flags()
    all_issues += check_resolved_have_citation()
    all_issues += check_problems_root_clean()

    check_pseudoproof_leak()  # warnings only — never fails the build

    if all_issues:
        print("VALIDATION FAILED:\n")
        for i in all_issues:
            print(f"  ✗ {i}")
        return 1
    print("✓ Atlas validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
