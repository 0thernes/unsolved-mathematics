# Collatz WTF Findings / Boundary-Push Atlas - 2026-07-05

Purpose: collect the strangest, most boundary-pushing Collatz findings from this repo and the public literature, then turn them into a hard-nosed research compass.

Status: synthesis artifact, not a proof. The Collatz conjecture remains open.

Companion: [`COLLATZ-WTF-ODDNESS-FIELD-GUIDE-2026-07-05.md`](COLLATZ-WTF-ODDNESS-FIELD-GUIDE-2026-07-05.md)
is the shorter field guide; this file is the ranked action atlas.

## Executive Read

The weirdest truth about Collatz is not that numbers go up and down. It is that almost every serious lens says "there should be no counterexample," while every lens also leaves a tiny, exact, persistent place where a counterexample could hide.

This repo's best current role is not theorem-frontier dominance. It is an unusually rich failure-and-boundary lab:

- `116` Markdown docs, `101` Python instruments, and `192` JSON artifacts are visible in the current working tree.
- `experiments/results/INDEX.md` indexes `109` result artifacts.
- `experiments/AUDIT-REGISTER.md` records `189` objectively checkable claims, with `10/189` adversarially verified in that audit run.
- The accepted math posture remains: open problem, finite evidence, theorem targets, and no public claim of proof.

The most promising "1/1-ish" value is methodological plus some local structural sharpening:

1. calibrated sibling controls showing what false Collatz-like worlds look like;
2. exact 2-adic spine/phase/regeneration language;
3. finite retimed-pressure ledgers that isolate a tiny local lift target;
4. a preserved ecology of proof-like failures, refutations, and quarantine.

## Research Ratings

| Axis | Rating | Meaning |
|---|---:|---|
| Literature frontier relevance | 9/10 | Aimed at the real public wall: distributional control does not imply pointwise convergence. |
| Mathematical proof status | 2/10 | No Collatz proof is present; the strongest objects here are theorem targets and finite ledgers. |
| Empirical/computational seriousness | 8/10 | The strongest repo claims are tied to exact identities, finite scans, sibling controls, and JSON-backed measurements. |
| Novelty as workflow | 9/10 | The rare part is the failure-containment lab: false proof routes are converted into instruments, audits, and no-repeat gates. |
| Novelty as accepted theorem | 3/10 | Some local formulations may be new, but no field-level theorem is claimed without outside review. |
| Boundary-pushing value | 9/10 | The weirdness map points to specific attack surfaces: odd-unit locks, retimed reserve induction, and epsilon-sensitive invariants. |

Blunt version: this is not "we beat Tao/Hercher/Barina." It is "we now know
where not to waste time, and we have unusually sharp places to push."

## Legend

| Score | Meaning |
|---:|---|
| WTF | How bizarre / intuition-breaking the finding is. |
| Boundary value | How much it points at an actual unknown unknown. |
| Novelty posture | Whether this is field-known, repo-sharpened, or potentially rare as an artifact. |
| Research action | What we should do with it next. |

Scale: `10` means "this should shape strategy."

## The Top WTF Findings

