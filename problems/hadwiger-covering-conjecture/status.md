# Status & Frontier — The Hadwiger Covering Conjecture

_Where the problem stands and what a resolution would require._

**Status: open** (per source metadata). The conjecture $c(K)\le 2^n$ for every convex body $K\subset\mathbb{R}^n$, with equality only for parallelepipeds, is unproven for all $n\ge 3$. The equivalent illumination form $I(K)\le 2^n$ is open in the same range. No accepted proof of the general case, and none of the full $3$-dimensional case, exists.

## What is known (unconditional)

- **$n=2$: fully solved.** $c(K)\le 4$, equality iff $K$ is a parallelogram (Levi).
- **Smooth bodies, any $n$:** $I(K)=n+1$, far below $2^n$.
- **General upper bound:** $c(K)\le \binom{2n}{n}(n\ln n + n\ln\ln n + 5n)$ for symmetric bodies (Huang–Slomka–Tkocz–Vritsiou, 2021), improving the classical Rogers/Erdős–Rogers estimate; in general $c(K)$ is bounded by a quantity of order $4^n$ up to polynomial factors. This is exponentially larger than the conjectured $2^n$.
- **Verified classes:** zonotopes/zonoids, belt polytopes and belt bodies, direct sums and many Cartesian products, centrally symmetric bodies in $\mathbb{R}^3$ ($c\le 8$, Lassak), constant-width bodies in $\mathbb{R}^3$, bodies of revolution, and bodies with sufficiently large symmetry groups.

## What is known (conditional / partial)

- For bodies already known to satisfy the bound, partial **rigidity** (equality forces near-parallelepiped) is understood, but a general stability theorem is missing.
- Fractional illumination yields the cleanest current bounds and stability estimates near the cube, but the **integrality gap** between fractional and integer covering numbers can be exponential.

## What a full resolution requires

1. **A non-volumetric method.** The probabilistic/economic-covering route is intrinsically lossy by a factor $\binom{2n}{n}/2^n\approx 2^n$. Reaching $2^n$ for all $K$ seems to demand an argument that exploits convex *structure* (faces, normal cones, polarity) rather than volume ratios.
2. **A vertex/normal-cone theory.** Even $n=3$ ($c\le 8$) hinges on controlling boundary points with large or irregular normal cones; the missing piece is a robust way to partition the sphere of directions into $\le 2^n$ illuminable regions for *arbitrary* bodies.
3. **The equality clause.** A complete solution must also prove uniqueness of parallelepipeds, i.e. a global rigidity/stability theorem, which currently lags the existence question.

## Plausible routes

- **Asymptotic geometric analysis:** push thin-shell/concentration and fractional methods (the Naszódi/Vritsiou direction) to shave the exponential gap, even partially (e.g. $c(K)\le c^n$ with $c<4$).
- **Structural low-dimensional attack:** resolve $\mathbb{R}^3$ outright via a new Gauss-map partition, then seek induction or transfer to higher dimensions.
- **Belt/symmetry expansion:** enlarge the family of structured bodies for which the bound holds until the residual "generic" case can be handled by approximation.

No route currently bridges the $2^n$-versus-$4^n$ gap for general bodies, and the consensus in the survey literature (Bezdek–Khan; Boltyanski–Martini–Soltan; Naszódi) is that a genuinely new idea is needed.

## Related problems

- [Hadwiger Conjecture (graph coloring)](../hadwiger-conjecture/) — Hadwiger's other namesake conjecture, in structural graph theory.
- [Hadwiger–Nelson Problem](../hadwiger-nelson-problem/) — chromatic number of the plane, another Hadwiger-linked combinatorial-geometry question.
- [Kakeya Conjecture](../kakeya-conjecture/) — extremal geometry of sets and coverings/projections in $\mathbb{R}^n$.
- [Inscribed Square Problem](../inscribed-square-problem/) — a sibling open problem in elementary/discrete geometry.
- [Moving Sofa Problem](../moving-sofa-problem/) — extremal convex-geometry optimization with an unknown extremizer, like the parallelepiped here.
