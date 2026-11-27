# Master Hardening Index & Table of Contents (`HARDENING_INDEX.md`)

> **Standards Applied:** **Build Standard for LLMs `v1.2.0`** (90 checks, Hard Rules R1–R8, 10 finding classes) & **Defensible Independent AI Research Playbook `v1.3`** (43-item Gold Release Checklist, Palomar Comparator isolation, 6-kernel Lean 4.35.0 verification, live negative kernel rejection, dual third-party cryptographic timestamps).
>
> **Current Release:** `v0.8.2` (`2026-11-27`) · **Scope:** All `1,997` tracked files across **10 subsystems**.

---

## Table of Contents (Repository Subsystems Audited Every Cycle)

| # | Subsystem | Canonical Paths | Primary Automated & Forensic Gates |
|---:|---|---|---|
| **I** | **Governance, Identity & Standards** | `README.md`, `VERSION`, `repo.yaml`, `CITATION.cff`, `pyproject.toml`, `LICENSE`, `LICENSE-CODE`, `THIRD_PARTY_NOTICES.md`, `CLAIMS.md`, `LIMITATIONS.md`, `ERRATA.md`, `CHANGELOG.md`, `AGENTS.md`, `REPLICATION.md`, `ROADMAP.md`, `AUTHORS.md`, `SUBMISSIONS.md`, `PHILOSOPHY.md`, `ARCHITECTURE.md`, `llms.txt`, `llms-full.txt`, `ro-crate-metadata.json`, `croissant.json`, `.zenodo.json` | `validate.py` (9-file version parity), `repo-standard.schema.json`, `Audit-Repo.ps1` / `audit-repo.sh`, `check_readme_axioms.py`, `test_verification_ladder.py` |
| **II** | **Canonical Problem Registry & Integrity Logs** | `data/problems.yaml`, `data/problems.json`, `data/citation-verification-log.json`, `data/retraction-audit.json`, `data/dossier-status.json`, `data/MANIFEST.sha256`, `data/MANIFEST.sha256.{tsr,ots}`, `schema/*.json` | JSON Schema Draft 2020-12 (`validate.py`), `generate.py --check`, live Crossref/arXiv/DataCite API logs, `build_data_manifest.py --check`, `timestamp_manifest.py --check` |
| **III** | **120 Seven-Section Research Dossiers** | `problems/<slug>/{README,history,originator,approaches,attempts,papers,mathematicians,status}.md`, `metadata.json`, `problems/collatz-conjecture/experiments/` | `check_dossiers.py --strict` (7-col `papers.md`, 5-col `mathematicians.md`, 1-to-1 verified bijection with `citation-verification-log.json`, zero duplicate/bare IDs, balanced `$`), `proof_claim_sweep.py`, `ruff E9/F63/F7/F82/B023`, zero local machine paths |
| **IV** | **120 AI-Assisted Meta-Analyses** | `meta-analyses/<slug>.md`, `meta-analyses/README.md` | `check_papers.py` (frontmatter schema, honesty banner, author credit, AI Review Panel, zero overclaim, balanced `$`), `validate.py` relative links |
| **V** | **External Daily Research-Program Mirror** | `data/external/lefttosolve/{snapshot.json,history.jsonl,items/*.jsonl}`, `data/external/crosswalk-overrides.yaml`, `docs/external/{PROGRAMS,CROSSWALK}.md`, `scripts/sync_external_programs.py`, `scripts/search_all_problems.py` | `sync_external_programs.py --check` (25 programs / 59,396 items, `< 4 MiB` A24 shards, zero excerpts, `solved_by_kind`, SHA-256 content digest, CC BY-SA carve-out), `tests/test_external_programs.py` |
| **VI** | **Standalone 8-Domain, 6-Kernel Lean 4.35.0 Formal Core** | `lean/lakefile.toml`, `lean/lake-manifest.json`, `lean/formalization.yaml`, `lean/comparator.json`, `lean/Challenge.lean`, `lean/Solution.lean`, `lean/NonVacuity.lean`, `lean/Adversarial.lean`, `lean/VerifyAxioms.lean`, `lean/FormalAtlas/*.lean`, `lean/STATEMENT_FIDELITY.md`, `lean/six_kernel_audit.txt`, `lean/ROADMAP.md` | `lake build`, `lake env lean VerifyAxioms.lean` (102 decls, standard axioms only), `scripts/check_readme_axioms.py` (Playbook v1.3 forbidden tokens, Palomar caps, symlinks, verbatim axiom parity), `scripts/test_lean_negative.py` (3/3 live rejections), 6-kernel `bwrap` `lake check --paranoid` + `lake comparator --paranoid` |
| **VII** | **Deterministic RAG Corpus & Retrieval** | `rag/build_corpus.py`, `rag/retriever.py`, `rag/embed.py`, `rag/corpus.jsonl` | Zero-drift CI rebuild (`git diff --exit-code`), global unique chunk IDs, BM25 permutation invariance (`test_verification_ladder.py`) |
| **VIII** | **AMS-LaTeX White Paper & arXiv Bundle** | `paper/Donahue_2026_unsolved_mathematics_atlas.{tex,pdf}`, `paper/references.bib`, `paper/arxiv_submission.tar.gz` | Tectonic 0-warning / 0-Overfull / 0-Underfull compile, clean-room tarball extraction + byte-identical PDF verification, 1-to-1 Claims Ledger & bibliography parity |
| **IX** | **Automation Scripts, Static Site & Verification Ladder** | `scripts/*.py`, `scripts/Audit-Repo.ps1`, `scripts/audit-repo.sh`, `examples/query_atlas.py`, `tests/*.py`, `tests/mutation_check.py`, `justfile`, `Makefile`, `build.ps1` | `pytest -v tests/` (95 tests), `tests/mutation_check.py` (10/10 = 100% kill), `ruff check`, `mypy --explicit-package-bases --check-untyped-defs` (20/20 modules = 0 errors), `_site/{index,blueprint,programs}.html` |
| **X** | **Documentation, Indexes, Cross-Atlas & GitHub Actions CI** | `docs/**/*.md`, `.github/workflows/{ci,validate-registry,pages,release,sync-external}.yml`, `.github/labels.tsv`, `.github/ISSUE_TEMPLATE/finding.yml` | Relative link audit across all 1,269+ `.md` files, LF-only check, `< 5 MB` A24 file cap, zero `github-actions[bot]` committers, Node 24 actions, SLSA provenance, Cross-Atlas parity against `unsolved-problems-mega-atlas` (`v2.10.0`, 2,000 problems) & `0thernes-research-archive` (`0TH-BUILD-004`) |

