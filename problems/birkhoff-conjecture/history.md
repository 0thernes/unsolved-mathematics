# History — The Birkhoff Conjecture (Integrable Billiards)

_Origin, formulation, and timeline._

## Origin and setting

A **mathematical billiard** in a smooth, strictly convex planar domain $\Omega$ models a point mass moving in straight lines and reflecting off $\partial\Omega$ with equal angles of incidence and reflection. The dynamics define the *billiard map* on the phase cylinder of oriented chords, parametrized by arclength $s$ along the boundary and the angle $\varphi\in(0,\pi)$ of reflection. This map is an area-preserving twist map, and its study lies at the crossroads of dynamical systems, the calculus of variations, and integrable systems.

George David Birkhoff introduced convex billiards as a tractable model embodying the qualitative features of Hamiltonian dynamics. In his 1927 monograph *Dynamical Systems* and surrounding work, Birkhoff observed that the billiard inside an **ellipse** is *integrable*: the phase space is foliated by invariant curves, and every trajectory has a *caustic* — a confocal ellipse or hyperbola to which it remains tangent. The conserved quantity is the product of angular momenta about the two foci (the "Joachimsthal integral"). The conjecture asks whether ellipses are the *only* such tables.

## Precise formulation and reformulations

The statement is sensitive to what "integrable" means, and the modern literature distinguishes several inequivalent versions.

- **Global integrability.** The billiard map admits a foliation of an open neighborhood of the boundary (in the phase cylinder) by continuous invariant curves, equivalently the table possesses a continuous family of caustics. The conjecture: such $\Omega$ is an ellipse (a disk being the degenerate case).
- **Local / rational integrability (Birkhoff–Poritsky form).** Following the formulation attributed to Hillel Poritsky (1950) and emphasized by Sergei Tabachnikov, one assumes the existence of an integrable region foliated by invariant curves accumulating on the boundary, with no requirement of integrability far from $\partial\Omega$. This *local* version is the form most modern theorems address.
- **Rational integrability.** A weaker hypothesis requiring only that the invariant curves consisting of $q$-periodic orbits (for all $q\ge 3$) form smooth curves — the version solved for perturbations of ellipses.

Whitney/Bialy-type total-integrability results and the Hopf-rigidity philosophy connect the problem to the absence of conjugate points and to spectral rigidity.

## Timeline

**1927** — G. D. Birkhoff publishes *Dynamical Systems*; convex billiards and their variational (least-action) structure are systematized. The integrability of the ellipse is folklore by this period; the conjecture that ellipses are the only integrable tables is attributed to Birkhoff in this era (sometimes dated to remarks around 1927–1930).

**1950** — Hillel Poritsky, in *The billiard ball problem on a table with a convex boundary*, gives a careful treatment and an early local rigidity argument; the "Birkhoff–Poritsky" local formulation traces here.

**1973** — H. Lazutkin proves existence of a positive-measure Cantor family of caustics (invariant curves) near the boundary of any smooth strictly convex billiard — a KAM-type result showing near-boundary "near-integrability" is generic, sharpening what genuine integrability must mean.

**1993** — Misha Bialy proves a global Hopf-type rigidity theorem: if the entire phase space (cylinder) is foliated by continuous invariant curves, the table is a disk. This settles the *strongest* global version.

**1995–1996** — Sergei Bolotin, and work in the geodesic-flow analogue, develop polynomial-integrability rigidity.

**2010s** — Vadim Kaloshin, Alfonso Sorrentino, and collaborators reframe the local conjecture via deformation/spectral methods.

**2017** — Avila, De Simoi, and Kaloshin prove **local rational integrability rigidity**: a small smooth perturbation of an ellipse of small eccentricity that remains rationally integrable must itself be an ellipse (published *Annals of Mathematics*, 2018).

**2018** — Kaloshin and Sorrentino establish **local integrability rigidity** near any ellipse: an integrable (in the Birkhoff sense) deformation of a generic ellipse is an ellipse (*Annals of Mathematics*, 2018).

**2018–2024** — Bialy and Mironov prove the **polynomial Birkhoff conjecture** (integrals polynomial in velocity) and announce progress toward the centrally-symmetric "rational" case via the algebraic/angular-momentum approach.

**Present** — The general conjecture (arbitrary integrable convex tables, not necessarily near an ellipse) remains **open**. The frontier is local rigidity around ellipses of all eccentricities and removing the near-circular smallness hypotheses.