| Rank | Finding | Source | WTF | Boundary | Novelty posture | Why it matters | Research action |
|---:|---|---|---:|---:|---|---|---|
| 1 | Generalized Collatz maps can simulate computation / become undecidable. | Conway, Kurtz-Simon, Lagarias surveys | 10 | 10 | Field-known | Any method broad enough to solve "all Collatz-like maps" is probably impossible. | Force every new approach to name the `3n+1`-specific ingredient. |
| 2 | The 2-adic world makes every parity sequence legal. | Terras, Bernstein-Lagarias, repo cylinder work | 10 | 10 | Field-known, repo-rederived | Local parity patterns cannot be forbidden; the positive integers are the exceptional slice. | Build a positive-integer separator, not another parity argument. |
| 3 | `3n+1` and `3n-1` have identical parity-word statistics but different truth behavior. | `SIBLING-CONTROL.md`, `EPSILON-BARRIER.md` | 10 | 10 | Repo-sharpened | Pure word/density/frontier statistics cannot prove Collatz because the same stats allow positive cycles in `3n-1`. | Every candidate proof must pass the epsilon-sibling control. |
| 4 | The all-odd survivor is `-eps`: `-1` for Collatz, `+1` for `3n-1`. | `SIBLING-CONTROL.md` | 10 | 10 | Repo-sharpened | The boundary point changes sign, and the positive survivor statement flips truth value. | Study intercept sign and finite-positive shadows, not just words. |
| 5 | Tao gets "almost bounded" for logarithmic almost all, but the exceptional set can still contain every counterexample. | Tao 2019 | 9 | 10 | Field frontier | The strongest modern theorem identifies the exact gap: density is not pointwise control. | Attack exceptional-set structure after Tao, not weaker average drift. |
| 6 | The survivor frontier has dimension `H(log_3 2) = 0.9499555...` and density about `2^-0.050044d`, yet never empties. | `FRONTIER-GEOMETRY.md`, `ESCAPE-ENVELOPE.md` | 9 | 10 | Field-aligned, repo-computed | The bad set is measure-zero but combinatorially huge: thin is not empty. | Convert thinness into a positive-integer escape theorem or stop. |
| 7 | Integers match the 2-adic/free-coin frontier model to shocking precision. | `FRONTIER-GEOMETRY.md` | 9 | 9 | Repo-measured | Mean `tau`, tail ratios, and Mersenne detachment all look measure-typical; no anomaly is visible. | Search specifically for deviations from measure-typicality at extreme depth. |
| 8 | Supercritical spines are nonpositive: positive integers can ride them but not live there. | `SPINE-LADDER.md` | 9 | 9 | Classical objects, repo-localized | Negative cycles are not bugs; they are exact supercritical spine residents. Positives only shadow them transiently. | Prove regeneration cannot sustain repeated supercritical shadowing. |
| 9 | Phase collision is an explicit odd-unit congruence lock, not vague "repulsion." | `SPINE-PHASE-COLLISION.md` | 9 | 9 | Repo-sharpened | Regeneration reduces to `3^a u == constant mod 2^R` in matched phases. | Quantify lock codimension across positive finite shadows. |
| 10 | The phase gate alone is far too permissive: allowed fraction about `0.75-0.78`. | `SPINE-PHASE-COLLISION.md` | 8 | 9 | Repo-negative result | "Phase mismatch kills regeneration" is false as a proof route. | Use odd-unit locks and positivity, not phase mismatch alone. |
| 11 | Nontrivial cycles, if any, need absurdly many odd terms, but finite lower bounds never become infinity. | Hercher, Barina, cycle labs | 8 | 8 | Field-known, repo rederived | The cycle side feels physically impossible and remains logically open. | Separate cycle exclusion from divergence; do not overclaim lower bounds. |
| 12 | `3n-1` cycle minima are detected exactly by the same machinery that is silent on Collatz. | `SIBLING-CONTROL.md` | 9 | 9 | Repo-calibrated | Instrument silence on Collatz is now meaningful because the instrument barks in a false sibling world. | Keep sibling controls mandatory in CI/audit gates. |
| 13 | `5n+1` shows divergence-typical behavior at about `17.55%`, matching its word-model survival constant. | `SIBLING-CONTROL.md` | 8 | 8 | Repo-calibrated | A similar-looking map can visibly leak into divergence. | Use `5n+1` to kill fake potentials and detectors. |
| 14 | Certificate thresholds are vacuous through depth 28: only `0` and `1` are sub-threshold exceptions. | `FRONTIER-GEOMETRY.md`, `THRESHOLD-ENVELOPE.md` | 8 | 9 | Repo-measured | Finite certificates are stronger than expected, yet the infinite frontier remains. | Push threshold-vacuity/lift proofs with formal certificates. |
| 15 | The first-moment escape envelope predicts worst certificate depth near `19.982b`. | `ESCAPE-ENVELOPE.md` | 8 | 9 | Repo-quantified | It turns "uniform escape" into a single measurable law. | Try to falsify with deeper frontier beam search; seek a theorem only after falsification pressure. |
| 16 | Retimed pressure events are prepaid before the obvious parent-child ledger sees enough new total credit. | Retimed-pressure series | 9 | 9 | Repo-specific finite discovery | The hard lift case is about timing, not just total credit. | Prove the local layer law, ideally with SAT/SMT certificates. |
| 17 | Every checked retimed pressure unit falls into exactly three dynamic regimes. | `BRANCH-PREFIX-RETIMED-THREE-REGIME-LEDGER.md` | 8 | 9 | Repo-specific finite discovery | Active ladder, post-ladder `EOO`, and low-repeat gates cover `16,085` pressure units. | Derive these regimes from live upper-lift algebra. |
| 18 | The tightest retimed cases are only five reserve-`1` cases. | `BRANCH-PREFIX-RETIMED-TIGHT-RESERVE-SOURCE.md` | 8 | 9 | Repo-specific finite discovery | The equality case moved backward to prior reserve source, not the final local word. | Prove pre-entry reserve `>= 1`; classify equality. |
| 19 | The local align-3 grammar is necessary but not sufficient: `511` records, only `5` tight. | Tight grammar/reserve series | 8 | 8 | Repo-negative result | Local low-word pattern alone overselects by 100x. | Add credit history, not more residue lookup tables. |
| 20 | Low-bit residue tables become predictive but never complete. | Retimed signature/post/low-repeat notes | 7 | 8 | Repo-negative result | Static finite-state classifiers keep missing dynamic context. | Use dynamic event algebra plus proof logs. |
| 21 | Kick repulsion looked proof-shaped, then failed on `199` starts while all still descended. | `KICK-REPULSION-CLAIM-AUDIT.md` | 9 | 8 | Repo failure artifact | The mechanism was useful but not sufficient; failures were informative. | Preserve as a falsifier and theorem-obligation ledger. |
| 22 | A tautological detector can look like a deep repulsion event. | `AFFINE-COCYCLE-CLAIM-AUDIT.md`, audit register | 9 | 8 | Repo failure artifact | Counting an identity is not proving it pays debt. | Require sibling failures and non-tautological obligations for every detector. |
| 23 | Fitted matrix/spectral contractions can "prove" convergent, divergent, and cyclic maps alike. | Audit register, failed-attempt atlas | 9 | 8 | Repo failure artifact | Regression is not theorem; denominator freeze can fake convergence. | Ban learned/fitted proof claims unless backed by exact inequalities. |
| 24 | Prompt-as-proof and category/topos proof families appeared and had to be quarantined. | `AUDIT-REGISTER.md`, unverified-claims history | 8 | 7 | Methodological rarity | The repo captures AI-era proof hallucination as data. | Keep quarantine and claim manifests; never delete without record. |
| 25 | Paradoxical post-stopping sequences can locally exceed odd-ratio expectations. | Rozier-Terracol 2025 | 8 | 8 | Public watchlist | Even after stopping-time intuition seems safe, finite behavior can surprise. | Compare with repo repayment motifs and rare outlier classes. |
| 26 | Reachability for generalized Collatz maps can be non-definable in Buchi arithmetic. | Dhiman-Pandey 2026 | 9 | 8 | Public logic edge | Finite automata / Presburger-style dreams have hard limits. | Use automata only as bounded certificate tools, not final proof language. |
| 27 | Operator-algebra formulations make Collatz equivalent to irreducibility/no reducing subspace conditions. | Mori 2024/2025 | 8 | 7 | Public weird reformulation | Beautiful equivalence may simply hide the same problem in Hilbert-space language. | Treat as conceptual watchlist, not primary route. |
| 28 | Near-conjugacy to irrational circle rotation gives bounded local error. | Honarvar Shakibaei Asli 2026 | 8 | 7 | Public geometric watchlist | Collatz can look like rotation plus arithmetic error; cumulative control is the monster. | Compare phase/rotation language to repo phase-collision locks. |
| 29 | A 3-smooth coordinate skeleton gives deterministic diagonal flow until boundary exits. | Williams 2026 | 8 | 7 | Public fresh watchlist | Coordinate systems can make parts trivial while pushing all difficulty to exit boundaries. | Cross-map with spine exits and regeneration equations. |
| 30 | Polynomial analogues over `F_2[x]` can be tractable while integers remain opaque. | Alon-Behajaina-Paran 2024 | 8 | 7 | Public analogue | Collatz-like behavior can become solvable in a different algebraic universe. | Use as contrast class only. |
| 31 | Formalization projects are barely started relative to the literature mass. | CCChallenge | 7 | 8 | Public infrastructure | Proof hygiene is itself a frontier; one formalized paper does not solve the gap. | Formalize repo lemmas only after prior-art mapping. |
| 32 | The repo's rare asset may be an AI-verification failure-containment artifact, not a math theorem. | `NOVELTY-POSITIONING-2026-07-02.md` | 8 | 8 | Potentially rare process artifact | This may be special even if the accepted mathematics is rediscovery. | Preserve provenance, failed claims, and exact rerun commands. |
| 33 | The central unknown is not "does average drift win?" but "why can no positive integer live in the ghost frontier forever?" | Whole corpus | 10 | 10 | Strategic synthesis | This is the cleanest boundary question. | Organize future work around positive-integer ghost separation. |

