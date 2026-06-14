# Status & Frontier — The KPZ Universality Conjecture

_Where the problem stands and what a resolution would require._

**Status: active-progress.** KPZ universality is not a single yes/no theorem but a program of convergence statements, and that program has advanced enormously while its core remains open. The honest summary: the conjecture is *proven* for a large, structurally privileged class of exactly solvable models, and *open* for genuinely generic ones.

**What is known (unconditional).**
- For exactly solvable models — longest increasing subsequences (Baik–Deift–Johansson 1999), exponential/geometric last-passage percolation (Johansson 2000), the PNG droplet (Prähofer–Spohn 2000), ASEP (Tracy–Widom 2009), and the KPZ equation with narrow-wedge data (Amir–Corwin–Quastel 2011) — the $t^{1/3}$ fluctuation exponent and the Tracy–Widom limit laws ($F_2$ for curved, $F_1$ for flat initial data) are theorems.
- The universal limiting objects exist and are constructed: the **KPZ fixed point** as a Markov process (Matetski–Quastel–Remenik 2021) and the **directed landscape** (Dauvergne–Ortmann–Virág 2022).
- **Convergence to these objects** is established for broad solvable families: TASEP/ASEP, general exclusion and several last-passage models converge to the KPZ fixed point (Quastel–Sarkar 2023; Virág and collaborators 2020+).
- For the KPZ *equation*, Hairer's regularity structures (2014) and paracontrolled/energy-solution methods give a rigorous, robust solution theory, and several **non-integrable** microscopic dynamics are proven to converge to the KPZ equation in the **weak-asymmetry (crossover) regime**.

**What is known (conditional / partial).** Correct fluctuation exponents $\big($variance of order $t^{2/3}$, spatial correlation length $t^{2/3}\big)$ are available for some less-solvable models via stationary-model and coupling arguments, but without the exact limit law. Many universality statements are conditional on integrability-adjacent assumptions on the weights or rates.

**What a full resolution requires.** A proof that an *arbitrary* $(1+1)$-dimensional growth model satisfying the KPZ symmetry assumptions — local, isotropic-up-to-tilt, with a nondegenerate curvature of the limit shape and finite-range randomness — converges, after $t^{1/3}$ centering and $t^{2/3}$ spatial rescaling, to the **directed landscape / KPZ fixed point**, with Tracy–Widom one-point marginals. The missing ingredient is a *non-integrable, non-perturbative* universality mechanism: an analogue of the Lindeberg replacement principle for the central limit theorem, but for this strongly-coupled critical scaling limit.

**Plausible routes.**
1. **Universality transfer** — prove the limit from a solvable model survives perturbation, via comparison/coupling estimates that do not rely on exact formulas (currently only crosses a thin neighborhood of the integrable locus).
2. **Geometric / geodesic methods** — leverage the directed-landscape geometry (geodesics, Busemann functions, coalescence) to characterize the limit intrinsically and then identify generic models within it.
3. **A renormalization-group construction** of the KPZ fixed point as a genuine RG attractor — the physicists' original picture, never made rigorous; this would most directly explain the breadth of the class.
4. **Stochastic-PDE bridge** — extend energy-solution / regularity-structure technology from the subcritical equation regime to the critical fixed-point regime.

No claimed proof of the non-integrable case exists, contested or otherwise; the status is steady frontier progress rather than imminent resolution.

## Related problems

- [Navier–Stokes smoothness](../navier-stokes-smoothness/) — another nonlinear stochastic/deterministic PDE where turbulence and scaling exponents resist rigorous control.
- [Yang–Mills mass gap](../yang-mills-mass-gap/) — like KPZ, hinges on constructing a renormalized continuum limit and an associated nonperturbative fixed point.
- [Self-avoiding walk](../self-avoiding-walk/) — a neighboring statistical-mechanics universality question with conjectured exponents proven only in special (e.g. high-dimensional or SLE-accessible) cases.
- [Riemann hypothesis](../riemann-hypothesis/) — connected through random matrix theory: the Tracy–Widom and sine-kernel statistics central to KPZ also govern conjectural zero-spacing laws.
