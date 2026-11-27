# Status & Frontier — The Černý Conjecture

_Where the problem stands and what a resolution would require._

**Overall status: `active-progress` (OPEN; even $O(n^2)$ or $o(n^3)$ is open).**

## What is known

- **Lower bound (sharpness):** $(n - 1)^2$ achieved for every $n \ge 2$ by Černý's 1964 family.
- **Best general upper bound:** $\le 0.1654\,n^3 + o(n^3)$ (Shitov 2019, `arXiv:1901.06542`, improving Szykuła 2017 `arXiv:1702.05455` and Pin–Frankl 1983 $n^3/6$).
- **Solved special classes:** Eulerian, circular, aperiodic, monotonic, one-cluster, and random automata satisfy quadratic (or sub-linear) bounds.
- **Formal tracking:** Formalized in Lean 4 in `google-deepmind/formal-conjectures` as `CernyConjecture.cerny_conjecture` (`kind: open`).

## What a resolution requires

First breaking the cubic barrier $o(n^3)$ — and ultimately finding a global amortized linear-algebraic or semigroup-theoretic invariant that caps total reset length at $(n-1)^2$ across all synchronizing DFAs.

## Related problems

- [The Caccetta–Häggkvist Conjecture](../caccetta-haggkvist-conjecture/README.md)
- [The Reconstruction Conjecture (Ulam)](../reconstruction-conjecture/README.md)
- [P versus NP](../p-versus-np/README.md)
