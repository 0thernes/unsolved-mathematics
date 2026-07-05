# Collatz Failed-Attempts And Weirdness Atlas - 2026-07-05

Purpose: keep future Collatz work from accidentally rediscovering old terrain.

This is not a claim that every paper in the full Collatz literature has been
individually reviewed here. Jeffrey Lagarias's annotated bibliographies are the
literal bibliography backbone. This file is the no-repeat map: families of
ideas, representative papers, what each family actually achieved, why it did
not prove the conjecture, and what strange residue it left behind.

Companion artifacts:

- Detailed 150-family atlas:
  [`experiments/COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md`](experiments/COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md).
- Paper-level CCChallenge scrape:
  [`experiments/COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md`](experiments/COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md).

## Coverage Snapshot - 2026-07-05

This pass refreshed the atlas against the main live/public spines: Lagarias's
annotated bibliographies and overview, CCChallenge, Tao's almost-bounded-values
paper, Barina's 2025 verification record, Knight's high-cycle result,
Angeltveit's 2026 verification algorithm, Kurtz-Simon generalized undecidability
work, and proof-claim/retraction examples such as Opfer 2011.

Local coverage now has four layers:

| Layer | File | Coverage role |
|---|---|---|
| User-facing no-repeat map | This file | 65 attempt families plus weirdness ranking and practical novelty filter |
| Detailed scored atlas | [`experiments/COLLATZ-FAILED-ATTEMPTS-ATLAS-2026-07-05.md`](experiments/COLLATZ-FAILED-ATTEMPTS-ATLAS-2026-07-05.md) | 70 scored attempt rows, including repo-specific routes and pseudo-proof archetypes |
| Deep idea-family atlas | [`experiments/COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md`](experiments/COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md) | 150 idea-family rows, 160 numbered table rows, failure modes, and future-use guardrails |
| Literature snapshot | [`experiments/COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md`](experiments/COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md) | 370 CCChallenge bibliography rows captured for later structured tagging |

Honesty boundary: this is exhaustive as an anti-repeat research map, not a
formal certification that every Collatz paper ever written has been individually
read. Future novelty claims should cite the nearest row here and state the
specific old failure mode they defeat.

## Source Backbone

Use these as the canonical literature spines before claiming novelty.

