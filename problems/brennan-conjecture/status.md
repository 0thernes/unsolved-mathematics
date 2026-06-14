# Status & Frontier — Brennan's Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** Brennan's conjecture (1978) is unresolved at its critical endpoint. No accepted proof or disproof exists; the dossier records no resolution claim.

## What is known (unconditional)

Let $\varphi:\Omega\to\mathbb{D}$ be conformal on a simply connected $\Omega\subsetneq\mathbb{C}$. The integrability
$$\int_\Omega |\varphi'(z)|^p\,dA(z) < \infty$$
holds for all $p$ in a range $(4/3,\, p_0)$ with $p_0 < 4$ proven, and is conjectured to hold for the full open interval $(4/3,4)$.

- The lower endpoint $p>4/3$ is elementary (area/Koebe estimates on the inverse map) and is a theorem.
- The conjecture is equivalent to the universal integral means spectrum identity $B(-2)=1$, where $B(t)=\sup_\psi \beta_\psi(t)$ over bounded univalent $\psi$.
- Successive upper bounds on $B(t)$ — Makarov; Carleson–Makarov (1994); Pommerenke; Bertilsson (1999); Hedenmalm–Shimorin (2005, Bergman-kernel method) — establish integrability up to a $p_0$ strictly below $4$. The Hedenmalm–Shimorin estimate is among the strongest unconditional results.
- Lower-bound (negative-direction) work, e.g. Kayumov-type results, shows the parabolic law $B(t)=t^2/4$ fails for large $|t|$, constraining any proof at $t=-2$.

## What is known (conditional)

- Brennan's conjecture follows immediately from the **universal spectrum conjecture** $B(t)=t^2/4$ for $|t|\le 2$ (Kraetzer's conjecture), evaluated at $t=-2$. It is thus a single-point corollary of a widely believed sharp identity.
- For self-similar / conformally dynamical boundaries (snowflakes, certain Julia sets), the integral means spectrum can be computed via thermodynamic formalism and matches $B(-2)=1$ in those classes (Beliaev–Smirnov and related). This is sharp only within those special families.

## What a full resolution requires

A proof must establish $B(-2)=1$ — i.e. close the gap between the best provable $p_0$ and $4$ — by controlling genuinely fractal extremal univalent functions, not merely dynamical or self-similar examples. Equivalently, one must show the universal supremum over *all* simply connected domains does not exceed the value attained by the snowflake/Julia candidates. A disproof would exhibit a domain forcing divergence for some $p<4$, contradicting all current numerics; no such example or obstruction is known, and the weight of evidence favors the conjecture.

## Plausible routes

1. Prove the universal spectrum conjecture $B(t)=t^2/4$ on $|t|\le 2$ (or just at $t=-2$), perhaps via an improved Bergman-kernel/asymptotic-variance identity extending Hedenmalm–Shimorin to the endpoint.
2. Establish a rigorous extremality theorem identifying snowflake/Julia-set boundaries as universal maximizers near $t=-2$.
3. Import sharp SLE/coupling estimates from the small-$|t|$ regime up to the boundary value $t=-2$, controlling the transition where the parabolic law is known to eventually fail.

## Related problems

- [Kakeya conjecture](../kakeya-conjecture/) — kindred sharp-exponent / fractal-geometry problem in harmonic analysis, with extremal sets analogous to extremal domains here.
- [Invariant subspace problem](../invariant-subspace-problem/) — adjacent operator/function-theory question; Brennan's own route to the conjecture passed through weighted approximation and invariant subspaces.
- [Sendov's conjecture](../sendov-conjecture/) — sibling sharp-constant problem in complex analysis / geometry of polynomials.
- [Crouzeix's conjecture](../crouzeix-conjecture/) — another conjectured sharp constant in complex analysis where the extremal configuration resists proof.
