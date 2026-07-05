# Collatz Failed Ideas Atlas - 2026-07-04/05

_Created: 2026-07-04/05. Status: research avoidance map, not a proof, not a complete bibliography._

## Purpose

This atlas is meant to stop the repo from redoing old Collatz work under new
names. It lists the main published, semi-published, computational, heuristic,
and pseudo-proof routes that have already been tried or circled around the
problem, then ranks them by weirdness and by "unknown-unknown" risk.

The literal paper universe is too large for one hand-maintained file. Lagarias'
annotated bibliography for 1963-1999 alone records well over a hundred items,
and its sequel covers 2000-2009. This file is instead a practical attack-history
map: what idea family was tried, what it achieved, why it did not solve the
conjecture, and what future work must not accidentally repeat.

Companion artifacts:

- Public weirdness/no-repeat map:
  [`../FAILED-ATTEMPTS-WEIRDNESS-ATLAS-2026-07-05.md`](../FAILED-ATTEMPTS-WEIRDNESS-ATLAS-2026-07-05.md).
- Paper-level source floor:
  [`COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md`](COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md).
- Strategic route-ranking version:
  [`COLLATZ-FAILED-ATTEMPTS-IDEA-ATLAS-2026-07-04.md`](COLLATZ-FAILED-ATTEMPTS-IDEA-ATLAS-2026-07-04.md).

## Source Anchors

Use these as the primary bibliography roots before launching any "new" idea:

- Lagarias 3x+1 page:
  https://websites.umich.edu/~lagarias//3x%2B1.html
- Lagarias, "The 3x+1 problem and its generalizations", Amer. Math. Monthly 92
  (1985), 3-23.
- Lagarias, "The 3x+1 problem: An annotated bibliography (1963-1999)",
  arXiv:math/0309224:
  https://arxiv.org/abs/math/0309224
- Lagarias, "The 3x+1 Problem: An Annotated Bibliography, II (2000-2009)",
  arXiv:math/0608208:
  https://arxiv.org/abs/math/0608208
- Lagarias ed., _The Ultimate Challenge: The 3x+1 Problem_, AMS, 2010.
  https://bookstore.ams.org/mbk-78
- Lagarias, "The 3x+1 Problem: An Overview", arXiv:2111.02635:
  https://arxiv.org/abs/2111.02635
- Terras, "A stopping time problem on the positive integers", Acta Arith. 30
  (1976), 241-252:
  https://eudml.org/doc/205476
- Everett, "Iteration of the number-theoretic function f(2n)=n,
  f(2n+1)=3n+2", Adv. Math. 25 (1977), 42-45:
  https://www.osti.gov/biblio/7357908
- Lagarias and Weiss, "The 3x+1 Problem: Two Stochastic Models", Ann. Appl.
  Prob. 2 (1992), 229-261:
  https://projecteuclid.org/journals/annals-of-applied-probability/volume-2/issue-1/The-3x--1-Problem-Two-Stochastic-Models/10.1214/aoap/1177005779.full
- Krasikov and Lagarias, "Bounds for the 3x+1 problem using difference
  inequalities", Acta Arith. 109 (2003), 237-258:
  https://arxiv.org/abs/math/0205002
- Simons and de Weger, "Theoretical and computational bounds for m-cycles of
  the 3n+1-problem", Acta Arith. 117 (2005), 51-70:
  https://doi.org/10.4064/aa117-1-3
- Hercher, "There are no Collatz-m-Cycles with m <= 91", J. Integer Seq. 26
  (2023), Article 23.3.5; arXiv:2201.00406:
  https://arxiv.org/abs/2201.00406
- Tao, "Almost all orbits of the Collatz map attain almost bounded values",
  arXiv:1909.03562:
  https://arxiv.org/abs/1909.03562
- Barina, "Convergence verification of the Collatz problem", J. Supercomput.
  77 (2021), 2681-2688; and "Improved verification limit for the convergence
  of the Collatz conjecture", J. Supercomput. 81 (2025), 810:
  https://pcbarina.fit.vutbr.cz/
- Angeltveit, "An improved algorithm for checking the Collatz conjecture for
  all n < 2^N", arXiv:2602.10466:
  https://arxiv.org/abs/2602.10466
- Chang, "Exploring Collatz Dynamics with Human-LLM Collaboration",
  arXiv:2603.11066:
  https://arxiv.org/abs/2603.11066

## Weirdness Scale

