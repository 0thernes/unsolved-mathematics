# Status & Frontier — The Inscribed Square Problem (Toeplitz)

_Where the problem stands and what a resolution would require._

**Status: open (active progress).** The general conjecture — *every continuous simple closed curve in $\mathbb{R}^2$ inscribes a square* — remains **unproved** for arbitrary Jordan curves. It is proved on every well-behaved subclass, and recent symplectic methods have closed the smooth case for the closely related rectangle problem.

## What is known (unconditional)

- **Convex curves:** Inscribed squares exist (Emch, 1913). Elementary and complete.
- **Smooth / analytic curves:** Schnirelmann (1929) and Jerrard (1961) prove existence via parity counts; the inscribed-square count is odd for generic smooth curves.
- **Locally monotone curves:** Stromquist (1989) proves the conjecture for all locally monotone curves, which include every piecewise-$C^1$ curve and every polygon. This is the strongest broad unconditional result and covers essentially all curves met in practice.
- **Lipschitz-graph unions:** Tao (2017) proves a square-peg theorem for curves that are unions of two Lipschitz graphs with small constant — an analytic route avoiding heavy topology.
- **Rectangles, all aspect ratios, smooth curves:** Greene and Lobb (2020) prove that **every smooth Jordan curve inscribes a rectangle of every aspect ratio**, in particular a square. This resolves the *smooth* square peg problem and is the headline recent advance.

## What is known (conditional / partial)

- Inscribed **rectangles** (some aspect ratio) exist on *every* Jordan curve, smooth or not (Vaughan's Möbius-band argument). The square is the rectangle constraint *plus* equal diagonals at $90°$, which the pure topology does not by itself force.
- Equivariant-topology and configuration-space methods (Matschke) give existence under explicit smoothness/$\varepsilon$ hypotheses but not for arbitrary continuous curves.
- Richard Schwartz and others have mapped out structural dichotomies for inscribed rectangles in general Jordan loops, isolating the genuinely wild regime.

## What a full resolution requires

A complete proof must handle **arbitrary continuous curves with no smoothness**, where the obstruction is uniform: prove that inscribed squares (or the relevant configuration intersections) **do not degenerate to a point** in the limit of a smooth approximation $\gamma_n \to \gamma$. Every special-case method secures a non-degenerate square via transversality, monotonicity, or a Lagrangian non-displaceability result that needs the curve to be smooth or tame. Removing that hypothesis — either by a new compactness/size bound or by a topological invariant defined directly for continuous curves — is the missing step.

## Plausible routes

1. **Extend the symplectic method off the smooth class.** Define the relevant Lagrangian objects (or a Floer-theoretic count) for rectifiable or merely continuous curves and recover the square as the aspect-ratio-1 rectangle. This is the most promising current direction but the symplectic data is not yet available for wild curves.
2. **A uniform non-degeneracy bound.** Prove a quantitative lower bound on the size of an inscribed square in terms of the geometry of $\gamma$, making the limiting argument valid for all continuous curves.
3. **Equivariant topology with weaker hypotheses.** Push Matschke-style $\mathbb{Z}/4$ configuration-space arguments down to the continuous category.

The consensus expectation is that the conjecture is **true**; no impossibility or barrier result is known. What is lacking is a way to convert the abundant smooth-case successes into a statement about the full, untamed class of Jordan curves.

## Related problems

- [Hadwiger–Nelson Problem](../hadwiger-nelson-problem/README.md)
- [Kakeya Conjecture](../kakeya-conjecture/README.md)
- [Hilbert's Sixteenth Problem](../hilbert-sixteenth-problem/README.md)
- [Hadwiger Conjecture](../hadwiger-conjecture/README.md)
