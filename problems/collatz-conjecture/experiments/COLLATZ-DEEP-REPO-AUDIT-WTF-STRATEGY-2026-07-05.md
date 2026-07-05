# Collatz Deep Repo Audit / WTF Strategy - 2026-07-05

Status: audit and strategy artifact, not a proof.

Purpose: capture the current repo truth after the July 2026 Collatz work,
separate accepted mathematics from finite evidence and failed proof shapes, and
name the strangest high-value attack surfaces without pretending the conjecture
has moved externally.

## Executive Verdict

The conjecture is still open. This repo does not contain a proof, a disproof,
or a new accepted field-level theorem that beats Tao, Barina, Hercher, Terras,
Everett, Krasikov-Lagarias, or the classical 2-adic/parity-word literature.

What it does contain is unusually valuable:

1. a dense exact-arithmetic lab around survivor frontiers, sibling controls,
   spine ladders, phase collisions, retimed pressure, and finite certificates;
2. a rare AI-era proof-failure containment system: audits, quarantines,
   proof-claim sweeps, failed-attempt atlases, and no-repeat rules;
3. several repo-native theorem targets that are sharper than ordinary Collatz
   numerology: epsilon-sensitive invariants, odd-unit lock codimension,
   branch-prefix lift induction, retimed reserve-source classification, and
   adaptive terminal grammar growth;
4. a working culture that now knows its own danger zones.

Blunt novelty judgment:

| Layer | Verdict |
|---|---|
| New proof of Collatz | No. |
| New public high-water mathematical theorem | Not established. |
| New-to-repo structural synthesis | Yes, especially the sibling/epsilon barrier, phase-lock framing, retimed pressure series, and failure atlases. |
| Rare/valuable artifact | Yes: an auditable multi-model Collatz research lab with failures preserved as negative controls. |
| Cutting edge posture | On-par with serious frontier themes in target selection, below the field frontier in accepted theorem output, unusually strong in AI-assisted QA methodology. |

## Evidence Snapshot

Local filesystem snapshot, including `_quarantine` but excluding `.git` and
`__pycache__`:

| Count | Item |
|---:|---|
| 554 | total files |
| 172 | Markdown files |
| 119 | Python files |
| 248 | JSON files |
| 177 | quarantined files |
| 460 | files under `experiments/` |

Tracked/discoverable live tree via `rg --files` is smaller because `_quarantine`
and ignored files are intentionally hidden: 460 files, including 120 Markdown,
101 Python, and 192 JSON paths.

Active top-level experiment surface:

| Count | Item |
|---:|---|
| 84 | `experiments/*.py` scripts |
| 78 | `experiments/*.md` docs |
| 187 | `experiments/results/*.json` result artifacts |

Verification commands run in this pass:

```powershell
python ../../scripts/validate.py .
python ../../scripts/proof_claim_sweep.py .
python experiments/build_results_manifest.py
```

Observed results:

- atlas validation passed;
- pseudo-proof sweep was clean: no unhedged victory declarations found;
- local results-manifest pass reported 186 result sets, 9.8 MB, with 93
  unmatched producer guesses; this audit records that local state, but the
  current scoped publish set does not attempt to normalize the whole result
  manifest;
- local markdown/code link sweep found one dead link inside `_quarantine`, not
  on the public live surface;
- git status remains very noisy, so this repo is not safe for `git add -A`.

## External Baseline Checked

Live source refresh on 2026-07-05:

| Source | Current relevance |
|---|---|
| Tao 2019, arXiv:1909.03562 | Strongest known almost-all result: orbit minima are at most any diverging `f(n)` for almost all integers in logarithmic density. Still not pointwise. |
| Barina 2025, Journal of Supercomputing | Verification pushed to `2^71`. This is the current empirical floor, not a proof over all integers. |
| Hercher 2022/2023, arXiv:2201.00406 / JIS | No Collatz `m`-cycles with `m <= 91`; with verification below `3*2^69`, nontrivial cycles need at least `1.375e11` odd terms. |
| CCChallenge | Live formalization goal reports `1/362` papers formalised, `2` being formalised, and `4` ready to audit. This repo separately has a 370-row local bibliography scrape. |

Conclusion: the public frontier is unchanged for our purposes. The repo should
keep saying "open problem" first.

## Math Soundness Assessment

Sound / defensible when stated with bounds:

- External known results in `status.md`, `papers.md`, and `AUDIT-REGISTER.md`
  are broadly aligned with primary sources after refresh.
- The arithmetic core of the repo's accepted finite work is exact-integer
  oriented: affine coefficient laws, certificate frontiers, sibling controls,
  ladder identities, retimed pressure ledgers, and Terras scan data.