| Rank | Label | Meaning |
|---:|---|---|
| W0 | Standard | Natural first attack; everyone rediscovers it |
| W1 | Serious classical | Accepted mathematics, but known not to close the conjecture |
| W2 | Deep partial | Strong theorem or computation with a sharp remaining gap |
| W3 | Strange dynamics | Reveals behavior that is hard to domesticate |
| W4 | Beyond-the-beyond | Touches undecidability, 2-adics, universality, or weird model behavior |
| W5 | Unknown-unknown trap | Seductive route that keeps generating false proofs or hidden circularity |

## Master Failure Modes

| Code | Failure mode | Anti-repeat test |
|---|---|---|
| F1 | "Almost all" is treated as "all" | Ask what happens to a density-zero exceptional set |
| F2 | Finite verification is treated as proof | Ask how the argument scales beyond the verified range |
| F3 | Cycle exclusion is confused with divergence exclusion | Ask where unbounded nonperiodic orbits are ruled out |
| F4 | Random drift is treated as deterministic descent | Ask for the orbitwise invariant |
| F5 | 2-adic typicality is transferred to positive integers | Ask why the integer subset is controlled |
| F6 | Congruence classes are checked at fixed modulus only | Ask what happens under lift to higher powers of 2 |
| F7 | Reverse tree coverage is assumed | Ask for a proof that every positive integer enters the tree |
| F8 | Hidden induction on unproved smaller descent | Ask where the first drop below start is proved |
| F9 | Analytic continuation or smooth extension imports the conclusion | Ask whether convergence was assumed in a functional equation |
| F10 | Heuristic search becomes theorem language | Ask for a counterexample harness or formal certificate |
| F11 | Generalized Collatz facts are transferred to the 3n+1 map | Ask which specific feature of 3 and 2 is being exploited |
| F12 | LLM or symbolic prose masks missing quantifiers | Ask for exact variables, domains, and falsifiable finite cases |

## Massive Attempt Atlas

