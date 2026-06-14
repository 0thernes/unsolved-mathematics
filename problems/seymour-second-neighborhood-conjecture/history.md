# History — Seymour's Second Neighborhood Conjecture

_Origin, formulation, and timeline._

## Origin

The conjecture was posed by **Paul Seymour** (Princeton University) around **1990** and first appeared in print in the **1995** PhD thesis of his student **Nathaniel Dean** and in the survey-style literature that followed. It concerns *oriented graphs*: directed graphs with no loops, no digons (no pair of opposite arcs $u\to v$ and $v\to u$), and at most one arc between any two vertices. Equivalently, an oriented graph is an orientation of a simple undirected graph.

For a vertex $v$ in a digraph $D$, write $N^+(v)$ for its **first out-neighborhood** (vertices reachable by a single arc out of $v$) and $N^{++}(v)$ for its **second out-neighborhood** (vertices at directed distance exactly $2$ from $v$, i.e. reachable in two arcs but not one). Seymour's conjecture asserts:

> Every oriented graph contains a vertex $v$ with $|N^{++}(v)| \ge |N^{+}(v)|$.

Such a vertex is now standardly called a **Seymour vertex**. The conjecture is the natural digraph generalization of an earlier statement about **tournaments**.

## Reformulations and the tournament root

The special case where $D$ is a **tournament** (an orientation of a complete graph) is the **second neighborhood conjecture for tournaments**, which is itself equivalent to a 1982 conjecture of **Dean**. In that form it is closely tied to questions about vertices of large out-degree dominating others "in two steps." A widely cited equivalent for the general conjecture: every oriented graph has a vertex $v$ such that the number of vertices at distance $\le 2$ from $v$ is at least $2\,|N^+(v)|$ (since $\{v\}\cup N^+\cup N^{++}$ are disjoint). The conjecture is also stated in a weighted/fractional form, and there is a celebrated reformulation through **median orders** of tournaments.

## Timeline

- **1982** — **Nathaniel Dean** poses the tournament version (a "second-out-neighborhood" question) in the context of his graduate work.
- **1990** — **Paul Seymour** formulates the general conjecture for all oriented graphs.
- **1995** — The conjecture circulates in print; **Dean and Latka** study the related class of "rose tournaments" and the tournament case.
- **1996** — **David C. Fisher** proves Dean's conjecture (the tournament case) using a probabilistic/weighting argument, the **"Squaring the Tournament"** paper — the first major positive result.
- **2000** — **Frank Havet and Stéphan Thomassé** give a clean combinatorial proof of the tournament case via **median orders**, and extend it to tournaments missing a perfect matching; they show the **feed vertex** (last vertex of a median order) is a Seymour vertex.
- **2003** — **Yahya Ould Hamidoune** and collaborators study vertex-transitive and Cayley-digraph cases.
- **2006** — **Guantao Chen, Jian Shen, and Raphael Yuster** prove that every oriented graph has a vertex $v$ with $|N^{++}(v)| \ge \gamma\,|N^{+}(v)|$ for $\gamma \approx 0.657$, the real root of $2x^3 + x^2 - 1 = 0$ — the best known general multiplicative bound.
- **2007** — **Fidler and Yuster** verify the conjecture for tournaments minus a star, and other near-complete classes.
- **2011–2017** — Verification for further structured families: graphs of small size, digraphs with specified degree conditions, and classes defined by forbidden substructures.
- **2019** — **Daamouch** and others confirm the conjecture for digraphs whose underlying graph is a comparability graph and related classes.
- **2020s** — Work continues on weighted versions, distance-domination analogues, and computational verification, but **the general conjecture remains open**.

The problem is regarded as a clean, deceptively simple statement that resists all known global techniques; only the tournament case and structured subfamilies are settled.
