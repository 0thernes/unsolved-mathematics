# Approaches — The Reconstruction Conjecture (Ulam)

_Major strategies, partial results, and barriers._

## Kelly's counting lemma and subgraph enumeration

The foundational engine is **Kelly's Lemma** (1957): for any graph $H$ with $|V(H)| < |V(G)|$, the number $s(H, G)$ of subgraphs of $G$ isomorphic to $H$ is reconstructible, because each such copy of $H$ misses at least one vertex and is therefore counted across the deck, with a clean multiplicity-correction. From this one extracts a cascade of **recognizable** parameters: the number of edges, the degree sequence, the number of copies of any small subgraph, and — via inclusion–exclusion — the number of *spanning* subgraphs of any fixed type up to the all-but-one level. Kelly's counting also yields **Tutte's reconstruction of the characteristic and chromatic polynomials** (Tutte, 1979), since these are generating functions over subgraph counts.

**Best result reached:** an enormous list of invariants is now known to be reconstructible — connectivity, the number of components, planarity, the degree sequence, the rank polynomial, the number of spanning trees, regularity, and more. **Barrier:** counting determines *how many* of each piece exist, not *how they fit together*. Two non-isomorphic graphs can share every subgraph-count below $n$ vertices; the lemma is blind to the global gluing, so it cannot by itself close the gap.

## Reduction to recognizable classes

A standard strategy proves the conjecture for graphs whose **defining property is recognizable from the deck**, so the problem decomposes class by class. If "being a tree," "being disconnected," "being regular," etc., is recognizable and the class is internally reconstructible, those graphs are settled.

**Best results:** reconstructibility is proven for **trees** (Kelly 1957), **disconnected graphs** (Kelly; Manvel), **regular graphs**, **unit-interval graphs**, **maximal planar graphs and outerplanar graphs**, **graphs with at most $n-2$ edges relative to certain bounds**, and **separable graphs without end-vertices**. **Barrier:** the hard residue is precisely the graphs that resist classification — sparse, irregular, $2$-connected graphs with no exploitable symmetry. Each new class chips at the periphery without touching the core.

## The dense / edge-counting attack (Lovász–Müller–Nash-Williams)

For **edge** reconstruction, an extremal counting argument is decisive. **Lovász (1972)** showed a graph is edge-reconstructible whenever $m > \binom{n}{2}/2$ (more than half the possible edges). **Müller (1977)** improved this to the sharp-feeling threshold $2^{m-1} > n!$, i.e. any graph with $m \ge \log_2 n! + 1$ edges is edge-reconstructible; equivalently all graphs with average degree above roughly $\log_2 n$ are settled. The proofs use a permutation-group / Möbius-function argument on the lattice of subgraphs.

**Best result:** essentially all *dense* graphs are edge-reconstructible. **Barrier:** the method's strength is exactly its weakness — it needs many edges. The vertex conjecture's open cases are **sparse**, where these bounds are vacuous.

## Probabilistic / "almost all graphs" approach (Bollobás)

**Bollobás (1990)** proved that **almost every graph is reconstructible**, and in a strong form: for the random graph $G(n, 1/2)$, with probability $\to 1$ as $n \to \infty$, $G$ is reconstructible from **only three** of its cards, and the **reconstruction number** is $3$ for almost all graphs. This shows the conjecture "generically" holds with massive redundancy.

**Best result:** the set of potential counterexamples has density $0$. **Barrier:** measure-zero is not emptiness. The conjecture is a statement about *every* graph, and the structured, low-entropy exceptions (vertex-transitive graphs, graphs with large automorphism groups, certain sparse families) are exactly where probabilistic genericity gives no information.

## Algebraic and group-theoretic methods

Several lines encode the deck algebraically: via the **lattice of subgraphs and its Möbius function** (underlying Lovász–Müller), via **association schemes and the characteristic polynomial** (Tutte), and via **automorphism-group constraints**. Nash-Williams' lemma on the symmetry of the "reconstruction matrix" formalizes when counting is invertible.

**Best result:** clean structural theorems (e.g. recognizability of the polynomial invariants; symmetry constraints on the deck). **Barrier:** the relevant linear systems are exactly singular in the hard cases; invertibility fails precisely where the global structure is underdetermined.

## Negative results, limits, and cautionary analogues

The conjecture is known to be **false for several close relatives**, which sharply constrains any proof strategy:

- **Digraphs:** **Stockmeyer (1977)** produced infinite families of non-reconstructible **tournaments and digraphs**, demolishing the directed analogue. Any proof of the undirected conjecture must use a property that directed graphs lack.
- **Hypergraphs:** **Kocay (1987)** and others exhibited non-reconstructible hypergraphs; **infinite graphs** also have explicit counterexamples (Fisher; Nash-Williams).
- **Set-reconstruction** (using the set rather than multiset of cards) fails in general for digraphs and is subtler for graphs.

**Implication:** these refute any argument that would apply equally to digraphs, hypergraphs, or infinite graphs. A successful proof must exploit something specific to **finite, undirected, simple** graphs — symmetry of adjacency, the finiteness of the deck, or the self-complementary counting structure — and this requirement is the central obstruction shaping all current work.
