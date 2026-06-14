# History — The Fontaine–Mazur Conjecture

_Origin, formulation, and timeline._

## Origin

The conjecture grew out of two converging streams of late-twentieth-century arithmetic geometry: the theory of $p$-adic Galois representations attached to algebraic varieties, and the increasingly precise dictionary between Galois representations and automorphic forms (the Langlands program). By the early 1990s it was understood, largely through the work of Jean-Marc Fontaine in $p$-adic Hodge theory, that the $p$-adic étale cohomology of a smooth proper variety over a number field carries a Galois representation with two decisive properties: it is **unramified at almost all primes**, and at primes above $p$ it is **de Rham** (equivalently, "geometric" in the local sense). Fontaine and Barry Mazur proposed the converse: these two properties characterize the representations of geometric origin.

The crystallization of this idea is the 1995 paper *Geometric Galois representations* (in *Elliptic Curves, Modular Forms, & Fermat's Last Theorem*, Hong Kong, 1993), where Fontaine and Mazur formulate what is now the canonical statement.

## Precise formulation

Let $G_{\mathbb{Q}} = \mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ and let
$$\rho: G_{\mathbb{Q}} \longrightarrow \mathrm{GL}_n(\overline{\mathbb{Q}_p})$$
be a continuous irreducible representation. Call $\rho$ **geometric** if it is unramified outside a finite set of primes and its restriction to a decomposition group at $p$ is de Rham (in Fontaine's sense). The conjecture asserts that every geometric $\rho$ is, up to twist by a power of the cyclotomic character, a subquotient of the $p$-adic étale cohomology $H^i_{\text{ét}}(X_{\overline{\mathbb{Q}}}, \mathbb{Q}_p)$ of some smooth projective variety $X/\mathbb{Q}$ — and, conjecturally, that it arises from an algebraic automorphic representation. Combined with reciprocity, this makes "geometric $\Leftrightarrow$ automorphic" the operative slogan.

A celebrated corollary in dimension $2$: an irreducible geometric $\rho: G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}_p})$ that is odd and Hodge–Tate regular comes from a modular (cuspidal) eigenform. Conversely, the conjecture predicts that an irreducible $2$-dimensional $\rho$ which is **not** de Rham at $p$ — for example, one with infinite image whose Hodge–Tate weights fail to be distinct integers — cannot be geometric, ruling out "exotic" sources.

## Timeline

- **1982–1994** — Fontaine develops $p$-adic Hodge theory: the rings $B_{\mathrm{cris}}$, $B_{\mathrm{st}}$, $B_{\mathrm{dR}}$ and the notions crystalline/semistable/de Rham, supplying the local condition at $p$.
- **1993/1995** — Fontaine and Mazur state the conjecture in *Geometric Galois representations*.
- **1995** — Wiles, with Taylor–Wiles, proves modularity of semistable elliptic curves; the residual-to-$p$-adic deformation method becomes the central tool.
- **1998–2002** — Diamond, Conrad, Breuil, Taylor establish the full modularity theorem for elliptic curves over $\mathbb{Q}$ (Breuil–Conrad–Diamond–Taylor, 2001).
- **2009** — Kisin's *Fontaine–Mazur conjecture for $\mathrm{GL}_2$* proves most cases of the two-dimensional odd conjecture over $\mathbb{Q}$ via $p$-adic local Langlands and his deformation-ring techniques.
- **2008–2014** — Emerton's completed-cohomology / local–global compatibility approach gives an independent proof of large parts of the $\mathrm{GL}_2/\mathbb{Q}$ case.
- **2013–2015** — Barnet-Lamb–Gee–Geraghty–Taylor and the "potential automorphy" program extend modularity-type results to higher dimension and totally real / CM fields.
- **2015–present** — Calegari–Geraghty derived deformation rings, Scholze's work on torsion in cohomology via perfectoid methods, and category-$\mathcal{O}$ formulations push the frontier toward non-self-dual and higher-rank cases.
- **Present** — The conjecture remains **open** in general; even the full $\mathrm{GL}_2/\mathbb{Q}$ statement has residual edge cases (e.g. certain weight-one / irregular and small-image situations), and higher-dimensional cases are largely conjectural beyond potential-automorphy.
