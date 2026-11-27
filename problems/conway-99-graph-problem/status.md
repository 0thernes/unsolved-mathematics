# Status & Frontier — Conway's 99-Graph Problem

_Where the problem stands and what a resolution would require._

**Overall status: `open` (\$1,000 Conway Prize unclaimed).**

## What is known

- **Existence:** Completely **OPEN** — neither a 99-vertex graph $\mathrm{srg}(99, 14, 1, 2)$ nor a proof of non-existence is known.
- **Automorphisms:** No prime $p \ge 5$ divides $|\mathrm{Aut}(G)|$; any surviving 99-graph must be non-vertex-transitive with very small $2,3$-automorphism group (possibly trivial).
- **Local structure:** Every vertex neighborhood is $7 K_2$, and the 84 non-neighbors biject cleanly onto cross-edge pairs of the 7 triangles.
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `Conway99Graph.conway99Graph` (`kind: open`).

## What a resolution requires

Either a clever non-obvious (likely asymmetric or weakly symmetric) combinatorial construction of $\mathrm{srg}(99, 14, 1, 2)$, OR a higher-order semidefinite-programming / Terwilliger-algebra / SAT-certified refutation proving global inconsistency of the 84-vertex second subconstituent.

## Related problems

- [The Hadamard Matrix Conjecture](../hadamard-matrix-conjecture/README.md)
- [The Reconstruction Conjecture (Ulam)](../reconstruction-conjecture/README.md)
- [The Hadwiger Conjecture (Graph Coloring)](../hadwiger-conjecture/README.md)
