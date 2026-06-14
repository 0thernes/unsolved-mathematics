# Originator(s) — Seymour's Second Neighborhood Conjecture

_Biography, background, and the ideas that led here._

## Paul Seymour

**Paul D. Seymour** (born 26 July 1950, Plymouth, England) is one of the most influential structural graph theorists of the past half-century. He earned his BA (1971) and DPhil (1975) at the University of Oxford. After positions at Oxford, University College of Swansea, Rutgers, Ohio State, and **Bellcore (Bell Communications Research)** in the 1980s and early 1990s, he joined **Princeton University**, where he has been a professor of mathematics for decades.

Seymour's reputation rests on landmark work, much of it joint with **Neil Robertson**, including the **Graph Minors Project** — twenty-plus papers proving the **Robertson–Seymour theorem** (graphs are well-quasi-ordered under the minor relation) and the existence of $O(n^3)$ algorithms for disjoint paths. With Robertson, Sanders, and Thomas he gave a computer-checked proof of the **Four Color Theorem** (1996). With Chudnovsky, Robertson, and Thomas he proved the **Strong Perfect Graph Theorem** (2006). He has received the **Ostrowski Prize**, multiple **Fulkerson Prizes**, the **Pólya Prize**, and was elected a Fellow of the Royal Society.

## Why he posed it

The Second Neighborhood Conjecture sits somewhat apart from Seymour's headline structural theorems: it is a short, elementary-looking inequality about out-degrees in oriented graphs. Its appeal is precisely that contrast. Many statements in tournament theory take the form "some vertex *dominates a large set in two steps*," and a recurring heuristic is that "second neighborhoods should be at least as large as first neighborhoods" — intuitively, expansion in directed graphs should not shrink as one steps outward, unless the local structure forces it. Seymour distilled this intuition into a sharp, universally quantified claim.

The conjecture also generalizes a natural tournament question. In a tournament, every vertex $v$ has out-degree $d^+(v)$, and one asks whether some vertex "sees" at least as many vertices at distance two as at distance one. **Nathaniel Dean** had raised the tournament version around **1982**, and Seymour's contribution was to recognize that the right level of generality is *all* oriented graphs, not merely complete ones. This wider statement is strictly stronger and remains open, while the tournament root is now a theorem (Fisher 1996; Havet–Thomassé 2000).

## The modern formulation versus the historical root

- **Historical root (Dean, 1982):** the tournament case — every tournament has a vertex whose second out-neighborhood is at least as large as its first.
- **Modern formulation (Seymour, c. 1990):** the same inequality for *every* oriented graph (no digons), the open conjecture that bears Seymour's name.

The two are linked: a proof of the general case implies the tournament case, and the tournament case is the testing ground that produced the median-order technique central to all later partial progress.

## Legacy

Seymour's broader legacy — well-quasi-ordering, graph minors, perfect graphs, structural decomposition — has reshaped combinatorics. The Second Neighborhood Conjecture is a smaller but durable thread: it has spawned a dedicated literature, the notion of a **Seymour vertex**, the use of **median orders** as a proof engine for digraph problems, and a steady stream of partial results. That a statement this concise has resisted resolution for over three decades is itself part of its appeal, and it is frequently cited as a benchmark open problem in directed graph theory.
