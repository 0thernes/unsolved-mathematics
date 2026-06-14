# Status & Frontier — The Bochner–Riesz Conjecture

_Where the problem stands and what a resolution would require._

**Status: active-progress.** The conjecture is **fully proved in dimension $n=2$** (Carleson–Sjölin, 1972) and **open in every dimension $n\ge3$**. The conjectured threshold $\delta(p)=\max\{\,n|1/p-1/2|-1/2,\,0\,\}$ is known to be *necessary* (sharp), so the open question is sufficiency above two dimensions.

## What is known

**Unconditional.**
- $n=2$: complete — $S^\delta_R$ is bounded on $L^p(\mathbb{R}^2)$ for all $\delta>\delta(p)$.
- All $n$: the Stein–Tomas $L^2$ restriction theorem (Tomas 1975) yields Bochner–Riesz boundedness for $\delta>\delta(p)$ on the restricted range up to the Stein–Tomas exponent $p=\tfrac{2(n+1)}{n-1}$ (and its dual).
- $n=3$ and above: substantially larger ranges than Stein–Tomas via the bilinear method (Tao–Vargas–Vega 1998; Lee 2004), the multilinear method (Bennett–Carbery–Tao 2006; Bourgain–Guth 2011), and polynomial partitioning / decoupling (Guth 2016–18; Bourgain–Demeter 2015; Guth–Hickman–Iliopoulou 2019). These record ranges still fall strictly short of $\delta(p)$ for the full $p$.

**Conditional.**
- The **restriction conjecture** for $S^{n-1}$ implies the Bochner–Riesz conjecture at matching exponents (via $\epsilon$-removal and Littlewood–Paley). So a proof of restriction in dimension $n$ would settle Bochner–Riesz in dimension $n$.
- Bochner–Riesz implies the **Kakeya maximal conjecture** (set-bound), so the conjecture is at least as hard as Kakeya — open for $n\ge3$.

## What a full resolution requires

A proof for $n\ge3$ must control wave packets adapted to the sphere through the full Kakeya/restriction range, i.e. handle the worst-case overlap of $\sim R^{(n-1)/2}$ tubes pointing in distinct directions, *at the critical exponent* without the $\epsilon$-loss that decoupling and multilinear methods incur. Concretely it would require either (i) a proof of the restriction conjecture, or (ii) a sharp linear (not merely multilinear or local) estimate that recovers the endpoint, or (iii) a new lossless mechanism converting the known multilinear/polynomial-partitioning gains into the linear bound.

## Plausible routes

- **Polynomial partitioning + decoupling refinements** (Guth–Hickman–Iliopoulou lineage) — the current frontier; the open problem is closing the multilinear-to-linear gap.
- **Restriction-first** — resolve the restriction conjecture (or its bilinear/multilinear endpoints) and transfer.
- **Kakeya-driven** — sharp Kakeya/incidence estimates (Katz–Zahl, Wang and collaborators) feeding back up the hierarchy; necessary but, alone, not known to be sufficient.

No accepted full proof for $n\ge3$ exists as of the present, and no full proof has been claimed by the community. The threshold $\delta(p)$ is not in dispute.

## Related problems

- [Restriction conjecture](../restriction-conjecture/) — the formally stronger problem that implies Bochner–Riesz.
- [Kakeya conjecture](../kakeya-conjecture/) — the geometric problem sitting below Bochner–Riesz in the hierarchy.
- [Falconer distance conjecture](../falconer-distance-conjecture/) — a sibling in the restriction/Kakeya circle of ideas.
- [Riemann hypothesis](../riemann-hypothesis/) — a thematic neighbor via Riesz means and summability of Dirichlet series.
