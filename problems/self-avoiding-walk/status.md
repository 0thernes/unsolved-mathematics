# Status & Frontier — Self-Avoiding Walk (Scaling & Connective Constant)

_Where the problem stands and what a resolution would require._

**Overall status: active-progress.** Existence of the connective constant $\mu = \lim_n c_n^{1/n}$ is fully rigorous (Hammersley, 1957), but its *value* is known exactly on essentially no standard lattice except the honeycomb, and the conjectured scaling exponents in $d=2$ and $d=3$ remain unproven. There is no claimed resolution and no disputed proof; the problem is genuinely open.

**What is known unconditionally.**
- $\mu$ exists for every $\mathbb{Z}^d$ and for periodic lattices; submultiplicativity gives $c_n \ge \mu^n$ and Hammersley–Welsh gives $c_n \le \mu^n e^{O(\sqrt n)}$ in general (improved to $e^{o(\sqrt n)}$ in $d\ge3$).
- **High dimensions ($d\ge5$):** Hara–Slade's lace expansion proves $\nu = 1/2$, $\gamma = 1$, $c_n\sim A\mu^n$, and convergence to Brownian motion. This is the only dimension range where the exponents are theorems.
- **Honeycomb lattice:** Duminil-Copin–Smirnov (2010; *Ann. of Math.*, 2012; arXiv:1007.0575) prove $\mu = \sqrt{2+\sqrt2}$ exactly — the flagship exact rigorous lattice result.
- **Critical dimension $d=4$ (weakly SAW only):** Bauerschmidt–Brydges–Slade rigorously establish the conjectured logarithmic corrections for the continuous-time weakly self-avoiding (Domb–Joyce) model.
- Kesten's pattern theorem and $c_{n+2}/c_n\to\mu^2$; continuity and monotonicity properties of $\mu$.

**What is known only conditionally / heuristically.**
- **2D exponents** $\nu=3/4$, $\gamma=43/32$: predicted by Nienhuis (Coulomb gas) and reproduced by $\mathrm{SLE}_{8/3}$, but proven only *conditional* on existence of a conformally invariant scaling limit (Lawler–Schramm–Werner, 2002/2004).
- **3D exponent** $\nu\approx 0.58759700$: known to high numerical precision (Clisby pivot Monte Carlo; conformal bootstrap) but with no rigorous proof and no conjectured closed form.

**What a full resolution requires.**
1. **Two dimensions:** prove that the SAW (e.g. the lace-walk or the uniform measure on $n$-step walks, suitably rescaled) has a scaling limit, and that this limit is conformally invariant — hence $\mathrm{SLE}_{8/3}$. This would yield $\nu=3/4$, $\gamma=43/32$ and the exact $\mathbb{Z}^2$ exponents. The missing ingredient is a discrete observable provably converging to a conformally covariant function, analogous to Smirnov's percolation/Ising observables.
2. **Three dimensions:** establish *any* rigorous control of the exponents below the critical dimension for the strict model — currently entirely out of reach.
3. **Exact $\mu$ on $\mathbb{Z}^2,\mathbb{Z}^3$:** likely transcendental; not expected to have a closed form, so the realistic target is rigorous scaling rather than an exact constant.

**Plausible routes.** (a) Extend parafermionic/discrete-holomorphic methods from the honeycomb to other lattices and to a full conformally covariant limit. (b) Build a convergent renormalization-group analysis below $d=4$, beginning with the weakly self-avoiding model. (c) Prove tightness and convergence of the SAW curve to $\mathrm{SLE}_{8/3}$ directly, closing the LSW conditional. None is close to completion; the honeycomb result shows method (a) is real but stubbornly geometry-specific.

## Related problems

- [KPZ universality](../kpz-universality/) — neighboring scaling-limit / universality program in 2D statistical mechanics.
- [Kakeya conjecture](../kakeya-conjecture/) — another problem where exact exponents and geometric measure govern the answer.
- [Yang–Mills mass gap](../yang-mills-mass-gap/) — shares the rigorous-renormalization-group and continuum-limit challenge.
- [Hadwiger–Nelson problem](../hadwiger-nelson-problem/) — combinatorial-geometric constant determination on lattices/graphs.
