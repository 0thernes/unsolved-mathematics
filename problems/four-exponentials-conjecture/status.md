# Status & Frontier — The Four Exponentials Conjecture

**Status: open.** The four exponentials conjecture has been an explicit open problem since the 1960s and remains unproved as of the present. It is widely believed true and is a known consequence of deeper, also-unproved conjectures.

## What is known (unconditional)

- **Six exponentials theorem (proved).** For $\mathbb{Q}$-linearly independent $x_1,x_2$ and $\mathbb{Q}$-linearly independent $y_1,y_2,y_3$, at least one of the six $e^{x_i y_j}$ is transcendental. This is a full theorem (Lang, Ramachandra, 1960s) and is the conjecture's proved sibling — differing only by the extra third value $y_3$.
- **Five exponentials theorem (proved, Waldschmidt).** Adjoining a single auxiliary quantity to the four-element configuration yields a four-exponentials-style conclusion. This is the strongest *unconditional* approach to the four exponentials statement and is sharp for current methods.
- **Strong six exponentials theorem (proved, Roy).** A strengthening, phrased via the rank of matrices whose entries are logarithms of algebraic numbers, that anchors the "strong" hierarchy.
- **Special cases.** The conjecture is known in numerous configurations where extra algebraic relations or independence hypotheses supply the missing interpolation data.

## What is known (conditional)

- **Implied by Schanuel's conjecture.** Both the four exponentials conjecture and its strengthening, the **strong four exponentials conjecture**, follow from Schanuel's conjecture (for $\mathbb{Q}$-linearly independent $z_1,\dots,z_n$, $\operatorname{trdeg}_\mathbb{Q}\mathbb{Q}(z_1,\dots,z_n,e^{z_1},\dots,e^{z_n}) \ge n$). This conditional proof is rigorous and explains why the community regards the conjecture as true; it is not an unconditional resolution, since Schanuel's conjecture is itself far harder and open.

## What a full resolution would require

A proof must establish the **rank-one collapse**: a $2\times2$ matrix whose four entries are logarithms of algebraic numbers, with $\mathbb{Q}$-linearly independent rows and columns, cannot exist — equivalently, the four values $e^{x_iy_j}$ cannot all be algebraic. The obstruction is sharp and well understood: the auxiliary-function and interpolation-determinant counts that succeed at six (and barely at five) fall one increment short at four. The analytic upper bound on the relevant determinant and the arithmetic Liouville-type lower bound cross only when a fifth or sixth exponential is present. Closing the gap therefore requires either a genuinely new transcendence technique that extracts a contradiction from strictly less interpolation data, or a structural input (e.g., progress toward Schanuel's conjecture, or a new algebraic-independence criterion in the spirit of Roy's matrices-of-logarithms program).

## Plausible routes

1. **A new zero estimate / extrapolation** sharp enough to function in the $2\times2$ regime — the most direct but least foreseeable path.
2. **Roy-style structural reformulation** of the strong four exponentials conjecture into an algebraic statement about the $\mathbb{Q}$-vector space of logarithms of algebraic numbers that might be settled by other means.
3. **Partial progress toward Schanuel's conjecture** in low transcendence degree, which would deliver the four exponentials conjecture as a corollary.

No timeline is credible; the problem has been stable for decades, and specialists treat it as a deep, long-horizon target rather than an imminently solvable one.

## Related problems

- [Schanuel's Conjecture](../schanuel-conjecture/README.md) — the master conjecture implying the four exponentials conjecture.
- [Lehmer–Mahler Measure Conjecture](../lehmer-mahler-measure-conjecture/README.md) — a sibling problem in heights and values of algebraic numbers within transcendence/Diophantine theory.
- [Littlewood Conjecture](../littlewood-conjecture/README.md) — a Diophantine approximation problem of comparable depth and similar resistance to current methods.
