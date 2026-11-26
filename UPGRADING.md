# Upgrading Guide (`UPGRADING.md`)

> **Build Standard v1.2.0 item A41.** Breaking changes, data migrations, and upgrade steps between structural versions of `unsolved-mathematics`.

---

## Upgrading from `v0.4.0` to `v0.5.0`

### 1. Structural & Additive Changes (Non-Breaking)

- **Eight-Domain Lean 4.35.0 Core (`22 → 45` theorems, `36 → 69` audited declarations):** All 22 `v0.4.0` comparator theorem names in `lean/Challenge.lean` are preserved verbatim; 23 new headline theorems, 4 new non-vacuity witnesses, and 6 new adversarial refutations were added across four new domain modules (`Primes.lean`, `Goldbach.lean`, `PerfectNumbers.lean`, `Ramsey.lean`) plus extensions to Collatz, Erdős–Straus, Lonely Runner ($n=3$), and Brocard ($n \le 20$).
- **FAIR Metadata (`ro-crate-metadata.json`, `croissant.json`):** Added RO-Crate 1.1 and MLCommons Croissant 1.0 files, tracked in `data/MANIFEST.sha256` (40 tracked files).
- **Live GitHub Pages Auto-Deploy:** `.github/workflows/pages.yml` now deploys `_site/index.html` and `_site/blueprint.html` automatically on push to `main`.
- **Runtime `NameError` fixed in `problems/collatz-conjecture/experiments/odd_unit_lock_bridge_refinement.py`**, guarded by `ruff --select E9,F63,F7,F82` in CI.

### 2. Upgrade Steps

```bash
git pull origin main
python -m pip install -r requirements-lock.txt
python scripts/generate.py --check
python scripts/validate.py
python scripts/check_retractions.py --check
python scripts/check_readme_axioms.py
python scripts/build_data_manifest.py --check
python -m pytest -v tests/
cd lean && lake build Challenge Solution NonVacuity Adversarial && lake env lean VerifyAxioms.lean
```

---

## Upgrading from `v0.3.x` to `v0.4.0`

### 1. Breaking / Structural Changes

- **Formal core moved `formal/` → `lean/`:** The Lean 4.35.0 package now lives under `lean/` (matching Build Standard `v1.2.0` `B22` and sibling `0thernes` repos). A redirect stub remains at `formal/ROADMAP.md` so legacy links do not 404.
- **Expanded Lean comparator targets (14 → 22 theorems) + `Adversarial.lean`:** All 14 `v0.3.x` theorem names are preserved verbatim; 8 new headline theorems and 8 adversarial false-variant refutations (`lean/Adversarial.lean`) were added (36 total audited declarations in `lean/VerifyAxioms.lean`).
- **New CI & verification gates:** `scripts/check_retractions.py --check` (`data/retraction-audit.json`), `scripts/check_readme_axioms.py` (verbatim `#print axioms` parity + Palomar limits), and `VERSION` parity extended to `lean/lakefile.toml` & `lean/formalization.yaml`.
- **Companion AMS-LaTeX white paper (`paper/`):** Compiled PDF and clean-room-verified `arxiv_submission.tar.gz` are now tracked in `data/MANIFEST.sha256` and attached to SLSA-attested GitHub Releases.

### 2. Upgrade Steps

```bash
git pull origin main
python -m pip install -r requirements-lock.txt
python scripts/generate.py --check
python scripts/validate.py
python scripts/check_retractions.py --check
python scripts/check_readme_axioms.py
python scripts/build_data_manifest.py --check
python -m pytest -v tests/
cd lean && lake build Challenge Solution NonVacuity Adversarial && lake env lean VerifyAxioms.lean
```

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
