# History — Brennan's Conjecture

_Origin, formulation, and timeline._

Brennan's conjecture is a sharp regularity statement about conformal mappings, posed by James E. Brennan in 1978. It belongs to the same circle of problems as the Bieberbach conjecture, Carleson's coefficient problems, and the theory of integral means of univalent functions, and it remains open in its critical range.

## Statement and reformulations

Let $\Omega \subsetneq \mathbb{C}$ be a simply connected domain and let $\varphi:\Omega \to \mathbb{D}$ be a conformal map onto the unit disk. Equivalently, let $\psi = \varphi^{-1}:\mathbb{D}\to\Omega$ be the Riemann map. Brennan's conjecture asserts that
$$\int_{\Omega} |\varphi'(z)|^{p}\, dA(z) < \infty \quad\text{for all } \tfrac{4}{3} < p < 4,$$
where $dA$ is planar Lebesgue measure. The non-trivial endpoint is $p \to 4$: the conjecture is that the upper bound for which finiteness holds for *every* such $\Omega$ is exactly $4$. The lower endpoint $p>4/3$ is the elementary part, established by area considerations on $\psi$.

A standard reformulation transfers the integral to the disk. Writing the integral in terms of $\psi'$ on $\mathbb{D}$, finiteness of $\int_\Omega |\varphi'|^p\,dA$ for $p<4$ is equivalent to a bound on the integral means $\int_0^{2\pi}|\psi'(re^{i\theta})|^{q}\,d\theta$ with the conjugate exponent $q = -p/(2-p)$, i.e. a statement about the **integral means spectrum** $\beta_\psi(t)$ of bounded univalent functions at a specific negative $t$. In Makarov's notation the conjecture is equivalent to the universal bound $B(-2) = 1$, where $B(t) = \sup_\psi \beta_\psi(t)$ over all bounded univalent $\psi$. This places Brennan's conjecture squarely inside the universal integral means spectrum program.

## Timeline

**1973** — Carleson and others sharpen the theory of harmonic measure and integral means for univalent functions, setting the stage.

**1978** — James E. Brennan formulates the conjecture in the context of weighted polynomial approximation and the $L^p$ integrability of derivatives of conformal maps; the precise exponent $4$ is conjectured.

**1985** — Nikolai Makarov's work on harmonic measure and the law of the iterated logarithm reframes such problems via the integral means spectrum, giving the modern $B(t)$ language.

**1989–1994** — Carleson and Jones connect the coefficient/integral-means problems to multifractal analysis and to the Hausdorff dimension of harmonic measure, providing numerical and conceptual evidence near the conjectured exponents.

**1990s** — Pommerenke's monograph *Boundary Behaviour of Conformal Maps* (1992) systematizes the integral means framework; partial integrability results push the established exponent upward from the trivial bound.

**1994** — Carleson–Makarov and related analyses give bounds on the universal spectrum that translate to partial progress on Brennan's exponent.

**2005** — Hedenmalm and Shimorin introduce a Bergman-space / heat-flow ("Brennan via Bergman kernels") approach, obtaining one of the strongest unconditional lower bounds on the admissible exponent at the time.

**2007–2008** — Bertilsson's thesis results and subsequent refinements give explicit numerical bounds on $B(t)$; the best provable exponent stands strictly below $4$.

**2013–2015** — Work linking Brennan's conjecture to the conjectured universal spectrum $B(t)=|t|^2/4$ (for small $t$) and to SLE/coupling heuristics sharpens the expected answer without resolving the endpoint.

**2018–2024** — Numerical experiments (extremal Julia-set and snowflake-type domains) and continued analytic refinements keep the best rigorous exponent close to but below $4$; the conjecture remains open at its critical endpoint.

The mathematical core has stayed remarkably stable: the trivial range and one endpoint are easy, the opposite endpoint $p=4$ is the entire difficulty, and every serious advance has been a fractional improvement of the provable threshold toward $4$.
