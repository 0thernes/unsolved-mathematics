# Collatz WTF Oddness Field Guide - 2026-07-05

Status: synthesis / route-selection artifact. This is not a proof of Collatz.

Purpose: collect the strangest, most useful, most boundary-pushing findings from
the public Collatz literature and this repo. These are the "pay attention"
signals: the places where the problem stops behaving like a toy iteration and
starts revealing hidden structure.

The rule for future work:

```text
Do not chase a new Collatz idea unless it touches one of these weirdness
frontiers, defeats a named old failure mode, and ships a falsification harness.
```

## Current Reality

The conjecture is still open. The public high-water marks remain:

- Tao: almost all orbits attain almost bounded values, in logarithmic density.
- Barina: computational verification below `2^71`.
- Hercher: no Collatz `m`-cycles with `m <= 91`, giving a huge cycle floor when
  combined with modern verification.
- Generalized Collatz work: broad Collatz-like systems can be undecidable, so a
  successful proof must exploit the specific `3` and `2` arithmetic.
- CCChallenge: the literature is large enough to need formalization; the field
  is moving toward proof-assistant hygiene, not accepting informal proof prose.

The repo's rare asset is not that it proves Collatz. It does not. The rare asset
is a dense, reproducible weirdness lab: exact local identities, sibling controls,
failed proof audits, phase-collision tests, frontier geometry, and retimed
pressure artifacts all living together with their failure walls named.

## Ranking Scale

| Score | Meaning |
|---:|---|
| 10 | Beyond-the-beyond: undecidability, ghost spaces, exact no-go barriers |
| 8-9 | Deeply strange and structurally useful |
| 6-7 | Weird enough to shape theorem targets |
| 4-5 | Important warning / repeat trap |
| 1-3 | Useful but ordinary |

## The Weirdest Findings

