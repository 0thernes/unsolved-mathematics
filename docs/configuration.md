# Configuration Reference

All configurable parameters for The Unsolved Mathematics Atlas (`v0.8.2`). The repository
runs fully offline out of the box with zero required secrets or environment
variables.

| Variable / File | Default | Purpose |
|---|---|---|
| `VERSION` | `0.8.2` | Single source of truth for semantic version (checked against `data/problems.yaml`, `CITATION.cff`, `pyproject.toml`, `lean/lakefile.toml`, `lean/formalization.yaml`, `ro-crate-metadata.json`, `croissant.json`) |
| `data/problems.yaml` | — | Single source of truth for all 120 problem entries, scores, and statuses |
| `scripts/generate.py` (`CURRENT_YEAR`) | `2026` | Frozen reference year for reproducible `age_score` calculation |
| `rag/build_corpus.py` (`TARGET_TOKENS`, `OVERLAP_TOKENS`) | `380`, `60` | Chunking window sizes for deterministic `rag/corpus.jsonl` generation |
| `PY` (env var) | `python` | Python executable override for `Makefile` and `justfile` |
| `ATLAS_CONTACT_EMAIL` (env var) | `0_0@0thernes.art` | Polite contact header for Crossref / DataCite / arXiv API verification (`scripts/verify_citations.py`, `scripts/check_retractions.py`) |
| `COMPARATOR_BWRAP` (env var) | `bwrap` | Path to Linux `bubblewrap` binary for sandboxed `lake check` / `lake comparator` |
| `ATLAS_EMBED_MODEL` (env var) | `all-MiniLM-L6-v2` | Optional SentenceTransformer model for `rag/embed_index.py` |
| `lean/lean-toolchain` | `leanprover/lean4:v4.35.0` | Pinned Lean 4 compiler and bundled external kernels |
| `lean/comparator.json` | — | Target 66-theorem list across 8 domains and permitted axiom allowlist for `lake comparator` (`autoImplicit = false` in `lean/lakefile.toml`) |

See `.env.example` for a copy-ready template.
