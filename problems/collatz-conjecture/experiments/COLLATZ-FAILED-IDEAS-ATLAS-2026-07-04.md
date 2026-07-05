# Collatz Failed-Ideas Atlas - 2026-07-04

## Purpose

This memo is a no-repeat map for future Collatz work. It collects the major
published and recurring attempted routes, explains how far each route got, why
it has not solved the conjecture, and ranks each by strangeness / weirdness /
"unknown-unknown" value.

It is exhaustive at the **approach-family** level, not a verbatim copy of every
bibliography entry. The paper-level backbone is:

- Jeffrey Lagarias, *The 3x+1 problem: An annotated bibliography
  (1963-1999)*, arXiv:math/0309224. The arXiv abstract says it annotates work
  from 1963 through 1999 and the comments report `197 references`.
- Jeffrey Lagarias, *The 3x+1 Problem: An Annotated Bibliography, II
  (2000-2009)*, arXiv:math/0608208. The abstract describes it as the sequel
  covering 2000 through 2009 plus later preprints by 2009.
- Jeffrey Lagarias, *The 3x+1 Problem: An Overview*, arXiv:2111.02635.
- The Collatz Conjecture Challenge, which frames the literature as dense and
  worth formalising in proof assistants.
- Local companion snapshot:
  `experiments/COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md`,
  a 370-entry scrape/triage table. Treat that file as the paper-level index and
  this file as the no-repeat research map.
- Strategic companion:
  `experiments/COLLATZ-FAILED-ATTEMPTS-IDEA-ATLAS-2026-07-04.md`, a shorter
  route-ranking version with repetition-risk and future-value scores.
- Repo files: `papers.md`, `approaches.md`, `attempts.md`, `status.md`, and the
  2026 experiment notes.

## Rating Keys

`Failure mode` means "why this has not closed Collatz," not "worthless."

`Weirdness`:

```text
1-2 = ordinary number theory / computation
3-4 = standard but subtle
5-6 = structurally interesting
7-8 = genuinely strange / cross-domain
9-10 = beyond-the-beyond: undecidability, 2-adic ghosts, formal equivalence traps
```

`Reuse guidance`:

```text
Avoid      = do not repeat except as baseline
Use        = reusable tool, not proof route by itself
Mine       = useful for generating hard cases or lemmas
Bridge     = promising only if connected to a new invariant
Quarantine = common proof-claim failure mode
```

## High-Level Map

The Collatz conjecture splits into:

```text
no divergent positive orbit
no nontrivial positive cycle
```

Old work has mostly failed in one of these ways:

1. **Average-case trap**: proves almost all / density one / stochastic descent,
   then cannot control the null exceptional set.
2. **Finite-bound trap**: verifies huge ranges or excludes cycles up to huge
   complexity, but leaves the infinite tail.
3. **2-adic trap**: gets beautiful dynamics on `Z_2`, but the positive
   integers are a measure-zero subset.
4. **Parity-word trap**: controls words or residues while losing the intercept
   / positivity information.
5. **Generalization trap**: finds a powerful method that also applies to maps
   where Collatz-like behavior is false or undecidable.
6. **Circular proof trap**: assumes boundedness, descent, or no hidden
   exceptional orbit in disguised form.

## Massive Attempt Atlas

