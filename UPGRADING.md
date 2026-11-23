# Upgrading Guide (`UPGRADING.md`)

> **Build Standard v1.1.0 item A41.** Breaking changes, data migrations, and upgrade steps between structural versions of `unsolved-mathematics`.

---

## Upgrading from `v0.2.0` to `v0.3.0`

### 1. Breaking / Behavioral Changes

- **Mandatory `jsonschema` validation:** `scripts/validate.py` and `scripts/check_papers.py` no longer silently skip schema checks if `jsonschema` is missing. Install pinned dependencies via `python -m pip install -r requirements-lock.txt`.
- **Deterministic RAG Chunk IDs (`rag/corpus.jsonl`):** Chunk IDs now use monotonic per-`(slug, section)` indices (`<slug>/<section>#<idx>`) instead of resetting `#0` per heading (which previously caused ~80% ID collisions in dict lookups). Downstream consumers caching old chunk IDs must re-index against the `v0.3.0` `rag/corpus.jsonl` (3,763 unique chunks).
- **Deterministic Token Estimator:** The optional `tiktoken` branch in `rag/build_corpus.py` was removed so token counts are identical across all environments.
- **Pinned `CURRENT_YEAR = 2026` & Tie-Breaking:** `scripts/generate.py` now computes ages against `CURRENT_YEAR = 2026`, breaks CSS ties deterministically by `(-composite_severity, slug)`, and refreshes all 106 `problems/<slug>/README.md` rank headers (fixing 81 stale ranks).
- **Tightened `proof_claim_sweep.py`:** Generic words (`candidate`, `heuristic`, `attempt`) no longer suppress proof-claim flags. Any refuted or speculative sketch must carry an explicit **WITHDRAWN / REFUTED** header or reside under `quarantine/`.
- **Stripped Invalid Citations:** 109 hallucinated/mismatched/404 identifiers were removed from 73 `problems/*/papers.md` files and replaced with `—` / `needs-verification` (full audit trail in `data/citation-verification-log.json`).
- **Compressed Collatz Archive File:** `problems/collatz-conjecture/experiments/results/odd_unit_lock_transition_microscope_d13_R12_N50000_20260705.json` (38.6 MB) was losslessly compressed to `.json.gz` (0.64 MB). Decompress with `gzip -dk` if re-running legacy scripts directly on it.
- **Workflow Change (Build Standard R2/R4):** `.github/PULL_REQUEST_TEMPLATE.md` was removed; development commits directly to `main` while external reports use `.github/ISSUE_TEMPLATE/` forms.

### 2. Upgrade Steps

```bash
git pull origin main
python -m pip install -r requirements-lock.txt
python scripts/generate.py --check
python scripts/validate.py
python scripts/build_data_manifest.py --check
python -m pytest -v tests/
```

To also verify the new `formal/` Lean 4.35.0 package, install `elan` (auto-reads `formal/lean-toolchain` = `leanprover/lean4:v4.35.0`) and run `cd formal && lake build && lake env lean VerifyAxioms.lean`.

---

## Upgrading from `v0.1.0` to `v0.2.0`

- Expanded registry from 40 to 106 problems (`data/problems.yaml`).
- Added `meta-analyses/` (106 AI-assisted syntheses) and `scripts/check_papers.py` integrity gate.
- Added `CITATION.cff`, `AUTHORS.md`, and `SUBMISSIONS.md`.
