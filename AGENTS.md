# AGENTS.md

Canonical instructions for every coding agent working in this repository
(Antigravity, Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Grok Build, etc.).
`CLAUDE.md`, `GEMINI.md`, `.cursor/rules/build-standard.mdc`, and `llms.txt` all
point here. Edit this file, never the pointers.

## Project

- **Name:** The Unsolved Mathematics Atlas (`0thernes/unsolved-mathematics`)
- **Purpose:** Reproducible, ranked, research-grade atlas of 106 open mathematical problems across 38 fields, paired with a standalone zero-Mathlib multi-kernel Lean 4.35.0 formal verification core (`lean/`), primary-source citation & Crossref retraction auditing, a deterministic BM25/dense RAG corpus, an interactive proof blueprint (`_site/blueprint.html`), and a compiled AMS-LaTeX technical white paper (`paper/`).
- **Owner:** Alexander S. Donahue (`@0thernes`, ORCID `0009-0006-8168-9648`, independent researcher — do NOT use `0thernes LLC` until an entity is legally formed)
- **Manifest:** `repo.yaml` (Build Standard for LLMs `v1.2.0`)
- **Version:** `VERSION` (single source of truth; verified equal to `data/problems.yaml`, `CITATION.cff`, `pyproject.toml`, `lean/lakefile.toml`, and `lean/formalization.yaml`)
- **Stack:** Python 3.11+ (`PyYAML`, `jsonschema`, `pytest`, `hypothesis`, `ruff`, `mypy`) + Lean 4.35.0 (`lean/`, zero Mathlib, 6-kernel `lake check --paranoid` + `lake comparator --paranoid`) + AMS-LaTeX (`tectonic`)
- **Layout:**
  - `data/` — canonical registry (`problems.yaml`), generated `problems.json`, `dossier-status.json`, `citation-verification-log.json`, `retraction-audit.json`, `MANIFEST.sha256` (+ DigiCert RFC 3161 `.tsr` & Bitcoin OpenTimestamps `.ots` proofs)
  - `problems/<slug>/` — 106 self-contained problem dossiers (8 markdown files + `metadata.json` + `rag/`)
  - `lean/` — standalone Lean 4.35.0 formal core (`autoImplicit = false`, `FormalAtlas/`, `Challenge.lean`, `Solution.lean`, `NonVacuity.lean`, `Adversarial.lean`, `VerifyAxioms.lean`, `comparator.json`, `formalization.yaml`, `STATEMENT_FIDELITY.md`, `six_kernel_audit.txt`)
  - `paper/` — AMS-LaTeX white paper (`Donahue_2026_unsolved_mathematics_atlas.tex`, `references.bib`, compiled PDF, clean-room-verified `arxiv_submission.tar.gz`)
  - `scripts/` — build engine (`generate.py`), integrity gate (`validate.py`), dossier/paper/pseudo-proof/citation/retraction/README-axiom checkers, live negative Lean kernel test (`test_lean_negative.py`), dual timestamp tool (`timestamp_manifest.py`), static site + proof blueprint builder (`build_site.py`), Build Standard v1.2.0 auditors (`Audit-Repo.ps1`, `audit-repo.sh`)
  - `rag/` — deterministic chunker (`build_corpus.py`), BM25 & optional dense retriever (`retriever.py`)
  - `tests/` — unit, negative, regression, property-based (Hypothesis), golden/determinism, differential, metamorphic, and mutation tests
  - `meta-analyses/` — 106 AI-assisted surveys (all explicitly labeled AI-generated, not peer-reviewed)
  - `docs/` — architecture, methodology, indexes, Cross-Atlas Audit (`docs/CROSS_ATLAS_AUDIT_2026-11-25.md`), ADRs (`docs/adr/`), forensic/red-team reviews (`docs/reviews/`), run log (`docs/run-log.md`)
  - `ERRATA.md` — append-only post-release correction & withdrawal ledger
  - `ro-crate-metadata.json`, `croissant.json` — machine-readable FAIR RO-Crate 1.1 & MLCommons Croissant 1.0 dataset metadata
- **Status:** active

## Commands

Use `justfile` (or `Makefile` / `build.ps1`). Every command works from a clean clone:

- `just setup` — install pinned Python dependencies
- `just build` — regenerate `data/problems.json`, `RANKING.md`, `README.md` table, and all 106 dossier headers
- `just corpus` — rebuild deterministic `rag/corpus.jsonl` with globally unique chunk IDs
- `just check` — run `generate.py --check`, `validate.py`, `check_papers.py`, `proof_claim_sweep.py`, `check_retractions.py --check`, `check_readme_axioms.py`, `build_data_manifest.py --check`, `timestamp_manifest.py --check`
- `just test` — run full pytest + Hypothesis + regression + differential + metamorphic suite
- `just formal` — build Lean 4.35.0 core (`lean/`), run `VerifyAxioms.lean`, `lake check --paranoid`, `lake comparator --paranoid`, `scripts/test_lean_negative.py`
- `just lint` — report-only `ruff` and `mypy` checks
- `just mutate` — run targeted mutation test harness on core engine & validators
- `just site` — build static Atlas explorer (`_site/index.html`) and Lean Proof Blueprint (`_site/blueprint.html`)
- `just reproduce` — clean-clone end-to-end reproduction of build, corpus, formal verification, and tests
- `just audit` — score repo against Build Standard `v1.2.0`

## Hard Rules (Build Standard v1.2.0 R1–R8)

- **R1.** Nothing may gate, block, or slow a commit or push. No branch protection, no required status checks, no mandatory git hooks, no merge queues.
- **R2.** Commit and push straight to `main`. No pull requests and no feature branches.
- **R3.** CI is informational. A red CI run is a finding to fix on `main`, never a barrier.
- **R4.** Banned tools/files: no Dependabot/Renovate auto-PRs, no `.github/PULL_REQUEST_TEMPLATE.md`, no CodeRabbit, no Copilot review or `.github/copilot-instructions.md`, no `FUNDING` file.
- **R5.** One-person lean, not corporate.
- **R6.** Never fabricate. Every number, citation, DOI, arXiv ID, badge, and test result must come from a real run or primary-source resolution. Unverified means labeled unverified.
- **R7.** Classify every finding as strictly one of the 10 classes: `bug`, `error`, `issue`, `problem`, `concern`, `dilemma`, `conflict`, `gap`, `hole`, `blindspot`.
- **R8.** Precedence: owner's explicit instruction > hard rules R1–R7 > Build Standard items > ecosystem conventions.

## Epistemic & Verification Rules (Defensible Independent AI Research Playbook v1.3)

1. **Zero overclaiming:** Never call any open problem "solved" unless mathematical consensus with a verified resolving citation exists. Explicitly distinguish `kernel-checked`, `certificate-checked`, `primary-source-verified`, `editorial-synthesis`, and `open-conjecture` in `CLAIMS.md`.
2. **Formal hygiene:** `lean/FormalAtlas/`, `lean/Solution.lean`, `lean/NonVacuity.lean`, and `lean/Adversarial.lean` MUST contain zero `sorry`, zero `admit`, zero `native_decide`, zero custom `axiom` declarations, and only `[propext, Classical.choice, Quot.sound]`. Every `.lean` file begins with `module` (Palomar rule); `lean/Challenge.lean` stays strictly ≤ 1,000 lines and ≤ 100 KiB.
3. **Citation & retraction hygiene:** Never commit an unverified DOI or arXiv ID as `verified`. Run `python scripts/verify_citations.py` and `python scripts/check_retractions.py` before promoting flags.
4. **Identity hygiene:** Attribute to `Alexander S. Donahue` (ORCID `0009-0006-8168-9648`, independent researcher). Never write `0thernes LLC` until an entity is legally formed. Never commit local machine paths (`C:\Users\...`, `Z:\[Vibe...`).

## Known Traps

- **PowerShell literal brackets:** The local workspace path contains `[Vibe Coded (AI)]`; always pass `-LiteralPath` in PowerShell file cmdlets, and sync `[System.IO.Directory]::SetCurrentDirectory` if calling `.NET` file APIs after `Set-Location`.
- **RAG chunk IDs:** `rag/build_corpus.py` MUST use a monotonic per-`(slug, section)` counter across headings (never reset per heading), otherwise `rag/retriever.py` `dense_search` silently clobbers chunks.
- **Dossier README rank drift:** Always run `python scripts/generate.py` after editing `data/problems.yaml` so all 106 `problems/<slug>/README.md` rank headers stay synced with `metadata.json`.
- **Windows `lake check` sandbox:** `lake check` / `lake comparator` require POSIX `bwrap` for sandboxed mode; on Windows verify via direct kernel binaries (`leanchecker-paranoid`, `lean4lean --import`, `nanoda_bin`, `con-leche --verified`, `con-ron --verified`) and rely on Ubuntu CI for `bwrap`-sandboxed `lake check --paranoid` + `lake comparator --paranoid`.
- **Collatz pseudo-proof contamination:** Never commit unhedged victory-declarations; run `python scripts/proof_claim_sweep.py` after any change in `problems/`.
