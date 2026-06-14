# Status & Frontier — The Fontaine–Mazur Conjecture

_Where the problem stands and what a resolution would require._

**Status: open, active progress.** The conjecture is unproven in general. It is, however, the rare open problem whose flagship case is "morally settled," and the gap between what is known and what is conjectured is unusually well mapped.

## What is known (unconditional)

The strongest unconditional result is the **$\mathrm{GL}_2$ over $\mathbb{Q}$** case. Kisin (2009) proved that an irreducible, odd, continuous $\rho: G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}_p})$ that is de Rham at $p$ with distinct (regular) Hodge–Tate weights is modular — hence geometric — outside a short list of degenerate residual situations. Emerton's completed-cohomology method gives an independent proof of large parts of the same statement. The residual modularity input these proofs require is supplied unconditionally over $\mathbb{Q}$ by **Serre's conjecture**, proved by Khare–Wintenberger (2009). Together with Breuil–Conrad–Diamond–Taylor (2001) on elliptic curves, this means: every elliptic curve over $\mathbb{Q}$, and essentially every regular odd two-dimensional geometric Galois representation of $G_{\mathbb{Q}}$, is automorphic.

## What is known (conditional)

In higher rank and over general number fields the results are largely **conditional or potential**. Potential automorphy (Taylor and collaborators; the 2023 potential-automorphy-over-CM-fields work) establishes automorphy after base change for **regular, essentially self-dual** representations, sufficient for Sato–Tate but weaker than the conjecture over the base field. Calegari–Geraghty (2018) extend modularity lifting to defect $\ell_0 > 0$ (e.g. imaginary quadratic fields, $\mathrm{GL}_n$) but contingent on expected properties of Galois representations attached to torsion cohomology and on local–global compatibility at $p$. Scholze's torsion construction supplies such representations but not, in full generality, the local conditions needed to close the argument.

## What a full resolution requires

1. A **$p$-adic local Langlands correspondence beyond $\mathrm{GL}_2(\mathbb{Q}_p)$** — the local engine that turns the de Rham condition into automorphic vectors. This is the dominant obstruction; it exists essentially only for $\mathrm{GL}_2(\mathbb{Q}_p)$.
2. **Unconditional local–global compatibility** and full control of Galois representations in the **torsion cohomology** of locally symmetric spaces, removing the conditionality in Calegari–Geraghty-type theorems.
3. A path to the **non-self-dual** case, where no Shimura variety directly produces the Galois representation.
4. Removal of the **regularity (distinct Hodge–Tate weights)** and oddness hypotheses, reaching irregular / weight-one and even-image situations.

## Plausible routes

The most active routes are the derived-deformation program (Calegari–Geraghty, Gee–Newton), the categorical/geometrization of local Langlands (Fargues–Scholze) feeding a spectral-action approach, and continued extension of potential automorphy. A clean general theorem likely awaits a usable higher-rank $p$-adic local Langlands, which most experts regard as years to decades away.

## Related problems

- [Tate Conjecture](../tate-conjecture/) — the analogous "cohomological origin" principle for algebraic cycles and $\ell$-adic representations.
- [Birch–Swinnerton-Dyer Conjecture](../birch-swinnerton-dyer/) — concerns the same elliptic-curve / modular-form objects whose Galois representations the conjecture governs.
- [Inverse Galois Problem](../inverse-galois-problem/) — a parallel structural question about realizing groups and representations of $G_{\mathbb{Q}}$.
- [Grand Riemann Hypothesis](../grand-riemann-hypothesis/) — concerns the $L$-functions attached to the automorphic forms predicted to exist here.
