# Collatz Failed Attempts and Idea Atlas

Date: 2026-07-04

Purpose: map the known Collatz literature and failed/partial routes so future work does not unknowingly repeat old ideas. This file is a strategic atlas, not a proof and not a full bibliographic substitute.

Primary sources used:

- CCChallenge live literature database, 370 entries, scraped into [`COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md`](COLLATZ-LITERATURE-CCCHALLENGE-370-SNAPSHOT-2026-07-04.md).
- Companion no-repeat map: [`COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md`](COLLATZ-FAILED-IDEAS-ATLAS-2026-07-04.md), which expands the route list into 150 approach families and area rankings.
- Lagarias annotated bibliographies: 1963-1999 and 2000-2009.
- Lagarias overview and AMS volume *The Ultimate Challenge: The 3x+1 Problem*.
- Local repo files: `papers.md`, `attempts.md`, `approaches.md`, `history.md`, `status.md`.
- Live source checks for Tao, Barina, Hercher, CCChallenge, Knight, and the Opfer proof-claim episode.

## Executive Verdict

Nearly every natural Collatz route has been tried in some form:

- density and "almost all" descent;
- stochastic/random-walk heuristics;
- cycle exclusion by continued fractions and linear forms in logarithms;
- 2-adic conjugacy and parity vectors;
- inverse trees and sufficient sets;
- finite computation and distributed verification;
- generalized maps and undecidability;
- analytic/functional/linear-algebraic encodings;
- modular/residue automata;
- rational and negative cycles;
- proof claims via hidden monotonicity, potential functions, or fitted models.

The strongest truth is not "nothing works." Many routes work beautifully on partial questions. They fail at the same wall: **none supplies a uniform mechanism excluding the exceptional positive-integer orbit.**

The highest future value is in routes that explicitly consume structure old methods leave on the floor: intercepts, integer finiteness, regeneration of 2-adic alignment, sibling-map controls, and machine-checkable finite certificates.

## Rating Scales

| Score | Meaning |
|---:|---|
| Weirdness 1 | Standard number-theory/computation route. |
| Weirdness 5 | Nonstandard but established in the literature. |
| Weirdness 10 | Deeply strange, generalized, undecidable, or "beyond the beyond." |
| Repetition Risk 1 | Unlikely we will accidentally duplicate it. |
| Repetition Risk 10 | Extremely easy to reinvent badly. |
| Future Value 1 | Mostly historical caution. |
| Future Value 10 | Still worth building on, with guardrails. |

## Master Route Ranking

