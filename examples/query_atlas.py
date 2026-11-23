#!/usr/bin/env python3
"""Minimal runnable example querying the Unsolved Mathematics Atlas & RAG corpus."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main() -> int:
    parser = argparse.ArgumentParser(description="Query the Unsolved Mathematics Atlas.")
    parser.add_argument("--top", type=int, default=10, help="Show top-N problems by CSS.")
    parser.add_argument("--field", type=str, default=None, help="Filter by primary field slug.")
    parser.add_argument("--status", type=str, default=None, help="Filter by status (open, partial, recently-resolved).")
    parser.add_argument("--search", type=str, default=None, help="Run BM25 retrieval query over rag/corpus.jsonl.")
    args = parser.parse_args()

    data = json.loads((ROOT / "data" / "problems.json").read_text(encoding="utf-8"))
    problems = data["problems"]

    if args.search:
        from rag.retriever import BM25, load_corpus

        bm25 = BM25(load_corpus())
        hits = bm25.search(args.search, k=5)
        print(f"BM25 top-{len(hits)} hits for {args.search!r}:")
        for score, doc in hits:
            print(f"  [{score:6.3f}] {doc['id']} ({doc.get('title', doc.get('slug'))} / {doc['section']})")
        return 0

    if args.field:
        problems = [p for p in problems if p.get("field") == args.field]
    if args.status:
        problems = [p for p in problems if p.get("status") == args.status]

    problems.sort(key=lambda p: (-float(p.get("css", 0.0)), p["slug"]))
    meta = data.get("meta", {})
    print(f"Atlas v{meta.get('version', '?')} (updated {meta.get('updated', '?')}) — showing {min(args.top, len(problems))}/{len(problems)} matches:")
    for i, p in enumerate(problems[: args.top], start=1):
        print(
            f"  {i:3d}. [{p['css']:5.1f}] {p['slug']:38s} "
            f"({p['status']}, {p['field']}, {p['year_posed']})"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
