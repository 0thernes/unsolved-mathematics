# Approaches — The Palis Conjecture (Finitude / Density of Attractors)

_Major strategies, partial results, and barriers._

The conjecture bundles three assertions — **finitude** of attractors, **metric covering** (basins of full Lebesgue measure), and **statistical stability** (robust SRB measures). Attacks proceed by isolating one piece, by lowering the regularity or dimension, or by replacing topological genericity with measure-theoretic typicality. No approach has reached the full statement in dimension $\geq 2$.

## Density of hyperbolicity in dimension one

**Core idea.** The simplest incarnation of the conjecture is Smale's question whether hyperbolic maps are dense among one-dimensional dynamics. If so, the typical interval/circle map has finitely many hyperbolic periodic attractors whose basins fill almost all of phase space.

**Best result.** Kozlovski, Shen, and van Strien (2007, *Annals of Mathematics*) proved **density of hyperbolicity for $C^k$ maps of the interval and circle**, completing the real one-dimensional case (building on Lyubich, Graczyk–Świątek, de Melo–van Strien, and the rigidity/complex-bounds machinery). This is the strongest unconditional confirmation of the Palis picture anywhere.

**Barrier.** The proof rests on one-dimensional tools — Schwarzian derivative, complex bounds, quasiconformal rigidity, real bounds — that have **no higher-dimensional analogue**. The renormalization rigidity that makes dimension one work is exactly what fails when stable/unstable directions coexist.

## $C^1$-generic dichotomies (Mañé–Pujals–Sambarino–Crovisier)

**Core idea.** Work in the $C^1$ topology, where Pugh's closing lemma, Hayashi's connecting lemma, and Mañé's ergodic-closing techniques give powerful perturbation control. Aim for a dichotomy: a generic system is either (essentially) hyperbolic or can be $C^1$-approximated by one with a homoclinic tangency or heterodimensional cycle.

**Best result.** Pujals–Sambarino proved that $C^1$ surface diffeomorphisms away from tangencies are essentially hyperbolic; Crovisier–Pujals (2018, *Inventiones*) established **"essential hyperbolicity"** results and the dichotomy in higher dimension under the absence of homoclinic bifurcations, via dominated splittings. Bonatti–Crovisier showed $C^1$-generic transitivity/decomposition phenomena.

**Barrier.** Results are confined to the $C^1$ topology, where perturbation lemmas are available but **SRB measures and metric (Lebesgue) statements are largely out of reach** — $C^1$ generic systems can lack SRB measures entirely, and the closing-lemma toolkit famously does not upgrade to $C^2$. The gap between "$C^1$ dense" and "full Lebesgue measure of parameters" is the heart of the difficulty.

## Dominated splittings and partial hyperbolicity (Bonatti–Díaz–Viana)

**Core idea.** Replace uniform hyperbolicity by weaker invariant structures — dominated splitting $TM = E \oplus F$, partial hyperbolicity with a neutral center — that survive perturbation and are conjectured to be the generic substitute for hyperbolicity. Build SRB measures for these "robustly non-hyperbolic" systems.

**Best result.** The Bonatti–Díaz–Viana monograph *Dynamics Beyond Uniform Hyperbolicity* (2005) systematizes robust transitivity and constructs SRB/physical measures for many partially hyperbolic classes (mostly contracting/expanding central direction). Alves–Bonatti–Viana gave SRB existence for non-uniformly expanding maps.

**Barrier.** SRB existence and finitude are proven only under structural hypotheses (mostly-contracting center, etc.). For a **neutral / one-dimensional center with mixed behavior**, finitude of attractors and existence of SRB measures can fail or remain unknown; the general non-uniformly hyperbolic case has no finitude theorem.

## SRB / physical-measure theory (Sinai–Ruelle–Bowen, Young, Benedicks–Carleson)

**Core idea.** Directly construct the physical measures the conjecture demands. For specific families (Hénon-like, Lorenz, unimodal), prove abundance of parameters with a finite set of SRB measures — a measure-theoretic, not topological, statement, exactly matching Palis's "almost every parameter."

**Best result.** Benedicks–Carleson (1991) and Mora–Viana established a **positive-measure set of Hénon parameters with a strange attractor carrying an SRB measure**; Young's tower/decay-of-correlations machinery makes the statistics statistically stable in many models. Tucker's rigorous solution of the Lorenz attractor gives a robust SRB attractor.

**Barrier.** These are **parametric, family-by-family** results requiring delicate parameter exclusion; they do not assemble into a global statement over all systems. Statistical stability under perturbation of the parameter is proven only in restricted regimes.

## Negative / obstruction results

The conjecture must coexist with genuine wildness. **Newhouse (1974)** gives open sets with infinitely many sinks — so *finitude can only hold off a measure-zero set*, never on a residual set. **Bonatti–Díaz** produced robustly non-hyperbolic (heterodimensional) systems. **Berger (2016)** proved **robust universality / Newhouse phenomena are themselves abundant in higher regularity** (open sets where infinitely many attractors persist), and constructed examples casting doubt on naive finitude in the $C^r$, $r \geq 2$, setting. These results delimit the conjecture: they show that any proof must exploit the *measure-zero* nature of the bad set and cannot proceed by topological density alone, and they leave open whether even the measure-theoretic statement survives in high regularity.
