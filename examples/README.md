# Examples (`examples/`)

Executable examples demonstrating how to query the canonical registry (`data/problems.json`), run deterministic BM25 retrieval over `rag/corpus.jsonl`, and inspect primary-source citation audit results (`data/citation-verification-log.json`).

## Quick Run

```bash
python examples/query_atlas.py --top 10
python examples/query_atlas.py --field "number-theory" --status open
python examples/query_atlas.py --search "positivity localization collatz"
```

All examples use only the Python standard library once `data/problems.json` and `rag/corpus.jsonl` are built.
