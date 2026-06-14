#!/usr/bin/env python3
"""
embed_index.py — Build a dense vector index over the corpus (optional).

Reads rag/corpus.jsonl, embeds every chunk with a sentence-transformers model
(default: all-MiniLM-L6-v2, 384-dim, runs on CPU), and writes a compact numpy
archive rag/index.npz consumed by retriever.py --dense.

    python rag/embed_index.py
    python rag/embed_index.py --model BAAI/bge-small-en-v1.5

Requires:  pip install -r requirements-rag.txt
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "rag" / "corpus.jsonl"
INDEX = ROOT / "rag" / "index.npz"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="sentence-transformers/all-MiniLM-L6-v2")
    ap.add_argument("--batch", type=int, default=64)
    args = ap.parse_args()

    try:
        import numpy as np
        from sentence_transformers import SentenceTransformer
    except Exception:
        raise SystemExit("Install deps first:  pip install -r requirements-rag.txt")

    if not CORPUS.exists():
        raise SystemExit("corpus.jsonl missing — run: python rag/build_corpus.py")

    docs = [json.loads(l) for l in CORPUS.read_text(encoding="utf-8").splitlines() if l.strip()]
    if not docs:
        raise SystemExit("Corpus is empty.")

    model = SentenceTransformer(args.model)
    texts = [d["text"] for d in docs]
    emb = model.encode(
        texts, batch_size=args.batch, normalize_embeddings=True, show_progress_bar=True
    )
    np.savez_compressed(
        INDEX,
        embeddings=np.asarray(emb, dtype="float32"),
        ids=np.array([d["id"] for d in docs], dtype=object),
        model=args.model,
    )
    print(f"Indexed {len(docs)} chunks with {args.model} -> {INDEX.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
