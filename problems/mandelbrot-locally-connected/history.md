# History — The MLC Conjecture (Mandelbrot Locally Connected)

_Origin, formulation, and timeline._

## Origin and the object of study

The Mandelbrot set $M$ is the set of parameters $c \in \mathbb{C}$ for which the orbit of $0$ under $f_c(z)=z^2+c$ remains bounded, equivalently the connectedness locus of the quadratic family. Although iterates of complex quadratics were studied by Fatou and Julia around 1918–1920, and Brooks–Matelski produced an early picture of $M$ around 1978, the set entered systematic study after Benoît Mandelbrot's 1980 computer plots. The decisive mathematical analysis came from Adrien Douady and John H. Hubbard, whose 1982 *Comptes Rendus* note and the 1984–1985 *Orsay Notes* (« Étude dynamique des polynômes complexes ») established the foundational structure theory: $M$ is connected, it carries a Riemann map $\Phi:\widehat{\mathbb{C}}\setminus M \to \widehat{\mathbb{C}}\setminus \overline{\mathbb{D}}$ from its complement, and parameter rays may be defined via $\Phi$.

## Precise formulation

**MLC** asserts that $M$ is **locally connected** as a topological space: every point has a neighborhood basis of connected open sets. Because $M$ is compact, connected and full, the Carathéodory theory implies that MLC is equivalent to the statement that the inverse Riemann map $\Phi^{-1}$ extends continuously to the boundary circle, so that every external parameter ray $\mathcal{R}_\theta$ lands and the landing point depends continuously on the angle $\theta$. This yields the **pinched-disk / abstract Mandelbrot set** model: $M$ would be homeomorphic to the quotient of $\overline{\mathbb{D}}$ by Douady–Thurston's combinatorial lamination of rational external angles.

The central consequence, isolated by Douady and Hubbard, is that **MLC implies density of hyperbolicity** in the quadratic family — that is, the conjecture that the hyperbolic components of $M$ are dense, every $f_c$ with an attracting cycle being structurally stable. This is the "Fatou conjecture" restricted to degree two, making MLC one of the cornerstone problems of one-dimensional complex dynamics.

## Reformulations

MLC was recast combinatorially through Yoccoz's **parapuzzle**, through Thurston's lamination model, and through the dictionary with the Fibonacci/renormalization combinatorics. Lyubich reformulated the local question via the geometry of the **principal nest** of puzzle pieces and the contraction of renormalization operators on suitable parameter slices. A persistent theme is the *parameter–dynamical transfer*: control of the Julia-set geometry of individual maps (local connectivity of $J(f_c)$, a priori bounds) is exported to the parameter plane $M$.

## Timeline

**1918–1920** — Fatou and Julia develop iteration theory of rational maps.

**1978** — Brooks and Matelski publish an early computed image of the connectedness locus.

**1980** — Mandelbrot produces detailed plots; the set is named after him by Douady and Hubbard.

**1982** — Douady–Hubbard announce the connectedness of $M$ and the structure theory ("Itération des polynômes quadratiques complexes", *C. R. Acad. Sci.*); MLC is posed.

**1984–1985** — The Orsay Notes circulate; parameter rays, the pinched-disk model and the MLC $\Rightarrow$ density-of-hyperbolicity implication are established.

**1990** — Jean-Christophe Yoccoz proves **MLC at every finitely renormalizable parameter** (and local connectivity of the corresponding Julia sets) via the puzzle/parapuzzle and *a priori* bounds; this is the foundational breakthrough.

**1993–1997** — Mikhail Lyubich and Curtis McMullen develop renormalization with complex bounds; Lyubich proves density of hyperbolicity along the real line (real quadratics), partly with Graczyk–Świątek.

**1997** — Lyubich announces MLC at infinitely renormalizable parameters of **bounded type** with sufficient *a priori* bounds.

**2000s** — Kahn, Lyubich, Kahn–Lyubich establish the **Quasi-Additivity Law** and "covering lemma", extending complex bounds to large classes of infinitely renormalizable maps.

**2009–2014** — Avila, Kahn, Lyubich, Shen and collaborators push *a priori* bounds and MLC into broader combinatorial regimes; the *molecule*/decorations of satellite renormalization are identified as the hard core.

**2010s–2020s** — Cheraghi, Chéritat, Buff, Shishikura and others analyze the *near-parabolic / Inou–Shishikura* renormalization, controlling the most resistant satellite-type combinatorics; Dudko–Lyubich and others advance the general theory.

**Present** — MLC remains **open in full generality**; the obstruction is concentrated at infinitely renormalizable parameters of unbounded satellite type (Feigenbaum-like and "molecule" combinatorics), where uniform *a priori* bounds are not known.
