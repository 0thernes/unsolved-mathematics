# Collatz Repo Deep Audit / WTF Boundary Review - 2026-07-05

Status: repo audit, research synthesis, and route-selection artifact. This is
not a proof of the Collatz conjecture. The conjecture remains open.

This file records the current live understanding of the repo after a fresh
local audit plus a small external status refresh. It is written for future
work: what is actually here, what is weird enough to keep pushing, what is
old terrain, and what must not be overclaimed.

## Executive Verdict

The repo is not a solved-Collatz repository. It is a dense, unusually honest
Collatz research lab with three valuable properties:

1. It preserves failures, refutations, and quarantined pseudo-proofs instead of
   letting them contaminate the evidence base.
2. It has real exact-arithmetic instruments around frontier residues, sibling
   controls, 2-adic obstruction geometry, retimed pressure, and terminal
   residue grammars.
3. It now has a literature/no-repeat layer that keeps future "new" ideas from
   accidentally rediscovering saturated Collatz folklore.

The most defensible novelty claim is process-level: an AI-assisted failure and
verification ecology that leaves a durable trail of claims, counterclaims,
scripts, JSON outputs, quarantines, and no-repeat maps. The mathematical
novelty is more modest: possible sharp local framings around epsilon-sensitive
barriers, retimed reserve-source induction, and endpoint grammar growth. None
of those is currently a theorem proving Collatz.

## Audit Window

Local checks run in:

`.\problems\collatz-conjecture`

Observed branch:

`codex/collatz-catalog-qa-routing`

Observed HEAD:

`a66c7cb docs(collatz): expand boundary findings atlas`

Observed remote:

`origin https://github.com/0thernes/unsolved-mathematics.git`

Working tree at audit time was intentionally noisy:

| Status kind | Count |
|---|---:|
| Modified | 18 |
| Deleted | 107 |
| Untracked | 6 |

Do not publish this tree with `git add -A`. Any publication should stage only
the intended files.

## Local Inventory Snapshot

| Surface | Count / note |
|---|---:|
| Active top-level experiment scripts in `experiments/*.py` | 84 |
| Active top-level experiment docs in `experiments/*.md` | 75 |
| JSON result artifacts in `experiments/results/*.json` | 187 |
| Files under `_quarantine/` | 177 |
| Selected markdown link check | passed |
| `python -m compileall -q experiments` | passed |
| `python ../../scripts/validate.py --help` | atlas validation passed |
| `python ../../scripts/proof_claim_sweep.py --help` | clean |

The compile check says the active Python files parse. It does not prove the
scripts are scientifically valid, fast, or executable under every CLI mode.

## External Sanity Refresh

The public baseline still agrees with the repo's caution.

- Barina's 2025 Journal of Supercomputing paper reports the computational
  verification limit as `2^71`: https://link.springer.com/article/10.1007/s11227-025-07337-0
- Barina's project page records milestones through `2^71` on 2025-01-15:
  https://pcbarina.fit.vutbr.cz/
- CCChallenge currently presents itself as "Formalising the Collatz literature,
  one paper at a time", with `1/362` papers formalised and `370` literature
  entries visible in the live page: https://ccchallenge.org/

This means the repo is current enough to be serious, but not special because
it has beaten the field. It has not.

## Repo Comprehension Map

The repo has five layers.

| Layer | Main files | Role |
|---|---|---|
| Public dossier | `README.md`, `status.md`, `papers.md`, `approaches.md`, `attempts.md` | Human-facing status, known results, and boundary statements |
| Experiment suite | `experiments/*.py`, `experiments/*.md` | Exact checks, finite scans, proof-target reports, and claim audits |
| Result ledger | `experiments/results/*.json`, `experiments/results/INDEX.md` | Raw outputs and provenance hints |
| Quarantine | `_quarantine/` | Refuted, disabled, or legacy artifacts that must not be cited as evidence |
| Governance | `AUDIT-REGISTER.md`, failed-attempt atlases, builder QA rubric, algorithm triage | Claim discipline, no-repeat routing, and publication hygiene |

This architecture is the repo's real strength. It makes "proof-like" text less
dangerous because there is a place to put it, test it, and demote it.

## Current Mathematical Posture

The problem remains split into the same two full-resolution obligations:

1. No divergent positive integer orbit.
2. No nontrivial positive integer cycle.

The repo's strongest internal work mostly attacks the divergence side through
finite residue certificates, frontier geometry, and positive-integer separation
from the all-odd 2-adic boundary.

The cycle side has useful in-repo rederivations and constraints, but the
public high-water marks still come from the computational verification plus
linear-forms-in-logarithms / continued-fraction lines. The repo should not
pretend its cycle work is beyond Hercher/Barina without a formal comparison.

## Weirdness Stack

These are the strangest findings that actually matter.

| Rank | Finding | Why it is weird | Research use | Proof status |
|---:|---|---|---|---|
| 1 | Epsilon barrier | `3n+1` and `3n-1` can share parity-word statistics while `3n-1` has positive cycles | Kills purely word-statistical proof routes | Strong local no-go framing |
| 2 | All-odd 2-adic ghost | The all-odd path survives every finite certificate depth as the 2-adic point `-1` | Forces positive-integer separation, not just finite covers | Known obstruction, locally instrumented |
| 3 | Survivor frontier dimension | The hard set is thin but persistent, with dimension near `H(log_3 2)` | Quantifies why density arguments miss possible exceptions | Repo theorem/verification surface, not Collatz proof |
| 4 | Threshold traps vanish | Certificate thresholds are far stronger than naive finite scans suggest | Moves attention to record/frontier integers | Strong local theorem, still not enough |
| 5 | Phase collision | Regeneration reduces to exact odd-unit congruence locks when valuations match | Converts vague "regeneration" into explicit arithmetic | Exact lab target; phase gate alone too permissive |
| 6 | Retimed pressure | New pressure can appear after earlier credit has already paid for it | Suggests temporal induction rather than static potential | Finite exact evidence, universal theorem open |
| 7 | Tight reserve source | The base case lives one credit event earlier than the visible local word | Points to a smaller induction invariant | Finite exact evidence |
| 8 | Terminal grammar growth | Endpoint residue trees almost transfer across depths but keep sparse new branches | Suggests controlled grammar growth, not fixed finite automaton | Strong finite evidence, no closure |
| 9 | Instrument-calibrated silence | Detectors stay silent on Collatz but fire in sibling worlds where bad behavior exists | Makes negative evidence meaningful instead of empty | Calibration strength, not proof |
| 10 | AI proof ecology | The same model ecology can invent false bridges and build refuters | Process-level novelty, math-level danger | Repo's best "1/1" process claim |

## What Looks Truly Special

Blunt split:

| Asset | New to literature? | New to this repo/workflow? | Verdict |
|---|---|---|---|
| Collatz proof | No | No | Not present |
| `2^71` verification | No | Used correctly | External baseline |
| Tao almost-all theorem | No | Used correctly | External high-water mark |
| Epsilon-sensitive sibling calibration | Likely known in spirit | Yes, unusually operationalized | Valuable local framing |
| Retimed reserve-source induction | Unknown priority | Yes | Best local theorem-target bet |
| Terminal endpoint grammar growth | Unknown priority | Yes | Good experimental frontier |
| Failure/quarantine/audit ecology | Maybe | Yes | Strongest special artifact |
| 1000-algorithm routing | No as math | Yes as repo governance | Useful only when tied to proof targets |
| 104-builder QA rubric | No as math | Yes as process | Useful as claim discipline |

## Most Important Risks

### 1. Dirty tree publication risk

There are many deletions and unrelated edits. A blind add/commit would mix
research content, repo hygiene, sibling-problem edits, and local churn.

Rule: stage named files only.

### 2. Stale provenance in result indexes

Several result rows still pointed at scripts now in quarantine. This audit
patched `experiments/results/INDEX.md` so the `beyond_*`, `chaitin_surprise`,
`defect_algebra*`, and `defect_spectral_sharp` rows point at `_quarantine`.

Remaining issue: many result rows still have producer `--` or name-matched
only. Treat them as weak provenance until rerun or linked to a script plus argv.

### 3. Surviving overstrong sketch language

`experiments/PROOF-SKETCH-AFFINE-COCYCLE-RIGIDITY-2026.md` is listed in the
README as speculative, but inside the file it still contains overstrong
"resolved in outline" style language. That should be bannered, demoted, or
moved to quarantine unless the repo wants to preserve it only as a historical
failure specimen.

