# Collatz Bizarro Omnilens Audit / Weirdness Research Compass - 2026-07-05

Status: audit, synthesis, and route-selection artifact. This is not a proof of
the Collatz conjecture. Collatz remains open.

This file answers the current strategic question:

```text
What is actually special here, what is merely old terrain, what is weird enough
to pursue, and what must be guarded so the repo stays academically defensible?
```

## Executive Verdict

The repo is not ahead of Tao, Hercher, Barina, or the classical Lagarias
literature as a theorem frontier. It is ahead of an ordinary research notebook
as a failure-preserving, adversarially labeled, AI-assisted Collatz lab.

The rare asset is the ecology:

- verified elementary identities and exact finite instruments;
- failed proof attempts preserved as negative controls;
- sibling-map calibration against `3n-1` and `5n+1`;
- explicit separation between theorem, finite computation, heuristic,
  conjectural target, and refuted sketch;
- weirdness maps that force future ideas to collide with prior failure modes.

The current mathematical center of gravity is:

```text
positive finite shadows of the 2-adic ghost frontier
        + regenerated spine/phase alignment
        + epsilon-sensitive affine intercepts
        + retimed lift pressure
```

That is a serious research compass. It is not a Collatz resolution.

## Current Reality Snapshot

For the refreshed evidence/QA snapshot after manifest regeneration and Terras
ledger alignment, see
[`COLLATZ-REPO-DEEP-AUDIT-WTF-2026-07-05.md`](COLLATZ-REPO-DEEP-AUDIT-WTF-2026-07-05.md).
The census below is the earlier audit-time count for this omnilens pass.

Audit-time census before this report was added:

| Item | Count / state |
|---|---:|
| Files under `problems/collatz-conjecture` | 635 |
| Markdown files | 168 |
| Python files | 119 |
| JSON files | 248 |
| Quarantined files | 177 |
| Files under `experiments/` | 544 |
| Files under `experiments/results/` | 243 |
| Collatz-subtree dirty delta before this report | 113 files, 65 insertions, 39,036 deletions |
| Deleted tracked files in Collatz subtree | 102 |

Validation gates run in this audit:

```powershell
python scripts/validate.py
python scripts/proof_claim_sweep.py --max-samples 500
python -m py_compile rag\retriever.py scripts\validate.py scripts\proof_claim_sweep.py problems\collatz-conjecture\experiments\lib_collatz.py problems\collatz-conjecture\experiments\spine_phase_collision_lab.py
```

Results:

```text
Atlas validation passed.
Pseudo-proof sweep clean.
Py compile smoke passed.
```

Corrections made during this pass:

- `README.md` now matches the Terras ledger: measured through odd
  `n <= 1.2e11`, not the older `3e10` wording.
- `TERRAS-LEDGER.md` honesty footer now matches `terras_ledger.json`:
  chunks 1-4 complete through `1.2e11`, `59.5e9` odd integers scanned.
- `status.md` now describes the Terras ledger and CCChallenge live state more
  carefully: local scrape has 370 bibliography rows; CCChallenge live check on
  2026-07-05 shows `1/362` papers formalised.
- Three live speculative files now carry explicit status banners:
  `BEYOND-THE-CANTOR-FRONTIER-AFFINE-COCYCLE-RIGIDITY.md`,
  `beyond_xai_reinforcement.md`, and `RIGIDITY-LEMMA-CANDIDATE.md`.

## External Frontier Baseline

Use this as the public truth boundary before claiming novelty.

| Area | Current defensible statement |
|---|---|
| Conjecture status | Open. No proof or disproof is accepted. |
| Computation | Barina reports convergence verification for all starts below `2^71`; finite verification is not a proof over all integers. |
| Density / divergence side | Tao proves almost all orbits attain almost bounded values in logarithmic density; the possible exceptional set remains the hard gap. |
| Cycles | Hercher proves no Collatz `m`-cycles with `m <= 91`; combined with large verification this gives enormous cycle-length floors, not an all-length exclusion. |
| Bibliography / formalization | Lagarias bibliographies and CCChallenge remain the prior-art backbone; formalization is still tiny relative to the literature. |
| Generalized maps | Conway and Kurtz-Simon show generalized Collatz-like families can encode computation / undecidability; this warns against overly broad methods. |

