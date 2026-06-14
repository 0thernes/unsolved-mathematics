# History — The Novikov Conjecture

_Origin, formulation, and timeline._

## How the problem arose

The Novikov Conjecture grew out of the surgery-theoretic classification of high-dimensional manifolds developed in the 1960s. The key invariant in surgery theory, the symmetric/quadratic signature, sees the rational Pontryagin classes of a manifold. By the Hirzebruch signature theorem, the signature of a closed oriented $4k$-manifold $M$ is $\langle L(M), [M]\rangle$, where $L$ is the Hirzebruch $L$-class, a specific polynomial in the Pontryagin classes. Sergei Novikov's celebrated 1965 theorem on the topological invariance of rational Pontryagin classes showed these classes are far more rigid than the smooth-structure intuition suggested. Yet the Pontryagin classes themselves are not homotopy invariants — only the signature itself, a single number, is.

Novikov's question was: which *combinations* of Pontryagin numbers, twisted by the fundamental group, remain homotopy invariant? For a closed oriented manifold $M^n$ with fundamental group $\pi = \pi_1(M)$ and classifying map $f\colon M \to B\pi$, and a cohomology class $x \in H^*(B\pi;\mathbb{Q})$, the **higher signature** is
$$
\sigma_x(M) = \langle L(M)\smile f^*x,\, [M]\rangle \in \mathbb{Q}.
$$
For $x = 1$ this recovers the ordinary signature, which is a homotopy invariant by Thom. The conjecture asserts that **every** higher signature $\sigma_x(M)$ is an oriented-homotopy invariant of the pair $(M, f)$, for every discrete group $\pi$.

## Reformulations

The conjecture acquired its modern shape through the assembly map. Following Wall, Mishchenko, Quinn, and later Ranicki, the higher-signature statement is equivalent to the **rational injectivity of the assembly map**
$$
A\colon H_*(B\pi;\mathbb{L}(\mathbb{Z}))\otimes\mathbb{Q} \to L_*(\mathbb{Z}\pi)\otimes\mathbb{Q}
$$
in $L$-theory, and (via the Mishchenko–Kasparov picture) to rational injectivity of the Baum–Connes assembly map $K_*(B\pi)\otimes\mathbb{Q}\to K_*(C^*_r\pi)\otimes\mathbb{Q}$. This index-theoretic and $C^*$-algebraic reformulation turned a question about manifolds into one about the large-scale geometry of groups, opening the door to functional-analytic and coarse-geometric methods.

## Timeline

- **1965** — Novikov proves the topological invariance of rational Pontryagin classes; in the same circle of ideas he formulates the higher-signature conjecture.
- **1970** — Novikov delivers his ICM (Nice) address; the conjecture is widely disseminated. Mishchenko begins the $C^*$-algebraic/Fredholm approach.
- **1972–1974** — Lusztig proves the conjecture for free abelian groups $\mathbb{Z}^n$ using families of elliptic operators and harmonic analysis.
- **1974–1981** — Mishchenko and Kasparov develop $KK$-theory and the symmetric-signature operator, proving the conjecture for groups with non-positively curved features (Mishchenko: groups acting on contractible manifolds).
- **1988** — Kasparov proves Novikov for discrete subgroups of Lie groups (using $KK$ and the Dirac–dual-Dirac method).
- **1991** — Connes–Gromov–Moscovici prove it for hyperbolic groups; Connes–Moscovici handle Gromov-hyperbolic and related cases via cyclic cohomology.
- **1993** — Carlsson–Pedersen establish injectivity results using controlled topology and bounded $K$-theory.
- **1998** — Ferry, Ranicki, and Rosenberg edit the two-volume *Novikov Conjectures, Index Theorems and Rigidity* (LMS proceedings), the field's reference compendium.
- **2000** — Guoliang Yu proves the conjecture for groups with finite asymptotic dimension, and for groups coarsely embeddable into Hilbert space — a landmark coarse-geometric advance.
- **2002–2005** — Higson, Lafforgue, and Skandalis exhibit counterexamples to the *Baum–Connes* conjecture with coefficients (Gromov monster groups), sharpening the distinction between Baum–Connes and Novikov, which remains open and unrefuted.
- **2004–2012** — Bartels, Lück, Reich, and collaborators prove the Farrell–Jones Conjecture (which implies Novikov) for hyperbolic groups, CAT(0) groups, and later mapping class groups and $\mathrm{GL}_n(\mathbb{Z})$.
- **Present** — Novikov is known for an enormous class of groups; no counterexample exists and none is expected. The frontier is the general case for all discrete groups, with property-(T)/expander obstructions limiting the coarse-geometric toolkit.
