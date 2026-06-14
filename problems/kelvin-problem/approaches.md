# Approaches — The Kelvin Problem (Optimal Space Partition)

_Major strategies, partial results, and barriers._

The Kelvin problem asks for the unit-volume partition of $\mathbb{R}^3$ of least surface-area density $\sigma$. Unlike the planar honeycomb problem — solved by Hales in 2001 — no approach has produced a rigorous global lower bound matching any explicit structure. Below are the principal lines of attack.

## Explicit candidate structures (constructive upper bounds)

**Core idea.** Build an explicit periodic partition obeying Plateau's laws, relax it numerically, and read off its surface-area density as an upper bound on the true minimum.

**Best result.** The **Weaire–Phelan (WP) structure** (1993), built on the A15 / $\beta$-tungsten lattice, gives the lowest known value, $\approx 0.3\%$ below Kelvin's relaxed truncated octahedron. Kelvin's own structure remains the second-best and the historical benchmark. Extensive searches over tetrahedrally close-packed (TCP) / Frank–Kasper structures (C15, Z, $\sigma$, etc.) by Sullivan, Kusner, and others have found nothing beating WP.

**Barrier.** Constructions yield only upper bounds. There are infinitely many periodic and aperiodic candidates, and no argument rules out a still-better structure (or a non-periodic minimizer). An upper bound, however refined, cannot prove optimality.

## Geometric measure theory and minimal-cluster regularity

**Core idea.** Treat the partition as an area-minimizing cluster / $(M,\varepsilon,\delta)$-minimal set and use the regularity theory of Almgren, Taylor, and the structure of minimizing currents to constrain the geometry of any optimum.

**Best result.** Jean Taylor's 1976 theorem rigorously proves Plateau's laws — that singular sets of soap-film-like minimizers consist only of the $120°$ triple curves and tetrahedral-angle quadruple points. This tells us _what any minimizer must look like locally_ and confirms the Kelvin and WP geometries are admissible.

**Barrier.** Local regularity does not yield a global lower bound on density. The theory describes minimizers but cannot, by itself, single out the periodic structure that achieves the infimum, nor even guarantee a minimizer exists as a nice periodic foam.

## Lower bounds via isoperimetric / Hales-type methods

**Core idea.** Adapt the strategy that solved the honeycomb problem: assign to each cell a local area "charge," prove a per-cell isoperimetric-type inequality, and sum to bound the global density from below.

**Best result.** In the plane, Hales (1999/2001) proved every cell of area $1$ has perimeter $\ge$ that of the regular hexagon, settling the honeycomb. The hoped-for $3$D analogue would prove every unit-volume cell has surface area $\ge$ some threshold.

**Barrier.** The naïve $3$D analogue is **false**: the optimal _single_ cell shape minimizing isolated surface area is the sphere, which does not tile, and the best space-filling polyhedron-type bound (a single Kelvin or WP cell in isolation) does not give a matching global bound because curvature is shared between neighbors. The per-cell decoupling that works in $2$D breaks down; there is no known way to localize the $3$D inequality.

## Restriction to lattices / fixed combinatorics

**Core idea.** Fix a crystallographic lattice or a class of combinatorial types (e.g., all cells congruent, or bounded face count) and minimize within that restricted family, where the optimization may be tractable.

**Best result.** Within single-cell (monohedral, congruent-cell) tilings, Kelvin's relaxed truncated octahedron is widely believed optimal and is the best known; this is itself an open sub-problem. Within A15-type two-cell families, WP is optimal.

**Barrier.** WP beats every monohedral candidate precisely _because_ it uses two cell types — so restricting to congruent cells excludes the conjectured global optimum. Any restricted result is conditional on the (false-in-general) assumption that the optimum lies in the chosen family.

## Numerical optimization (Surface Evolver)

**Core idea.** Use Ken Brakke's **Surface Evolver** to evolve trial foams toward Plateau equilibrium under volume constraints, scanning many topologies for the lowest density.

**Best result.** This is how WP was found (1993) and how its density has been computed to high precision; it has effectively closed the search among known crystallographic candidates.

**Barrier.** Evolver finds local minima of given topology; it cannot certify a global minimum or exclude untested topologies. It is a discovery and verification tool, not a proof method. No interval-arithmetic or computer-assisted **proof** of even a local-minimality statement for WP in $\mathbb{R}^3$ has been completed.

## Summary of obstructions

The decisive gap is the absence of a global lower bound. Every approach delivers either a constructive upper bound (candidate structures, Evolver) or local geometric constraints (GMT regularity), but the honeycomb-style summable per-cell inequality that would close the gap has no working $3$D form. Even the weaker question — is Kelvin's foam a local minimizer? — lacks a complete proof.
