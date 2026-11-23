# Changelog

All notable changes to The Unsolved Mathematics Atlas are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/); versions follow
[SemVer](https://semver.org/) on the *structure/schema* (content grows
continuously between structural versions).

## [0.3.0] — 2026-11-23

### Added
- **Standalone Lean 4.35.0 Multi-Kernel Formal Core (`formal/`):** Zero-Mathlib formalization proving **14 headline theorems** across 4 open problems (Collatz 8 theorems including Terras parity-word bijection, unconditional Positivity Localization $\rho_w \le -1$, and the $\varepsilon$-invariance $3n-1$ barrier; Erdős–Straus Mordell mod-840 covering 834/840 classes; Lonely Runner all-$n$ sharpness + $n \in \{1, 2\}$; Brocard Brown solutions + exhaustive $n \le 12$), plus `Challenge.lean` + `comparator.json`, `NonVacuity.lean` (6 computable witnesses), `VerifyAxioms.lean` (strictly $\subseteq \{\text{propext}, \text{Classical.choice}, \text{Quot.sound}\}$), and `STATEMENT_FIDELITY.md`. Verified across Lean 4.35.0's bundled independent kernels (`lean`, `leanchecker-paranoid`, `nanoda_bin`, `con-leche`, `con-ron`, plus full `bwrap`-sandboxed 6-kernel `lake check --paranoid` and `lake comparator --paranoid` in Ubuntu CI).
- **Automated Primary-Source Citation Verification (`scripts/verify_citations.py` + `data/citation-verification-log.json`):** Queried all 552 identifier-bearing rows across 106 `papers.md` dossiers against live `export.arxiv.org` and `api.crossref.org` APIs (`network_error: 0`): promoted **443 live-verified rows** to `verified`, and caught & stripped **109 invalid/hallucinated/404 identifiers** (downgraded honestly to `—` / `needs-verification`).
- **Build Standard v1.1.0 & Playbook Governance Suite:** `VERSION`, `CLAIMS.md` (falsification matrix), `LIMITATIONS.md`, `REPLICATION.md`, `ROADMAP.md`, `SECURITY.md`, `SUPPORT.md`, `UPGRADING.md`, `THIRD_PARTY_NOTICES.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursor/rules/build-standard.mdc`, `llms.txt`, `llms-full.txt`, `.editorconfig`, `.env.example`, `.github/labels.tsv`, `pyproject.toml`, `requirements-lock.txt`, `justfile`, `repo.yaml`, `docs/adr/0001–0003`, `docs/configuration.md`, `docs/operations.md`, `docs/threat-model.md`, `docs/faq.md`, `docs/glossary.md`, `docs/run-log.md`, `docs/media/social-preview.svg`, `examples/query_atlas.py`, `scripts/build_data_manifest.py` + `data/MANIFEST.sha256`, and `docs/reviews/2026-11-23-forensic-philosophical-audit.md` (6-class taxonomy + 5W1H + Deductive/Inductive/Abductive & Philosophy of Mathematics analysis + 10-pass review log).
- **Verification Test Ladder (`tests/`):** Added `tests/test_verification_ladder.py` (negative tests, bug-regression tests, golden determinism, schema contracts, Python differential reference oracles for Lean theorems, metamorphic tests), `tests/test_properties.py` (Hypothesis property-based testing), and `tests/mutation_check.py` (100% mutant kill rate across targeted core invariants).
- **Cross-Platform CI & SLSA Provenance Releases:** Upgraded `.github/workflows/ci.yml` (`ubuntu-latest` + `windows-latest`, pytest/Hypothesis/mutation/ruff/mypy/security-hygiene + sandboxed 6-kernel Lean 4.35.0 verification) and added `.github/workflows/release.yml` (`SHA256SUMS` + `actions/attest-build-provenance@v2`).

