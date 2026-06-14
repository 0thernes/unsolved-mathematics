# History — The Erdős Unit Distance Problem

_Origin, formulation, and timeline._

## How the problem arose

In 1946 Paul Erdős published a short, now-canonical paper, *On sets of distances of $n$ points* (American Mathematical Monthly, 53, 248–250), in which he posed two intertwined extremal questions about a planar point set of size $n$. The first — the **distinct distances problem** — asks for the minimum number of *distinct* distances the set must determine. The second — the **unit distance problem** — asks for the **maximum** number of pairs at one fixed distance (say distance $1$). Write $u(n)$ for that maximum. Erdős's geometric instinct was that the densest possible configuration is essentially a piece of the integer lattice, where number-theoretic counting of representations as sums of two squares governs the answer.

## Precise formulation

Let $P$ be a set of $n$ points in $\mathbb{R}^2$ and let
$$u(n) = \max_{|P|=n}\#\{(p,q)\in P\times P : p<q,\ \|p-q\|=1\}.$$
Erdős asked for the growth rate of $u(n)$. From the $\sqrt{n}\times\sqrt{n}$ integer grid he derived the lower bound $u(n) \ge n^{1+c/\log\log n}$, using Landau's theorem on the number of representations of an integer by sums of two squares. He conjectured this lower bound is essentially the truth: $u(n) = n^{1+o(1)}$, in particular $u(n) \le n^{1+\varepsilon}$ for every $\varepsilon>0$. The lower bound was never matched; every known upper bound has the form $u(n) = O(n^{4/3})$ or close variants, and the factor-of-$n^{1/3}$ gap remains the central open problem.

## Reformulations

The problem is naturally cast in **incidence geometry**: unit distances among $P$ are incidences between the points $P$ and the family of $n$ unit circles centered at those points. Bounding point–circle incidences (Szemerédi–Trotter-type) yields the $O(n^{4/3})$ bound. It also connects to the **Hadwiger–Nelson problem** (chromatic number of the plane), the **distinct distances problem** (resolved up to logarithms by Guth–Katz in 2010/2015), and to higher-dimensional analogues where the truth is fully known in $\mathbb{R}^d$ for $d\ge 4$.

## Timeline

- **1946** — Erdős poses both the distinct-distances and unit-distance problems; obtains the grid lower bound $n^{1+c/\log\log n}$ and the easy upper bound $O(n^{3/2})$.
- **1972** — Józsa and Szemerédi improve the upper bound to $o(n^{3/2})$, the first sub-$3/2$ result.
- **1973** — Beck and others refine; the problem becomes a flagship of the emerging field of combinatorial geometry.
- **1984** — Spencer, Szemerédi, and Trotter prove $u(n) = O(n^{4/3})$, the bound that still stands today, via a crossing-number / incidence argument.
- **1983–1984** — Szemerédi and Trotter establish the general incidence theorem; Clarkson, Edelsbrunner, Guibas, Sharir, and Welzl (1990) give a simpler crossing-number proof (after Székely).
- **1997** — Székely's crossing-number method gives a transparent reproof of $O(n^{4/3})$, decoupling it from heavy machinery.
- **2008** — Constraints on near-extremal configurations studied; the conjecture's number-theoretic flavor sharpened.
- **2010/2015** — Guth and Katz resolve the *distinct* distances problem ($\Omega(n/\log n)$) using polynomial partitioning and algebraic geometry — but their method does **not** transfer to the unit-distance count.
- **2015–2020** — Polynomial-method and algebraic approaches probed for the unit-distance problem; partial results for structured point sets (e.g., points on few lines/circles), and improved bounds for unit distances in special norms.
- **2020s** — The $O(n^{4/3})$ upper bound remains unbeaten in general; activity focuses on algebraic structure of extremal sets and on the analogous problem in other metrics and over finite fields.

The defining tension persists: the lower bound $n^{1+o(1)}$ and the upper bound $n^{4/3}$ have not moved toward each other in the general planar case since 1984.
