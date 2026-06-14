# 🔎 RAG Layer — Retrieval-Augmented Generation over the Atlas

The Atlas is designed from the ground up to be **machine-ingestible**. Every
human-readable dossier doubles as a retrieval corpus. This directory turns the
`problems/` tree into a queryable knowledge base.

## Pipeline

```
data/problems.yaml ──generate.py──▶ problems/<slug>/*.md
                                          │
                                build_corpus.py   (heading-aware, token-aware chunking)
                                          ▼
                                  rag/corpus.jsonl  ◀── BM25 retriever (zero deps)
                                          │
                                  embed_index.py    (optional, sentence-transformers)
                                          ▼
                                   rag/index.npz   ◀── dense retriever (--dense)
```

## Quickstart

```bash
# 1. Build / refresh the corpus (stdlib only)
python rag/build_corpus.py

# 2. Query immediately with BM25 — no model download required
python rag/retriever.py "connection between the Riemann Hypothesis and random matrices"
python rag/retriever.py --k 8 --section papers "bounded gaps between primes"

# 3. (Optional) Build a dense index and use semantic search
pip install -r requirements-rag.txt
python rag/embed_index.py
python rag/retriever.py --dense "Hodge classes and algebraic cycles"
```

## Corpus schema (`corpus.jsonl`)

One JSON object per chunk:

| Field | Meaning |
|-------|---------|
| `id` | `slug::section::n` stable chunk id |
| `rank` | Atlas rank of the parent problem |
| `slug` / `title` / `field` | Problem identity |
| `section` | Which dossier file (`history`, `papers`, …) |
| `heading` | Nearest markdown heading |
| `text` | The chunk text (~380 tokens, 60-token overlap) |
| `source` | Path back to the source markdown |
| `tokens` | Token count (tiktoken if available) |

## Design choices

- **Heading-aware chunking** keeps a paper list, a biography, and a proof
  sketch from bleeding into one another.
- **Deterministic output** so `corpus.jsonl` diffs cleanly in git.
- **Graceful degradation**: everything works with the standard library; heavy
  ML deps are strictly optional and only power semantic search.
- **Provenance preserved**: each chunk links back to its source file and to the
  problem's `metadata.json`, so a downstream agent can cite exactly.

## Using it as an agent tool

`corpus.jsonl` is a drop-in source for LangChain, LlamaIndex, a custom MCP
server, or Anthropic's Files/embeddings APIs. The `retriever.BM25` class is
importable directly:

```python
from rag.retriever import BM25, load_corpus
hits = BM25(load_corpus()).search("odd perfect numbers lower bound", k=5)
```
