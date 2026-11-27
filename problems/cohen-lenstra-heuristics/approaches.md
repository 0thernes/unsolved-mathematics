# Approaches — The Cohen–Lenstra Heuristics

_Major strategies, partial results, and barriers._

1. **Geometry of Numbers & Parametrization of Rings (Davenport–Heilbronn; Bhargava).** By class field theory, $\mathrm{Cl}(K)[3]$ corresponds to unramified cubic extensions of $K$, which Davenport–Heilbronn parametrized via binary cubic forms. Bhargava's higher composition laws extend this to degree 4 and 5 rings — but for $p \ge 5$ torsion of quadratic class groups, no analogous low-degree prehomogeneous vector space parametrization is known!
2. **Homological Stability of Hurwitz Spaces (Ellenberg–Venkatesh–Westerland 2016; Landesman–Levy).** Over function fields $\mathbb{F}_q(t)$, counting $\mathrm{Sur}(\mathrm{Cl}(K), G)$ translates to counting $\mathbb{F}_q$-points on Hurwitz moduli spaces of $G$-covers of $\mathbb{P}^1$. Proving homological stability of Hurwitz spaces plus Grothendieck–Lefschetz yields the large-$q$ function-field Cohen–Lenstra theorem.
3. **2-Part / Rédei Matrix & Markov Chain Methods (Fouvry–Klüners 2007; Smith 2025).** For $p = 2$, genus theory gives explicit control over $\mathrm{Cl}(K)[2]$ via quadratic reciprocity (Rédei matrices); Smith's breakthrough iterates higher $2^k$-Selmer / class-group pairings as a Markov process across quadratic twists.

## Core Barrier
Over number fields ($\mathbb{Q}$), for **every odd prime $p \ge 5$**, we do not even know the **first moment** (average size of $\mathrm{Cl}(K)[p]$) — nor even the *second* moment for $p = 3$! There is currently no number-field replacement for the topological Hurwitz-space / Grothendieck–Lefschetz machinery that succeeded over $\mathbb{F}_q(t)$.
