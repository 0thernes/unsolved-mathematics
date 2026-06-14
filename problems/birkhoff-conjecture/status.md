# Status & Frontier — The Birkhoff Conjecture (Integrable Billiards)

_Where the problem stands and what a resolution would require._

## Current status: open (active progress)

The general Birkhoff conjecture — that the *only* smooth strictly convex billiard tables whose dynamics are integrable are ellipses — remains **unproven**. The metadata status is *active-progress*: there is no accepted full proof, but the last decade produced decisive *local* and *algebraic* rigidity theorems that constrain where a counterexample could possibly live.

## What is known unconditionally

- **Global (total) integrability ⇒ disk.** If the *entire* phase cylinder is foliated by continuous invariant curves, the table is a disk (Bialy, 1993, Hopf-type rigidity). The disk and ellipse are the only confirmed integrable convex tables.
- **Universal near-boundary caustics.** Every smooth strictly convex billiard has a positive-measure Cantor family of caustics near the boundary (Lazutkin, 1973). Integrability is the statement that this family is *complete* (gap-free).
- **Polynomial integrals ⇒ conics.** Convex billiards admitting an integral polynomial in momenta are conics (Bialy–Mironov program). This settles the *algebraic* Birkhoff conjecture.

## What is known conditionally / locally

- **Small-eccentricity rational integrability.** A rationally integrable small smooth perturbation of an ellipse of small eccentricity is an ellipse — Avila, De Simoi, Kaloshin, *Annals of Mathematics* (2018); arXiv:1412.2853.
- **Local Birkhoff rigidity near generic ellipses.** An integrable (Birkhoff–Poritsky) deformation of a generic ellipse of any eccentricity is an ellipse — Kaloshin, Sorrentino, *Annals of Mathematics* (2018); arXiv:1612.09194.
- **Toward arbitrary eccentricity.** Extensions (e.g., Koval, 2023, arXiv:2306.04143) push rational-integrability rigidity to ellipses of arbitrary eccentricity, and Bialy–Mironov address the centrally symmetric Birkhoff–Poritsky case (preprints, ~2021).

All of these are **local**: they assume proximity to an ellipse (or a polynomial/algebraic integral, or central symmetry).

## What a full resolution requires

1. **Remove the nearness hypothesis.** Pass from "integrable deformations *of an ellipse*" to "*any* integrable convex table," with no perturbative assumption — the central gap.
2. **Bridge from local to global / from polynomial to analytic.** Either show every integrable billiard admits a polynomial (or algebraic) integral, reducing to Bialy–Mironov, or develop a non-perturbative caustic-foliation rigidity that does not start from a conic.
3. **Close the Aubry–Mather gaps.** Prove that a complete caustic foliation accumulating on the boundary forces global confocal structure, controlling the instability regions where Mather theory destroys invariant curves.
4. **Weaken regularity.** Most theorems require $C^\infty$ or analytic boundaries; the natural conjecture is robust and should hold under finite smoothness.

## Plausible routes

The deformation/spectral-rigidity program (Kaloshin–Sorrentino–De Simoi) is the most likely to extend the local results outward, possibly merging with inverse-spectral ("hearing the shape") techniques. The Bialy–Mironov algebraic line is the most likely to deliver clean global statements under structural hypotheses (central symmetry, polynomial integrals). A genuine resolution probably requires a new idea linking these two — a non-perturbative mechanism forcing algebraicity of integrable caustics.

## Related problems

- [Hilbert's Sixteenth Problem](../hilbert-sixteenth-problem/README.md) — rigidity and finiteness in planar dynamical/algebraic systems.
- [Weinstein Conjecture](../weinstein-conjecture/README.md) — periodic orbits and Hamiltonian/Reeb dynamics, the variational backdrop of billiards.
- [Mandelbrot Set Local Connectivity](../mandelbrot-locally-connected/README.md) — another rigidity-flavored conjecture at the order/chaos boundary in dynamics.
- [Invariant Subspace Problem](../invariant-subspace-problem/README.md) — a structural "the only objects are the obvious ones" rigidity question in a different setting.
