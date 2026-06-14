# History — The Reconstruction Conjecture (Ulam)

_Origin, formulation, and timeline._

## How the problem arose

The Reconstruction Conjecture is a question about how much of a graph's global structure is encoded in its local "pieces." Given a finite simple graph $G$ on $n$ vertices, delete one vertex at a time to obtain the $n$ vertex-deleted subgraphs $G - v$. The **deck** of $G$ is the multiset $\{\, G - v : v \in V(G)\,\}$ of these $n$ cards, each taken only up to isomorphism (the labels are erased). The conjecture asserts that for $n \ge 3$ the deck determines $G$ up to isomorphism: no two non-isomorphic graphs on at least three vertices have the same deck.

The problem grew out of conversations between **Stanisław Ulam** and **Paul J. Kelly** at the University of Wisconsin around 1941. Ulam, whose mathematical taste favored questions about what minimal information pins down a structure, posed the metric/set-theoretic ancestor of the question; Kelly, his doctoral student, gave the precise graph-theoretic formulation and proved the first cases. The conjecture was first put in print, somewhat obliquely, in Ulam's 1960 *A Collection of Mathematical Problems*, and the graph-theoretic content was established in Kelly's 1942 thesis and his 1957 paper. Because both men shaped it, the statement is often called the **Kelly–Ulam conjecture**; Frank Harary's influential reframing in the 1960s coined the now-standard vocabulary ("deck," "card," "reconstructible") and an explicit edge-deletion analogue.

## Formulations and reformulations

- **Vertex reconstruction (the conjecture proper):** every graph on $n \ge 3$ vertices is reconstructible from its vertex-deck.
- **Edge Reconstruction Conjecture (Harary, 1964):** every graph with at least four edges is determined by its multiset of edge-deleted subgraphs $G - e$. Vertex-reconstructibility for graphs of minimum degree $\ge 1$ would imply edge-reconstructibility, but the two are studied as distinct problems.
- **Set-reconstruction (Harary):** can $G$ be recovered from the *set* (not multiset) of cards? This is formally stronger.
- **Reconstruction of invariants ("recognizability"):** rather than rebuild $G$, show that a parameter (degree sequence, number of edges, connectedness, characteristic polynomial) is determined by the deck. This pragmatic weakening drives most progress.
- **Kelly's Lemma (the counting identity):** the number of subgraphs of $G$ isomorphic to any fixed graph $H$ with fewer vertices than $G$ is computable from the deck. This is the workhorse behind nearly all positive results.

## Timeline

- **1941** — Stanisław Ulam and Paul Kelly discuss the question at the University of Wisconsin; Kelly begins systematic study.
- **1942** — Kelly's PhD thesis proves the conjecture for trees and several small cases.
- **1957** — Kelly publishes *A congruence theorem for trees*, giving the counting lemma and the tree result in the open literature.
- **1960** — Ulam publishes *A Collection of Mathematical Problems*, broadcasting the conjecture to a wide audience.
- **1964** — Frank Harary formalizes the modern terminology and states the **Edge Reconstruction Conjecture**.
- **1969** — Harary's survey crystallizes the problem and lists tractable subclasses (later reprinted in his *Graph Theory*).
- **1970** — Bohdan Zelinka and others extend reconstructibility to further classes; recognizability of degree sequence and edge count established.
- **1974** — Greenwell and Lovász, and independently others, sharpen edge-reconstruction tools; the "graphs vs. their complements" symmetry is exploited.
- **1977** — **László Lovász** proves edge-reconstructibility whenever $2^{m} > 2 \cdot e!$-type bounds hold, i.e. for graphs with many edges relative to $n$.
- **1977** — **Vera Sós / Müller**: Müller's counting argument shows a graph is edge-reconstructible if $2^{m-1} > n!$, settling all sufficiently dense graphs.
- **1980** — **Béla Bollobás** proves that *almost every* graph is reconstructible from just three well-chosen cards; reconstruction holds with probability $1$ as $n \to \infty$.
- **1981** — **Bollobás** establishes that almost all graphs are reconstructible, reframing the conjecture as a question about a sparse, structured residue.
- **1988** — **Nash-Williams** surveys the lattice/counting machinery; recognizability results accumulate (planarity, regularity, connectivity, characteristic polynomial via Tutte).
- **1990s** — **Bondy**'s survey *A graph reconstructor's manual* (1991) becomes the standard reference; positive classes now include regular graphs, disconnected graphs, trees, unit-interval graphs, maximal planar graphs, and outerplanar graphs.
- **2000s–2010s** — Computational verification pushes exhaustive checks; Brendan McKay verifies all graphs up to $n = 11$ (and beyond) are reconstructible.
- **2010s–present** — Work focuses on the recalcitrant sparse cases, digraph counterexamples (Stockmeyer), hypergraph and infinite-graph variants, and structural reductions; the finite simple-graph conjecture remains **open** as of 2026.
