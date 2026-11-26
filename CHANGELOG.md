# Changelog

All notable changes to The Unsolved Mathematics Atlas are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/); versions follow
[SemVer](https://semver.org/) on the *structure/schema* (content grows
continuously between structural versions).

## [0.6.0] — 2026-11-26

### Added (Cycle 5 Bleeding-Edge Milestone · Complete Lonely Runner $n\le 3$ · Euclid Even-Perfect · Exact Ramsey $R(3,4)=9$ · Dual Cryptographic Timestamps)
- **Expanded Zero-Mathlib Lean 4.35.0 Formal Core (`lean/`, `autoImplicit = false`, `69 → 81` Audited Declarations):** Added **8 major headline theorems**, **2 non-vacuity witnesses**, and **2 adversarial refutations** (**53 headline theorems + 12 witnesses + 16 adversarial refutations = 81 audited declarations**, 13 requiring zero axioms; zero `sorry`/`admit`/`native_decide`/custom `axiom`, axioms strictly within `{propext, Classical.choice, Quot.sound}`, all 81 accepted by all 6 independent kernels + `lake comparator`):
  - **Collatz Positive-Cycle Obstructions (+4 → 18 thms):** `thm_collatz_positive_cycle_has_odd_step`, `thm_collatz_positive_cycle_intercept_pos`, `thm_collatz_positive_cycle_subcritical` ($3^o < 2^d \land 2^d - 3^o \le c(w)$), and `thm_collatz_no_positive_cycle_d1` ($\forall x > 0,\ T(x) \ne x$) + adversarial refutation `adv_collatz_no_d1_positive_fixed_point`.
  - **COMPLETE Lonely Runner Conjecture for $n = 3$ (+1 → 8 thms):** `thm_lonely_runner_n3` proved constructively for **ALL** positive integer speed triples $(v_1, v_2, v_3) \in \mathbb{Z}_{>0}^3$ in pure zero-Mathlib Lean Core via 2-adic strong induction, quarter-shift counting, self-contained Bézout congruence, and rational nudging + concrete witness `witness_lonely_runner_n3_div4` for `(3, 5, 60)` at `t = 61/480`.
  - **Euclid's General Even Perfect Number Theorem (+1 → 4 thms):** `thm_euclid_even_perfect` ($\forall p \ge 2,\ \mathrm{IsPrime}(2^p - 1) \implies \mathrm{IsPerfect}(2^{p-1}(2^p - 1))$) proved directly against `divSum` + witness `witness_euclid_perfect_28`.
  - **Exact Ramsey Number $R(3,4) = 9$ (+2 → 4 thms):** `thm_ramsey_R34_upper` (complete Handshaking Lemma $9 \times 3 = 27$ odd contradiction on $K_9$ reusing `ramsey_R33_upper`) and `thm_ramsey_R34_lower` (explicit symmetric circulant $C_8(1,4,7)$ coloring on $K_8$) + adversarial refutation `adv_ramsey_R34_not_le_8`.
- **Live Negative Lean 4.35.0 Kernel & Axiom-Gate Rejection (`scripts/test_lean_negative.py`):** Proves empirically on every CI run (3/3 checks) that our active Lean 4.35.0 kernel rejects false Brocard (`6!+1 = 27^2`) and false Lonely Runner (`1/9 >= 1/3`) claims and that our axiom allowlist gate actively catches `sorryAx`.
- **Dual Third-Party Cryptographic Timestamps (`scripts/timestamp_manifest.py`):** Mints and verifies offline both a **DigiCert RFC 3161 TSA reply** (`data/MANIFEST.sha256.tsr`) and a **3-calendar Bitcoin OpenTimestamps proof** (`data/MANIFEST.sha256.ots`) bound to `data/MANIFEST.sha256`, attached to GitHub Releases & SLSA provenance attestations, and registered in `ro-crate-metadata.json`.
- **Mega-Atlas `v2.7.0` Cross-Atlas Sync & Upgraded White Paper (`paper/`):** Synchronized `docs/CROSS_ATLAS_AUDIT_2026-11-25.md` and white paper Table 6 to `unsolved-problems-mega-atlas v2.7.0` (`541f093`, 1,900 macro problems, 103 Lean invariants, 16 archive entries across 76 public repos, strictly `0/1,900` retired); recompiled `Donahue_2026_unsolved_mathematics_atlas.pdf` with 0 warnings / 0 overfull hboxes, byte-identical clean-room arXiv tarball, and visual PDF verification; expanded pytest verification ladder to **70 passing tests**.