---

## Ten-Class Finding Taxonomy (Build Standard `v1.2.0` R7)

Every hardening cycle classifies discoveries strictly into the ten classes below — **never collapsing distinct failure modes**:

1. **`bug`** — Runtime, parser, Markdown-rendering, boundary-condition, or logic defect in code/content (e.g., unescaped `|` breaking Markdown tables, `limit <= 0` returning a hit, `B023` closure capture, odd `$` math delimiters).
2. **`error`** — Factual, mathematical, bibliographic, schema, typing, or numerical inaccuracy (e.g., duplicate/hallucinated citation IDs, `repo.yaml` invalid enum `lean4`, `mypy` type errors, statement-audit wording drift, stale counts).
3. **`issue`** — Hygiene, formatting, line-ending, or deprecation defect (e.g., CRLF files, Node 20 Actions deprecation, backticked `\$` rendering literal backslashes).
4. **`problem`** — Structural, architectural, or environmental constraint requiring explicit engineering workarounds (e.g., POSIX `bwrap` unavailable natively on Windows; Collatz experimental data footprint asymmetry).
5. **`concern`** — Security, privacy, provenance, or epistemic-risk exposure (e.g., local Windows path leaks, unreviewed AI prose hygiene).
6. **`dilemma`** — Trade-off between two competing valid engineering goals requiring an explicit recorded design decision (e.g., migrating `formal/` → `lean/` while keeping a redirect stub; preserving historical bot commit in git history while transparently disclosing `A23` at `98.5%`).
7. **`conflict`** — Direct contradiction between two active files, workflows, or policies (e.g., `sync-external.yml` using `github-actions[bot]` while Build Standard `A23` requires verified human author identity; session label mismatch).
8. **`gap`** — Missing capability, documentation artifact, regression test, or mutant required by the standards (e.g., missing `HARDENING_INDEX.md`, missing M7–M10 mutants covering dossier/paper/search invariants).
9. **`hole`** — Weak or incomplete validation gate that allowed an existing bug/error to slip past CI (e.g., `check_dossiers.py --strict` not enforcing column counts or 1-to-1 citation-log bijection; `validate.py` not scanning `meta-analyses/` or `lean/` links; `check_papers.py` not checking math balance).
10. **`blindspot`** — Entire verification class previously unmonitored (e.g., retraction status of verified DOIs; live negative Lean kernel rejection; PrimeGrid exact open-candidate count drift in `riesel-problem/status.md`).