| # | Area | Representative papers / people | What was tried | What it found | Why it failed to close | Weirdness | Avoid repeating by |
|---:|---|---|---|---|---|---:|---|
| 1 | Survey baseline | Lagarias 1985 | Systematize known routes and generalizations | Made the problem a mature research object | Survey, not a new invariant | W1 | Read before naming any "new" category |
| 2 | Annotated bibliography | Lagarias 1963-1999 | Exhaustive historical paper map | Canonical pre-2000 map | Bibliography, not closure | W1 | Check old entries before declaring novelty |
| 3 | Annotated bibliography II | Lagarias 2000-2009 | Post-2000 continuation | Captures modern explosion | Stops before 2010s/2020s | W1 | Extend, do not replace |
| 4 | AMS volume | Lagarias ed. 2010 | Survey, stochastic, computation, early papers | Best compact field snapshot | Up to 2010 only | W1 | Use as taxonomy root |
| 5 | Overview | Lagarias 2010/2021 arXiv | Why easy statement is hard | Frames no-cycle/no-divergence split | Expository | W1 | Quote as status, not result |
| 6 | Early origin | Collatz, Hasse, Ulam folklore | Original iteration problem | Simple map, hard dynamics | No proof method | W0 | Do not re-present statement as insight |
| 7 | Stopping time | Terras 1976 | Prove almost all numbers drop below start | Natural density-one finite stopping time | Density-zero exceptional set remains | W2 | Any density proof must name exceptional set |
| 8 | Almost all descent | Everett 1977 | Parity-vector counting | Almost every integer eventually drops below start | "Almost every" is not every | W2 | Never upgrade density to pointwise |
| 9 | Korec exponent descent | Korec | Bound minimum orbit value by N^theta for almost all | Stronger almost-all descent | Still almost all; exponent not 0 | W2 | Compare to Tao before using |
| 10 | Tao theorem | Tao 2019 | Entropy/3-adic random variable transport | Almost all orbits attain almost bounded values | Log-density exceptional set remains | W3 | If weaker than Tao, say so |
| 11 | Tao-style entropy | Post-Tao papers | Refine probabilistic transport | Formalizes random heuristic | Does not rule out bad orbit | W3 | Ask where pointwise control enters |
| 12 | Natural density upgrades | Many | Try to promote almost all to all | Better density statements | Exceptional orbit can hide in null set | W5 | Demand a universal invariant |
| 13 | Difference inequalities | Krasikov 1989 | Inequalities for convergent-count lower bounds | Polynomial lower bounds | Exponent below 1 leaves huge gap | W2 | Do not call x^a with a<1 "almost all" |
| 14 | Optimized inequalities | Krasikov-Lagarias 2003 | Computer-aided full extraction of inequalities | At least x^0.84 converge | Positive-exponent complement remains | W2 | Need exponent 1 with error control |
| 15 | Tree-search density | Applegate-Lagarias 1995 | Search inverse tree for density bounds | Improved lower-density evidence | Tree density is not full coverage | W2 | Separate tree mass from all integers |
| 16 | Krasikov inequality variants | Applegate-Lagarias 1995 | Refine inequality systems | Better convergent-set counts | Same exponent barrier | W2 | Avoid rebranding as certificate proof |
| 17 | 3x+1 tree distribution | Applegate-Lagarias 1995 | Statistical structure of inverse tree | Quantified tree growth | Inverse tree not known to contain all | W2 | Need a membership proof |
| 18 | Total stopping records | Applegate-Lagarias 2003 | Construct lower bounds for total stopping time | Very large record behavior | Records are convergent, not obstructive proof | W2 | Records are stress tests |
| 19 | Oliveira e Silva records | Oliveira e Silva 1999+ | Max excursion/stopping time computation | Record-holders and empirical floor | Computation finite | W2 | Use as benchmark only |
| 20 | GPU verification | Barina 2020/2025 | Verify all n below 2^68 then 2^71 | No counterexample below 2^71 | Polya/Mertens warning: finite range not proof | W2 | Treat as lower bound on possible counterexamples |
| 21 | Verification algorithms | Angeltveit 2026 | Faster all-n<2^N verification | Better scaling strategy | Still finite verification | W2 | Link to manifest, not theorem |
| 22 | Distributed search | Roosendaal/others | Independent large-range computation | Confirms empirical convergence | Finite range only | W2 | No "therefore true" language |
| 23 | Cycle 1 exclusion | Steiner 1977 | Exclude 1-cycles | No nontrivial one-cycle | Higher cycles remain | W1 | Do not confuse one-cycle with all cycles |
| 24 | Cycle lower bounds | Eliahou 1993 | Lower bounds on nontrivial cycle length | Huge cycle-length floor | Finite lower bound | W2 | State exact dependency on verification |
| 25 | m-cycle bounds | Simons-de Weger 2005 | Diophantine + computation for m-cycles | No m-cycles for m <= 75 / m>=76 | Only bounded m | W2 | Do not say no cycles |
| 26 | m<=91 exclusion | Hercher 2023 | Stronger local-minimum cycle exclusion | No Collatz m-cycles with m<=91 | m>=92 remains; divergence untouched | W2 | Cycle result only |
| 27 | Baker theory | Tijdeman/Baker machinery in cycle papers | Linear forms in logarithms | Explicit upper/lower incompatibilities | Constants/finite parameters only | W2 | Needs independent infinite argument |
| 28 | Continued fractions | Many cycle papers | Approximate log_2(3) | Exclude near ratios at finite ranges | Cannot cover all lengths alone | W1 | Use for cycle side only |
| 29 | LLL lattice reduction | Simons-de Weger style | Improve Diophantine cycle search | Better finite exclusions | Still finite-dimensional cases | W2 | Record exact bounds |
| 30 | Rational cycles | Lagarias 1990 | Study rational cycles for 3x+1 | Rich rational periodic structure | Positive integer cycles remain separate | W3 | Avoid transferring rational to integer |
| 31 | Negative integers | Classic folklore / Angeltveit | Analyze negative cycles | Multiple negative cycles exist | Positive dynamics differ | W3 | Use as sibling control |
| 32 | 5x+1 and siblings | Lagarias-Kontorovich, others | Compare divergent/alternate maps | Shows constants matter | General behavior not 3x+1 proof | W3 | Use as falsification control |
| 33 | 3x+d maps | Matthews-Watts, Wirsching | Generalized affine maps | Markov/ergodic framework | Specific map still open | W3 | Identify 3n+1-specific property |
| 34 | Generalized Collatz | Conway | Unpredictable iterations | Universality in generalized maps | Not original map | W4 | Do not overstate undecidability |
| 35 | FRACTRAN | Conway | Arithmetic universal programming language | Shows iteration can simulate computation | Different system | W4 | Conceptual warning only |
| 36 | Pi^0_2 completeness | Kurtz-Simon 2007 | Generalized Collatz undecidability | Natural generalization is Pi^0_2-complete | Original conjecture not proved undecidable | W4 | Use as method-bound warning |
| 37 | Mortality/affine automata | Rystsov and related | Connect to automata mortality | Undecidability analogies | Generalized systems | W4 | No direct transfer |
| 38 | Busy beaver links | Collatz-like/Erdos digit problems | Encode hard number conjectures into machines | Shows tiny machines can hide Collatz-like hardness | Not proof of Collatz | W4 | Use only as weirdness marker |
| 39 | Antihydra-like systems | Busy-beaver literature | Collatz-like halting barriers | Recent hard machine behavior | Adjacent, not original map | W4 | Avoid conflating |
| 40 | 2-adic extension | Lagarias, Bernstein-Lagarias | Extend map to Z_2 | Shift conjugacy and parity coding | Positive integers are special, measure-zero | W4 | Need integer-subset control |
| 41 | Conjugacy map | Bernstein-Lagarias 1996 | Parity sequence conjugacy | Exact symbolic dynamics in Z_2 | Typical 2-adics do not settle integers | W4 | Do not equate symbolic with positive |
| 42 | Ergodic theory | Matthews-Watts, Wirsching | Markov chains/ergodicity | Explains average behavior | Almost-sure not pointwise | W3 | Ask for exceptional-orbit exclusion |
| 43 | Markov models | Matthews-Watts | Model generalized Syracuse maps | Distributional predictions | Model != deterministic proof | W3 | Use as heuristic only |
| 44 | Stochastic models | Lagarias-Weiss 1992 | Random walk approximations | Mimic stopping-time features | Randomness assumption unproved | W3 | Need derandomization |
| 45 | 3-adic random walk | Tao 2019 | Skew random walk on 3-adic cyclic group | Deep almost-all theorem | Still logarithmic density | W4 | Compare exact theorem strength |
| 46 | Benford law | Kontorovich-Miller; Lagarias-Soundararajan | Digit distribution/statistical laws | Statistical regularities in iterates | Digit law cannot force every orbit | W3 | Avoid digit-stat proof |
| 47 | Extreme stopping stats | Melas-Poulios 2026 | Predict long stopping times statistically | Identifies unusual long-orbit candidates | Statistical, not proof | W3 | Use for stress tests |
| 48 | Paradoxical sequences | 2025 preprint | Sequences exceeding expected bounds after stopping time | Shows non-typical finite behavior matters | Supports/frames, does not close | W3 | Treat as obstruction map |
| 49 | Random drift | Folklore | Expected multiplier <1 | Strong reason to believe | Worst-case can beat average | W5 | Need orbitwise descent |
| 50 | Martingale dreams | Many | Search for Lyapunov/supermartingale | If found, would be huge | No known valid one on integers | W5 | Test against high records |
| 51 | Monotone invariant | Many pseudo-proofs | Define energy that always drops | Usually fails on odd spikes | No global monotone found | W5 | Falsify on known records |
| 52 | Modular classes | Countless | Partition by residues mod 2^k or m | Finite covers at fixed scale | Lift creates new residue behavior | W5 | Require all-level lift proof |
| 53 | Parity vectors | Terras/Everett onward | Encode finite trajectory by parity word | Exact finite formula | Bad infinite words remain | W3 | Need infinite-language exclusion |
| 54 | Parity-word counting | Many | Show most words descend | Density result | Bad words may be rare but infinite | W3 | Require uniform bound |
| 55 | All-odd boundary | Folklore / 2-adic | Study 2-adic fixed/spine paths | Explains extremal obstruction | Not positive integer directly | W4 | Use as boundary, not counterexample |
| 56 | Mersenne spine | Many | Follow 2^k-1-like high odd density | Hard finite examples | Eventually descends in known cases | W3 | Stress case only |
| 57 | Preimage tree | Many | Build all numbers reaching 1 backwards | Huge tree of convergent integers | Need prove every n is in it | W5 | Membership is the conjecture |
| 58 | Tree density | Applegate-Lagarias | Count inverse tree growth | Large convergent population | Not full coverage | W2 | State density only |
| 59 | Graph visualization | Many | Plot Collatz graph/tree/spiral | Pattern discovery | Visual evidence no theorem | W1 | Use only for intuition |
| 60 | Collatz spiral | Popular/pseudo | Geometry/spiral diagrams | Pretty structure | No rigorous descent | W1 | Do not cite as proof |
| 61 | Base representation | Many | Use base 2/3/6/10 digit patterns | Finds digit regularities | Carries/correlations uncontrolled | W5 | Test under carry propagation |
| 62 | Sum of digits | Many | Digital-root or digit-sum invariants | Modular observations | Too weak; cycles mod m exist | W0 | Require actual descent |
| 63 | Mod 3 arguments | Beginners | Since 3n+1 has special residues | Local constraints | Division by 2 scrambles | W0 | Check after several steps |
| 64 | Mod 8 tables | Beginners/serious local work | Small residue transition tables | Useful local grammar | Finite table does not close lifts | W2 | Need induction over modulus |
| 65 | Induction on n | Common false proof | If orbit drops below n, induction works | Correct conditional | Missing proof of first drop | W5 | This is exactly Terras barrier |
| 66 | Strong induction with cases | Common false proof | Split parity cases | Even case works, odd grows | Odd branch not smaller | W0 | Never leave odd branch unresolved |
| 67 | Minimal counterexample | Common | Assume smallest bad n | Would drop if ever below n | Need prove it drops | W5 | Same as first-drop problem |
| 68 | Descent certificates | Computational | Find k with T^k(n)<n | Works for finite ranges | Uniform certificate missing | W2 | Convert to coverage theorem |
| 69 | Finite automata for residues | Serious/adjacent | Model transitions at fixed modulus | Can verify local claims | Sound abstraction hard | W3 | Prove abstraction overapproximates |
| 70 | Symbolic execution | Modern tooling | Extract path conditions | Great for finite claims | Path explosion / finite only | W2 | Attach solver certificates |
| 71 | SAT/SMT encodings | Modern tooling | Search finite counterexamples | Useful falsification | Bounded only | W2 | Publish as obstruction harness |
| 72 | Proof assistants | Modern | Formalize small lemmas | Increases reliability | Formalizing false target proves little | W2 | Start with affine-map lemmas |
| 73 | E-graphs/rewrite systems | Modern tooling | Normalize affine identities | Reduces duplicate algebra | Missing hypotheses hidden | W3 | Track side conditions |
| 74 | Quantifier elimination | Modern tooling | Bounded Presburger-like claims | Exact finite elimination | Nonlinear/exponential terms hard | W3 | Bound domain honestly |
| 75 | BDD/ZDD compression | Modern tooling | Exact frontier sets | Scales exact enumeration | Compression not proof | W2 | Require exact count match |
| 76 | Difference equations | Various | Recurrences for counts | Good lower bounds | Cannot force every orbit | W2 | Connect to pointwise |
| 77 | Generating functions | Various | Encode tree or stopping times | Analytic structure | Singularities hard; coverage missing | W3 | Watch circularity |
| 78 | Complex analytic extensions | Opfer 2011 | Holomorphic/analytic mapping proof | Public claimed proof attempt | Hidden circularity/gap; not accepted | W5 | Do not assume nondivergence |
| 79 | Real interpolation | Chamberland/others | Smooth/real extensions of Collatz | Dynamical-systems insight | Real map differs from integer orbit | W3 | Needs integer restriction proof |
| 80 | p-adic analytic methods | Various | Non-Archimedean dynamics | Natural for parity | Typical p-adics not positives | W4 | Explicit embedding control |
| 81 | Semigroup methods | Applegate-Lagarias | 3x+1 semigroup structure | Algebraic organization | Semigroup complexity remains | W3 | Need invariant or certificate |
| 82 | Approximate squaring | Lagarias-Sloane | Related semigroup/approximation behavior | Strange arithmetic dynamics | Related problem, not closure | W3 | Treat as analogy |
| 83 | Wild/Wooley numbers | Lagarias | Multiplicative semigroup weirdness | Shows related arithmetic wildness | Not Collatz proof | W3 | Use for caution |
| 84 | Harmonic analysis | Tao and related | Fourier decay / high frequencies | Powerful almost-all theorem | Exceptional set remains | W4 | Do not simplify to "random enough" |
| 85 | Large deviations | Many | Bound rare high-odd words | Explains rarity | Rare is not impossible | W3 | Need zero, not small |
| 86 | Entropy barriers | Tao-like | Entropy decrement/transport | Converts heuristic to theorem | Not pointwise | W4 | State density type |
| 87 | Sieve analogies | Many | Treat bad classes like sifted set | Useful warning | Parity-style obstruction | W3 | Ask what sieve cannot see |
| 88 | Additive combinatorics | Tao | Control distributions | Deep partial result | Still almost-all | W4 | Avoid redoing weaker form |
| 89 | Diophantine approximation | Cycle papers | Control 2^a vs 3^b | Strong no-cycle constraints | Divergence not addressed | W2 | Label cycle-only |
| 90 | Transcendence bounds | Baker-style | Explicit no-cycle windows | Works with computation | Constants finite | W2 | Needs unbounded argument |
| 91 | Local minima cycles | Hercher | Count minima in hypothetical cycles | m>=92 | Higher m remain | W2 | Do not collapse to no cycles |
| 92 | Odd-member cycle lower bounds | Hercher/Eliahou | Huge K lower bound | Any cycle astronomically long | Still possible in principle | W2 | Cite exact assumptions |
| 93 | Exhaustive congruence pruning | Verification codes | Skip redundant classes | Efficient computation | Finite | W2 | Keep manifests |
| 94 | GPU acceleration | Barina | Massive speedup | 2^71 verified | Still finite | W2 | Operational, not proof |
| 95 | Negative map analogy | Angeltveit etc. | Verify negative analogue/cycles | Tests algorithms | Positive case unaffected | W3 | Use as sibling control |
| 96 | 5x+1 divergence | Comparative dynamics | Show drift can flip | Warning about constants | Not proof of 3x+1 | W3 | Keep as falsifier |
| 97 | 3n-1 cycles | Sibling control | Known cycles | Shows similar maps differ | 3n+1 still open | W3 | Use as control |
| 98 | Random sampling experiments | Countless | Look for counterexamples | None found | Sampling cannot prove absence | W1 | Record as empirical only |
| 99 | ML pattern mining | Recent | Predict stopping times/classes | Can guide scans | Not proof; overfit risk | W3 | Must feed exact verifier |
| 100 | LLM collaboration | Chang 2026 | Human-LLM structural exploration | Conditional framework, burst-gap ideas | Key hypotheses open | W4 | Separate proved lemmas from hypotheses |
| 101 | LLM proof attempts | Many | Ask models for proof | Finds plausible prose | Frequent false quantifiers | W5 | Extract obligations only |
| 102 | Burst-gap decomposition | Chang 2026 | Gap/burst orbit framing | Conditional convergence chain | Orbitwise hypotheses open | W4 | Prove hypotheses or mark conditional |
| 103 | Modular scrambling | Chang 2026 | High-bit bijection/scrambling | Structural finite results | Scrambling does not imply convergence | W4 | Need descent bridge |
| 104 | Persistent states | Chang 2026 | Characterize persistent/gap behavior | New language for hard orbits | Conditional | W4 | Falsify with exact runs |
| 105 | Fiber/return kernels | Chang-related | Return maps on modular fibers | Perron/eigenvalue structure | Model-level, not global theorem | W4 | Identify exact domain |
| 106 | Paradoxical finite behavior | 2025 work | Finite sequences exceeding expected first term | Shows surprise beyond stopping time | Still not nonconvergence | W3 | Use as stress class |
| 107 | Extreme stopping prediction | 2026 statistical | Predict large normalized stopping times | Good hard-case finder | Statistical | W3 | Add to test suite |
| 108 | "No finite cycle" claims | Various preprints | Binary sequence/cycle number arguments | Often claim too much | Usually hidden gap in admissibility/infinite passage | W5 | Require expert source check |
| 109 | Published-looking low-tier proofs | Various journals/preprints | Claimed elementary proofs | Sometimes polished | Not accepted by specialist community | W5 | Compare to Lagarias/Tao/Hercher standards |
| 110 | "Base-X" proofs | Recent web papers | Reframe in positional base | Novel terminology | Usually digit/carry gap | W5 | Demand exact carry theorem |
| 111 | Prime-only reductions | Various | Analyze primes or odd numbers | Smaller domain intuition | Composite/iterate closure fails | W2 | Need invariant subset |
| 112 | Stopping-time tables | OEIS/A006577 etc. | Catalog total stopping times | Excellent data | Data not proof | W1 | Use to test claims |
| 113 | Record trajectory lore | Numberphile/popular | Public hard examples | Inspires intuition | Not rigorous | W1 | Treat as communication |
| 114 | "Counterexample must be huge" rhetoric | Popular | Use verification floor | True but insufficient | Huge can exist | W1 | Cite finite bound |
| 115 | "Expected contraction" proof | Common | Multiply by 3 half the time, divide by 2 | Negative drift | Parity not independent for a fixed orbit | W5 | Need independence proof |
| 116 | "Every odd becomes even" proof | Beginner | Odd step followed by even | True | Net can grow: (3n+1)/2 > n | W0 | Compute net effect |
| 117 | "Two steps shrink" claims | Beginner | Check pairs | Some pairs grow | False on residues | W0 | Test residues |
| 118 | "Modulo cycle impossible" proof | Beginner | Show cycles impossible mod m | Mod images allow fake cycles | Lifting issue | W0 | Need integer equality |
| 119 | "Closed-form orbit" proof | Many | Write affine formula for parity word | Correct finite formula | Does not select actual infinite word | W3 | Need admissibility + descent |
| 120 | "All parity words occur" misuse | 2-adic theory | Every finite parity vector corresponds mod 2^k | True finite fact | Positive infinite orbit control missing | W4 | Separate finite/infinite |
| 121 | "Measure-preserving shift proves randomness" | 2-adic misuse | Shift conjugacy | Real theorem | Typicality not pointwise positives | W5 | Ask for positive-integer theorem |
| 122 | "Tree has exponential growth" proof | Reverse tree misuse | Many preimages | True | Could miss infinite set | W5 | Need density/coverage bridge |
| 123 | "No cycles implies convergence" | Common | Rule out periodic alternatives | False: divergence possible | Missing unbounded orbit case | W0 | Always split two failure modes |
| 124 | "Divergence implies high odd density" | Heuristic | Any divergent orbit needs many odd steps | Useful necessary condition | Need prove impossible, not unlikely | W3 | Quantify all windows |
| 125 | "High odd density impossible" | Attempts | Bound runs of odd-heavy words | Local constraints help | Regeneration can occur | W4 | Test on spines/records |
| 126 | "Potential/energy" repo-style | Current repo and others | Credits/defects/repulsion | Good falsifiable framework | Needs universal induction | W3 | SAT/SMT counterexample harness |
| 127 | "Affine cocycle rigidity" | Current repo/unreviewed | Cocycle/repulsion language | Some identities valid | Sufficiency subclaims can fail | W4 | Keep in claim audit |
| 128 | "Kick repulsion" | Current repo audit | +1 term creates separating force | Linear descent pieces survive | Counted-repulsion sufficiency failed | W4 | Preserve failed lemma |
| 129 | "Retimed reserve" | Current repo | Credit arrives before pressure | Strong finite evidence | Universal induction open | W4 | Need lift theorem |
| 130 | "Phase collision" | Current repo / share ingest | Exact collision and odd-unit locks | Useful normal form | Phase gate too permissive alone | W4 | Need odd-unit lock theorem |
| 131 | "Density-zero survivor frontier" | Current repo/Tao-adjacent | Bad set has tiny dimension/density | Explains rarity | Tiny not empty | W5 | Never use dimension=0 as empty |
| 132 | "Hausdorff/box dimension" | Fractal framing | Survivor set dimension estimates | Geometric insight | Exceptional set may remain | W4 | Require arithmetic exclusion |
| 133 | "Equidistribution bridge" | Many | If representatives equidistribute, descent follows | Plausible bridge | Equidistribution unproved orbitwise | W5 | Name as hypothesis |
| 134 | "Orbitwise independence" | Many | Treat parity bits as independent | Predicts convergence | Exactly the hard part | W5 | Need theorem, not model |
| 135 | "Finite support/topos/groupoid" | Exotic pseudo-proof family | Category/topos language | Expressive | Usually no exact Collatz content | W5 | Translate to residues or reject |
| 136 | "p-divisible/pro-etale" | Exotic pseudo-proof family | Algebraic geometry vocabulary | May be metaphor | No verified theorem bridge | W5 | Demand formal definitions |
| 137 | "Ultrametric contraction" | Exotic/current repo | 2-adic contraction claims | Natural metric intuition | 2-adic contraction can oppose real descent | W5 | Track real height too |
| 138 | "Information/complexity proof" | Chaitin/Kolmogorov attempts | Bad orbit would be compressible/impossible | Interesting | Usually non-rigorous complexity leap | W5 | Need formal coding theorem |
| 139 | "Busy-beaver proof route" | Complexity folklore | Use BB bounds | Shows hardness | Completely impractical | W4 | Use as warning only |
| 140 | "Computer algebra simplification" | CAS attempts | Symbolic manipulate iterations | Helps finite identities | Cannot choose true parity sequence globally | W3 | Attach branch conditions |
| 141 | "Graph SCC closure" | Algorithmic | Look for bad SCCs in finite quotient | Useful abstraction | Quotient may be unsound | W3 | Prove overapproximation |
| 142 | "Markov-chain stationary proof" | Probabilistic | Stationary distribution has descent | Model proof | Deterministic orbit not sampled | W4 | Need coupling theorem |
| 143 | "Benford/random digits proof" | Digit/statistical | Digits look random | Real statistical laws | Exceptional deterministic orbits | W3 | Use only as diagnostic |
| 144 | "Stopping-time regression" | Statistical ML | Predict total stopping time | Useful estimates | Prediction not proof | W2 | Benchmark, no theorem |
| 145 | "Visualization-first proof" | Popular | Spiral/lattice/grid pictures | Finds patterns | Pattern not invariant | W1 | Demand algebra |
| 146 | "Local-to-global by optimism" | Universal failure | Verify many local motifs | Encouraging | Missing cover/lift/induction | W5 | Require explicit cover theorem |
| 147 | "One magical invariant" | Dream route | Search for monotone quantity | Would solve | None known; many false | W5 | Test against hard records and siblings |
| 148 | "General theorem for all Collatz-like maps" | Too broad | Try universal convergence theorem | Impossible due undecidability/general counterexamples | Specific constants needed | W4 | Narrow to 3n+1 |
| 149 | "Pure computation to infinity" | Naive | Keep verifying higher bound | Improves floor | Infinity not reached | W2 | Use to support cycle bounds |
| 150 | "Proof by exhaustion of patterns" | Common | Enumerate pattern classes | Can be strong finite proof | Infinite pattern regeneration | W5 | Need well-founded descent on classes |