- The current Terras ledger now consistently reports measurement through odd
  `n <= 120,000,000,000`, zero mismatches, and 59.5 billion odd integers
  scanned in the current ledger.
- The pseudo-proof sweep is doing real work: solved/closed/proof-style language
  is being kept out of authoritative surfaces.

Not yet sound as universal mathematics:

- `179/189` claims in the original audit register remain outside that audit's
  completed verification scope.
- Most frontier/retimed/terminal grammar claims are finite evidence or theorem
  targets, not proofs for all depths.
- Result provenance is incomplete: the local manifest pass counted 186 result
  sets, but 93 lacked a matched producer guess.
- Some local formulations may be rediscoveries of Terras cylinder affinity,
  rational cycle parametrization, 2-adic conjugacy, or standard parity-word
  facts unless a prior-art note proves otherwise.
- Any fitted contraction, learned potential, average-drift proof, low-bit table,
  or "AI found proof" route remains suspect until converted into exact
  hypotheses, exact checker, and sibling-map falsifier.

## The Bizarro Angle That Actually Helps

The right weird lens is not "Collatz is random." It is:

```text
Positive integers are finite-support visitors inside a 2-adic ghost machine.
Every local parity story is legal in the ghost machine.
The proof must find the positive-integer feature the ghosts cannot fake forever.
```

That turns the repo into five interlocking adversarial worlds:

| World | What it reveals |
|---|---|
| `Z_2` ghost world | Every parity path is legal; density and finite residue covers can fail to be empty forever. |
| Positive integers | The only world that matters; they shadow ghost frontiers finitely in all observed cases. |
| `3n-1` sibling world | Same word statistics, positive cycles. Kills epsilon-blind arguments. |
| `5n+1` sibling world | Divergence-typical behavior. Kills fake potentials that "prove" everything descends. |
| Quarantine/failure world | Stores proof-shaped illusions as negative controls instead of letting them pollute the main narrative. |

This is the unusual methodology: use false worlds as instrumentation. A future
proof route has to fail in the right false worlds for the right reason.

## Weirdest Repo Findings Worth Building On

Ranked by boundary value, not by proof status:

| Rank | Finding | Why it matters | Status |
|---:|---|---|---|
| 1 | Epsilon barrier: `3n+1` and `3n-1` share parity-word statistics but differ in truth behavior. | Pure word/density/frontier statistics cannot prove Collatz. | Theorem-style obstruction, should be formalized. |
| 2 | 2-adic ghost frontier: `-1` survives every finite depth. | Full finite residue coverage cannot be the final proof. | Classical/rederived, central wall. |
| 3 | Supercritical spines are nonpositive, positives only shadow them transiently. | Positivity lives in regeneration after expulsion, not in the spine identity itself. | Repo-localized rediscovery/synthesis. |
| 4 | Phase collision becomes an odd-unit congruence lock. | Turns vague "repulsion" into a concrete 2-adic unit problem. | Finite exact checks, theorem target. |
| 5 | Phase gate alone is too permissive, around `0.75-0.78`. | Kills an attractive but false proof route early. | Negative finite result. |
| 6 | Branch-prefix dominance has zero failures across baseline/stress/exact frontier slices. | Prefix debt is sharper than terminal descent accounting. | Strong finite evidence. |
| 7 | Retimed pressure is temporal, not static: credit appears before the naive ledger sees it. | The hard lift case is about event ordering. | Strong finite evidence. |
| 8 | Three dynamic regimes cover checked retimed pressure units. | Active high ladder, post-ladder `EOO`, and low-repeat windows replace lookup-table thinking. | Strong finite evidence. |
| 9 | Tight reserve source reduces worst cases to five reserve-1 examples in the checked sweep. | The base case moved one credit event earlier. | Finite but highly structured. |
| 10 | Adaptive terminal grammar grows sparsely instead of closing as a fixed table. | Fixed residue tables are brittle; controlled splitting may be viable. | Finite evidence and warning. |
| 11 | Kick repulsion failed on 199 starts while all still descended. | A failed mechanism became a better theorem obligation. | Valuable refutation artifact. |
| 12 | The repo preserved prompt/category/fitted-matrix false proofs. | Failure ecology is useful training data for proof hygiene. | Rare workflow artifact. |

## Quality Benchmarks