## Repo-Specific WTF Stack

These are the local findings most worth building around.

### 1. The Epsilon Barrier

The killer sentence:

```text
No epsilon-invariant/parity-word-statistical argument can prove the divergence half of Collatz.
```

Why: `(3,+1)` and `(3,-1)` have the same parity-word distribution, same survivor counts, same frontier dimension, and same word-model mean. But `(3,-1)` has positive nontrivial cycles. Therefore a proof must consume the intercept sign, not only words.

Research consequence: every proposed invariant gets tested on `3n-1` and `5n+1`. If it also "proves" those false sibling maps, it is dead.

### 2. Ghost Frontier vs Positive Integers

The frontier is a 2-adic survivor Cantor set. It contains `-1` forever. Positive integers shadow it only finitely in every observed case. The hard statement is:

```text
S ∩ Z_{>0} = empty
```

or, operationally:

```text
No finite positive shadow can regenerate supercritical alignment forever.
```

Research consequence: stop proving the frontier is tiny. Prove positives cannot inhabit it.

### 3. Spine Ladders

Every supercritical parity word has a rational/2-adic spine `rho_w`, and every checked/derived supercritical spine satisfies `rho_w <= -1`. The exact ladder law burns one bit of alignment per shortcut step while riding a spine.

Why weird: the scary supercritical attractors are real, exact, and nonpositive. Positive integers do not live there; they surf the ghost boundary and get expelled.

