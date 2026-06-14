# Approaches — Navier–Stokes Existence and Smoothness

_Major strategies, partial results, and barriers._

The central obstruction shadows every approach: the 3D problem is **energy-supercritical**. Under the scaling $u\mapsto u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$, the conserved energy $\|u(t)\|_{L^2}^2$ scales by $\lambda^{-1}$, so as one zooms toward a putative singularity the only globally controlled quantity becomes weaker, not stronger. Every coercive a priori bound currently known is supercritical or at best critical-borderline; none dominates the nonlinearity at small scales. Most strategies below succeed in two dimensions (critical) and stall in three for exactly this reason.

## Weak solutions and partial regularity

Leray's 1934 construction yields global finite-energy weak solutions that satisfy the energy inequality (Leray–Hopf solutions); existence is never the difficulty — uniqueness and smoothness are. The deepest result on this line is the **Caffarelli–Kohn–Nirenberg theorem** (1982): for a suitable weak solution, the singular set $\Sigma$ has one-dimensional parabolic Hausdorff measure zero, hence parabolic Hausdorff dimension $\le 1$. This is the strongest *unconditional* regularity statement known. Its barrier is structural: it bounds the *size* of a singular set but cannot exclude it, and improving the dimension below $1$ would require controlling a supercritical quantity the method does not provide.

## Conditional regularity (Serrin/Prodi–Serrin and endpoint criteria)

A vast literature gives sufficient conditions for smoothness: if a Leray–Hopf solution lies in $L^p_t L^q_x$ with $\tfrac{2}{p}+\tfrac{3}{q}\le 1$ (the Prodi–Serrin–Ladyzhenskaya range), it is smooth. The critical endpoint $u\in L^\infty_t L^3_x$ was settled by **Escauriaza–Seregin–Šverák** (2001). Vorticity criteria (Beale–Kato–Majda style: control of $\int \|\omega\|_{L^\infty}\,dt$) and one-component or geometric criteria (Constantin–Fefferman alignment of vorticity direction) refine this. The barrier: every such criterion presupposes control at the *critical* scaling, which the supercritical energy cannot supply unconditionally. They convert the problem rather than solve it.

## Mild solutions and harmonic analysis (Kato/Koch–Tataru)

Treating the equation via the Duhamel/heat-semigroup formulation gives unique local strong ("mild") solutions in critical spaces. Kato–Fujita (1962) worked in $\dot H^{1/2}$; the apex is **Koch–Tataru** (2001), global well-posedness for small data in $BMO^{-1}$, the largest scale-invariant space in which the problem is known to be well-posed. Barriers: results are small-data or local-in-time; and **Bourgain–Pavlović** (2008) showed norm inflation/ill-posedness in $\dot B^{-1}_{\infty,\infty}$, marking the outer edge of this method. Largeness of data is the wall.

## Geometric / Lagrangian and conserved-quantity methods

Constantin–Fefferman, Constantin (active scalar/2D SQG analogies), and the helicity/vorticity-stretching viewpoint seek extra geometric coercivity — e.g. depletion of nonlinearity when vortex lines are locally coherent. These yield genuine conditional theorems but no global control, because vortex stretching $\omega\cdot\nabla u$ is precisely the supercritical term.

## Numerical search for blow-up

Large-scale computation (Hou–Luo found apparent finite-time blow-up for the *axisymmetric Euler* equations near a boundary in 2014; many Navier–Stokes searches by Kerr, Grauer, and others) probes whether singularities form. For Navier–Stokes itself no computation has produced convincing self-consistent blow-up; viscosity appears to regularize. This is suggestive, not decisive: numerics cannot certify global smoothness and resolution always runs out near a putative singularity.

## Convex integration and non-uniqueness (negative results)

The most consequential recent development is a *barrier*, not a proof of regularity. Adapting Nash–Kuiper and the **De Lellis–Székelyhidi** program for Euler (which culminated in the resolution of the Onsager conjecture by Isett, 2018, and Buckmaster–De Lellis–Székelyhidi–Vicol, 2019), **Buckmaster–Vicol** (2019) proved that weak solutions of 3D Navier–Stokes with bounded kinetic energy are **non-unique**. This shows the weak/distributional framework alone cannot characterize physical solutions: any successful theory must exploit the energy inequality and the Leray class specifically, ruling out purely soft existence arguments. Convex integration thus delimits what cannot work.

## Model problems and the supercriticality barrier

A defining negative result is **Tao's averaged Navier–Stokes** (2014): Tao engineered a system with the same energy identity and scaling as 3D Navier–Stokes but with the nonlinearity replaced by an averaged variant, and proved it blows up in finite time. The lesson is sharp: no argument relying *only* on the energy inequality and the scaling structure can prove global regularity, since such an argument would falsely apply to Tao's blowing-up surrogate. Any resolution must use finer structure of the true quadratic nonlinearity than energy-plus-scaling alone — this is the cleanest articulation of why the problem is hard.
