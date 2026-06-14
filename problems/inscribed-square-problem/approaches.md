# Approaches — The Inscribed Square Problem (Toeplitz)

_Major strategies, partial results, and barriers._

The known proofs all establish the conjecture on restricted classes of curves and then attempt — so far unsuccessfully in full generality — to pass to the limit of arbitrary continuous curves. The strategies fall into a few families.

## Smoothing and limiting arguments

The core idea: prove inscribed squares for smooth curves, approximate an arbitrary Jordan curve $\gamma$ by smooth curves $\gamma_n \to \gamma$ uniformly, extract inscribed squares $S_n \subset \gamma_n$, and take a limit $S_n \to S$. **Best result:** this yields the conjecture for every curve in a class closed under good approximation and is the engine behind most special-case theorems. **Barrier:** the limit square $S$ may **degenerate to a single point**. A square inscribed in $\gamma_n$ can shrink as $n \to \infty$, so one needs a uniform lower bound on the size of the inscribed square — and no such bound is known for arbitrary continuous curves. Defeating this collapse is *the* central obstruction; it is why roughness, not non-convexity, is the enemy.

## Parity / degree-theoretic counting (Emch, Schnirelmann, Jerrard)

For smooth or analytic curves one counts inscribed squares (or inscribed rectangles, or midpoint configurations) modulo 2 and shows the count is **odd**, hence nonzero. Emch (1913) used the medians/chords of convex curves; Schnirelmann (1929) and Guggenheimer gave a $C^2$ argument via a transversality/degree count; Jerrard (1961) ran a parity argument for analytic curves. **Best result:** the conjecture holds for $C^2$ (and analytic) curves with an *odd* — therefore stable, generically transverse — number of inscribed squares. **Barrier:** parity arguments need transversality of an auxiliary map, which requires smoothness; they say nothing when the curve is merely continuous, and the odd count can collapse under degeneration.

## Locally monotone and bounded-variation curves (Stromquist)

Walter Stromquist (1989) proved the conjecture for **locally monotone** curves: curves that are, near each point, a monotone graph in some rotated coordinate frame. This class contains all piecewise-$C^1$ curves and all polygons. The method tracks "inscribed square" configurations through a continuous family and uses a connectedness/winding argument to force one to be a genuine square. **Best result:** one of the strongest *unconditional* general theorems; covers essentially every curve arising in practice. **Barrier:** local monotonicity is exactly the hypothesis that fails for genuinely wild curves (nowhere-monotone, fractal), which is where the open part of the problem lives.

## Topology in $\mathbb{R}^4$: the Möbius band and surfaces (Vaughan, Hugelmeyer)

Encode an unordered pair of points of $\gamma$ as a point of the configuration space; the space of such pairs is a **Möbius band** whose boundary is $\gamma$. Vaughan (c. 1977, published 1995) used this to show every Jordan curve inscribes a **rectangle**, since the relevant map cannot embed the Möbius band in the plane without a coincidence. Hugelmeyer (2018–2021) lifted these ideas to smooth knot theory, mapping the inscribed-rectangle question to embeddings of tori/Klein bottles in $\mathbb{R}^4$ and recovering rectangle results for many aspect ratios on smooth curves. **Best result:** rectangles (any aspect ratio in the smooth case via later work), and a clean topological proof for *some* rectangles on *all* Jordan curves. **Barrier:** a square is a rectangle of aspect ratio 1 *plus* the extra equation that the diagonals be equal/perpendicular at $90°$ — the topology that forces a rectangle does not, by itself, force the additional square constraint, and the strongest square versions still require smoothness.

## Symplectic geometry: Lagrangian tori (Greene–Lobb)

The most striking modern advance. Greene and Lobb (2020) reformulate inscribed rectangles for **smooth** Jordan curves as an intersection problem for Lagrangian tori in the symplectic 4-manifold $\mathbb{R}^4 \cong \mathbb{C}^2$. Using results on the non-displaceability/Floer-theoretic structure of monotone Lagrangian tori (à la Polterovich, Cieliebak–Mohnke), they prove that **every smooth Jordan curve inscribes a rectangle of every aspect ratio** — in particular a square. **Best result:** complete resolution of the *smooth* rectangle (hence smooth square) problem, a landmark. **Barrier:** the Lagrangian-torus machinery requires the curve to be smooth (or at least rectifiable enough to define the relevant Lagrangian submanifold); extending to merely continuous curves is open and appears to need genuinely new ideas, since the symplectic objects are not defined for wild curves.

## Special quadrilaterals and inscribed-figure variants

A parallel line studies which quadrilaterals are inscribable: every Jordan curve inscribes a rectangle (Vaughan); smooth curves inscribe all aspect-ratio rectangles (Greene–Lobb); cyclic quadrilaterals and other shapes give related theorems. **Best result:** broad families of inscribed shapes for smooth curves. **Barrier:** these results sharpen intuition but the square-on-continuous-curve case is strictly harder, sitting at the intersection of the degeneration problem and the loss of smoothness.

**Summary of the obstruction.** No fundamental impossibility (relativization-style barrier) is known — the conjecture is widely believed true. The single recurring obstacle is the **degeneration of inscribed squares to points under approximation**, which every smooth-case method must control and which no method yet controls for arbitrary continuous curves.