Research consequence: the open problem is not initial alignment. It is regenerated alignment after expulsion.

### 4. Phase Collision And Odd-Unit Locks

Regeneration toward a later spine has the form:

```text
T^t(x) - eta = 3^a(t) 2^(m-t) u + (rho_t - eta)
```

Only matched valuations allow deep cancellation. Then the whole problem becomes an odd-unit congruence lock.

Why weird: "repulsion" becomes a precise congruence equation. The monster has coordinates.

Research consequence: count and bound repeated odd-unit locks; do not rely on phase mismatch alone.

### 5. Retimed Pressure

In exact frontier lifts `18 -> 19` through `25 -> 26`, all `13,856` retimed transitions and `16,085` above-parent pressure units were covered by three regimes:

```text
active high ladder: 15,259
post-ladder EOO:      646
low-repeat OO/OOEOO:  180
```

Every pressure layer matched its event index; layer `1` occurred exactly once per retimed transition.

Why weird: new pressure arrives, but the relevant credit was already visible earlier. The proof-shaped object is temporal, not just algebraic.

Research consequence: prove a local lift theorem where the m-th pressure layer is paid by the m-th dynamic event.

### 6. Tight Reserve Source

The hardest checked retimed cases reduce to five reserve-`1` examples. All five have exactly two prior credit events before the final align-3 entry; four source from previous align-3 high-ladder credit, one from low-repeat align-8 credit.

Why weird: the "base case" is not where the visible local word is. It lives one credit event earlier.

Research consequence: classify equality by prior reserve source.

