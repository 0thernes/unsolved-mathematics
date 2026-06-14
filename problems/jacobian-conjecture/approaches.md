# Approaches — The Jacobian Conjecture

_Major strategies, partial results, and barriers._

## Reduction of degree (the Bass–Connell–Wright / Yagzhev program)

The most consequential structural result is that the conjecture in arbitrary degree reduces to a single, sharply restricted family. Bass, Connell, and Wright (1982), with Yagzhev independently, showed that to prove the Jacobian Conjecture in all dimensions it suffices to prove it for maps $F = X + H$ with $H$ **homogeneous of degree 3**. Drużkowski (1983) reduced further to the *cubic-linear* case, where $H_i = (a_i\cdot x)^3$. For such maps the conjecture becomes equivalent to **nilpotency** of the Jacobian matrix $DH$.

**Best result.** Complete reduction to cubic (indeed cubic-linear) homogeneous maps; this is a permanent foundation of the subject.

**Barrier.** The reduction trades degree for *dimension*: a degree-$d$ map in dimension $n$ becomes a cubic map in a much larger dimension. So the cubic case is genuinely as hard as the general one; it concentrates the difficulty rather than dissolving it. No dimension-uniform handle on nilpotency has emerged.

## Low-dimension and low-degree verification

A long line of work confirms the conjecture under bounds. The degree-2 case holds in all dimensions (quadratic maps with constant Jacobian are invertible). In dimension 2, Moh (1983) proved the conjecture for maps of degree $\le 100$, and refinements pushed the bound further. Many special families — maps with symmetric Jacobian, maps whose Jacobian is a particular nilpotent type — are settled.

**Best result.** Full settlement of bounded-degree subcases and of structurally special families (e.g., de Bondt–van den Essen's results on symmetric and on certain nilpotent Jacobians).

**Barrier.** These results do not extend to a uniform bound: there is no known degree threshold beyond which the general case follows, and the dimension-2 problem itself remains open in unbounded degree.

## Nilpotency and the structure of $DH$

Recasting the cubic case as "$DH$ is nilpotent $\Rightarrow$ $X+H$ invertible" turned the problem into linear-algebra-flavored combinatorics of nilpotent matrices over polynomial rings. De Bondt and van den Essen, and others, classified nilpotent Jacobians in low dimensions and proved invertibility in those classes; symmetric reductions (where $DH$ is symmetric, so $H$ is a gradient) connect to Hessians and to the study of homogeneous polynomials with nilpotent Hessian.

**Best result.** Resolution for nilpotent Jacobians up to certain ranks/dimensions; the **symmetric (gradient) case** reduces to understanding polynomials with nilpotent Hessian, a problem with its own rich partial theory.

**Barrier.** The combinatorial explosion of nilpotency conditions in growing dimension has resisted a general argument; counterexamples to *overly optimistic* nilpotency statements (e.g., in the analogous Hessian classification) show the terrain is subtle.

## The Mathieu–Zhao / vanishing-conjecture framework

Wenhua Zhao reformulated the conjecture using differential operators and "Mathieu subspaces" (Mathieu–Zhao spaces). The **vanishing conjecture** states, roughly, that for a homogeneous polynomial $P$, if $\Delta^m(P^m) = 0$ for all $m\ge 1$ (with $\Delta$ the Laplacian), then $\Delta^m(P^{m+1}) = 0$ for all large $m$. Zhao proved this framework is *equivalent* to the Jacobian Conjecture, recasting an algebraic-geometric statement as one about iterated differential operators.

**Best result.** A genuine new equivalent formulation and a battery of special cases of the vanishing conjecture; fertile links to noncommutative algebra.

**Barrier.** The reformulation has not yet been easier to attack than the original; the general vanishing statement is as open as the conjecture itself.

## The Dixmier–Weyl-algebra connection (Belov-Kanel–Kontsevich)

Belov-Kanel and Kontsevich (2007) proved that the **Dixmier conjecture** (every endomorphism of the Weyl algebra $A_n$ is an automorphism) implies — and is, in a stably-equivalent sense, tightly linked to — the Jacobian Conjecture in dimension $2n$. This embeds the problem in noncommutative algebra and quantization.

**Best result.** A precise bridge: $\mathrm{JC}_{2n}$ and $\mathrm{DC}_n$ are equivalent under the stabilization "$JC = \varinjlim DC$."

**Barrier.** It relates one famously open problem to another equally open one (Dixmier's conjecture is itself unproven), so it relocates rather than removes the difficulty.

## Tame–wild automorphism theory and the inertia/Newton-polytope methods

Studying $\mathrm{Aut}(\mathbb{C}[x_1,\dots,x_n])$ directly, Shestakov–Umirbaev (2004) proved that the Nagata automorphism is *wild* in dimension 3 — a landmark in the structure theory of polynomial automorphisms. While this resolves the tame-generation question rather than the Jacobian Conjecture, the toolkit (degree estimates, reduction theory) informs attacks on it. Newton-polytope and tropical methods give degree bounds on the formal inverse.

**Best result.** Degree bounds for inverses (e.g., $\deg F^{-1} \le (\deg F)^{n-1}$ when $F$ is invertible), and sharp structural understanding in dimension 2–3.

**Barrier.** These bounds presuppose invertibility or control only formal data; they do not by themselves force a polynomial (rather than power-series) inverse, which is the crux.

## Why no "natural" obstruction has settled it

Unlike complexity theory (relativization, natural proofs, algebrization) or sieve theory (the parity barrier), the Jacobian Conjecture has **no widely accepted formal barrier theorem** explaining why proofs fail. The recurring failure mode is instead empirical: arguments that work in low dimension or low degree do not survive the dimension/degree trade-off, and the local-to-global gap (analytic-local inverse $\Rightarrow$ polynomial-global inverse) repeatedly evades control. The abundance of *retracted* general proofs is itself the field's main cautionary signal.
