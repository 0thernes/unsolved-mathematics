# Status & Frontier — The Erdős Unit Distance Problem

_Where the problem stands and what a resolution would require._

**Status: open.** The problem has stood unresolved since 1946, and the decisive gap has barely narrowed since 1984. Let $u(n)$ denote the maximum number of unit distances among $n$ points in $\mathbb{R}^2$.

## What is known (unconditional)

- **Lower bound (1946, Erdős).** The $\sqrt n \times \sqrt n$ integer grid realizes
$$u(n) \ge n^{1 + c/\log\log n}$$
for some constant $c>0$, via Landau's count of sum-of-two-squares representations. This is the best lower bound known; it has *never* been improved.
- **Upper bound (1984, Spencer–Szemerédi–Trotter).**
$$u(n) = O(n^{4/3}).$$
This remains the record. Székely's 1997 crossing-number proof reestablished it transparently, and subsequent work (Pach–Tardos and others) has improved only the constant, not the exponent. The current best constant places the bound near $u(n) \lesssim c\, n^{4/3}$ with a small explicit $c$.
- **Conjecture (Erdős).** $u(n) = n^{1+o(1)}$; equivalently $u(n) = O(n^{1+\varepsilon})$ for every $\varepsilon>0$. The believed truth is essentially the lattice rate.

So the live gap is the factor $n^{1/3}$ between $n^{1+o(1)}$ (conjectured/lower) and $n^{4/3}$ (proved upper).

## Conditional and special-case results

- **Convex position:** points in convex position determine $O(n\log n)$ unit distances (essentially tight), far below $n^{4/3}$.
- **Structured inputs:** points on few lines or circles, or sets with small additive doubling, satisfy near-conjectural bounds via polynomial partitioning and additive combinatorics.
- **Other dimensions:** in $\mathbb{R}^d$, $d\ge 4$, the answer is $\Theta(n^2)$ (Lenz construction); in $\mathbb{R}^3$ the best bounds are around $n^{3/2}$, improved by Zahl and others. These are *not* conditional in the plane but illuminate which features make $d=2$ hard.
- **Sibling resolved:** the *distinct* distances problem — Erdős's companion 1946 question — was settled up to a logarithm by Guth and Katz (2010 preprint; Annals of Mathematics, 2015; DOI 10.4007/annals.2015.181.1.2), giving $\Omega(n/\log n)$ distinct distances. Their polynomial method has **not** transferred to the unit-distance count.

## What a full resolution would require

A proof of $u(n) = n^{1+o(1)}$ must do something no current method can: exploit a property **special to the round Euclidean circle**. This is forced by a barrier — there exist norms (with suitable unit balls) for which the maximum number of unit distances is genuinely $\Theta(n^{4/3})$. Hence any argument relying only on combinatorial, topological, or generic-convexity features (which apply uniformly to all "nice" norms) cannot beat $n^{4/3}$. A resolution must invoke the strict, uniform convexity of the circle together with the rigidity that two congruent circles meet in at most two points, and likely must prove a structural theorem forcing near-extremal sets to be lattice-like.

## Plausible routes

1. **A genuinely algebraic upper bound** that, unlike Guth–Katz, controls a *count* rather than a set of distinct values — e.g., a polynomial partition adapted to congruent-circle arrangements that uses curvature.
2. **A structure theorem** for near-extremal sets (additive-combinatorics / Freiman-type), proving they must concentrate on a sublattice, then bootstrapping the grid lower bound to an upper bound.
3. **A new incidence inequality for congruent circles** that strictly improves on Szemerédi–Trotter by using metric (not just topological) information — the route most directly blocked by the norm barrier, hence requiring an essentially Euclidean input.

Expert consensus rates the problem genuinely hard (the metadata difficulty is 84, tractability 28): the conjecture is almost universally believed, but no approach is currently near closing the $n^{1/3}$ gap.

## Related problems

- [Erdős Distinct Distances / Falconer Distance Conjecture](../falconer-distance-conjecture/README.md) — the continuous and distinct-value cousins of the same distance philosophy.
- [Hadwiger–Nelson Problem](../hadwiger-nelson-problem/README.md) — chromatic number of the unit-distance graph of the plane; same graph, different invariant.
- [Kakeya Conjecture](../kakeya-conjecture/README.md) — another geometry problem where the polynomial method reshaped the landscape.
- [Moving Sofa Problem](../moving-sofa-problem/README.md) — a sibling extremal-geometry problem in the same combinatorial-geometry tradition.
- [Inscribed Square Problem](../inscribed-square-problem/README.md) — companion open question in elementary plane geometry.