| Rank | WTF finding | Where it comes from | Why it is strange | Boundary-pushing use | Risk |
|---:|---|---|---|---|---|
| 1 | Generalized Collatz can be undecidable / `Pi^0_2` complete | Conway; Kurtz-Simon; loop-termination links | Tiny-looking residue-wise affine maps can hide computation | Use as a negative-control test: any method too general is suspect | Overstating this as original Collatz undecidability |
| 2 | The cleanest dynamics live in the wrong universe: `Z_2` | Hedlund / Lagarias / Bernstein-Lagarias; repo frontier work | Every parity word is natural 2-adically, including nonpositive ghosts | Search for a positive-integer separator inside 2-adic cylinders | Treating typical 2-adics as positive integers |
| 3 | The all-odd path survives every finite residue depth | Certificate-frontier theory; `-1` fixed 2-adic point | A finite descent certificate can cover almost everything and still never close | Turn the survivor set into an exact target, not a nuisance | Saying density zero means empty |
| 4 | The survivor frontier has dimension `H(log_3 2) = 0.9499555...` | `FRONTIER-GEOMETRY.md` | The bad set is measure zero but huge as a fractal object | Build envelope and extreme-value tests around this exact dimension | Confusing thin with impossible |
| 5 | `3n+1` and `3n-1` have identical parity-word statistics but opposite truth behavior | `SIBLING-CONTROL.md` | Pure word statistics cannot see the sign of the `+1`/`-1` intercept | Force future proofs to consume intercepts / affine translations | Any epsilon-blind argument is dead on arrival |
| 6 | In `3n-1`, positive cycles sit exactly where Collatz wants no positive survivor | Sibling controls | The same frontier geometry contains `1, 5, 17` in the false sibling | Use sibling maps as proof-sketch lie detectors | Ignoring controls because "Collatz is different" |
| 7 | Tao's theorem uses 3-adic high-frequency mixing and still stops at almost all | Tao 2019 | The strongest modern theorem is both extremely deep and still distributional | Look only for pointwise exceptional-set mechanisms beyond Tao | Publishing weaker almost-all variants |
| 8 | Computational certainty reaches `2^71`, but infinity does not care | Barina 2025; Angeltveit 2026 | The verified floor is astronomical yet logically finite | Use verification for floors, cycle bounds, and test data only | Treating computation as proof |
| 9 | Hercher's cycle wall pushes cycles past absurd size but leaves divergence untouched | Hercher 2023; cycle labs | Cycle-side progress can be enormous and still irrelevant to divergent orbits | Keep cycle work separate from divergence work | Saying "no cycles" when only bounded `m` is excluded |
| 10 | Negative cycles are not trivia; they are 2-adic spine controls | Classical negative dynamics; `SPINE-LADDER.md` | Nonpositive periodic structures organize positive finite shadows | Use them as control spines and sign-blindness detectors | Dismissing them because positives are positive |
| 11 | Supercritical spines are all nonpositive, yet positive shadows can ride them transiently | `SPINE-LADDER.md` | Positivity is not visible from spine algebra alone | Target regenerated alignment after deterministic expulsion | Overclaiming ladder expulsion as global proof |
| 12 | Phase collision has an exact normal form | `SPINE-PHASE-COLLISION.md` | Fresh alignment reduces to a concrete odd-unit congruence lock | Attack regeneration via codimension / entropy / odd-unit locks | Vague "repulsion" language |
| 13 | The phase gate alone is too permissive: allowed fraction about `0.777558620542` | `spine_phase_collision_lab.py` | The obvious phase-mismatch proof target is false in the finite library | Push beyond phase into odd-unit and positivity constraints | Rebranding phase match as proof |
| 14 | The `-1` to `-5` Mersenne lock asks for `3^k == -1 mod 2^e` | Phase-collision lab | Regeneration becomes a powers-of-3 modulo powers-of-2 obstruction | Use as a clean toy model for odd-unit locks | Treating a toy lock as the whole theorem |
| 15 | The boundary-ray positivity sensor grows huge distances | Phase-collision lab | Critical residues do not look like fixed positive integers in low-bit truncations | Track positivity-specific fingerprints | Mistaking a sensor for a proof |
| 16 | Mersenne shadows of `-1` detach at the random-model rate | `FRONTIER-GEOMETRY.md` | The most obvious positive approximants to the ghost show no anomaly | If an anomaly appears, it becomes a genuine signal | Over-reading normal behavior |
| 17 | `5n+1` lights up the same machinery as divergence-typical | `SIBLING-CONTROL.md` | The detector can hear disease in a false sibling | Calibrate every invariant against false maps | Trusting silent instruments without controls |
| 18 | Low alignment has a precise repeat gate: `x == -5 mod 64` | `LOW-ALIGNMENT-STRUCTURE.md` | A local residue explains many prior low-branch failures | Prove regenerated repeat gates cannot persist globally | Treating a finite repeat law as global closure |
| 19 | High alignment has a precise ladder: `x = 2^a q - 1` burns one bit per odd shortcut | `HIGH-ALIGNMENT-LADDER.md` | The high branch has exact algebra, not just heuristics | Use ladder credit in global prefix dominance | Forgetting regenerated ladders |
| 20 | Branch potential has zero failures on large adversarial tests but is still finite evidence | Branch-potential suite | The ledger looks powerful yet remains non-universal | Turn it into a local lift theorem with certificates | "Zero failures" language |
| 21 | Exact frontier lift found a retimed-pressure hard class | Branch-prefix lift suite | Some children need pressure before new total credit appears | Focus proof effort on timing, not aggregate credit | Naive monotone-credit proof |
| 22 | Retimed pressure is dynamic, not a low-bit lookup table | `BRANCH-PREFIX-RETIMED-SIGNATURE.md` | No pure child-residue bucket through modulus `65536` | Prove dynamic algebraic regimes, not fixed tables | More table mining |
| 23 | The retimed class splits into active ladder, post-ladder, and low-repeat regimes | Three-regime ledger | The hard class decomposes exactly after the right lens is used | Prove every layer is paid by these formulas | Losing the regime split in prose |
| 24 | Layer 1 is the induction knife edge | Layer-margin / tight-layer docs | Higher layers have buffer; only first pressure units are tight | Prove the layer-1 base case first | Trying to prove all layers uniformly |
| 25 | Only five surplus-1 tight cases exist in the checked sweep | Tight layer / lift algebra docs | The nastiest local cases are tiny and structured | Classify equality by previous reserve source | Calling five cases a theorem |
| 26 | Local grammar is necessary but wildly insufficient: `511` records, `506` near-misses | Tight grammar docs | The seductive local pattern almost works and still fails | Add minimal-credit / pre-entry reserve conditions | Grammar-only proof |
| 27 | The terminal rare endpoint table is pure at one depth and false as a fixed universal table | Terminal residue/lift docs | Finite purity breaks under deeper sampling, then resolves with more bits | Seek adaptive splitting, not fixed tables | Freezing a lookup table |
| 28 | Adaptive terminal grammar stays sparse as it grows | Terminal tree docs | The hard tail sprouts rare new branches, not chaos everywhere | Prove controlled sparse growth of terminal families | Assuming base-28 closure |
| 29 | Cycle floors are controlled by stubborn rational approximations to `log_2 3` | Cycle-bound / Baker handoff docs | The whole cycle side balances on how well powers of 2 approximate powers of 3 | Keep Diophantine cycle work modular | Mixing cycle and divergence arguments |
| 30 | The near-miss cycle denominators are themselves stress objects | Cycle labs | Continued-fraction denominators become concrete obstruction landmarks | Use them to test any cycle-side claim | Treating "astronomically unlikely" as impossible |
| 31 | Claimed proofs fail in repeatable archetypes | `attempts.md`; no-repeat atlases; Opfer-style history | False proofs are patterned, not random | Turn archetypes into automated QA checks | Being impressed by polished prose |
| 32 | LLMs can generate both useful theorem targets and fluent false bridges | Share ingest; failed-attempts atlases | The workflow is new; the validation problem is old | Use models for search, never as proof authority | Prompt-as-proof |
| 33 | CCChallenge shows the literature is not just big; it is underformalized | ccchallenge.org | 370 entries, tiny formalized fraction | Formalize accepted lemmas and proof obligations | Treating informal consensus as machine-checkable |
| 34 | Rewrite-system termination can be equivalent to Collatz | Yolcu-Aaronson-Heule line; CCChallenge entry | Automated theorem proving can touch meaningful weakenings | Generate certified weakenings and counterexamples | Thinking equivalence makes it easier |
| 35 | Operator algebra, `p,q`-adic, polynomial, and geometric analogues keep appearing | 2024-2026 literature sweep | Collatz casts shadows in many mathematical languages | Mine analogues for falsifiers and invariants | Mistaking a new language for progress |