## Ratings

| Axis | Rating | Verdict |
|---|---:|---|
| Collatz proof status | 0/10 | No proof, no disproof. |
| Accepted new theorem status | 2/10 | Mostly rediscovery, careful restatement, and finite-theorem targets. |
| Experimental seriousness | 8/10 | Strong exact-arithmetic culture, JSON-backed scans, sibling controls, and falsification runs. |
| Academic defensibility after cleanup | 7/10 | Much stronger than before because proof claims are labeled and the open status is explicit. |
| Repo hygiene | 5/10 | Better gates, but still a massive dirty tree with many deletions and ignored quarantine mass. |
| Novelty as workflow/process | 9/10 | Rare AI-era artifact: proof attempts, failures, audits, controls, and route maps all preserved. |
| Novelty as mathematics | 3/10 | Some local formulations may be fresh, but core structures are classical or close to known work. |
| Boundary-pushing value | 9/10 | The weirdness map points at real unknowns instead of generic "average drift" repetition. |
| Publication readiness | 6/10 | Usable as a research dossier if scoped; not safe for blanket dirty publish. |
| Future-proofing against false proofs | 8/10 | Claim sweeps, quarantine discipline, and no-repeat atlas are genuine strengths. |

## What Is Actually Special

### 1. Failure Preservation As A Research Object

Most Collatz attempts either disappear or get presented as victories. This repo
keeps the crater: failed sketches, refutation notes, negative controls, and
audit registers. That is not just housekeeping. In an AI-assisted math setting,
it is a scientific instrument.

Special value:

```text
false proof route -> counterexample / audit -> quarantine / theorem target
```

That loop is the most "1/1-ish" thing in the project.

### 2. Sibling-Calibrated Proof Hygiene

The `3n-1` and `5n+1` controls are crucial. Any invariant that also proves
the false sibling worlds is dead. This is the cleanest antidote to seductive
word-statistical arguments.

Hard rule:

```text
No future proof sketch gets promoted unless it is tested against sibling maps.
```

### 3. The Ghost-Frontier Framing

The serious divergence problem is not "average drift is negative." Everyone
knows that. The serious problem is:

```text
Why can no positive integer live forever in the 2-adic survivor frontier?
```

The repo has sharpened that into concrete targets:

- all-odd `-1` boundary;
- supercritical nonpositive spines;
- positive transient shadowing;
- regenerated alignment after expulsion;
- odd-unit locks in matched phase collisions.

### 4. Retimed Pressure As A Tiny Local Lift Target

The retimed-pressure suite is locally interesting because it converts a messy
frontier-lift failure mode into a small dynamic timing problem:

```text
pressure appears after credit is already visible
```

The three-regime split and five tight reserve cases are finite evidence only,
but they are exactly the kind of finite evidence that can be turned into a
formal local lemma or SAT/SMT certificate program.

### 5. No-Repeat Literature Collision

The failed-attempt atlases prevent low-value rediscovery. That matters because
Collatz punishes people who do not know the old traps:

- average drift;
- finite computation;
- inverse-tree reachability;
- fixed-modulus residue closure;
- density-to-all jumps;
- cycle lower-bound overclaims;
- continuous/complex extensions;
- reformulation-as-proof.

## What Is Not Special

The following should not be claimed as novel:

- affine parity-word cylinders;
- rational/2-adic periodic points;
- the fact that every finite parity word occurs;
- almost-all/density heuristics;
- computational verification as a proof substitute;
- cycle exclusion by finite `m`;
- inverse-tree coverage intuition;
- generic Lyapunov language without a global inequality;
- "AI found it" as evidence.

