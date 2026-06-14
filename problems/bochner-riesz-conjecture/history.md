# History — The Bochner–Riesz Conjecture

_Origin, formulation, and timeline._

## Origin

The conjecture grows out of the classical problem of summing multiple Fourier series and integrals. For a function $f$ on $\mathbb{R}^n$, the **Bochner–Riesz means** of order $\delta \geq 0$ are defined by the Fourier multiplier
$$
\widehat{S^\delta_R f}(\xi) = \left(1 - \frac{|\xi|^2}{R^2}\right)_+^{\delta} \widehat{f}(\xi),
$$
where $t_+ = \max(t,0)$. As $R \to \infty$ one asks: for which pairs $(\delta, p)$ does $S^\delta_R f \to f$ in $L^p(\mathbb{R}^n)$? At $\delta = 0$ this is the (false, for $n \geq 2$, $p \neq 2$) ball multiplier; positive $\delta$ smooths the cutoff. The mechanism was introduced by Marcel Riesz in the one-dimensional summation theory of the 1910s–1920s and lifted to several variables by Salomon Bochner in **1936**, who used these "spherical Riesz means" to study eigenfunction expansions and multiple Fourier series.

The **Bochner–Riesz conjecture** asserts that $S^\delta_R$ is bounded on $L^p(\mathbb{R}^n)$ (uniformly in $R$, hence convergence holds) precisely when
$$
\delta > \delta(p) := \max\left\{ n\left|\tfrac{1}{p} - \tfrac{1}{2}\right| - \tfrac{1}{2},\, 0 \right\}.
$$
For $\delta \le \delta(p)$ with $p \neq 2$ boundedness fails; the conjecture is the claim that this necessary condition is also sufficient. The critical case is $\delta = \delta(p)$, where boundedness fails but weak/restricted estimates are the live question. The conjecture is intimately tied to the **restriction conjecture** for the sphere and, below it, to the **Kakeya conjecture**: known implications run Restriction $\Rightarrow$ Bochner–Riesz, and Bochner–Riesz $\Rightarrow$ Kakeya (set-bound).

## Timeline

- **1936** — Bochner introduces spherical Riesz means for multiple Fourier expansions, establishing $L^p$ convergence for large $\delta$.
- **1954** — E. M. Stein develops interpolation of analytic families of operators, the basic tool for moving in $\delta$.
- **1971** — Fefferman proves the **ball multiplier theorem**: the $\delta=0$ disc multiplier is unbounded on $L^p(\mathbb{R}^n)$, $n\ge2$, $p\ne2$, using Besicovitch/Kakeya sets — cementing the Kakeya connection.
- **1972** — Carleson and Sjölin settle the planar case $n=2$ completely: $S^\delta_R$ is bounded on $L^p(\mathbb{R}^2)$ for all $\delta > \delta(p)$. The **Carleson–Sjölin theorem** remains the only full-dimensional resolution.
- **1973–74** — Fefferman, and Córdoba, give geometric/square-function proofs in the plane; Córdoba's argument isolates the Kakeya maximal function in $\mathbb{R}^2$.
- **1977** — Fefferman, Stein and others connect Bochner–Riesz to the cone and restriction problems.
- **1991** — Bourgain's breakthrough on the restriction and Kakeya problems improves the $n=3$ Bochner–Riesz range past $\delta = 1/4$.
- **1995** — Tao, Vargas, Vega and others develop the bilinear restriction method, feeding into Bochner–Riesz.
- **2003** — Tao proves a "Bochner–Riesz implies restriction" type equivalence and sharp bilinear restriction (Tao 2003) advances all three problems jointly.
- **2006** — Lee uses bilinear estimates to improve higher-dimensional ranges.
- **2011** — Bourgain and Guth introduce the **multilinear method** (via Bennett–Carbery–Tao 2006), yielding the best Bochner–Riesz ranges in dimensions $n \ge 3$ for two decades.
- **2017–2019** — Polynomial-partitioning (Guth) and the **decoupling theorem** (Bourgain–Demeter) sharpen restriction/Bochner–Riesz estimates; Guth–Hickman–Iliopoulou push the multilinear-to-linear conversion.
- **2020s** — The frontier remains: $n=2$ solved; $n\ge3$ open, with the best known ranges still short of the conjectured $\delta(p)$.
