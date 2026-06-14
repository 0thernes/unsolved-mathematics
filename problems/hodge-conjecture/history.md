# History — The Hodge Conjecture

_Origin, formulation, and timeline._

## How the problem arose

The Hodge conjecture sits at the junction of three nineteenth- and twentieth-century developments: the theory of algebraic cycles (Severi, Lefschetz), the topology of complex manifolds, and the harmonic theory of differential forms. On a compact Kähler manifold $X$, W. V. D. Hodge's theory of harmonic integrals (developed in the 1930s and codified in his 1941 book *The Theory and Applications of Harmonic Integrals*) produces the **Hodge decomposition** of complex cohomology,
$$H^{n}(X,\mathbb{C}) \;=\; \bigoplus_{p+q=n} H^{p,q}(X), \qquad \overline{H^{p,q}} = H^{q,p},$$
where $H^{p,q}$ consists of classes representable by harmonic forms of type $(p,q)$. An irreducible algebraic subvariety $Z \subset X$ of complex codimension $p$ defines, via its fundamental class, a cohomology class in $H^{2p}(X,\mathbb{Q})$ whose image in $H^{2p}(X,\mathbb{C})$ lies in the middle piece $H^{p,p}(X)$. The question Hodge raised is the **converse**: which rational $(p,p)$-classes arise this way?

A **Hodge class** of codimension $p$ is an element of
$$\mathrm{Hdg}^{p}(X) := H^{2p}(X,\mathbb{Q}) \cap H^{p,p}(X).$$
The conjecture asserts that on a *non-singular complex projective* variety $X$, every Hodge class is a $\mathbb{Q}$-linear combination of fundamental classes of algebraic subvarieties (algebraic cycles). For $p=1$ this is a theorem — the **Lefschetz $(1,1)$-theorem** (Lefschetz 1924) — which identifies $\mathrm{Hdg}^{1}(X)$ with the image of the Picard group (divisors / line bundles). The Hodge conjecture is the program to extend that theorem to all codimensions.

## Formulation and reformulations

Hodge's original 1950 statement was broader and partly *false* as stated: it included an integral version and a statement about the Hodge filtration's lower pieces. Two corrections shaped the modern form:

- **Integral Hodge conjecture is false.** Atiyah and Hirzebruch (1962) used topological $K$-theory and Steenrod operations to produce torsion cohomology classes that are Hodge but not algebraic, forcing the rational coefficients $\mathbb{Q}$.
- **The "general Hodge conjecture" (lower filtration levels) needed amendment.** Grothendieck (1969), in a sharply worded note, showed Hodge's general statement was false and proposed the corrected version now called the **Grothendieck amended general Hodge conjecture**, phrased via coniveau / the Hodge filtration.

The standard reference statement today is the one in the official **Clay Mathematics Institute Millennium Problem description** (Deligne, 2000), which restricts to the codimension-$p$ rational case on smooth projective varieties.

## Timeline

- **1924** — Lefschetz proves the $(1,1)$-theorem, the codimension-1 case, via normal functions and Poincaré normal functions.
- **1941** — Hodge publishes *The Theory and Applications of Harmonic Integrals*, establishing the Hodge decomposition.
- **1950** — Hodge poses the conjecture in his ICM (Cambridge, MA) address, "The topological invariants of algebraic varieties."
- **1957** — Kodaira's embedding theorem and Hodge theory mature; Weil and others reformulate cycles cohomologically.
- **1961–62** — Atiyah–Hirzebruch disprove the **integral** Hodge conjecture.
- **1969** — Grothendieck publishes "Hodge's general conjecture is false for trivial reasons," giving the amended general conjecture.
- **1969** — Mumford shows $0$-cycles on surfaces with $p_g>0$ are "infinite-dimensional," signalling deep obstructions for related cycle questions.
- **1977** — Deligne, Milne, Ogus, Shih develop **absolute Hodge cycles**; Deligne proves Hodge classes on abelian varieties are absolutely Hodge.
- **1995** — Lewis publishes *A Survey of the Hodge Conjecture*, the standard modern reference.
- **2000** — Clay Mathematics Institute names it one of seven **Millennium Prize Problems** (\$1,000,000), with Deligne's official problem description.
- **2013** — Voisin's monograph and survey articles map the obstruction landscape (Kähler counterexamples, defect of the integral conjecture).
- **Present** — The conjecture remains **open** in every codimension $p\ge 2$; verified only in special families (abelian varieties of low dimension, hypersurfaces, certain $K3$ and Calabi–Yau cases) and via the unconditional Lefschetz $(1,1)$ result.
