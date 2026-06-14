# Approaches — Furstenberg's ×2 ×3 Conjecture

_Major strategies, partial results, and barriers._

The conjecture is unproven, but a sharp dichotomy organizes all known progress: every approach succeeds when the invariant measure has **positive entropy** and fails in the **zero-entropy** regime. Below, $\mu$ denotes a $\langle T_2, T_3\rangle$-invariant ergodic non-atomic measure on $\mathbb{T}$; $h_\mu(T_p)$ is its entropy under $x \mapsto px$.

## Rudolph's entropy method (the positive-entropy theorem)

**Core idea.** Rudolph (1990) studied the action of the $\times 2, \times 3$ semigroup together with its natural extension and the structure of conditional measures along the "common refinement" of the two partitions into digit cylinders. The crux is that positive entropy forces the conditional measures of $\mu$ on appropriate fibers to be genuinely spread out; combined with the multiplicative independence of $2$ and $3$, this spreading propagates under both maps until $\mu$ must be Lebesgue.

**Best result.** If $h_\mu(T_2) > 0$ (equivalently $h_\mu(T_3) > 0$, since the two are proportional for ergodic joint-invariant measures with the same entropy-rate constraint), then $\mu$ is Lebesgue measure. Johnson (1992) extended this to all multiplicatively independent $p, q \ge 2$; Host (1995) and Lindenstrauss (et al.) gave alternative proofs and refinements.

**Barrier.** The argument is fundamentally entropy-driven and gives *no information* when $h_\mu(T_2) = 0$. Zero entropy is exactly where a putative counterexample would live, so the method, by design, cannot close the conjecture.

## The zero-entropy obstruction

**Core idea.** A non-Lebesgue counterexample must have zero entropy under both maps. Such a measure would be a deterministic, "low-complexity" object that is nonetheless invariant under two independent expansions — a configuration no one can construct and no one can exclude.

**Best result.** Conditional results: *if* one could show every joint-invariant ergodic measure has either zero or "full" entropy with no intermediate behavior, or *if* one could rule out positive-dimension zero-entropy measures, the conjecture would follow. These remain conjectural.

**Barrier.** There is no known mechanism — entropy, recurrence, or harmonic-analytic — that constrains zero-entropy joint-invariant measures. This is widely seen as the true heart of the problem.

## Host's normal-numbers / disjointness approach

**Core idea.** Host (1995) reproved positive-entropy rigidity by showing that for $\mu$-typical points the base-$p$ digit sequence is "normal" in a strong sense, exploiting the independence of the two expansions through a martingale/conditional-expectation argument rather than Rudolph's coding directly.

**Best result.** An independent proof of the Rudolph–Johnson theorem, plus pointwise statements about normality of digits for positive-entropy invariant measures (with applications to a.e. equidistribution of $\{2^n 3^m x\}$).

**Barrier.** Same entropy wall: the disjointness/normality input degenerates at zero entropy.

## Higher-rank homogeneous-dynamics analogy

**Core idea.** Reframe the commuting endomorphisms as a rank-$\ge 2$ abelian action and import the measure-classification machinery developed for diagonal flows on homogeneous spaces (Margulis, Einsiedler, Katok, Lindenstrauss). The conditional-measure / entropy-from-positive-leaf techniques used to attack **Littlewood's conjecture** (Einsiedler–Katok–Lindenstrauss, 2006) are structurally parallel.

**Best result.** Spectacular successes in the homogeneous setting (Littlewood exceptional set has Hausdorff dimension $0$; classification of positive-entropy measures for higher-rank diagonalizable actions). These confirm that "higher rank ⇒ rigidity" is the right paradigm.

**Barrier.** The homogeneous theorems all require a positive-entropy or positive-dimension hypothesis along some direction; the endomorphism (non-invertible, no homogeneous structure) setting lacks the unipotent dynamics that make Ratner-type arguments work. Transferring the technique to the zero-entropy $\times 2, \times 3$ case has not succeeded.

## Fourier-analytic and additive-combinatorial inputs

**Core idea.** Use that $\mu$ invariant under $T_p$ forces relations among its Fourier coefficients $\hat\mu(k)$ and $\hat\mu(pk)$; multiplicative independence then over-constrains the spectrum. Related: Bourgain-type sum–product and decoupling estimates that quantify expansion.

**Best result.** Quantitative equidistribution and dimension estimates (e.g. work connecting to Hochman–Shmerkin and to Furstenberg's slicing/intersection conjectures, the latter resolved in 2019 by Shmerkin and by Wu).

**Barrier.** Fourier decay alone does not detect zero-entropy singular measures finely enough; the slicing-conjecture techniques address Hausdorff-dimension statements, not the full invariant-measure classification.

## Summary of the obstruction

Every successful line of attack converts to a statement that is true under positive entropy and silent under zero entropy. The open problem is essentially: **construct, or prove the nonexistence of, a zero-entropy non-atomic measure jointly invariant under two multiplicatively independent expansions.** No counterexample is believed to exist, but no current technique reaches the regime where one could hide.
