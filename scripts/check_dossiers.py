#!/usr/bin/env python3
"""
check_dossiers.py — Completeness report for authored dossiers.

For every problem folder, reports which of the 7 section files are authored
(template marker removed), the paper-row and mathematician-row counts, and an
overall authored/total tally. Prints a table and a machine-readable JSON to
data/dossier-status.json so the Kanban / CI can consume it.

This is a *report*, not a gate (validate.py is the gate). Exit code is always 0
unless --strict is passed, in which case any un-authored section fails the run.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "problems"
OUT = ROOT / "data" / "dossier-status.json"
SECTIONS = ["history", "originator", "approaches", "attempts", "papers", "mathematicians", "status"]
MARKER = "<!-- DOSSIER:"


def count_table_rows(text: str) -> int:
    """Count markdown table data rows (excludes header + separator)."""
    rows = 0
    seen_sep = False
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        if re.match(r"^\|[\s:|-]+\|?$", s):
            seen_sep = True
            continue
        if seen_sep:
            rows += 1
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    if not PROBLEMS.exists():
        print("No problems/ directory.")
        return 0

    report = []
    for folder in sorted(PROBLEMS.iterdir()):
        if not folder.is_dir():
            continue
        meta_p = folder / "metadata.json"
        meta = json.loads(meta_p.read_text(encoding="utf-8")) if meta_p.exists() else {}
        entry = {"slug": folder.name, "rank": meta.get("rank"), "title": meta.get("title", folder.name),
                 "authored": {}, "papers": 0, "mathematicians": 0}
        for sec in SECTIONS:
            f = folder / f"{sec}.md"
            authored = f.exists() and MARKER not in f.read_text(encoding="utf-8")
            entry["authored"][sec] = authored
            if sec == "papers" and authored:
                entry["papers"] = count_table_rows(f.read_text(encoding="utf-8"))
            if sec == "mathematicians" and authored:
                entry["mathematicians"] = count_table_rows(f.read_text(encoding="utf-8"))
        entry["complete"] = all(entry["authored"].values())
        report.append(entry)

    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    complete = sum(1 for e in report if e["complete"])
    print(f"{'#':>3}  {'slug':32} {'sections':9} {'papers':>6} {'people':>6}")
    print("-" * 64)
    for e in sorted(report, key=lambda x: (x["rank"] or 999)):
        n = sum(e["authored"].values())
        mark = "OK " if e["complete"] else "   "
        print(f"{str(e['rank'] or '?'):>3}  {e['slug']:32} {mark}{n}/7   {e['papers']:>6} {e['mathematicians']:>6}")
    print("-" * 64)
    print(f"Complete dossiers: {complete}/{len(report)}  ->  data/dossier-status.json")

    if args.strict and complete != len(report):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
