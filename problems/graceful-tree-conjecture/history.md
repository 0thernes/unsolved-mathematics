# History — The Graceful Tree Conjecture (Ringel–Kotzig)

_Origin, formulation, and timeline._

The Graceful Tree Conjecture grew out of a problem in combinatorial design theory rather than from any abstract interest in labeling per se. In 1963, **Gerhard Ringel** posed what is now called the **Ringel Conjecture**: the complete graph $K_{2n+1}$ can be decomposed into $2n+1$ edge-disjoint copies of any fixed tree $T$ on $n+1$ vertices. Decomposing $K_{2n+1}$ into copies of a path or star was classical; Ringel's question generalized this to arbitrary trees. The search for a *systematic* way to produce such decompositions led directly to the labeling that now bears the name "graceful."

The decisive step was taken by **Alexander Rosa** in his 1967 paper *On certain valuations of the vertices of a graph* (in the proceedings of the Rome symposium *Théorie des graphes*). Rosa introduced a hierarchy of vertex valuations — which he named $\alpha$, $\beta$, $\sigma$, and $\rho$ — for a graph with $m$ edges. A **$\beta$-valuation** assigns to the vertices distinct integers in $\{0,1,\dots,m\}$ so that the $m$ induced edge labels $|f(u)-f(v)|$ are exactly $\{1,2,\dots,m\}$. Rosa proved that if a tree $T$ with $n$ edges has a $\beta$-valuation, then $K_{2n+1}$ has a cyclic decomposition into $2n+1$ copies of $T$ — connecting his labeling to Ringel's conjecture. **Solomon W. Golomb**, around 1972, renamed the $\beta$-valuation "**graceful labeling**," and that terminology stuck after appearing in popular accounts including Martin Gardner's *Scientific American* column.

The precise modern statement: a tree on $n$ vertices (hence $n-1$ edges) is **graceful** if its vertices can be labeled with distinct integers from $\{0,1,\dots,n-1\}$ such that the edge labels — absolute differences of endpoint labels — are exactly $\{1,2,\dots,n-1\}$. The **Graceful Tree Conjecture (GTC)**, attributed to Ringel, Kotzig, and Rosa and often called the **Ringel–Kotzig conjecture**, asserts that *every* tree is graceful. **Anton Kotzig** was an energetic promoter of the problem and conjectured the strong form; the conjecture's joint attribution reflects Ringel's decomposition motivation, Kotzig's advocacy, and Rosa's formalization.

A finer invariant emerged immediately: Rosa's **$\alpha$-labeling** is a graceful labeling for which there exists a threshold $\lambda$ separating the labels of the two color classes of the (bipartite) tree. Trees with $\alpha$-labelings are far more powerful for decomposition arguments, and much of the field bifurcated into "graceful" versus the stronger "$\alpha$" question.

### Timeline

- **1963** — Gerhard Ringel poses the Ringel Conjecture on tree-decompositions of complete graphs, the motivating problem.
- **1964** — The strong "every tree is graceful" form is articulated in the Ringel–Kotzig circle; commonly cited as the conjecture's origin year.
- **1966–67** — Alexander Rosa introduces $\alpha,\beta,\sigma,\rho$ valuations and proves the link between $\beta$-valuations and cyclic $K_{2n+1}$ decompositions.
- **c. 1972** — Solomon Golomb coins the term "graceful labeling"; Martin Gardner popularizes it.
- **1979** — Kotzig surveys decompositions and labelings, consolidating "graceful" as a research program.
- **1980s** — Bermond and others verify gracefulness for caterpillars, certain lobsters, symmetrical trees; the difficulty of general trees becomes apparent.
- **1998 (and continuing)** — Joseph Gallian launches *A Dynamic Survey of Graph Labeling* in the *Electronic Journal of Combinatorics*, updated yearly, the field's reference catalog.
- **1999** — Aldred and McKay computationally verify that all trees up to 27 vertices are graceful (later extended).
- **2002** — Brankovic, Murch, Pond, Rosa et al. extend computational verification (trees to ~29–35 vertices in subsequent work).
- **2004** — Van Bussel and others give bounded-diameter and near-graceful results; "range-relaxed" graceful labelings introduced.
- **2009–2010** — Superior and Hrnčiar–Haviar establish gracefulness for trees of diameter at most 5; bounded-degree subclasses advance.
- **2020** — Montgomery, Pokrovskiy, and Sudakov prove the **Ringel Conjecture** for all large $n$, and (with Keevash–Staden–Su independent work on related decompositions) resolve a long-standing motivating problem — though *not* the GTC itself.
- **2021–2025** — Bipartite/$\alpha$-labeling techniques, probabilistic absorption, and large-tree asymptotics continue; the GTC remains open for general trees.
