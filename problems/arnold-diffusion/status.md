# Status & Frontier — Arnold Diffusion (Genericity)

**Overall status: active-progress, open.** Arnold's genericity conjecture — that for $n \ge 3$ degrees of freedom a topologically large set of perturbations of a nondegenerate integrable Hamiltonian admits orbits whose action variables drift by $O(1)$ — is **proven in the lowest nontrivial setting and open in general.**

**What is known (unconditional).**
- *Existence* of diffusion in a priori unstable systems is established rigorously by both geometric (Delshams–de la Llave–Seara scattering map) and variational (Cheng–Yan, Bernard, Treschev) methods, including the large-gap case.
- *Genericity* in the smooth-convex category for **two and a half degrees of freedom** (i.e. $n=2$ plus time, the lowest case where diffusion is possible) is the headline modern result, via the program of Bernard–Kaloshin–Zhang and Kaloshin–Zhang. Kaloshin and Zhang, *Arnold Diffusion for Smooth Convex Systems of Two and a Half Degrees of Freedom* (Mathematical Surveys and Monographs, AMS, 2020), is the consolidated reference; it controls both single- and the difficult double-resonance regions for a generic perturbation.
- *Speed bounds*: under steepness/convexity, Nekhoroshev's theorem makes any diffusion exponentially slow, $|t| \gtrsim \exp(c\,\varepsilon^{-b})$, so the phenomenon is real but extraordinarily slow.
- *Concrete systems*: computer-assisted proofs (Gidea, de la Llave, Capiński, Zgliczyński) establish diffusion in specific models, including the elliptic restricted three-body problem.

**What is known (conditional / partial).**
- Diffusion across and along resonance chains in higher dimension is understood under additional non-degeneracy or transversality hypotheses that are believed generic but not yet proven generic in full.
- Several results hold for *residual* (Baire-generic) sets; whether the diffusing set is *prevalent* (full-measure-like, Kolmogorov-typical) is largely open even in two and a half degrees of freedom.

**What a full resolution requires.**
1. A genericity proof valid for **arbitrary $n \ge 3$**, controlling the entire resonance web including triple and higher crossings, where no clean local reduction is known.
2. A resolution of the **topological-vs-metric** gap: upgrading residual genericity to prevalence / positive measure of diffusing perturbations.
3. Extension to the **analytic category**, where the absence of bump functions and the scarcity of perturbations defeat current smooth-category techniques; this is widely regarded as the deepest obstacle.

**Plausible routes.**
- Scaling the Kaloshin–Zhang normal-form atlas and double-resonance analysis to higher dimension, combined with the scattering-map bookkeeping of the geometric school.
- Stronger weak-KAM / Mather-theory inputs giving hyperbolicity of minimizers along the whole web.
- Quantitative, possibly computer-assisted, control of homoclinic transversality that is uniform over a large family of perturbations.

No announced proof of the full conjecture has passed community refereeing; any future claim — especially in arbitrary dimension or the analytic class — should be treated as needing verification.

## Related problems

- [KAM / Hamiltonian stability lineage — Hilbert's sixteenth problem](../hilbert-sixteenth-problem/) — limit cycles and the qualitative theory of dynamical systems.
- [Birkhoff conjecture](../birkhoff-conjecture/) — integrability and rigidity for billiards, a sibling question on the boundary of integrability.
- [Weinstein conjecture](../weinstein-conjecture/) — periodic orbits in Hamiltonian/contact dynamics.
- [Palis conjecture](../palis-conjecture/) — density/finiteness of dynamical behaviour, a genericity program for general dynamical systems.
- [Mandelbrot set local connectivity](../mandelbrot-locally-connected/) — another deep genericity/structure question in dynamics.
