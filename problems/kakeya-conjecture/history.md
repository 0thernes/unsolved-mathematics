# History — The Kakeya Conjecture

_Origin, formulation, and timeline._

The problem began as a question in elementary geometry. In 1917 the Japanese mathematician Sōichi Kakeya asked for the **smallest area of a planar region in which a unit needle can be continuously rotated through a full $180^\circ$** (a "Kakeya needle problem"). It was widely believed the optimal shape would be a convex region — the deltoid (three-cusped hypocycloid) of area $\pi/8$ was conjectured optimal. The surprise came in 1928, when **Abram Besicovitch** showed, building on a construction he had developed around 1919–1920 in Perm (originally to answer a Riemann-integration question), that there exist sets of **arbitrarily small measure** containing a unit segment in every direction. With an added "Pál joins" sprouting argument, this implies the needle can be turned in a region of arbitrarily small area. The needle problem thus had no positive answer.

Attention then shifted from *area* to *dimension*. A **Besicovitch set** (or **Kakeya set**) in $\mathbb{R}^n$ is a set containing a unit line segment in every direction. Besicovitch sets of Lebesgue measure zero exist in every $\mathbb{R}^n$, $n\ge 2$. The modern **Kakeya conjecture** asserts the residual structure cannot be too thin:

> Every Besicovitch set in $\mathbb{R}^n$ has **Hausdorff dimension $n$** (and the stronger **Minkowski/box-counting** version: Minkowski dimension $n$).

In the plane this is a theorem: **Roy Davies** proved in 1971 that every planar Kakeya set has Hausdorff dimension $2$, fixing the precise dimensional formulation that defines the open problem for $n\ge 3$. The conjecture acquired outsized importance once **Charles Fefferman** (1971) disproved the disc multiplier conjecture using a Besicovitch construction, and once **Bourgain** and **Wolff** in the 1990s tied Kakeya to the **Fourier restriction**, **Bochner–Riesz**, and **local smoothing** problems in harmonic analysis. Kakeya sits at the base of a tower of conjectures whose top is restriction theory.

**Timeline**

- **1917** — Sōichi Kakeya poses the needle-rotation problem; the deltoid is conjectured optimal.
- **1919–1920** — Besicovitch constructs measure-zero sets containing segments in all directions, for an unrelated Riemann-integration question (work disrupted by the Russian Revolution).
- **1928** — Besicovitch publishes the resolution of the needle problem: rotation is possible in arbitrarily small area. With Pál's joins, area can be made arbitrarily small.
- **1971** — Roy Davies proves every Kakeya set in $\mathbb{R}^2$ has Hausdorff dimension $2$, fixing the $n=2$ case and the dimensional formulation.
- **1971** — Fefferman disproves the ball multiplier conjecture via a Besicovitch set, embedding Kakeya in harmonic analysis.
- **1991** — Bourgain introduces the "bush" argument, proving $\dim \ge \tfrac{n+1}{2}$ and linking Kakeya to restriction.
- **1995** — Thomas Wolff proves the **hairbrush** bound $\dim \ge \tfrac{n+2}{2}$, the benchmark for over a decade.
- **1999** — Bourgain's arithmetic/combinatorial method (sum-difference sets) pushes past $\tfrac{n+2}{2}$ in high dimensions; birth of the additive-combinatorics approach.
- **1999** — Wolff formalizes the **finite-field Kakeya** model problem as a testing ground.
- **2002** — Katz–Łaba–Tao improve the $n=3$ Minkowski bound to $\tfrac{5}{2}+\varepsilon$; Bennett–Carbery–Tao prove the multilinear Kakeya estimate (2006).
- **2009** — Zeev Dvir proves the **finite-field Kakeya conjecture** via the polynomial method, a landmark that nonetheless does not transfer to $\mathbb{R}^n$.
- **2015** — Guth–Katz polynomial-method techniques; Katz–Zahl prove $\dim \ge 5/2+\varepsilon_0$ in $\mathbb{R}^3$ (improved subsequently).
- **2017–2021** — Katz–Zahl, Zahl push the $\mathbb{R}^3$ Hausdorff bound toward $\sim 2.5$–$2.7$; refined sticky/grains analysis.
- **2025** — **Hong Wang and Joshua Zahl** announce a proof that every Kakeya set in $\mathbb{R}^3$ has Hausdorff (and Minkowski) dimension $3$, resolving the conjecture in three dimensions. The case $n\ge 4$ remains open.