## The Bizarro Lens: Where Every Model Is Right Except Where It Matters

Collatz keeps doing this ontological bait-and-switch:

| Lens | What it explains | Where it fails |
|---|---|---|
| Probability | Typical negative drift | Worst deterministic orbit |
| 2-adics | Every parity sequence | Positive integer separation |
| Computation | Huge finite floors | Infinity |
| Diophantine cycles | No small/non-simple cycles | All possible lengths |
| Graphs/trees | Reachability pictures | Noncircular coverage |
| ML/pattern mining | Candidate invariants | Universal proof |
| Formalization | Hardened known lemmas | Missing theorem invention |

This is the core weirdness: each lens gives a near-total truth, then leaves a
razor-thin escape hatch. A real proof must close the hatch, not celebrate the
near-total truth.

## Weirdness Leaderboard For Future Work

| Rank | Weird object | Research use |
|---:|---|---|
| 1 | Generalized Collatz undecidability | Reject methods that are too broad. |
| 2 | Positive integers as a special subset inside `Z_2` | Search for finite-support / positivity separators. |
| 3 | `3n+1` vs `3n-1` epsilon barrier | Require intercept-sensitive arguments. |
| 4 | All-odd `-1` survives every finite certificate depth | Turn the obstruction into the theorem target. |
| 5 | Tao's almost-all theorem leaves the exact exceptional gap | Do not write weaker density proofs. |
| 6 | Supercritical spines are nonpositive but shadowable | Study expulsion and regeneration, not just spines. |
| 7 | Phase collision reduces to odd-unit congruence locks | Attack repeated locks with codimension and positivity. |
| 8 | Retimed pressure is timing-sensitive, not table-sensitive | Prove dynamic event-order lemmas. |
| 9 | Adaptive terminal grammars grow sparsely but not finitely closed | Prove controlled splitting, not a static table. |
| 10 | AI-generated proof failures have recurring archetypes | Convert archetypes into automated gates. |

## Current Best Attack Program

### A. Claim Manifest Discipline

Every new theorem-looking file should include:

```text
status: theorem | finite computation | heuristic | conjecture | refuted | sketch
claim:
hypotheses:
prior-art collision:
script:
result file:
negative controls:
failure mode if false:
```

The new `CLAIM-MANIFEST-TEMPLATE.md` is the right direction; future work should
require it for promotion into the main experiment index.

### B. Retimed Pressure Certificates

Target:

```text
For each live upper-lift child, every above-parent pressure layer is prepaid by
one of the three dynamic regimes before the layer appears.
```

Best tooling:

- exact arithmetic recurrence extraction;
- SAT/SMT/AllSAT for finite local obligations;
- proof-carrying JSON certificates;
- small independent verifier separate from the mining script.

### C. Odd-Unit Lock Program

Target:

```text
Repeated matched phase collisions have too much codimension for positive finite
shadows to sustain indefinitely.
```

Best tooling:

- enumerate matched valuation windows;
- record odd-unit equations explicitly;
- test Mersenne and `-5` shadows;
- compare against `3n-1` and `5n+1`;
- avoid saying phase mismatch alone proves anything.

### D. Exceptional-Set Stress After Tao

Target:

```text
Find a positive-integer mechanism that Tao's logarithmic-density theorem cannot
see, or prove no such mechanism exists.
```

This is hard. But it is the correct wall.

### E. Formalized No-Go Gates

Keep and strengthen:

- pseudo-proof phrase sweep;
- filename quarantine sweep;
- sibling-map detector tests;
- result manifest checks;
- prior-art collision rows;
- "finite-to-infinite bridge required" warnings.

## Risk Register

