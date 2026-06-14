# History — The KPZ Universality Conjecture

_Origin, formulation, and timeline._

The KPZ universality conjecture grew out of a single 1986 letter-length paper on the physics of randomly growing interfaces, and over four decades it crystallized into one of the central organizing principles of modern probability. The claim is that an enormous and structurally diverse family of $(1+1)$-dimensional random growth models — ballistic deposition, the corner-growth/last-passage models, directed polymers in a random environment, the asymmetric simple exclusion process (ASEP), the stochastic heat equation, and more — all share the same large-scale statistics: a height function $h(x,t)$ that fluctuates on scale $t^{1/3}$, decorrelates over spatial scale $t^{2/3}$, and, after centering and rescaling, converges to a universal limiting object whose one-point laws are the **Tracy–Widom** distributions ($\mathrm{GUE}$ for curved/droplet initial data, $\mathrm{GOE}$ for flat) and whose full space-time scaling limit is the **KPZ fixed point** / **directed landscape**.

The physical origin is the **Kardar–Parisi–Zhang stochastic PDE**,
$$\partial_t h = \nu\,\partial_x^2 h + \tfrac{\lambda}{2}(\partial_x h)^2 + \sqrt{D}\,\xi,$$
with $\xi$ space-time white noise. Kardar, Parisi and Zhang argued via a dynamic renormalization (one-loop) analysis that the nonlinearity is relevant in $d=1$ and forces the exponents $\chi=1/2$, $z=3/2$ ($\beta=\chi/z=1/3$). The equation is ill-posed classically — the Cole–Hopf transform $Z=\exp(h)$ formally linearizes it into the multiplicative-noise stochastic heat equation — and giving it rigorous meaning was itself a decade-long project.

**Timeline**

- **1985** — Family–Vicsek propose the dynamic scaling ansatz $w(L,t)\sim L^\chi f(t/L^z)$ for growing surfaces, anticipating universal exponents.
- **1986** — Kardar, Parisi, Zhang publish *Dynamic Scaling of Growing Interfaces* (PRL), introducing the KPZ equation and the $1/3$–$2/3$ exponents.
- **1992** — Krug and Spohn survey the field, sharpening the conjectural exponents and connections to growth models.
- **1994** — Tracy and Widom derive the GUE largest-eigenvalue distribution $F_2$ in terms of a Painlevé II function — later the universal one-point law.
- **1999** — Baik, Deift, Johansson prove the longest increasing subsequence of a random permutation has $F_2$ fluctuations: the first rigorous KPZ-class limit theorem.
- **2000** — Johansson proves $F_2$ fluctuations for geometric/exponential last-passage percolation (corner growth).
- **2000** — Prähofer and Spohn introduce the Airy$_2$ process; the PNG (polynuclear growth) droplet is solved.
- **2009** — Tracy and Widom obtain exact ASEP transition probabilities and one-point fluctuation formulas.
- **2010–11** — Amir–Corwin–Quastel, and independently Sasamoto–Spohn (physics, 2010), establish the exact one-point distribution of the KPZ equation / continuum directed polymer with narrow-wedge data, confirming $F_2$ and the crossover.
- **2012** — Corwin's survey *The Kardar–Parisi–Zhang equation and universality class* consolidates the field.
- **2014** — Martin Hairer awarded the Fields Medal; his theory of **regularity structures** (2013) gives a rigorous solution theory for the KPZ equation. Paracontrolled distributions (Gubinelli–Imkeller–Perkowski) appear in parallel.
- **2014** — Borodin–Corwin's **Macdonald processes** provide an algebraic engine for exactly solvable models.
- **2016–18** — Matetski, Quastel, Remenik construct the **KPZ fixed point** as a Markov process (exact transition probabilities via TASEP).
- **2018–22** — Dauvergne, Ortmann, Virág construct the **directed landscape**, the full scaling limit and conjectured universal object.
- **2023** — Quastel–Sarkar and Virág prove **convergence to the KPZ fixed point** for broad classes of models (e.g. ASEP, general exclusion), the strongest universality results to date — yet still confined to integrable or near-integrable models.

The frontier remains the same gap the physicists left in 1986: universality is rigorously established only where exact solvability or special algebraic structure is available. A non-integrable, non-perturbative proof — convergence for genuinely generic growth models — is open.
