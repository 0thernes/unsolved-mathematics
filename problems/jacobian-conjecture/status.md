# Status & Frontier — The Jacobian Conjecture

_Where the problem stands and what a resolution would require._

## Current status: open

The Jacobian Conjecture is **open** in every dimension $n \ge 2$, over $\mathbb{C}$ (equivalently, over any field of characteristic zero). The case $n=1$ is trivial. No proof or counterexample in $n\ge 2$ has survived refereeing, despite more than eighty years of attempts and a substantial record of withdrawn general claims. There is no metadata flag of "resolved" or "disputed-claim," and none is warranted: any announcement to the contrary should be treated as unverified pending independent confirmation.

## What is known (unconditional)

- **Reduction to cubic / cubic-linear maps.** It suffices to prove the conjecture for $F = X + H$ with $H$ homogeneous of degree 3 (Bass–Connell–Wright; Yagzhev), and further for the cubic-linear normal form $H_i = (a_i\cdot x)^3$ (Drużkowski). Equivalently, one must show $DH$ nilpotent $\Rightarrow$ $X+H$ invertible.
- **Low-degree settlement.** Degree-2 maps are invertible in all dimensions.
- **Dimension 2, bounded degree.** Moh (1983) settled degree $\le 100$ in the plane; the plane case in unbounded degree remains open.
- **Structural special cases.** The symmetric (gradient) case and various nilpotent-Jacobian classes are resolved in low rank/dimension (de Bondt–van den Essen).
- **Inverse degree bound.** If $F$ is invertible then $\deg F^{-1} \le (\deg F)^{n-1}$ — a bound on the *inverse assuming it exists*, not a proof that it exists.

## What is known (conditional / equivalences)

- **Dixmier $\Rightarrow$ Jacobian.** Belov-Kanel and Kontsevich (2007) proved $\mathrm{JC}_{2n}$ is stably equivalent to the Dixmier conjecture $\mathrm{DC}_n$ on endomorphisms of the Weyl algebra. A proof of Dixmier's conjecture would settle the Jacobian Conjecture (and conversely in the stable limit).
- **Vanishing conjecture $\Leftrightarrow$ Jacobian.** Zhao's vanishing conjecture for the Laplacian (and the Mathieu–Zhao-space formulation) is equivalent to the full conjecture.

## What a full resolution would require

A complete proof must close the **local-to-global gap**: the constant-Jacobian hypothesis already supplies an analytic/formal local inverse everywhere, so the work is to force that inverse to be a single *global polynomial*. Concretely, a resolution would need either (a) a dimension-uniform proof that nilpotency of $DH$ forces invertibility of $X+H$ in the cubic-linear case — overcoming the degree/dimension trade-off that defeats inductive arguments — or (b) a proof of an equivalent conjecture (Dixmier, or Zhao's vanishing conjecture) by methods strong enough to transfer back. A counterexample, conversely, would require a polynomial map with constant nonzero Jacobian that fails to be injective or whose inverse is non-polynomial; the analytic rigidity of $\mathrm{char}\,0$ makes such an object hard even to search for, and none is known.

## Plausible routes

1. **Noncommutative / quantization route.** Attack the Dixmier conjecture directly, exploiting the Weyl-algebra bridge.
2. **Differential-operator route.** Prove cases of Zhao's vanishing conjecture, building toward the general statement via Mathieu–Zhao-space theory.
3. **Structural induction on nilpotency.** Extend de Bondt–van den Essen classifications to higher rank, seeking a uniform argument.
4. **Tropical / Newton-polytope degree control.** Combine inverse-degree bounds with combinatorial constraints to rule out non-polynomial inverses.

Each route is active; none has yet produced a path that survives the dimension barrier.

## Related problems

- [Hodge Conjecture](../hodge-conjecture/README.md)
- [Schanuel's Conjecture](../schanuel-conjecture/README.md)
- [Invariant Subspace Problem](../invariant-subspace-problem/README.md)
- [P versus NP](../p-versus-np/README.md)
