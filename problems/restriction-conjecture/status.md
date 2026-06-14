# Status & Frontier — The Restriction Conjecture

_Where the problem stands and what a resolution would require._

**Status: active-progress, open in all dimensions $n\ge 3$.** Metadata records the conjecture as unsolved, with steady frontier movement driven by the polynomial method, decoupling, and the Kakeya connection.

## What is known unconditionally

- **Dimension $n=2$: proven.** The extension operator maps $L^\infty(S^1)\to L^q(\mathbb{R}^2)$ for all $q>4$ (Fefferman–Stein, Carleson–Sjölin circle, c. 1970–72). This is the only complete case.
- **Stein–Tomas (1975):** $E:L^2(S^{n-1})\to L^q(\mathbb{R}^n)$ for $q\ge \tfrac{2(n+1)}{n-1}$, all $n$ — the universal baseline, sharp on the $L^2$ line.
- **$\mathbb{R}^3$ record:** Guth's polynomial-partitioning estimates (2016, 2018) give the extension bound for $q>3.25$, against the conjectural endpoint $q>3$.
- **Higher $n$:** Hickman–Rogers and related polynomial-partitioning results give the current best ranges, all strictly inside the conjectural region.
- **Decoupling:** the Bourgain–Demeter $\ell^2$ decoupling theorem (2015) is proven and sharp, but only up to the Stein–Tomas exponent.

## What is known conditionally

- **Restriction $\Rightarrow$ Kakeya:** any restriction estimate implies the corresponding Kakeya bound, so the conjecture is at least as hard as Kakeya. The 2025 Wang–Zahl proof of the **three-dimensional Kakeya set conjecture** removes the principal geometric obstruction in $n=3$ but does **not** by itself yield restriction (the implication does not reverse).
- A full sharp **Kakeya maximal** bound, combined with effective $\varepsilon$-removal and the broad–narrow machinery, is widely believed sufficient to push restriction in $\mathbb{R}^3$ to the endpoint — but no such implication is yet a theorem at the endpoint.

## What a full resolution requires

1. Closing the exponent gap (e.g. from $q>3.25$ to $q>3$ in $\mathbb{R}^3$) at the **sharp endpoint**, not merely up to $\varepsilon$.
2. Controlling **algebraic/sticky Kakeya configurations** — tubes clustered near low-degree varieties — which resist current cellular induction.
3. Capturing cancellation between **non-transversal wave packets**, beyond what $\ell^2$ orthogonality (decoupling) and multilinear transversality can see.

## Plausible routes

- **Polynomial method + refined Kakeya:** leverage Wang–Zahl-style volume/incidence estimates to feed sharper $\mathbb{R}^3$ restriction.
- **Decoupling beyond $\ell^2$:** new square-function or "small-cap" decoupling estimates targeting the restriction (not Stein–Tomas) exponent.
- **Hybrid bilinear/multilinear–polynomial schemes** with improved $\varepsilon$-removal to reach the endpoint.

## Related problems

- [Kakeya Conjecture](../kakeya-conjecture/) — the governing geometric obstruction; restriction $\Rightarrow$ Kakeya.
- [Bochner–Riesz Conjecture](../bochner-riesz-conjecture/) — sibling summability conjecture, implied by and closely paired with restriction.
- [Falconer Distance Conjecture](../falconer-distance-conjecture/) — geometric-measure-theory neighbor attacked with the same tools.
- [Hilbert's Sixteenth Problem](../hilbert-sixteenth-problem/) — unrelated in statement but a fellow long-standing analysis/geometry challenge for contrast.
- [Navier–Stokes Smoothness](../navier-stokes-smoothness/) — dispersive-PDE neighbor where restriction/Strichartz estimates are foundational tools.
