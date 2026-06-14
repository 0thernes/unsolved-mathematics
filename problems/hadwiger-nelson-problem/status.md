# Status & Frontier — The Hadwiger–Nelson Problem

_Where the problem stands and what a resolution would require._

**Current state: `active-progress`, unresolved.** The chromatic number of the plane is known to satisfy
$$5 \le \chi(\mathbb{R}^2) \le 7,$$
and exactly which of $5$, $6$, $7$ is correct is open. The lower endpoint moved from $4$ to $5$ only in 2018; the upper endpoint of $7$ has stood since 1950 (Isbell).

### What is known (unconditional)

- **$\chi \ge 5$.** Established by **Aubrey de Grey (2018)**, "The chromatic number of the plane is at least 5," arXiv:1804.02385, via an explicit $1581$-vertex unit-distance graph with no proper $4$-coloring. The proof is finite and has been independently verified by SAT solvers. This is the strongest unconditional lower bound.
- **$\chi \le 7$.** Isbell's $7$-coloring of a hexagonal tiling (1950), unimproved.
- **Minimization.** Via Polymath16 and Marijn Heule, the smallest known $5$-chromatic unit-distance graphs have been reduced to roughly $500$ vertices (examples near $510$ and $509$ vertices reported), with machine-checkable certificates.

### What is known (conditional / restricted)

- **Measurable chromatic number $\ge 5$**, and stronger LP/spectral lower bounds, due to **Falconer (1981)** and later density/Lovász-theta arguments. These constrain colorings whose color classes are well-behaved (measurable), but a true optimal coloring could be non-measurable.
- **Possible axiom dependence.** Work of **Shelah–Soifer** shows that closely related distance-graph chromatic numbers can differ between ZFC and models where all sets are measurable, keeping alive Erdős's suspicion that the plane's $\chi$ might not be fully determined by ZFC alone — though this has not been demonstrated for the plane itself.

### What a full resolution would require

- **To prove $\chi \ge 6$:** exhibit a finite unit-distance graph that is not $5$-colorable (by De Bruijn–Erdős, one such graph suffices). None is known, and there is no proof one exists. This is the most natural next target and the focus of ongoing computational search.
- **To prove $\chi = 5$:** beyond the existing $\chi \ge 5$, one would need a *$5$-coloring of the entire plane* with no monochromatic unit pair — no such coloring is known, and constructing one (or proving none exists) is wide open.
- **To prove $\chi \le 6$:** find an explicit $6$-coloring (e.g. a clever tiling or aperiodic scheme); every attempt to beat Isbell's $7$ has failed.
- **To prove $\chi = 7$:** establish a $6$-coloring is impossible — a much harder, currently inaccessible structural result.

### Plausible routes

The most active route is **computer-assisted finite search** (SAT solvers, vertex-criticality reduction) to either find a $6$-chromatic graph or to keep shrinking $5$-chromatic ones for insight. A second route is **analytic/measure-theoretic and LP/SDP bounds** pushing the measurable chromatic number (and density results $m_1(\mathbb{R}^2)$) higher, which could at least force $\chi \ge 6$ under regularity. A third, more speculative route engages the **set-theoretic** question of whether $\chi$ is ZFC-determined. Closing the upper bound below $7$ would likely require a genuinely new coloring idea rather than incremental tiling tweaks. Most experts regard $\chi \in \{5,6,7\}$ as genuinely undecided, with no strong consensus on the answer.

## Related problems

- [Hadwiger Conjecture](../hadwiger-conjecture/README.md) — the graph-minor / chromatic-number conjecture bearing the same originator's name.
- [Inscribed Square Problem](../inscribed-square-problem/README.md) — another deceptively elementary open question in plane geometry.
- [Kakeya Conjecture](../kakeya-conjecture/README.md) — geometric–measure-theoretic problem about configurations in Euclidean space.
- [Lonely Runner Conjecture](../lonely-runner-conjecture/README.md) — a combinatorial-geometry problem with a similarly simple statement and stubborn difficulty.
