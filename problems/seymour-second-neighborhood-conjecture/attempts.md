# Attempts — Seymour's Second Neighborhood Conjecture

_Notable attempts, near-misses, retracted proofs._

## Fisher's resolution of the tournament case (1996)

The first major breakthrough was **David C. Fisher's** proof of **Dean's conjecture**, the tournament special case, in *"Squaring a tournament: a proof of Dean's conjecture"* (J. Graph Theory, 1996). Fisher used a probabilistic weighting argument. This is a genuine, accepted theorem and settled the historical root of the problem — but it does **not** extend to general oriented graphs, where digons are absent and the density that drives the weighting is gone.

## Havet–Thomassé via median orders (2000)

**Frédéric Havet and Stéphan Thomassé** gave a transparent combinatorial proof of the tournament case using **median orders**, showing the *feed vertex* (final vertex of a median order) is a Seymour vertex, and extending the result to **tournaments missing a perfect matching**. This is regarded as the cleanest proof of the tournament case and introduced the technique underlying most subsequent partial progress. It is a near-miss for the general conjecture in the sense that it suggests a local certificate (the feed vertex) — but the certificate provably fails for sparse oriented graphs.

## Chen–Shen–Yuster constant-factor bound (2003/2006)

**Guantao Chen, Jian Shen, and Raphael Yuster** proved that *every* oriented graph has a vertex $v$ with $|N^{++}(v)| \ge \gamma\,|N^+(v)|$, where $\gamma \approx 0.657$ is the real root of $2x^3 + x^2 - 1 = 0$. This is the strongest unconditional general statement to date and the closest anyone has come to the full conjecture across all oriented graphs. It falls short of the exact constant $\gamma = 1$, and the gap has not been meaningfully narrowed since.

## Verified subclasses (near-complete results)

A substantial near-miss literature confirms the conjecture for structured families without resolving the general case:

- **Fidler and Yuster (2007):** tournaments minus a star, and digraphs missing a "generalized star."
- **Dean and Latka:** the class of **rose tournaments** and related tournament families.
- Digraphs with prescribed minimum out-degree, regular and quasi-regular oriented graphs, vertex-transitive and Cayley digraphs, and digraphs whose underlying graph is a comparability or interval graph (**Daamouch** and others, 2010s).
- Small cases established by **computer search**.

Each result is correct within its scope; none reaches the adversarial sparse instances that make the general problem hard.

## On claimed general proofs

Over the years, informal claims of a full proof have circulated in preprint form and on discussion forums. As of the latest reliable surveys, **no claimed proof of the general conjecture has been accepted by the community**, and the problem is uniformly listed as open. We do not cite specific unrefereed manuscripts here: per the honesty standard of this reference, a claim is reported as established only when it has cleared peer review, and we are not aware of a refereed proof of the general case. Readers encountering a purported solution should check whether it (a) handles digon-free *sparse* oriented graphs, not just tournaments, and (b) avoids the false summed inequality $\sum_v |N^{++}(v)| \ge \sum_v |N^{+}(v)|$, which has explicit counterexamples — the two places where attempts most commonly break down.