### 7. Instrument-Calibrated Silence

The detector matrix finds exactly the known `3n-1` cycle minima `{1,5,17}` and flags `5n+1` divergence-typicality, while staying silent on Collatz through the checked range.

Why weird: silence normally means nothing. Here it means the instrument has been calibrated in worlds where the bad thing exists.

Research consequence: every future detector must have a false-world calibration.

### 8. Failure Preservation

The repo preserved proof-shaped failures:

- counted repulsion insufficiency;
- tautological event detectors;
- fitted contraction pseudo-proofs;
- prompt-as-proof/category errors;
- exotic vocabulary without residue-level content.

Why weird: in AI-assisted math, the failure ecology may be as scientifically valuable as the successes.

Research consequence: keep failed ideas as negative controls and training data for theorem hygiene.

## Public Literature WTF Stack

Use this as the outside-world strange-residue baseline.

| Area | Why it is bizarre | Why it does not solve Collatz |
|---|---|---|
| Generalized undecidability / FRACTRAN | Arithmetic iteration can simulate computation. | Original `3n+1` may be special; general hardness is not a proof. |
| 2-adic shift conjugacy | Every parity sequence corresponds to one 2-adic integer. | Most of those are ghosts, not positive integers. |
| Tao 2019 | Deep harmonic/entropy machinery reaches almost-bounded values for almost all. | Counterexamples can hide in the exceptional set. |
| Hercher / cycle floors | Nontrivial cycles are pushed to absurd complexity. | Infinite cycle lengths remain. |
| Barina verification | Everything below `2^71` converges. | Finite verification is not infinity. |
| Buchi non-definability | Generalized reachability may evade finite automata arithmetic. | Family result, not original convergence. |
| Operator algebras | Collatz becomes irreducibility/equivalence in C*-algebra terms. | Equivalent hard condition can be as hard as original. |
| Near circle rotation | Collatz resembles irrational rotation plus bounded error. | Local/cumulative error control is still the problem. |
| Paradoxical sequences | Post-stopping behavior can exceed ratio-based expectations. | Finiteness/impact remains conjectural. |
| Polynomial analogues | Another algebraic world may be tractable. | Analogue is not integer Collatz. |

## Current External Sanity Check (2026-07-05)

The public baseline still says "open":

- Tao's arXiv page states that for any `f(n) -> infinity`, the Collatz orbit
  minimum is at most `f(n)` for almost all positive integers in logarithmic
  density. This is still almost-all, not every integer.
- Hercher's arXiv page states no Collatz `m`-cycles with `m <= 91`, and notes
  the conditional path to a cycle floor of at least `1.375 * 10^11` odd terms
  once convergence is checked below `3 * 2^69`.
- Barina's 2025 Journal of Supercomputing article reports verification below
  `2^71`; this is the current empirical floor, not a theorem over all integers.
- Lagarias's overview frames the problem as hard despite being easy to state;
  the annotated bibliography records the conjecture as unsolved.
- Kurtz-Simon's generalized Collatz result is `Pi^0_2`-complete for a natural
  generalized problem, not a proof about the original `3n+1` map.
- Rozier/Terracol's paradoxical-sequence paper is useful finite-structure
  stress input around stopping-time intuition, not a proof.
- Angeltveit's 2026 paper is a verification algorithm, not a proof.
- Carelli's 2026 loop-termination paper is useful because it ties
  one-variable loops to generalized Collatz sequences; it transfers difficulty
  rather than settling original Collatz.
- Chang's 2026 human-LLM paper is useful as a structural/process object, but
  even its abstract says it is not a proof of Collatz.

Correct posture: current, aggressive, and boundary-aware; still strictly open.

## What Looks Truly Special Here

Blunt novelty split:

