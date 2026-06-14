# Status & Frontier — The Volume Conjecture

_Where the problem stands and what a resolution would require._

**Status: active progress; open in general.** The Volume Conjecture is unproven for arbitrary hyperbolic knots, but it is a theorem in several concrete cases and is supported by extensive, high-precision numerical evidence across the knot and $3$-manifold censuses.

## What is known (unconditional)

- **Torus knots.** The conjecture holds: the limit is $0$, matching the vanishing simplicial volume (Kashaev–Tirkkonen). This validates the use of *simplicial* (Gromov) volume in the general statement.
- **Figure-eight knot $4_1$.** Fully proved, with a complete asymptotic expansion, by saddle-point analysis (Ohtsuki, building on Andersen–Hansen). The geometric critical point of the dilogarithm potential is shown to dominate and yields $\mathrm{Vol}(4_1)=2.029883\ldots$.
- **Further small knots.** $5_2$, $6_1$, and several twist / double-twist knots, often with the complexified statement (recovering $\mathrm{Vol}+i\,\mathrm{CS}$).
- **Turaev–Viro / Chen–Yang formulation.** For fundamental shadow links and certain Dehn fillings, the volume-conjecture-type growth is proved (Belletti–Detcherry–Kalfagianni–Yang). This is currently the largest family with a rigorous result, though it concerns links/$3$-manifolds rather than all knots in $S^3$.
- **Structural facts.** The colored Jones is $q$-holonomic (Garoufalidis–Lê), and the geometric saddle value provably equals the complex volume for triangulated complements (Yokota potential functions). Numerical verification is essentially universal within reach of computation.

## What is known (conditional / heuristic)

- Under the AJ conjecture and assumptions on dominance of the geometric flat connection, the generalized (Gukov) Volume Conjecture would follow from character-variety/$A$-polynomial data.
- Resurgence and the Garoufalidis–Zagier quantum-modularity conjectures predict the *entire* transseries (all Stokes data, all flat connections) and have been checked to very high precision, but remain conjectural for general knots.

## What a full resolution requires

A proof for all hyperbolic knots would need a *uniform* mechanism, replacing today's knot-by-knot labor:
1. A general way to represent $J_N(K;e^{2\pi i/N})$ as an integral (or controlled sum) with summand $\exp(N\,S)$ and explicit error bounds, from any diagram or triangulation.
2. A theorem that the **geometric** critical point of $S$ exists (the positively oriented hyperbolic structure) and **dominates** all other critical points (parabolic, reducible, other Galois conjugates) for every hyperbolic knot.
3. Rigorous contour deformation onto the corresponding Lefschetz thimble, controlling the Stokes phenomenon uniformly.

Step 2 is the crux: there is presently no general proof that the geometric flat connection has the largest growth rate for arbitrary knots.

## Plausible routes

- **Uniform saddle-point via Neumann–Zagier data**, making the geometric-dominance argument structural rather than case-specific.
- **Quantum modularity / resurgence** matured into rigorous theorems, extracting the leading exponential from the Borel/Stokes structure.
- **TQFT (Chen–Yang) bootstrap**, leveraging $6j$-symbol asymptotics ($\to$ hyperbolic tetrahedron volumes) and gluing to cover all triangulated hyperbolic manifolds, then specializing to knot complements.
- **Teichmüller TQFT (Andersen–Kashaev)** as an analytic route to the same volume/Chern–Simons asymptotics.

## Related problems

- [AbC Conjecture](../abc-conjecture/README.md) — like the VC, a deep "two worlds" bridge (here, analytic vs. arithmetic) resistant to direct proof.
- [Hodge Conjecture](../hodge-conjecture/README.md) — another conjecture asserting that algebraic/combinatorial data must encode geometry.
- [Birch–Swinnerton-Dyer Conjecture](../birch-swinnerton-dyer/README.md) — a leading-asymptotics-encodes-geometry statement (special-value of an $L$-function), structurally analogous in spirit.
- [Yang–Mills Mass Gap](../yang-mills-mass-gap/README.md) — shares the quantum-field-theory (Chern–Simons / path-integral) heuristics underlying Kashaev's and Witten's constructions.
