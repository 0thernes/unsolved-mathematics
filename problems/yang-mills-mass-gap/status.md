# Status & Frontier — Yang–Mills Existence and Mass Gap

_Where the problem stands and what a resolution would require._

**Status: open.** No construction satisfying the Clay Mathematics Institute criteria has been produced and accepted. The problem remains one of the seven Millennium Prize Problems, unsolved as of this compilation.

## What is known (unconditional)

- **Lower dimensions are settled.** Two-dimensional Yang–Mills is essentially exactly solvable (Driver, Sengupta, Lévy). The 2D and 3D Yang–Mills *measures* have been rigorously constructed by Chandra–Chevyrev–Hairer–Shen (2020–2022) via stochastic quantization, with a gauge-invariant state space and renormalized Langevin dynamics.
- **UV stability in 4D, finite volume.** Bałaban (1984–1989) proved uniform ultraviolet bounds for four-dimensional lattice Yang–Mills in finite volume via a renormalization-group expansion; Magnen–Rivasseau–Sénéor (1993) gave a complementary multiscale construction with an infrared cutoff. These are the deepest steps toward 4D existence but do not reach the infinite-volume continuum theory.
- **Strong-coupling lattice gap.** On the lattice at strong coupling, a positive mass gap and confinement are provable (Osterwalder–Seiler) via convergent expansions — but this is not the continuum (weak-coupling) regime.
- **Large-$N$ and Wilson-loop results.** Chatterjee (2015–2019) gave rigorous lattice results on Wilson loops and the large-$N$ limit, including a rigorous gauge–string duality at strong coupling.

## What is known (conditional / heuristic)

- Lattice Monte-Carlo simulations give strong numerical evidence for a positive glueball mass and confinement (e.g. Morningstar–Peardon, 1999), consistent with asymptotic freedom and dimensional transmutation. These are not theorems.
- Supersymmetric and holographic analyses (Seiberg–Witten; AdS/CFT) explain *mechanisms* (monopole/dual-superconductor condensation) for a gap in related theories, but not for pure $SU(N)$ Yang–Mills on $\mathbb{R}^4$.

## What a full resolution requires

For a compact simple gauge group $G$, construct a quantum Yang–Mills theory on $\mathbb{R}^4$ that:

1. satisfies the **Wightman axioms** (equivalently the Osterwalder–Schrader axioms for the Euclidean theory) — a separable Hilbert space, a unique vacuum, a positive-energy unitary representation of the Poincaré group, and gauge-invariant local observables;
2. is **non-trivial** (genuinely interacting, not Gaussian/free) — guarding against an analogue of the $\phi^4_4$ triviality result; and
3. has a **mass gap** $\Delta > 0$: the energy spectrum has an isolated lowest eigenvalue $0$ (vacuum) with a strictly positive gap to the rest, equivalently exponential clustering of correlations.

This means simultaneously controlling the ultraviolet (renormalization, using asymptotic freedom), the infrared/confining (strong-coupling) regime, the infinite-volume limit, gauge redundancy (Gribov ambiguities), and reflection positivity — in the continuum.

## Plausible routes

The most active current avenue is **stochastic quantization** (regularity structures / paracontrolled calculus), which has conquered $d=2,3$; extending it past the critical dimension $d=4$ is the obstacle. The classical **renormalization-group / constructive** program (Bałaban-style) holds the strongest 4D partial results and could in principle be pushed to infinite volume and to a gap, but the infrared regime is the unsolved heart. **Lattice-continuum** analysis (proving the weak-coupling continuum limit exists and retains a gap) is conceptually direct but technically formidable. No single route is favored to succeed soon; the consensus is that the problem requires genuinely new nonperturbative analysis in four dimensions.

## Related problems

- [Navier–Stokes Smoothness](../navier-stokes-smoothness/README.md) — the other Millennium analysis/PDE problem; both concern global control of a nonlinear field equation.
- [Hodge Conjecture](../hodge-conjecture/README.md) — sibling Millennium Problem; geometry/topology feeding into gauge theory.
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — Millennium Problem; spectral interpretations and zeta-function analogies recur in QFT.
- [P versus NP](../p-versus-np/README.md) — Millennium Problem in complexity theory, often cited alongside as a benchmark of difficulty.
