# Status & Frontier — Crouzeix's Conjecture

_Where the problem stands and what a resolution would require._

**Status: open, with active progress.** The conjecture — that for every square matrix $A$ and every polynomial $p$,
$$ \|p(A)\| \le 2\,\max_{z\in W(A)}|p(z)|, $$
with the constant $2$ optimal — remains **unproven in general** as of the latest reliable literature. It is widely believed true.

**Strongest unconditional result.** The best general theorem is the Crouzeix–Palencia bound (2017):
$$ \|p(A)\| \le (1+\sqrt 2)\,\|p\|_{W(A)} \approx 2.4142, $$
which holds for all matrices, all dimensions, and all polynomials (indeed all functions analytic on a neighborhood of $W(A)$). This superseded Crouzeix's own 2007 constant of $11.08$. Subsequent work by Ransford and Schwenninger re-derived the bound, exhibited small refinements, and showed that the unmodified Crouzeix–Palencia mechanism cannot itself break much below $\approx 2.4$ — closing the remaining interval down to $2$ requires a genuinely new ingredient.

**Unconditional special cases (where $2$ is proved).** The sharp constant $2$ is established for: all $2\times 2$ matrices; matrices whose numerical range is a disc (via the Okubo–Ando dilation); nilpotent Jordan blocks; and various structured (e.g. certain tridiagonal Toeplitz) and low-dimensional families. These cases also confirm that $2$ is *optimal*, since $2\times 2$ examples approach the ratio $2$ in the limit.

**Conditional results.** Several authors have obtained bounds approaching $2$ under additional hypotheses — on the geometry of $\partial W(A)$ (smoothness, absence of corners), on normality/structure of $A$, or within the completely-bounded (dilation) framework. None of these hypotheses has been removed in the general case.

**What a full resolution would require.** A proof must (i) hold for *arbitrary* convex $W(A)$, including those with corners and flat boundary segments; (ii) be uniform in dimension and polynomial degree; and (iii) reach exactly $2$, not merely some constant below $2.4$. The leading candidates are (a) an *asymmetric* sharpening of the Crouzeix–Palencia boundary pairing that avoids the lossy symmetrization, (b) a normal-dilation construction realizing constant $2$ on a general convex domain (which would give the stronger *complete* spectral-set statement), or (c) a potential-theoretic/Faber-operator bound controlling the relevant Cauchy operator over all convex curves. Computational extremal search continues to find no counterexample and to corroborate that the supremum of $\|p(A)\|/\|p\|_{W(A)}$ sits at $2$.

**Plausible routes.** Most observers expect progress first on the fully general $3\times 3$ case and on matrices with mildly non-smooth numerical range, then on a unified boundary or dilation argument. Because there is no formal barrier (no relativization-, natural-proofs-, or parity-type obstruction), the problem is regarded as hard-but-tractable: a single new idea bridging the $(2,\,1+\sqrt2]$ gap could resolve it.

## Related problems

- [Invariant Subspace Problem](../invariant-subspace-problem/README.md) — a central operator-theory open problem sharing the Hilbert-space functional-analytic setting.
- [Sendov's Conjecture](../sendov-conjecture/README.md) — like Crouzeix, a conjecture on the location/control of polynomial values relative to a geometric region in the complex plane.
- [Hadamard Matrix Conjecture](../hadamard-matrix-conjecture/README.md) — another matrix-analysis existence/extremal problem.
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — connected through spectral and potential-theoretic methods that recur in the analysis of $W(A)$.
