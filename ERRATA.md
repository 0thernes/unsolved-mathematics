# Errata & Post-Release Correction Policy

This file maintains the public, append-only errata and correction ledger for **The Unsolved Mathematics Atlas** (`0thernes/unsolved-mathematics`), its Lean 4.35.0 formal core (`lean/`), and its companion white paper (`paper/Donahue_2026_unsolved_mathematics_atlas.pdf`).

## Correction & Withdrawal Policy

1. **Errors found after a tagged release are NEVER silently rewritten.** Every factual, mathematical, citation, formalization, or metadata error discovered after publication is logged here with date, affected version/tag, finding class (`bug`, `error`, `issue`, `problem`, `concern`, `dilemma`, `conflict`, `gap`, `hole`, `blindspot`), root cause, and commit SHA of the fix.
2. **Formal proof defect protocol:** If any theorem in `lean/` is discovered to have a statement-fidelity mismatch, vacuous hypothesis, disallowed axiom, or unsound modeling assumption, it is immediately flagged in this ledger and in `lean/STATEMENT_FIDELITY.md` before or alongside a corrective tag.
3. **Withdrawal / Retraction protocol:** If a major headline claim or white paper is found to be fatally flawed, we publish an explicit withdrawal notice at the top of this file, in `README.md`, and on the affected GitHub Release / Zenodo record rather than deleting history.
4. **How to report an error:** Open a GitHub Issue using the Bug / Error / Factual Correction form or email `0_0@0thernes.art` (see [`SECURITY.md`](SECURITY.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md)).

---

## Errata Ledger

| Date | Affected Release | Class | Component | Description & Resolution | Fixed In |
|---|---|---|---|---|---|
| `2026-11-23` | `v0.2.0` | `error` | `problems/*/papers.md` | 109 LLM-generated arXiv/DOI identifiers failed live primary-source verification against Crossref/arXiv APIs. All 109 bad identifiers were stripped and downgraded to `needs-verification`; 445 identifiers were API-verified (`data/citation-verification-log.json`). | `v0.3.0` (`8f1c94c`) |
| `2026-11-23` | `v0.2.0` | `error` | `data/problems.yaml`, `problems/unit-distance-problem/` | Erdős Unit Distance Problem remained marked `open` after the May 2026 arXiv disproof (`arXiv:2605.20695`). Updated to `recently-resolved` with explicit peer-review caveats; 14 live-verified 2024–2026 frontier citations added across 11 dossiers. | `v0.3.0` (`8f1c94c`) |
| `2026-11-23` | `v0.3.0` | `error` | `CLAIMS.md` (`C-03`), `meta-analyses/` | `CLAIMS.md` C-03 inverted the supercritical Collatz inequality sign; `meta-analyses/goldbach-conjecture.md` gave an outdated density (`0.72`); `meta-analyses/navier-stokes.md` gave an outdated year (`2003`); `meta-analyses/unit-distance-problem.md` lagged the May 2026 status update. All corrected with dated November 2026 addenda. | `v0.3.1` (`2c3e80a`) |
| `2026-11-23` | `v0.3.0` | `bug` | `docs/GLOSSARY.md` | Uppercase filename broke Build Standard check `A44` (`docs/glossary.md`) on case-sensitive Linux runners. Renamed to `docs/glossary.md` via two-step `git mv`. | `v0.3.1` (`2c3e80a`) |
| `2026-11-25` | `v0.3.1` | `conflict` | `docs/faq.md` vs `LIMITATIONS.md` | `docs/faq.md:20` cited `claude-opus-4-6` while `LIMITATIONS.md:26` and all 106 `meta-analyses/*.md` files recorded the non-canonical 2026-06-14 session label `claude-opus-4-8`. Reconciled `docs/faq.md` to accurately report the historical non-canonical label `claude-opus-4-8`. | `v0.4.0` |
| `2026-11-25` | `v0.3.1` | `concern` | `problems/collatz-conjecture/experiments/` | 9 historical July 2026 experiment logs/JSONs leaked local Windows filesystem paths (`C:\Users\...` and `Z:\[Vibe Coded (AI)]\...`). Sanitized to repo-relative paths and guarded by an automated regression test in `tests/test_verification_ladder.py`. | `v0.4.0` |
| `2026-11-25` | `v0.3.1` | `bug` | `scripts/Audit-Repo.ps1` | PowerShell `Set-Location` did not update `.NET` `[System.Environment]::CurrentDirectory`, causing false failures on `B10`/`B13`/`B17`/`B18` when invoked from another working directory. Fixed via `[System.IO.Directory]::SetCurrentDirectory($Root)`. | `v0.4.0` |
| `2026-11-25` | `v0.3.1` | `issue` | `docs/indexes/*.md`, `problems/collatz-conjecture/experiments/` | 89 non-PowerShell tracked files carried CRLF (`\r\n`) endings contrary to `.gitattributes`. Normalized to LF (`\n`) and ensured index/register scripts write `newline="\n"`. | `v0.4.0` (`f811c9b`) |
| `2026-11-25` | `v0.4.0` | `bug` | `problems/collatz-conjecture/experiments/odd_unit_lock_bridge_refinement.py` | Misplaced `if all_die: interpretation = ...` block inside `classify_refinement()` caused runtime `NameError` (`all_die` undefined in `classify_refinement`, `interpretation` undefined in `run()`). Relocated block into `run()` and added a permanent `ruff --select E9,F63,F7,F82` guard in CI and pytest. | `v0.5.0` |
| `2026-11-25` | `v0.4.0` | `error` | `SECURITY.md`, `README.md`, `docs/{operations,threat-model,glossary}.md`, `docs/adr/0002-multi-kernel-lean-core.md` | 18 stale pre-migration `formal/` path references and `Build Standard v1.1.0` strings remained after the `v0.4.0` `formal/` → `lean/` migration. Reconciled all active docs to `lean/` and `Build Standard v1.2.0` and added an automated stale-reference regression test. | `v0.5.0` |