## The Five Deep Walls

| Wall | What it blocks | What would count as progress |
|---|---|---|
| Exceptional-set wall | Density, probability, and Tao-style almost-all methods | A pointwise theorem excluding the null exceptional set |
| 2-adic ghost wall | Parity-word and residue arguments | A positivity / finite-support invariant inside 2-adic cylinders |
| Intercept wall | Epsilon-blind word statistics | A proof that consumes the `+1` affine translation, not just words |
| Regeneration wall | Spine-ladder and branch-credit programs | A theorem bounding fresh alignment after expulsion or lift |
| Finite-to-infinite wall | Computation, tables, and local grammars | Certificates or induction proving all lifts, not sampled depths |

## What Looks Most 1/1 In This Repo

The following are not claims of literature priority. They are the strongest
repo-native directions that are unusual enough to keep:

| Candidate | Why it feels special | Exact next obligation |
|---|---|---|
| Epsilon-invariance barrier with sibling controls | It turns "word statistics are insufficient" into a controlled no-go statement | Formalize the theorem and keep every new proof sketch sibling-tested |
| Phase-collision odd-unit lock | It names regeneration as a concrete 2-adic congruence problem | Prove a codimension/positivity theorem for repeated locks |
| Retimed reserve-source induction | It reduces a messy lift problem to prepaid one-unit pressure | Prove pre-entry reserve `>= 1` and classify equality |
| Adaptive terminal grammar | It replaces brittle finite tables with sparse controlled growth | Prove mixed endpoint parents resolve after finite lifting |
| Branch-prefix dominance | It upgrades terminal credit accounting to prefix-local debt control | Prove the local lift lemma over the whole survivor frontier |
| Weirdness atlas / proof-claim quarantine workflow | It preserves failures as useful evidence instead of deleting them | Convert rows into automated anti-repeat checks |

