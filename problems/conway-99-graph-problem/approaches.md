# Approaches — Conway's 99-Graph Problem

_Major strategies, partial results, and barriers._

1. **Automorphism-Group Elimination (Makhnev–Minakova; Behbahani–Lam; Brouwer–Van Maldeghem).** By analyzing fixed-point subgraphs of prime-order automorphisms, researchers eliminated every prime $p \ge 5$ from $|\mathrm{Aut}(G)|$ and ruled out almost every possible group of order $2^a 3^b$ (including all vertex-transitive and edge-transitive candidates). If a 99-graph exists, its symmetry group must be tiny (possibly trivial!).
2. **Local Subconstituent & Star-Complement Decomposition.** Every vertex $x$ has neighborhood $G(x) \cong 7 K_2$ (seven disjoint edges, 14 vertices) and non-neighborhood $G_2(x)$ of $84$ vertices, where each non-neighbor is adjacent to exactly two non-adjacent vertices in $G(x)$. Because $\binom{7}{2} \times 4 = 84$, there is a **1-to-1 bijection** between the 84 vertices of $G_2(x)$ and pairs of vertices from two distinct triangles at $x$! Trying to extend this rigid local structure consistently across all 99 vertices drives SAT / integer-programming / backtracking searches.
3. **Semidefinite Programming (SDP) & Terwilliger Algebra.** Higher-order Delsarte / Lovász / Terwilliger-algebra SDP hierarchies test whether 3-vertex and 4-vertex subconfiguration counts are globally feasible; so far the parameters $(99, 14, 1, 2)$ have survived standard spectral and Krein bounds.

## Core Barrier
The problem lies in the worst computational and theoretical blind spot: **99 vertices is far too large for brute-force SAT/graph enumeration** when $|\mathrm{Aut}(G)|$ can be trivial, yet **too small and algebraically "clean"** for asymptotic or standard spectral inequalities to yield a contradiction!
