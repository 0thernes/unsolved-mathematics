# Status & Frontier — The Unique Games Conjecture

**Status: active-progress; open.** The Unique Games Conjecture remains unproven and unrefuted. The community does not have consensus on whether it is true. What has changed dramatically since 2002 is the depth of partial results bracketing it from both sides.

## What is known (unconditional)

The strongest unconditional result is the **2-to-2 Games Theorem** of Khot, Minzer, and Safra (completed 2018, building on Dinur–Khot–Kindler–Minzer–Safra 2018). It proves NP-hardness of 2-to-2 games with imperfect completeness, which implies that unique games are NP-hard to distinguish between $(1/2-\varepsilon)$-satisfiable and $\varepsilon$-satisfiable. Concretely, this yields that **Vertex Cover is NP-hard to approximate within $\sqrt{2}-\varepsilon$**, improving on the prior $1.36$ bound of Dinur–Safra (2005). The technical core was the resolution of the **Grassmann-graph expansion** conjecture: non-expanding sets in the Grassmann graph are structured. Key arXiv references for the 2-to-2 cluster are *On Independent Sets, 2-to-2 Games, and Grassmann Graphs* and *Pseudorandom Sets in Grassmann Graph Have Near-Perfect Expansion* (Khot–Minzer–Safra, 2017–2018); the existence of these papers is high-confidence, though specific identifiers should be verified before citation.

The opposing unconditional fact is the **subexponential algorithm** of Arora–Barak–Steurer (2010), solving Unique Games in time $2^{n^{\varepsilon}}$. This is a *barrier*: any proof of UGC must yield instances solvable in subexponential time, so UGC cannot hold in the strongest exponential-hardness sense.

## What is known (conditional)

Assuming UGC, the picture is extraordinarily complete. **Raghavendra (2008)** proved that UGC implies a single semidefinite-programming relaxation achieves the *optimal* approximation ratio for **every** constraint satisfaction problem — so under UGC, approximation thresholds are exactly the SDP integrality gaps. UGC implies Max-Cut is hard beyond $\alpha_{GW}\approx 0.878$ (Khot–Kindler–Mossel–O'Donnell, with Majority Is Stablest), Vertex Cover beyond $2-\varepsilon$ (Khot–Regev), and tight bounds for sparsest-cut, multicut, and many ordering/grouping problems. UGC is also tightly linked to the **Small-Set Expansion Hypothesis** (Raghavendra–Steurer 2010), giving a purely graph-theoretic reformulation.

## What a full resolution requires

To **prove** UGC: a PCP/long-code reduction producing unique-games instances with completeness $1-\varepsilon$. The 2-to-2 framework reaches completeness $\approx 1/2$; bridging the gap to near-$1$ completeness is the central open obstacle and is not believed to be a routine extension. To **refute** UGC: a polynomial-time (or polynomial-round Sum-of-Squares) algorithm distinguishing the gap, which would make the conjecture false. Whether $\text{poly}(n)$-round SoS solves unique games is itself open and is the leading candidate refutation route.

## Plausible routes

1. **Lift completeness in the Grassmann/2-to-2 program** — extend the structured-expansion machinery to $d$-to-$1$ games with completeness $\to 1$.
2. **Settle Sum-of-Squares** — prove either an SoS algorithm (refuting UGC) or an $n^{\Omega(1)}$-round SoS integrality-gap lower bound (strong evidence for UGC).
3. **Resolve Small-Set Expansion** — an unconditional proof or refutation of SSE would likely carry UGC with it.

The honest assessment in 2026: substantial, carefully-vetted progress on both sides, a halfway hardness result in hand, and no settled answer.

## Related problems

- [P versus NP](../p-versus-np/README.md) — UGC is a refined hardness hypothesis living inside the P-vs-NP landscape of optimal inapproximability.
- [Hadwiger Conjecture](../hadwiger-conjecture/README.md) — a hard combinatorial-coloring problem of the kind whose approximability UGC would help pin down.
- [Sunflower Conjecture](../sunflower-conjecture/README.md) — a neighboring extremal/combinatorial question central to theoretical computer science.
