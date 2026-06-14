# Status & Frontier — Ryser's Conjecture (Hypergraph Covering)

_Where the problem stands and what a resolution would require._

**Status: active progress; open for all $r \ge 4$.** The conjecture asserts $\tau(H) \le (r-1)\,\nu(H)$ for every $r$-partite $r$-uniform hypergraph $H$, where $\nu$ is the matching number and $\tau$ the covering (transversal) number. It is a theorem for $r \le 3$ and remains unproven, with no announced full proof, for every larger rank.

## What is known (unconditional)

- **$r = 2$:** Exactly König's theorem (1931); in fact $\tau = \nu$.
- **$r = 3$:** Proven. First by **Henderson (1971)**; then by **Aharoni (2001)** via topological connectivity of independence complexes, using the Aharoni–Haxell hypergraph Hall theorem. The extremal $3$-partite hypergraphs were fully characterized by **Haxell, Narins and Szabó**.
- **Fractional version:** True for all $r$. By LP duality $\nu \le \nu^* = \tau^* \le \tau$, and Lovász–Füredi-type bounds give $\tau \le (r-1)\nu^*$. The obstruction to the full conjecture is the integer–fractional gap.
- **Intersecting case ($\nu = 1$, so the claim is $\tau \le r-1$):** Open in general. Tight examples come from **truncated projective planes of order $r-1$**, giving $\tau = r-1$ exactly when such a plane exists. In ranks where **no projective plane of order $r-1$ exists**, strict improvements $\tau \le r-2$ (or better) are known (Haxell–Scott; Bishnoi–Das–Morris–Pokrovskiy; Francetić–Herke–McKay–Wanless).
- **Small ranks:** **Haxell and Scott (2017)** obtained the strongest partial results for $r = 4$ and $r = 5$.
- **Extremal structure:** Uniqueness of projective-plane extremizers is **false** — Abu-Khazneh, Barát, Pokrovskiy and Szabó constructed non-projective-plane intersecting hypergraphs with $\tau = r-1$.

## What is known (conditional)

The exact intersecting bound $\tau = r-1$ in ranks where a projective plane of order $r-1$ *does* exist is sharp and unconditional as a lower bound; the difficulty is the matching **upper** bound for general configurations. No statement here is conditional on unproved hypotheses such as RH; the conditioning is on the (independent, unsolved) **existence question for projective planes**, which couples Ryser to finite geometry.

## What a full resolution requires

A proof must (i) handle **arbitrary $\nu$**, not just $\nu = 1$, since stability/connectivity arguments need a base bound to perturb; and (ii) **break the connectivity barrier** at $r = 4$ — the independence complexes governing the Aharoni–Haxell method are demonstrably not connected enough for $r \ge 4$, so a genuinely new tool is needed. A disproof would require an $r$-partite $r$-uniform hypergraph with $\tau > (r-1)\nu$; none is known, and computational search has found none in small ranks.

## Plausible routes

1. **A post-topological method** that controls $\tau$ without high-connectivity hypotheses (e.g. absorption, container, or entropy methods adapted to transversal covers).
2. **Settling the intersecting case for all $r$** first — widely seen as the crux — possibly via a structural dichotomy "small cover, or projective-plane-like."
3. **Rank-by-rank breakthroughs** at $r = 4$ that expose a generalizable mechanism.

This problem is **not** resolved, disputed, or independent; the metadata status is *active-progress*, and that is accurate. No resolution claim is made or cited here because none exists.

## Related problems

- [Hadamard Matrix Conjecture](../hadamard-matrix-conjecture/) — design theory and $(0,1)$/$\pm1$-matrix existence, Ryser's home territory.
- [Caccetta–Häggkvist Conjecture](../caccetta-haggkvist-conjecture/) — a sibling open problem in extremal directed-graph/cycle covering.
- [Union-Closed Sets Conjecture](../union-closed-sets-conjecture/) — another deceptively elementary extremal set-system conjecture.
- [Sunflower Conjecture](../sunflower-conjecture/) — extremal hypergraph structure and covering, methodologically adjacent.
- [Total Coloring Conjecture](../total-coloring-conjecture/) — min–max covering/coloring duality in the König–Vizing lineage.
