# Approaches — The Total Coloring Conjecture

_Major strategies, partial results, and barriers._

The TCC has resisted a uniform proof, so progress has come along several largely independent fronts: exhausting small maximum degree by hand, bounding the additive slack asymptotically by probabilistic means, exploiting sparsity/planarity through discharging, and reducing to or strengthening into list-coloring and structural frameworks.

## Small-$\Delta$ exhaustion (degree-by-degree)

**Core idea.** Verify $\chi''(G)\le\Delta+2$ for each fixed small $\Delta$ by structural case analysis, often reducing to critical (minimal counterexample) graphs and forbidding local configurations.

**Best result.** The conjecture is fully proved for $\Delta\le 5$. The cubic case $\Delta=3$ (giving $\chi''\le 5$) is due to Rosenfeld and to Vijayaditya (1971); $\Delta=4$ and $\Delta=5$ were settled by Kostochka (works spanning 1977–1996), with contributions by others. For these degrees the bound is now a theorem, not a conjecture.

**Barrier.** The case analysis grows combinatorially with $\Delta$: the number of reducible configurations and the interplay with edge coloring (itself NP-hard to decide for $\chi'=\Delta$ vs $\Delta+1$) make a hand proof intractable past $\Delta=5$. There is no induction on $\Delta$ that lowers the problem one degree at a time, because total colorings do not restrict cleanly to subgraphs of smaller degree.

## Probabilistic method (Molloy–Reed and the additive constant)

**Core idea.** Color edges and vertices in randomized rounds. Use the **Lovász Local Lemma** to show a partial random total coloring can almost always be completed, and **concentration inequalities** (Talagrand) to control the number of available colors at each element. This bounds $\chi''$ by $\Delta$ plus an absolute constant independent of $\Delta$.

**Best result.** Molloy and Reed (1998) proved $\chi''(G)\le\Delta+C$ with $C$ an absolute constant; their explicit value is astronomically large ($C=10^{26}$). This is the strongest *general* statement known and is essentially the reason the conjecture is believed. Subsequent refinements (e.g., work building on Reed's "$\omega,\Delta,\chi$" program and later sharpenings of local-lemma constants) have reduced the constant for restricted classes and improved the machinery, but no published general bound has driven $C$ down to anything near $2$.

**Barrier.** The probabilistic argument is inherently lossy: the local lemma "wastes" colors to guarantee completion, and Talagrand concentration introduces $\sqrt{\Delta}$-scale slack at intermediate stages that the final rounding absorbs into a large constant. Closing the gap from $C\approx 10^{26}$ to $C=2$ would require either a derandomized/entropy-compression scheme with near-zero waste or an entirely structural completion argument; this is the central obstruction to a full proof along this line.

## Sparsity, planarity, and discharging

**Core idea.** For graphs with bounded density (planar, bounded genus, bounded maximum average degree, $k$-degenerate), use the **discharging method**: assign charges to vertices/faces, redistribute, and derive a contradiction from a hypothetical minimal counterexample. Sparsity forbids the dense local structure that makes completion hard.

**Best result.** The TCC holds for all planar graphs with $\Delta\ge 7$ (Borodin and successors; the $\Delta\ge 9$ case was earliest, then pushed to $\Delta\ge 7$). Planar graphs with $\Delta\le 5$ are covered by the general small-$\Delta$ theorems, leaving $\Delta=6$ as the only open planar degree. Strong results also exist for graphs of bounded maximum average degree, series-parallel and outerplanar graphs (Type-1 classifications), and $K_4$-minor-free graphs.

**Barrier.** Discharging is class-specific and does not extend to dense graphs; the methods exploit Euler's formula or degeneracy and break down without a global sparsity hypothesis. The stubborn planar $\Delta=6$ case reflects how delicately the discharging weights must be tuned near the threshold.

## List total coloring and choosability

**Core idea.** Strengthen the conjecture to its **list** version: each vertex and edge gets a list of $\Delta+2$ admissible colors, and one seeks a proper total coloring choosing from the lists. The **List Total Coloring Conjecture** (Borodin–Kostochka–Woodall, 1997) posits the total choosability $\mathrm{ch}''(G)$ also satisfies $\mathrm{ch}''(G)\le\Delta+2$, and in fact that it equals $\chi''(G)$.

**Best result.** The list version is proved for the same small-$\Delta$ and many planar cases; for instance the total choosability of planar graphs with large $\Delta$ matches the ordinary bound. Probabilistic arguments (à la Molloy–Reed) port to the list setting, giving $\mathrm{ch}''(G)\le\Delta+C$.

**Barrier.** Choosability is strictly harder than coloring in general, and tools like the polynomial method (Combinatorial Nullstellensatz) that succeed for edge/total list coloring of special graphs do not scale to arbitrary $G$.

## Structural and algebraic reductions

**Core idea.** Relate $\chi''(G)$ to better-understood parameters — embedding total coloring into fractional/relaxation frameworks, using the relation between $\chi''$ and the edge chromatic number, or reducing to coloring the total graph via Nullstellensatz/permanent arguments.

**Best result.** Tight Type-1/Type-2 classifications for complete graphs $K_n$, complete bipartite graphs $K_{m,n}$, cycles, and several product/join families are known exactly; these confirm TCC with the precise value of $\chi''$.

**Barrier.** No reduction is known that converts TCC into a previously solved problem. Because deciding $\chi''(G)=\Delta+1$ vs $\Delta+2$ is **NP-hard** in general (shown for total coloring, paralleling Holyer's hardness for edge coloring), there is a complexity-theoretic obstruction to a simple efficiently-checkable structural characterization of Type-2 graphs.