| Rank | Route / Attempt Family | Representative Papers / Names | What It Achieved | Why It Has Failed So Far | Weirdness | Repetition Risk | Future Value |
|---:|---|---|---|---|---:|---:|---:|
| 1 | Density / almost-all stopping time | Terras 1976; Everett 1977; Tao 2019/2022 | Density-one finite stopping; almost all orbits attain almost bounded values. | Exceptional set remains uncontrolled; "almost all" cannot become "all." | 6 | 9 | 10 |
| 2 | Stochastic / random-walk models | Lagarias-Weiss 1992; Crandall; Kontorovich-Miller; Lagarias-Soundararajan | Explains negative drift, stopping-time distributions, Benford behavior. | Heuristics are blind to worst-case deterministic exceptions. | 7 | 10 | 9 |
| 3 | Cycle exclusion by Diophantine approximation | Steiner; Eliahou; Simons; Simons-de Weger; Hercher 2023 | Excludes low-complexity cycles; any cycle must be enormous. | Finite lower bounds never rule out all cycle lengths. | 5 | 8 | 9 |
| 4 | 2-adic parity-vector conjugacy | Hedlund lineage; Lagarias 1985; Lagarias 1990; Bernstein-Lagarias 1996; Monks/Yazinski/Kraft | Exact conjugacy to shift; rational/2-adic cycles organized. | 2-adic typicality does not pin down positive integers. | 9 | 8 | 10 |
| 5 | Inverse tree / preimage tree density | Applegate-Lagarias; tree-search methods; inverse-iteration papers | Counts large subtrees leading to 1; gives density lower bounds. | Tree mass can be large while still missing a thin counterexample path. | 6 | 8 | 8 |
| 6 | Krasikov inequalities / difference inequalities | Krasikov; Applegate-Lagarias; Krasikov-Lagarias 2003 | Strongest explicit lower bound family for convergent set, e.g. `x^0.84`. | Positive-exponent gap remains below full density. | 5 | 7 | 8 |
| 7 | Computational verification | Oliveira e Silva; Roosendaal; Barina 2020/2025; Angeltveit 2026 | Verified all starts below huge bounds, now `2^71`; improves cycle floors. | Finite verification cannot close infinite domain. | 3 | 10 | 8 |
| 8 | Generalized Collatz / undecidability | Conway 1972/1987; Kurtz-Simon 2007; FRACTRAN/TC work | Shows broad Collatz-like families simulate computation / can be undecidable. | Negative backdrop only; does not settle classic `3n+1`. | 10 | 7 | 9 |
| 9 | Rational / negative / nonpositive cycles | Böhm-Sontacchi; Lagarias rational cycles; Halbeisen-Hungerbühler | Reveals negative cycles, rational periodicity, cycle families. | Explains why sign-blind arguments overclaim; does not separate positives. | 9 | 8 | 9 |
| 10 | Sufficient sets / arithmetic progressions | Andaloro; Monks 2006 | Shows many subsets/progressions are sufficient reductions. | Reduction can be equivalent-strength; does not prove base set converges. | 5 | 8 | 7 |
| 11 | Semigroup / operator algebra | Applegate-Lagarias semigroup; affine semigroup work | Encodes iteration as generated affine maps. | Algebraic encoding preserves difficulty; no monotone invariant. | 7 | 7 | 8 |
| 12 | Functional equations / analytic continuations | Opfer 2011; assorted analytic claimed proofs | Attempted continuous/complex analytic leverage. | Hidden circularity or unjustified extension from discrete orbit to analytic control. | 7 | 8 | 3 |
| 13 | Linear algebra / matrix encodings | Alves et al.; local fitted-matrix failures | Repackages transitions, sometimes useful computationally. | A matrix model is not the nonlinear integer dynamics unless soundly exact. | 5 | 10 | 5 |
| 14 | Modular automata / finite residue graphs | many residue-class papers; local frontier tools | Exact finite-depth structure and prefix/cylinder checks. | Every fixed depth leaves survivors; all-ones/2-adic boundary persists. | 6 | 9 | 9 |
| 15 | Stopping-time records / heights / excursions | Garner; Oliveira e Silva; Applegate-Lagarias | Deep empirical map of hard finite starts. | Records reveal extreme tail but cannot bound all future starts. | 4 | 8 | 8 |
| 16 | Benford / leading-digit / distribution laws | Kontorovich-Miller; Lagarias-Soundararajan | Confirms randomness-like statistical behavior. | Distributional truth is compatible with a thin exceptional set. | 6 | 6 | 5 |
| 17 | Generalized `qx+r`, `3x+d`, `px+q` variants | Matthews-Watts; Franco-Pomerance; Simons generalized work | Shows how special or non-special `3x+1` is among relatives. | General route often proves too much or meets counterexamples in sibling systems. | 8 | 8 | 8 |
| 18 | Topological/fractal/geometric visualizations | many amateur/professional expository routes | Excellent intuition, sometimes useful for tree and dimension measurements. | Visual pattern recognition rarely supplies a universal invariant. | 7 | 10 | 4 |
| 19 | Probabilistic lower bounds for connected-to-1 count | Daudin and related heuristic estimates | Refines expected density/tree-size pictures. | Heuristic lower bound is not a proof of all convergence. | 5 | 7 | 5 |
| 20 | Formal verification of literature | CCChallenge; proof assistants | Hardens known partial results and prevents false proofs. | Formalizes existing truth; does not invent missing theorem. | 6 | 2 | 10 |
| 21 | Busy Beaver / Turing machine encodings | Conway; Michel; BB challenge-adjacent work | Shows Collatz-like statements can sit near computability frontiers. | Classic Collatz is not reduced to a solved halting instance. | 10 | 5 | 7 |
| 22 | Parity-sequence exact formulas | Terras, Böhm-Sontacchi, Lagarias, many cyclic formula papers | Complete formula for any fixed parity word. | Fixed-word exactness does not control which words positive orbits realize forever. | 8 | 10 | 10 |
| 23 | Potential / Lyapunov functions | many claimed proofs; local failed proof family | Natural dream: find decreasing energy. | Known candidates either decrease on average or assume escape. | 6 | 10 | 8 |
| 24 | Local macro rules / compressed odd maps | Syracuse map literature, local branch-prefix work | Simplifies branch structure and exposes runs/bursts. | Compression can hide regeneration and carry effects. | 6 | 9 | 8 |
| 25 | Claimed elementary proofs | Thwaites; Opfer; many preprints/arXiv-like uploads | Occasionally reveal useful reformulations. | Usually smuggle "almost all => all", circularity, finite-to-infinite leap, or empirical proof. | 8 | 10 | 2 |

## Weirdness / Beyond Ranking

