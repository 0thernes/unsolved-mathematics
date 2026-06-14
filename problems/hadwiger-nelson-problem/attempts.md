# Attempts — The Hadwiger–Nelson Problem

_Notable attempts, near-misses, retracted proofs._

For nearly seven decades the problem produced no movement on either bound, so its "attempts" are largely a story of incremental insight, clever finite configurations, and one spectacular breakthrough — rather than disputed proofs of the full answer. Because the answer is still unknown ($5 \le \chi \le 7$), there is no claimed *complete* resolution to contest; the disputes that exist concern the correctness of specific finite constructions, all of which were settled by independent computer verification.

## The Moser spindle and early lower bounds

The earliest substantive "attempt" beyond Nelson's original $4$-point idea was the **Moser spindle** (Leo and William Moser, 1961): a rigid $7$-vertex, $11$-edge unit-distance graph that is $4$-chromatic, giving a clean and memorable proof of $\chi \ge 4$. For decades, efforts to extend this to a $5$-chromatic finite graph by hand failed. Larger hand-built configurations (e.g. Golomb's graph, various "pinwheel" and fused-spindle constructions) reached chromatic number $4$ but never $5$, reinforcing a widespread expectation that improvement might require entirely new ideas — or that the answer might simply be $4$.

## De Grey's 2018 breakthrough (verified)

The genuine near-miss-turned-success was **Aubrey de Grey's** April 2018 construction of a $1581$-vertex unit-distance graph with no proper $4$-coloring, proving $\chi \ge 5$. Because the claim rested on a finite, explicit graph, it was immediately checkable: within days, independent researchers reproduced the non-$4$-colorability using SAT solvers and confirmed all unit-distance constraints. The result has been accepted without serious dispute. De Grey's paper itself candidly noted that his particular $1581$-vertex graph was almost certainly far from minimal, inviting the community to simplify it.

## Polymath16 minimizations (verified, with healthy scrutiny)

The **Polymath16** collaboration (2018–) set out to shrink de Grey's graph and to probe whether $\chi \ge 6$ might be reachable. It produced a cascade of smaller $5$-chromatic unit-distance graphs — examples with around $600$, $553$, $529$, $517$, $510$, and $509$ vertices have been reported, with searches for still smaller ones ongoing. Each reduction was a small "attempt" subject to the same SAT-based verification, and several intermediate claims were corrected through the open online review process — a model case of distributed, transparent error-checking rather than a dispute over a finished proof. Marijn Heule contributed both record-small constructions and machine-checkable UNSAT certificates, raising the standard of rigor.

## Searches for a 6-chromatic graph (unresolved)

A natural and much-attempted route to $\chi \ge 6$ is to find a finite unit-distance graph that is not $5$-colorable. Despite substantial computational effort within and beyond Polymath16, **no such graph has been found**, and there is no proof that one exists. This is the principal open near-miss: every attempt to force a sixth color has so far failed, leaving genuine uncertainty about whether $\chi = 5$.

## The measurable / axiom-dependence thread

A subtler "attempt" concerns whether the problem is even fully determined by ZFC. **Kenneth Falconer (1981)** showed the *measurable* chromatic number is at least $5$, and **Saharon Shelah and Alexander Soifer** later exhibited related distance-graph colorings whose chromatic numbers depend on the underlying set theory (e.g. differing between ZFC and systems where all sets are measurable). No one has shown that the plane's *ordinary* chromatic number is axiom-dependent, but the possibility — championed by Erdős and Soifer — remains a live, unrefuted concern that complicates any attempted unconditional resolution.

## Status of disputes

In summary: there is no retracted or seriously disputed claimed proof of the *value* of $\chi$. The one historic breakthrough (de Grey, $\chi \ge 5$) and all subsequent minimizations were finite and machine-verifiable, and survived independent scrutiny. The open questions — whether a $6$-chromatic finite graph exists, whether the upper bound can be beaten below $7$, and whether the true value is even ZFC-determined — remain genuinely unsettled rather than contested.
