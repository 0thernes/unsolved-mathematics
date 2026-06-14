# Status & Frontier — The Reconstruction Conjecture (Ulam)

_Where the problem stands and what a resolution would require._

**Official status: OPEN** (as of 2026). No counterexample exists and no community-accepted proof exists for finite simple graphs on $\ge 3$ vertices.

## What is known (unconditional)

A large body of *partial* and *recognizability* results is firmly established:

- **Reconstructible classes.** Trees (Kelly 1957), disconnected graphs, regular graphs, graphs with an end-vertex, unit-interval graphs, maximal planar and outerplanar graphs, and several other structured families are proven reconstructible.
- **Recognizable invariants.** Via **Kelly's Lemma**, the deck determines the number of edges, the degree sequence, the number of components, connectivity, planarity, the number of subgraphs isomorphic to any fixed smaller graph, and (Tutte) the characteristic, chromatic, and rank/Tutte polynomials.
- **Dense graphs (edge version).** **Müller (1977)**'s bound $2^{m-1} > n!$, building on **Lovász (1972)**, proves edge-reconstructibility for all graphs with more than about $\log_2 n!$ edges — i.e. essentially every dense graph.
- **Generic case.** **Bollobás (1990)** proved that **almost all graphs are reconstructible**, with reconstruction number $3$ — counterexamples, if any, form a density-zero, highly structured set.
- **Computation.** Exhaustive checks (Brendan McKay, via *nauty*) confirm reconstructibility for all graphs up to at least $n = 11$, with no exception ever found.
- **Sharp negative results on relatives.** The conjecture is **false** for **digraphs/tournaments** (Stockmeyer 1977), for **hypergraphs** (Kocay 1987), and for **infinite graphs**. These do not bear on the finite simple-graph case but rigidly constrain admissible proof methods.

## Strongest current results (conditional)

There are no widely used *conditional* theorems of the "assuming X, the conjecture holds" type comparable to RH-conditional results in number theory. The closest analogues are **implication results**: vertex-reconstructibility of graphs with minimum degree $\ge 1$ would imply edge-reconstructibility; and recognizability of additional structural parameters would shrink the open residue. The practical frontier is therefore unconditional but incremental — each newly settled class or recognizable invariant narrows the space where a counterexample could hide.

## What a full resolution would require

A proof must handle the **sparse, irregular, $2$-connected** graphs with small automorphism groups — exactly the cases where counting (Kelly's Lemma, Lovász–Müller) is too weak and probabilistic genericity (Bollobás) says nothing. Crucially, the argument must exploit a property **specific to finite undirected simple graphs**: any method that generalizes to digraphs is refuted on arrival by Stockmeyer's counterexamples. Plausibly viable routes:

1. **A new global invariant** recoverable from the deck that pins down the gluing, not just subgraph counts — something the directed case provably lacks.
2. **A structural reduction** of the conjecture to a finite or highly constrained family, then exhaustive/computer-assisted closure (extending the McKay verification with a theorem bounding the worst case).
3. **A self-complementary or symmetry argument** leveraging the finiteness and undirected symmetry of the deck's counting matrix to force invertibility in the singular sparse regime.

A disproof would require an explicit pair of non-isomorphic graphs with identical decks; the exhaustive verifications make any small counterexample impossible, so a disproof would have to be large and structured, against the grain of all current evidence.

## Related problems

- [Graceful Tree Conjecture](../graceful-tree-conjecture/README.md) — another deep, simply-stated open problem about trees in graph theory.
- [Cycle Double Cover Conjecture](../cycle-double-cover-conjecture/README.md) — a flagship structural conjecture on covering graphs with cycles.
- [Hadwiger Conjecture](../hadwiger-conjecture/README.md) — a central open question linking graph coloring and minors.
- [Caccetta–Häggkvist Conjecture](../caccetta-haggkvist-conjecture/README.md) — an open conjecture on directed graphs, where reconstruction is known to fail.
