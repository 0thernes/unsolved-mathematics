# Collatz Failed / Insufficient Attempts Atlas - 2026-07-05

Purpose: avoid repeating old Collatz work under new names.

Status: research-routing atlas, not a proof document. "Failed" means "failed to prove or disprove the original positive-integer Collatz conjecture." Many entries below are excellent mathematics and valid partial results; they are "failed" only in the sense that the full conjecture remains open.

Primary anchors checked for this atlas:

- Jeffrey C. Lagarias, [The 3x+1 problem: An annotated bibliography (1963-1999)](https://arxiv.org/abs/math/0309224), 197 references.
- Jeffrey C. Lagarias, [The 3x+1 Problem: An Annotated Bibliography, II (2000-2009)](https://arxiv.org/abs/math/0608208), 134 entries.
- Jeffrey C. Lagarias ed., [The Ultimate Challenge: The 3x+1 Problem](https://bookstore.ams.org/mbk-78), 2010 AMS volume.
- Jeffrey C. Lagarias, [The 3x+1 Problem: An Overview](https://arxiv.org/abs/2111.02635), overview/survey.
- Terence Tao, [Almost all orbits of the Collatz map attain almost bounded values](https://arxiv.org/abs/1909.03562).
- Christian Hercher, [There are no Collatz-m-Cycles with m <= 91](https://arxiv.org/abs/2201.00406).
- David Barina, [Improved verification limit for the convergence of the Collatz conjecture](https://link.springer.com/article/10.1007/s11227-025-07337-0), plus [project log](https://pcbarina.fit.vutbr.cz/).
- [CCChallenge](https://ccchallenge.org/) and the local [`COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md`](COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md) bibliography snapshot.
- Recent focused checks: Knight 2026 high cycles, Angeltveit 2026 verification algorithm, Kurtz-Simon generalized undecidability, and proof-claim cautionary cases such as Opfer 2011.
- Recent arXiv sweep through early July 2026 for modern variants, operator/geometric/formal-language attempts, and AI-assisted Collatz exploration.

Coverage note: this compact scored atlas has 70 attempt rows. The broader local
avoidance layer is
[`COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md`](COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md),
which carries 150 idea-family rows and a larger pseudo-proof taxonomy. Neither
file certifies that every paper ever written has been read; both are meant to
stop future repo work from unknowingly replaying saturated routes.

## Reading Rules

Use this file as a red-team filter:

1. If a new idea fits one of these rows exactly, assume it is old until proven otherwise.
2. If it only improves finite computation, call it computation, not proof.
3. If it proves "almost all", density, measure, or probability, ask what happens on the exceptional set.
4. If it proves something on generalized maps, ask whether it uses constants special to `3n+1`.
5. If it proposes a monotone potential, test it on known hard records, negative cycles, and `3n-1` / sibling maps.
6. If it is tree-based, ask what prevents an infinite branch not containing `1`.
7. If it is 2-adic, ask how it separates positive integers from 2-adic ghosts.

## Scoring

| Score | Meaning |
|---:|---|
| Weirdness | How strange / beyond-the-usual the idea is. |
| Unknown-unknown value | How much it exposes hidden structure or a real blind spot. |
| Repetition risk | How likely we are to accidentally rediscover it. |
| Full-proof gap | How far the route remains from proving Collatz. |

Scale: 1 low, 10 extreme.

## The Giant Attempt Map

| # | Attempt family | Representative sources / names | What it tries | What it achieved | Why it still fails / gap | Weird | Unknowns | Repeat risk | Gap |
|---:|---|---|---|---|---|---:|---:|---:|---:|
| 1 | Direct computation / verification to a bound | Oliveira e Silva, Roosendaal, Barina | Check every start below a threshold. | Current verified frontier is at least `2^71` per Barina 2025/project log. | Infinite tail remains; computation only moves floor. | 2 | 3 | 8 | 10 |
| 2 | Stop when orbit drops below start | Standard induction criterion; Terras-style stopping time | Prove every `n>1` eventually has `T^k(n)<n`. | Equivalent to full conjecture; finite certificates work for scanned classes. | Universal descent is exactly the hard problem. | 3 | 5 | 10 | 10 |
| 3 | Density-one finite stopping time | Terras 1976, Everett 1977 | Show almost all integers drop below start. | Natural-density-one descent. | Exceptional set may contain all counterexamples. | 4 | 7 | 9 | 8 |
| 4 | Stronger density / lower-bound counting | Krasikov, Krasikov-Lagarias | Count many starts known to converge. | `# {n <= x: n -> 1} >> x^0.84` strand. | Still far from all integers. | 5 | 6 | 7 | 8 |
| 5 | Tao almost-bounded-values method | Tao 2019 | Use entropy/3-adic mixing to push almost all orbits near bounded values. | Strongest "almost all" theorem. | Logarithmic-density almost all, not pointwise all. | 8 | 9 | 7 | 7 |
| 6 | Random-walk negative drift heuristic | Lagarias-Weiss, many surveys | Treat parity as random; expected log drift is negative. | Explains why convergence is plausible. | Heuristics cannot exclude rare deterministic orbit. | 4 | 6 | 10 | 9 |
| 7 | Large deviations / entropy corridors | Terras, Tao-adjacent, many computational notes | Bound high-odd-density paths. | Sharp estimates for typical/frontier mass. | Bad path can live in exponentially thin set. | 5 | 8 | 9 | 8 |
| 8 | Benford/log-distribution analysis | Kontorovich-Miller; Lagarias-Soundararajan | Study leading digits/log distribution under Collatz-like dynamics. | Valid statistical structure. | Distributional facts do not force convergence. | 6 | 7 | 6 | 8 |
| 9 | Cycle exclusion by continued fractions | Steiner, Eliahou, Simons-de Weger, Hercher | Use approximations to `log_2 3` and cycle equations. | No small `m`-cycles; Hercher gives `m >= 92`; huge odd-term floor with verification. | Infinite possible cycle lengths remain. | 6 | 7 | 8 | 8 |
| 10 | Baker / linear forms in logarithms | Eliahou, Simons-de Weger, Hercher line | Lower-bound closeness of `2^a` and `3^b`. | Massive finite cycle lower bounds. | Constants finite; cannot rule all cycles. | 6 | 7 | 6 | 8 |
| 11 | S-unit / exponential Diophantine equations | Cycle literature; parity-vector equations | Convert parity words into equations involving powers of 2 and 3. | Exact constraints for hypothetical cycles/records. | Equations still allow infinitely many hard possibilities. | 7 | 8 | 7 | 8 |
| 12 | 2-adic extension | Hedlund, Lagarias, Bernstein-Lagarias | Extend map to `Z_2`; use parity-sequence conjugacy. | Deep structural model; parity words become natural. | Positive integers are a tiny special subset; ghosts remain. | 9 | 10 | 9 | 8 |
| 13 | Shift-map conjugacy / parity vector bijection | Terras, Bernstein-Lagarias | Encode orbit by binary parity sequence. | Exact bijective/cylinder machinery. | Encoding all sequences includes non-positive / ghost behavior. | 7 | 8 | 10 | 8 |
| 14 | Rational cycles / 2-adic periodic points | Lagarias rational cycles; Bernstein-Lagarias | Classify periodic/rational points in 2-adics. | Explains negative cycles and ghost spines. | Does not exclude positive divergent orbits. | 9 | 9 | 8 | 8 |
| 15 | Negative integer cycles as controls | Classical integer extension | Use `-1`, `-5/-7/-10`, `-17...` cycles to test mechanisms. | Excellent refutation tool for sign-blind arguments. | Controls are not proof for positives. | 8 | 9 | 9 | 7 |
| 16 | Inverse tree / preimage graph | Collatz tree literature, Oliveira e Silva records | Show `1` has a huge inverse tree and many integers enter it. | Tree structure explains known convergence. | Need prove every positive integer is in tree. | 4 | 6 | 10 | 9 |
| 17 | Tree pathfinding "every node has a route to root" | Many claimed proofs / modern preprints | Construct paths in inverse tree. | Often visually persuasive. | Usually assumes reachability or misses infinite branch obstruction. | 5 | 5 | 10 | 10 |
| 18 | Modular residue covers | Many elementary attempts | Cover residues mod `2^k` or mixed moduli with descent certificates. | Works for finite covers/classes. | No finite 2-adic cover; all-ones path survives. | 4 | 7 | 10 | 9 |
| 19 | Parity-word affine law | Terras/cylinder law; many rediscoveries | `T^d(x)=(3^o x+c)/2^d` on a cylinder. | Exact, essential local law. | Local affine law is sign-blind and finite-word only. | 4 | 7 | 10 | 8 |
| 20 | Descent certificates by multiplier `3^o<2^d` | Certificate frontier work | Certify whole residue classes eventually descend. | Good finite proof infrastructure. | Frontier with high odd density survives every depth. | 5 | 8 | 9 | 9 |
| 21 | Mersenne/all-ones boundary | `2^m-1` shadows of `-1` | Study finite shadows of 2-adic fixed point `-1`. | Shows exact boundary leakage. | Mersenne family exits; arbitrary high-odd words remain. | 7 | 8 | 9 | 8 |
| 22 | Motif forcing / repayment windows | Finite frontier experiments, motif miners | Find unavoidable subcritical windows. | Strong theorem target. | Need uniform forcing for all positive finite shadows. | 6 | 8 | 8 | 8 |
| 23 | Branch-credit / potential accounting | Modern in-repo attempts; similar potential methods | Count high-ladder and low-repeat events to pay excess. | Finds useful finite ledgers. | Global induction and regeneration remain open. | 6 | 8 | 9 | 9 |
| 24 | Monotone Lyapunov/potential functions | Countless proof attempts | Find a quantity always decreasing. | Useful for finite heuristics. | Collatz has local increases; potentials usually fail on hard records/sibling maps. | 5 | 6 | 10 | 10 |
| 25 | Matrix/spectral regression potentials | In-repo pseudo-proof family; spectral attempts | Fit contraction from sampled features. | Can classify sampled behavior. | Regression is not theorem; nonlinear dynamics not controlled. | 6 | 4 | 8 | 10 |
| 26 | Transfer-operator spectral theory | Surveyed by modern AI/LLM-assisted papers; dynamical systems line | Study operators on distributions. | Good for distributional convergence. | Spectral gap on distributions does not imply every integer orbit. | 8 | 8 | 6 | 8 |
| 27 | Martingales / supermartingales | Probabilistic heuristics and Tao-adjacent attempts | Turn negative drift into high-probability descent. | Explains typical behavior. | Need deterministic exceptional-set exclusion. | 7 | 8 | 6 | 8 |
| 28 | Modular sieving | Verification algorithms; elementary papers | Remove many residue classes cheaply. | Strong computational acceleration. | Sieve leaves infinite survivors. | 4 | 6 | 9 | 8 |
| 29 | Accelerated / Syracuse map | Standard formulation | Remove forced even division after odd step. | Simplifies proofs and computations. | Equivalent reformulation, not solution. | 2 | 5 | 10 | 10 |
| 30 | Total stopping time record studies | Oliveira e Silva; record-holder papers | Analyze hardest known trajectories. | Record sequences and max excursions catalogued. | Records are finite evidence only. | 4 | 6 | 7 | 9 |
| 31 | Giant random-number verification | Elsenhans-style billion-digit random starts | Test huge individual numbers. | Demonstrates algorithms can handle enormous instances. | Random samples say little about universal theorem. | 5 | 5 | 5 | 10 |
| 32 | Polynomial analogues over `F_2[x]` | Alon-Behajaina-Paran 2024, earlier polynomial map work | Transfer Collatz-like map to polynomial rings. | New theorems in analogue worlds. | Analogue is not original integers. | 8 | 8 | 5 | 9 |
| 33 | Generalized `qx+d` maps | Conway, Kurtz-Simon, Wirsching, many surveys | Study larger family of Collatz-like maps. | Shows family can be undecidable / wildly complex. | Original `3x+1` may use special constants. | 10 | 10 | 7 | 9 |
| 34 | FRACTRAN / computation universality | Conway, "Unpredictable iterations", FRACTRAN | Encode computation in arithmetic iteration. | Reveals deep reason generalizations are dangerous. | Negative result for general class, not proof/disproof of original. | 10 | 10 | 5 | 8 |
| 35 | Undecidability / `Pi^0_2` completeness | Kurtz-Simon 2007 | Prove generalized Collatz decision problem is very hard. | Major obstruction result. | Does not prove original Collatz undecidable. | 10 | 10 | 6 | 8 |
| 36 | Buchi arithmetic / automata non-definability | Dhiman-Pandey 2026 generalized maps | Study reachability definability for generalized maps. | Shows reachability can evade finite automata formalisms. | Family result, not original proof. | 9 | 9 | 4 | 8 |
| 37 | Formal languages / symbolic dynamics | String-rewriting and symbolic formulations | Encode orbits as words/rewrites. | Good representation and audit tool. | Language acceptance is not enough without arithmetic control. | 7 | 8 | 8 | 8 |
| 38 | Binary-string proofs | Many claimed proofs, e.g. binary-string arXiv attempts | Use binary representation to show progress toward `1`. | Sometimes rederives affine/parity laws. | Usually smuggles in monotonicity or ignores carries. | 6 | 5 | 10 | 10 |
| 39 | Carry/bit-level local analysis | Verification algorithms; binary-string variants | Track how `3n+1` carries propagate. | Useful for computation and local lemmas. | Carries can regenerate bad alignments. | 7 | 8 | 9 | 8 |
| 40 | Automata / finite-state decomposition | Petri nets, finite state papers, model-checking ideas | Represent bounded inverse graphs or recurrence classes. | Good finite visual/structural models. | Infinite reachability remains. | 7 | 7 | 8 | 9 |
| 41 | Petri nets | Recent MDPI-style Petri-net attempts | Model inverse graph transitions. | Visualization / bounded reachability. | Bounded net behavior does not prove unbounded convergence. | 7 | 6 | 5 | 9 |
| 42 | Operator algebras / C*-algebras | Mori 2024/2025 | Reformulate conjecture as irreducibility/no reducing subspace condition. | Elegant equivalence/implication framework. | Equivalent condition may be as hard as original. | 9 | 8 | 4 | 9 |
| 43 | Near-conjugacy to circle rotation | Honarvar Shakibaei Asli 2026 | Approximate Collatz by irrational rotation plus error. | Interesting geometric lens. | Bounded local error does not control cumulative arithmetic exceptional cases. | 8 | 8 | 5 | 8 |
| 44 | Coordinate systems / 3-smooth skeletons | Williams 2026 | Re-coordinate integers by 2/3 factorization skeletons. | May reveal structure of boundary exits. | New coordinates do not imply descent. | 8 | 8 | 7 | 8 |
| 45 | Sharkovsky / nonlinear dynamics analogies | Recent nonlinear dynamics preprints | Apply dynamical-systems ordering/phase concepts. | May organize phases. | Continuous-dynamics analogies often lose arithmetic specificity. | 7 | 6 | 6 | 8 |
| 46 | Paradoxical sequences after stopping time | Rozier-Terracol 2025/2026 | Study trajectories exceeding first term despite odd-ratio expectations. | Good warning against naive odd-ratio criteria. | Supports heuristics but does not prove finite occurrence. | 8 | 9 | 6 | 8 |
| 47 | Coefficient stopping time | Winkler 2017-2026 | Relate parity vectors to exponential Diophantine equations and congruence class trees. | Deterministic structures and finite coverage bounds. | Coefficient stopping time not proven equal to classical stopping time. | 8 | 8 | 5 | 8 |
| 48 | Markov chains / ergodic generalized maps | Matthews-Watts, Wirsching, AMS surveys | Treat generalized dynamics probabilistically. | Robust framework for typical behavior. | Markov/ergodic results lose individual orbits. | 7 | 8 | 7 | 8 |
| 49 | `5x+1`, `7x±1`, sibling maps | Lagarias-Weiss, many variant studies | Compare Collatz to related maps, some divergent/cyclic. | Excellent control systems. | Variant behavior warns but does not solve original. | 8 | 9 | 7 | 8 |
| 50 | `3n+3k` and scaled variants | Modern arXiv variants | Generalize or scale the recurrence. | Usually equivalent or tangential. | Often reparameterization, not new obstruction control. | 5 | 5 | 6 | 9 |
| 51 | Modular extensions `mod 2^p+2^q` | Recent generalized conjecture preprints | Invent broader families. | May unify toy maps. | Broader conjecture is harder and may be false. | 7 | 6 | 4 | 10 |
| 52 | Invariant residue partitions | Many "sets cover all integers" papers | Partition numbers into supposedly convergent classes. | Sometimes useful finite class taxonomy. | Must prove union is all positives; usually exactly the missing step. | 5 | 6 | 10 | 10 |
| 53 | Induction on odd numbers only | Syracuse formulation variants | Reduce to odd subsequence. | Standard simplification. | Odd-only map still has same hard reachability. | 3 | 5 | 10 | 10 |
| 54 | Minimal counterexample descent | Classical proof skeleton | Assume smallest counterexample and force smaller one. | Correct if universal descent found. | Finding smaller one is full problem. | 3 | 5 | 10 | 10 |
| 55 | Bounded excursion / max-height arguments | Record-holder and stopping-time literature | Bound peaks or total stopping time by functions of size. | Strong finite observations. | Any universal computable stopping-time bound would solve it; remains unproved. | 5 | 6 | 8 | 10 |
| 56 | Gamma / stopping-time asymptotic constants | Lagarias-Weiss, stochastic models | Predict record growth slopes. | Good benchmark for experiments. | Extremal deterministic tail unproved. | 6 | 7 | 8 | 8 |
| 57 | Fractal / Hausdorff dimension of survivor sets | 2-adic frontier/density analyses | Measure size of exceptional symbolic sets. | Shows survivors can be thin but nonempty. | Thin nonempty can still contain counterexamples. | 8 | 8 | 7 | 8 |
| 58 | Topological/frieze-pattern analogies | Coxeter, early AMS reprints | Find hidden combinatorial geometry. | Historical and aesthetic structure. | Not tied to universal descent. | 8 | 6 | 4 | 9 |
| 59 | `3x+1` as rewrite system | String rewriting papers | Normalize arithmetic into symbolic rules. | Useful for formalization. | Termination of rewrite system often equivalent to conjecture. | 7 | 7 | 7 | 9 |
| 60 | Formal proof assistant / CCChallenge-style formalization | ccchallenge.org and modern formalization efforts | Formalize existing literature. | Prevents fake proofs; clarifies gaps. | Formalizing partial results is not solving gap. | 6 | 8 | 6 | 8 |
| 61 | AI/LLM collaboration | Chang 2026; this repo's EDAP line | Use LLMs to explore, classify, refute. | High-throughput theorem-target mining. | Models hallucinate; need external verification. | 8 | 8 | 8 | 9 |
| 62 | "Paradigm exhaustion" claims | Chang 2026 abstract claims; broad AI surveys | Catalog frameworks and obstructions. | Useful meta-map. | Exhaustion theorem must itself be audited; does not solve. | 9 | 8 | 5 | 8 |
| 63 | Claimed proof by inverse-tree pathfinding | Wey-style arXiv proof claims and many web papers | PathFinding to root in virtual tree. | Usually an algorithmic narrative. | Typically assumes every node is connected to root. | 6 | 4 | 9 | 10 |
| 64 | Claimed proof by binary / continuous exponent interpolation | Binary-string and continuous-power attempts | Smooth discrete powers of 2/3 into continuous arguments. | Can produce plausible formulas. | Discrete integer/carry obstruction returns. | 7 | 5 | 9 | 10 |
| 65 | Claimed proof by complexity/Kolmogorov/surprise | Pseudo-proof archetype | Say counterexample would be too complex/surprising. | None as proof. | Complexity of description does not bound existence. | 8 | 3 | 7 | 10 |
| 66 | Claimed proof by prompt/axiom/narrative | AI pseudo-proof archetype | Treat desire for proof as premise. | None. | Category error; not mathematics. | 10 | 2 | 5 | 10 |
| 67 | Claimed proof by finite sampled contraction | Regression / fitted matrix archetype | Fit a contraction from sampled orbits. | Can classify samples. | No theorem about true nonlinear map. | 7 | 4 | 7 | 10 |
| 68 | Claimed proof by tautological detector | Repulsion identity archetype | Count events true by algebraic identity. | Detects tautology, not sufficiency. | Control maps refute sufficiency. | 7 | 5 | 8 | 10 |
| 69 | Prime/distribution heuristics | Folk and elementary attempts | Treat odd/even or divisibility as random primes. | Motivating intuition. | Independence assumptions false in rare tails. | 4 | 5 | 9 | 9 |
| 70 | Graph visualization / network science | Many popular and recent papers | Draw orbit graph/preimage graph. | Useful communication. | Pictures do not prove no escaping branch. | 5 | 4 | 10 | 10 |

## Weirdness / Strangeness Ranking

| Rank | Route | Why it is weird | Why it matters |
|---:|---|---|---|
| 1 | Generalized Collatz undecidability / FRACTRAN | Arithmetic iteration can simulate computation. | Any overly general proof route is suspect. |
| 2 | 2-adic shift conjugacy | Every parity sequence is natural in `Z_2`, including ghost orbits. | Explains why local parity arguments overclaim. |
| 3 | Negative integer cycles | The same ladder identities can be true where nontrivial cycles exist. | Best control test for sign-blind proof sketches. |
| 4 | Tao's 3-adic high-frequency mixing | Uses skew random walks on 3-adic cyclic groups to prove almost-bounded values. | Strongest modern progress; also clarifies the exceptional-set wall. |
| 5 | Buchi non-definability for generalized reachability | Finite-automaton arithmetic may be structurally too weak. | Warns against expecting finite automata to encode full reachability. |
| 6 | Operator-algebra irreducibility formulations | Collatz can be phrased as a C*-algebra reducibility condition. | Elegant equivalence, but may simply hide the same difficulty. |
| 7 | Polynomial `F_2[x]` analogues | Collatz-like maps become tractable in another algebraic world. | Useful contrast class; not proof over integers. |
| 8 | Paradoxical post-stopping sequences | Odd-ratio intuition can fail after first descent. | Directly relevant to our branch-pressure/repayment work. |
| 9 | Near-conjugacy to circle rotation | Collatz resembles an irrational rotation plus arithmetic error. | May expose phase drift; error control is the beast. |
| 10 | Coefficient stopping-time congruence trees | Deterministic trees of congruence classes encode stopping-time structure. | Similar to our frontier/certificate work; avoid rediscovery. |
| 11 | Benford/log laws | Leading digits and logs obey nontrivial statistical laws. | Distributional structure is real but not decisive. |
| 12 | Huge random-number verification | Individual numbers with billions of digits can be tested. | Demonstrates computation strength while proving almost nothing universal. |
| 13 | 3-smooth coordinate skeletons | Integers can be organized by 2/3 factorization triangles. | May reframe exits; needs proof of global descent. |
| 14 | Fractal survivor sets | Bad symbolic sets can be measure-thin yet infinite. | "Small" cannot mean "empty." |
| 15 | AI-produced proof/refutation ecology | Same model ecology can fabricate and refute. | Process novelty; mathematically dangerous without proof discipline. |

## The "Do Not Repeat Unless..." Ledger

| Tempting idea | Already tried as | Do not repeat unless you add |
|---|---|---|
| "Almost all descend, therefore all descend." | Terras/Everett/Krasikov/Tao line | A mechanism excluding the exceptional set. |
| "High odd density is exponentially rare." | Entropy/frontier estimates | A proof positive integers cannot remain in the rare set forever. |
| "The affine cylinder law explains everything." | Terras parity-vector machinery | A positivity-specific separator beyond sign-blind affine algebra. |
| "Every residue class eventually descends." | Descent certificates | Infinite-depth boundary control. |
| "All paths in inverse tree reach root." | Tree/pathfinding proofs | Proof that there is no infinite positive branch outside the root tree. |
| "No small cycles, so no cycles." | Cycle-exclusion literature | Uniform all-length Diophantine exclusion. |
| "Random drift is negative." | Lagarias-Weiss/stochastic heuristics | Deterministic tail control. |
| "A potential usually decreases." | Lyapunov/potential attempts | Hard-record and sibling-map verification plus universal inequality. |
| "A finite state model captures the behavior." | Automata/Petri/formal-language routes | Exact proof that abstraction is complete for unbounded integers. |
| "Generalized maps are hard/undecidable." | Conway/Kurtz-Simon | A special invariant unique to `3n+1`. |
| "Binary strings show carries dissipate." | Binary-string proof claims | A theorem controlling all carries/regeneration, not examples. |
| "A fitted matrix contracts." | Empirical regression pseudo-proof | A proven linearization/transfer theorem for the actual nonlinear dynamics. |
| "2-adic orbits are understood." | Bernstein-Lagarias/Lagarias rational cycles | Separation of positive integers from 2-adic ghost boundary. |
| "AI found a new proof skeleton." | LLM-assisted attempts | Independent formal proof or executable refutation-resistant certificate. |

## Current Repo-Specific Collision Points

Our current work overlaps heavily with known literature in these ways:

| In-repo object | Prior-art collision | Safe framing |
|---|---|---|
| Cylinder affine law | Terras parity-vector/cylinder machinery. | Classical reimplementation. |
| Parity-word bijection | Terras / 2-adic conjugacy background. | Classical lemma. |
| Spine ladder | Rational cycles / 2-adic periodic point structure. | Rediscovery with possible presentation margins. |
| Supercritical spine positivity localization | Related to negative cycle / rational periodic point literature. | Possible narrow margin; specialist review needed. |
| Regeneration functional | Same wall as powers of 2/3 digit problems and Mahler-style issues. | Theorem target, not result. |
| Branch-prefix pressure ledgers | New finite experiment line, but motifs/certificates overlap old descent-certificate methods. | Finite theorem mining only. |
| Algorithm attack matrix | Process/audit artifact. | Useful routing, not math progress. |

## Method Families Still Worth Pursuing

These remain worth attacking because they target a precise gap rather than repeating a solved partial strand.

1. **Positive-integer separator for 2-adic ghosts.**
   - Need: invariant that distinguishes finite positive shadows from persistent 2-adic boundary points.
   - Avoid: sign-blind affine identities.

2. **Regeneration bound after spine expulsion.**
   - Need: theorem controlling `v2(3^j u + delta)` across changing spines/phases.
   - Avoid: assuming randomness of low bits without proof.

3. **Retimed-pressure local lift theorem.**
   - Need: prove credit arrives before pressure in every live child transition.
   - Avoid: finite `d=25 -> 26` extrapolation without induction.

4. **Finite claims with SAT/SMT certificates.**
   - Need: solver-generated counterexamples or UNSAT certificates for local forbidden classes.
   - Avoid: solver output without proof log.

5. **Formalization of accepted lemmas.**
   - Need: make rediscovered classical pieces machine-checkable.
   - Avoid: prose-only "refereed by model" claims.

## Source Notes

The two Lagarias bibliographies are the authoritative starting point: the first covers 1963-1999 with 197 references; the second covers 2000-2009 with 134 entries. The AMS volume organizes the literature by survey, stochastic/computational papers, early reprints, and annotated bibliography. Modern source refresh added Tao 2019/2022, Hercher 2022/2023, Barina 2025, 2024-2026 analogue/operator/formal-language/geometric preprints, and AI-assisted Collatz exploration.

This atlas is therefore exhaustive at the **method-family** level, not literally every arXiv/web "proof" claim one by one. Low-quality proof claims are covered by archetype rows because listing each would add noise without improving avoidance.

## Bottom Line

Most Collatz attempts die at one of five walls:

1. **Exceptional-set wall:** almost all is not all.
2. **2-adic ghost wall:** parity words include non-positive / non-integer-real behavior.
3. **Regeneration wall:** bad alignment can disappear and later reappear.
4. **Infinite-family wall:** finite cycle/computation bounds never eliminate all lengths/starts.
5. **Abstraction-completeness wall:** trees, automata, operators, potentials, and coordinates often restate the conjecture in a new language.

Future work should only proceed when it names which wall it attacks and gives a falsifiable test for that attack.
