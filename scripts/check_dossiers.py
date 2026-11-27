#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""
check_dossiers.py — Completeness & structural integrity report for authored dossiers.

For every problem folder, reports which of the 7 section files are authored
(template marker removed), the paper-row and mathematician-row counts, and an
overall authored/total tally. Prints a table and writes data/dossier-status.json.

With --strict, also enforces structural & epistemic table invariants:
  - Every data row in papers.md has exactly 7 Markdown columns (catches unescaped
    `|` inside LaTeX absolute values).
  - Every data row in mathematicians.md has exactly 5 Markdown columns
    (`# | Name | Era | Role | Contribution`).
  - Zero duplicate non-dash identifiers inside any single papers.md.
  - Zero bare arXiv IDs missing the canonical `arXiv:` prefix.
  - Exact 1-to-1 parity between `verified` rows in papers.md and `verified`
    records in data/citation-verification-log.json (zero unlogged verified rows).
  - Zero lines with odd unescaped `$` outside fenced code blocks.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[union-attr]
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "problems"
OUT = ROOT / "data" / "dossier-status.json"
CIT_LOG = ROOT / "data" / "citation-verification-log.json"
SECTIONS = ["history", "originator", "approaches", "attempts", "papers", "mathematicians", "status"]
MARKER = "<!-- DOSSIER:"
BARE_ARXIV_RE = re.compile(r"^(?:\d{4}\.\d{4,5}(?:v\d+)?|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})$", re.I)
VALID_VERIFY_FLAGS = {"verified", "high-confidence", "needs-verification", "ai-suggested"}


def count_table_rows(text: str) -> int:
    """Count markdown table data rows across one or more tables (excludes every
    table's header and separator rows)."""
    rows = 0
    in_table_body = False
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            in_table_body = False
            continue
        if re.match(r"^\|[\s:|-]+\|?$", s):
            in_table_body = True
            continue
        if in_table_body:
            rows += 1
    return rows


def check_table_structure(slug: str, section: str, text: str, expected_cols: int) -> tuple[list[str], list[tuple[str, str]]]:
    """Validate table column counts and (for papers.md) identifier hygiene."""
    errors: list[str] = []
    verified_pairs: list[tuple[str, str]] = []
    in_table_body = False
    seen_ids: set[str] = set()
    for lineno, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if not s.startswith("|"):
            in_table_body = False
            continue
        if re.match(r"^\|[\s:|-]+\|?$", s):
            in_table_body = True
            continue
        if not in_table_body:
            continue
        cols = [c.strip() for c in s.strip("|").split("|")]
        if len(cols) != expected_cols:
            errors.append(
                f"{slug}/{section}.md:{lineno}: expected {expected_cols} columns, found {len(cols)} "
                "(check for unescaped '|' inside LaTeX math)"
            )
            continue
        if section == "papers":
            ident, flag = cols[5], cols[6].lower()
            if flag not in VALID_VERIFY_FLAGS:
                errors.append(f"{slug}/papers.md:{lineno}: invalid Verify flag '{cols[6]}'")
            if BARE_ARXIV_RE.match(ident):
                errors.append(f"{slug}/papers.md:{lineno}: bare arXiv ID '{ident}' missing 'arXiv:' prefix")
            if ident not in ("—", "-", ""):
                key = ident.lower()
                if key in seen_ids:
                    errors.append(f"{slug}/papers.md:{lineno}: duplicate identifier '{ident}'")
                seen_ids.add(key)
            if flag == "verified":
                if ident in ("—", "-", ""):
                    errors.append(f"{slug}/papers.md:{lineno}: verified row has empty identifier")
                else:
                    verified_pairs.append((slug, ident.lower()))
    return errors, verified_pairs


def check_dollar_balance(slug: str, section: str, text: str) -> list[str]:
    """Flag lines with an odd count of unescaped inline `$` outside fenced code blocks."""
    errors: list[str] = []
    in_code = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        cleaned = re.sub(r"`[^`]+`", "", line).replace(r"\$", "").replace("$$", "")
        if cleaned.count("$") % 2 == 1:
            errors.append(f"{slug}/{section}.md:{lineno}: odd unescaped '$' count (broken inline math or unescaped currency)")
    return errors


def load_logged_verified_set() -> set[tuple[str, str]] | None:
    if not CIT_LOG.exists():
        return None
    data = json.loads(CIT_LOG.read_text(encoding="utf-8"))
    out: set[tuple[str, str]] = set()
    for rec in data.get("records", []):
        if rec.get("verdict") == "verified":
            out.add((str(rec["slug"]), str(rec.get("identifier_raw", "")).strip().lower()))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    if not PROBLEMS.exists():
        print("No problems/ directory.")
        return 0

    report: list[dict[str, Any]] = []
    structural_errors: list[str] = []
    all_verified_in_md: list[tuple[str, str]] = []

    for folder in sorted(PROBLEMS.iterdir()):
        if not folder.is_dir():
            continue
        meta_p = folder / "metadata.json"
        meta = json.loads(meta_p.read_text(encoding="utf-8")) if meta_p.exists() else {}
        entry: dict[str, Any] = {
            "slug": folder.name,
            "rank": meta.get("rank"),
            "title": meta.get("title", folder.name),
            "authored": {},
            "papers": 0,
            "mathematicians": 0,
        }
        for sec in SECTIONS:
            f = folder / f"{sec}.md"
            text = f.read_text(encoding="utf-8") if f.exists() else ""
            authored = f.exists() and MARKER not in text
            entry["authored"][sec] = authored
            if authored:
                structural_errors.extend(check_dollar_balance(folder.name, sec, text))
                if sec == "papers":
                    entry["papers"] = count_table_rows(text)
                    errs, vpairs = check_table_structure(folder.name, sec, text, expected_cols=7)
                    structural_errors.extend(errs)
                    all_verified_in_md.extend(vpairs)
                elif sec == "mathematicians":
                    entry["mathematicians"] = count_table_rows(text)
                    errs, _ = check_table_structure(folder.name, sec, text, expected_cols=5)
                    structural_errors.extend(errs)
        entry["complete"] = all(entry["authored"].values())
        report.append(entry)

    logged_verified = load_logged_verified_set()
    if logged_verified is not None:
        md_set = set(all_verified_in_md)
        for slug, ident in sorted(md_set - logged_verified):
            structural_errors.append(
                f"{slug}/papers.md: verified identifier '{ident}' is missing from data/citation-verification-log.json"
            )
        for slug, ident in sorted(logged_verified - md_set):
            structural_errors.append(
                f"data/citation-verification-log.json: logged verified identifier ({slug}, '{ident}') is not marked verified in papers.md"
            )

    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")

    complete = sum(1 for e in report if e["complete"])
    print(f"{'#':>3}  {'slug':32} {'sections':9} {'papers':>6} {'people':>6}")
    print("-" * 64)
    for e in sorted(report, key=lambda x: (x["rank"] or 999)):
        n = sum(e["authored"].values())
        mark = "OK " if e["complete"] else "   "
        print(f"{str(e['rank'] or '?'):>3}  {e['slug']:32} {mark}{n}/7   {e['papers']:>6} {e['mathematicians']:>6}")
    print("-" * 64)
    print(f"Complete dossiers: {complete}/{len(report)}  ->  data/dossier-status.json")

    if structural_errors:
        print(f"\nStructural/citation integrity errors ({len(structural_errors)}):")
        for err in structural_errors[:30]:
            print(f"  - {err}")
        if len(structural_errors) > 30:
            print(f"  ... (+{len(structural_errors) - 30} more)")

    if args.strict and (complete != len(report) or structural_errors):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
