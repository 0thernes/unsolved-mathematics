# Collatz Algorithm Catalog Triage - 2026-07-04

## Source

User-supplied attachment:

```text
[redacted-local-session-attachment]/pasted-text.txt
```

The attachment is titled **The 1000 Algorithms, Categories, and Domains** and
claims catalog version `0.9.13-local`.

Parsed shape of the 1000-row catalog:

| Engine | Rows | Collatz value | Use policy |
|---|---:|---|---|
| `logic` | 122 | Very high | Proof search, exact encodings, counterexample mining |
| `automata` | 35 | Very high | Parity languages, frontier states, lift transitions |
| `sketch` | 70 | High | Compression of large frontier families; measurement only unless exact |
| `parsing` | 50 | Medium-high | Grammar extraction for parity words and residue motifs |
| `probability` | 122 | Medium | Model checking against random-walk heuristics; not proof by itself |
| `graph` | 135 | Medium | State-space search and dependency graphs |
| `optimization` | 104 | Medium-low | Heuristic search for hard cases; weak proof value |
| `undecidable` | 20 | Medium-low | Conceptual framing; mostly not an actionable proof path |
| `topology` | 64 | Low-medium | Useful only for specific state-space geometry or visualization |
| `flow` | 60 | Low-medium | Potential for dependency/obstruction networks |
| `crypto` | 79 | Low | Integrity/provenance tooling, not Collatz mathematics |
| `distributed` | 85 | Low | Large-run infrastructure, not mathematical leverage |
| `quantum` | 44 | Very low | Mostly distraction for this problem |
| `evolution` | 10 | Very low | Heuristic only |

## Verdict

Yes, the catalog helps, but only after aggressive filtering.

It is not a Collatz proof source. It is a method inventory. Most entries are
irrelevant to the current mathematical wall. The useful subset is the formal
methods / automata / symbolic-search cluster that can attack the repo's exact
open target:

```text
spine phase-collision odd-unit locks
  + retimed frontier-lift reserve-source induction
  + density-zero survivor frontiers
```

The right use is not "try 1000 algorithms." The right use is to build a small
arsenal of proof-search and falsification tools around the current bottleneck.

## Scoring Rule

| Score | Meaning |
|---:|---|
| 5 | Produces exact proof obligations, unsat cores, formal certificates, or exhaustive finite evidence |
| 4 | Compresses or normalizes exact Collatz structures without changing the mathematics |
| 3 | Discovers patterns that later need exact verification |
| 2 | Helps visualization, performance, or corpus organization only |
| 1 | Mostly aesthetic or unrelated |
| 0 | Actively likely to create noise or overclaiming |

Noise risk is scored in the opposite direction: `1` is low risk, `5` is high
risk. No method is allowed to upgrade a mathematical claim unless it produces
an exact witness, exact count, replayable certificate, or counterexample.

## Current Bottleneck

The repo's latest durable state is:

- [`SPINE-PHASE-COLLISION.md`](SPINE-PHASE-COLLISION.md): regeneration is an
  exact phase-collision plus odd-unit congruence-lock problem.
- [`COLLATZ-PURSUIT-CURRENT-STATE-2026-07-02.md`](COLLATZ-PURSUIT-CURRENT-STATE-2026-07-02.md):
  Round 20 file-dependent claims are not accepted; density-zero is not
  emptiness; the bridge target is phase locks plus retimed reserve-source
  induction.
- Retimed-reserve series: local frontier lifts show structural credit and
  tight reserve-source patterns, but the universal induction is not proved.

Any catalog method is useful only if it helps one of these:

1. prove no infinite positive bad path survives;
2. prove odd-unit locks accumulate codimension faster than survivor entropy;
3. prove every retimed lift has pre-entry reserve at least `1`;
4. produce certified counterexamples to proposed lemmas;
5. emit machine-checkable certificates for finite claims.

## Highest-Leverage Methods

