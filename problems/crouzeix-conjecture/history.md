# History — Crouzeix's Conjecture

_Origin, formulation, and timeline._

Crouzeix's conjecture lives at the intersection of matrix analysis, operator theory, and complex approximation. Its central object is the **numerical range** (or field of values) of a square matrix $A \in \mathbb{C}^{n\times n}$,
$$ W(A) = \{ \langle Ax, x\rangle : x \in \mathbb{C}^n,\ \|x\|=1 \}, $$
a compact convex subset of the plane (Toeplitz–Hausdorff theorem, 1918–1919). The conjecture asserts that $W(A)$ is a *spectral set up to a universal constant*: for every polynomial $p$,
$$ \|p(A)\| \le 2 \, \max_{z \in W(A)} |p(z)|, $$
where $\|\cdot\|$ is the operator (spectral) norm. The constant $2$ is conjectured to be optimal — it is approached by simple $2\times 2$ examples but never exceeded.

The problem arose from Crouzeix's program on functional calculus and resolvent estimates in numerical analysis. The natural comparison is the classical theory of **spectral sets** of von Neumann (1951): a set $\Omega$ is a spectral set for $A$ if $\|f(A)\| \le \|f\|_{\infty,\Omega}$ for every rational $f$ with poles off $\Omega$. Von Neumann's inequality says the closed unit disc is a spectral set whenever $\|A\|\le 1$ (constant $1$). The numerical range is generally *not* a spectral set, but Crouzeix proposed it is a **$K$-spectral set** with an absolute constant $K$ independent of the matrix, the dimension, and the polynomial degree, conjecturing the sharp $K$ equals $2$.

**Reformulations.** Several equivalent or closely related statements circulate. By a normal-dilation argument and the von Neumann theory, the polynomial bound extends to all functions analytic on a neighborhood of $W(A)$, and to rational functions with poles off $W(A)$. A potential-theoretic reformulation recasts the inequality through harmonic measure and conformal maps of the complement of $W(A)$. A particularly fruitful reformulation, due to Crouzeix and later sharpened by Crouzeix–Palencia, replaces the spectral-set framework by a direct estimate using the Cauchy transform and the boundary of $W(A)$, splitting $f$ into a function and a conjugated companion.

## Timeline

- **1918–1919** — Toeplitz and Hausdorff prove that $W(A)$ is convex, founding the modern theory of the numerical range.
- **1951** — von Neumann establishes his inequality, the prototype for "spectral set" estimates and the conceptual ancestor of the conjecture.
- **1990s–2003** — Crouzeix develops functional-calculus and resolvent estimates motivated by the numerical analysis of matrix functions and semigroups; the role of $W(A)$ as a quasi-spectral set emerges.
- **2004** — Michel Crouzeix poses the conjecture in the form $\|p(A)\|\le C\,\|p\|_{W(A)}$ with a universal constant, identifying $C=2$ as the conjectured optimal value. He proves the qualitative statement with a finite (large) constant in *Bull. Sci. Math.*
- **2007** — Crouzeix (*"Numerical range and functional calculus in Hilbert space,"* J. Funct. Anal. 244) proves the universal bound $\|p(A)\| \le 11.08\,\|p\|_{W(A)}$, the first clean explicit absolute constant.
- **2017** — Crouzeix and Palencia (*SIAM J. Matrix Anal. Appl.*) prove the landmark bound $\|p(A)\| \le (1+\sqrt 2)\,\|p\|_{W(A)} \approx 2.414$, a dramatic improvement via a boundary argument pairing $f$ with a conjugate companion.
- **2017–2019** — Ransford–Schwenninger, Greenbaum–Choi and others streamline, reinterpret, and slightly sharpen the Crouzeix–Palencia argument; conditional and restricted improvements appear.
- **2017** — Greenbaum, Choi and collaborators verify the conjecture computationally for broad classes and probe near-extremal examples; the $2\times 2$ case is settled with sharp constant $2$.
- **2018–2020** — The conjecture is proved for several special cases: $2\times 2$ matrices, nilpotent Jordan blocks, certain $3\times 3$ classes, and matrices whose numerical range is a disc.
- **2022** — Schwenninger, Ransford and others push the universal constant slightly below $1+\sqrt 2$ in refined settings; the general optimal $2$ remains open.
- **2024–present** — Work continues on $3\times 3$ matrices, on the boundary geometry of $W(A)$, on dilation-theoretic and complete-bound versions, and on closing the gap between the proven $\approx 2.414$ and the conjectured $2$.