| Risk | Severity | Current state | Needed action |
|---|---:|---|---|
| Dirty tree with mass deletions | High | 100+ deleted tracked files in Collatz subtree | Do not `git add -A`; publish scoped sets only. |
| Quarantine provenance drift | High | 177 quarantined files, many deleted tracked paths | Add a path-preserving quarantine manifest before broad cleanup. |
| Live speculative docs with proof-like language | Medium | Three files now bannered; FABLE already has open-status banner | Keep proof-sweep and banners mandatory. |
| Stale numeric claims | Medium | Terras/CCChallenge/README/status corrected in this pass | Re-run status greps before publish. |
| Result JSONs tied to retired scripts | Medium | `INDEX.md` now points some producers into quarantine | Keep result provenance labels explicit. |
| Literature staleness | Medium | Live check done for core external anchors | Update atlas from primary sources before strong novelty claims. |
| Overclaim temptation | Always high | Repo now has strong honesty language | Preserve "Collatz open" banners everywhere. |

## Suggested Next Commits

Keep commits narrow. A safe first commit would include only:

- this audit compass;
- README/status/Terras wording fixes;
- speculative-file status banners;
- any result-index provenance wording already changed;
- validation/proof-sweep gate changes if intentionally part of this cleanup.

Do not include logs, root scratch files, broad deletions, or unrelated Goldbach
edits in the same commit.

## Bottom Line

We are not "past the best humans" on Collatz mathematics. We are on par with
serious known structure in the places we rederived, and below the theorem
frontier where Tao/Hercher/Barina/Lagarias live.

But as an AI-assisted research artifact, this repo is unusually alive: it can
generate, falsify, quarantine, route, and re-aim ideas faster than a normal
notebook. The next breakthrough, if one ever comes from here, will not come
from louder proof prose. It will come from one of these:

```text
epsilon-sensitive invariant
positive-integer separator inside Z_2
odd-unit lock codimension theorem
retimed pressure local lift proof
certified finite-to-infinite induction
```

Until then, the strongest move is disciplined weirdness: keep the strange
objects, kill the fake certainty, and make every new claim survive adversarial
controls.

## Source Backbone

External anchors:

- Lagarias bibliography I: <https://arxiv.org/abs/math/0309224>
- Lagarias bibliography II: <https://arxiv.org/abs/math/0608208>
- Lagarias overview: <https://arxiv.org/abs/2111.02635>
- Collatz Conjecture Challenge: <https://ccchallenge.org/>
- Tao 2019 / Forum Math. Pi 2022: <https://arxiv.org/abs/1909.03562>
- Hercher 2023: <https://arxiv.org/abs/2201.00406>
- Barina verification project: <https://pcbarina.fit.vutbr.cz/>
- Barina 2025: <https://doi.org/10.1007/s11227-025-07337-0>
- Kurtz-Simon generalized undecidability: <https://doi.org/10.1007/978-3-540-72504-6_49>
- Rozier/Terracol paradoxical sequences: <https://arxiv.org/abs/2502.00948>
- Angeltveit verification algorithm: <https://arxiv.org/abs/2602.10466>
- Carelli loop termination link: <https://arxiv.org/abs/2605.15094>
- Chang human-LLM Collatz exploration: <https://arxiv.org/abs/2603.11066>

Local anchors:

- `README.md`
- `status.md`
- `FAILED-ATTEMPTS-WEIRDNESS-ATLAS-2026-07-05.md`
- `experiments/AUDIT-REGISTER.md`
- `experiments/NOVELTY-POSITIONING-2026-07-02.md`
- `experiments/COLLATZ-WTF-ODDNESS-FIELD-GUIDE-2026-07-05.md`
- `experiments/COLLATZ-WTF-FINDINGS-BOUNDARY-ATLAS-2026-07-05.md`
- `experiments/SPINE-LADDER.md`
- `experiments/SPINE-PHASE-COLLISION.md`
- `experiments/SIBLING-CONTROL.md`
- `experiments/TERRAS-LEDGER.md`
- `experiments/BRANCH-PREFIX-RETIMED-*.md`