| Rank | Catalog method(s) | Collatz target | Expected output | Proof relevance |
|---:|---|---|---|---|
| 1 | SAT / CDCL / SMT / AllSAT / MaxSAT / QBF | Encode finite phase-lock, reserve-source, and low-bit survivor constraints | counterexample assignment, UNSAT core, or certificate | Very high for finite lemma falsification |
| 2 | BDD / ZDD family compression | Compress survivor-frontier and lock-residue families | canonical finite set representation, exact counts, inclusion tests | Very high for frontier structure |
| 3 | Abstract interpretation + CEGAR | Build a finite abstraction of infinite positive orbits using alignment, reserve, phase, and residue features | abstract bad trace or proof after refinements | Very high for the divergence half |
| 4 | Buchi automata emptiness / parity games / model checking | Treat infinite bad orbits as omega-regular traces over abstract states | accepting cycle or emptiness witness | Very high if abstraction is sound |
| 5 | E-graphs / equality saturation / Knuth-Bendix / superposition | Normalize affine Collatz identities, high-ladder laws, low-repeat laws, and phase-collision equations | rewrite system, canonical forms, missing critical pairs | High for theorem organization |
| 6 | LLL lattice reduction / continued-fraction tooling | Cycle equation side: control `2^d - 3^o` and near coincidences | sharper cycle obstruction probes | High, but mostly cycle-side |
| 7 | DRAT / LRAT / proof certificates / proof by reflection | Make finite SAT/SMT/BDD claims independently checkable | replayable proof certificate | High for credibility, not discovery |

## Why These Fit

### SAT / SMT / AllSAT

Use for finite lock and lift claims. Examples:

```text
Given depth d and residue width R, is there a positive finite shadow that:
  - survives the certificate frontier;
  - enters a matched phase collision;
  - avoids all known high-ladder / low-repeat reserve sources;
  - keeps prefix deficit nonnegative?
```

If satisfiable, the model is a new hard family or a lemma refutation. If
unsatisfiable, a DRAT/LRAT or SMT certificate can harden the finite claim.

### BDD / ZDD

Use for exact symbolic sets:

```text
frontier residues
phase-matched residues
odd-unit lock residues
retimed lift children
tight reserve-source cases
```

This could replace ad hoc JSON tables with canonical set operations:
intersection, projection, difference, lift, and emptiness.

### Abstract Interpretation / CEGAR

This is the best match for the real proof gap. A first abstraction could track:

```text
alignment bucket
source spine family
target spine family
phase match flag
odd-unit lock depth
prefix reserve
last credit source
frontier status
```

The CEGAR loop:

```text
1. abstract infinite orbit space;
2. find abstract bad trace;
3. replay concretely with exact Collatz arithmetic;
4. if spurious, refine by the missing residue/phase/reserve predicate;
5. repeat until a real counterexample family appears or no accepting trace remains.
```

This is not a proof by itself, but it is the cleanest way to turn the current
human-led pattern mining into a falsifiable theorem engine.

### Automata / Omega Automata

The survivor problem is naturally language-like: parity words, finite shadows,
frontier lifts, and infinite bad paths. Model checking becomes useful when we
can make a sound finite abstraction.

The target question:

```text
Does the abstract transition system contain an accepting cycle that keeps a
positive orbit in the survivor frontier while avoiding enough odd-unit-lock
codimension and reserve credit?
```

An accepting cycle is either a real obstruction candidate or a spurious trace
that tells us which invariant is missing.

### Rewriting / E-Graphs

The repo now has several overlapping exact identities:

```text
T^t(x)-eta = 3^a 2^(m-t)u + (rho_t-eta)
x = 2^a q - 1 high ladder
x == -5 mod 64 low-repeat gate
OOE(x) = (9x + 5)/8
EOO(y) = (9y + 10)/8
T^j(child)-T^j(parent)=3^o_j 2^(d-j)
```

An e-graph or rewrite system can expose whether the retimed reserve-source
formulas are just local projections of the phase-collision lock. This is
exactly the bridge target.

### LLL / Diophantine Tools

Useful mostly for cycles. It does not solve divergence. It can still sharpen:

```text
2^d - 3^o
cycle fixed-point denominators
near-critical convergents of log_2(3)
```

This belongs beside the cycle-bound lab, not the regeneration lab.