### Fixed (Cycle 5 Audit)
- **C5-HOLE-01 (`lean/FormalAtlas/Defs.lean`, `lean/lakefile.toml`):** Lifted `isqrt` binary-search fuel from fixed `32` (which silently capped exactness at $2^{32}$) to `n` and proved `isqrt_spec` unconditionally for ALL $n \in \mathbb{N}$; enabled strict `autoImplicit = false` in `lean/lakefile.toml`.

## [0.5.0] — 2026-11-25

### Added (Cycle 4 Deep Refinement · 8-Domain Lean Core · FAIR Metadata · 10-Page Monograph)
- **Eight-Domain, 69-Declaration Zero-Mathlib Lean 4.35.0 Formal Core (`lean/`):** Doubled headline theorems from `22 → 45` (+ `10` non-vacuity witnesses + `14` adversarial false-variant refutations = **69 audited declarations**, zero `sorry`/`admit`/`native_decide`/custom `axiom`, axioms strictly within `{propext, Classical.choice, Quot.sound}`, 12 requiring zero axioms; all 69 pass 6 independent Lean 4.35.0 kernels + `lake comparator`):
  - **Collatz (+3 → 14 thms):** `thm_collatz_zero_fixed_point`, `thm_collatz_intercept_nonneg`, `thm_collatz_parity_word_length`.
  - **Erdős–Straus (+2 → 5 thms):** `thm_erdos_straus_symmetry` and `thm_erdos_straus_all_le_30`.
  - **Lonely Runner (+3 → 7 thms):** `thm_lonely_runner_period_shift`, `thm_lonely_runner_neg_time`, and `thm_lonely_runner_n3_nondiv4` (4 runners across all `7/8` mod-4 residue combinations with $4 \nmid v_i$).
  - **Brocard (+3 → 7 thms):** `thm_brocard_not_div3_ge_3`, `thm_brocard_mod10_ge_5`, and `thm_brocard_exhaustive_le_20` (through $20!+1 = 2{,}432{,}902{,}008{,}176{,}640{,}001$).
  - **NEW `FormalAtlas/Primes.lean` (4 thms):** Euclid's infinitude of primes, arbitrary prime gaps via $(k+1)!+2$, oddness of primes $\ge 3$, and twin-prime mod-6 rigidity ($p \equiv 5 \pmod 6$ for $p \ge 4$).
  - **NEW `FormalAtlas/Goldbach.lean` (3 thms):** Certified prime-pair decomposition for all even $4 \le n \le 100$, odd binary prime-sum obstruction ($p=2 \lor q=2$), and binary Goldbach failure at $11$.
  - **NEW `FormalAtlas/PerfectNumbers.lean` (3 thms):** Pure algebraic factorization proof of Mersenne prime exponent necessity ($2^a - 1 \mid 2^{ab} - 1$), first four even perfect numbers $\{6, 28, 496, 8128\}$, and exhaustive odd-perfect exclusion $n \le 100$.
  - **NEW `FormalAtlas/Ramsey.lean` (2 thms):** Exact first-principles determination of $R(3,3) = 6$ ($K_6$ pigeonhole upper bound + explicit symmetric $C_5$ coloring on $K_5$).
- **Expanded 10-Page Publication-Grade AMS-LaTeX White Paper (`paper/`):** Upgraded `Donahue_2026_unsolved_mathematics_atlas.tex` (+4 verified references in `references.bib`) with the Top-15 ranked CSS table, 15-field empirical citation-corruption table + TikZ horizontal bar chart, 8-domain 6-kernel TikZ architecture DAG, all 45 formal theorems, Definition & Kernel tables, synchronized `unsolved-problems-mega-atlas v2.4.0` Table 6, and 10-class hardening Table 7 — compiled with **0 warnings / 0 overfull hboxes**, byte-identical clean-room arXiv tarball compile, and full page-by-page visual PDF inspection.
- **FAIR Dataset Descriptors (`ro-crate-metadata.json`, `croissant.json`):** Added RO-Crate 1.1 and MLCommons Croissant 1.0 JSON-LD descriptors, tracked in `data/MANIFEST.sha256` (40 tracked files) and validated in pytest.
- **Live GitHub Pages Auto-Deploy (`.github/workflows/pages.yml`):** Enabled automatic deployment of `_site/index.html` and the upgraded 8-domain, 45-theorem `_site/blueprint.html` on every push to `main`.
- **Cross-Atlas Synchronization (`docs/CROSS_ATLAS_AUDIT_2026-11-25.md`):** Synchronized verbatim with `unsolved-problems-mega-atlas v2.4.0` (1,900 macro problems, 92 Lean invariants, `0/1,900` macro retirements across all 7 companion `0TH-2026-004..012` preprints).

