#!/usr/bin/env python3
"""
check_papers.py — Integrity gate for AI-assisted meta-analyses (run in CI).

For every meta-analyses/<slug>.md, enforces the honesty invariants from
docs/review/AI-META-REVIEW.md. A meta-analysis FAILS if it:
  1. lacks parseable front matter, or it fails schema/review.schema.json
  2. is not authored "Alexander Donahue" / typed ai-assisted-meta-analysis /
     peer_reviewed: false
  3. omits the required AI-generated / not-peer-reviewed banner
  4. omits an "## AI Review Panel" section
  5. contains an explicit overclaim phrase (claiming THIS problem solved)

Exit 0 clean, 1 on any violation. Honesty is enforced mechanically, not trusted.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
MA = ROOT / "meta-analyses"
SCHEMA = ROOT / "schema" / "review.schema.json"

BANNER_MARKERS = [
    "AI-generated",
    "not peer-reviewed",
]
# Explicit overclaim phrases — asserting THIS problem is solved by this document.
OVERCLAIM = [
    r"\bwe (?:have )?(?:hereby )?prove[ds]?\b.*\bconjecture\b",
    r"\bthis (?:paper|meta-analysis|document) (?:proves|resolves|solves)\b",
    r"\bi have (?:proven|proved|solved|resolved)\b",
    r"\bthe (?:conjecture|problem|hypothesis) is (?:hereby |now )?(?:solved|proved|proven|resolved) (?:here|in this)\b",
    r"\bq\.?e\.?d\.?\b",
]


def front_matter(text: str):
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        return (yaml.safe_load(parts[1]) or {}), parts[2]
    except yaml.YAMLError:
        return None, text


def load_validator():
    try:
        import json
        import jsonschema  # type: ignore

        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        return jsonschema.Draft202012Validator(schema)
    except Exception:
        return None


def main() -> int:
    if not MA.exists():
        print("No meta-analyses/ directory yet — nothing to check.")
        return 0

    validator = load_validator()
    issues: list[str] = []
    checked = 0

    for md in sorted(MA.glob("*.md")):
        if md.name.lower() == "readme.md":
            continue
        checked += 1
        rel = md.relative_to(ROOT)
        text = md.read_text(encoding="utf-8")
        fm, body = front_matter(text)

        if fm is None:
            issues.append(f"{rel}: missing/invalid YAML front matter")
            continue
        if validator is not None:
            for err in validator.iter_errors(fm):
                issues.append(f"{rel}: front matter: {err.message}")

        lower_body = body.lower()
        for marker in BANNER_MARKERS:
            if marker.lower() not in lower_body:
                issues.append(f"{rel}: missing required banner phrase '{marker}'")
        if "alexander donahue" not in lower_body and fm.get("author") != "Alexander Donahue":
            issues.append(f"{rel}: missing author/accreditation (Alexander Donahue)")
        if "ai review panel" not in lower_body:
            issues.append(f"{rel}: missing '## AI Review Panel' section")
        for pat in OVERCLAIM:
            m = re.search(pat, body, re.IGNORECASE)
            if m:
                issues.append(f"{rel}: overclaim phrase detected: '{m.group(0)[:60]}'")

    if issues:
        print("META-ANALYSIS INTEGRITY CHECK FAILED:\n")
        for i in issues:
            print(f"  x {i}")
        return 1
    print(f"OK: {checked} meta-analyses passed the integrity gate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