## Medium-Leverage Methods

| Catalog method(s) | Useful for | Why not primary |
|---|---|---|
| Genetic algorithms / CMA-ES / simulated annealing | Mining hard residue families or candidate invariants | heuristic only; no proof without exact follow-up |
| Monte Carlo / reservoir sampling / sketches | large-scale telemetry over orbit families | estimates cannot close a null exceptional set |
| Graph SCC / max-flow / reachability | finite transition graph analysis | useful after a sound state graph exists |
| Symbolic execution / weakest preconditions | verifying the experiment scripts and extracting path conditions | supports tooling more than math |
| Craig interpolation / unsat cores | deriving candidate invariants from failed SAT instances | powerful if the SAT encoding is good |
| TLA+ / Petri nets / timed automata | checking pipeline/process invariants | mostly engineering hygiene |

## Low-Leverage For The Proof

These may help presentation, apps, or visualization, but they are not currently
proof-relevant:

- sorting algorithms;
- quantum algorithms such as Shor/Grover/QAOA;
- distributed consensus protocols;
- cryptographic primitives except proof-certificate machinery;
- procedural graphics/noise/generative systems;
- generic ML training algorithms;
- visualization families unless attached to exact data.

The catalog's `Collatz Function Iteration` entry is not itself useful beyond
reminding us that general Collatz-like systems touch undecidability. The proof
must exploit the specific arithmetic of `3n+1`, not generic iteration.

## Concrete Build Queue

### A. Lock-SAT Exporter

File target:

```text
experiments/collatz_phase_lock_sat_export.py
```

Purpose:

```text
Export bounded phase-collision / odd-unit-lock instances as CNF or SMT-LIB.
```

First falsifiable question:

```text
At fixed source/target spine depth and modulus R, can a positive finite shadow
match phase and avoid all known reserve-source predicates?
```

Expected outputs:

```text
experiments/results/phase_lock_sat_d*_r*_20260704.json
experiments/results/phase_lock_sat_d*_r*.smt2
```

### B. Retimed CEGAR Prototype

File target:

```text
experiments/collatz_retimed_cegar.py
```

Purpose:

```text
Model frontier-lift transitions using abstract states:
(phase, alignment_bucket, reserve_bucket, last_credit_source, low_bits).
```

First falsifiable question:

```text
Can the abstraction produce an infinite path with reserve < 1 before final
align-3 entry?
```

### C. Affine Rewrite / E-Graph Rulebook

File target:

```text
experiments/COLLATZ-AFFINE-REWRITE-RULEBOOK.md
```

Purpose:

```text
Canonicalize all exact formulas currently scattered across spine ladder,
phase collision, high ladder, low repeat, post ladder, and affine lift notes.
```

First falsifiable question:

```text
Do the retimed equality cases reduce to phase-collision odd-unit locks under a
common rewrite basis?
```

### D. BDD/ZDD Frontier Set Compressor

File target:

```text
experiments/collatz_frontier_zdd_probe.py
```

Purpose:

```text
Represent survivor residues, phase-matched residues, and reserve-source
residues as canonical decision diagrams.
```

First falsifiable question:

```text
Does the set difference "phase matched but no reserve source" shrink, stabilize,
or reproduce under depth lift?
```

## Immediate Recommendation

Start with **A + C**:

1. `collatz_phase_lock_sat_export.py` gives a hard falsification engine.
2. `COLLATZ-AFFINE-REWRITE-RULEBOOK.md` prevents the algebra from fragmenting.

Then add **B** only after the finite SAT/SMT predicates are stable. CEGAR is
where this could become genuinely theorem-shaped, but only if the predicates
are exact.

## Bottom Line

The 1000-item catalog helps as a disciplined search lens. Its useful core is
roughly 20 methods, not 1000. The valuable direction is:

```text
formalize finite lock/reserve claims
  -> emit counterexamples or certificates
  -> abstract infinite traces
  -> refine until the bad path either becomes real or disappears
```

That fits the repo's current state. It is still exploratory, but it is the
right kind of exploratory: exact, falsifiable, and capable of producing either
new hard data or machine-checkable negative results.
