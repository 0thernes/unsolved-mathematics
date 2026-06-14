# Approaches — The Hadwiger–Nelson Problem

_Major strategies, partial results, and barriers._

The problem decomposes into two essentially independent tasks: **lowering the upper bound** below $7$ (a coloring/construction problem) and **raising the lower bound** above $5$ (a forbidden-configuration problem). The two halves have completely different toolkits, and the gap $5 \le \chi \le 7$ has stubbornly resisted both.

## Finite unit-distance graphs (lower bounds via De Bruijn–Erdős)

The foundational reduction is the **De Bruijn–Erdős theorem** (1951): the chromatic number of the infinite plane graph equals the supremum of the chromatic numbers of its *finite* subgraphs (this uses the axiom of choice / compactness). Hence to prove $\chi \ge k$ it suffices to exhibit a single **finite unit-distance graph** that is not $(k-1)$-colorable. This converts an infinitary problem into a finite combinatorial search.

- **Core idea.** Build a finite set of plane points, all pairwise unit distances forming edges, whose chromatic number is high.
- **Best result.** The **Moser spindle** (7 vertices, 1961) gives $\chi \ge 4$. Aubrey de Grey's $1581$-vertex graph (2018) gives $\chi \ge 5$. Polymath16 reduced the minimal known $5$-chromatic example to a few hundred vertices (notably examples with $510$ and $509$ vertices, and smaller candidates have been reported).
- **Barrier.** No finite $6$-chromatic unit-distance graph is known, and there is no proof that one exists. If $\chi = 5$, then *no* such graph exists and this entire route to $\chi \ge 6$ is closed; one would then need a fundamentally different (likely non-constructive or measure-theoretic) argument. The search space grows combinatorially, and human intuition for which rigid point configurations force high chromatic number is limited.

## SAT solvers and computer-assisted search

De Grey's breakthrough and all of Polymath16's refinements are inseparable from automated reasoning.

- **Core idea.** Encode "$G$ is $k$-colorable" as a Boolean satisfiability instance; a SAT solver either finds a coloring or produces an UNSAT certificate proving none exists. To *shrink* a known $5$-chromatic graph, repeatedly delete vertices and re-test, keeping deletions that preserve $5$-chromaticity (vertex-criticality search).
- **Best result.** Independent SAT verification of de Grey's $1581$-vertex graph; minimization to $\sim 500$–$600$ vertex $5$-chromatic graphs; DRAT/LRAT-style proof certificates giving machine-checkable UNSAT proofs.
- **Barrier.** Establishing $\chi \ge 6$ would require an UNSAT instance for $5$-coloring of some unit-distance graph, but candidate graphs are far larger and the search is wildly under-constrained — one must first *find* a $6$-chromatic configuration before a solver can certify it. SAT scales poorly as graph size grows, and the geometric realizability constraint (points must have exact unit distances, often involving irrational coordinates) complicates encoding.

## Measurable and density colorings

A parallel line studies colorings with regularity assumptions, where powerful analytic tools apply.

- **Core idea.** Restrict to colorings whose color classes are Lebesgue-measurable (or otherwise structured), and use harmonic analysis / measure theory to forbid low color counts.
- **Best result.** **Falconer (1981/1991)** proved that any coloring of the plane into measurable color classes needs at least $5$ colors — i.e. the *measurable chromatic number* satisfies $\chi_m(\mathbb{R}^2) \ge 5$. More recently, spectral and density arguments (e.g. via the **Lovász theta function** and linear-programming bounds on the independence ratio of the unit-distance graph) push the measurable lower bound higher; results pushing $\chi_m \ge 6$ have been reported under measurability.
- **Barrier.** These methods bound the *measurable* chromatic number, which may strictly exceed the ordinary $\chi$. A coloring achieving the true $\chi$ might be highly non-measurable (using the axiom of choice), so measurable bounds need not transfer. This is the heart of Erdős's speculation that the answer could be **axiom-dependent**: the value of $\chi$ might differ under ZFC versus models with strong regularity (e.g. solvability/measurability of all sets, as under the axiom of determinacy). Shelah and Soifer constructed colorings illustrating such dependence in related distance graphs.

## Upper-bound (coloring) constructions

The complementary effort tries to beat Isbell's $7$.

- **Core idea.** Design an explicit, ideally periodic, partition of the plane into "unit-distance-avoiding" regions using fewer than $7$ colors, or prove via fractional/LP relaxation that fewer colors could suffice.
- **Best result.** Isbell's hexagonal $7$-coloring remains the record; **no construction with $6$ colors is known.** Probabilistic and "almost" colorings (e.g. colorings that fail only on a measure-zero set, or that avoid a slightly perturbed distance) have produced $6$-coloring-like results for variants, but not for the exact unit distance in the full plane.
- **Barrier.** Tilings with $6$ regions of bounded diameter seem to be obstructed by elementary packing constraints around each point, and no flexible non-tiling scheme has succeeded. There is no known structural reason the upper bound *must* be $7$, but every attempt to reach $6$ has failed, suggesting either a hidden obstruction or simply that the right construction has not been found.

## Spectral / linear-programming and fractional relaxations

- **Core idea.** Bound the **fractional chromatic number** and independence density of $G(\mathbb{R}^2)$ using eigenvalue (Hoffman-type) and LP/SDP methods, then leverage $\chi \ge \chi_f$.
- **Best result.** The fractional chromatic number is known to be strictly greater than $4$ (consistent with $\chi \ge 5$), and LP bounds give nontrivial constraints on the maximum density of a unit-distance-avoiding set (the "$m_1(\mathbb{R}^2)$" problem), with the best upper bounds on this density below $0.23$.
- **Barrier.** Fractional and measure-theoretic relaxations are inherently weaker than integer chromatic number and, like the measurable approach, do not directly control non-measurable colorings; they have so far been unable to force $\chi_f$ above $5$.

Across all approaches, the central obstruction is structural: we possess no theorem that *characterizes* when a unit-distance graph requires many colors, so progress depends on either lucky explicit constructions (the lower-bound side) or on regularity assumptions that may not capture the true, possibly pathological, optimal coloring (the upper-bound and measurable sides).
