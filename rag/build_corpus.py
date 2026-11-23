#!/usr/bin/env python3
"""
build_corpus.py — Turn the Atlas into a retrieval-ready corpus.

Walks every problems/<slug>/ dossier, splits each markdown document into
overlapping, heading-aware chunks, and writes a single deterministic JSONL
corpus that any RAG stack can ingest:

    rag/corpus.jsonl   (one JSON object per chunk)

Each record carries a globally unique id:
    {
      "id":        "riemann-hypothesis::papers::3",
      "rank":      1,
      "slug":      "riemann-hypothesis",
      "title":     "The Riemann Hypothesis",
      "field":     "Analytic Number Theory",
      "section":   "papers",
      "heading":   "Foundational papers",
      "text":      "....",
      "source":    "problems/riemann-hypothesis/papers.md",
      "tokens":    412
    }

Stdlib-only and environment-independent: token counts use a deterministic
4-chars/token estimator so outputs are byte-identical across machines and CI
regardless of optional third-party tokenizer packages.
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


def count_tokens(s: str) -> int:
    """Deterministic, zero-dependency token estimate (~4 chars/token)."""
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
    """Greedy paragraph packing into ~TARGET_TOKENS chunks w/ overlap."""
    units = re.split(r"\n\s*\n", text)  # paragraph-level units
    chunks: list[str] = []
    cur: list[str] = []
    cur_tok = 0
    for u in units:
        ut = count_tokens(u)
        if cur and cur_tok + ut > TARGET_TOKENS:
            chunks.append("\n\n".join(cur))
            # build overlap tail
            tail: list[str] = []
            tail_tok = 0
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


def build_records(problems_dir: Path = PROBLEMS_DIR, root: Path = ROOT) -> list[dict]:
    """Build deterministic corpus records with globally unique chunk IDs."""
    records: list[dict] = []
    seen_ids: set[str] = set()
    for folder in sorted(problems_dir.iterdir()):
        if not folder.is_dir():
            continue
        meta = load_metadata(folder)
        slug = meta.get("slug", folder.name)
        for section in SECTION_FILES:
            doc = folder / f"{section}.md"
            if not doc.exists():
                continue
            md = doc.read_text(encoding="utf-8")
            chunk_idx = 0
            for heading, body in split_by_heading(md):
                for chunk in window(body):
                    cid = f"{slug}::{section}::{chunk_idx}"
                    if cid in seen_ids:  # pragma: no cover - invariant guard
                        raise ValueError(f"Duplicate corpus chunk id generated: {cid}")
                    seen_ids.add(cid)
                    chunk_idx += 1
                    records.append(
                        {
                            "id": cid,
                            "rank": meta.get("rank"),
                            "slug": slug,
                            "title": meta.get("title", folder.name),
                            "field": meta.get("field"),
                            "section": section,
                            "heading": heading,
                            "text": chunk,
                            "source": str(doc.relative_to(root)).replace("\\", "/"),
                            "tokens": count_tokens(chunk),
                        }
                    )
    return records


def build() -> int:
    if not PROBLEMS_DIR.exists():
        print("No problems/ directory yet — run scripts/generate.py first.")
        return 0

    records = build_records(PROBLEMS_DIR, ROOT)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="\n") as fh:
        for r in records:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    total_tokens = sum(r["tokens"] for r in records)
    print(f"Wrote {len(records)} chunks ({total_tokens:,} tokens) -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(build())
