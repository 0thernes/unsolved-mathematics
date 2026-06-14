#!/usr/bin/env python3
"""
build_corpus.py — Turn the Atlas into a retrieval-ready corpus.

Walks every problems/NNN-slug/ dossier, splits each markdown document into
overlapping, heading-aware chunks, and writes a single JSONL corpus that any
RAG stack can ingest:

    rag/corpus.jsonl   (one JSON object per chunk)

Each record:
    {
      "id":        "riemann-hypothesis::papers::3",
      "rank":      1,
      "slug":      "riemann-hypothesis",
      "title":     "The Riemann Hypothesis",
      "field":     "Analytic Number Theory",
      "section":   "papers",
      "heading":   "Foundational papers",
      "text":      "....",
      "source":    "problems/001-riemann-hypothesis/papers.md",
      "tokens":    412
    }

Stdlib-only. Token counting uses tiktoken if installed, else a ~4-chars/token
heuristic. Designed to be deterministic so the corpus is diff-friendly in git.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
OUT = ROOT / "rag" / "corpus.jsonl"

TARGET_TOKENS = 380      # nominal chunk size
OVERLAP_TOKENS = 60      # sliding-window overlap between chunks
SECTION_FILES = [
    "README", "history", "originator", "approaches",
    "attempts", "papers", "mathematicians", "status",
]

try:
    import tiktoken  # type: ignore

    _ENC = tiktoken.get_encoding("cl100k_base")

    def count_tokens(s: str) -> int:
        return len(_ENC.encode(s))
except Exception:  # pragma: no cover
    def count_tokens(s: str) -> int:
        return max(1, len(s) // 4)


def load_metadata(folder: Path) -> dict:
    meta = folder / "metadata.json"
    if meta.exists():
        return json.loads(meta.read_text(encoding="utf-8"))
    return {}


def split_by_heading(md: str) -> list[tuple[str, str]]:
    """Return list of (heading, body) blocks split on markdown ATX headings."""
    blocks: list[tuple[str, str]] = []
    current_heading = ""
    buf: list[str] = []
    for line in md.splitlines():
        if re.match(r"^#{1,6}\s", line):
            if buf:
                blocks.append((current_heading, "\n".join(buf).strip()))
                buf = []
            current_heading = line.lstrip("#").strip()
        else:
            buf.append(line)
    if buf:
        blocks.append((current_heading, "\n".join(buf).strip()))
    return [(h, b) for h, b in blocks if b]


def window(text: str) -> list[str]:
    """Greedy sentence/paragraph packing into ~TARGET_TOKENS chunks w/ overlap."""
    units = re.split(r"\n\s*\n", text)  # paragraph-level units
    chunks: list[str] = []
    cur: list[str] = []
    cur_tok = 0
    for u in units:
        ut = count_tokens(u)
        if cur and cur_tok + ut > TARGET_TOKENS:
            chunks.append("\n\n".join(cur))
            # build overlap tail
            tail, tail_tok = [], 0
            for piece in reversed(cur):
                pt = count_tokens(piece)
                if tail_tok + pt > OVERLAP_TOKENS:
                    break
                tail.insert(0, piece)
                tail_tok += pt
            cur, cur_tok = list(tail), tail_tok
        cur.append(u)
        cur_tok += ut
    if cur:
        chunks.append("\n\n".join(cur))
    return chunks


def build() -> int:
    if not PROBLEMS_DIR.exists():
        print("No problems/ directory yet — run scripts/generate.py first.")
        return 0

    records: list[dict] = []
    for folder in sorted(PROBLEMS_DIR.iterdir()):
        if not folder.is_dir():
            continue
        meta = load_metadata(folder)
        slug = meta.get("slug", folder.name.split("-", 1)[-1])
        for section in SECTION_FILES:
            doc = folder / f"{section}.md"
            if not doc.exists():
                continue
            md = doc.read_text(encoding="utf-8")
            for heading, body in split_by_heading(md):
                for i, chunk in enumerate(window(body)):
                    records.append(
                        {
                            "id": f"{slug}::{section}::{len(records)}",
                            "rank": meta.get("rank"),
                            "slug": slug,
                            "title": meta.get("title", folder.name),
                            "field": meta.get("field"),
                            "section": section,
                            "heading": heading,
                            "text": chunk,
                            "source": str(doc.relative_to(ROOT)).replace("\\", "/"),
                            "tokens": count_tokens(chunk),
                        }
                    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as fh:
        for r in records:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    total_tokens = sum(r["tokens"] for r in records)
    print(f"Wrote {len(records)} chunks ({total_tokens:,} tokens) -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(build())
