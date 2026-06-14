# Status & Frontier — The Kelvin Problem (Optimal Space Partition)

_Where the problem stands and what a resolution would require._

**Status: open.** No partition of $\mathbb{R}^3$ into unit-volume cells has been proven to minimize surface-area density. The problem has been open since Kelvin posed it in 1887.

## What is known

**Unconditional facts.**
- Kelvin's relaxed truncated-octahedron foam (1887) is an explicit, Plateau-law-satisfying partition with density $\sigma \approx 5.306$ (area per cell of unit volume); it is **not** the optimum.
- The **Weaire–Phelan structure** (Weaire & Phelan, 1994, _Phil. Mag. Lett._ **69**, 107–110, DOI 10.1080/09500839408241577), built on the A15 / $\beta$-tungsten lattice with two equal-volume cell types ($12$- and $14$-faced), has density about $0.3\%$ below Kelvin's. This is an explicit, rigorous **upper bound** and the lowest value known.
- **Plateau's laws hold for any minimizer** (Taylor, 1976): the singular set of an area-minimizing foam consists only of $120°$ triple curves meeting four-at-a-time at the tetrahedral angle $\approx 109.47°$. Both Kelvin and WP are admissible under this constraint.
- The planar analogue is fully settled: the regular hexagonal honeycomb is optimal (Hales, 1999/2001).

**Conditional / numerical results.**
- Extensive Surface Evolver searches over TCP and Frank–Kasper structures have found nothing below WP, supporting (but not proving) the conjecture that **WP is the global optimum**.
- Numerical evidence indicates both Kelvin and WP are stable local minima, but no published theorem establishes local minimality of WP (or Kelvin) in $\mathbb{R}^3$ via a verified second-variation / interval-arithmetic argument.

## What a full resolution requires

A complete solution must (1) establish existence of a minimizing partition in a suitable class, and (2) supply a **global lower bound** on density matching some explicit structure's upper bound. The decisive missing ingredient is a $3$D analogue of Hales' summable per-cell isoperimetric inequality. The naïve localization fails because, unlike the plane, the optimal isolated cell (a sphere, isoperimetric quotient $1$) does not tile, and curvature is shared between neighboring cells, so per-cell area cannot be decoupled. Even the weaker target — proving WP is a **local** minimizer — remains open.

## Plausible routes

- **Hales-style lower bounds**: invent a localizable $3$D area inequality, summing over cells to match the WP density. No working form is known; this is the main obstruction.
- **Computer-assisted local minimality**: a rigorous second-variation analysis of WP via interval arithmetic, certifying it as a strict local minimum — a realistic medium-term goal that would not, however, settle global optimality.
- **GMT existence + structure theory**: combine Almgren–Taylor regularity with periodicity arguments to constrain minimizers to a finite candidate list, then compare.
- **New candidate structures**: continued searches could, in principle, dethrone WP as the honeycomb conjecture's $2$D answer was never in doubt but the $3$D answer twice surprised the field.

No development to date (as of 2026) has produced a global lower bound, so the conjecture "Weaire–Phelan is optimal" stands unproven, and Kelvin's century-old question remains unanswered.

## Related problems

- [The Honeycomb / planar analogue context — kakeya-conjecture](../kakeya-conjecture/) — adjacent extremal-geometry and incidence problem.
- [Hilbert's Sixteenth Problem](../hilbert-sixteenth-problem/) — another classical geometry problem on configurations in space.
- [Hadwiger Conjecture](../hadwiger-conjecture/) — extremal/covering geometry of convex bodies.
- [Moving Sofa Problem](../moving-sofa-problem/) — a fellow geometric optimization problem with a conjectured-but-unproven optimum.
- [Inscribed Square Problem](../inscribed-square-problem/) — a long-open elementary-geometry question in the same low-traffic, high-difficulty register.