| # | Approach / idea family | Representative papers / people | What it discovered | Why it has not solved Collatz | Weirdness | Reuse |
|---:|---|---|---|---|---:|---|
| 1 | Shortcut map normalization | Terras, Everett, Lagarias surveys | The accelerated map `T(n)=n/2` or `(3n+1)/2` is cleaner than raw `3n+1` | Normalization changes notation, not the hard exceptional set | 2 | Use |
| 2 | Stopping time / finite stopping time | Terras 1976/1979, Everett 1977 | Almost all integers descend below their start | "Almost all" cannot be promoted to "all" | 3 | Use |
| 3 | Natural-density one descent | Terras / Everett line | Density-one convergence-to-lower-start framework | A divergent orbit can live in density-zero set | 4 | Avoid as proof |
| 4 | Lower bounds on convergent set | Krasikov 1989, Krasikov-Lagarias 2003 | Positive lower exponent; large provable convergent population | Exponent below `1` leaves too much room | 3 | Use |
| 5 | Difference inequalities | Krasikov-Lagarias | Converts counting into inequalities / nonlinear programming | Counting still not orbitwise universal | 4 | Mine |
| 6 | Tao logarithmic-density theorem | Tao 2019 | Almost all orbits attain almost bounded values, via 3-adic/random-walk machinery | Log-density almost-all and almost-bounded are both weaker than every orbit reaches `1` | 7 | Bridge |
| 7 | Entropy / information flow | Tao, Lagarias overview | The problem can be reframed as controlling information loss and transport | Entropy methods discard exceptional structured orbits | 7 | Bridge |
| 8 | Skew random walk on `3`-adic cyclic groups | Tao 2019 | Deepest modern analytic machinery; high-frequency estimates matter | Still an average / logarithmic-density theorem | 8 | Mine |
| 9 | Probabilistic negative drift | Lagarias-Weiss, Matthews-Watts, folklore | Explains why conjecture is overwhelmingly plausible | Probabilistic model is not deterministic proof | 3 | Avoid as proof |
| 10 | Markov models | Matthews, Watts, generalized Syracuse work | Gives distributional models and transition statistics | Model states do not certify each integer | 4 | Use |
| 11 | Random parity-vector heuristic | Many surveys | Expected multiplier roughly `3/4` per odd cycle | Independence is false for adversarial orbits | 3 | Avoid |
| 12 | Large deviations / renewal processes | Tao and related analytic routes | Rare trajectories can be quantified statistically | Quantifying rarity is not excluding existence | 6 | Bridge |
| 13 | Benford-law behavior | Kontorovich-Miller, Lagarias-Soundararajan | Collatz values show logarithmic distribution structure | Distributional law, not termination proof | 5 | Use |
| 14 | Maximum excursion statistics | Oliveira e Silva, record-holders papers | Finds extreme records and calibrates models | Records do not bound future records | 4 | Use |
| 15 | Total stopping time / delay records | Roosendaal, Oliveira e Silva line | Catalogs extreme finite orbits | Finite records cannot rule out infinite orbit | 3 | Use |
| 16 | Computational verification | Oliveira e Silva, Roosendaal, Bařina 2020/2025 | Verified all starts below `2^71`; strengthens cycle bounds | Finite range only | 2 | Use |
| 17 | Verification acceleration algorithms | Oliveira e Silva, Bařina, Angeltveit 2026 | Faster exhaustive checking, residue precomputation, ctz/table methods | Still finite computation | 3 | Use |
| 18 | Modular residue sieving | Computational verification literature | Eliminates huge congruence classes at once | Survivor residue set never becomes empty by these methods alone | 4 | Mine |
| 19 | Certificate-frontier descent | Current repo, standard residue-class idea | Exact finite residue classes certify descent | The all-odd `-1` 2-adic boundary survives every depth | 7 | Bridge |
| 20 | Inverse tree / preimage tree | Many Collatz graph papers | Tree of numbers known to reach `1`; rich branching structure | Showing many/preponderance of preimages is not showing all integers appear | 4 | Use |
| 21 | Collatz graph connectivity | Graph-theoretic attempts | Reformulates convergence as reachability to `1` in directed graph | Infinite graph reachability remains original problem | 5 | Avoid as proof |
| 22 | Cycle equation / rational fixed point | Böhm-Sontacchi, Lagarias rational cycles | Exact formulas for cycles and rational/negative cycles | Positive nontrivial cycle exclusion remains infinite Diophantine task | 5 | Use |
| 23 | Negative cycles | Böhm-Sontacchi, Lagarias, ccchallenge summary | Only known integer cycles outside positives: `-1`, `-5`, `-17` | Negative dynamics explain spines but not positive termination | 8 | Bridge |
| 24 | Rational cycles with odd denominator | Lagarias 1985/1990 | Collatz naturally extends beyond integers | Rational periodicity conjecture is itself open/general | 8 | Mine |
| 25 | Continued fractions for `log_2 3` | Steiner, Eliahou, Simons-de Weger, Hercher | Excludes cycles with bounded complexity | Cannot exclude all denominators/lengths | 5 | Use |
| 26 | Baker / linear forms in logarithms | Simons-de Weger, Hercher, transcendence machinery | Huge lower bounds for possible cycle lengths | Constants finite; infinite family remains | 5 | Use |
| 27 | One-cycle exclusion | Steiner 1977 | Rules out simplest nontrivial cycle pattern | Higher cycle structure remains | 3 | Use |
| 28 | `m`-cycle exclusion | Simons-de Weger, Hercher 2023 | No `m`-cycles for `m <= 91`; odd-term floors become enormous with verification | Only bounded `m` | 4 | Use |
| 29 | Eliahou cycle lower bounds | Eliahou 1993 | Very large lower bounds on cycle length | Lower bound, not impossibility | 4 | Use |
| 30 | Luca and related cycle refinements | Luca 2005 and successors | More Diophantine constraints on hypothetical cycles | Still conditional/finite-range style | 4 | Use |
| 31 | Parity vector / cylinder maps | Terras, Everett, Lagarias, current repo | Exact affine map on each parity cylinder | Word data alone loses positivity/intercept | 7 | Bridge |
| 32 | 2-adic conjugacy to shift | Bernstein-Lagarias / Hedlund-style framework | Parity sequence gives a deep symbolic dynamics model | Shift-typical behavior ignores integer subset | 9 | Bridge |
| 33 | Ergodic theory on `Z_2` | Matthews-Watts, Lagarias surveys | Explains measure-preserving / typical behavior | Integers are measure-zero in `Z_2` | 9 | Mine |
| 34 | 3-adic viewpoints | Tao, some modern preprints | `3`-adic mixing appears in strongest theorem | Still not integer-universal | 8 | Mine |
| 35 | Generalized Collatz maps | Conway, Kurtz-Simon | General families can simulate computation / be undecidable | Any general method is suspect; original map may need special arithmetic | 10 | Bridge |
| 36 | Undecidability / `Pi^0_2` completeness | Conway, Kurtz-Simon 2007 | Natural generalized Collatz problem is highly undecidable | Negative warning, not proof/disproof of original | 10 | Mine |
| 37 | Busy-beaver / computation-limits analogies | Modern expository / generalized maps | Shows simple iteration can hide enormous computation | Analogy not proof | 9 | Use cautiously |
| 38 | Automata / formal languages | Various, plus catalog route | Encodes parity languages / residue transitions | Requires sound abstraction; finite automata may miss unbounded arithmetic | 7 | Bridge |
| 39 | Matrix products / semigroups | Many algebraic attempts | Collatz steps as products of affine matrices | Semigroup reachability remains hard | 6 | Mine |
| 40 | Group-theoretic reformulation | Kohl 2015 | Transitivity of certain permutation groups equivalent to Collatz | Beautiful equivalence; transitivity as hard as original | 9 | Mine |
| 41 | Thompson-like / class transposition groups | Kohl | Puts Collatz in simple-group / permutation context | Equivalence does not reduce difficulty yet | 10 | Mine |
| 42 | Residue-class-wise affine groups | Group / RCWA literature | Exact algebra of residue-wise affine maps | Structural equivalence without termination invariant | 8 | Bridge |
| 43 | Functional equations / generating functions | Various older papers | Encodes trajectories into analytic/algebraic objects | Usually re-encodes problem or assumes convergence domain | 6 | Avoid as proof |
| 44 | Complex analytic interpolation | Opfer 2011, other claimed proofs | Attempts to extend Collatz to holomorphic or smooth functions | Famous circularity / hidden assumption failure | 8 | Quarantine |
| 45 | Real-valued smooth extensions | Chamberland-style and successors | Strange real dynamics, cycles, chaotic structure | Real extension has extra dynamics not equivalent to integer problem | 8 | Mine only |
| 46 | Dynamical systems / chaos pictures | Many expository and computational papers | Reveals fractal-like orbit structure and sensitivity | Pictures do not certify integer termination | 6 | Use for intuition |
| 47 | Fractal / self-similarity arguments | Popular and semi-formal attempts | Captures visual recursion of inverse tree | Often proves only visual/statistical self-similarity | 6 | Quarantine if proof claim |
| 48 | Mod `3` one-way gate | Common observation | After initial odd step, odd multiples of `3` behave specially | Local residue fact, not global invariant | 3 | Use |
| 49 | Bit-length descent / branch proofs | Many internet/preprint claims | Tracks binary length changes | Usually averages bit growth or loses rare carry cases | 4 | Quarantine |
| 50 | Peak-value bounds | Schwob-Shiue-Venkat and related algorithmic work | Relations among starts, stopping time, peak values | Helpful telemetry; no universal bound | 4 | Use |
| 51 | Monotone Lyapunov functions | Countless attempts, current repo audits | Would solve divergence if found | Existing candidates either empirical, circular, or fail controls | 8 | Bridge |
| 52 | Potential / repulsion functions | Current repo's withdrawn affine-cocycle claim and similar | Structural credit ideas can be useful | Repulsion events often tautological or insufficient | 8 | Mine with audits |
| 53 | Carry / intercept lemmas | Current repo, parity-cylinder literature | Intercept is where positivity hides | No global carry lemma yet | 9 | Bridge |
| 54 | High-alignment ladder laws | Current repo, classical affine-cylinder substrate | Exact transient dynamics near negative spines | Needs regeneration control after expulsion | 8 | Bridge |
| 55 | Low-repeat `-5 mod 64` gates | Current repo | Sharp local repeat law | Local grammar does not close global frontier | 8 | Bridge |
| 56 | Spine phase-collision / odd-unit lock | Current repo 2026 | Fresh regeneration becomes exact 2-adic congruence | Phase gate alone too permissive; unit codimension theorem missing | 9 | Bridge |
| 57 | Density firewall / coefficient barrier | Current repo + share-thread replication | Barrier survivor density decays rapidly | Density zero is not emptiness | 7 | Bridge |
| 58 | Boundary rays / Mersenne shadows | Current repo and folklore around `-1` | Detects 2-adic ghosts such as all-odd path | Positive finite shadows can track then depart | 9 | Mine |
| 59 | Terminal residue tables | Current repo | Rare endpoints compress into low-bit families | Tables grow / transfer imperfectly with depth | 6 | Use |
| 60 | Adaptive decision trees | Current repo | Efficiently classifies finite endpoint residues | Finite classifier not universal proof | 5 | Mine |
| 61 | SAT/SMT proof search | Algorithm catalog recommendation | Could produce finite UNSAT certificates | Needs exact encoding; bounded only unless lifted | 6 | Bridge |
| 62 | BDD/ZDD compression | Algorithm catalog recommendation | Canonical frontier/lock set operations | Still finite unless paired with induction | 6 | Bridge |
| 63 | CEGAR / abstract interpretation | Algorithm catalog recommendation | Promising structure for infinite bad-trace elimination | Sound abstraction and refinement are hard | 8 | Bridge |
| 64 | E-graphs / rewrite normalization | Algorithm catalog recommendation | Could unify scattered affine formulas | Organizes algebra; does not by itself prove termination | 6 | Use |
| 65 | Proof assistants / formalization | Collatz Conjecture Challenge | Prevents false claims, hardens known lemmas | Formalizing known partial results is not solving conjecture | 7 | Use |
| 66 | Human-LLM collaboration | Chang 2026 and current repo case-study style | Helps generate/review many candidate lemmas quickly | LLM output needs strict proof/audit discipline | 7 | Use cautiously |
| 67 | Kolmogorov / compression arguments | Recurring modern false-proof family | Tries to bound counterexample by description length | Usually category error; no theorem bounds existence this way | 9 | Quarantine |
| 68 | Prompt-as-proof / self-reference claims | Current repo quarantines | Shows how AI-era proof claims can go off rails | Not mathematics | 10 | Quarantine |
| 69 | Empirical matrix contraction | Current repo quarantines and similar | Fits dynamics into contraction model | Fitted contraction is not theorem about true map | 7 | Quarantine |
| 70 | Visual analogy proofs | Bessel graphs, weather graphs, fractal overlays, etc. | Can inspire metaphors | Similar-looking plots do not imply arithmetic implication | 8 | Quarantine |
| 71 | Modular induction on odd/even branches | Common amateur proof route | Tries to split even/odd and recurse | Usually misses that `3n+1` can increase indefinitely before falling | 3 | Quarantine |
| 72 | "All odds handled" reductions | Common false route | Reduces to odd subsequence | Odd subsequence is exactly the hard part | 2 | Quarantine |
| 73 | Inverse-branch coverage claims | Common tree proof route | Shows many branches reach all tested classes | Coverage of infinite set is not proved | 4 | Quarantine |
| 74 | Finite automaton claimed universal | Various low-bit classifiers | Low bits classify many cases | Higher bits can always reintroduce mixed buckets | 6 | Quarantine unless certified |
| 75 | Pure residue-cycle elimination | Many modular attempts | Excludes some cycles/residue classes | No finite modulus captures all integer height/intercept behavior | 5 | Avoid as proof |
| 76 | Algebraic closed-form trajectory formulas | Many papers/preprints | Exact formula from parity vector | Formula depends on unknown parity vector; no termination control | 4 | Use |
| 77 | Predecessor density lower bounds | Tree-counting literature | Many convergent numbers at each depth | Lower bound not total coverage | 4 | Use |
| 78 | Random number generator / cryptographic uses | Applied Collatz papers | Uses chaotic-looking behavior | Application, not proof | 5 | Ignore for proof |
| 79 | Educational / recreational expositions | Veritasium, Quanta, popular pieces | Communicates hardness and current best result | Not primary proof work | 2 | Use as outreach |
| 80 | "Mathematics not ready" obstruction framing | Erdos/Guy/Lagarias overview | Correctly warns against naive attacks | Psychological guidance, not proof | 7 | Use |
| 81 | Arithmetic progressions as sufficient sets | Monks 2006 | Recasts Collatz as covering enough arithmetic progressions | Sufficiency is not an achieved universal cover | 6 | Bridge |
| 82 | Autoconjugacy and shift endomorphisms | Monks-Yazinski, Kraft-Monks | Finds symmetries of the 2-adic parity system | Symmetry does not force positive-integer convergence | 8 | Mine |
| 83 | Base-conversion embeddings | Sterin-Woods, Sterin | Collatz process embeds base conversion / ancestor encodings | Embedding explains complexity; it does not terminate all paths | 9 | Mine |
| 84 | Cellular automata encodings | Korec, Kari, Kari-Kopra, Cloney-Goles-Vichniac | Collatz-like behavior appears inside automata/powers of `p/q` | Encodings often expose hardness instead of reducing it | 9 | Bridge |
| 85 | Automated rewrite-system termination | Yolcu-Aaronson-Heule, Scollo | Termination of selected rewrite systems can be equivalent or related | Full equivalence is as hard as Collatz; weakened systems only prove weakenings | 9 | Bridge |
| 86 | Base `3/2` number systems | Mahler, Eliahou-Verger-Gaugry | Powers of `3/2` and rational-base representations expose the central arithmetic tension | Representation theory alone has not produced a descent invariant | 8 | Mine |
| 87 | `p,q`-adic hybrid analysis | Siegel-style recent work, older 2-adic/3-adic lines | Tries to keep both parity and multiplication structure visible | Risk of proving statements in the completion, not on positive integers | 9 | Bridge |
| 88 | Holomorphic / complex dynamics | Letherman-Schleicher-Wood, Urata, related work | Complex extensions produce rich dynamical systems | Extra complex orbits are not equivalent to integer Collatz | 8 | Mine only |
| 89 | Real continuous dynamics | Chamberland, Misiurewicz-Rodriguez, Konstadinidis | Smooth extensions reveal attracting cycles and chaotic regions | Real dynamics can be false friends for integer dynamics | 8 | Mine only |
| 90 | Directed graph and congruential graph regularity | Andaloro, Urvoy, Zarnowski | Graph regularities and congruence structure help organize computation | Infinite graph reachability is still the problem | 6 | Use |
| 91 | Height / coalescence / consecutive-height studies | Garner, Gao, Wu, Gluck-Taylor | Measures orbit shape and coalescence structure | Shape statistics do not imply universal termination | 5 | Use |
| 92 | Tile/DNA/origami computation routes | Cook-Sterin-Woods, Sterin | Links Collatz encodings to physical/tiling computation | Mostly hardness/encoding context, not a proof path | 9 | Mine |
| 93 | Machine-verified conditional theories | Park-style recent work, proof-assistant ecosystem | Can make conditional reductions exact and auditable | Conditional theory is only as strong as its missing hypothesis | 7 | Use |
| 94 | Recent high-cycle exclusions | Knight 2026, Hercher line | Further walls off possible cycle classes | Still attacks cycles, not divergent orbits | 6 | Use |
| 95 | Claimed proof literature | Bruckman, Cadogan, Ke, Halemane, Novgorodtsev-style entries in the snapshot | Useful corpus of failure patterns and terminology traps | Must not be treated as evidence without independent proof audit | 10 | Quarantine |

