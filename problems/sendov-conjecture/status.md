# Status & Frontier — Sendov's Conjecture

**Status: active progress; open.** The conjecture is *not* resolved. It is, however, in an unusual state: proven at both ends of the degree spectrum, with only a finite (but enormous) intermediate range unproven.

## What is known (unconditional)

- **Small degrees.** The conjecture holds for all polynomials of small degree, verified rigorously through approximately $n \le 8$ (Brown, Brown–Xiang, and the earlier degree-by-degree program; the case $n=3$ goes back to Rubinstein, 1968). The trivial cases $n=2$ and the extremal example $p(z)=z^n-1$ pin down the sharp constant $1$.
- **Large degrees — the landmark result.** **Terence Tao (2020)**, *"Sendov's conjecture for sufficiently high degree polynomials"* (arXiv:2012.04125), proved that the conjecture holds for **all $n$ above some threshold $n_0$**. The proof encodes the roots as a probability measure, passes to a limiting equilibrium measure via compactness, and analyzes the location of critical points in that limit.
- **Interior-root regime.** **Jérôme Dégot (2014)** proved the conjecture for large degree when the distinguished root is bounded away from the unit circle, isolating the boundary as the hard case.
- **Structured classes.** Various special families (e.g., real-rooted polynomials, certain symmetric configurations) satisfy the conjecture for all degrees.

## Strongest current results, conditionally framed

There is no widely used *conditional* result (e.g., "assuming X, Sendov follows") in this problem; progress has been unconditional but partial. The operative conditional-style statement is internal to Tao's method: **if** the threshold $n_0$ from the compactness argument could be made explicit and shown to be $\le 8$ (or to overlap the computational frontier), the conjecture would follow completely. As stated, the compactness step is non-effective, so this junction is not yet closed.

## What a full resolution would require

Two complementary things:

1. **An effective large-degree threshold.** Convert Tao's existence-of-$n_0$ into an explicit, *usable* bound. Tao's argument as published does not yield such a bound at a scale that meets the verified small degrees.
2. **Closing the finite gap.** Either push rigorous (possibly computer-assisted) verification up from $n \approx 8$ to meet a lowered threshold, or replace the compactness step with a quantitative argument valid for all $n$ — particularly in the **boundary-sharp regime** where the distinguished root sits on or near the unit circle and there is no error budget.

## Plausible routes

- **Effectivize Tao.** The most direct path: make the equilibrium-measure / compactness argument quantitative.
- **Quantitative potential theory.** Sharpen logarithmic-potential estimates so the large-$n$ argument covers moderate $n$ directly.
- **Boundary analysis.** Resolve the critical-points-near-the-circle case (current work by Chalebgwa and others), the genuinely tight regime.
- **Heavy computation.** Extend rigorous degree-by-degree verification, ideally with interval-arithmetic or certified numerics, to shrink the open band from below.

A complete proof likely requires the first or second route to render the gap finite-and-checkable, then the fourth to finish it. As of now the conjecture stands open across the intermediate degrees, with no claimed complete proof surviving expert scrutiny.

## Related problems

- [Riemann Hypothesis](../riemann-hypothesis/README.md) — like Sendov, a question about the locations of zeros, here of an analytic function.
- [Hilbert's Sixteenth Problem](../hilbert-sixteenth-problem/README.md) — geometry/topology of solution sets, a kindred "location of special points" theme.
- [Jacobian Conjecture](../jacobian-conjecture/README.md) — another deceptively elementary statement in the geometry of polynomial maps that resists uniform proof.
- [Crouzeix's Conjecture](../crouzeix-conjecture/README.md) — a modern complex-analysis conjecture about polynomials and the numerical range, with a similar sharp-constant flavor.
- [Invariant Subspace Problem](../invariant-subspace-problem/README.md) — an operator/analysis problem where partial results and limiting arguments dominate the landscape.