## Immediate Research Program

### 1. Build a WTF regression suite

Every new idea should be tested against:

```text
Collatz records
Mersenne shadows 2^k - 1
low-repeat shadows 2^k q - 5
high-ladder states 2^a q - 1
3n-1 cycles {1,5,17}
5n+1 divergence-typical starts
phase-collision odd-unit locks
retimed surplus-1 records
claimed-proof archetype rows
```

### 2. Convert weirdness into theorem targets

Do not ask "does this look true?" Ask:

```text
Which wall does it attack?
Which sibling map should break it?
Which finite class can falsify it?
Which old row does it avoid repeating?
Which exact local identity is being consumed?
```

### 3. Keep the frontier split clean

Cycle work belongs with Diophantine approximation and `log_2 3`.
Divergence work belongs with exceptional sets, 2-adic ghosts, intercepts, and
regeneration. Mixing them is one of the oldest ways to fool ourselves.

## Source Backbone

Primary external anchors checked or reused:

- Lagarias bibliography I: <https://arxiv.org/abs/math/0309224>
- Lagarias bibliography II: <https://arxiv.org/abs/math/0608208>
- Lagarias overview: <https://arxiv.org/abs/2111.02635>
- Collatz Conjecture Challenge: <https://ccchallenge.org/>
- Tao 2019: <https://arxiv.org/abs/1909.03562>
- Hercher 2023: <https://arxiv.org/abs/2201.00406>
- Barina project / verification: <https://pcbarina.fit.vutbr.cz/>
- Barina 2025 Springer article: <https://link.springer.com/article/10.1007/s11227-025-07337-0>
- Angeltveit 2026 verification algorithm: <https://arxiv.org/abs/2602.10466>
- Carelli 2026 loop termination link: <https://arxiv.org/abs/2605.15094>
- Kurtz-Simon generalized undecidability: <https://people.cs.uchicago.edu/~simon/RES/collatz.pdf>

Primary local anchors:

- `status.md`
- `FAILED-ATTEMPTS-WEIRDNESS-ATLAS-2026-07-05.md`
- `experiments/COLLATZ-FAILED-ATTEMPTS-ATLAS-2026-07-05.md`
- `experiments/COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md`
- `experiments/SPINE-LADDER.md`
- `experiments/SPINE-PHASE-COLLISION.md`
- `experiments/SIBLING-CONTROL.md`
- `experiments/FRONTIER-GEOMETRY.md`
- `experiments/BRANCH-PREFIX-RETIMED-*.md`
- `experiments/LOW-ALIGNMENT-STRUCTURE.md`
- `experiments/HIGH-ALIGNMENT-LADDER.md`
- `experiments/AFFINE-COCYCLE-CLAIM-AUDIT.md`
- `experiments/AUDIT-REGISTER.md`

## Bottom Line

The most useful weirdness is not spectacle. It is the precise places where
Collatz almost yields and then refuses:

```text
almost all, but not all
finite cover, but not infinite lift
parity exact, but sign-blind
spine expulsion, but fresh regeneration
pure table, but unstable under depth
AI-generated insight, but not proof
```

That is the engine. Future work should live there.