### 4. Audit register is partial

`AUDIT-REGISTER.md` records `10/189` verified claims. This is honest, but it
means the majority of quantitative claims remain self-reported unless a later
audit specifically verifies them.

### 5. "Weird" can become theater

The repo is strongest when weirdness becomes a precise falsifiable target:
odd-unit locks, retimed pressure units, reserve-source base cases, endpoint
grammar splits. It becomes weak when weirdness becomes vocabulary without a
checkable object.

## Do-Not-Repeat Rules

1. Do not present density-one or logarithmic-density results as pointwise
   convergence.
2. Do not present finite verification, however large, as proof over all
   positive integers.
3. Do not use parity-word statistics alone; the epsilon barrier says that
   route cannot distinguish Collatz from sibling maps with cycles.
4. Do not use a fixed residue table as a final proof unless it comes with a
   lift theorem.
5. Do not trust LLM-generated proof prose without an executable checker or
   formal proof target.
6. Do not cite quarantined files as evidence.
7. Do not claim "new to the field" without mapping the claim against Lagarias,
   Wirsching, Terras, Tao, Barina, Hercher, and the CCChallenge bibliography.

## Best Next Attack Surfaces

### A. WTF Regression Harness

Build one script that reruns the smallest checks behind the weirdness stack:

- epsilon barrier sanity examples;
- all-odd `-1` frontier survival;
- phase-collision valuation identity;
- retimed first-threshold layer-one cases;
- tight reserve-source equality cases;
- terminal grammar held-out contradictions.

Goal: every new theorem target gets tested against the same minimal obstacle
set before it enters prose.

### B. Retimed Reserve-Source Induction

This is the most promising local proof-shaped route. The observed hard case is
not "credit exists somewhere"; it is "credit exists before the pressure layer
needs it". That is a temporal statement and should be formalized as a local
lift induction.

Needed theorem pieces:

- upper-child affine lift law;
- first pressure unit is one layer above parent;
- pressure unit belongs to active ladder, post-ladder, or low-repeat regime;
- layer-one reserve is already present before final align-3 entry;
- equality cases are classified by previous reserve source.

### C. Odd-Unit Lock Codimension

The phase gate is too permissive. The next useful theorem is not "phase mismatch
usually kills regeneration"; it is a positivity/codimension theorem for the
matched phase locks.

Needed output:

- exact lock equation;
- finite-support positivity condition;
- sibling-map control;
- failed-lock counterexample harness.

### D. Terminal Grammar Growth

The fixed automaton dream is already false or at least unsupported: deeper
frontiers introduce sparse novel branches. The stronger target is controlled
growth.

Needed theorem:

Every mixed terminal parent either resolves after bounded/adaptively bounded
additional low bits or enters a class that cannot reproduce hard-tail behavior.

### E. Formalization Triage

Only formalize after prior-art mapping. Good candidates:

- affine coefficient law;
- threshold-envelope trap-window theorem;
- epsilon barrier;
- branch-prefix affine lift lemma;
- retimed three-regime ledger schema.

## Current Build Queue

| Priority | Build | Output |
|---:|---|---|
| 1 | `wtf_regression_harness.py` | One fast script proving the weirdness stack has not drifted |
| 2 | `retimed_reserve_cegar.py` | Counterexample-guided splitter for the reserve-source induction |
| 3 | `odd_unit_lock_sat.py` | SAT/SMT exporter for phase-lock congruence and positivity constraints |
| 4 | `terminal_grammar_growth.py` | Cross-depth adaptive split monitor with contradiction minimizer |
| 5 | `result_provenance_linter.py` | Flags `--` producers, quarantined producers, missing argv, stale paths |

## Final Read

We are not outside the known mathematical universe. We are inside a very small,
very hard room of it.

The weirdness is real, but the useful weirdness is not mystical. It is exact:
same parity statistics with different truth values, a 2-adic ghost that finite
certificates cannot kill, pressure that arrives after its payment, endpoint
grammars that almost but not quite stabilize, and an AI workflow that can both
hallucinate and self-police.

The right posture is aggressive but clean:

- proof status: open;
- repo status: unusually rich and auditable;
- novelty: strongest at process and theorem-target formulation;
- next move: convert the weirdness stack into regression tests and local
  induction obligations.
