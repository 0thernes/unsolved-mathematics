# Status & Frontier — Hilbert's Sixteenth Problem (Second Part)

_Where the problem stands and what a resolution would require._

**Status: open.** More than a century after 1900, the core question is unanswered even in its simplest nontrivial case. The Hilbert number $H(n)$ — the maximum number of limit cycles of a real planar polynomial vector field of degree $n$ — is not known to be **finite** for any $n \ge 2$. In particular it is unknown whether $H(2) < \infty$ for quadratic systems. This is the central, embarrassing gap: no one can rule out that some sequence of degree-2 systems has unboundedly many limit cycles.

## What is known (unconditional)

- **Individual finiteness.** Every *fixed* analytic planar vector field has finitely many limit cycles (Ilyashenko 1991; Écalle 1992), repairing Dulac's flawed 1923 proof. This bounds cycles for each system separately but gives **no** degree-uniform bound, hence does not bound $H(n)$.
- **Local cyclicity.** Bautin (1952): at most $3$ small-amplitude cycles bifurcate from a focus/center of a quadratic system. Analogous finite local bounds exist for cubics.
- **Lower bounds.** $H(2)\ge 4$ (Shi 1980; Chen–Wang 1979); $H(3)\ge 13$ (Chinese-school constructions); and for general $n$, configurations of order $n^2\log n$ cycles are known, giving $H(n)\gtrsim \tfrac{1}{2}n^2\log n$. The growth is therefore at least slightly super-quadratic.
- **Smale's Liénard restriction** and slow–fast canard theory give finite, computable bounds in special families, but the Lins–de Melo–Pugh conjectured bound for general polynomial Liénard systems is **false** (Dumortier–Panazzolo–Roussarie 2007).

## Strongest conditional / partial results

The most tractable proxy is the **infinitesimal (weakened) Hilbert 16th problem**: bound the number of zeros of Abelian integrals $I(h)=\oint_{\gamma_h}\omega$ over degree-$n$ Hamiltonians and forms. Binyamini, Novikov and Yakovenko (2010, *Inventiones*) proved an **explicit uniform upper bound** for the number of such zeros at bounded distance from the boundary of the period annulus — the first fully effective uniform result, albeit with an astronomically large bound. Sharp counts are known for special families (elliptic Hamiltonians, the quadratic infinitesimal case). A finite infinitesimal bound is necessary groundwork but is **not** equivalent to a finite $H(n)$: passing from the first-order Melnikov approximation to the actual cycles requires controlling all higher orders and the loss of integrability.

## What a full resolution would require

A complete solution would need to (i) prove $H(n)$ is finite for every $n$ — the **existence** of the bound — and ideally (ii) compute or bound it, plus describe the **relative position/configuration** of the cycles. The decisive obstruction is the possible accumulation of limit cycles onto a **polycycle** (the Hilbert–Arnold problem: uniform finite cyclicity of limit periodic sets across a family). This is proven only for **elementary** polycycles (all vertices hyperbolic/semi-hyperbolic; Ilyashenko–Yakovenko, Kaloshin); the general case, with degenerate (nilpotent) and non-monodromic vertices, is open and is exactly what blocks a uniform bound.

## Plausible routes

1. **Effective/tame-geometry program** — make Ilyashenko–Écalle finiteness *quantitative* via o-minimality, pfaffian bounds, and Pila–Wilkie-style point counting (Binyamini–Novikov and collaborators). Most credible path to a uniform bound.
2. **Complete the Hilbert–Arnold finite-cyclicity program** for all polycycles up to some degree, then assemble a bound on $H(n)$ via compactness of the parameter space.
3. **Quadratic-only attack** — even just proving $H(2)<\infty$ (the long-conjectured value is $4$) would be a landmark and might isolate the essential difficulty.

## Related problems

- [Kakeya Conjecture](../kakeya-conjecture/README.md) — another deep question at the interface of real analysis and geometric measure of solution sets.
- [Jacobian Conjecture](../jacobian-conjecture/README.md) — polynomial maps and their global behavior, a sibling in real/complex algebraic dynamics.
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — the comparison case among Hilbert's problems for "famous, deep, and resistant."
- [Navier–Stokes Smoothness](../navier-stokes-smoothness/README.md) — a sibling open problem in the qualitative theory of differential equations.
