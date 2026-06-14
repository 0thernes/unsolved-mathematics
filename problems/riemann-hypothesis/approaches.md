# Approaches — The Riemann Hypothesis

_Major strategies, partial results, and barriers._

## Zero-detection and critical-line methods

The most direct line of attack proves that some, then most, then ideally all non-trivial zeros lie on $\Re(s)=\tfrac12$. Hardy (1914) showed infinitely many zeros lie on the line using the sign changes of the real-valued function $Z(t)$. Selberg (1942) proved a *positive proportion* lie on the line; Levinson (1974), via mollified moments and his theorem on zeros of $\zeta'$, pushed this past one third; Conrey (1989) reached more than two fifths (40.7%), and subsequent refinements (Bui–Conrey–Young, Pratt–Robles–Zaharescu) inch toward but stay well below 50%. **Barrier:** these are positive-proportion results; the method, resting on second- and fourth-moment mollifiers, has no known route to "100% on the line, none off it." Even a full-density result would not exclude finitely or sparsely many off-line zeros.

## Hilbert–Pólya / spectral approach

The idea, attributed to Hilbert and Pólya, is to realize the imaginary parts of the zeros $\tfrac12+i\gamma$ as eigenvalues of a self-adjoint operator $H$; self-adjointness forces $\gamma\in\mathbb{R}$ and hence RH. Montgomery's (1973) pair-correlation conjecture and Dyson's observation that the zero statistics match the Gaussian Unitary Ensemble (GUE) of random Hermitian matrices gave this striking empirical support, confirmed in large-scale computation by Odlyzko. Berry–Keating proposed a candidate classical Hamiltonian $H\sim xp$. **Barrier:** no one has produced a natural self-adjoint operator whose spectrum is provably the zeta zeros. The Connes (1999) trace-formula program reformulates RH as a positivity (a Lefschetz/trace identity over the adèle class space), recasting the difficulty rather than removing it; the needed positivity remains unproven.

## Function-field and arithmetic-geometry analogues

For zeta functions of curves and varieties over finite fields, the analogue of RH is a *theorem*: Weil (1948) proved it for curves and abelian varieties, and Deligne (1974) proved the Weil conjectures in general, using $\ell$-adic cohomology and the geometry of the Frobenius. This shows RH is not isolated and gives a template—cohomology with a positive-definite pairing. **Barrier:** the proofs depend essentially on an underlying geometry (a variety over $\mathbb{F}_q$, with Frobenius and Poincaré duality) that has no established counterpart for $\zeta(s)$ over $\mathbb{Q}$. The search for the "field with one element" $\mathbb{F}_1$ and an arithmetic geometry over it is an attempt to supply that missing structure; it remains speculative.

## Explicit-formula / positivity criteria

Weil's explicit formula recasts RH as the positivity of a certain quadratic functional (the Weil distribution) on test functions; Weil's positivity criterion states RH holds iff this functional is non-negative. Related are Li's criterion (RH iff the Li coefficients $\lambda_n\ge0$ for all $n\ge1$) and the Báez-Duarte / Nyman–Beurling formulation (RH iff a specific dilation family is dense in $L^2(0,1)$). **Barrier:** each converts RH into an equivalent positivity or density statement that is no easier to establish unconditionally; they organize the problem and guide computation but have not been pushed through.

## Analytic / sieve and moment methods

Zero-free regions—the foundation of the Prime Number Theorem—give unconditional but far weaker information: de la Vallée Poussin's region, the Vinogradov–Korobov region $\sigma>1-c/(\log t)^{2/3}(\log\log t)^{1/3}$, and zero-density estimates (Ingham, Huxley) bounding the number of possible off-line zeros. Moment computations (Hardy–Littlewood, Ingham; the CFKRS random-matrix predictions, 2005) describe the average behavior of $\zeta$ on the line. **Barrier:** zero-free regions have not been widened to a *strip* of positive width inside the line, and there is a recognized obstruction—any subconvexity/zero-density approach hits the limit that one cannot currently rule out a Siegel-type or exceptional zero by these means; the *parity problem* of sieve theory blocks naive sieve attacks on the prime correlations that underlie strong forms.

## De Bruijn–Newman constant

One can deform $\zeta$ via the heat flow, parameterizing a family $H_t$ whose $t=0$ member encodes the zeros; RH is equivalent to $\Lambda\le 0$ for the de Bruijn–Newman constant $\Lambda$. Newman conjectured $\Lambda\ge0$, suggesting RH, if true, is "barely true." **Result:** Rodgers and Tao (2020) proved $\Lambda\ge0$, confirming Newman's conjecture; Polymath15 (2019) established the upper bound $\Lambda\le0.22$. **Barrier:** closing the gap to prove $\Lambda\le0$ *is* RH, and the flow-based methods that gave the lower bound do not obviously supply the matching upper bound.
