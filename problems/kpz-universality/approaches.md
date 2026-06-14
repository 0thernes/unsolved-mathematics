# Approaches — The KPZ Universality Conjecture

_Major strategies, partial results, and barriers._

## Exact solvability / integrable probability

**Core idea.** A privileged subfamily of KPZ-class models carries hidden algebraic structure — determinantal/Pfaffian point processes, Bethe ansatz, the Robinson–Schensted–Knuth (RSK) correspondence, Macdonald and Schur measures, $q$-deformations — that yields *exact* formulas for one-point distributions and correlation kernels. One extracts the $t^{1/3}$ scaling and Tracy–Widom limit by steepest-descent asymptotics on these formulas.

**Best results.** This is the source of nearly every rigorous theorem in the field: Baik–Deift–Johansson (1999) for longest increasing subsequences; Johansson (2000) for exponential/geometric last-passage percolation; Prähofer–Spohn (2000) for the PNG droplet and the Airy$_2$ process; Tracy–Widom (2009) for ASEP; Amir–Corwin–Quastel (2011) for the KPZ equation itself; Borodin–Corwin's Macdonald processes (2014); and convergence to the KPZ fixed point (Matetski–Quastel–Remenik 2021; Quastel–Sarkar 2023; Virág 2020+).

**Barrier.** The method is fundamentally non-robust: it requires the model to be *exactly solvable*. Perturbing the jump rates, the noise distribution, or the geometry generically destroys the algebraic identities. Integrability is a measure-zero condition in model space, so this route, by design, cannot reach genuine universality for arbitrary models.

## Stochastic-PDE / pathwise solution theory

**Core idea.** Make sense of the KPZ equation directly despite its analytic ill-posedness (the $(\partial_x h)^2$ term acting on a distribution-valued $h$). **Regularity structures** (Hairer 2013) and **paracontrolled distributions** (Gubinelli–Imkeller–Perkowski 2015) provide renormalized, locally subcritical solution theories; energy-solution and martingale-problem approaches (Gonçalves–Jara 2014; Gubinelli–Perkowski 2018) characterize the equation as a scaling limit of conservative particle systems.

**Best results.** Hairer's theory gives a robust well-posedness and a meaning to "the" KPZ equation; the energy-solution framework proves that several non-integrable microscopic dynamics (e.g. certain weakly asymmetric exclusion and zero-range processes) converge to the KPZ equation in the **weak-asymmetry / crossover** regime. This is the closest thing to a universality engine that is *not* tied to exact solvability.

**Barrier.** These results live at the level of the *KPZ equation* (the crossover / Edwards–Wilkinson-to-KPZ scaling), not the *KPZ fixed point* (the strong-asymmetry $t^{1/3}$ regime with Tracy–Widom statistics). The equation is subcritical; the fixed point is critical, beyond the reach of current renormalization technology. Passing from equation to fixed point still requires integrable input.

## Probabilistic / geometric and coupling methods

**Core idea.** Exploit monotonicity, attractiveness, and stationary measures of the underlying particle systems to control fluctuations without exact formulas — the "Cator–Groeneboom / Balázs–Cator–Seppäläinen" busy-period and competition-interface arguments, and the geometry of geodesics in last-passage percolation.

**Best results.** Stationary-model and coupling techniques give the correct **fluctuation exponents** $1/3$ and $2/3$ (variance bounds of the right order) for some models lacking full solvability, and a rich theory of semi-infinite geodesics, Busemann functions, and coalescence in the directed landscape.

**Barrier.** These methods reliably deliver *exponents* and qualitative geodesic structure but typically not the *exact limiting distribution*. Upgrading order-of-magnitude variance control to a Tracy–Widom limit law has resisted purely probabilistic argument outside the integrable cases.

## Renormalization group (physics) and mode-coupling

**Core idea.** The original dynamic-RG of Kardar–Parisi–Zhang and later mode-coupling / functional-RG schemes compute exponents and scaling functions perturbatively, and predict universality directly from symmetry and the RG flow.

**Best results.** Correct $1+1$ exponents, accurate numerical scaling functions, and the celebrated **nonlinear fluctuating hydrodynamics** program (Spohn) that extends KPZ predictions to coupled conservation laws and anomalous transport. Conjecturally explains why the class is so wide.

**Barrier.** Non-rigorous. The one-loop result is *exact* in $1+1$ for accidental reasons but the RG fixed point itself has never been constructed rigorously; in higher dimensions even the exponents are uncontrolled (the existence/location of the roughening transition for $d\geq 2$ remains open). No RG argument has been turned into a proof of the distributional universality.

## Universality-transfer / comparison arguments

**Core idea.** Prove the limit for one solvable model, then *transfer* it to nearby non-solvable models by coupling, slow-bond / perturbation estimates, or invariance principles — analogous to the Lindeberg method for the CLT.

**Best results.** Local-statistics universality has been pushed for *certain* perturbations (e.g. corner-growth with general weights satisfying integrability-adjacent conditions; some results on last-passage with non-exponential weights via comparison). Time-correlation and multi-point universality have been established within solvable families.

**Barrier.** No general "Lindeberg principle for KPZ" exists. Transfer arguments have, so far, only crossed a thin neighborhood of the integrable locus; a genuinely model-independent comparison theorem — the analogue of the central limit theorem's universality — is the missing keystone.
