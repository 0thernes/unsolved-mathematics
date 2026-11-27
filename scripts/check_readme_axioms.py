#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Verify README.md & STATEMENT_FIDELITY.md verbatim `#print axioms` parity + Palomar limits.

Playbook v1.3 Checklist #4 & #10:
  1. Parses every `#print axioms <decl>` in `lean/VerifyAxioms.lean`.
  2. Verifies every audited declaration appears verbatim inside the `<!-- AXIOMS:START -->`
     ... `<!-- AXIOMS:END -->` block of `README.md` AND inside `lean/STATEMENT_FIDELITY.md`.
  3. Verifies zero disallowed axioms appear anywhere in those verbatim blocks
     (strictly subset of `{propext, Classical.choice, Quot.sound}`).
  4. Checks Palomar rules on `lean/`:
     - Every `.lean` file begins with `module`.
     - `lean/Challenge.lean` is strictly <= 1,000 lines and <= 100 KiB.
     - Every other `.lean` file is <= 10,000 lines.
     - Zero `sorry`, `admit`, `native_decide`, `sorryAx`, `Lean.trustCompiler`, or custom
       `axiom` in code (comments stripped) outside `lean/Challenge.lean`.

Exit code 0 = clean; 1 = drift or violation.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEAN_DIR = ROOT / "lean"
README = ROOT / "README.md"
FIDELITY = LEAN_DIR / "STATEMENT_FIDELITY.md"
VERIFY_AXIOMS = LEAN_DIR / "VerifyAxioms.lean"
COMPARATOR = LEAN_DIR / "comparator.json"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}

AXIOM_LINE_RE = re.compile(
    r"'([^']+)'\s+(?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)",
    re.S,
)
FORBIDDEN_RE = re.compile(
    r"\b(sorry|admit|native_decide|sorryAx|Lean\.trustCompiler|Lean\.ofReduceBool|implemented_by)\b"
    r"|^\s*((?:private|protected|noncomputable)\s+)*axiom\b"
    r"|@\[(?:extern|csimp)\b"
    r"|_native\.",
    re.M,
)


def strip_lean_comments(src: str) -> str:
    out: list[str] = []
    i, n, depth = 0, len(src), 0
    while i < n:
        if depth == 0 and src[i : i + 2] == "--":
            while i < n and src[i] != "\n":
                i += 1
        elif src[i : i + 2] == "/-":
            depth += 1
            i += 2
        elif depth > 0 and src[i : i + 2] == "-/":
            depth -= 1
            i += 2
        elif depth == 0:
            out.append(src[i])
            i += 1
        else:
            if src[i] == "\n":
                out.append("\n")
            i += 1
    return "".join(out)


def parse_expected_declarations() -> list[str]:
    decls: list[str] = []
    for line in VERIFY_AXIOMS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*#print\s+axioms\s+([A-Za-z0-9_.]+)\s*$", line)
        if m:
            decls.append(m.group(1))
    return decls


def check_verbatim_block(path: Path, text: str, expected_decls: list[str]) -> list[str]:
    issues: list[str] = []
    found: dict[str, set[str]] = {}
    for m in AXIOM_LINE_RE.finditer(text):
        name = m.group(1)
        raw = m.group(2) or ""
        used = {a.strip() for a in raw.split(",") if a.strip()}
        found[name] = used
        bad = used - ALLOWED_AXIOMS
        if bad:
            issues.append(f"{path.relative_to(ROOT)}: disallowed axiom(s) {sorted(bad)} in {name}")
    missing = [d for d in expected_decls if d not in found]
    if missing:
        issues.append(
            f"{path.relative_to(ROOT)}: missing {len(missing)} audited declaration(s) from verbatim `#print axioms`: {missing[:5]}"
        )
    return issues


def main() -> int:
    issues: list[str] = []
    if not LEAN_DIR.exists():
        print("ERROR: lean/ directory missing.", file=sys.stderr)
        return 1

    expected_decls = parse_expected_declarations()
    comp = json.loads(COMPARATOR.read_text(encoding="utf-8"))
    comp_theorems = comp.get("theorem_names", [])
    for t in comp_theorems:
        if t not in expected_decls:
            issues.append(f"lean/VerifyAxioms.lean missing comparator theorem: {t}")

    # Check README.md verbatim block
    readme_txt = README.read_text(encoding="utf-8")
    m = re.search(r"<!-- AXIOMS:START -->(.*?)<!-- AXIOMS:END -->", readme_txt, re.S)
    if not m:
        issues.append("README.md missing <!-- AXIOMS:START --> ... <!-- AXIOMS:END --> verbatim #print axioms block")
    else:
        issues.extend(check_verbatim_block(README, m.group(1), expected_decls))

    # Check lean/STATEMENT_FIDELITY.md verbatim block
    if not FIDELITY.exists():
        issues.append("lean/STATEMENT_FIDELITY.md missing")
    else:
        issues.extend(check_verbatim_block(FIDELITY, FIDELITY.read_text(encoding="utf-8"), expected_decls))

    # Palomar rules & forbidden token audit
    if not (LEAN_DIR / "lake-manifest.json").exists():
        issues.append("lean/lake-manifest.json missing (required by Palomar rules)")
    lean_files = sorted(LEAN_DIR.rglob("*.lean"))
    lean_files = [f for f in lean_files if ".lake" not in f.parts and "build" not in f.parts]
    for lf in lean_files:
        if lf.is_symlink():
            issues.append(f"{lf.relative_to(ROOT).as_posix()}: symlinked .lean file forbidden by Palomar rules")
            continue
        raw = lf.read_text(encoding="utf-8")
        lines = raw.splitlines()
        rel = lf.relative_to(ROOT).as_posix()
        if not any(ln.strip() == "module" for ln in lines[:10]):
            issues.append(f"{rel}: missing `module` header (Palomar rule)")
        if lf.name == "Challenge.lean":
            if len(lines) > 1000:
                issues.append(f"{rel}: exceeds Palomar 1,000-line limit ({len(lines)} lines)")
            if len(raw.encode("utf-8")) > 100 * 1024:
                issues.append(f"{rel}: exceeds Palomar 100 KiB limit ({len(raw.encode('utf-8'))} bytes)")
        else:
            if len(lines) > 10000:
                issues.append(f"{rel}: exceeds Palomar 10,000-line limit ({len(lines)} lines)")
            code = strip_lean_comments(raw)
            for fm in FORBIDDEN_RE.finditer(code):
                lineno = code[: fm.start()].count("\n") + 1
                issues.append(f"{rel}:{lineno}: forbidden Lean proof token `{fm.group(0)}`")

    if issues:
        print("AXIOM & PALOMAR CHECK FAILED:", file=sys.stderr)
        for i in issues:
            print(f"  - {i}", file=sys.stderr)
        return 1

    print(
        f"OK: {len(expected_decls)} declarations ({len(comp_theorems)} comparator theorems) verified in "
        f"README.md + lean/STATEMENT_FIDELITY.md; {len(lean_files)} Lean files satisfy Palomar limits & zero forbidden tokens."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