| Candidate | New to field? | New / rare as artifact? | Verdict |
|---|---|---|---|
| Collatz proof | No | No | Not present. |
| Parity-vector/cylinder/2-adic machinery | No | Locally reimplemented | Classical. |
| Spine ladder identity | Probably no | Useful local unification | Rediscovery with presentation value. |
| Positivity localization of supercritical spines | Needs prior-art review | Locally sharp | Possible narrow presentation margin. |
| Epsilon barrier with identical frontier statistics and calibrated detectors | Needs specialist prior-art review | Strong local artifact | High-value local contribution candidate. |
| Retimed pressure three-regime finite ledger | Not a theorem yet | Locally unusual | Theorem-target mining. |
| AI proof-failure containment / audit trail | Maybe | Yes | Best 1/1 process claim. |

## The Real Unknown-Unknown Targets

These are the places where pushing boundaries is rational.

1. **Positive-integer separator for 2-adic ghosts**
   - Need: a theorem distinguishing finite positive shadows from persistent ghost residents.
   - Falsifier: a sibling map or negative cycle where the same separator gives a false result.

2. **Regeneration bound after spine expulsion**
   - Need: control of `v2(3^j u + delta)` across changing spines/phases.
   - Falsifier: families whose regenerated alignment exceeds random-model envelopes.

3. **Odd-unit lock codimension theorem**
   - Need: show repeated locks cost enough entropy that positives cannot sustain them forever.
   - Falsifier: constructive lock chains with low cumulative codimension.

4. **Retimed local lift theorem**
   - Need: prove every live upper-lift pressure layer is dynamically prepaid.
   - Falsifier: SAT/SMT-found child transition with pressure before credit.

5. **Adaptive terminal grammar growth bound**
   - Need: prove rare endpoint classes split into pure terminal leaves under bounded or controlled lifting.
   - Falsifier: persistent mixed endpoint family under deeper probes.

6. **Cycle-side all-length Diophantine exclusion**
   - Need: uniform control of `2^d - 3^o` beyond finite continued-fraction/Baker floors.
   - Falsifier: hypothetical parity words producing better and better near-misses.

7. **Formal certificate infrastructure**
   - Need: proof logs for finite unsat/lift obligations.
   - Falsifier: any certificate that cannot be independently replayed.

## New Work Rule

Every future Collatz idea should start with this declaration:

```text
This attacks wall: [exceptional set / 2-adic ghost / regeneration / infinite cycle family / abstraction completeness].
It uses special 3n+1 information: [intercept sign / positive finite support / 2-vs-3 Diophantine arithmetic / other].
It fails on the following sibling/control: [3n-1 / 5n+1 / negative cycles / known records].
It has this falsifier: [script / SAT query / exact counterexample class].
```

If an idea cannot fill those four lines, it is probably old, circular, or just pretty.

## Hard No-Repeat Rules

1. Do not do another average-drift proof unless it names the exceptional set
   and kills it pointwise.
2. Do not do another inverse-tree proof unless it proves coverage without
   circularly assuming convergence.
3. Do not do another finite-verification proof unless the induction beyond the
   verified floor is explicit.
4. Do not do another parity-word proof unless it fails on `3n-1` for the right
   reason.
5. Do not do another "repulsion" proof unless low alignment and high alignment
   are separated.
6. Do not do another AI-generated theorem stack without a manifest of exact
   identities, tested claims, and open obligations.

## Boundary Bets

| Bet | Artifact | Kill condition | Win condition |
|---|---|---|---|
| Odd-unit codimension is real | `collatz_odd_unit_lock_census.py` | Locks stay permissive after unit filtering | Repeated regeneration forces measurable codimension loss |
| Retimed reserve is inductive | `branch_prefix_retimed_induction_probe.py` | A deeper lift violates the three-regime / reserve-source pattern | The layer law persists and admits symbolic proof |
| Sibling lint catches bad proofs | `collatz_epsilon_lint.py` | A proposed invariant distinguishes siblings only by narration | Every accepted invariant consumes `eps` or `c_d` explicitly |
| Tight cases have phase signature | `retimed_phase_bridge.py` | The five tight cases are ordinary in lock space | Reserve-`1` cases map to an extreme congruence/codimension class |
| Paradoxical sequences stress potentials | `paradoxical_sequence_import.py` | Drift/potential claims survive only because tests are too tame | Potentials are repaired against known paradoxical finite behavior |

## Immediate Build Queue

