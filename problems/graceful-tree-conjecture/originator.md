# Originator(s) — The Graceful Tree Conjecture (Ringel–Kotzig)

_Biography, background, and the ideas that led here._

The conjecture carries three names, reflecting a layered origin: **Gerhard Ringel** supplied the motivating decomposition problem, **Anton Kotzig** championed and sharpened the strong form, and **Alexander Rosa** gave the precise labeling-theoretic formulation.

## Gerhard Ringel (1919–2008)

Ringel was a German-born topological and combinatorial graph theorist, among the most influential of the twentieth century. Born in Kollnbrunn, Austria, he was a prisoner of war for five years before completing his doctorate at the University of Bonn in 1951. He held positions in Berlin and at the Free University, and from 1970 at the University of California, Santa Cruz, where he spent the rest of his career. Ringel's monumental achievement was the proof — with **J. W. T. Youngs** in 1968 — of the **Heawood map-coloring conjecture**, establishing the genus of every complete graph on a surface. His work on surface embeddings, Eulerian and Hamiltonian structure, and graph decompositions gave him a deep instinct for *building large structures out of repeated small ones*. The Ringel Conjecture on decomposing $K_{2n+1}$ into copies of a tree is exactly of this flavor: it asks for a perfect, balanced tiling of the complete graph's edge set by a single tree pattern. Graceful labeling entered as the algebraic device that, when present, mechanically produces the cyclic decomposition. Ringel's legacy includes the books *Map Color Theorem* (1974) and *Pearls in Graph Theory* (with Nora Hartsfield), and the field of topological graph theory he helped found.

## Anton Kotzig (1919–1991)

Kotzig was a Slovak–Canadian mathematician whose breadth spanned graph theory, combinatorics, and probability. Born in Kočovce (then Czechoslovakia), he worked in Bratislava — where he supervised and collaborated with a generation of Slovak combinatorialists, Rosa among them — before emigrating to Canada in 1969, settling at the Université de Montréal (CRM). Kotzig is remembered for the theory of *graph decompositions*, for "Kotzig's theorem" on the structure of 3-connected planar graphs (every such graph has an edge whose endpoint degrees sum to at most 13), and for sustained work on magic and graceful labelings. He was the conjecture's most vocal advocate: he repeatedly emphasized the strong claim that *all* trees are graceful and framed it as one of the central open problems of labeling theory, reportedly calling the difficulty of the general case "a disease." His enthusiasm and lecturing turned a technical decomposition tool into a named conjecture pursued for its own sake.

## Alexander Rosa (b. 1937)

Rosa, a Slovak–Canadian combinatorialist and student of Kotzig's circle, is the figure who made the conjecture precise. In his 1967 paper *On certain valuations of the vertices of a graph*, he defined the $\alpha$, $\beta$, $\sigma$, $\rho$ valuations and proved the foundational equivalence between $\beta$-valuations (graceful labelings) of a tree $T$ with $m$ edges and cyclic decompositions of $K_{2m+1}$ into copies of $T$. The still-stronger $\alpha$-labeling he introduced in the same work remains the most useful refinement, because $\alpha$-labeled graphs decompose complete *bipartite* graphs and lift to a wide range of further decompositions. Rosa spent his career at McMaster University and became a leading authority on combinatorial design theory, Steiner systems, and graph labelings. His valuations paper is among the most cited starting points in the entire labeling literature.

### Two formulations, one problem

The *historical root* is Ringel's tree-decomposition conjecture; the *modern formulation* is Rosa's purely arithmetic statement that every tree admits distinct vertex labels in $[0,n-1]$ inducing the full edge-difference set $\{1,\dots,n-1\}$. The two are tightly linked — every graceful tree yields a cyclic decomposition — but they are not identical: the 2020 resolution of the Ringel Conjecture for large $n$ did not settle the GTC, because near-decompositions can be achieved without each individual tree being graceful.
