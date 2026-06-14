# Approaches — Sarnak's Möbius Disjointness Conjecture

_Major strategies, partial results, and barriers._

The conjecture asks for $\frac{1}{N}\sum_{n\le N}\mu(n)f(T^n x)\to 0$ for every zero-entropy $(X,T)$. Because $\mu$ is a fixed arithmetic object, every approach must combine sieve/analytic-number-theory input on $\mu$ with dynamical structure theory of the system. The strategies below are largely complementary; none yet reaches the full statement.

## The Bourgain–Sarnak–Ziegler (BSZ) orthogonality criterion

**Core idea.** A bounded sequence $\xi(n)$ is orthogonal to $\mu$ provided a *bilinear / type-II* estimate holds: for distinct primes $p,q$ the shifts $\xi(pn)$ and $\xi(qn)$ decorrelate on average,
$$
\sum_{p\le P}\frac{1}{p}\Big|\frac{1}{N}\sum_{n\le N}\xi(pn)\overline{\xi(qn)}\Big| \to 0.
$$
This reduces the multiplicative-function sum to a question about the system's own correlations under prime dilations, via Cauchy–Schwarz and a Turán–Kubilius / large-sieve input.

**Best result reached.** BSZ (2013) used it to prove disjointness for the horocycle flow and, combined with Green–Tao, for all **nilsystems**; it is the standard engine for verifying disjointness of concrete sequences.

**Barrier.** The criterion requires control of $\xi(pn)$ for *many* primes simultaneously — a uniform decorrelation that fails or is unknown for general low-complexity systems (e.g. many rank-one or substitution systems), so BSZ does not by itself reach arbitrary zero entropy.

## Structure theory of zero-entropy systems (ergodic-theoretic)

**Core idea.** Decompose a general zero-entropy system into tractable pieces — discrete/quasi-discrete spectrum, nilfactors, isometric extensions, joinings — and prove disjointness factor by factor. Sarnak's conjecture is a *joining* statement: $\mu$ should be disjoint, in Furstenberg's sense, from every zero-entropy measure-preserving system.

**Best result reached.** Frantzikinakis–Host (2018) proved the conjecture (in logarithmic average) for **all systems with countably many ergodic invariant measures**, the deepest general theorem; results also cover discrete-spectrum systems, quasi-discrete spectrum (Liu–Sarnak), and certain distal systems.

**Barrier.** Systems with *uncountably many* ergodic measures and genuinely "wild" zero-entropy behavior (positive but sub-exponential complexity, certain smooth area-preserving flows) escape the structure theorems; the general decomposition needed is not available.

## The Chowla route and entropy decrement

**Core idea.** Prove (a form of) the Chowla conjecture — vanishing of correlations of $\lambda$/$\mu$ — which *implies* Sarnak. Tao's **entropy decrement argument** controls correlations $\frac{1}{\log N}\sum \lambda(n)\lambda(n+h)/n$ by exploiting the multiplicativity of $\lambda$ across scales $p$, paying a slowly decaying entropy cost.

**Best result reached.** Tao (2016) proved the **logarithmically-averaged two-point Chowla**; Tao–Teräväinen extended to odd-order log-Chowla and to log-Sarnak; Tao (2017) proved log-Sarnak $\iff$ log-Chowla.

**Barrier.** The entropy decrement loses a logarithm, yielding only **logarithmic** Cesàro averages $\frac1{\log N}\sum \cdot/n$, not the natural $\frac1N\sum$. Upgrading log-averages to ordinary averages is a fundamental open obstacle; even two-point Chowla with ordinary averaging is unproven.

## Exponential-sum / type-I–type-II (Vaughan / Heath-Brown) methods

**Core idea.** Expand $\mu$ via Vaughan's or Heath-Brown's identity into bilinear forms and treat $\sum_n f(T^n x)$ as an arithmetic exponential sum; bound type-I (smooth) and type-II (bilinear) pieces using equidistribution of the dynamical orbit.

**Best result reached.** Decisive for "algebraic" sequences: Davenport's bound for $e(n\alpha)$, Mauduit–Rivat for the Thue–Morse and Rudin–Shapiro (automatic) sequences, and polynomial-phase / nilsequence bounds.

**Barrier.** Requires the orbit sums to behave like genuine exponential sums with usable cancellation; for systems without algebraic/arithmetic structure (generic low-complexity, interval exchanges of high genus) the type-II estimates are inaccessible.

## Sieve and "averaged" / almost-all approaches

**Core idea.** Prove disjointness on average over a parametrized family, or for almost every point/parameter, using sieve majorants for $\mu$ and ergodic averaging — weaker than pointwise-for-all-$x$ but often attainable.

**Best result reached.** Disjointness for almost every interval-exchange / translation-flow direction; "on average" Chowla (Matomäki–Radziwiłł–Tao) and the landmark **Matomäki–Radziwiłł theorem** on multiplicative functions in short intervals, which underlies most recent progress.

**Barrier.** Averaged statements do not yield the required *every $x$, every $f$* conclusion; exceptional orbits/parameters cannot be excluded by these methods alone.

## Known obstructions and negative results

- The conjecture is **false without the zero-entropy hypothesis**: positive-entropy systems (e.g. full shifts) carry observables correlating with $\mu$, so entropy is not a removable technicality.
- Sarnak does *not* imply Chowla in general (only the converse and the log-equivalence are known), so the two cannot be freely interchanged at the Cesàro level.
- The log-to-ordinary-average gap is a genuine barrier: several results are known *only* logarithmically, and no general device converts them.
- Möbius–Liouville sums are sensitive to a hypothetical Siegel zero; while disjointness statements are usually unconditional, the strongest quantitative forms interact with the absence of exceptional characters.