### Changed
- **Consolidated `codex/collatz-catalog-qa-routing` (PR #2, 30 commits) + July 2–5 tree straight onto `main`** and removed banned `.github/PULL_REQUEST_TEMPLATE.md` (Build Standard R2/R4).
- **2024–2026 Mathematical Frontier Updates (live-verified via arXiv API):** Updated 11 problem dossiers including Erdős Unit Distance (`recently-resolved`, May 20, 2026 disproof `arXiv:2605.20695`), 3D Kakeya (Wang–Zahl `2502.17655`, Guth–Wang–Zahl `2601.14411`, Hong Wang Fields Medal July 2026), Riemann & Grand Riemann (Guth–Maynard `2405.20552` + conservative Nov 2026 Lean frontier watch), Navier–Stokes (Nov 2026 frontier watch), Lonely Runner (`n = 8..13`), Moving Sofa (Baek & Trela), Linear Hadwiger, Sunflower, Union-Closed Sets, Crouzeix, and Sendov.
- **Canonical Identity & Honest Provenance:** Added verified ORCID `0009-0006-8168-9648` and CRediT roles to `CITATION.cff` and `.zenodo.json`; replaced misleading "four-model review panel" wording in `README.md` with transparent `1/4` Claude self-review / `0/106` human peer-review disclosure.
- **Lossless Storage Hygiene:** Losslessly gzip-compressed the 38.6 MB `odd_unit_lock_transition_microscope_d13_R12_N50000_20260705.json` file to 0.64 MB (`.json.gz`), removing the sole file > 5 MB in the working tree.

### Fixed
- **BUG-01:** Fixed silent RAG chunk-ID collisions in `rag/build_corpus.py` (all 3,763 chunks now have globally unique `(slug, section, chunk_idx)` IDs).
- **BUG-02 & BUG-03:** Fixed `scripts/generate.py` to refresh all 106 per-dossier `README.md` rank headers (81 were stale), added deterministic `(-css, slug)` tie-breaking, and pinned `CURRENT_YEAR = 2026`.
- **BUG-04 & BUG-05:** Made `jsonschema` mandatory in `scripts/validate.py` & `scripts/check_papers.py`, added real freshness / `VERSION` parity / relative-link / chunk-uniqueness checks, fixed multi-table `count_table_rows` in `scripts/check_dossiers.py`, and removed environment-dependent `tiktoken` branching in `rag/build_corpus.py`.
- **BUG-06:** Replaced Windows-only `2>NUL` in `Makefile` with POSIX `2>/dev/null` and wired full `pytest` coverage.
- **BUG-07:** Tightened `scripts/proof_claim_sweep.py` to eliminate single-word hedge bypasses (`candidate`/`heuristic`), catching and adding an explicit **WITHDRAWN / REFUTED** retraction banner to `problems/collatz-conjecture/experiments/PROOF-SKETCH-AFFINE-COCYCLE-RIGIDITY-2026.md`.
- **ERR-02 & ERR-03:** Fixed inverted Goldbach exceptional-set exponent ($E(X) \ll X^{0.72}$) and corrected Navier–Stokes Escauriaza–Seregin–Šverák publication year from `2001` to `2003`.

## [0.2.0] — 2026-06-14
### Added
- **Authorship & accreditation to Alexander Donahue** (human-in-the-loop):
  copyright holder on CC BY 4.0 content + MIT code, `CITATION.cff`, `AUTHORS.md`,
  and README credit.
- **AI-Reviewed Meta-Analysis framework**: a four-model AI review panel (Grok,
  Gemini, GPT, Claude) with an honest process spec
  ([docs/review/AI-META-REVIEW.md](docs/review/AI-META-REVIEW.md)), review record
  schema, panel prompt/record template, and an auto-generated review register.
- **Academic-review option**: how-to and responsible-outreach protocol
  ([docs/review/ACADEMIC-REVIEW.md](docs/review/ACADEMIC-REVIEW.md)), an
  academic-review issue template, and an outreach tracker (`SUBMISSIONS.md`).
- **`meta-analyses/`**: AI-assisted meta-analysis write-ups (one per problem),
  each accredited to the author, AI-reviewed in-house by Claude with pending
  slots for GPT/Gemini/Grok, and clearly labeled AI-generated / not peer-reviewed.
- **Integrity gate** `scripts/check_papers.py` (CI-enforced): rejects any
  meta-analysis lacking the honesty banner, accreditation, or review block, or
  containing a "solved" overclaim. Repository made **public**.

## [Unreleased]
### Added
- **Expanded to 106 problems** (wave 4 — crossed 100): added 21 spanning harmonic
  analysis (restriction, Bochner–Riesz), ergodic theory (Furstenberg ×2×3),
  dynamics (Palis, Arnold diffusion), model theory (Cherlin–Zilber),
  combinatorics (Ryser), discrete geometry (Hadwiger covering, Kelvin),
  probability/statistical mechanics (self-avoiding walk, KPZ universality),
  number theory (Carmichael totient, Giuga, Pillai), complex analysis (Brennan),
  algebra (Dixmier), Diophantine geometry (Zilber–Pink), anabelian geometry
  (Grothendieck's section conjecture), Galois representations (Fontaine–Mazur),
  Iwasawa theory (Greenberg), and chromatic homotopy (the telescope conjecture,
  disproved 2023) — each fully authored. RAG corpus now **3,754 chunks
  (~765k tokens)**; **~2,650 flagged citations** (968 high-confidence,
  1,406 needs-verification, 271 ai-suggested, 0 yet human-verified).
- **Expanded to 85 problems** (wave 3): added 25 spanning analytic number theory
  (Grand RH, Elliott–Halberstam, Chowla, Sarnak–Möbius), Diophantine geometry
  (Vojta, Bombieri–Lang, Hall), complex dynamics (MLC), dynamical systems
  (Birkhoff billiards), symplectic/contact (Weinstein), 4-manifolds (smooth
  Poincaré), geometric topology (Borel, Zeeman, Eilenberg–Ganea), knot theory
  (volume, slice–ribbon), graph theory (Erdős–Hajnal, Seymour 2nd neighborhood,
  total coloring), order theory (1/3–2/3), algebraic geometry (Zariski
  cancellation), ring theory (Köthe), model theory (Vaught), modular forms
  (Lehmer τ), and aliquot sequences (Catalan–Dickson) — each fully authored.
  RAG corpus now **3,027 chunks (~617k tokens)**; **~2,120 flagged citations**
  (776 high-confidence, 1,113 needs-verification, 231 ai-suggested, 0 yet human-verified).
- **Expanded to 60 problems** (wave 2): added 20 spanning set theory (Continuum
  Hypothesis, with a new `independent` status), arithmetic geometry (Tate),
  topology / K-theory (Novikov, Baum–Connes, Whitehead, Hilbert–Smith),
  complexity (Unique Games), graph theory (reconstruction, cycle double cover,
  graceful trees, Caccetta–Häggkvist), geometry (moving sofa, unit distance,
  Falconer), algebra (inverse Galois), and number theory (Schinzel H, Artin
  primitive root, Lehmer–Mahler, four exponentials) — each fully authored.
  RAG corpus now **2,106 chunks (~434k tokens)**; **~1,500 flagged citations**
  (525 high-confidence, 760 needs-verification, 210 ai-suggested, 0 yet human-verified).
- **Full dossiers authored for all 40 problems** (EPIC-1): every problem now has
  history, originator biography, attack strategies, notable attempts, **25 key
  papers** and **10 key mathematicians** (each citation verification-flagged),
  and a live-frontier status with cross-links.
- Cross-cutting indexes (`docs/indexes/`): by field, by status, by era,
  originators index, and a **verification dashboard** (1,000 citations:
  357 high-confidence, 501 needs-verification, 142 ai-suggested, 0 yet human-verified).
- Glossary of recurring concepts (`docs/GLOSSARY.md`).
- RAG corpus expanded to **1,403 chunks (~289k tokens)** of real content.
- `scripts/build_indexes.py` and `scripts/check_dossiers.py`; `Makefile` + `build.ps1`.
- Initial repository architecture and single-source-of-truth registry
  (`data/problems.yaml`) with 40 ranked open problems.
- Deterministic ranking engine (`scripts/generate.py`) computing the Composite
  Severity Score (CSS) and scaffolding per-problem dossiers.
- JSON Schemas for problems, papers, and people.
- RAG pipeline: heading/token-aware chunker, zero-dependency BM25 retriever,
  optional sentence-transformers dense index.
- Documentation suite: README, ARCHITECTURE, PHILOSOPHY, ranking methodology,
  sourcing standard, ER model, data model, and the research Kanban board.
- CI/CD workflows (validation, ranking freshness, corpus build) and
  issue/PR templates.

### Pending
- Verification pass on all paper/person citations (EPIC-2) — promote
  `needs-verification` / `ai-suggested` flags to `verified` against primary sources.
- Dense index productionization + optional MCP retrieval server (EPIC-3).
- Breadth expansion to 100+ problems (EPIC-4).

## [0.1.0] — 2026-06-14
- Project genesis. Scaffold, registry, ranking engine, RAG layer, and docs.
