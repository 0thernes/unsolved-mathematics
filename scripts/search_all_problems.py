#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""search_all_problems.py — fast offline unified search across the curated Atlas + all 59k+ mirrored Left to Solve items.

Searches both:
  1. Curated Atlas dossiers (data/problems.json — full 7-section dossiers + CSS ranks)
  2. All 25 daily-mirrored Left to Solve programs (data/external/lefttosolve/items/*.jsonl)

Zero third-party dependencies beyond Python stdlib.

Examples:
    python scripts/search_all_problems.py --query "prime gap"
    python scripts/search_all_problems.py --program "Erdős Problems" --prize-only --kind open
    python scripts/search_all_problems.py --field "Number Theory" --kind open --limit 30
    python scripts/search_all_problems.py --query "collatz" --json
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_JSON = ROOT / "data" / "problems.json"
EXT_DIR = ROOT / "data" / "external" / "lefttosolve"
SNAPSHOT = EXT_DIR / "snapshot.json"
ITEMS_DIR = EXT_DIR / "items"


def search_atlas(
    query: str = "",
    field: str = "",
    limit: int = 25,
) -> list[dict[str, Any]]:
    """Search curated Atlas core problems in data/problems.json."""
    if limit <= 0 or not PROBLEMS_JSON.exists():
        return []
    reg = json.loads(PROBLEMS_JSON.read_text(encoding="utf-8"))
    q = query.strip().lower()
    fld = field.strip().lower()
    hits: list[dict[str, Any]] = []
    for p in reg.get("problems", []):
        blob = " ".join(
            [
                str(p.get("slug", "")),
                str(p.get("title", "")),
                str(p.get("field", "")),
                " ".join(p.get("subfields") or []),
                " ".join(p.get("tags") or []),
                str(p.get("statement_plain", "")),
            ]
        ).lower()
        if q and q not in blob:
            continue
        if fld and fld not in str(p.get("field", "")).lower() and not any(fld in sf.lower() for sf in (p.get("subfields") or [])):
            continue
        hits.append(
            {
                "layer": "curated-atlas",
                "rank": p.get("rank"),
                "id": p["slug"],
                "title": p["title"],
                "field": p.get("field", ""),
                "status": p.get("status", ""),
                "css": p.get("css"),
                "url": f"https://github.com/0thernes/unsolved-mathematics/tree/main/problems/{p['slug']}",
            }
        )
        if len(hits) >= limit:
            break
    return hits


def search_external(
    query: str = "",
    program: str = "",
    field: str = "",
    kind: str = "",
    prize_only: bool = False,
    solved_only: bool = False,
    limit: int = 25,
) -> list[dict[str, Any]]:
    """Search all daily-mirrored Left to Solve items across all 25 sharded JSONL programs."""
    if limit <= 0 or not SNAPSHOT.exists():
        return []
    snap = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    q = query.strip().lower()
    prog_q = program.strip().lower()
    fld = field.strip().lower()
    knd = kind.strip().lower()
    # Search formal/curated Lean programs before large unformalized Q&A/comment streams
    programs = sorted(
        snap.get("programs", []),
        key=lambda p: (1 if "(not formalized)" in str(p.get("name", "")).lower() else 0, str(p.get("name", ""))),
    )
    hits: list[dict[str, Any]] = []
    for p in programs:
        if prog_q and prog_q not in p["name"].lower() and prog_q not in p["slug"].lower():
            continue
        shard_names = p.get("shards") or [f"{p['slug']}.jsonl"]
        for fn in shard_names:
            sp = ITEMS_DIR / fn
            if not sp.exists():
                continue
            with sp.open("r", encoding="utf-8") as fh:
                for line in fh:
                    if not line.strip():
                        continue
                    it = json.loads(line)
                    if knd and str(it.get("kind", "")).lower() != knd:
                        continue
                    if prize_only and not it.get("prize"):
                        continue
                    if solved_only and not it.get("solved"):
                        continue
                    if fld and not any(fld in str(f).lower() for f in (it.get("fields") or [])):
                        continue
                    if q:
                        hay = f"{it.get('id', '')} {it.get('title', '')} {' '.join(it.get('fields') or [])}".lower()
                        if q not in hay:
                            continue
                    hits.append(
                        {
                            "layer": "external-lefttosolve",
                            "program": p["name"],
                            "id": it["id"],
                            "title": it["title"],
                            "kind": it["kind"],
                            "fields": it.get("fields") or [],
                            "prize": it.get("prize"),
                            "solved": bool(it.get("solved")),
                            "url": f"https://lefttosolve.com/p/{urllib.parse.quote(str(it['id']), safe='.-_')}",
                        }
                    )
                    if len(hits) >= limit:
                        return hits
    return hits


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]
    except Exception:
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--query", "-q", default="", help="Substring search over id, title, fields, tags")
    ap.add_argument("--program", "-p", default="", help="Filter Left to Solve program name or slug")
    ap.add_argument("--field", "-f", default="", help="Filter mathematical field substring")
    ap.add_argument("--kind", "-k", default="", help="Filter external kind: open, known, warmup, unformalized")
    ap.add_argument("--prize-only", action="store_true", help="Only return external items carrying a prize label")
    ap.add_argument("--solved-only", action="store_true", help="Only return external items with site solved flag")
    ap.add_argument("--layer", choices=("all", "atlas", "external"), default="all", help="Search scope")
    ap.add_argument("--limit", "-n", type=int, default=20, help="Max results per layer (default 20)")
    ap.add_argument("--json", action="store_true", dest="as_json", help="Emit JSON output")
    args = ap.parse_args()

    atlas_hits = [] if args.layer == "external" or args.program or args.kind or args.prize_only or args.solved_only else search_atlas(
        query=args.query, field=args.field, limit=args.limit
    )
    ext_hits = [] if args.layer == "atlas" else search_external(
        query=args.query,
        program=args.program,
        field=args.field,
        kind=args.kind,
        prize_only=args.prize_only,
        solved_only=args.solved_only,
        limit=args.limit,
    )
    if args.as_json:
        print(json.dumps({"atlas": atlas_hits, "external": ext_hits}, ensure_ascii=False, indent=2))
        return 0

    print(f"=== Curated Atlas Core ({len(atlas_hits)} match(es)) ===")
    for h in atlas_hits:
        print(f"  #{h['rank']:>3} [{h['status']}] {h['title']} ({h['field']}) — {h['id']}")
    print(f"\n=== Left to Solve Daily Mirror ({len(ext_hits)} match(es), cap={args.limit}) ===")
    for h in ext_hits:
        pr = f" [{h['prize']}]" if h.get("prize") else ""
        sl = " [site-solved]" if h.get("solved") else ""
        print(f"  [{h['program']} | {h['kind']}{pr}{sl}] {h['id']} — {h['title']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
