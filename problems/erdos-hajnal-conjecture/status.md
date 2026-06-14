# Status & Frontier — The Erdős–Hajnal Conjecture

_Where the problem stands and what a resolution would require._

**Status: open, with active progress.** The conjecture is unresolved in full generality. It is firmly believed to be true, and the last few years have seen the first real movement on both the general bound and on previously inaccessible cases.

## What is known (unconditional)

- **General lower bound.** Every $n$-vertex $H$-free graph contains a homogeneous set of size at least $\exp\big(c(H)\sqrt{\log n \,\log\log n}\big)$ (Nguyen, Scott, Seymour, 2022–2023), improving for the first time the classical $\exp\big(c\sqrt{\log n}\big)$ of Erdős–Hajnal (1989). Both are *subpolynomial* — short of the conjectured $n^{c}$.
- **Verified $H$.** The conjecture holds for: all graphs on $\le 4$ vertices; all **cographs** ($P_4$-free graphs), via the substitution theorem (Alon–Pach–Solymosi, 2001); the **bull** (Chudnovsky–Safra, 2015); the **five-cycle $C_5$** (Bucić–Nguyen–Scott–Seymour, 2023); and the closures of all these under substitution and blow-up, plus several additional sporadic graphs from the 2023–2024 Nguyen–Scott–Seymour papers.
- **Tournament analogue.** A directed analogue is established for many tournaments (Berger–Choromanski–Chudnovsky and successors).
- **Equivalences.** The clique/stable-set form, the bi-clique ("large complete or empty bipartite pair") form, and the polynomial Rödl property are known to be equivalent (Fox–Sudakov), so resolving any one resolves all.

## What is known (conditional / structural)

- For **stable** classes (forbidding a half-graph, i.e. an order property), homogeneous sets of *linear* size exist — far stronger than EH, but under a stronger hypothesis.
- Bounded-VC-dimension (NIP) regularity gives strong structure for $H$-free classes, but not yet polynomial homogeneity; the gap is exactly the unstable part.

## What a full resolution requires

A proof must handle **prime graphs**, where substitution gives nothing, *uniformly* across all $H$ — the present case-by-case structural arguments do not generalize. Equivalently, one must produce, for every $H$, a homogeneous set of size $n^{c(H)}$, crossing the subpolynomial wall that all general methods (including regularity-based ones, which incur $\exp(\sqrt{\log n})$-type losses) currently hit. Even prominent small cases — notably the path $P_5$ — remain open, so a uniform technique is the central missing ingredient.

## Plausible routes

1. **Extend the $C_5$ machinery** (tree-decomposition / asymptotic-dimension structure of induced subgraphs) to broader families of prime graphs, ideally to all paths and then to a general principle.
2. **Break the regularity barrier** with an essentially regularity-free argument that converts local pattern-avoidance directly into polynomial order.
3. **Model-theoretic tameness**: leverage NIP structure to recover polynomial (not merely subpolynomial) homogeneity, bridging the stable and unstable cases.
4. **Further improve the general exponent** beyond $\sqrt{\log n\,\log\log n}$, ideally to $(\log n)^{1-o(1)}$ in the exponent, which would be a major step toward the polynomial target.

## Related problems

- [Hadwiger Conjecture](../hadwiger-conjecture/README.md)
- [Total Coloring Conjecture](../total-coloring-conjecture/README.md)
- [Seymour's Second Neighborhood Conjecture](../seymour-second-neighborhood-conjecture/README.md)
- [Reconstruction Conjecture](../reconstruction-conjecture/README.md)
- [Unit Distance Problem](../unit-distance-problem/README.md)