### Fixed (Cycle 4 Hostile Sweep)
- **C4-BUG-01 (`problems/collatz-conjecture/experiments/odd_unit_lock_bridge_refinement.py`):** Fixed real Python `NameError` (`all_die` undefined in `classify_refinement()`, `interpretation` undefined in `run()`); added permanent `ruff --select E9,F63,F7,F82` guard in CI and pytest.
- **C4-ERR-01 (`README.md`, `SECURITY.md`, `docs/{operations,threat-model,glossary}.md`, `docs/adr/0002-multi-kernel-lean-core.md`):** Eliminated all 18 stale pre-migration `formal/` and `Build Standard v1.1.0` references; added permanent stale-reference regression test in pytest.

## [0.4.0] — 2026-11-25

### Added (Three-Cycle Hardening Audit · Build Standard v1.2.0 · Playbook v1.3)
- **Expanded Lean 4.35.0 Multi-Kernel Formal Core (`formal/` → `lean/`):** Migrated package cleanly to `lean/` (retaining redirect stub `formal/ROADMAP.md`) and expanded from 14 → **22 headline theorems** (+ **6 non-vacuity witnesses** + **8 explicit adversarial false-variant refutations** in `lean/Adversarial.lean` = **36 audited declarations**, zero `sorry`/`admit`/`native_decide`/custom `axiom`, axioms strictly within `{propext, Classical.choice, Quot.sound}`, 10 requiring zero axioms):
  - Collatz (+3): Böhm–Sontacchi exact cycle equation (`thm_collatz_cycle_equation`), parity-word cocycle (`thm_collatz_parity_word_append`), and negative integer cycles `-5` & `-17` of true $3n+1$ (`thm_collatz_negative_cycles`).
  - Erdős–Straus (+2): multiplicative closure / prime reduction (`thm_erdos_straus_multiplicative_closure`) and resolution of all 6 smallest Mordell exceptional squares `{121, 169, 289, 361, 529, 841}` (`thm_erdos_straus_mordell_exceptions_small`).
  - Lonely Runner (+1): exact rational speed-scaling invariance (`thm_lonely_runner_speed_scaling`).
  - Brocard (+2): mod-4 parity constraint $n \ge 4 \Rightarrow n!+1 \equiv 1 \pmod 4$ (`thm_brocard_mod4_ge_4`) and exhaustive classification extended to $n \le 15$ (`thm_brocard_exhaustive_le_15`, through $15!+1 = 1{,}307{,}674{,}368{,}001$).
- **Publication-Grade AMS-LaTeX White Paper & arXiv Bundle (`paper/`):** Authored and compiled `paper/Donahue_2026_unsolved_mathematics_atlas.tex` + 100% live-verified `paper/references.bib` via Tectonic 0.17.0 with **0 warnings / 0 overfull hboxes** (`paper/Donahue_2026_unsolved_mathematics_atlas.pdf`, 135.5 KiB) plus clean-room-compiled `paper/arxiv_submission.tar.gz`, bundled into GitHub Release & SLSA provenance attestations.
- **Interactive Lean Proof Blueprint (`_site/blueprint.html`):** Upgraded `scripts/build_site.py` to emit a standalone interactive Proof Blueprint with SVG dependency DAG and filterable 22-theorem explorer alongside `_site/index.html`.
- **Live Crossref + DataCite Retraction Audit (`scripts/check_retractions.py` → `data/retraction-audit.json`):** Audited all **220 primary-source-verified DOIs** (`0` retractions, `3` publisher errata/corrections transparently recorded, `0` network errors).
- **Verbatim `#print axioms` Parity & Palomar Gate (`scripts/check_readme_axioms.py`):** Pasted exact 36-declaration `#print axioms` output into `README.md` (`<!-- AXIOMS:START/END -->`) and wired CI drift & Palomar limit enforcement.
- **Cross-Atlas Resolution Audit (`docs/CROSS_ATLAS_AUDIT_2026-11-25.md`):** Primary-evidence reconciliation of `0thernes/unsolved-problems-mega-atlas` (1,900 problems) ↔ `unsolved-mathematics` (106 problems) ↔ all 11 sibling `0thernes` research repositories (honest verdict: `0/1,900` macro closures, 3 specific 2026 sub-conjecture preprints, 11 partial-progress frontiers).
- **Post-Release Governance & Licensing (`ERRATA.md`, SPDX headers):** Added `ERRATA.md` with append-only correction & withdrawal policy and `SPDX-License-Identifier: MIT` / `CC-BY-4.0` headers across core Python, Lean, and TeX sources.
- **Three-Cycle 10-Class Hardening Report (`docs/reviews/2026-11-25-three-cycle-hardening-audit.md`):** Upgraded to **Build Standard `v1.2.0`** (all 10 finding classes synced live on GitHub labels; `scripts/audit-checks.tsv`, `audit-repo.sh`, `Audit-Repo.ps1` upgraded; **100.0% core and 98.5%+ / 100.0% applicable structure score**).

