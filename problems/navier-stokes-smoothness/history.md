# History — Navier–Stokes Existence and Smoothness

_Origin, formulation, and timeline._

The Navier–Stokes equations describe the motion of a viscous, incompressible Newtonian fluid. They emerged from a century-long effort to add internal friction to Euler's frictionless equations of 1755. Claude-Louis Navier derived them in 1822 from a molecular-attraction model; the derivation was physically idiosyncratic but produced the correct viscous term. Over the following two decades Siméon Denis Poisson (1831), Adhémar de Saint-Venant (1843), and finally George Gabriel Stokes (1845) re-derived the same system from continuum-mechanical principles, placing it on the rigorous footing it retains today. In modern form the unknowns are a velocity field $u(x,t)$ and a pressure $p(x,t)$ on $\mathbb{R}^3$ (or $\mathbb{T}^3$) satisfying

$$\partial_t u + (u\cdot\nabla)u = -\nabla p + \nu\,\Delta u + f, \qquad \nabla\cdot u = 0,$$

with given divergence-free initial data $u_0$. The nonlinear transport term $(u\cdot\nabla)u$ and the smoothing Laplacian $\nu\Delta u$ compete; whether smoothing always wins in three dimensions is the open question.

The mathematical problem — as opposed to the physical equations — was crystallized by Jean Leray. In his landmark 1934 paper Leray constructed global **weak** (finite-energy) solutions for any finite-energy initial data, proved they exist for all time, but could not show they remain smooth or unique. He introduced the notion of a "turbulent solution" and the possibility of a finite-time singularity, framing the regularity question that still stands. Eberhard Hopf extended weak existence to bounded domains in 1951; these are now called Leray–Hopf solutions. The complementary local theory of unique smooth solutions was supplied by Kiyosi Itô, Hopf, Kato–Fujita (1962), and others, who showed smooth solutions exist for a short time and remain smooth as long as suitable norms stay finite.

The defining structural results came in the 1960s. Olga Ladyzhenskaya proved global regularity and uniqueness in **two** dimensions, definitively settling the 2D case. James Serrin (1962) and others established conditional regularity criteria. In 1982 Luis Caffarelli, Robert Kohn, and Louis Nirenberg proved their celebrated partial-regularity theorem: the singular set of a suitable weak solution has parabolic Hausdorff dimension at most one — the strongest unconditional result to date.

In May 2000 the Clay Mathematics Institute named the global existence and smoothness of 3D Navier–Stokes solutions one of seven Millennium Prize Problems, with a \$1,000,000 award. Charles Fefferman wrote the official problem statement, fixing the precise conjectures (existence/smoothness on $\mathbb{R}^3$ and $\mathbb{T}^3$, plus breakdown variants) that define the prize.

### Timeline

- **1755** — Euler publishes the equations for inviscid (frictionless) fluid flow.
- **1822** — Claude-Louis Navier introduces viscous terms via a molecular model.
- **1845** — George Gabriel Stokes gives the modern continuum derivation; the system acquires its name.
- **1934** — Jean Leray constructs global weak solutions in $\mathbb{R}^3$ and poses the regularity/uniqueness problem.
- **1951** — Eberhard Hopf proves weak existence on bounded domains (Leray–Hopf solutions).
- **1962** — Kato–Fujita establish local well-posedness in $H^s$; Serrin proves conditional regularity criteria.
- **1960s** — Olga Ladyzhenskaya proves global regularity and uniqueness in two dimensions.
- **1982** — Caffarelli–Kohn–Nirenberg prove the partial-regularity theorem (singular set has dimension $\le 1$).
- **2000** — Clay Mathematics Institute designates 3D smoothness a Millennium Prize Problem; Fefferman writes the official statement.
- **2001** — Escauriaza–Seregin–Šverák prove the endpoint $L^3_x$ regularity criterion.
- **2014** — Terence Tao constructs blow-up for an averaged Navier–Stokes system, formalizing the "supercriticality barrier".
- **2019** — Buckmaster–Vicol prove non-uniqueness of weak solutions below the Leray class via convex integration.
- **2021–2022** — Convex-integration methods sharpen near-Onsager non-uniqueness; the regularity problem for genuine Leray–Hopf solutions remains open.
