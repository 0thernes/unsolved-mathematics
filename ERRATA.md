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
| `2026-11-25` | `v0.4.0` | `bug` | `problems/collatz-conjecture/experiments/odd_unit_lock_bridge_refinement.py` | Misplaced `if all_die: interpretation = ...` block inside `classify_refinement()` caused runtime `NameError` (`all_die` undefined in `classify_refinement`, `interpretation` undefined in `run()`). Relocated block into `run()` and added a permanent `ruff --select E9,F63,F7,F82` guard in CI and pytest. | `v0.5.0` (`0604df5`) |
| `2026-11-25` | `v0.4.0` | `error` | `SECURITY.md`, `README.md`, `docs/{operations,threat-model,glossary}.md`, `docs/adr/0002-multi-kernel-lean-core.md` | 18 stale pre-migration `formal/` path references and `Build Standard v1.1.0` strings remained after the `v0.4.0` `formal/` → `lean/` migration. Reconciled all active docs to `lean/` and `Build Standard v1.2.0` and added an automated stale-reference regression test. | `v0.5.0` (`0604df5`) |
| `2026-11-26` | `v0.5.0` | `hole` | `lean/FormalAtlas/Defs.lean` (`isqrt`), `lean/lakefile.toml` | `Defs.isqrt` passed fixed fuel `32` to `isqrtAux`, which was exact for all `v0.5.0` witnesses ($n \le 8128$) and $n < 2^{32}$ but silently truncated for $n \ge 2^{32}$; additionally `lean/lakefile.toml` did not explicitly enforce `autoImplicit = false`. Raised `isqrt` fuel to `n`, proved `isqrt_spec` unconditionally for ALL $n \in \mathbb{N}$ in `PerfectNumbers.lean` (unlocking general `thm_euclid_even_perfect`), and enabled `autoImplicit = false` in `lean/lakefile.toml`. | `v0.6.0` |

---

## 2026-11-26 statement audit

An independent statement audit of `v0.5.0` (commit `0604df5`) was carried out on 2026-11-26. Audit log: <https://github.com/0thernes/0thernes-research-archive/blob/main/docs/reviews/2026-11-26-statement-audit.md>. The claim documents (`README.md`, `CLAIMS.md`, `LIMITATIONS.md`, `docs/`) and the descriptive text of `lean/formalization.yaml` were corrected in place. The items below sit in the frozen white paper, in `lean/` documentation, or in the Lean sources, and are recorded here instead of being edited. The 12 declarations added in `v0.6.0` were not part of the audit.

### White paper (`paper/Donahue_2026_unsolved_mathematics_atlas.tex` and the `v0.6.0` PDF)

1. **Where:** abstract (tex line 74, "the $3n-1$ barrier"); Explicit Non-Claim box (tex lines 108-112, "or methodological no-go barrier"); Section "Domain I" title (tex line 356, "$3n-1$ Sibling Barrier"); Theorem item at tex line 381 ("$\varepsilon$-Invariance barrier").
   **What is wrong:** the wording presents a formal barrier. `thm_collatz_epsilon_invariance_barrier` states only that the $3n-1$ map $T_-$ has the Terras parity-word bijection for every $d$ and positive supercritical cycles at $5$ (period 3) and $17$ (period 11). No Lean statement quantifies over arguments or proofs.
   **Correction:** read these passages as "the $3n-1$ sibling comparison". The inference that arguments which do not distinguish $\varepsilon = \pm 1$ cannot settle $3n+1$ is a heuristic, not a formalized theorem.
   **Affects a theorem statement:** no. The Lean statement and its mathematical content in the tex item at line 381 are correct; only the label and the summary wording overstate it.

2. **Where:** Explicit Non-Claim box (tex lines 110-112, "Lonely Runner for $n \ge 4$ and uniform $n$ ... remain open") and the Lonely Runner theorem block (tex lines 415-431).
   **What is wrong:** the state of the art is misstated and prior work is not credited. The Lonely Runner conjecture is proved for up to 13 runners in recent preprints: Rosenfeld, arXiv:2509.14111 (8 runners); Trakulthongchai, arXiv:2511.22427 (9 and 10 runners); Sungkawichai and Trakulthongchai, arXiv:2604.23906 (11 to 13 runners). The 4-runner case formalized as `thm_lonely_runner_n3` is classical (Betke–Wills 1972; Cusick 1973, as cited in `lean/STATEMENT_FIDELITY.md`).
   **Correction:** "the Lonely Runner conjecture remains open in general; it is proved for up to 13 runners (preprints above). The cases $n \le 3$ formalized here are classical."
   **Affects a theorem statement:** no.

### `lean/` documentation (not edited in this pass)

3. **Where:** `lean/STATEMENT_FIDELITY.md` line 65 (row 30, `thm_lonely_runner_n3_nondiv4`, "Elementary mod-4 coverage (7/8 classes)"); also the historical `CHANGELOG.md` entry for `[0.5.0]` ("all `7/8` mod-4 residue combinations").
   **What is wrong:** the hypothesis is $4 \nmid v_1, v_2, v_3$. Of the $4^3 = 64$ residue classes of speed triples mod 4, $3^3 = 27$ satisfy it. No reading gives 7/8. The proof uses the single witness $t = 1/4$.
   **Correction:** "27 of 64 speed-triple residue classes mod 4 (no speed divisible by 4), witness $t = 1/4$".
   **Affects a theorem statement:** no. The Lean statement is correct; the coverage figure in the prose is wrong.

4. **Where:** `lean/STATEMENT_FIDELITY.md` line 119 ("$n \ge 4$ and the general uniform conjecture for all $n$ remain OPEN").
   **What is wrong:** $n = 4$ to $12$ (5 to 13 runners) are proved in the preprints cited in item 2.
   **Correction:** "not formalized here for $n \ge 4$; proved in the literature for up to 13 runners; open in general".
   **Affects a theorem statement:** no.

### Known issues in the formal code (not yet fixed)

5. **Where:** `lean/FormalAtlas/Collatz.lean` lines 8-9 (module docstring, "no-go barriers"), lines 698-701 (section comment and docstring, "ε-Invariance / Sign-Blindness Barrier"), and the declaration name `thm_collatz_epsilon_invariance_barrier` (`lean/Challenge.lean` line 54, `lean/Solution.lean` line 58).
   **What is wrong:** the name and docstrings describe a barrier that the statement does not contain (see item 1).
   **Correction:** in a future release, reword the docstrings to "3n-1 sibling comparison" and consider a neutral alias for the declaration. Renaming requires updating `Challenge.lean`, `comparator.json` and `VerifyAxioms.lean` together.
   **Affects a theorem statement:** no.

6. **Where:** `lean/FormalAtlas/Defs.lean` lines 140-155 (`divSumPairs`, `divSum`, `IsPerfect`).
   **What is wrong:** `divSum n` sums divisor pairs up to `isqrt n`. `isqrt_spec` is now proved, but no Lean lemma states that `divSum n` equals $\sum_{d \mid n} d$. The agreement is checked only by pytest differential tests.
   **Correction:** add a lemma `divSum n = ∑ d ∣ n, d` (or an equivalent list-based statement) and cite it in `STATEMENT_FIDELITY.md`.
   **Affects a theorem statement:** yes, in its reading. `thm_perfect_numbers_first_four`, `thm_no_odd_perfect_le_100` and `thm_euclid_even_perfect` are kernel-checked statements about `IsPerfect` as defined. Their identification with the textbook statements ($\sigma(n) = 2n$) rests on the missing lemma.
