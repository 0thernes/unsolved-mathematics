# Repository Audit — The Unsolved Mathematics Atlas

_Read-only deep-dive audit · snapshot 2026-07-02 · branch `main` · v0.2.0 · no files modified._
_Visual companion (charts, diagrams, 25-point scorecard): Claude artifact `repo-audit-v1`._

> **Overall: B− (66/100).** World-class knowledge architecture — reproducible registry → generator →
> 106 complete dossiers → schema-gated RAG — held back by operational debt: testing, dependency
> pinning, git/quarantine hygiene, and an unstarted citation-verification sweep. No mathematical
> surface overclaims; Collatz is correctly marked **open** everywhere.

## Headline metrics (measured)

| Metric | Value |
|---|---:|
| Total files (non-git) | 1,715 |
| Markdown / JSON / Python files | 1,127 / 301 / 132 |
| Python LOC / Markdown LOC | 31,880 / 70,372 |
| Problems in registry | 106 |
| Dossiers structurally complete (8 md + metadata + rag/) | **106 / 106 (100%)** |
| Unauthored template dossiers | 0 |
| RAG corpus chunks (dossier-sourced) | 3,758 |
| Test functions / lines | 8 / 63 |
| Python files with a dedicated test | ~6 / 132 (4.5%) |
| Citations, verified / high-conf / needs-verif / ai-suggested | ~18 / 968 / 1,406 / 271 |
| collatz files / bytes vs median problem | 496 / 7.3 MB  vs  10 / 29 KB |
| Uncommitted working-tree entries | 78 |
| Quarantined numerology files (`_quarantine/`) | 141 (5.6 MB, untracked) |

## 25-point scorecard

Severity: 🟢 healthy · 🟡 attention · 🔴 defect. Score = auditor health estimate (0–100).

| # | Point | Cat | Sev | Score | Evidence |
|--:|---|---|:--:|--:|---|
| 1 | Single source of truth | Arch | 🟢 | 94 | `data/problems.yaml` → `generate.py`; no hand-duplicated authority |
| 2 | Deterministic ranking (CSS) | Arch | 🟢 | 92 | pure function of registry; CI fails on drift |
| 3 | Dossier completeness | Arch | 🟢 | 98 | 106/106, zero templates |
| 4 | Problem-size balance | Arch | 🔴 | 34 | collatz ≈49× files / 255× bytes of median |
| 5 | Top-level cleanliness | Arch | 🔴 | 38 | 2 crank `.md` loose in `problems/` root |
| 6 | Core script quality | Code | 🟢 | 85 | 6 idempotent scripts + 3 RAG; prose never clobbered |
| 7 | Test coverage | QA | 🔴 | 36 | 8 tests; experiments untested; no coverage metric |
| 8 | Dependency pinning | Code | 🔴 | 32 | lower-bounds only; no lock / `pyproject.toml` |
| 9 | Lint / format enforcement | Code | 🟡 | 48 | ruff non-gating; no pre-commit; no type-check |
| 10 | Experiment code hygiene | Code | 🟡 | 44 | tracked `*.bak/.prev/.bak.<ts>`; 95 unvetted scripts |
| 11 | Efficiency / time-complexity | Code | 🟡 | 62 | DP poly-time & sound; 2^k enums bounded; heavy tree |
| 12 | CI integrity gating | CI/CD | 🟢 | 80 | schema, ranking freshness, corpus, honesty gate, pytest |
| 13 | CI scope gaps | CI/CD | 🟡 | 50 | no coverage / retrieval benchmark; experiments ungated |
| 14 | Deployment / Pages | CI/CD | 🟡 | 52 | `pages.yml` disabled; site step a placeholder |
| 15 | Git hygiene | CI/CD | 🔴 | 40 | 78 uncommitted; `_quarantine/` not gitignored |
| 16 | Security / supply chain | CI/CD | 🟡 | 46 | no Dependabot / SAST / secret scan |
| 17 | Schema rigor | Data | 🟢 | 90 | `additionalProperties:false`, enums, bounds, regex |
| 18 | Citation verification | Data | 🔴 | 38 | <1% verified repo-wide (collatz swept only) |
| 19 | RAG corpus health | Data | 🟢 | 82 | clean provenance; 21 cosmetic term-mentions |
| 20 | Kanban / board freshness | Data | 🟡 | 54 | board shows 0 verified though collatz has 18 |
| 21 | Documentation depth | Data | 🟢 | 78 | ERD/DATA-MODEL/methodology/kanban/review present; **no PRD** |
| 22 | Collatz status honesty | Collatz | 🟢 | 92 | metadata/status/README all "open"; self-documents quarantine |
| 23 | Verified honest math thread | Collatz | 🟢 | 80 | 7 CI-green artifacts, both halves; all hedged |
| 24 | Quarantine completeness | Collatz | 🟡 | 50 | 141 isolated, but ~19 numerology files still live |
| 25 | Multi-session process control | Collatz | 🔴 | 36 | concurrent sessions re-deposit crank; experiments ungated |

## Gaps & holes — prioritized remediation

**P0 (integrity / correctness)**
1. **Move the two stray crank files** (`problems/11.8_MASTER_THEOREM.md`, `problems/defect_algebra_formal_proof.md`) out of `problems/` root into `_quarantine/` or delete; add a `validate.py` rule that `problems/` contains only slug directories.
2. **Enforce & complete the quarantine:** add `**/_quarantine/` to `.gitignore` (status.md already claims this); sweep the ~19 residual `P-*` / `defect_algebra` / `11.8` / `unverified-claims/` files in; fix the status.md wording.
3. **Gate the experiments tree in CI:** fail the build if any `problems/*/experiments/**` file matches proof-claim markers (`P⊢C`, `THE-PROMPT-IS-THE-PROOF`, `QED`+Collatz).

**P1 (quality / reproducibility)**
4. Grow tests: cover `rag/retriever.py`, `build_corpus.py`, and the honesty gate; wire `pytest --cov` with a floor.
5. Add `pyproject.toml` + a compiled lock; pin CI tool versions (pytest, ruff).
6. Start the citation-verification sweep by field; make the Kanban board reflect real counts.

**P2 (hygiene / polish)**
7. Delete tracked `*.bak/*.prev/*.orig`; add them to `.gitignore`.
8. Add a one-page PRD; regenerate the Kanban board; flip ruff to gating after a cleanup pass; wire `pages.yml`.

## Collatz — honest verdict

The thread splits cleanly into **real, verified mathematics** and **quarantined numerology**. The
genuine thread produced 7 CI-green artifacts across both halves of the conjecture's elementary
structure (descent/entropy ceiling; box + Hausdorff dimension = `H(log₃2)=0.94996`; the exact cycle
equation validated on all six known sibling cycles). Every one is a *classical result cleanly
re-proved* — no new theorem. A documented barrier (measure-zero survivor set; sign-blind siblings
`3n−1`/`5n+1` that genuinely have cycles) proves this family of methods **cannot** resolve Collatz.
The problem remains **open**, and the repo says so on every authoritative surface. That honesty is
the point — and it is the single most valuable thing to protect against the concurrent proof-claim
generation (points 24–25).

_Prepared as a read-only audit. Health scores are calibrated judgement, not repo metrics. A live
multi-session tree means file counts drift by a few between measurement and reading._
