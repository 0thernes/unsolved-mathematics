# Status & Frontier — The Whitehead Asphericity Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** Posed by J. H. C. Whitehead in 1941, the conjecture — *every connected subcomplex of an aspherical $2$-dimensional CW complex is itself aspherical* — has neither been proved in general nor refuted by a counterexample in over eighty years. There is no claimed resolution, disputed or otherwise, of the full statement.

## What is known (unconditional)

The conjecture is a **theorem in substantial special classes**:

- **One-relator complexes.** Via Lyndon's Identity Theorem, a one-relator presentation with non-proper-power relator is aspherical, and deleting its single $2$-cell trivially preserves asphericity. Confirmed.
- **Locally indicable fundamental group.** Howie proved subcomplex-asphericity whenever $\pi_1$ is locally indicable, covering a broad torsion-free range.
- **Diagrammatically reducible (DR) complexes.** Asphericity-by-reducibility is inherited by subcomplexes automatically; thus the conjecture holds for all complexes satisfying small-cancellation conditions ($C(6)$, $C(4)\&T(4)$) or a valid weight test (Gersten, Sieradski, Pride, Huck–Rosebrock).
- **Finite-case constraints.** Howie's reduction shows any *finite* counterexample forces a fundamental group outside the locally indicable class, carrying torsion, with sharply restricted structure.

## What is known (conditional / structural)

The dominant structural result is the **finite-vs-infinite dichotomy**: a counterexample, if it exists, is either finite (and then heavily constrained per Howie) or genuinely infinite, likely arising as an ascending union of relators. The infinite version is widely regarded as the more plausible home of a counterexample. The problem is also **entangled with other open questions** — the **Eilenberg–Ganea problem**, the **relation gap problem**, and coherence of one-relator groups — sometimes via implications running in the direction that a counterexample to one could feed a counterexample to another, which is part of why it is considered hard.

## What a full resolution would require

A **proof** must reach the residual class that all current tools miss: aspherical $2$-complexes that are **not diagrammatically reducible** and whose fundamental group is **not locally indicable** (in particular, groups with torsion). This requires a method to certify $\pi_2(L)=0$ for a subcomplex $L$ from asphericity of $K$ *without* assuming reducibility or indicability — for example, an exactness argument over $\mathbb{Z}[\pi_1]$ that survives deletion of cells, or a new curvature/$L^2$-vanishing principle valid for torsion groups. A **disproof** would exhibit an aspherical $2$-complex $K$ with a subcomplex $L$ having nonzero $\pi_2$; the most-pursued route is an infinite construction (acyclic / Andrews–Curtis-flavored) where $\pi_2$ of a sub-presentation is forced nonzero in the colimit.

## Plausible routes

1. **$L^2$-homology and the Atiyah conjecture** — vanishing theorems for $\ell^2$-Betti numbers that would push past the locally indicable barrier.
2. **One-relator coherence and negative curvature** — leveraging recent advances (Wilton, Linton, and collaborators) on one-relator and hyperbolic-like groups to enlarge the confirmed class.
3. **Infinite counterexample search** — explicit ascending unions or acyclic complexes engineered to break asphericity, informed by relation-gap phenomena.
4. **Sharper diagrammatic invariants** — refinements of weight tests / test maps that detect asphericity beyond strict reducibility.

## Related problems

- [Andrews–Curtis Conjecture](../andrews-curtis-conjecture/README.md)
- [Eilenberg–Ganea / Hilbert–Smith Conjecture](../hilbert-smith-conjecture/README.md)
- [Novikov Conjecture](../novikov-conjecture/README.md)
- [Baum–Connes Conjecture](../baum-connes-conjecture/README.md)
- [Connes Embedding (aftermath)](../connes-embedding-aftermath/README.md)