## Area Rankings For No-Repeat Planning

| Rank | Area | Weirdness | Current best value | Primary failure wall | Future use |
|---:|---|---:|---|---|---|
| 1 | Generalized Collatz undecidability | 10 | Shows simple-looking affine iteration can simulate computation | Says little directly about ordinary `3x+1` | Negative-control test for overgeneral methods |
| 2 | 2-adic conjugacy / autoconjugacy | 9 | Exact symbolic model of parity dynamics | Positive integers are measure-zero | Pair with positivity/intercept invariant |
| 3 | Rewrite-system equivalence | 9 | Converts Collatz to formal termination / ATP target | Equivalent systems are not easier by default | Generate certified counterexamples to weak lemmas |
| 4 | Base conversion / cellular automata / tilings | 9 | Reveals hidden computational substrate | Mostly re-encoding/hardness | Mine for obstruction examples |
| 5 | Negative/rational cycles and spines | 9 | Shows boundary ghosts are real mathematical objects | Positive exclusion remains open | Use as sibling/control dynamics |
| 6 | Tao entropy / 3-adic stochastic machinery | 8 | Strongest unconditional almost-all theorem | Exceptional set survives | Bridge only with pointwise mechanism |
| 7 | Holomorphic/real extensions | 8 | Imports dynamical-systems tools and pictures | Exact integer restriction usually lost | Intuition only unless equivalence is formal |
| 8 | Diophantine cycle bounds | 6 | Massive finite lower bounds for cycles | Cannot reach infinite lengths alone | Keep as separate cycle module |
| 9 | Computational verification | 3 | Concrete verified floor through huge ranges | Finite by nature | Maintain as evidence, not proof |
| 10 | Claimed proof / pseudo-proof corpus | 10 | Teaches what false closure smells like | Not reliable mathematics | Quarantine and regression-test against it |

