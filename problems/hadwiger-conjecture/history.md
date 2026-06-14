# History — Hadwiger's Conjecture (Graph Coloring)

_Origin, formulation, and timeline._

## How the problem arose

Hadwiger's Conjecture sits at the confluence of two of the deepest currents in twentieth-century combinatorics: the map-coloring tradition that began with the Four Color Problem (Guthrie, 1852) and the emerging structural theory of graph minors. By the early 1940s the Four Color Conjecture — every planar map is properly 4-colorable — had resisted proof for nearly a century, but it had been recast in graph-theoretic language. A pivotal reformulation due to Klaus Wagner (1937) showed that the Four Color Conjecture is equivalent to the statement that every graph with no $K_5$ minor is 4-colorable. Wagner's theorem characterized $K_5$-minor-free graphs by a clique-sum decomposition over planar pieces and the Wagner graph $V_8$, exposing minors as the natural setting for coloring obstructions.

In 1943 Hugo Hadwiger, writing in the *Vierteljahrsschrift der Naturforschenden Gesellschaft in Zürich*, proposed the bold generalization that bears his name.

## Precise formulation

A graph $H$ is a **minor** of $G$ if $H$ can be obtained from a subgraph of $G$ by contracting edges. Write $\chi(G)$ for the chromatic number. **Hadwiger's Conjecture** asserts:

$$\chi(G) \ge t \implies G \text{ contains } K_t \text{ as a minor.}$$

Equivalently, every graph with no $K_t$ minor is $(t-1)$-colorable; equivalently, every graph $G$ has a $K_{\chi(G)}$ minor. Writing $h(G)$ for the **Hadwiger number** (the order of the largest clique minor), the conjecture is $h(G) \ge \chi(G)$. The cases $t=1,2,3$ are elementary. The case $t=4$ was proved by Hadwiger (1943) and independently by Dirac (1952). The case $t=5$ is **equivalent** to the Four Color Theorem via Wagner's 1937 reduction; the case $t=6$ was reduced to the Four Color Theorem by Robertson, Seymour, and Thomas (1993). For $t \ge 7$ the conjecture remains open.

## Timeline

- **1852** — Francis Guthrie poses the Four Color Problem, the historical seed of minor-based coloring.
- **1937** — Klaus Wagner proves his structure theorem for $K_5$-minor-free graphs, equating the $K_5$ case with the Four Color Conjecture.
- **1943** — Hugo Hadwiger states the conjecture for all $t$ and proves the case $t=4$.
- **1952** — Gabriel Dirac independently proves the $t=4$ case and reframes the problem in modern graph-theoretic terms; the conjecture begins circulating widely under Hadwiger's name.
- **1976** — Kenneth Appel and Wolfgang Haken prove the Four Color Theorem, thereby establishing the $t=5$ case of Hadwiger's Conjecture.
- **1980** — Alexander Kostochka proves that $K_t$-minor-free graphs have average degree $O(t\sqrt{\log t})$, yielding $\chi(G) = O(h(G)\sqrt{\log h(G)})$.
- **1984** — Andrew Thomason independently re-derives the $O(t\sqrt{\log t})$ extremal bound on density forcing a $K_t$ minor.
- **1993** — Neil Robertson, Paul Seymour, and Robin Thomas prove the $t=6$ case, showing any minimal counterexample is apex (planar plus one vertex) and reducing it to the Four Color Theorem.
- **2001** — Thomason determines the exact extremal constant in the Kostochka–Thomason bound, $c = 0.6382\ldots$, settling the precise density needed to force $K_t$.
- **2005** — Reed and Seymour prove the fractional relaxation of Hadwiger's Conjecture; the conjecture is also verified for almost all (random) graphs.
- **2019** — Sergey Norin, Luke Postle, and Zi-Xia Song break the $\sqrt{\log t}$ barrier, proving $\chi(G) = O(h(G)(\log h(G))^{1/4 + o(1)})$ for $K_t$-minor-free graphs.
- **2020** — Postle, and Norin–Postle, drive the exponent of $\log h(G)$ below $1/4$ toward $o(1)$.
- **2021–2023** — Michelle Delcourt and Luke Postle obtain $\chi(G) = O(h(G)\log\log h(G))$, the current best general upper bound, leaving only a $\log\log$ gap to linearity.
- **2024–present** — Work continues on whether $\chi(G) = O(h(G))$ holds, on linear bounds under structural restrictions, and on the still-open exact cases $t \ge 7$.

The arc runs from an audacious 1943 generalization, through the resolution of small cases tied to the Four Color Theorem, to a still-active extremal-combinatorics frontier whose central question is whether $\chi(G) = O(h(G))$ — let alone the exact bound $\chi(G) \le h(G)$.
