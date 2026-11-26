# Three-Cycle Deep-Dive Hardening Audit (`v0.4.0`, 2026-11-25)

> **Standards Applied:**
> - **Build Standard for LLMs `v1.2.0`** (`2026-11-24`, 90 items, Hard Rules R1–R8, **10 finding classes**)
> - **Defensible Independent AI Research Playbook `v1.3`** (`2026-11-24`, 43-item Gold Standard Release Checklist, 10-pass review protocol, Palomar rules, verbatim `#print axioms` parity, Crossref/DataCite retraction audit, adversarial false-variant tests, publication-grade AMS-LaTeX white paper + clean-room arXiv bundle)

---

## Table of Contents

1. [Repository Index & Census (All Tracked Directories & Extensions)](#1-repository-index--census)
2. [Methodology: Deductive, Inductive & Abductive Inference Protocol](#2-methodology-deductive-inductive--abductive-inference-protocol)
3. [Cycle 1 — Full-Tree Syntax, Hygiene, Token, Link, Privacy, Retraction & Build Standard v1.2.0 Audit](#3-cycle-1--structural-hygiene-privacy-retraction--build-standard-v120)
4. [Cycle 2 — Lean 4.35.0 Expansion (`formal/` → `lean/`), Adversarial Refutations, Blueprint & White Paper](#4-cycle-2--lean-4350-expansion-adversarial-tests-blueprint--ams-latex-white-paper)
5. [Cycle 3 — Hostile Full-Spectrum Red-Team Re-Audit & Release Verification](#5-cycle-3--hostile-red-team-re-audit--release-verification)
6. [Master 10-Class Finding Ledger (Complete 5W1H Traceability)](#6-master-10-class-finding-ledger)
7. [Cross-Atlas Resolution Verdict (`unsolved-problems-mega-atlas` 1,900 Problems)](#7-cross-atlas-resolution-verdict)

---

## 1. Repository Index & Census

Complete census executed at the start of Cycle 1 (`v0.3.1` baseline, `1,756` git-tracked files + `196` local untracked/ignored files; `v0.4.0` adds `lean/Adversarial.lean`, `lean/six_kernel_audit.txt`, `ERRATA.md`, `scripts/check_retractions.py`, `scripts/check_readme_axioms.py`, `data/retraction-audit.json`, `docs/CROSS_ATLAS_AUDIT_2026-11-25.md`, `paper/*`, and this report):

| Index Section | Directory / Scope | Tracked Files (Baseline) | Primary Checks Run |
|---|---|---:|---|
| **I. Root Governance** | `(root)` (`README.md`, `AGENTS.md`, `CLAIMS.md`, `LIMITATIONS.md`, `ERRATA.md`, `REPLICATION.md`, `VERSION`, `repo.yaml`, `CITATION.cff`, `pyproject.toml`, `justfile`, `Makefile`) | 39 | Version parity, Build Standard v1.2.0 audit, verbatim `#print axioms` parity, link & encoding checks |
| **II. Canonical Registry & Logs** | `data/` (`problems.yaml`, `problems.json`, `citation-verification-log.json`, `retraction-audit.json`, `dossier-status.json`, `MANIFEST.sha256`) | 5 | Draft 2020-12 JSON Schema, determinism, Crossref/DataCite retraction check, SHA-256 manifest |
| **III. Problem Dossiers** | `problems/<slug>/` (106 dossiers × 8 md + `metadata.json` + Collatz laboratory) | 1,518 | Rank header sync, paper flag check, proof-claim sweep, machine-path privacy scan, LF normalization, link check |
| **IV. Meta-Analyses** | `meta-analyses/` (106 AI-assisted surveys) | 107 | `check_papers.py` honesty banner & overclaim gate, frontmatter consistency audit |
| **V. Formal Core** | `lean/` (migrated from `formal/`; `FormalAtlas/*.lean`, `Challenge.lean`, `Solution.lean`, `NonVacuity.lean`, `Adversarial.lean`, `VerifyAxioms.lean`) | 17 → 19 | Palomar `module`/size limits, comment-stripped forbidden-token audit, `#print axioms`, 6-kernel independent replay, `lake comparator` |
| **VI. White Paper & Blueprint** | `paper/` (`*.tex`, `references.bib`, compiled PDF, `arxiv_submission.tar.gz`) + `scripts/build_site.py` (`_site/blueprint.html`) | New in `v0.4.0` | Tectonic 0-warning compile, clean-room arXiv tarball extraction + recompile, PDF magic/size check |
| **VII. Pipeline, RAG & Tests** | `scripts/`, `rag/`, `tests/`, `schema/`, `examples/` | 28 → 30 | Python AST, `ruff`, `mypy`, `pip-audit`, 55+ pytest/Hypothesis/oracle/metamorphic tests, 100% mutation kill |
| **VIII. Docs & CI** | `docs/`, `.github/`, `.cursor/` | 42 | Relative markdown link check across all 1,100+ `.md` files, case-sensitivity check, 10-class GitHub labels |

---

## 2. Methodology: Deductive, Inductive & Abductive Inference Protocol

- **Deductive verification:** Machine-checked proofs in Lean 4.35.0 (`lean/`, 22 theorems + 6 non-vacuity witnesses + 8 adversarial false-variant refutations = 36 declarations) replayed across 6 independent kernels (`lean`, `leanchecker-paranoid`, `lean4lean`, `nanoda_bin`, `con-leche`, `con-ron`), plus exact integer/rational Python differential oracles (`fractions.Fraction`, `math.factorial`).
- **Inductive verification:** Exhaustive empirical scanning across all `1,756+` tracked files (AST, JSON/YAML/TOML/SVG parsers, UTF-8/BOM/CRLF bytes, regex token sweeps, all markdown relative links), Hypothesis property-based fuzzing, targeted mutation testing (100% kill rate), live API resolution of 554 citation identifiers, and live retraction auditing of all 220 verified DOIs.
- **Abductive diagnosis:** Root-cause investigation of every defect observed — tracing CRLF drift back to missing `newline="\n"` in `scripts/build_indexes.py` & `scripts/build_review_register.py`; tracing `Audit-Repo.ps1` cross-directory false failures back to PowerShell `Set-Location` vs `.NET` `[System.Environment]::CurrentDirectory`; tracing Crossref `HTTP 404` on `10.48550/arXiv.2405.20552` back to DataCite vs Crossref DOI routing; and tracing a drafted white-paper CSS weight mismatch back to `scripts/generate.py` before publication.

---

## 3. Cycle 1 — Structural, Hygiene, Privacy, Retraction & Build Standard v1.2.0

Every tracked file was parsed and scanned programmatically (`cycle1_deep_scan.py` & `cycle1_paths_and_crlf.py`):
- **Syntax & links baseline:** `0` Python syntax errors, `0` JSON/JSONL errors, `0` YAML/CFF errors, `0` TOML errors, `0` SVG errors, `0` UTF-8 errors, `0` BOM files, `0` broken relative links across all 1,110 tracked `.md` files, `0` case-mismatch links.
- **Defects discovered and fixed in Cycle 1:**
  - **`C1-BUG-01` (`scripts/Audit-Repo.ps1`):** Added `[System.IO.Directory]::SetCurrentDirectory($Root)` after `Set-Location` so `.NET` `OpenRead` resolves paths cleanly from any caller directory.
  - **`C1-BUG-02` (`scripts/build_indexes.py`, `scripts/build_review_register.py`) & `C1-ISS-01`:** Enforced `newline="\n"` in both generators and normalized all **89** non-PS1 CRLF tracked files to LF (`\n`).
  - **`C1-CONC-01` (Machine-path privacy leak):** Found and sanitized **9** historical July 2026 Collatz experiment files leaking `C:\Users\Alexa\...` or `Z:\[Vibe Coded (AI)]\...` to clean repo-relative paths; added a permanent regression guard in `tests/test_verification_ladder.py`.
  - **`C1-CONF-01` (Session label conflict):** `docs/faq.md:20` and `CLAIMS.md:35` stated `claude-opus-4-6`, conflicting with `LIMITATIONS.md:26` and all 106 `meta-analyses/*.md` files (`claude-opus-4-8` historical 2026-06-14 non-canonical session label). Reconciled consistently across `docs/faq.md`, `CLAIMS.md`, `AUTHORS.md`, and `LIMITATIONS.md`, with a regression test.
  - **`C1-GAP-01` (`.gitignore`):** Added `.hypothesis/`, `lean/.lake/`, `lean/build/`, `paper/build/`.
  - **`C1-GAP-02` (Build Standard `v1.2.0`):** Upgraded `.github/labels.tsv` to all **10 finding classes** (`bug`, `error`, `issue`, `problem`, `concern`, `dilemma`, `conflict`, `gap`, `hole`, `blindspot`) and synced all 20 labels live via `gh label create --force`; upgraded `scripts/audit-checks.tsv`, `audit-repo.sh`, `Audit-Repo.ps1`, `repo.yaml`, `AGENTS.md`, `.cursor/rules/build-standard.mdc`.
  - **`C1-BLIND-01` (Retraction Watch / Crossref + DataCite blindspot):** Created `scripts/check_retractions.py` auditing all **220** primary-source-verified DOIs (`data/retraction-audit.json`): routed `10.48550/*` to DataCite and standard DOIs to Crossref → **220/220 audited, 0 retracted, 3 publisher errata/corrections transparently recorded, 0 network errors**.
  - **`C1-GAP-03` (Post-release errata & licensing):** Added `ERRATA.md` with append-only correction & withdrawal policy, added `SPDX-License-Identifier: MIT` to 17 Python files and Lean sources, and authored `docs/CROSS_ATLAS_AUDIT_2026-11-25.md`.

---

## 4. Cycle 2 — Lean 4.35.0 Expansion, Adversarial Tests, Blueprint & AMS-LaTeX White Paper

- **Migration (`formal/` → `lean/`, `C1-DIL-01`):** Clean `git mv formal lean` satisfying Build Standard `v1.2.0` `B22` (`dir:proofs|lean|coq|isabelle`), while leaving a redirect stub at `formal/ROADMAP.md` so legacy URLs never 404.
- **Expanded Lean 4.35.0 Formal Core (14 → 22 Headline Theorems + 6 Non-Vacuity Witnesses + 8 Adversarial False-Variant Refutations = 36 Audited Declarations):**
  - Collatz (+3): `thm_collatz_cycle_equation`, `thm_collatz_parity_word_append`, `thm_collatz_negative_cycles` (`-5` period 3, `-17` period 11 under true `T`).
  - Erdős–Straus (+2): `thm_erdos_straus_multiplicative_closure`, `thm_erdos_straus_mordell_exceptions_small` (`{121, 169, 289, 361, 529, 841}`).
  - Lonely Runner (+1): `thm_lonely_runner_speed_scaling`.
  - Brocard (+2): `thm_brocard_mod4_ge_4` and `thm_brocard_exhaustive_le_15` (through $15!+1 = 1{,}307{,}674{,}368{,}001$).
  - Adversarial suite (`lean/Adversarial.lean`, Playbook #12): 8 explicit proofs of `¬ P` refuting zero denominators, false triples, universal 1-step descent, sign-free cycle exclusion, false localization converse, strict Lonely Runner improvement, bad gap times, and near-square non-Brown factorials.
  - Verbatim `#print axioms` parity + Palomar gate (`scripts/check_readme_axioms.py`): exact 36-declaration output embedded in `README.md` (`<!-- AXIOMS:START/END -->`) and `lean/STATEMENT_FIDELITY.md`, checked automatically in CI.
- **Interactive Proof Blueprint (`_site/blueprint.html`):** Upgraded `scripts/build_site.py` to generate a zero-dependency interactive Proof Blueprint with SVG dependency DAG and filterable 22-theorem explorer.
- **Publication-Grade AMS-LaTeX White Paper (`paper/`):** Authored `paper/Donahue_2026_unsolved_mathematics_atlas.tex` + 100% live-verified `paper/references.bib` (including exact live-verified authors for `arXiv:2605.20695` and exact `scripts/generate.py` CSS weights caught and corrected during drafting). Compiled with Tectonic 0.17.0 with **`LOG_WARNING_COUNT=0` (0 warnings, 0 overfull hboxes)** to `paper/Donahue_2026_unsolved_mathematics_atlas.pdf` (`139,114` bytes) and clean-room-verified `paper/arxiv_submission.tar.gz` (extracted to empty temp dir → byte-identical `139,114`-byte PDF).

---

## 5. Cycle 3 — Hostile Red-Team Re-Audit & Release Verification

Every modified and newly created artifact underwent a third full hostile pass before tagging `v0.4.0`:
- **Self-caught pre-release errors (`C2-ERR-01`, `C2-ERR-02`, `C2-ERR-03`):**
  1. White paper §2.1 initially drafted incorrect CSS weights (`0.35/0.30/0.25/0.10`) instead of `scripts/generate.py`'s actual `0.40/0.30/0.20/0.10` — caught by cross-checking `data/problems.yaml` & `scripts/generate.py`, corrected, and recompiled cleanly.
  2. Initial `references.bib` placeholder author for `arXiv:2605.20695` caught against `data/citation-verification-log.json` and replaced with the exact verified 9-author list (`Alon, Bloom, Gowers, Litt, Sawin, Shankar, Tsimerman, Wang, Wood`).
  3. `CLAIMS.md` C-04 cited `ErdosStrausHolds` (actual Lean name `HasErdosStraus`), C-09 cited nonexistent `docs/indexes/by-severity.md` (actual `RANKING.md`), `llms-full.txt` cited `data/schema.json` (actual `schema/problem.schema.json`) and `552` (actual `554`), and `README.md:247` still mentioned `PR templates` — all corrected.
- **Automated Gate Sweep (`v0.4.0`):**
  - `generate.py --check`, `validate.py` (extended to `lean/lakefile.toml` & `lean/formalization.yaml` parity), `check_dossiers.py --strict`, `check_papers.py`, `proof_claim_sweep.py`, `check_retractions.py --check`, `check_readme_axioms.py`, `build_site.py`, `build_data_manifest.py --check`: **ALL PASS**.
  - `pytest -v tests/`: **55/55 PASS** (including 10 new Cycle 1–3 oracle, retraction, privacy, Palomar, blueprint, PDF, and label tests).
  - `tests/mutation_check.py`: **6/6 (100% mutant kill rate)**.
  - `ruff check scripts rag tests examples` & `mypy`: **0 errors**.
  - Six independent Lean 4.35.0 kernels: verified locally (`lean/six_kernel_audit.txt`) and in `bwrap`-sandboxed Ubuntu CI.
  - Build Standard `v1.2.0` (`Audit-Repo.ps1` / `audit-repo.sh`): **100.0% structure (68/68) / 100.0% completion (68/68) / 100.0% core (28/28)** (`B44` auto-matched dated ephemeral CI replication records; independent human mathematician review remains transparently disclosed as `0/106` in `repo.yaml`, `LIMITATIONS.md`, and `README.md`).

---

## 6. Master 10-Class Finding Ledger

| ID | Class | What | Where | Why (Root Cause) | Remediation & Verification |
|---|---|---|---|---|---|
| `C1-BUG-01` | `bug` | `.NET` CWD mismatch in `Audit-Repo.ps1` | `scripts/Audit-Repo.ps1:24` | PowerShell `Set-Location` does not update `[System.Environment]::CurrentDirectory` | Added `[System.IO.Directory]::SetCurrentDirectory($Root)`; verified cross-directory execution |
| `C1-BUG-02` | `bug` | Missing `newline="\n"` in index/register generators | `scripts/build_indexes.py`, `scripts/build_review_register.py` | Default Windows `write_text` wrote CRLF contrary to `.gitattributes` | Added `newline="\n"` and normalized 89 tracked files to LF |
| `C1-ERR-01` | `error` | Stale versions & misnamed refs (`ErdosStrausHolds`, `data/schema.json`, `552`, `PR templates`) | `CLAIMS.md`, `llms-full.txt`, `README.md`, `docs/configuration.md` | Incremental edits across `v0.3.0`/`v0.3.1` drifted | Fixed every reference; extended `validate.py` version parity to `lean/` |
| `C2-ERR-01` | `error` | Draft white-paper CSS weights mismatch & unverified `2605.20695` author | `paper/Donahue_2026_unsolved_mathematics_atlas.tex`, `paper/references.bib` | Drafted from memory before checking `scripts/generate.py` & `citation-verification-log.json` | Caught in Cycle 2/3 review; synced verbatim to `scripts/generate.py` & API log; recompiled 0 warnings |
| `C1-ISS-01` | `issue` | 89 tracked text files carried CRLF line endings | `docs/indexes/`, `problems/collatz-conjecture/experiments/` | Generated on Windows without `newline="\n"` | Normalized all 89 non-PS1 files to LF |
| `C1-PROB-01` | `problem` | Windows Lean 4.35.0 lacks POSIX `bwrap` for `lake check` | Local Windows dev environment | Upstream OS sandbox dependency | Verified via direct 6-kernel binary replay locally + full `bwrap` sandbox in Ubuntu CI |
| `C1-CONC-01` | `concern` | Local Windows filesystem path leak (`C:\Users\Alexa`, `Z:\[Vibe...`) | 9 historical July 2026 Collatz experiment files | Automated scripts recorded absolute paths | Sanitized all 9 files + permanent negative regression test in `tests/test_verification_ladder.py` |
| `C1-DIL-01` | `dilemma` | Migrating `formal/` → `lean/` (`B22`) vs breaking external links | `formal/` → `lean/` | Build Standard v1.2.0 `B22` checks `lean/`; prior releases linked `formal/` | Migrated via `git mv` AND left concise redirect stub `formal/ROADMAP.md` |
| `C1-CONF-01` | `conflict` | `docs/faq.md` & `CLAIMS.md` said `claude-opus-4-6` while `LIMITATIONS.md` & `meta-analyses/` said `claude-opus-4-8` | `docs/faq.md`, `CLAIMS.md`, `AUTHORS.md`, `LIMITATIONS.md` | Historical non-canonical 2026-06-14 session label paraphrased inconsistently | Reconciled all files to state `claude-opus-4-8` (explicitly labeled non-canonical historical session label) + regression test |
| `C1-GAP-01` | `gap` | Missing `.hypothesis/`, `lean/.lake/`, `paper/build/` in `.gitignore` | `.gitignore` | Added Hypothesis tests & new `lean/` / `paper/` dirs | Added all four entries cleanly |
| `C1-GAP-02` | `gap` | Build Standard `v1.2.0` upgrades (`blindspot` label, `v1.2.0` audit scripts, 10 finding classes) | `.github/labels.tsv`, `scripts/audit-*`, `repo.yaml`, `AGENTS.md` | Standard upgraded `v1.1.0 → v1.2.0` on 2026-11-24 | Upgraded all files & synced all 20 GitHub labels live |
| `C1-GAP-03` | `gap` | Playbook `v1.3` Gold Checklist artifacts (`ERRATA.md`, `Adversarial.lean`, README verbatim axioms, Blueprint HTML, compiled PDF + arXiv tarball, SPDX headers) | Root, `lean/`, `paper/`, `scripts/` | Playbook upgraded `v1.2 → v1.3` on 2026-11-24 | Delivered all artifacts and wired into CI + SLSA Release |
| `C1-HOLE-01` | `hole` | Missing automated guards for README axiom drift, Palomar limits, local machine-path leaks, and `lean/` version parity | `scripts/check_readme_axioms.py`, `scripts/validate.py`, `tests/` | Manual inspection alone can drift across commits | Implemented automated CI + pytest guards for every invariant |
| `C1-BLIND-01` | `blindspot` | Verified DOIs were never checked for subsequent retractions / publisher errata | `scripts/check_retractions.py`, `data/retraction-audit.json` | DOI resolution confirms existence, not retraction status | Audited all 220 verified DOIs via Crossref + DataCite (`0` retracted, `3` publisher errata logged, `0` errors) |

---

## 7. Cross-Atlas Resolution Verdict

Full primary-evidence reconciliation against `0thernes/unsolved-problems-mega-atlas` (`v2.4.0`, 1,900 problems) and all companion `0thernes` repositories is published in [`docs/CROSS_ATLAS_AUDIT_2026-11-25.md`](../CROSS_ATLAS_AUDIT_2026-11-25.md): **0 / 1,900** flagship Mega-Atlas macro problems are closed by `0thernes`; all 7 companion `0TH-2026-004..012` preprints are explicitly reconciled with parent status `OPEN` (or `N/A` for standalone `0TH-2026-006`).

---

## Cycle 4 — Post-`v0.4.0` Hostile Deep Refinement & `v0.5.0` Escalation

After `v0.4.0` (`f811c9b`) passed 100% green across all GitHub Actions jobs (CI `45724228403` + SLSA Release `45724232811`), an additional hostile AST/syntax/reference sweep across the entire repository uncovered two hidden defects and six opportunities to match and exceed sibling `unsolved-problems-mega-atlas v2.4.0`:

| ID | Class | Location | Defect / Opportunity | Resolution & Permanent Guard (`v0.5.0`) |
|---|---|---|---|---|
| **C4-BUG-01** | `bug` | `problems/collatz-conjecture/experiments/odd_unit_lock_bridge_refinement.py` | Real Python `NameError` (`all_die` undefined inside `classify_refinement()`, `interpretation` undefined inside `run()`), missed previously because `ruff` only linted `scripts/ rag/ tests/ examples/`. | Relocated `if all_die: interpretation = ...` cleanly into `run()`; added `ruff check --select E9,F63,F7,F82 problems/collatz-conjecture/experiments` to CI and pytest. |
| **C4-ERR-01** | `error` | `README.md`, `SECURITY.md`, `docs/{operations,threat-model,glossary}.md`, `docs/adr/0002-multi-kernel-lean-core.md` | 18 stale pre-migration `formal/` paths and `Build Standard v1.1.0` references survived `v0.4.0`. | Reconciled all 18 active references to `lean/` and `Build Standard v1.2.0`; added automated stale-reference regression check in `tests/test_verification_ladder.py`. |
| **C4-GAP-01** | `gap` | `lean/` | Formal core covered 4 domains / 22 theorems / 36 declarations. | Expanded zero-Mathlib Lean 4.35.0 core to **8 domains / 45 headline theorems / 10 witnesses / 14 adversarial refutations = 69 audited declarations** (adding `Primes.lean`, `Goldbach.lean`, `PerfectNumbers.lean`, `Ramsey.lean`, Lonely Runner $n=3$, Brocard $n \le 20$), all passing all 6 independent kernels. |
| **C4-GAP-02** | `gap` | `ro-crate-metadata.json`, `croissant.json` | Missing machine-readable FAIR dataset descriptors. | Authored RO-Crate 1.1 and MLCommons Croissant 1.0 JSON-LD descriptors, tracked in `data/MANIFEST.sha256` (40 files) and schema-checked in pytest. |
| **C4-GAP-03** | `gap` | `.github/workflows/pages.yml`, `scripts/build_site.py` | Pages workflow was `workflow_dispatch`-only and blueprint covered 4 domains. | Activated auto-deploy on push to `main` and upgraded `_site/blueprint.html` to all 8 domains / 45 theorems. |
| **C4-ERR-02** | `error` | `paper/Donahue_2026_unsolved_mathematics_atlas.tex` | Draft `\code{\nolinkurl{...}}` stripped spaces and italicized inside theorems; 4 tables overflowed `\textwidth`; zero-axiom count off by 1 (`13` vs `12`). | Fixed with `\PassOptionsToPackage{obeyspaces}{url}` + `\upshape`, `tabularx`, exact count `12`, 15-field corruption TikZ chart, and 8-domain bus DAG — compiled to a 10-page **0-warning / 0-overfull** PDF verified page-by-page visually. |
