# History — The Inscribed Square Problem (Toeplitz)

_Origin, formulation, and timeline._

The Inscribed Square Problem — often called the **square peg problem** — asks whether every continuous simple closed curve (Jordan curve) in the Euclidean plane $\mathbb{R}^2$ contains four points that are the vertices of a square. The conjecture is that the answer is yes: every Jordan curve inscribes at least one square.

## How the problem arose

The problem was posed by **Otto Toeplitz** in 1911, at a meeting of the Deutsche Mathematiker-Vereinigung (German Mathematical Society) in Karlsruhe, where he announced the conjecture and reported partial results. It belongs to a family of "inscribed figure" questions that flourished in the early twentieth century alongside the rigorous development of plane topology, itself driven by Camille Jordan's curve theorem (1887) and the subsequent search for proofs (Veblen, 1905). Toeplitz's formulation is deceptively elementary — it requires no machinery to state — yet it resists elementary resolution because the class of Jordan curves includes wildly non-smooth, nowhere-differentiable, and fractal-like examples (e.g., curves with positive area cannot occur, but Koch-type and Osgood curves do). The central difficulty is precisely this generality: techniques that work for smooth or convex curves break down on rough curves.

## Formulation and reformulations

The **modern formulation** is: for every injective continuous map $\gamma : S^1 \to \mathbb{R}^2$, the image $\gamma(S^1)$ contains four points forming a (non-degenerate) square. A key topological reformulation, due to the consideration of the configuration space of inscribed squares, recasts existence as a $\mathbb{Z}/4$-equivariant question or a question about the intersection/cobordism of certain surfaces in $\mathbb{R}^4$ — the approach exploited by Vaughan, Stromquist, and later by Hugelmeyer and Greene–Lobb. A natural generalization (the **rectangle peg** and **similar-quadrilateral** problems) asks which quadrilaterals can be inscribed; rectangles of every aspect ratio turn out to be more tractable on smooth curves than squares are on general curves.

## Timeline

- **1887** — Camille Jordan states the Jordan curve theorem, setting the topological backdrop for inscribed-figure problems.
- **1911** — Otto Toeplitz poses the square peg conjecture and announces partial results for convex curves.
- **1913** — Arnold Emch publishes a proof for smooth convex curves; over 1913–1916 he extends results to certain piecewise-analytic curves.
- **1929** — Lev Schnirelmann proves the conjecture for sufficiently smooth ($C^2$-type) curves; the argument is refined and corrected in later editions.
- **1944** — Ogilvy and others popularize and discuss the problem; partial results accumulate for special curve classes.
- **1961** — R. P. Jerrard establishes inscribed squares for analytic curves with a parity/transversality argument.
- **1989** — Walter Stromquist proves the conjecture for the broad class of "locally monotone" curves (including all piecewise-$C^1$ curves), one of the strongest general results.
- **1995** — H. Vaughan's slick topological argument shows every Jordan curve inscribes a **rectangle** (the Möbius-band/$\mathbb{R}^4$ method), influencing later square results.
- **2014–2017** — Benjamin Matschke writes an influential survey and obtains results for curves satisfying explicit smoothness/"$\varepsilon$" conditions; Terence Tao proves a square-peg variant for curves that are unions of Lipschitz graphs.
- **2020** — Joshua Greene and Andrew Lobb prove that every **smooth** Jordan curve inscribes rectangles of *every* aspect ratio, using symplectic geometry in $\mathbb{R}^4$ (Lagrangian tori); Cole Hugelmeyer obtains related rectangle-inscription results via knot/embedding theory.
- **2021–present** — Greene–Lobb and others extend the smooth rectangle results; the general (continuous, non-smooth) square case remains open. The frontier is bridging from smooth/locally-monotone curves to arbitrary Jordan curves.

After more than a century, the conjecture is **proved for essentially every reasonable smoothness class** (convex, analytic, piecewise-$C^1$, locally monotone, bounded-variation) but **remains open for the full class of continuous Jordan curves**, where the lack of any smoothness obstructs the limiting and transversality arguments on which all known proofs rely.