1. **WTF harness**
   - One script that runs any proposed invariant on Collatz, `3n-1`, `5n+1`, negative cycles, Mersenne shadows, hard records, and retimed frontier examples.

2. **SAT/SMT retimed-lift checker**
   - Encode the local lift pressure-before-credit claim for bounded depth.
   - Emit counterexamples or replayable UNSAT proofs.

3. **Odd-unit lock miner**
   - Mine repeated phase-collision locks by source/target spine pair and estimate cumulative codimension.

4. **Reserve-source formalization**
   - Translate the five tight reserve cases and the 511 local-grammar records into exact lemmas with side conditions.

5. **Terminal grammar stress expansion**
   - Extend base-depth probes and track whether mixed endpoint buckets persist, split, or regenerate.

6. **Structured prior-art CSV**
   - Convert Lagarias bibliographies + CCChallenge + recent arXiv watchlist into tagged rows so every new idea gets a prior-art collision report.

## Bottom Line

The most boundary-pushing path is not another grand proof sketch.

It is this:

```text
Use false sibling maps and 2-adic ghosts as adversarial controls.
Find the exact value-level feature that positives have and ghosts do not.
Prove that feature survives frontier lift and kills regeneration.
Make every finite step replayable by certificate.
```

That is where the weirdness points. That is the seam worth hitting.

## Sources Touched In This Pass

Local:

- `README.md`
- `status.md`
- `experiments/README.md`
- `experiments/AUDIT-REGISTER.md`
- `experiments/NOVELTY-POSITIONING-2026-07-02.md`
- `experiments/COLLATZ-PURSUIT-CURRENT-STATE-2026-07-02.md`
- `FAILED-ATTEMPTS-WEIRDNESS-ATLAS-2026-07-05.md`
- `experiments/COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md`
- `experiments/COLLATZ-FAILED-ATTEMPTS-ATLAS-2026-07-05.md`
- `experiments/SIBLING-CONTROL.md`
- `experiments/EPSILON-BARRIER.md`
- `experiments/SPINE-LADDER.md`
- `experiments/SPINE-PHASE-COLLISION.md`
- `experiments/FRONTIER-GEOMETRY.md`
- `experiments/ESCAPE-ENVELOPE.md`
- `experiments/KICK-REPULSION-CLAIM-AUDIT.md`
- `experiments/BRANCH-PREFIX-RETIMED-THREE-REGIME-LEDGER.md`
- `experiments/BRANCH-PREFIX-RETIMED-TIGHT-RESERVE-SOURCE.md`
- `experiments/results/INDEX.md`

Public:

- Lagarias annotated bibliography I: https://arxiv.org/abs/math/0309224
- Lagarias annotated bibliography II: https://arxiv.org/abs/math/0608208
- Lagarias overview: https://arxiv.org/abs/2111.02635
- AMS Ultimate Challenge volume: https://bookstore.ams.org/mbk-78
- Tao almost-bounded-values theorem: https://arxiv.org/abs/1909.03562
- Hercher `m <= 91` cycle exclusion: https://arxiv.org/abs/2201.00406
- Barina verification project: https://pcbarina.fit.vutbr.cz/
- Barina 2025 verification article: https://link.springer.com/article/10.1007/s11227-025-07337-0
- Kurtz-Simon generalized undecidability: https://link.springer.com/chapter/10.1007/978-3-540-72504-6_49
- CCChallenge formalization project: https://ccchallenge.org/
- Rozier-Terracol paradoxical sequences: https://arxiv.org/abs/2502.00948
- Angeltveit verification algorithm: https://arxiv.org/abs/2602.10466
- Carelli loop-termination link: https://arxiv.org/abs/2605.15094
- Dhiman-Pandey Buchi non-definability: https://arxiv.org/abs/2602.06066
- Mori operator theory: https://arxiv.org/abs/2411.08084
- Honarvar Shakibaei Asli near-conjugacy: https://arxiv.org/abs/2601.04289
- Williams coordinate system: https://arxiv.org/html/2607.01718v1
- Chang human-LLM Collatz dynamics: https://arxiv.org/abs/2603.11066
