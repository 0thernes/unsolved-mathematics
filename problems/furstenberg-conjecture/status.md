# Status & Frontier — Furstenberg's ×2 ×3 Conjecture

_Where the problem stands and what a resolution would require._

**Status: open (`active-progress`).** No proof and no counterexample exists. The metadata status is `active-progress`: a major conditional theorem is established, the full statement is not. Nothing here should be read as a claim of resolution.

## What is known (unconditional)

- **Topological rigidity (Furstenberg, 1967, proved).** Every closed subset of $\mathbb{T}$ invariant under $x \mapsto 2x$ and $x \mapsto 3x$ is finite or all of $\mathbb{T}$. This is the closed-set analogue and is settled; it is *not* the measure conjecture.
- **Positive-entropy rigidity (Rudolph, 1990; Johnson, 1992; Host, 1995).** Any $\langle T_2, T_3\rangle$-invariant ergodic measure $\mu$ with $h_\mu(T_2) > 0$ is Lebesgue measure. Key paper: D. J. Rudolph, *"×2 and ×3 invariant measures and entropy,"* Ergodic Theory and Dynamical Systems, **10** (1990), 395–406. Johnson (1992) generalized to all multiplicatively independent $p, q$.
- **Cousin conjectures resolved (2019).** Furstenberg's intersection/slicing conjectures (Hausdorff-dimension statements about $\times 2$ vs. $\times 3$ invariant sets) were proved independently by P. Shmerkin and by M. Wu. These are related but distinct from the measure-rigidity conjecture and do not imply it.

## What is known (conditional)

- The conjecture is **equivalent to ruling out the zero-entropy case**: it would follow at once if one proved that no non-atomic $\langle T_2, T_3\rangle$-invariant ergodic measure has $h_\mu(T_2) = 0$ unless it is atomic. Positive entropy is fully handled.
- Various sufficient conditions (positive Hausdorff dimension under both maps, certain Fourier-decay or sum–product hypotheses) imply the conclusion, but each is currently unverifiable for a hypothetical exotic measure.

## What a full resolution requires

A complete proof must control **zero-entropy, deterministic** invariant measures — objects invisible to every entropy-based tool. One must show that joint invariance under two multiplicatively independent expansions is *itself* incompatible with low dynamical complexity unless the measure is Lebesgue or atomic. No existing mechanism (entropy, conditional measures along leaves, Fourier analysis, additive combinatorics) reaches this regime.

## Plausible routes

1. **Higher-rank measure rigidity transferred from homogeneous dynamics** — adapt the Einsiedler–Katok–Lindenstrauss conditional-measure machinery (Littlewood's conjecture, 2006) to the non-invertible endomorphism setting; the obstacle is the absence of unipotent/Ratner structure.
2. **Additive-combinatorial expansion** — leverage sum–product and decoupling estimates to force entropy to be positive or the measure to be Lebesgue, attacking the zero-entropy gap directly.
3. **Fractal-geometry crossover** — extend the $L^q$-norm and CP-chain methods that resolved the intersection conjecture (Shmerkin, Wu, 2019) from dimension statements to full measure classification.

Expert consensus: a counterexample almost certainly does not exist, but proving so likely requires a genuinely new idea about zero-entropy systems.

## Related problems

- [Littlewood's conjecture](../littlewood-conjecture/) — the Diophantine cousin whose exceptional set was bounded by the same measure-rigidity techniques.
- [Schanuel's conjecture](../schanuel-conjecture/) — another deep multiplicative-independence question in transcendence/number theory.
- [Montgomery's pair correlation conjecture](../montgomery-pair-correlation/) — a parallel rigidity/equidistribution problem in a number-theoretic spectral setting.
- [Riemann hypothesis](../riemann-hypothesis/) — the archetypal equidistribution/spectral conjecture whose methods periodically touch homogeneous dynamics.