| Weirdness Rank | Zone | Why It Is Strange | Known Lesson |
|---:|---|---|---|
| 1 | Generalized Collatz undecidability | Simple arithmetic maps can encode computation. | Any proof must exploit exact `3` and `2`, not generic Collatz-ness. |
| 2 | 2-adic conjugacy to shift | Collatz becomes a shift map on `Z_2`, where all parity words are legal. | Perfect symbolic order exists in the wrong space. |
| 3 | Negative cycles | `3n+1` on negatives has real nontrivial cycles `-1`, `-5`, `-17`. | Sign-blind arguments are dangerous. |
| 4 | Rational cycles / odd-denominator rationals | Dynamics naturally extend beyond integers. | Positive-integer specificity is the hard constraint. |
| 5 | Busy Beaver / small machines | Collatz-like claims appear near computation-limit phenomena. | Impossibility flavor does not imply classic Collatz undecidability. |
| 6 | Tao's logarithmic-density theorem | Huge advance that still cannot touch a possible null exceptional orbit. | The problem lives in the exceptional set. |
| 7 | Hercher / Diophantine cycle floors | A finite verification bound plus log approximations force absurd cycle length. | Enormous is not impossible. |
| 8 | Sufficient arithmetic progressions | Many arbitrary-looking subsets are enough to prove the full conjecture. | Reduction can preserve full difficulty. |
| 9 | Benford/randomness laws | Orbits obey statistical laws while individual fate remains open. | Randomness is explanatory, not coercive. |
| 10 | Inverse-tree abundance | Huge forests flow to 1 but may still miss a pathological branch. | Counting mass is not covering all points. |

## Do-Not-Repeat List

These are the routes most likely to waste time if restarted naively.

1. **"Average multiplier is below 1, therefore all orbits descend."**
   - Already known; invalid because worst-case exceptional paths are not average.

2. **"Almost all descend, therefore all descend."**
   - Terras/Everett/Tao already do the almost-all part at high sophistication.

3. **"Finite computation plus no counterexample implies theorem."**
   - Computation helps cycle floors but cannot close infinity.

4. **"All parity words are random/independent."**
   - As a 2-adic model, yes; as a positive-integer orbit theorem, no.

5. **"Cycle lower bound is enormous, therefore no cycle."**
   - Hercher/Eliahou/Simons already push this far; finite lower bound remains finite.

6. **"Find a matrix/potential fitted to sampled orbits."**
   - Useful heuristic; not proof unless it soundly over-approximates exact dynamics.

7. **"Use inverse tree pictures to show all nodes are covered."**
   - Must prove coverage, not just observe growth.

8. **"Use 2-adic conjugacy to claim convergence."**
   - The conjugacy explains symbolic dynamics but includes nonpositive/rational ghosts.

9. **"Generalize Collatz and prove the family."**
   - Broad families contain counterexamples or undecidable behavior.

10. **"Analytic continuation / smooth interpolation controls integer orbit."**
    - The dangerous step is almost always assuming the discrete result inside the continuous extension.

## Failure Modes by Claim Type

| Claim Type | Typical Old Failure | Required Future Guardrail |
|---|---|---|
| Divergence exclusion | Controls density, not the exceptional orbit. | Name the exceptional-set mechanism. |
| Cycle exclusion | Bounds finite cycle complexity only. | State exact remaining infinite family. |
| Parity-word proof | Ignores intercept/sign/positive-integer restriction. | Test on `3n-1`, negatives, rationals. |
| Potential proof | Decreases in sampled or average cases only. | Prove universal monotone inequality. |
| Computational proof | Exhausts a finite range. | Emit exact finite domain and no universal language. |
| Tree proof | Counts many preimages of 1. | Prove every positive integer enters tree. |
| Formal proof | Formalizes a partial theorem. | Do not claim it formalizes Collatz. |
| LLM/AI proof | Inflates plausible algebra into theorem. | Require claim manifest, source, checker, counterexample slot. |

## Literature Families and Local Route Tags

### Density / Almost-All

Representative entries: `Terras1976`, `Terras1979`, `Everett1977`, `KrasikovLagarias2003`, `Tao2022`, Applegate-Lagarias density papers.

Local route tag: `density-exceptional-set`.

Current lesson: this is the most powerful proven route for divergence but cannot see a measure-zero counterexample.

### Cycles / Diophantine

Representative entries: `Steiner1977`, `Eliahou1993`, `SimonsWeger2005`, `Hercher2023`, `Knight2026`, `RhinToffin1986`, Belaga, Halbeisen-Hungerbühler.

Local route tag: `cycle-diophantine-ladder`.

Current lesson: avoid redoing crude continued-fraction bounds unless we add a new effective-log-forms improvement, high-cycle classification, or formal proof certificate.

