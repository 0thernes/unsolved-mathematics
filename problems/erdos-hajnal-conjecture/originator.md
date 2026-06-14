# Originator(s) — The Erdős–Hajnal Conjecture

_Biography, background, and the ideas that led here._

The conjecture is the joint creation of two of the twentieth century's most influential combinatorialists, **Paul Erdős** and **András Hajnal**, whose decades-long collaboration produced more than fifty joint papers and helped found modern combinatorial set theory and Ramsey theory.

## Paul Erdős (1913–1996)

Erdős was born in Budapest to two mathematics teachers; a child prodigy, he earned his doctorate at the University of Budapest at twenty-one. Driven out of Europe by the rise of fascism, he became the archetypal itinerant mathematician — owning almost nothing, travelling continuously between collaborators, and famously declaring property "a nuisance." He published roughly 1,500 papers with some 500 coauthors, giving rise to the "Erdős number." His method was problem-centric: he distilled deep phenomena into crisp, often elementary-sounding questions, frequently attaching cash prizes. Erdős essentially founded the probabilistic method in combinatorics (his 1947 lower bound for Ramsey numbers is its prototype) and, with Hajnal, much of partition calculus and the theory of chromatic number for infinite graphs. The Erdős–Hajnal conjecture bears his signature instinct: take a celebrated theorem (Ramsey's), impose a single natural restriction (forbidding an induced subgraph), and ask whether the qualitative behavior jumps — here, from logarithmic to polynomial.

## András Hajnal (1931–2016)

Hajnal, also Hungarian, took his doctorate under László Kalmár and Géza Fodor at Szeged and spent much of his career at the Hungarian Academy of Sciences and Eötvös Loránd University, later at Rutgers, where he directed DIMACS. He was a master of set theory and infinite combinatorics: the Hajnal–Szemerédi theorem on equitable colorings, fundamental results in the partition calculus, and the theory of set mappings are among his contributions. With Erdős he developed the framework — relations like $n \to (k)^2_2$ and their generalizations — within which Ramsey-type questions about graphs are naturally posed. Hajnal's structural sensibility complemented Erdős's extremal one; the conjecture's emphasis on *induced* subgraphs (a more rigid, structural constraint than ordinary subgraph containment) reflects this.

## The idea behind the problem

By the 1980s both men understood that the probabilistic Ramsey bound is sharp only because random graphs are "generic" — they contain every small graph as an induced subgraph. The natural conjecture was that forbidding even one such pattern destroys this genericity enough to force unusually large order. They could prove a quantitative improvement, $\exp(c\sqrt{\log n})$, over the universal $\log n$, but not the polynomial leap. The gap between $\exp(c\sqrt{\log n})$ and $n^c$ has resisted attack for over thirty years and defines the problem.

## Legacy

The conjecture has become a central organizing question of structural graph theory and modern Ramsey theory, spawning the "EH property," the polynomial Rödl property, and connections to perfect graphs, VC-dimension, and twin-width. Erdős's prizes and Hajnal's structural program both live on in the active research community, and the partial resolutions (cographs, the bull, $C_5$) are celebrated precisely because they chip at a problem the two originators left as a clean, durable challenge. The modern statement is essentially identical to the 1989 original; only the equivalent reformulations (bi-clique, polynomial Rödl) have been added.
