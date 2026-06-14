# Attempts — The Total Coloring Conjecture

_Notable attempts, near-misses, retracted proofs._

## Early exact verifications

The first confirmations were exact computations on highly structured families. Behzad, Chartrand, and Cooper (1967) determined $\chi''(K_n)$ and $\chi''(K_{m,n})$, establishing TCC there and exhibiting both Type-1 and Type-2 behavior (e.g. $K_n$ is Type 1 iff $n$ is odd). These calculations gave confidence in the $\Delta+2$ ceiling and, crucially, showed the bound is *sometimes tight*, ruling out any hope of a universal $\Delta+1$ theorem.

## The cubic case and small degrees

Rosenfeld and, independently, Vijayaditya (both 1971) proved $\chi''(G)\le 5$ for every graph with $\Delta=3$ — the first nontrivial *infinite* family settled. Kostochka then carried the program through $\Delta=4$ and $\Delta=5$ over roughly two decades (1977–1996). These are genuine theorems, but each required dedicated, increasingly intricate analysis, and the method visibly does not generalize: the absence of any proof for $\Delta=6$ in full generality is the clearest signal that degree-by-degree exhaustion has stalled.

## The Molloy–Reed breakthrough (1998)

The deepest near-resolution is the theorem of **Molloy and Reed**: $\chi''(G)\le\Delta+C$ for an absolute constant $C$, proved by the probabilistic method (Lovász Local Lemma plus Talagrand concentration). This reduced the conjecture from "is the slack bounded?" to "is the bounded slack exactly 2?" — a qualitative leap. Its weakness is quantitative: the explicit constant is on the order of $10^{26}$, so the result is morally decisive but numerically enormous. Driving $C$ from $10^{26}$ to $2$ is the outstanding challenge, and no incremental sharpening has come close.

## Asymptotic and large-degree results

Hind (1990) and Bollobás–Harris (1985), and later Hind–Molloy–Reed, produced bounds of the form $\chi''(G)\le\Delta+O(\sqrt{\Delta}\log\Delta)$ and $\Delta+O(\log\Delta/\log\log\Delta)$ for certain regimes before the constant bound — important near-misses that sharpened the probabilistic toolkit. Yap and collaborators (1989–1992) proved TCC for graphs whose maximum degree is large relative to the number of vertices (e.g. $\Delta\ge n-k$ for small $k$), covering the "dense" end exactly.

## Planar frontier

Borodin (1989) and successors established TCC for planar graphs with $\Delta\ge 9$, later improved to $\Delta\ge 7$. Combined with the small-$\Delta$ theorems ($\Delta\le 5$), the **only open planar case is $\Delta=6$** — a famously stubborn near-miss. Many partial results pin down $\Delta=6$ planar graphs under extra girth or sparsity hypotheses, but the unconditional case persists.

## Disputed and withdrawn claims

The TCC is a recurring target for **claimed elementary proofs**, none of which has survived scrutiny. A representative pattern: preprints periodically appear on arXiv and similar venues announcing a short proof of the general conjecture (often via an inductive or greedy completion argument). The standard objection is that such arguments implicitly assume a partial total coloring of a subgraph extends to the deleted vertex/edges, which is exactly the step that fails — the same obstruction that forced Molloy and Reed to deploy the local lemma rather than naive greediness. Because no such claim has been accepted by the refereed literature or verified by the community, the conjecture remains officially **open**. Stated neutrally: the metadata status is *active-progress*, not *resolved*; readers should treat any announcement of a full elementary proof with caution and look for peer-reviewed confirmation before citing it.

The honest summary is that two genuine partial results dominate the landscape — exact theorems for $\Delta\le 5$ and the Molloy–Reed constant-slack bound — and the remaining gap (a large constant down to $2$, plus the planar $\Delta=6$ hole) has not been closed by any verified argument.