### 2-Adic / Conjugacy / Symbolic Dynamics

Representative entries: `Lagarias1985`, `Lagarias1990`, `BernsteinLagarias1996`, `MonksYazinski2004`, `KraftMonks2010`, shift-endomorphism papers.

Local route tag: `2adic-spine-regeneration`.

Current lesson: this is closest to the repo's spine-ladder work; future work must clearly say which parts are rediscovery and which are new packaging.

### Computation / Records / Verification

Representative entries: Oliveira e Silva, Roosendaal, Barina, Angeltveit, Applegate-Lagarias lower-bound record work.

Local route tag: `finite-verification`.

Current lesson: useful for falsification and cycle floors; never a complete proof.

### Generalized Maps / Undecidability / Computation Theory

Representative entries: `Conway1972`, `Conway1987`, `KurtzSimon2007`, FRACTRAN and generalized Collatz papers.

Local route tag: `generalized-map-warning`.

Current lesson: any argument invariant under broad generalized maps is probably too weak.

### Sufficient Sets / Reductions

Representative entries: Andaloro, Monks, arithmetic-progression sufficiency papers.

Local route tag: `reduction-equivalence-risk`.

Current lesson: a beautiful reduction can still be full-strength equivalent to Collatz.

### Analytic / Linear Algebra / Functional Reformulations

Representative entries: Alves-Graca-Dias-Ramos linear algebra, Opfer episode, miscellaneous analytic approaches.

Local route tag: `encoding-not-proof`.

Current lesson: encodings are useful only when they add a new invariant or certified bound.

### Heuristic / Distribution / Benford / Randomness

Representative entries: Lagarias-Weiss, Kontorovich-Miller, Lagarias-Soundararajan, Daudin.

Local route tag: `random-model-calibration`.

Current lesson: use these for expected behavior and anomaly detection, not as proof.

## Highest-Value Unknown-Unknown Zones

These are not "untried"; they are under-controlled.

1. **Regeneration of 2-adic alignment after expulsion.**
   - Old literature has 2-adic conjugacy; repo work has a spine-ladder package.
   - The hard part is not initial alignment but regenerated alignment under powers of 3.

2. **Positive-integer separation from 2-adic/rational ghosts.**
   - Negative/rational cycles show exact structures that positive arguments must exclude.

3. **Intercept-sensitive parity statistics.**
   - Parity words alone are too blind; intercepts distinguish `3n+1` from sibling maps.

4. **Finite certificate families with proof objects.**
   - SAT/SMT/Lean-style finite certificates could prevent local overclaiming.

5. **Cycle classifications beyond "low/high/circuit" categories.**
   - Knight 2026 suggests modern cycle taxonomy is still moving.

6. **Exceptional-set arithmetic after Tao.**
   - The density frontier is now about the residual null set.

7. **Sibling-map controls as proof filters.**
   - Every mechanism should be tested against `3n-1`, `5n+1`, negatives, and rationals.

## Future Research Rules

Before pursuing a "new" Collatz idea, run this checklist:

1. Is it just average negative drift?
2. Is it just a parity-vector formula?
3. Is it just a finite residue computation?
4. Is it just a cycle lower bound?
5. Is it just a sufficient-set reduction?
6. Is it just 2-adic conjugacy?
7. Is it invariant under `3n-1` or negative cycles?
8. Does it use positivity anywhere real?
9. Does it control regenerated alignment, not only initial alignment?
10. Can it name a counterexample shape if false?

If the answer to 1-7 is yes and 8-10 is no, it is probably old wine in a shiny bottle.

## Immediate Repo Actions

1. Treat the 370-entry snapshot as the local "prior-art floor".
2. Add any new route to `CLAIM-MANIFEST-TEMPLATE.md` before it becomes a theorem file.
3. For each future proof attempt, assign one route tag from this atlas.
4. Require a sibling-control test for any parity/statistical/potential mechanism.
5. Require a "prior-art overlap" paragraph for all spine, 2-adic, cycle, density, and sufficient-set claims.
6. Update `papers.md` from the 370-entry snapshot, but only after source-checking individual entries.

## Bottom Line

The old literature is not barren. It is dense, strange, and full of partial victories. The danger is not missing all prior art; the danger is rediscovering a known partial structure and mistaking the last missing quantifier for a solved theorem.

Future work should aim at the places old routes explicitly fail:

- exceptional-set control beyond density;
- cycle exclusion beyond finite complexity;
- positive-integer separation from 2-adic/rational ghosts;
- regeneration control for powers of 3 modulo powers of 2;
- proof certificates for finite claims;
- sibling-map falsification of mechanisms.
