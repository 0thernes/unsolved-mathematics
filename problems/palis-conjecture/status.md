# Status & Frontier — The Palis Conjecture (Finitude / Density of Attractors)

_Where the problem stands and what a resolution would require._

**Status: open.** No proof exists in any dimension $\geq 2$, and the full conjecture (finitude of attractors, basins of full Lebesgue measure, statistical stability of physical measures, for almost every system in generic families) is unproven even for diffeomorphisms of surfaces. The metadata status is "open," and nothing below should be read as a resolution.

## What is known (unconditional)

- **Dimension one is settled in the relevant sense.** Kozlovski–Shen–van Strien (2007) proved **density of hyperbolicity** for $C^k$ interval and circle maps; combined with Lyubich's "regular or stochastic" theorem (2003) and Avila–Lyubich–de Melo for analytic unimodal families, almost every map in the quadratic family is either regular (a single hyperbolic attracting cycle) or stochastic (an absolutely continuous SRB measure). The Palis picture holds completely here.
- **Partial structures in higher dimension.** SRB measures and finitude exist for broad classes of **partially hyperbolic** systems with mostly-contracting or mostly-expanding center (Bonatti–Viana; Alves–Bonatti–Viana). Positive-Lebesgue-measure sets of Hénon parameters carry SRB attractors (Benedicks–Carleson; Mora–Viana). Tucker (2002) rigorously established the Lorenz attractor with its physical measure.
- **$C^1$-generic dichotomies.** Pujals–Sambarino and Crovisier–Pujals show that, in the $C^1$ topology, systems away from homoclinic tangencies/heterodimensional cycles are essentially hyperbolic — confirming the *structural* sub-conjecture (density of hyperbolicity or homoclinic bifurcations) in significant generality.

## What is known (conditional / constrained)

The above $C^1$ results do not yield the **metric and statistical** clauses, because $C^1$-generic systems may possess no SRB measure at all. Finitude in higher dimension is known only under structural domination hypotheses. The honest gap: there is no general theorem that a typical $C^2$ (or higher) surface diffeomorphism has finitely many attractors.

## Obstructions

- **Newhouse phenomenon:** open sets with infinitely many sinks force any finitude statement to allow a measure-zero exceptional set — the conjecture can only be metric, never topological.
- **Berger's robust universality (2016):** open sets in $C^r$, $r \ge 2$, with persistent Newhouse phenomena and unbounded attractor complexity, placing the high-regularity finitude clause under genuine tension and possibly demanding refinement of the precise hypotheses.

## What a full resolution requires

A proof must (i) construct SRB/physical measures for the generic non-uniformly hyperbolic system — a problem with no current general technique; (ii) prove finitude of attractors off a Lebesgue-null parameter set, reconciling this with Newhouse/Berger abundance; and (iii) establish statistical stability of those measures under perturbation. Plausible routes: extend the $C^1$-generic dichotomy framework with new tools to control physical measures; develop a higher-dimensional substitute for one-dimensional renormalization rigidity; or prove a sharp finitude theorem inside the partially hyperbolic / dominated-splitting category and then show such structures are generic. Most experts regard the conjecture as decades away, with the high-regularity universality results a serious caveat on its scope.

## Related problems

- [Hilbert's Sixteenth Problem](../hilbert-sixteenth-problem/) — finiteness of limit cycles, the planar-flow analogue of finitude of attractors.
- [Arnold Diffusion](../arnold-diffusion/) — instability and transport in near-integrable Hamiltonian dynamics, the conservative counterpart to dissipative attractor theory.
- [Collatz Conjecture](../collatz-conjecture/) — a discrete dynamical system whose orbit structure resists the same kind of global control.
- [Birkhoff Conjecture](../birkhoff-conjecture/) — rigidity of integrable billiards, a neighboring rigidity question in smooth dynamics.
- [Weinstein Conjecture](../weinstein-conjecture/) — existence of periodic orbits, another structural question about the orbit content of dynamical systems.
