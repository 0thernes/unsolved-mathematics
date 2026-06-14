# Approaches — The Birkhoff Conjecture (Integrable Billiards)

_Major strategies, partial results, and barriers._

## Hopf-type rigidity (total integrability)

**Core idea.** Adapt E. Hopf's theorem (a Riemannian metric on the torus without conjugate points is flat) to the billiard return map. If the *entire* phase cylinder is foliated by continuous invariant curves (graphs over the boundary circle), an integral-geometric inequality forces the curvature to be constant.

**Best result.** Misha Bialy (1993) proved: if the phase space of a convex billiard is *globally* foliated by continuous invariant curves, the table is a **disk**. This is a complete, unconditional theorem — but for the strongest, global form of integrability.

**Barrier.** The hypothesis (foliation of the *whole* cylinder, including orbits hitting the boundary nearly tangentially and nearly perpendicularly) is far stronger than the Birkhoff–Poritsky local form. Hopf rigidity says nothing about tables integrable only near the boundary, which is the genuinely hard case.

## Polynomial / algebraic integrability

**Core idea.** Restrict to integrals that are polynomial in the velocity (momentum) components. The ellipse's Joachimsthal integral is quadratic, so one asks: are there integrable billiards with a polynomial first integral of any degree, other than circles and ellipses (and confocal/quadric tables)?

**Best result.** Bialy and Mironov, in a sustained program (2010s–2020s), proved rigidity for polynomial integrals: convex billiards admitting a polynomial-in-momenta integral are conics. Their machinery uses the angular-momentum integral, algebraic geometry of the boundary curve, and analysis of the integral's behavior at the curve. This resolves the **algebraic Birkhoff conjecture** in significant generality and underpins their attack on the centrally symmetric case.

**Barrier.** Genuine integrability need not be polynomial — caustics can be encoded by real-analytic or merely continuous integrals. Reducing general integrability to polynomial integrability is not available, so the algebraic theorems do not imply the analytic conjecture.

## Deformation / spectral (Kaloshin–Sorrentino) approach

**Core idea.** Treat the conjecture as a *rigidity* statement: an integrable deformation of an ellipse must be an ellipse. One linearizes the integrability condition along a one-parameter family of tables, obtaining infinitely many constraints from the preserved $q$-periodic orbits and their action ("Mather $\beta$-function"). The annihilation of all deformations except the trivial conformal-affine ones is shown via Fourier analysis on the boundary and properties of the action spectrum. The technique is intertwined with the *dynamical spectral rigidity* program (whether the length/marked-length spectrum determines the table), via Laplace-spectrum and isospectral deformation arguments.

**Best results.**
- Avila, De Simoi, Kaloshin (2016/2018): a *rationally integrable* small smooth perturbation of an ellipse of **small eccentricity** is an ellipse.
- Kaloshin, Sorrentino (2018): **local Birkhoff rigidity** — an integrable deformation of a generic ellipse (any eccentricity, in the local Birkhoff–Poritsky sense) is an ellipse.
- Subsequent work (Huang, Kaloshin, Sorrentino; Koval) pushes toward removing smallness-of-eccentricity hypotheses and toward rational integrability for all ellipses; Comlan Koval's results (2020s) extend rigidity to ellipses of arbitrary eccentricity under rational-integrability assumptions.

**Barrier.** These are *local* theorems: they require the table to be $C^\infty$- (or analytically) close to an *ellipse*. They give no information about integrable tables far from the family of conics, and the perturbative estimates degenerate as eccentricity grows or as smoothness drops.

## Caustics and the calculus of variations

**Core idea.** Integrability is equivalent to existence of a continuous family of caustics filling a neighborhood of the boundary; caustics correspond to invariant curves of the billiard map and to solutions of an associated string/evolute construction. One studies the geometry and analytic continuation of caustics directly.

**Best result.** Lazutkin (1973) proved that a smooth strictly convex billiard always has a **positive-measure Cantor set** of caustics accumulating on the boundary (a KAM phenomenon), with explicit asymptotics ("Lazutkin coordinates"). This shows near-integrability is universal — and therefore that the conjecture is about the *completeness* of the caustic foliation, not its existence.

**Barrier.** Lazutkin's caustics generically form a Cantor set with gaps (Aubry–Mather sets / Birkhoff instability regions fill the gaps); proving the gaps must vanish for an integrable table is exactly the open difficulty. Mather's destruction-of-invariant-curves results show how delicate full foliation is.

## Length-spectrum / inverse-spectral connections

**Core idea.** The set of perimeters of periodic billiard orbits (the length spectrum) is closely tied to the Laplace eigenvalues (Weyl law, wave trace). Integrability constrains the length spectrum strongly; conversely, spectral rigidity for ellipses feeds back into Birkhoff rigidity.

**Best result.** Hezari–Zelditch and De Simoi–Kaloshin–Wei established dynamical/Laplace spectral rigidity for ellipses of small eccentricity and for centrally symmetric analytic domains, results technically entangled with the integrability rigidity theorems.

**Barrier.** Spectral determination of the domain is itself open in general ("can one hear the shape of a drum" remains negative in some classes), so this route inherits the same locality and symmetry restrictions.

## Net assessment

Every unconditional theorem either assumes *global* integrability (Bialy), a *polynomial* integral (Bialy–Mironov), or *proximity to an ellipse* (Avila–De Simoi–Kaloshin, Kaloshin–Sorrentino, Koval). The conjecture in full — arbitrary smooth strictly convex tables, locally integrable in the Birkhoff–Poritsky sense, with no nearness assumption — remains beyond all current methods.
