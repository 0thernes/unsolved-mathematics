# History — Arnold Diffusion (Genericity)

The problem grows out of the central question of Hamiltonian perturbation theory: how stable are the motions of a nearly integrable system? An integrable Hamiltonian system of $n$ degrees of freedom foliates phase space into invariant tori carrying quasi-periodic motion, on which the action variables $I \in \mathbb{R}^n$ are constants. The Kolmogorov–Arnold–Moser (KAM) theorem (Kolmogorov 1954, Arnold 1963, Moser 1962) shows that under a small perturbation $\varepsilon H_1$ a positive-measure Cantor set of these tori survives, so most initial conditions yield actions that stay $O(\varepsilon)$-close to their initial values for all time. The decisive subtlety is dimension. For $n=2$ the surviving 2-tori separate the 3-dimensional energy surface, trapping the actions and forcing *perpetual stability*. For $n \ge 3$ the $n$-tori have codimension $> 1$ and no longer disconnect the energy level; the gaps between KAM tori — the "Arnold web" of resonances — form a connected network along which the actions can in principle drift by an $O(1)$ amount.

Arnold's 1964 note exhibited a concrete two-parameter example,
$$ H = \tfrac{1}{2}(I_1^2 + I_2^2) + \varepsilon(\cos\varphi_1 - 1)\big(1 + \mu(\sin\varphi_2 + \cos t)\big), $$
in which orbits provably travel a fixed distance in $I_2$ regardless of how small $\varepsilon$ is. The mechanism — chains of partially hyperbolic ("whiskered") tori whose stable and unstable manifolds intersect transversally, linked by a "transition chain" — became the template for the entire field. Arnold conjectured that such instability is not special to his example but is the *typical* (generic) behaviour for $n \ge 3$. Turning that conjecture into a theorem about a topologically large or prevalent set of perturbations is the open problem catalogued here.

**Timeline**

- **1954** — Kolmogorov announces the persistence of invariant tori, founding KAM theory.
- **1962–1963** — Moser (smooth twist maps) and Arnold (analytic case) supply full proofs of the KAM theorem.
- **1964** — Arnold publishes "Instability of dynamical systems with several degrees of freedom," giving the first example of action drift and conjecturing its genericity for $n \ge 3$.
- **1971–1977** — Nekhoroshev proves exponentially long-time stability ($|I(t)-I(0)| = O(\varepsilon^a)$ for $|t| \le \exp(c\,\varepsilon^{-b})$) under a steepness condition, bounding the *speed* of any diffusion.
- **1974** — Chirikov's "resonance overlap" criterion gives physicists a heuristic for the onset of large-scale stochasticity and diffusion in action space.
- **1990s** — Mather develops variational (minimal-measure / Aubry–Mather) theory; Bessi, Bernard, and others recast diffusion as a problem of action-minimizing orbits.
- **1996** — Bessi gives a variational reinterpretation of Arnold's original example.
- **2003–2004** — Mather circulates a long manuscript announcing generic diffusion for a priori unstable systems and a program for the nearly integrable case; Delshams–de la Llave–Seara introduce the geometric "scattering map" method and prove diffusion in a model with large gaps.
- **2010** — Cheng–Yan, Bernard, and Treschev give variational and normal-form proofs of diffusion in a priori unstable systems.
- **2015–2017** — Bernard–Kaloshin–Zhang and Kaloshin–Zhang prove diffusion across a single resonance and along resonance chains for *generic* perturbations of nearly integrable systems with two and a half degrees of freedom (three including time), a major step toward Arnold's conjecture.
- **2020** — Kaloshin–Zhang publish the monograph *Arnold Diffusion for Smooth Convex Systems of Two and a Half Degrees of Freedom*, consolidating the generic result in that setting.
- **2020s** — Work continues on higher dimension, on prevalence / Kolmogorov genericity rather than topological genericity, on quantitative diffusion times, and on analytic and a priori chaotic regimes. The conjecture for arbitrary $n \ge 3$ remains open.

The frontier today is the gap between proven generic diffusion in the lowest nontrivial dimension and Arnold's claim of typicality in *all* dimensions and regularity classes.