## Strangest Discoveries / Unknown-Unknowns

### 1. The `Z_2` Ghost Problem

The 2-adic model makes parity sequences look clean and shift-like, but the
positive integers are a tiny, measure-zero subset. This is the central ghost:
typical 2-adic behavior is not integer behavior.

**Do not repeat:** arguing from `Z_2` typicality to all positive integers.

**Maybe new path:** identify a positivity-specific invariant that survives
inside 2-adic cylinders.

### 2. The Negative Spine Problem

The negative cycles `-1`, `-5`, and `-17` are not side curiosities. They are
periodic 2-adic spines that positive finite shadows can approach transiently.

**Do not repeat:** saying "positive integers cannot be negative cycles" and
thinking that closes the issue.

**Maybe new path:** prove regenerated alignment to later spines requires
odd-unit locks whose codimension accumulates.

### 3. Density Zero Is Not Empty

Almost every strong theorem ends here. Tao's theorem, frontier decay, residue
certificates, stochastic drift, and density-firewall counts all thin the bad set.
None automatically empties it.

**Do not repeat:** treating density-zero survivor sets as no survivors.

**Maybe new path:** combine thinning with a no-infinite-branch theorem.

### 4. Generalized Collatz Is Undecidable

Conway/Kurtz-Simon show that sufficiently general Collatz-like systems can be
computationally universal / undecidable.

