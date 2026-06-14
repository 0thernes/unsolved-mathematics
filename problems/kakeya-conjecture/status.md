# Status & Frontier — The Kakeya Conjecture

_Where the problem stands and what a resolution would require._

**Status: active progress, with the three-dimensional case recently claimed resolved.** The conjecture — every Kakeya (Besicovitch) set in $\mathbb{R}^n$ has Hausdorff and Minkowski dimension $n$ — is a theorem for $n=2$ (Davies, 1971) and, as of 2025, is reported solved for $n=3$. It remains open for every $n \ge 4$.

## What is known (unconditional)

- **$n=2$:** Fully resolved. Every planar Kakeya set has Hausdorff dimension $2$ (Davies, 1971); the Minkowski version holds too.
- **$n=3$:** **Hong Wang and Joshua Zahl (2025)** announced a proof that every Kakeya set in $\mathbb{R}^3$ has Hausdorff and Minkowski dimension $3$ — *"Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions"* (Wang & Zahl, 2025; arXiv:2502.17655, identifier to be verified). The argument reduces to sticky Kakeya sets and runs a multi-scale grains/projection analysis. As a very recent, very long manuscript it is in the normal process of community verification; it should be cited as the claimed/announced resolution of $n=3$.
- **General $n$ (lower bounds):** Wolff's hairbrush gives Hausdorff dimension $\ge \tfrac{n+2}{2}$. The additive-combinatorics method (Bourgain 1999; Katz–Tao) improves this in high dimensions to roughly $\ge (2-\sqrt{2})(n-4)+3$, i.e. asymptotically about $0.596\,n$ — still far below $n$ for large $n$.
- **Model problem:** The **finite-field Kakeya conjecture** is fully proved (Dvir, 2009): a Kakeya set in $\mathbb{F}_q^n$ has $\gtrsim_n q^n$ points. This does **not** transfer to $\mathbb{R}^n$.
- **Multilinear version:** The sharp multilinear Kakeya inequality is proved (Bennett–Carbery–Tao 2006; Guth 2010), but it bypasses the hard non-transverse regime.

## What a full resolution would require

A proof for general $n$ must control the **sticky, non-transverse** configurations where tubes cluster into lower-dimensional structures — precisely the regime the multilinear and finite-field methods cannot see. The $\mathbb{R}^3$ proof leans on three-dimensional incidence geometry, Bourgain's projection theorem, and Furstenberg-set estimates that are not yet available in sharp form in higher dimensions. Extending to $n \ge 4$ plausibly requires: (i) higher-dimensional projection and Furstenberg-set theory of comparable strength; (ii) a robust multi-scale induction (grains/structure) that survives the richer geometry of $k$-planes for $1 < k < n-1$; and (iii) handling intermediate-dimensional concentration phenomena absent in $\mathbb{R}^3$.

## Plausible routes

The most promising route is to generalize the **Wang–Zahl sticky-Kakeya / projection program** to $n\ge 4$, developing the missing higher-dimensional Furstenberg and projection estimates. Parallel programs — polynomial partitioning (Guth–Katz), decoupling (Bourgain–Demeter), and $k$-broad restriction estimates — feed Kakeya progress and are reciprocally advanced by it. A full resolution would have large downstream consequences: Kakeya is a necessary case of the **restriction**, **Bochner–Riesz**, and **local smoothing** conjectures, so progress here propagates up the tower of harmonic-analysis problems.

## Related problems

- [Riemann Hypothesis](../riemann-hypothesis/README.md)
- [Hilbert's Sixteenth Problem](../hilbert-sixteenth-problem/README.md)
- [Hadwiger–Nelson Problem](../hadwiger-nelson-problem/README.md)
- [Inscribed Square Problem](../inscribed-square-problem/README.md)
- [Montgomery Pair Correlation](../montgomery-pair-correlation/README.md)
