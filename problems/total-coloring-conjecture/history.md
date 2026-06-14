# History — The Total Coloring Conjecture

_Origin, formulation, and timeline._

## Origin and formulation

A **total coloring** of a finite simple graph $G$ assigns colors to both its vertices and its edges so that (i) adjacent vertices receive distinct colors, (ii) adjacent edges receive distinct colors, and (iii) every edge differs in color from each of its two endpoints. Equivalently, it is a proper coloring of the **total graph** $T(G)$, whose vertices are the vertices and edges of $G$, with two of them adjacent iff they are adjacent or incident in $G$. The least number of colors needed is the **total chromatic number** $\chi''(G)$ (also written $\chi_T(G)$).

A trivial lower bound is $\chi''(G) \ge \Delta(G) + 1$, since a vertex of maximum degree $\Delta$ together with its $\Delta$ incident edges forms a clique of size $\Delta+1$ in $T(G)$. The **Total Coloring Conjecture (TCC)** asserts the matching upper bound is nearly tight:
$$\chi''(G) \le \Delta(G) + 2.$$
Graphs attaining $\Delta+1$ are called **Type 1** and those requiring $\Delta+2$ are **Type 2**; the conjecture says no graph needs more.

The conjecture is the total-coloring analogue of Vizing's edge-coloring theorem ($\chi'(G)\le\Delta+1$). It was formulated independently around 1964–1965 by **Mehdi Behzad**, in his 1965 Michigan State University doctoral thesis written under Edward Nordhaus and Gary Chartrand, and by **Vadim G. Vizing**, who recorded it in his influential 1964/1968 surveys of chromatic problems. For this reason it is sometimes called the **Behzad–Vizing conjecture**.

## Timeline

**1964** — Vizing, in his work on the chromatic theory of graphs, raises the question of bounding the total chromatic number and conjectures the $\Delta+2$ bound.

**1965** — Behzad introduces the total graph $T(G)$ and the total chromatic number in his Ph.D. dissertation, independently conjecturing $\chi''(G)\le\Delta+2$.

**1967** — Behzad, Chartrand, and Cooper publish results on the total chromatic numbers of complete graphs and complete bipartite graphs, confirming the conjecture in these families.

**1968** — Vizing's survey "Some unsolved problems in graph theory" (Russian Math. Surveys) circulates the conjecture widely to the international community.

**1971** — Rosenfeld and, independently, Vijayaditya verify the conjecture for $\Delta \le 3$ (the cubic/subcubic case), proving $\chi''(G)\le 5$ for graphs of maximum degree 3.

**1977** — Kostochka begins a sequence of works that ultimately settle $\Delta=4$ and $\Delta=5$; the $\Delta=4$ and $\Delta=5$ cases are established by Kostochka over 1977–1996.

**1989** — Hind initiates strong asymptotic bounds, showing $\chi''(G) \le \Delta + O(\sqrt{\Delta}\,\log\Delta)$-type results and bounds in terms of vertex coloring.

**1990** — Bollobás and Harris give early probabilistic upper bounds of the form $\chi''(G)\le (1+o(1))\Delta$ approaches, later sharpened.

**1992** — Yap, Wang, and others verify the conjecture for graphs of large maximum degree relative to order, and for several structural classes.

**1998** — **Molloy and Reed** prove, via the probabilistic method (Lovász Local Lemma and concentration), that $\chi''(G) \le \Delta + C$ for an absolute constant $C$; their argument gives $C=10^{26}$. This is the landmark unconditional result: total chromatic number exceeds the maximum degree by at most a constant.

**1996–2005** — The conjecture is verified for planar graphs with $\Delta \ge 9$ (Borodin and others), and Type-1/Type-2 questions for planar graphs become a major industry; planar graphs with $\Delta\ge 7$ are eventually handled, with $\Delta\le 5$ planar cases settled and $\Delta=6$ remaining partly open.

**2014–present** — Refinements of the Molloy–Reed constant, list-total-coloring variants (the **List Total Coloring Conjecture** of Borodin–Kostochka–Woodall), and verifications for sparse, planar, and bounded-treewidth families continue. The general conjecture remains open; the strongest general statement is still $\chi''(G)\le\Delta + C$ for an explicit but large constant.

The frontier today combines (a) shrinking the additive constant toward 2, (b) closing remaining small-$\Delta$ planar cases, and (c) attacking the list-coloring strengthening.