---

## Hardening Cycle History & Detailed Forensic Ledgers

| Release | Date | Cycles Run | Full Ledger & Audit Record | Key Verified Metrics |
|---|---|---|---|---|
| `v0.4.0` | `2026-11-25` | Cycles 1–3 | [`docs/reviews/2026-11-25-three-cycle-hardening-audit.md`](docs/reviews/2026-11-25-three-cycle-hardening-audit.md#3-cycle-1--structural-hygiene-privacy-retraction--build-standard-v120) | 106 problems, 22 Lean thms / 36 decls (4 domains), 220 DOIs retraction-audited, 55 pytest, 6/6 mutants, first AMS-LaTeX PDF |
| `v0.5.0` | `2026-11-25` | Cycle 4 | [`docs/reviews/2026-11-25-three-cycle-hardening-audit.md`](docs/reviews/2026-11-25-three-cycle-hardening-audit.md#cycle-4--post-v040-hostile-deep-refinement--v050-escalation) | 8-domain Lean core (45 thms / 69 decls), RO-Crate 1.1 & Croissant 1.0, GitHub Pages auto-deploy |
| `v0.6.0` | `2026-11-26` | Cycle 5 | [`docs/reviews/2026-11-25-three-cycle-hardening-audit.md`](docs/reviews/2026-11-25-three-cycle-hardening-audit.md#cycle-5--bleeding-edge-milestone-v060-2026-11-26) | Complete Lonely Runner $n\le 3$, Euclid even-perfect, $R(3,4)=9$ (53 thms / 81 decls), `autoImplicit=false`, live negative kernel tests, RFC 3161 + Bitcoin OTS |
| `v0.7.0` | `2026-11-26` | `/goal` Cycles 1–3 | [`docs/reviews/2026-11-25-three-cycle-hardening-audit.md`](docs/reviews/2026-11-25-three-cycle-hardening-audit.md#9-goal-three-cycle-deep-forensic-hardening--landmark-formal-core-expansion-v070-2026-11-26) | Complete Euclid–Euler + `divSum_eq_divSumLin` + Euler $2p\mid(q-1)$, Collatz Fine–Wilf / $d\le 7$ / 1-/2-odd exclusion / catalytic cylinder (66 thms / 102 decls), all 6 statement-audit items resolved, Node 24 CI |
| `v0.8.0`–`v0.8.1` | `2026-11-27` | Expansion + Drift Fix | [`CHANGELOG.md`](CHANGELOG.md#080--2026-11-27) | 120 curated dossiers, daily 25-program / 59,396-item sharded Left to Solve mirror, unified offline search CLI, zero-drift corpus parity |
| **`v0.8.2`** | **`2026-11-27`** | **`/goal` Cycles 1–3 (10-Subsystem Audit)** | [`docs/reviews/2026-11-25-three-cycle-hardening-audit.md`](docs/reviews/2026-11-25-three-cycle-hardening-audit.md#10-v082-three-cycle-ten-subsystem-forensic-hardening-2026-11-27) & [`ERRATA.md`](ERRATA.md) | **120 dossiers (`check_dossiers --strict` 100% clean), exact 537/537 1-to-1 citation-log bijection (646 audited, 0 dupes, 0 bare IDs, 287/287 DOIs 0 retracted), 0 statement-audit drift in `build_site.py`, `mypy --check-untyped-defs` 20/20 clean, `repo.yaml` schema-valid, 95 pytest PASS, 10/10 (100%) mutants, 42-file SHA-256 + RFC 3161 + Bitcoin OTS manifest, Mega-Atlas `v2.10.0` (2,000 problems / 290 crosswalk) parity** |