### Fixed
- **C1-BUG-01 (`scripts/Audit-Repo.ps1`):** Added `[System.IO.Directory]::SetCurrentDirectory($Root)` after `Set-Location` so `.NET` `OpenRead` resolves paths accurately when invoked from another working directory.
- **C1-BUG-02 (`scripts/build_indexes.py`, `scripts/build_review_register.py`) & `C1-ISS-01`:** Enforced `newline="\n"` and normalized 89 tracked CRLF files to LF.
- **C1-CONC-01 (Machine-path privacy leak):** Sanitized local Windows paths (`C:\Users\...`, `Z:\[Vibe...`) across 9 historical July 2026 Collatz experiment files and added a permanent pytest negative guard.
- **C1-CONF-01 (`docs/faq.md`, `CLAIMS.md`, `AUTHORS.md`):** Reconciled historical June 14, 2026 self-review session label (`claude-opus-4-8`) consistently across all documentation.
- **C1-GAP-01 (`.gitignore`):** Added `.hypothesis/`, `lean/.lake/`, `lean/build/`, and `paper/build/`.
- **C1-ERR-01 (`README.md`, `llms-full.txt`, `CLAIMS.md`, `scripts/validate.py`):** Removed stale PR-template mention in `README.md`, corrected `HasErdosStraus` & `schema/problem.schema.json` references, and extended `VERSION` parity checking to `lean/lakefile.toml` and `lean/formalization.yaml`.

## [0.3.1] — 2026-11-23

### Fixed (Hostile Adversarial Second-Pass Audit — Pass 11)
- **Mathematical prose accuracy (`CLAIMS.md` C-03):** Corrected a prose sign inversion in C-03 so it faithfully matches `formal/FormalAtlas/Collatz.lean` (`thm_collatz_positivity_localization`: every **supercritical** word $3^{o(w)} > 2^{|w|}$ satisfies $c(w) \ge 3^{o(w)} - 2^{|w|}$, forcing its rational periodic fixed point $\rho_w \le -1$, while the sibling $3n-1$ barrier admits positive supercritical cycles at $5$ and $17$).
- **Meta-analyses consistency & residual errata (`meta-analyses/`):** Fixed residual inverted Goldbach exponent ($\delta \approx 0.7 \to E(X) \ll X^{0.72}$, $\delta \approx 0.28$) in `meta-analyses/goldbach-conjecture.md`; corrected Escauriaza–Seregin–Šverák year (`2001 → 2003`) in `meta-analyses/navier-stokes-smoothness.md`; resolved body-vs-frontmatter contradiction in `meta-analyses/unit-distance-problem.md` with the May 20, 2026 disproof (`arXiv:2605.20695`); added dated `2026-11-23` Frontier Addenda to 9 additional updated meta-analyses (`lonely-runner`, `hadwiger`, `riemann`, `grand-riemann`, `moving-sofa`, `sunflower`, `union-closed`, `crouzeix`, `sendov`).
- **Linux case-sensitivity parity (`A44`):** Renamed `docs/GLOSSARY.md` → `docs/glossary.md` via `git mv` and updated references in `README.md` and `SUPPORT.md` so Ubuntu CI (`audit-repo.sh`) matches Windows (`Audit-Repo.ps1`) at **98.5% (67/68) overall / 100.0% (28/28) core**.
- **Formal docs & verbatim axiom transparency (`formal/`):** Updated stale `formal/ROADMAP.md` (marking Phase 1 items 1–13 done and 6-kernel verified), cleaned scratch-pad comments in `formal/NonVacuity.lean`, and appended verbatim `#print axioms` output and 6/6 kernel verdicts to `formal/STATEMENT_FIDELITY.md`.
- **Honest outward disclosure (`SUBMISSIONS.md`, `meta-analyses/README.md`, `AUTHORS.md`):** Removed misleading `"put it through a four-model AI review panel"` line in the academic outreach cover-letter template and added ORCID `0009-0006-8168-9648`.
- **Static HTML Atlas builder (`scripts/build_site.py`, `.github/workflows/pages.yml`):** Replaced the placeholder Pages script with a zero-dependency searchable static HTML Atlas generator (`_site/index.html`) + regression test.
- **Additional verified DOIs & live GitHub labels:** Verified Gerver (1992, `10.1007/bf02414066`) and Kallus–Romik (2018, `10.1016/j.aim.2018.10.022`) against Crossref (`443 → 445` API-verified citations); synced all 6 Build Standard finding-class labels (`bug`, `error`, `issue`, `problem`, `dilemma`, `conflict`) + domain labels live on GitHub; added 5 Pass #2 regression tests (**45/45 pytest**, **6/6 mutation kill**).

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