**Do not repeat:** building a method so generic that it would also prove false
Collatz-like maps.

**Maybe new path:** exploit constants `2` and `3`, not "piecewise affine maps"
in general.

### 5. Parity Words Are Not Enough

Parity-vector methods are exact and powerful, but parity alone is blind to the
intercept / carry / positivity data.

**Do not repeat:** pure word-statistics proof attempts.

**Maybe new path:** word plus intercept plus finite-support positivity.

### 6. Phase Matching Is Too Permissive

The repo's phase-collision lab found that the phase gate alone allows too many
source-alignment residues.

**Do not repeat:** "phase mismatch kills regeneration."

**Maybe new path:** use the odd-unit lock, not phase matching alone.

### 7. The Retimed Pressure Class

Finite frontier lifts show the hard cases are not arbitrary. They are retimed,
upper-child, structurally prepaid, and split into high-ladder / post-ladder /
low-repeat regimes.

**Do not repeat:** more broad table mining without a theorem target.

**Maybe new path:** prove pre-entry reserve `>= 1` and classify equality.

## No-Repeat Rules For Future Pursuits

1. Do not publish or pursue a proof that only establishes "almost all."
2. Do not treat computation below a bound as a proof beyond the bound.
3. Do not use stochastic independence without proving it for the relevant
   deterministic residue family.
