# Approaches — Seymour's Second Neighborhood Conjecture

_Major strategies, partial results, and barriers._

Throughout, $D$ is an oriented graph (no loops, no digons), $N^+(v)$ and $N^{++}(v)$ are the first and second out-neighborhoods, and a **Seymour vertex** is one with $|N^{++}(v)| \ge |N^{+}(v)|$.

## Median orders (feed-vertex method)

**Core idea.** Order the vertices of a tournament as $v_1,\dots,v_n$ so as to *maximize* the number of forward arcs (arcs $v_i\to v_j$ with $i<j$); such an ordering is a **median order**. The last vertex $v_n$ (the **feed vertex**) has strong local properties: between any two consecutive intervals, more than half the arcs point forward. Havet and Thomassé (2000) showed the feed vertex of a median order is always a Seymour vertex, giving a fully combinatorial proof of the tournament case and recovering Fisher's result.

**Best result reached.** The complete tournament case; tournaments minus a perfect matching; tournaments minus a star (Fidler–Yuster, 2007); and several near-tournament classes. Median orders also yield the existence of *two* Seymour vertices in any tournament without a "dominant" vertex.

**Barrier.** Median orders are defined via a global optimization specific to complete graphs. For general oriented graphs the analogous "local median" property fails: non-adjacent pairs carry no arc, so the counting argument that makes the feed vertex work collapses. Extending the feed-vertex argument past tournament-like density is the central obstruction.

## Probabilistic / weighting (Fisher's method)

**Core idea.** Fisher's 1996 proof of Dean's conjecture assigns weights to vertices and analyzes $\sum_v (|N^{++}(v)| - |N^{+}(v)|)$ via a clever probability distribution on tournaments ("squaring the tournament"), showing the average sign forces some vertex to satisfy the inequality.

**Best result reached.** A complete, independent proof of the tournament case predating the median-order argument.

**Barrier.** The weighting exploits that *every* pair of vertices is joined by an arc, so the global sum telescopes cleanly. In sparse oriented graphs the cancellation no longer holds, and naive averaging can fail because most vertices have small out-degree and the "missing" arcs are not neutral.

## Multiplicative relaxation (constant-factor bounds)

**Core idea.** Rather than prove $|N^{++}| \ge |N^+|$, prove $|N^{++}(v)| \ge \gamma\,|N^{+}(v)|$ for the best constant $\gamma \le 1$ one can establish for *all* oriented graphs.

**Best result reached.** **Chen, Shen, and Yuster (2006)** proved the conjecture holds with $\gamma = $ the real root of $2x^3 + x^2 - 1 = 0$, approximately $\gamma \approx 0.6573$. This is the strongest unconditional general result: every oriented graph has a vertex whose second out-neighborhood is at least about $0.657$ times its first.

**Barrier.** Closing the gap from $0.657$ to $1$ appears to require fundamentally new ideas; the analytic argument saturates and incremental improvements have not pushed $\gamma$ near $1$.

## Structural / forbidden-substructure classes

**Core idea.** Verify the conjecture for digraphs whose underlying graph or arc structure is restricted: tournaments and near-tournaments, comparability/interval-graph orientations, digraphs of bounded chromatic number or with specified minimum out-degree, "rose" tournaments (Dean–Latka), vertex-transitive and Cayley digraphs, and small cases by computer.

**Best result reached.** Confirmation across a wide patchwork of families — e.g. tournaments (settled), digraphs missing a generalized star, certain regular and quasi-regular oriented graphs, and digraphs whose underlying graph is a comparability graph (Daamouch and others).

**Barrier.** Each class is handled by ad hoc structure; there is no unifying decomposition that all hard instances reduce to. The extremal-looking cases (sparse oriented graphs balancing many small out-neighborhoods) evade every known structural reduction.

## Counting and discharging / local arguments

**Core idea.** Sum a local quantity over all vertices and use a discharging scheme to force the existence of a Seymour vertex, mirroring techniques from planar coloring.

**Best result reached.** Partial: produces the conjecture under degree-regularity or sparsity hypotheses, and reproves tournament cases.

**Barrier.** A clean global identity $\sum_v |N^{++}(v)| \ge \sum_v |N^{+}(v)|$ is **false in general** (paths and other sparse digraphs are explicit counterexamples to the summed inequality), so any counting proof must locate the *single* good vertex without summing — exactly where local-to-global control breaks down.

## Why no global technique closes it

The recurring obstruction is **sparsity with balance**: adversarial oriented graphs distribute out-degree so that no vertex is forced to expand, while the absence of digons removes the arc density that makes tournament arguments succeed. Every successful method (median orders, Fisher weighting) leans on completeness; every general method (multiplicative bounds, discharging) stalls strictly below the exact inequality. Bridging that gap is the open problem.
