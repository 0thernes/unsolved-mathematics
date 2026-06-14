#!/usr/bin/env python3
"""
retriever.py — Query the Atlas corpus.

Zero-dependency BM25 retriever over rag/corpus.jsonl, with an optional dense
(embedding) path if sentence-transformers + numpy are installed and an index
has been built by rag/embed_index.py.

Usage:
    python rag/retriever.py "what is the connection between RH and random matrices"
    python rag/retriever.py --k 8 --section papers "bounded gaps between primes"
    python rag/retriever.py --dense "Hodge classes and algebraic cycles"

The BM25 implementation is intentionally small and self-contained so the atlas
is queryable out of the box, in CI, and offline.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "rag" / "corpus.jsonl"
INDEX = ROOT / "rag" / "index.npz"   # written by embed_index.py (optional)

TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokenize(s: str) -> list[str]:
    return TOKEN_RE.findall(s.lower())


def load_corpus() -> list[dict]:
    if not CORPUS.exists():
        raise SystemExit("corpus.jsonl missing — run: python rag/build_corpus.py")
    return [json.loads(line) for line in CORPUS.read_text(encoding="utf-8").splitlines() if line.strip()]


class BM25:
    """Okapi BM25 over the corpus chunks."""

    def __init__(self, docs: list[dict], k1: float = 1.5, b: float = 0.75):
        self.docs = docs
        self.k1, self.b = k1, b
        self.tok = [tokenize(d["text"]) for d in docs]
        self.len = [len(t) for t in self.tok]
        self.avgdl = (sum(self.len) / len(self.len)) if self.len else 0.0
        self.df: Counter = Counter()
        for t in self.tok:
            self.df.update(set(t))
        self.N = len(docs)
        self.idf = {
            term: math.log(1 + (self.N - n + 0.5) / (n + 0.5))
            for term, n in self.df.items()
        }
        self.tf = [Counter(t) for t in self.tok]

    def search(self, query: str, k: int = 5, section: str | None = None) -> list[tuple[float, dict]]:
        q = tokenize(query)
        scored: list[tuple[float, dict]] = []
        for i, d in enumerate(self.docs):
            if section and d.get("section") != section:
                continue
            score = 0.0
            dl = self.len[i] or 1
            for term in q:
                if term not in self.tf[i]:
                    continue
                f = self.tf[i][term]
                idf = self.idf.get(term, 0.0)
                score += idf * (f * (self.k1 + 1)) / (
                    f + self.k1 * (1 - self.b + self.b * dl / (self.avgdl or 1))
                )
            if score > 0:
                scored.append((score, d))
        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[:k]


def dense_search(query: str, k: int, section: str | None):
    try:
        import numpy as np
        from sentence_transformers import SentenceTransformer
    except Exception:
        raise SystemExit("Dense search needs: pip install -r requirements-rag.txt")
    if not INDEX.exists():
        raise SystemExit("No dense index — run: python rag/embed_index.py")
    data = np.load(INDEX, allow_pickle=True)
    mat, ids = data["embeddings"], list(data["ids"])
    docs = {d["id"]: d for d in load_corpus()}
    model = SentenceTransformer(str(data["model"]))
    q = model.encode([query], normalize_embeddings=True)[0]
    sims = mat @ q
    order = sims.argsort()[::-1]
    out = []
    for idx in order:
        d = docs.get(ids[idx])
        if d is None or (section and d.get("section") != section):
            continue
        out.append((float(sims[idx]), d))
        if len(out) >= k:
            break
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Query the Unsolved Mathematics Atlas.")
    ap.add_argument("query", nargs="+")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--section", default=None, help="restrict to a dossier section")
    ap.add_argument("--dense", action="store_true", help="use embedding search")
    args = ap.parse_args()
    query = " ".join(args.query)

    if args.dense:
        hits = dense_search(query, args.k, args.section)
    else:
        hits = BM25(load_corpus()).search(query, args.k, args.section)

    if not hits:
        print("No matches.")
        return 0
    for rank, (score, d) in enumerate(hits, 1):
        print(f"\n[{rank}] score={score:.3f}  #{d.get('rank')} {d['title']} · {d['section']}/{d.get('heading','')}")
        print(f"    {d['source']}")
        snippet = d["text"].replace("\n", " ")
        print("    " + (snippet[:280] + "…" if len(snippet) > 280 else snippet))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
