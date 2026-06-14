# History — The Erdős–Hajnal Conjecture

_Origin, formulation, and timeline._

## Origin and motivation

The conjecture springs from Ramsey theory, the study of unavoidable order in large structures. The classical Ramsey theorem guarantees that every $n$-vertex graph contains a clique or an independent set ("homogeneous set") of size at least $\tfrac{1}{2}\log_2 n$, and Erdős's probabilistic lower bound of 1947 shows this logarithmic order is essentially optimal for general graphs. Paul Erdős and András Hajnal asked what happens when one forbids a fixed pattern: if a graph $G$ contains no *induced* copy of a fixed graph $H$, must its largest homogeneous set be far larger than logarithmic? Their answer, conjectured to be yes, is striking — a single local constraint forces a polynomial-size island of perfect order.

## Precise formulation

**Erdős–Hajnal Conjecture.** For every graph $H$ there exists a constant $c = c(H) > 0$ such that every $H$-free graph $G$ on $n$ vertices (no induced subgraph isomorphic to $H$) contains a clique or independent set of size at least $n^{c(H)}$.

"EH property" denotes graphs $H$ for which such a $c(H)$ exists. The best *unconditional* bound for general $H$ has long been $\exp\big(c\sqrt{\log n}\big)$ — superpolylogarithmic, but far below any $n^c$. An influential reformulation, due to Erdős and Hajnal and sharpened by Fox–Sudakov, replaces "clique or stable set" with "large complete or empty bipartite pair," giving the equivalent bi-clique and "polynomial Rödl property" versions used in most modern work.

## Timeline

**1947** — Erdős's probabilistic argument shows the general Ramsey bound $R(t,t) \ge 2^{t/2}$ is near-optimal, establishing the logarithmic baseline the conjecture seeks to beat.

**1977** — Rödl proves that $H$-free graphs contain linear-size induced subgraphs that are very dense or very sparse — a structural precursor (the "Rödl property").

**1989** — Erdős and Hajnal publish *Ramsey-type theorems* (Discrete Applied Mathematics), stating the conjecture and proving the $\exp(c\sqrt{\log n})$ lower bound valid for all $H$.

**2001** — Erdős, Hajnal, and Pach revisit bipartite and multicolor variants, strengthening the structural picture.

**2001** — Alon, Pach, and Solymosi prove the EH property is preserved under *substitution* (lexicographic blow-up of one vertex by a graph), giving the first systematic way to build new EH graphs from old.

**2014** — Chudnovsky's survey *The Erdős–Hajnal conjecture — a survey* crystallizes the state of the art; the case of every graph on $\le 4$ vertices is by then complete (notably $P_4$, all cographs).

**2014** — Fox and Sudakov develop density and dependent-random-choice techniques and the bi-clique reformulation.

**2015** — Chudnovsky and Safra confirm the case of the "bull" graph.

**2019** — Bonnet, Thomassé and collaborators connect EH-type structure to twin-width and algorithmic meta-theorems.

**2021–2022** — Nguyen, Scott, and Seymour launch a sustained program ("Induced subgraphs and tree-decompositions"; EH-related papers), and obtain the first asymptotic improvement on 1989: an $\exp\big(c\sqrt{\log n \log\log n}\big)$ general bound.

**2023** — Bucić, Nguyen, Scott, and Seymour prove EH holds for $H = C_5$ (the five-cycle), a long-standing test case, with a polynomial bound — widely regarded as a landmark.

**2023–2024** — Nguyen–Scott–Seymour establish EH for further infinite families via substitution/blow-up closures and for several sporadic graphs; the $C_5$ methods extend to additional cases.

**Present frontier** — The conjecture remains open for almost all $H$ on $\ge 5$ vertices outside the verified families; even the path $P_5$ and most prime graphs are unresolved, though $C_5$ and a growing list of cases are now settled.