4. Do not rely on parity vectors without the affine intercept.
5. Do not use a smooth/complex/real extension unless the restriction back to
   positive integers is exact and noncircular.
6. Do not claim a finite residue table is universal unless a lift theorem is
   proved.
7. Do not trust a Lyapunov or potential function until it is checked on sibling
   controls such as `3n-1` and `5n+1`.
8. Do not use generalized Collatz arguments unless they exploit the specific
   `2`/`3` arithmetic of the original map.
9. Do not cite unreviewed proof preprints as evidence; use them only as failure
   pattern examples.
10. Do not rebuild an old idea unless we can name the old barrier and the new
    ingredient that crosses it.

## Routes Still Worth Mining

### A. Formal finite falsification

Use SAT/SMT/BDD/ZDD to turn proposed local lemmas into exact finite questions
with counterexamples or certificates.

### B. CEGAR for infinite bad traces

Build abstract states from:

```text
alignment
phase match
odd-unit lock depth
reserve
last credit source
frontier status
low residue bits
```

Then ask whether an infinite accepting bad trace survives. Refine with exact
arithmetic whenever a trace is spurious.

### C. Rewrite rulebook for affine identities

Unify:

```text
spine ladder
phase collision
high ladder
low repeat
post ladder
affine lift
retimed reserve source
```