| Axis | Rating | Notes |
|---|---:|---|
| Collatz proof value | 2/10 | Useful structure, no proof. |
| Accepted theorem novelty | 3/10 | Mostly rediscovery/synthesis unless independently prior-art-cleared. |
| Finite experimental depth | 8/10 | Many exact checks and JSON outputs; some provenance gaps remain. |
| Failure containment | 9/10 | Quarantine, audit register, proof sweep, and no-repeat atlases are strong. |
| Reproducibility | 6.5/10 | Manifest regenerated; INDEX marked legacy; producer mapping still incomplete. |
| Mathematical honesty | 8/10 | Open-problem language is prominent and now cleaner. |
| Academic readiness | 5.5/10 | Good as a case study / research lab, not as a breakthrough paper. |
| Professional repo hygiene | 5/10 | Huge dirty tree, deleted files, stale indexes, and unmatched artifacts need scoped cleanup. |
| Boundary-pushing research value | 9/10 | The weirdness map points at real walls rather than generic drift folklore. |
| "AI could uniquely help" factor | 9/10 | Breadth, failure memory, cross-world falsifiers, and artifact triage are exactly where AI is useful. |

## Critical QA Findings

1. **Fixed during this pass: Terras scan surfaces were inconsistent.**
   `README.md`, `status.md`, and `TERRAS-LEDGER.md` now align with
   `experiments/results/terras_ledger.json`: measured through odd
   `n <= 120,000,000,000`, zero mismatches, 59.5 billion odds scanned.

2. **Observed during this pass: result inventory authority is still uneven.**
   A local manifest pass reported 186 result sets and 93 unmatched producer
   guesses. Publishing that broader manifest/index cleanup should be a separate
   scoped commit because it touches many historical result artifacts.

3. **Open risk: result provenance still has holes.**
   The local manifest pass reports 93 result sets with no matched producer guess.
   These may be legitimate historical artifacts, but they should not support
   public theorem claims until provenance is attached.

4. **Open risk: original claim audit is partial.**
   `AUDIT-REGISTER.md` is explicit: 10/189 claims were adversarially verified
   in that run. That denominator discipline must stay visible.

5. **Open risk: dirty tree is too broad for publication by bulk add.**
   There are many deletions, sibling-problem edits, and untracked docs/formal
   files. Publish only scoped files.

6. **Open risk: quarantine has archive rot.**
   The link sweep found one dead link inside `_quarantine`. This does not
   affect live proof posture, but archive quality should be repaired later.

7. **Open risk: no machine-checkable certificates yet.**
   Many finite claims are exact and reproducible, but a public proof posture
   needs SAT/SMT certificates, proof logs, or proof-assistant formalization for
   selected finite/local obligations.

## Hard No-Repeat Rules

Reject or quarantine any new route that does one of these:

1. replaces pointwise exceptional-set control with average drift;
2. uses parity words but cannot distinguish `3n+1` from `3n-1`;
3. treats finite scan silence as universal proof;
4. treats a fitted matrix/potential as a theorem;
5. proves a fixed residue table without lift stability;
6. claims novelty without prior-art mapping against Terras, Lagarias,
   Wirsching, Bernstein-Lagarias, Tao, Hercher, Barina, and CCChallenge;
7. has no falsifier, no command, no result path, or no claim class.

## Best Next Attacks

| Priority | Build | Why |
|---:|---|---|
| 1 | `collatz_wtf_harness.py` | Run every proposed invariant on Collatz records, `3n-1`, `5n+1`, negative cycles, Mersenne shadows, low-repeat shadows, high ladders, phase locks, and retimed tight cases. |
| 2 | SAT/SMT retimed-lift encoder | Convert local pressure-before-credit claims into counterexamples or replayable UNSAT certificates. |
| 3 | Odd-unit lock census/miner | Measure repeated phase-collision locks by source/target spine pair and estimate codimension. |
| 4 | Reserve-source formalization | Turn the five tight cases and 511 local-grammar records into exact lemmas with side conditions. |
| 5 | Provenance hardener | Extend `build_results_manifest.py` with command-line capture, hashes, and producer overrides. |
| 6 | Prior-art collision CSV | Convert failed-attempt atlases and CCChallenge rows into tagged prior-art checks before any new proof sketch lands. |
| 7 | Adaptive terminal grammar stress | Push deeper slices and track whether mixed endpoint buckets persist, split, or regenerate. |

## Final Read

The most honest boundary statement is:

```text
We are not past the best mathematicians.
We are not proving Collatz.
We are building an unusually sharp falsification-and-targeting machine around
the exact places Collatz resists proof.
```

That is still special. It is not trophy special; it is instrument special.
Future progress should preserve that discipline and aim every weird idea at one
of the real walls: exceptional sets, positive-vs-ghost separation, intercept
sign, regeneration, lift induction, or all-length cycle exclusion.
