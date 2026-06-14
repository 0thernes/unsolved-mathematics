# History — Ryser's Conjecture (Hypergraph Covering)

_Origin, formulation, and timeline._

## Origin

Ryser's Conjecture is a sweeping generalization of one of the foundational duality theorems of combinatorics, **König's theorem** (1931), which states that in any bipartite graph the maximum size of a matching equals the minimum size of a vertex cover. Restated in hypergraph language, a bipartite graph is a $2$-partite $2$-uniform hypergraph, and König's theorem asserts that for such objects the covering number $\tau$ equals the matching number $\nu$.

The conjecture proposes the natural higher-dimensional analogue. Let $H$ be an **$r$-partite $r$-uniform hypergraph**: its vertex set is partitioned into $r$ classes, and every edge is a transversal containing exactly one vertex from each class. Write $\nu(H)$ for the maximum number of pairwise disjoint edges (the matching number) and $\tau(H)$ for the minimum number of vertices meeting every edge (the covering or transversal number). The conjecture states
$$\tau(H) \le (r-1)\,\nu(H).$$
For $r = 2$ this is exactly König's theorem (with equality $\tau = \nu$). The factor $r-1$ is best possible: truncated projective planes of order $r-1$ furnish $r$-partite $r$-uniform hypergraphs with $\nu = 1$ and $\tau = r-1$ whenever a projective plane of that order exists.

## Attribution

The statement is universally credited to **Herbert J. Ryser**, but it does not appear in a paper authored by him. It is recorded in the **1971 Ph.D. thesis of J. R. Henderson**, written at Caltech under Ryser's supervision, and the inequality is sometimes called the **Ryser–Henderson conjecture**. Henderson's thesis already contains the first nontrivial result, the case $r = 3$, and connects the problem to the theory of $(0,1)$-matrices and Latin squares that occupied Ryser throughout his career.

A widely studied companion is the **intersecting case** ($\nu = 1$), where the conjecture reduces to $\tau \le r-1$. This special case is itself open in general and is essentially equivalent to a conjecture of **Zsolt Tuza** and to questions about covering the edges of an $r$-partite intersecting hypergraph; the equality cases (when $\tau = r-1$) are conjectured to come precisely from projective planes, a refinement often attributed to **Lovász**, **Füredi**, and others.

## Timeline

- **1931** — König proves the bipartite min-max theorem ($r=2$ base case).
- **1971** — J. R. Henderson's Caltech thesis (under H. J. Ryser) states the conjecture and proves the case $r=3$.
- **1975** — Lovász studies fractional covers and the intersecting case, locating projective planes as extremal objects and proving $\tau \le r-1$ fractionally.
- **1980s** — Füredi develops the fractional and "covering by stars" machinery; bounds of the form $\tau \le (r-1)\nu$ are established under fractional relaxation, and $\tau/\nu$ is studied asymptotically.
- **2001** — Aharoni proves the conjecture for $r=3$ in full generality using a topological (Sperner-lemma / Aharoni–Haxell) argument, recovering Henderson's case with a powerful new method.
- **2009** — Haxell, Narins, and Szabó analyze the equality case for $r=3$, characterizing extremal $3$-partite hypergraphs.
- **2014** — Abu-Khazneh, Barát, Pokrovskiy, Szabó and related groups study intersecting $r$-partite hypergraphs, constructing new non-projective-plane extremal examples and disproving uniqueness in some equality refinements.
- **2017** — Haxell and Scott obtain partial results for $r=4$ and $r=5$, proving $\tau \le (r-1)\nu$ asymptotically / with constant improvement for small $r$.
- **2017–2021** — Bishnoi, Das, Morris, Pokrovskiy, Tuza and others refine the intersecting case, improving upper bounds on $\tau$ for intersecting $r$-partite hypergraphs below the trivial $r-1$ in infinitely many ranks where projective planes fail to exist.
- **Present** — The conjecture remains **open for every $r \ge 4$**. It is proven only for $r \le 3$; the intersecting case is the principal battleground, with the topological method of Aharoni–Berger–Ziv and the projective-plane extremal theory as the two dominant frameworks.