The goal is to see whether the local retimed equality cases are phase-lock
instances in disguise.

### D. Diophantine cycle handoff

Keep cycle work separate: use continued fractions, Baker bounds, and LLL-style
search only for cycle constraints. Do not confuse this with divergence.

### E. Proof-assistant formalization

Anything that becomes a theorem should be shaped for Lean/Coq/Isabelle-style
formalization, or at least for replayable finite certificates.

## Attempt Families Most Dangerous To Accidentally Repeat

| Danger | Why it seduces | Why it fails |
|---|---|---|
| Probabilistic drift proof | The drift is real and negative | Rare deterministic orbits are not ruled out |
| Density-zero proof | Looks almost solved | Null set can still contain the counterexample |
| Residue table proof | Works beautifully at finite depth | Mixed buckets reappear under lifting |
| Bit-length proof | Easy to measure up/down movement | Carry spikes can erase average descent |
| Complex interpolation proof | Imports powerful analysis | Usually loses equivalence to integer iteration |
| Tree coverage proof | The inverse tree is huge | Need proof every integer appears |
| Cycle lower-bound proof | Bounds become astronomical | Still finite |
| Generalized-map theorem | Feels broad and powerful | Broad class contains false/undecidable maps |
| AI-discovered potential | Fast to generate candidates | Empirical fit is not invariant proof |
| Visual/fractal analogy | The pictures are compelling | Visual similarity is not arithmetic implication |

## What This Means For Our Repo

The current repo direction is not a repeat of the standard failed routes if it
keeps these constraints:

- use spine-ladder and phase-collision as exact affine identities, not visuals;
- treat density/firewall results as thinning only;
- force every finite claim into reproducible scripts and, eventually,
  certificates;
- connect local retimed reserve source to global odd-unit locks;
- test every proposed global potential on sibling controls.

The next non-repeating move is:

```text
phase-lock SAT/SMT exporter
  + affine rewrite rulebook
  + CEGAR bad-trace abstraction
```

That combination directly targets the old barriers instead of rebranding them.

## Source Links

- Lagarias annotated bibliography I: <https://arxiv.org/abs/math/0309224>
- Lagarias annotated bibliography II: <https://arxiv.org/abs/math/0608208>
- Lagarias overview: <https://arxiv.org/abs/2111.02635>
- Collatz Conjecture Challenge story: <https://ccchallenge.org/story>
- Tao 2019: <https://arxiv.org/abs/1909.03562>
- Hercher 2023: <https://arxiv.org/abs/2201.00406>
- Kurtz-Simon generalized undecidability: <https://people.cs.uchicago.edu/~simon/RES/collatz.pdf>
- Bařina verification project: <https://pcbarina.fit.vutbr.cz/>
- Kohl group-theoretic context: <https://stefan-kohl.github.io/articles/collatzgroups.pdf>
