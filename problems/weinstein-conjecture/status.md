# Status & Frontier — The Weinstein Conjecture

**Metadata status: active-progress.** The conjecture is *proved in dimension three* and *open in dimensions $\geq 5$*. It is neither fully resolved nor disputed: the three-dimensional theorem is settled and accepted, while the general statement remains a major open problem.

## What is known (unconditional)

- **Dimension three — solved.** Every Reeb vector field on a closed contact 3-manifold has a closed orbit. This is **Clifford Taubes, *The Seiberg–Witten equations and the Weinstein conjecture*, Geom. Topol. 11 (2007)** (arXiv:math/0611007, high confidence in author/year/venue). The proof uses Seiberg–Witten Floer theory and the nontriviality of the monopole invariant; it is independent of contact-homology transversality and is universally accepted.
- **Euclidean case, all dimensions.** Every hypersurface of contact type in $\mathbb{R}^{2n}$ carries a closed characteristic — **Viterbo (1987)**.
- **Overtwisted contact structures**, in every dimension where the notion is defined, have closed Reeb orbits (Hofer in dimension three; higher dimensions after Borman–Eliashberg–Murphy).
- **Multiplicity in dimension three.** Every contact form on a closed 3-manifold has **at least two** embedded Reeb orbits (Cristofaro-Gardiner–Hutchings, 2016), and infinitely many in many/generic cases (Cristofaro-Gardiner–Hutchings–Pomerleano and later work).

## What is known (conditional / restricted)

In dimensions $\geq 5$, existence is established for:
- contact manifolds admitting a **symplectic filling**, via symplectic homology / Rabinowitz–Floer homology (Cieliebak–Frauenfelder–Oancea and collaborators);
- **Boothby–Wang / prequantization bundles** and subcritically Stein-fillable manifolds;
- cases where **contact homology** is well-defined and nonvanishing (now on firm footing via polyfold/virtual foundations of Hofer–Wysocki–Zehnder and Pardon).

These results all carry hypotheses (fillability, special topology, displaceability) that the conjecture itself does not assume.

## What a full resolution requires

The remaining problem is the **unconditional statement in dimensions $\geq 5$**: a closed Reeb orbit for *every* contact form on *every* closed contact manifold of dimension $\geq 5$, with no fillability or topological hypothesis. The obstruction is structural. The decisive three-dimensional tool — Seiberg–Witten Floer theory / ECH — is intrinsically low-dimensional and has no known analogue in higher dimensions. A general proof would need either a higher-dimensional invariant of comparable force, or a holomorphic-curve/SFT argument that does not require a filling, or an entirely new mechanism guaranteeing orbits from the contact-type condition alone.

## Plausible routes

1. **Higher-dimensional Floer or gauge invariants** that play the role ECH plays in dimension three, detecting orbits without a filling.
2. **Foundationally complete SFT/contact homology** (post-polyfold) proving nonvanishing in full generality, removing the fillability hypothesis.
3. **Holomorphic-curve compactness arguments** generalizing Hofer's degeneration beyond the overtwisted and fillable regimes.
4. **Quantitative/dynamical inputs** (e.g., from symplectic capacities or $C^0$-dynamics) forcing orbits abstractly.

No counterexample is known or expected; the consensus is that the conjecture is true in all dimensions and the difficulty is method, not truth.

## Related problems

- [Birkhoff Conjecture](../birkhoff-conjecture/README.md) — billiard dynamics and integrability, closely tied to Reeb/Hamiltonian flows.
- [Hilbert's Sixteenth Problem](../hilbert-sixteenth-problem/README.md) — limit cycles and periodic orbits of planar vector fields.
- [Smooth 4-Dimensional Poincaré Conjecture](../smooth-4d-poincare-conjecture/README.md) — adjacent low-dimensional topology where gauge theory is decisive.
- [Yang–Mills Mass Gap](../yang-mills-mass-gap/README.md) — another problem driven by gauge-theoretic analysis.
