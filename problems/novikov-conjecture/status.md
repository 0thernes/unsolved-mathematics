# Status & Frontier — The Novikov Conjecture

_Where the problem stands and what a resolution would require._

**Status: active-progress (open).** The Novikov Conjecture is unresolved in full generality but verified for an enormous and ever-growing class of discrete groups. No counterexample is known, and none is expected; the consensus is that the conjecture is *true* and that the obstacle is finding a method uniform across all groups.

## What is known (unconditional)

The conjecture holds for, among others:

- **Free abelian groups** $\mathbb{Z}^n$ (Lusztig, 1972) and amenable groups.
- **Discrete subgroups of Lie groups** and lattices (Kasparov, 1988).
- **Word-hyperbolic groups** and groups with bounded cohomology classes (Connes–Gromov–Moscovici; Connes–Moscovici, 1990).
- **Groups of finite asymptotic dimension** and, far more generally, **groups that coarsely embed into Hilbert space** (Yu, 2000) — this single theorem subsumes most "geometrically tame" groups.
- **All linear groups** $\subseteq \mathrm{GL}_n(K)$ over any field (Guentner–Higson–Weinberger, 2005).
- **Hyperbolic and CAT(0) groups, mapping class groups, $\mathrm{GL}_n(\mathbb{Z})$, and many lattices**, via the stronger Farrell–Jones Conjecture (Bartels–Lück–Reich; Bartels–Lück, 2012).

Equivalently, the **rational injectivity of the $L$-theory assembly map** (and of the Baum–Connes assembly map) is established for all these classes.

## Strongest current results (conditional vs unconditional)

Unconditionally, Yu's coarse-embeddability theorem and the Farrell–Jones results are the high-water marks. Conditionally, the **Farrell–Jones Conjecture implies Novikov** (and Borel rigidity); so any group for which FJC is proved gains Novikov for free. The standing *negative* datum is **Higson–Lafforgue–Skandalis (2002)**: Gromov monster groups yield counterexamples to the **Baum–Connes Conjecture with coefficients** (DOI 10.1007/s00039-002-8249-5). This refutes a stronger neighboring conjecture and shows the coarse-embedding method cannot be the whole story — but it does **not** refute Novikov, which remains open even for monster groups.

## What a full resolution would require

A proof for *all* discrete groups must handle groups whose large-scale geometry defeats Hilbert-space embedding — paradigmatically **Gromov random groups containing expanders** and groups with **property (T)**. The needed advance is either (a) a new index-theoretic invariant insensitive to the expander obstruction (work on Banach-space/$\ell^p$ and warped-cone methods, and on the "Hilbert–Hadamard space" embeddings of Gong–Wu–Yu, pushes here), or (b) a purely homotopy-theoretic/controlled-topology assembly argument that bypasses analysis entirely. A disproof would require exhibiting a closed manifold whose higher signature changes under a homotopy equivalence — for which there is no candidate.

## Plausible routes

1. **Beyond Hilbert space:** coarse embeddings into $\ell^p$ spaces, Banach spaces, or Hilbert–Hadamard spaces (Kasparov–Yu; Gong–Wu–Yu) to capture monster groups.
2. **Farrell–Jones expansion:** enlarging the class of groups satisfying FJC via new flow-space and transfer techniques.
3. **Quantitative / controlled $K$-theory:** Oyono-Oyono–Yu's controlled assembly to localize the obstruction.
4. **Hybrid analytic–topological descent** unifying the surgery and operator-algebra pictures.

## Related problems

- [Baum–Connes Conjecture](../baum-connes-conjecture/README.md) — the stronger $C^*$-algebraic statement that implies Novikov; its coefficient form is known to fail.
- [Hodge Conjecture](../hodge-conjecture/README.md) — kindred question on which characteristic/cohomology classes are realized by geometry.
- [Connes Embedding (aftermath)](../connes-embedding-aftermath/README.md) — operator-algebraic embeddability questions in the same analytic milieu.
- [Yang–Mills Mass Gap](../yang-mills-mass-gap/README.md) — index-theoretic and functional-analytic methods overlap with the Dirac-operator toolkit.