| Source | Coverage | Why it matters |
|---|---|---|
| Lagarias, ["The 3x+1 problem: An annotated bibliography (1963-1999)"](https://arxiv.org/abs/math/0309224), arXiv:math/0309224 | 197 references through 1999 | The primary pre-2000 bibliography. |
| Lagarias, ["The 3x+1 Problem: An Annotated Bibliography, II (2000-2009)"](https://arxiv.org/abs/math/0608208), arXiv:math/0608208 | 134 entries in v6 | The sequel bibliography for 2000-2009 plus some later preprints. |
| Lagarias, ["The 3x+1 Problem: An Overview"](https://arxiv.org/abs/2111.02635), arXiv:2111.02635 | Survey overview, published in the AMS volume | The shortest professional map of what was known by the 2010 survey era. |
| Lagarias (ed.), [The Ultimate Challenge: The 3x+1 Problem](https://bookstore.ams.org/mbk-78), AMS, 2010 | Surveys, early papers, stochastic/computational chapters, bibliography | The standard book-length reference. |
| [Lagarias's University of Michigan 3x+1 page](https://websites.umich.edu/~lagarias//3x%2B1.html) | Curated papers by Lagarias and collaborators | Reliable source for rational cycles, trees, conjugacy, stochastic models, semigroup papers. |
| [CCChallenge](https://ccchallenge.org/) | Live formalization-oriented bibliography; local snapshot has 370 rows | Best current source for broad paper discovery and proof-assistant/formalization status. |
| Tao, ["Almost all orbits of the Collatz map attain almost bounded values"](https://arxiv.org/abs/1909.03562), arXiv:1909.03562 / Forum Math. Pi | Strongest modern density theorem | Essential ceiling on what "almost all" currently means. |
| Hercher, ["There are no Collatz m-Cycles with m <= 91"](https://arxiv.org/abs/2201.00406), arXiv:2201.00406 / JIS 2023 | Current m-cycle exclusion frontier | Important for cycle-side claims and computational thresholds. |
| Barina, [verification project](https://pcbarina.fit.vutbr.cz/) and [2025 J. Supercomputing record](https://www.fit.vut.cz/research/result/c197809/.en) | Verification to n < 2^71 as of 2025-01-15 | Current empirical floor and input to cycle lower bounds. |
| Recent 2025-2026 preprints | [Rozier/Terracol paradoxical sequences](https://arxiv.org/abs/2502.00948), [Angeltveit verification algorithm](https://arxiv.org/abs/2602.10466), [Chang LLM-collaboration reductions](https://arxiv.org/abs/2603.11066), [Carelli loop termination links](https://arxiv.org/abs/2605.15094), [Knight high cycles](https://hal.science/hal-04261183v1) | Watchlist material: useful leads, not settled proof paths. |

## Reading Of "Failed"

"Failed" here means "failed to prove Collatz." It does not mean bad work. Many
rows are excellent mathematics. Their failure mode is exactly what we need to
remember: density is not universality, computation is not infinity, a
reformulation is not a proof, and a generalized theorem may be blind to the
specific constants 3 and 2.

## Scales

| Scale | Meaning |
|---|---|
| Weirdness 1-10 | How strange / beyond-the-beyond the leftover phenomenon is. |
| Saturation 1-5 | How heavily this approach has already been tried. 5 means "assume prior art until proven otherwise." |
| Future value | Block, Watch, Reuse, or Attack. |

## Executive Verdict

The most saturated old ideas are:

1. elementary descent by average drift;
2. parity-vector and residue-class enumeration;
3. finite computational verification;
4. cycle exclusion by continued fractions / linear forms in logarithms;
5. inverse tree coverage;
6. 2-adic "almost every" arguments;
7. real/complex/holomorphic extensions;
8. claimed proofs by reformulation.

The most valuable still-open weird residues are:

1. the integer line is a measure-zero exceptional set inside the 2-adic model;
2. every finite parity word occurs, so local patterns alone cannot forbid bad behavior;
3. generalized Collatz families are undecidable, so any universal method is suspect;
4. Tao reaches almost bounded values for logarithmic almost all integers but not every orbit;
5. cycles are forced to absurd size if they exist, yet no infinite-length exclusion is known;
6. continuous extensions can behave unlike the integers, including extra fixed points or escape;
7. Collatz-like siblings can share statistics while having totally different positive cycles;
8. paradoxical sequences and permutation patterns show hidden finite structure that still does not yield a global invariant.

## Weirdness Leaderboard

| Rank | Weird residue | Score | Why it matters |
|---|---:|---:|---|
| 1 | Generalized Collatz maps can simulate computation; some universal questions are Pi^0_2-complete. | 10 | Any proof method that is too general should be distrusted. The proof must consume special 3x+1 structure. |
| 2 | 2-adic dynamics is measure-theoretically clean, but positive integers are an exceptional zero-measure subset. | 10 | Explains why beautiful ergodic statements miss the actual hard set. |
| 3 | Tao's theorem pushes "almost all" extremely far, yet an arbitrarily thin exceptional set may still contain all counterexamples. | 9 | The strongest partial result exposes the main gap with high precision. |
| 4 | A nontrivial cycle would need at least about 1.375e11 odd terms under current cycle/verification data. | 9 | The cycle side is almost physically absurd, but still not logically impossible. |
| 5 | Every finite parity vector occurs for exactly one residue class modulo 2^k. | 9 | No finite pattern is intrinsically forbidden; local symbolic arguments are dangerous. |
| 6 | Continuous/holomorphic extensions produce alien dynamics not equivalent to the integer problem. | 8 | Smooth pictures are seductive and often irrelevant. |
| 7 | Paradoxical sequences can locally exceed what their odd/even ratio suggests; finiteness of such behavior would imply strong consequences. | 8 | A current "strange finite obstruction" line worth watching, not proof. |
| 8 | Collatz permutation patterns are Fibonacci-like up to a point, then excess patterns appear. | 7 | Finite combinatorial order emerges, then breaks. Good warning against small-depth pattern worship. |
| 9 | Busy-beaver / program-complexity encodings can connect Collatz-like statements to enormous computational hardness. | 9 | A philosophical warning: "simple to state" can hide impossible search depth. |
| 10 | The inverse tree seems to cover everything empirically, but a proof of coverage is essentially the conjecture. | 8 | Many false proofs die here. |
| 11 | Benford/log-distribution behavior appears in iterates but does not control worst cases. | 6 | Statistical regularity is real but proof-weak. |
| 12 | Modular graph reductions often reveal exact bijections and spectral gaps without closing orbitwise mixing. | 7 | A useful modern tool, but orbit-level bias remains. |

## No-Repeat Matrix

| # | Attempt family | Representative sources | What worked | Why it did not prove Collatz | Weird residue | Saturation | Future value |
|---:|---|---|---|---|---|---:|---|
| 1 | Direct brute-force verification | Oliveira e Silva; Barina 2020, 2025; Angeltveit 2026 | Verified enormous initial intervals; current public floor n < 2^71. | Infinity remains. Counterexamples may be larger. | Smallest counterexample, if any, is beyond astronomical verified range. | 5 | Reuse |
| 2 | Optimized search/sieving programs | Leavens-Vermeulen 1992; Oliveira e Silva; Barina; Angeltveit | Faster exact checking; reduced work per interval. | Verification algorithms do not create a uniform theorem. | Hardware-scale truth without theorem-scale truth. | 5 | Reuse |
| 3 | Record-holder tables for delay/max excursion | Oliveira e Silva; Roosendaal; OEIS records | Found extreme stopping-time and peak examples. | Records suggest behavior but cannot exclude non-record counterexamples. | Rare records dominate intuition. | 4 | Reuse |
| 4 | Stopping-time density | Terras 1976/1979; Everett 1977 | Almost all integers drop below their start. | Almost all is not all. Exceptional set may contain a divergent orbit. | The first major theorem already shows the main trap. | 5 | Attack only with new exceptional-set control |
| 5 | Coefficient stopping time | Terras; Garner; modern coefficient-stopping preprints | Separates coefficient drop from actual descent. | Equality of coefficient and actual stopping time remains open. | Coefficient says "should drop" while intercept can still interfere. | 4 | Watch |
| 6 | Krasikov inequalities / difference inequalities | Krasikov 1989; Krasikov-Lagarias 2003 | Proved a lower bound about x^0.84 for numbers reaching 1. | Exponent less than 1 leaves a huge exceptional complement. | Computer-aided inequalities extract much but not all density. | 5 | Reuse for bounds, not proof |
| 7 | Tree-search density bounds | Applegate-Lagarias 1995 | Improved lower-density machinery via inverse trees. | Tree coverage cannot be promoted to all integers. | The inverse tree looks full but has no global certificate. | 5 | Reuse |
| 8 | Tao entropy / almost bounded values | Tao 2019/2022 | For any f(n)->infinity, almost all orbits attain values <= f(n) in logarithmic density. | Logarithmic almost all and almost bounded still miss universality and boundedness. | Best theorem leaves a thin abyss. | 5 | Attack only beyond Tao's exceptional-set barrier |
| 9 | Stochastic random-walk heuristics | Lagarias-Weiss 1992; Kontorovich-Lagarias 2010 | Explains negative drift and expected convergence. | Randomness is not a proof for deterministic worst cases. | The heuristic is too convincing and therefore dangerous. | 5 | Reuse for intuition |
| 10 | Benford-law/log-distribution methods | Kontorovich-Miller 2005; Lagarias-Soundararajan 2006 | Quantified digit/statistical behavior in iterates. | Distributional laws do not force every orbit to descend. | Iterates look statistically natural without giving an invariant. | 4 | Watch |
| 11 | Markov chains for generalized maps | Matthews-Watts; Matthews survey | Gives ergodic/probabilistic structure for generalized Syracuse maps. | Model typicality does not settle the specific integer orbit problem. | Markov clarity coexists with integer opacity. | 4 | Reuse |
| 12 | 2-adic extension | Hedlund; Lagarias; Wirsching | Extends dynamics to Z_2 and encodes parity sequences. | Z_2 almost-everywhere statements miss positive integers as a special subset. | The natural completion makes the hard set measure zero. | 5 | Attack only with integer-subset theorem |
| 13 | 2-adic conjugacy map | Bernstein-Lagarias 1996 | Conjugates Collatz dynamics to a shift on Z_2; studies finite permutations. | Conjugacy explains symbolic freedom; it does not imply positive integer convergence. | Perfect symbolic order, no descent invariant. | 5 | Reuse |
| 14 | Non-iterative 2-adic reformulations | Bernstein 1994 and related | Rephrases the conjecture in 2-adic terms. | Equivalent reformulation does not reduce difficulty by itself. | A crisp alternate statement that is still hard. | 4 | Watch |
| 15 | Rational cycles | Lagarias 1990; Bohm-Sontacchi tradition | Parameterized rational cycles and periodic points. | Positive integer cycles remain unexcluded at all lengths. | Many rational/2-adic ghosts around one integer cycle question. | 4 | Reuse |
| 16 | 1-cycle and m-cycle exclusion | Steiner; Simons; Simons-de Weger; Hercher | Excluded increasingly complex classes of cycles, now m <= 91. | Still finite m. No proof for arbitrary m. | Hypothetical cycles are forced into monstrous complexity. | 5 | Reuse |
| 17 | Linear forms in logarithms / continued fractions | Baker/Rhin machinery; Eliahou; Simons-de Weger; Hercher | Gives lower bounds on cycle length and constraints from log_2(3). | Constants and verified floors grow but never become infinity. | Cycles require extreme Diophantine near-misses. | 5 | Reuse |
| 18 | Few-descents / high-cycle work | Brox; Chisala; Garner; Knight 2026 high cycles | Excludes special cycle shapes. | Special shapes do not cover all cycles. | Certain "obvious" cycle geometries are impossible. | 4 | Watch |
| 19 | Modular residue sieves | Many classic and amateur lines; Garner; modern graph preprints | Finds forbidden/required residue behavior. | Finite moduli cannot see infinite orbit balance unless lifted uniformly. | Local congruence order keeps regenerating at larger modulus. | 5 | Block unless new lift theorem |
| 20 | Congruence-class trees | Terras-style residue classes; Winkler-style deterministic structures | Exact classes for finite parity/stopping data. | Finite congruence coverage stops before global stopping-time equality. | Every finite word has a class, including scary ones. | 5 | Watch |
| 21 | Inverse Collatz tree coverage | Classic inverse tree, tree trunk/branch claims | Generates all known convergent integers from 1. | Showing every integer is in the tree is the conjecture. | The tree is a proof-shaped mirage. | 5 | Block unless coverage theorem is noncircular |
| 22 | Graph-theoretic Collatz diagrams | Andaloro; Kimms; many graph reformulations | Reveals structure in reverse graph and components. | Graph connectivity to root is equivalent to the conjecture. | Visual connectedness can hide missing reachability. | 5 | Watch |
| 23 | Eulerian/Cayley/middle-pages graph proof claims | Recent graph-color/preprint claims | May reveal exact graph encodings. | Typically converts the problem into an unproved coverage/tour assertion. | Beautiful graph symmetry can be non-equivalent. | 3 | Block until peer-reviewed/equivalence checked |
| 24 | Affine semigroups | Applegate-Lagarias 3x+1 semigroup; affine block maps | Gives algebra of composed parity blocks. | Semigroup structure alone lacks a positivity/descent invariant. | Exact algebra, missing order. | 4 | Attack with invariant only |
| 25 | Approximate squaring and related recurrences | Lagarias-Sloane | Shows Collatz-adjacent nonlinear maps with rich behavior. | Adjacent dynamics are not the original proof. | Simple recurrences can be wildly complex. | 3 | Watch |
| 26 | 3-smooth representation methods | Blecksmith-McCallum-Selfridge and related | Connects powers of 2 and 3 in representation questions. | Does not control arbitrary orbit intercepts. | Powers of 2 and 3 are the hidden arithmetic engine. | 3 | Reuse |
| 27 | Generalized 3x+1 maps | Hasse generalizations; Matthews-Watts; Wirsching | Classifies related maps and behaviors. | General methods cannot settle all maps; many variants diverge or cycle. | The original map is special but hard to isolate. | 5 | Reuse only for contrast |
| 28 | 5x+1, 3x-1, ax+b siblings | Lagarias-Weiss; Kontorovich-Lagarias; generalized-map literature | Shows similar maps can behave very differently. | Statistical analogy does not transfer proof. | Sibling maps can share drift-looking features but fail convergence. | 4 | Reuse as falsification tests |
| 29 | Undecidability of generalized Collatz | Conway; Kurtz-Simon 2007 | Proved natural generalized problems undecidable / Pi^0_2-complete. | Does not imply original Collatz is undecidable or solved. | The broader family is computation in disguise. | 5 | Reuse as warning |
| 30 | FRACTRAN / computation simulation | Conway | Shows arithmetic iteration can encode machines. | Too general; not specific to 3x+1. | Multiplicative fractions become universal computation. | 4 | Reuse as warning |
| 31 | Piecewise affine mortality / loop termination | Ben-Amram; Carelli 2026 | Connects Collatz-like maps to program termination. | The hard instances remain hard; equivalence can transfer difficulty rather than solve it. | One-variable loops and Collatz live in the same cave system. | 3 | Watch |
| 32 | Busy-beaver / program-complexity links | Calude-Calude-Dinneen; related complexity papers | Measures difficulty and finite refutability variants. | Nonconstructive difficulty measures do not produce a proof. | A tiny statement may imply unreachable computation. | 3 | Watch |
| 33 | Formal proof / proof assistant projects | Collatz Challenge and formalization efforts | Can certify known lemmas and stop bogus proofs. | Formalizing known partials does not invent the missing theorem. | Proof hygiene is valuable even without new math. | 2 | Reuse |
| 34 | Real-line continuous extensions | Chamberland 1996 | Produces smooth maps matching Collatz on integers. | Real dynamics has extra fixed points/escaping orbits; not equivalent to integer convergence. | The smooth world lies. | 5 | Block unless integer bridge is proved |
| 35 | Holomorphic/complex dynamics | Letherman-Schleicher-Wood 1999; Opfer 2011 claim | Gives fractal/complex dynamical analogues. | Analytic continuation often assumes or changes the discrete problem. Opfer-style proof failed by circularity. | Complex pictures are compelling and treacherous. | 5 | Block for proof claims |
| 36 | Fixed-point/analytic claimed proofs | Opfer and many later preprints | Sometimes identify real functional equations. | Hidden circularity: nondivergence or branch control is assumed. | The proof can smuggle Collatz into a lemma. | 5 | Block |
| 37 | "Pathfinding" inverse-tree proof claims | Recent arXiv/preprint proof claims | Algorithms can find paths for tested n. | A pathfinding procedure for each n needs a proof of termination for all n. | Algorithmic confidence masquerades as universal proof. | 5 | Block |
| 38 | Topological/thermodynamic formalisms | 2026 topological/ergodic preprints | May characterize recurrence/periodicity equivalences. | Equivalence and existence statements do not prove all positive orbits recur correctly. | Heavy machinery can repackage the same missing step. | 3 | Watch |
| 39 | Non-Archimedean spectral/Hydra/Numen formalisms | 2024-2026 preprints | Builds broad p-adic/global-field frameworks. | Framework is not proof without a Collatz-specific descent theorem. | Big algebraic language may or may not expose an invariant. | 2 | Watch |
| 40 | Modular graph Fibonacci theorems | 2026 modular graph preprints; Albert-Gudmundsson-Ulfarsson | Exact Fibonacci/spectral counts for special avoidance classes. | Avoidance decay is not universal convergence. | Fibonacci order appears inside parity/modular paths. | 3 | Watch |
| 41 | Collatz permutation patterns | Albert-Gudmundsson-Ulfarsson; Nathanson | Enumerates possible order patterns, positive densities, missing patterns. | Pattern avoidance does not force descent. | Fibonacci behavior up to length 14, then excess. | 3 | Watch |
| 42 | Paradoxical sequences | Rozier-Terracol 2025/2026 | Connects rare finite paradoxes to stopping-time/counterexample structure. | Finiteness of paradoxical sequences is still conjectural. | If only finitely many exist, very strong consequences follow. | 2 | Attack/Watch |
| 43 | One-bit/burst-gap/orbit-mixing reductions | Chang 2026 preprints | Reduces some bias to orbit-level mixing hypotheses. | Orbitwise mixing hypotheses remain open. | Map-level balance is exact; orbit-level balance is the abyss. | 2 | Watch |
| 44 | Human-LLM collaboration explorations | Chang 2026 and this repo's own work | Finds structures, lemmas, and falsification workflows. | LLM-assisted discovery is not validation. | New workflow, old mathematical wall. | 1 | Reuse with QA |
| 45 | Binary/trailing-zero single-branch formulas | 2024-2026 formula preprints | Compactly encodes branch behavior. | A closed formula for iteration is not a convergence proof. | Branching can be hidden inside valuations. | 4 | Block unless new bound appears |
| 46 | Palindrome/reflection formulations | Recent binary-palindrome preprints | Finds surprising coincidences with binary structure. | Equivalent reformulations do not control all orbits. | Aesthetic structure may be numerology unless bridged. | 3 | Watch |
| 47 | Modular extensions like mod 2^p+2^q | 2026 generalization preprints | Creates families containing Collatz-like rules. | Generalization increases burden and may import false siblings. | Bigger families amplify undecidability risk. | 3 | Watch |
| 48 | Prime-only or subset reductions | Many claimed proof papers | Sometimes reduces checks to odd numbers or residue classes. | Reduction usually loses or hides even-step/global orbit coverage. | "Only prove it on subset X" is often the same problem. | 5 | Block |
| 49 | Monotone potential functions | Countless elementary attempts | Works for many toy maps. | No known potential decreases on every Collatz step/orbit segment. | The missing Lyapunov function is the holy grail. | 5 | Attack only if truly global |
| 50 | Average logarithmic drift | Folklore, Lagarias surveys, random models | Gives negative expected drift log(3/4)/2-style heuristics. | Worst-case parity sequences can beat the average locally. | The average truth is not the pointwise truth. | 5 | Block as proof |
| 51 | "Odd steps must be less than even steps" cycle arguments | Elementary cycle proofs | Correctly identifies necessary inequalities. | Necessity is not contradiction; approximations to log_2(3) allow near balance. | Cycles require extreme but possible-looking balance. | 5 | Block |
| 52 | Induction on smaller descent | Classic proof template | If every n drops below itself, Collatz follows. | Proving first descent for every n is Terras' conjecture, still open. | The obvious induction reduces to the whole problem. | 5 | Attack only with new descent theorem |
| 53 | Minimal counterexample arguments | Common proof attempts | If a smallest divergent/cyclic counterexample exists, it has constraints. | Divergent orbits may not have a useful minimal counterexample behavior beyond starting value. | Minimality gives weak local constraints. | 5 | Block |
| 54 | Invariant modulo m arguments | Common elementary attempts | Can rule out small cycle patterns and test claims. | Any fixed modulus loses high-order carry/valuation behavior. | Bad behavior can regenerate beyond the modulus. | 5 | Block unless liftable |
| 55 | Generating functions | Various analytic/combinatorial attempts | Encodes tree counts and stopping distributions. | Singularities/counts do not imply full coverage. | Analytic mass may miss exceptional needles. | 4 | Watch |
| 56 | Sieve/character-sum analogies | Analytic approaches and Tao-adjacent heuristics | Clarifies parity-like obstructions. | No sieve sees both 2-adic branching and 3-adic multiplication enough to kill exceptions. | A Collatz parity problem analogue. | 3 | Attack only with new bilinear input |
| 57 | Erdos ternary-digit / Mahler Z-number analogies | Tao blog/context; digit-distribution analogies | Highlights difficulty of powers of 2/3 digit structure. | Analogies do not transfer a theorem. | Powers of 3 in base 2 are an old wall. | 3 | Reuse as difficulty warning |
| 58 | Local finite automata / regular-language models | Automata-style reformulations | Represents finite parity or residue languages exactly. | The infinite arithmetic condition is not regular without loss. | Regular shadows of nonregular arithmetic. | 3 | Watch |
| 59 | SAT/SMT finite encodings | Modern formal-methods route, not classical mainstream | Can falsify local lemmas or certify finite UNSAT obligations. | Finite UNSAT does not imply global theorem unless obligations form a proved cover. | Good QA tool, not a magic proof engine. | 1 | Attack for certificates |
| 60 | E-graphs/rewrite normalization | Modern proof-engine idea | Can prevent duplicate affine/parity identities. | Normal forms do not prove positivity/descent. | Algebra can be exact while order remains missing. | 1 | Attack for QA |
| 61 | Machine-learning / pattern discovery | Recent informal and LLM-era work | Finds conjectures, clusters, and candidate invariants. | Statistical discovery cannot certify a universal arithmetic statement. | Useful idea generator with high hallucination risk. | 2 | Reuse only with adversarial checks |
| 62 | Visual/fractal plots | Popular and complex-dynamics sources | Communicates orbit/tree structure. | Pictures do not prove reachability. | Strong intuition, weak theorem. | 5 | Reuse for exposition |
| 63 | Claimed elementary proofs in low-tier journals/preprints | Ongoing | Sometimes contain useful definitions. | Standard failures: hidden induction gap, density-to-all jump, circular inverse-tree coverage. | The problem attracts proof-shaped illusions. | 5 | Block unless independently formalized |
| 64 | Prize/problem folklore | Thwaites, Guy, Erdos quote, folklore | Frames the problem's danger. | Folklore is not method. | The sociology is part of the problem. | 5 | Reuse as caution |
| 65 | This repo's spine/ladder/retimed-reserve work | Local verified artifacts | Unifies affine block identities and exposes regeneration. | It does not bound indefinite regeneration or prove frontier separation. | Regeneration is the current local unknown-unknown. | 1 | Attack |

## Areas We Should Treat As Already Saturated

Do not spend serious time here unless we can state the genuinely new ingredient
in one sentence.

| Saturated area | Why to avoid repeating it |
|---|---|
| "The average multiplier is less than 1" | This is the oldest heuristic. It ignores adversarial parity sequences. |
| "Every tested number works" | True to 2^71, still finite. |
| "The inverse tree reaches everything" | That is equivalent to the conjecture unless a new coverage theorem appears. |
| "Modulo m proves all classes eventually fall" | Fixed m does not control lifted carries and future valuations. |
| "Almost all means all for practical purposes" | The exceptional set is exactly where a counterexample could live. |
| "No small cycles means no cycles" | Current cycle lower bounds are huge but finite. |
| "A continuous/complex extension converges" | Extensions change the problem unless the integer restriction is rigorously bridged. |
| "A graph is connected by construction" | The construction often assumes the missing reachability. |
| "A probability model says divergence has probability zero" | Probability zero events can still contain deterministic integers. |
| "A reformulation is simpler" | Simpler equivalent statements are still equivalent. |

## Higher-Value Non-Repeated Directions

These are the less-saturated routes that might actually be worth controlled
experiments in this repo.

| Direction | Why it is not merely old repetition | Required proof obligation |
|---|---|---|
| Exceptional-set attack after Tao | Instead of proving another average theorem, target the exact class that Tao cannot reach. | A mechanism that upgrades logarithmic almost-all to orbitwise control or kills the exceptional set. |
| Regeneration bound for 2-adic spine alignment | This repo's current sharp local obstruction is regeneration, not first-discovery of affine cylinders. | Prove indefinite supercritical alignment cannot regenerate along positive integer orbits. |
| SAT/SMT certificates for finite lift lemmas | Formal-methods certificates can make finite claims independently checkable. | Show the finite obligations cover an infinite theorem, not just sampled depth. |
| E-graph normal forms for affine block identities | Prevents rediscovery and hidden algebra gaps. | Pair normal forms with positivity/valuation hypotheses. |
| Paradoxical-sequence finiteness stress tests | Rozier/Terracol suggests a rare finite obstruction with theorem-level consequences. | Convert empirical finiteness into a theorem or find counterexamples. |
| Orbit-level mixing for fixed low-bit variables | Chang-style map-level balance says the remaining bias is orbitwise. | Prove every orbit samples the required residue classes with enough balance. |
| 3n+1 vs sibling-map differential tests | A real invariant must distinguish Collatz from siblings with similar statistics. | Any proposed invariant must fail on known divergent/cyclic siblings. |
| Formal proof claim quarantine | Collatz is proof-claim toxic; QA is a real research function. | Every lemma carries provenance, exact hypotheses, and a falsification script. |

## Practical Novelty Filter

Before adding a new Collatz idea to the repo, answer these.

1. Which row of the no-repeat matrix is this closest to?
2. What exact old failure mode does it avoid?
3. Is it a theorem, a computation, a heuristic, or a reformulation?
4. If it is finite, what proves the finite set covers the infinite problem?
5. If it is probabilistic, what controls the exceptional deterministic orbits?
6. If it is 2-adic, what brings positive integers back into the argument?
7. If it is a graph/tree proof, where is noncircular reachability proved?
8. If it is a cycle argument, does it cover unbounded m?
9. If it uses a sibling/generalized map, what property is special to 3x+1?
10. What script, certificate, or proof assistant check can falsify it?

## Future Bibliography Expansion Plan

The next pass should not try to reread 300+ papers linearly. Use this route.

1. Import Lagarias bibliography I and II into a structured CSV with fields:
   `year`, `author`, `title`, `family`, `claim_type`, `status`, `failure_mode`,
   `weirdness`, `url_or_identifier`.
2. Add post-2009 papers from arXiv, MathSciNet/Zentralblatt where available,
   and the AMS volume references.
3. Tag every local repo idea against the same family list.
4. For each future theorem sketch, require a "prior-art collision" section:
   which row it extends, and which old failure it defeats.
5. Keep claimed-proof preprints in a quarantine table unless peer-reviewed or
   independently formalized.

## Bottom Line

We are not in an empty wilderness. Collatz has a deep, weird, heavily mined
literature. The rare air is not "I found a new reformulation." The rare air is:

- controlling the exceptional set left by density theorems;
- proving a genuine orbitwise mixing/descent statement;
- preventing indefinite 2-adic regeneration on positive integers;
- producing machine-checkable certificates that cover an infinite family;
- finding an invariant that distinguishes 3x+1 from deceptive sibling maps.

Everything else should be treated as probably rediscovered until it survives
the no-repeat matrix.
