# AGENTS.md

Canonical instructions for every coding agent working in this repository
(Antigravity, Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Grok Build, etc.).
`CLAUDE.md`, `GEMINI.md`, `.cursor/rules/build-standard.mdc`, and `llms.txt` all
point here. Edit this file, never the pointers.

## Project

- **Name:** The Unsolved Mathematics Atlas (`0thernes/unsolved-mathematics`)
- **Purpose:** Reproducible, ranked, research-grade dossier of 106 open mathematical problems across 38 fields, paired with a standalone multi-kernel Lean 4.35.0 formal verification core (`formal/`), primary-source citation auditing, and a deterministic BM25/dense RAG corpus.
- **Owner:** Alexander S. Donahue (`@0thernes`, ORCID `0009-0006-8168-9648`, independent researcher — do NOT use `0thernes LLC` until an entity is legally formed)
- **Manifest:** `repo.yaml` (Build Standard for LLMs v1.1.0)
- **Version:** `VERSION` (single source of truth; verified equal to `data/problems.yaml`, `CITATION.cff`, and `pyproject.toml` by `scripts/validate.py`)
- **Stack:** Python 3.11+ (`PyYAML`, `jsonschema`, `pytest`, `hypothesis`, `ruff`, `mypy`) + Lean 4.35.0 (`formal/`, zero Mathlib, 6-kernel `lake check --paranoid` + `lake comparator --paranoid`)
- **Layout:**
  - `data/` — canonical registry (`problems.yaml`), generated `problems.json`, `dossier-status.json`, `citation-verification-log.json`, `MANIFEST.sha256`
  - `problems/<slug>/` — 106 self-contained problem dossiers (8 markdown files + `metadata.json` + `rag/`)
  - `formal/` — standalone Lean 4.35.0 formal core (`FormalAtlas/`, `Challenge.lean`, `Solution.lean`, `NonVacuity.lean`, `VerifyAxioms.lean`, `comparator.json`, `formalization.yaml`, `STATEMENT_FIDELITY.md`)
  - `scripts/` — build engine (`generate.py`), integrity gate (`validate.py`), dossier/paper/pseudo-proof/citation checkers
  - `rag/` — deterministic chunker (`build_corpus.py`), BM25 & optional dense retriever (`retriever.py`)
  - `tests/` — unit, negative, regression, property-based (Hypothesis), golden/determinism, differential, metamorphic, and mutation tests
  - `meta-analyses/` — 106 AI-assisted surveys (all explicitly labeled AI-generated, not peer-reviewed)
  - `docs/` — architecture, methodology, indexes, ADRs (`docs/adr/`), forensic/red-team reviews (`docs/reviews/`), run log (`docs/run-log.md`)
- **Status:** active

## Commands

Use `justfile` (or `Makefile` / `build.ps1`). Every command works from a clean clone:

- `just setup` — install pinned Python dependencies
- `just build` — regenerate `data/problems.json`, `RANKING.md`, `README.md` table, and all 106 dossier headers
- `just corpus` — rebuild deterministic `rag/corpus.jsonl` with globally unique chunk IDs
- `just check` — run `generate.py --check`, `validate.py`, `check_papers.py`, `proof_claim_sweep.py`
- `just test` — run full pytest + Hypothesis + regression + differential + metamorphic suite
- `just formal` — build Lean 4.35.0 core, run `VerifyAxioms.lean`, `lake check --paranoid`, `lake comparator --paranoid`
- `just lint` — report-only `ruff` and `mypy` checks
- `just mutate` — run targeted mutation test harness on core engine & validators
- `just reproduce` — clean-clone end-to-end reproduction of build, corpus, formal verification, and tests
- `just audit` — score repo against Build Standard v1.1.0

## Hard Rules (Build Standard v1.1.0 R1–R8)

- **R1.** Nothing may gate, block, or slow a commit or push. No branch protection, no required status checks, no mandatory git hooks, no merge queues.
- **R2.** Commit and push straight to `main`. No pull requests and no feature branches.
- **R3.** CI is informational. A red CI run is a finding to fix on `main`, never a barrier.
- **R4.** Banned tools/files: no Dependabot/Renovate auto-PRs, no `.github/PULL_REQUEST_TEMPLATE.md`, no CodeRabbit, no Copilot review or `.github/copilot-instructions.md`, no `FUNDING` file.
- **R5.** One-person lean, not corporate.
- **R6.** Never fabricate. Every number, citation, DOI, arXiv ID, badge, and test result must come from a real run or primary-source resolution. Unverified means labeled unverified.
- **R7.** Classify every finding as strictly one of: `bug`, `error`, `issue`, `problem`, `dilemma`, `conflict`.
- **R8.** Precedence: owner's explicit instruction > hard rules R1–R7 > Build Standard items > ecosystem conventions.

## Epistemic & Verification Rules (Defensible Independent AI Research Standard)

1. **Zero overclaiming:** Never call any open problem "solved" unless mathematical consensus with a verified resolving citation exists. Explicitly distinguish `kernel-checked`, `certificate-checked`, `literature-verified`, `editorial-estimate`, and `open-conjecture` in `CLAIMS.md`.
2. **Formal hygiene:** `formal/FormalAtlas/`, `formal/Solution.lean`, and `formal/NonVacuity.lean` MUST contain zero `sorry`, zero `admit`, zero `native_decide`, zero custom `axiom` declarations, and only `[propext, Classical.choice, Quot.sound]`. Every Lean file begins with `module` (Palomar rule).
3. **Citation hygiene:** Never commit an unverified DOI or arXiv ID as `verified`. Run `python scripts/verify_citations.py` before promoting flags.
4. **Identity hygiene:** Attribute to `Alexander S. Donahue` (ORCID `0009-0006-8168-9648`, independent researcher). Never write `0thernes LLC` until an entity is legally formed.

## Known Traps

- **PowerShell literal brackets:** The local workspace path contains `[Vibe Coded (AI)]`; always pass `-LiteralPath` in PowerShell file cmdlets.
- **RAG chunk IDs:** `rag/build_corpus.py` MUST use a monotonic per-`(slug, section)` counter across headings (never reset per heading), otherwise `rag/retriever.py` `dense_search` silently clobbers chunks.
- **Dossier README rank drift:** Always run `python scripts/generate.py` after editing `data/problems.yaml` so all 106 `problems/<slug>/README.md` rank headers stay synced with `metadata.json`.
- **Windows `lake check` sandbox:** `lake check` / `lake comparator` require POSIX `bwrap` for sandboxed mode; on Windows use `--from-export ... --inadvisably-no-sandbox` (or run full `bwrap` sandbox in Ubuntu CI).
- **Collatz pseudo-proof contamination:** Never commit unhedged victory-declarations; run `python scripts/proof_claim_sweep.py` after any change in `problems/`.
