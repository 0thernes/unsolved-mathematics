# Originator(s) — The 1/3–2/3 Conjecture

_Biography, background, and the ideas that led here._

The conjecture carries three names — **Sergei Kislitsyn**, **Michael Fredman**, and **Nati Linial** — because it was raised independently from two directions, an Eastern combinatorial root and a Western algorithmic one, before being unified into the statement bearing the fraction $1/3$.

## Sergei S. Kislitsyn — the historical root (1968)

Kislitsyn was a Soviet mathematician working in combinatorics and order theory. In a 1968 Russian-language paper he studied what would now be called the distribution of an element's rank across the linear extensions of a finite poset, and posed the existence of a pair of elements whose relative order is "undecided" by the partial order — i.e. realized in a balanced fraction of completions. His framing predates the algorithmic motivation entirely and is the earliest known statement of the problem. Because the work appeared in a venue with limited Western circulation, it was rediscovered only after the conjecture had already become famous under Linial's name; the field now credits Kislitsyn as the originator, and several surveys (Brightwell; Trotter) take care to restore the attribution. Little biographical detail circulates in the English-language literature, which is itself part of the story: the conjecture's history is a case study in how a problem can be posed, lost, and re-posed across a language barrier.

## Michael Fredman — the algorithmic angle (1976)

Michael L. Fredman (b. 1946) is an American computer scientist, a foundational figure in data structures and the analysis of algorithms (later famous for Fredman–Tarjan Fibonacci heaps and the Fredman–Komlós–Szemerédi hashing scheme). In the mid-1970s, working on sorting and merging with partial information, he confronted the question: if you have already learned a partial order $P$, can a single well-chosen comparison always cut the number of consistent total orders by a guaranteed constant factor? That is exactly the balanced-pair question, now read as an information-theoretic lower bound for sorting. Fredman's motivation supplied the "why it matters" that made the conjecture central to theoretical computer science: a positive answer would say the information-theoretic bound $\log_2 e(P)$ is essentially achievable.

## Nathan (Nati) Linial — the modern formulation (1984)

Nati Linial (b. 1953) is an Israeli mathematician and computer scientist at the Hebrew University of Jerusalem, known for deep contributions to combinatorics, the geometry of metric spaces, distributed computing, and high-dimensional combinatorics. In his 1984 paper *The information-theoretic bound is good for merging*, Linial crystallized the problem into the now-canonical form — "every finite non-chain poset has an incomparable pair with $\Pr[x\prec y]\in[\frac13,\frac23]$" — and proved it for **width-2 posets** with the sharp constant $\tfrac12-\tfrac{\sqrt5}{10}$, the value forced by Fibonacci/golden-ratio counting of extensions of a 2-chain interleaving. Linial's paper is what gave the conjecture its name, its precise constant $1/3$, and its place on every list of open problems in order theory. His broader research program — using probabilistic, entropic, and geometric methods on discrete structures — is also the toolkit from which the major partial results were later built.

## Why $1/3$, and what the originators saw

All three were circling the same phenomenon: a partial order that is "far from total" must hide a comparison whose outcome is genuinely uncertain. The genius of the $1/3$ formulation is its exactness — the bound is tight on the smallest non-trivial poset, so the conjecture is not "some constant exists" (that part Kahn–Saks settled) but "the constant is exactly the obvious extremal one." The historical and modern formulations agree on content; they differ only in motivation (Kislitsyn's pure order theory, Fredman's sorting lower bounds, Linial's information theory).

## Legacy

The conjecture became a flagship problem connecting order theory, the geometry of polytopes, entropy, and the complexity of sorting. It motivated the Kahn–Saks application of Brunn–Minkowski inequalities to combinatorics and the Kahn–Kim entropy method, both of which outgrew the original problem. Fredman and Linial each went on to shape large areas of TCS and combinatorics; the conjecture remains one of the most cited open problems carrying their names, and a standard test case for new techniques in the probabilistic combinatorics of posets.