## Weirdness Ranking: Top "Beyond The Beyonds"

| Rank | Thing | Why it matters | Do not repeat mistake |
|---:|---|---|---|
| 1 | Generalized Collatz undecidability | Any too-general method must fail somewhere | Prove a 3n+1-specific theorem |
| 2 | 2-adic shift conjugacy | Dynamics are simple in Z_2 yet hard on positive integers | Typical 2-adic behavior is not integer behavior |
| 3 | Tao's almost-bounded theorem | The best modern theorem is still "almost all" | Do not produce a weaker almost-all result and call it new |
| 4 | Dimension/density-zero survivor sets | A tiny exceptional set can still contain every counterexample | Tiny is not empty |
| 5 | Finite verification to 2^71 | Empirical certainty is enormous but not proof | Finite is finite |
| 6 | Cycle exclusions m<=91 | The cycle side can be pushed astronomically far | Divergent noncycle orbits remain |
| 7 | FRACTRAN/universal arithmetic programs | Simple arithmetic iterations can simulate computation | Avoid broad generalized claims |
| 8 | Paradoxical finite sequences | Finite pieces can violate average intuition | Stress-test every drift heuristic |
| 9 | LLM proof fluency | Models generate plausible but false quantifier bridges | Extract obligations, not prose |
| 10 | Reverse tree seduction | The tree looks huge enough to cover everything | Coverage is the conjecture |

