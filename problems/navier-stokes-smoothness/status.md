# Status & Frontier — Navier–Stokes Existence and Smoothness

_Where the problem stands and what a resolution would require._

**Status: open.** No proof of global existence and smoothness for 3D incompressible Navier–Stokes is known, and no finite-time singularity for the viscous equations has been demonstrated. The problem remains an unclaimed Clay Millennium Prize.

## What is known (unconditional)

- **Global weak solutions exist** for any finite-energy divergence-free data (Leray 1934, Hopf 1951). They satisfy the energy inequality but are not known to be unique or smooth.
- **2D is fully solved:** in two dimensions solutions are globally smooth and unique (Ladyzhenskaya and others). The 2D energy is critical, not supercritical, which is exactly why the argument closes there and not in 3D.
- **Local-in-time smoothness:** smooth data yield a unique smooth solution on a (possibly short) time interval; smoothness persists as long as critical norms (e.g. $\|u\|_{L^\infty_t L^3_x}$ or $\int\|\omega\|_{L^\infty}dt$) stay finite.
- **Partial regularity (CKN 1982):** for suitable weak solutions the singular set has parabolic Hausdorff dimension at most $1$ — the strongest unconditional control to date.
- **Small-data global existence** in scale-critical spaces up to $BMO^{-1}$ (Koch–Tataru 2001), the optimal known threshold; ill-posedness sets in just beyond, in $\dot B^{-1}_{\infty,\infty}$ (Bourgain–Pavlović 2008).

## Strongest conditional results

- **Prodi–Serrin–Ladyzhenskaya criteria:** $u\in L^p_t L^q_x$ with $\tfrac2p+\tfrac3q\le 1$ implies smoothness; the critical endpoint $L^\infty_t L^3_x$ is included (Escauriaza–Seregin–Šverák 2001).
- **Geometric criteria** (Constantin–Fefferman): local coherence of the vorticity direction depletes the nonlinearity and prevents blow-up.

Each conditional theorem assumes control at the *critical* scaling — precisely the quantity the supercritical energy cannot supply unconditionally. This gap is the heart of the problem.

## What a full resolution requires

A positive resolution must produce an a priori bound, valid for arbitrarily large smooth data, that controls the solution at or below the critical scaling for all time — something strictly stronger than the supercritical energy estimate. **Tao's 2014 averaged-equation blow-up** proves that no argument using only the energy inequality and the scaling symmetry can work, since such an argument would also (falsely) regularize a system known to blow up. Any proof must therefore exploit the specific quadratic, divergence-free structure of the true nonlinearity. A negative resolution must exhibit smooth data whose Leray–Hopf solution forms a genuine finite-time singularity — for the *viscous* equation, not Euler or an averaged model.

## Plausible routes

- Sharpening partial regularity below dimension $1$, toward an empty singular set.
- New critical-scale a priori estimates beyond $BMO^{-1}$ exploiting incompressibility geometrically.
- Rigorous blow-up via self-similar or near-self-similar profiles, extending the Euler blow-up program (Elgindi 2021; Hou–Luo numerics) to the viscous setting — though viscosity is widely expected to defeat known Euler mechanisms.
- Convex-integration insights to characterize, and then exclude, pathological behavior within the Leray–Hopf class.

The honest consensus is that resolution likely awaits a genuinely new analytic idea adequate to the supercritical barrier; current methods are understood to be insufficient.

## Related problems

- [Yang–Mills Existence and Mass Gap](../yang-mills-mass-gap/README.md) — sibling Millennium Prize PDE/analysis problem.
- [Hilbert's Sixteenth Problem](../hilbert-sixteenth-problem/README.md) — dynamics and qualitative behavior of solutions to differential equations.
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — another Millennium Prize Problem of comparable centrality.
- [Kakeya Conjecture](../kakeya-conjecture/README.md) — harmonic-analytic obstructions closely tied to the techniques used here.
