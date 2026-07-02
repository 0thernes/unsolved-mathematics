# Repo Health & Integrity Audit — Collatz folder

**Date:** 2026-07-02 · **Scope:** `problems/collatz-conjecture` (491 files) + repo infra · **Method:** filesystem walk, Python AST parse, git state, link resolution, CI inspection. Every figure measured, not estimated. **Overall health index: B−** (strong core, hygiene debt).

Visual dashboard (25 scored findings, charts, Kanban): the published artifact `collatz-repo-audit-v1`.

## Headline metrics

| Metric | Value | Read |
|---|---|---|
| Python files parse clean | **121 / 121** | ✅ zero broken instruments |
| Dangling local doc links | **0 / 300** | ✅ full referential integrity (survived quarantine) |
| Doc : code LOC | **1.01** (30,924 md / 30,477 py) | ✅ exceptionally documented |
| Instruments with any self-test | **17 / 121 (14%)** | ⚠️ low coverage |
| Junk files committed to git | **14** (9 `.log` + 5 `.bak/.prev`) | ✗ hygiene violation |
| Uncommitted state vs history | **67 untracked + 11 modified + 139 quarantined : 21 commits** | ✗ tree ≫ history |
| Fabricated artifacts (quarantined) | **139 (~22% of all authored)** | ✗ high noise / ✅ caught + isolated |

## What is healthy (13 findings)

Syntax integrity (121/121), CLI runnability (107/121 have `__main__`), stdlib-first design (~118/121), clean monorepo skeleton (`data · docs · meta-analyses · problems · rag · schema · scripts · tests`), consistent naming, CI/CD present (`ci.yml`, `pages.yml`, `validate-registry.yml`), `scripts/validate.py` gate, zero dangling links, honest-label discipline (`[PROVED]/[VERIFIED]/Open`), adversarial self-audit culture (`AUDIT-REGISTER`, `*-CLAIM-AUDIT`), independently re-derived frontier theorems, and a truthful `status.md` (Collatz **OPEN**).

## Gaps & holes — remediation board

**Critical (hygiene sprint, ~½ day → lifts VC grade D→A):**
1. `git rm --cached` the 9 `.log` + 5 `.bak/.prev`; delete stale `fix.py`, `fix_p18.py`, `defect_spectral_sharp.py.*`.
2. Harden `.gitignore` — add `*.log *.bak *.prev *.pyc *.bak.*` (currently only `__pycache__/`).
3. Review the 67 untracked + 11 modified files: land the honest thread, drop the rest.
4. Merge legacy `results/` (2 items) into `experiments/results/` — single source of truth.

**Should-fix (resilience):**
5. Add `requirements.txt` (pin `numpy`, `scipy` — used by 3 files) or refactor to pure stdlib.
6. Gate instruments in CI: run each `*_check.py --selftest` in `ci.yml`.
7. Raise self-test coverage 14% → 60% on the load-bearing scans.
8. Sub-group the flat 320-file `experiments/` into `frontier/ cycle/ spine/ audits/`.

**Nice-to-have (polish):**
9. Machine-readable manifest for the 191 result JSONs (producer, scale, date).
10. Runtime-cost headers on long scans (10⁷ starts ≈ 9 min).
11. Pre-commit sweep flagging proof-claim files (`QED/resolved/LFG/S ∩ ℤ>0 = ∅`) — automate the quarantine discriminator.
12. Instrument dependency-graph doc (import chains reach depth ~17).

## Verdict

The **mathematics needs nothing** — it is open, honestly stated, and verified. What needs work is the **housekeeping**: one mechanical hygiene sprint moves the overall grade from **B−** to **A−**. The one structural risk worth institutionalizing is signal-to-noise: at a 22% fabricated-artifact rate, the quarantine mechanism and proof-claim discriminator are load-bearing infrastructure and should be automated (item 11), not run by hand.