## Do-Not-Repeat List

Before pursuing a future idea, answer these:

1. Is it stronger than Terras/Everett/Tao, or merely another almost-all theorem?
2. Does it rule out divergence, or only cycles?
3. Does it prove first descent for every positive integer, or only for a finite scan?
4. Does it control all lifts to higher powers of 2?
5. Does it distinguish positive integers from generic 2-adics?
6. Does it have a counterexample-search harness?
7. Does it survive known high-stopping-time records?
8. Does it survive sibling maps where analogous claims should fail?
9. Are all hypotheses explicit and weaker than the conclusion?
10. Is every "new" term translatable into parity words, residues, affine maps, or a
    formal theorem statement?

## Future Literature Expansion Queue

This file should be expanded in three passes:

1. Parse Lagarias 1963-1999 bibliography into a CSV with columns:
   `author`, `year`, `paper`, `idea_family`, `result`, `why_not_closed`.
2. Parse Lagarias 2000-2009 bibliography the same way.
3. Add 2010-2026 papers manually, especially:
   Tao 2019; Hercher 2023; Barina 2020/2025; Angeltveit 2026; Chang 2026;
   recent stopping-time/statistical papers; and any serious proof-assistant or
   SAT/SMT work that exists.

## Operational Rule For This Repo

No new Collatz pursuit should start from a blank page. It should cite at least
one row above and declare:

```text
This is not repeating row(s): ...
The old failure mode was: ...
The new ingredient is: ...
The falsification harness is: ...
The exact theorem target is: ...
```

If those five lines cannot be filled in, the idea is probably old wine in a
new bottle.
