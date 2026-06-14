# Attempts — The Kelvin Problem (Optimal Space Partition)

_Notable attempts, near-misses, retracted proofs._

## Kelvin's own conjecture (1887) — the long-standing presumed answer

Kelvin proposed his relaxed truncated-octahedron foam not merely as a candidate but with the strong belief that it was optimal. For over a century the structure functioned as the _de facto_ answer in physics and crystallography texts. This was never a proof — Kelvin offered geometric and physical plausibility, models, and the consistency of his cell with Plateau's laws — but the absence of any competitor for $106$ years hardened belief into near-consensus. The "attempt" here is best understood as a widely accepted conjecture that turned out to be **false as an optimality claim**.

## The Weaire–Phelan refutation (1993) — the decisive near-miss against optimality

Denis Weaire and Robert Phelan did not set out to prove Kelvin wrong; they were exploring foam structures inspired by the A15 / $\beta$-tungsten clathrate using Brakke's Surface Evolver. Their structure came in about $0.3\%$ below Kelvin's density, decisively refuting Kelvin's optimality conjecture. This is the central event in the problem's history. Importantly, WP is itself only a **conjectured** optimum: Weaire and Phelan made no claim to have proven global minimality, and none exists. The discovery converted a "solved" problem back into an open one with a new leading candidate.

## Searches for structures beating Weaire–Phelan (1994–present)

Following 1993, several groups — including Sullivan, Kusner, Kraynik, and the foam-physics community — systematically scanned tetrahedrally close-packed (TCP) and Frank–Kasper structures (C15, Z, $\sigma$-phase, and combinations) using Surface Evolver, seeking a foam below WP. **None has been found.** These are honest negative results: they strengthen confidence in WP as the optimum but prove nothing, since the search space (periodic and aperiodic partitions) is unbounded. Occasional claims of marginally competitive structures have not survived careful relaxation and volume-equalization.

## Partial rigorous results adjacent to the problem

- **Hales (1999, published 2001) — the honeycomb theorem.** Hales rigorously proved the $2$D analogue: the regular hexagonal tiling minimizes perimeter among equal-area planar partitions, vindicating a conjecture going back to antiquity. This is a genuine, complete proof — but of the planar problem, not Kelvin's. It is the closest thing to a model for how a $3$D proof might be structured, while also illustrating why the $3$D case is harder.
- **Taylor (1976) — Plateau's laws.** Jean Taylor proved that area-minimizing soap-film-like sets have exactly the singularity structure ($120°$ triple curves, tetrahedral-angle vertices) that Kelvin and WP exhibit. This certifies the candidates are geometrically admissible minimizers but does not select among them.
- **Local-minimality of WP / Kelvin.** Numerical evidence (Surface Evolver, and analyses by Kusner–Sullivan and others) strongly suggests both are stable local minima, but no computer-assisted proof (e.g., via interval arithmetic establishing the second variation is positive) has been completed and published as a theorem.

## Status of disputed or retracted claims

There is **no notable retracted "proof"** of Kelvin's optimality in the literature; the conjecture was disproved by counterexample rather than collapsing under a flawed proof. Likewise, no one has published a claimed proof that Weaire–Phelan is optimal, so there is no disputed optimality proof to adjudicate. The honest current position: WP is the best known partition, Kelvin's is second, and the global minimum is unknown — a rare case where the field is confident about the candidate but lacks even a local-minimality theorem, let alone a global one.
