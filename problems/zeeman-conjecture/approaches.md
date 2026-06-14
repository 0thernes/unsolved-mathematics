# Approaches — The Zeeman Conjecture

_Major strategies, partial results, and barriers._

The Zeeman conjecture (ZC) asks that $K \times [0,1]$ be collapsible for every contractible compact $2$-complex $K$. Attacks fall into a handful of broad families, each making genuine progress on subclasses while running into a shared obstruction: the absence of a *local* certificate that a global collapse exists.

## Direct combinatorial collapsing

**Core idea.** Exhibit an explicit collapsing sequence for $K \times I$ given any contractible $K$. One builds the collapse from the product cell structure: free faces of $K \times I$ arise from faces of $K$ paired across the interval direction, and one collapses "downward" toward $K \times \{0\}$.

**Best result.** This works for the canonical examples. Zeeman himself collapsed $D \times I$ for the dunce hat $D$; the same is classical for **Bing's house with two rooms** $H$ (also contractible, non-collapsible, with $H \times I$ collapsible). More generally, if $K$ collapses to a point after deletion of a single $2$-cell, or has a "collapsible-after-one-expansion" structure, the product collapses.

**Barrier.** The product-collapse argument requires a starting free face whose removal does not destroy contractibility of the remaining complex; for a general contractible $2$-complex with no free faces and intricate identifications, no canonical first move is known. The combinatorics are not uniformly controllable.

## Reduction to Andrews–Curtis

**Core idea.** ZC implies the **Andrews–Curtis conjecture** (AC): a balanced presentation $\langle x_1,\dots,x_n \mid r_1,\dots,r_n\rangle$ of the trivial group can be reduced to the trivial presentation by elementary AC-transformations. Via the $2$-complex / spine dictionary, collapsibility of $K \times I$ corresponds to AC-trivializability of the associated presentation (after stabilization). One therefore studies ZC through presentations.

**Best result.** Many specific balanced presentations are known to be AC-trivializable, confirming ZC for the corresponding $K$. The dictionary makes ZC testable on infinite families parametrized by group presentations.

**Barrier.** AC is itself a famous open problem with strong **potential counterexamples** — the Akbulut–Kirby presentations $AK(n)$ for $n \ge 3$, and Miasnikov-type examples — that have resisted trivialization despite massive computer search. Since ZC is *stronger* than AC, any genuine AC counterexample would refute ZC. This makes the reduction a double-edged tool: it explains why ZC is hard and supplies the most credible candidates for a counterexample.

## Discrete Morse theory and metric/PL combinatorics

**Core idea.** Recast collapsibility as the existence of a **discrete Morse function** with a single critical cell. Collapsibility of a product can sometimes be deduced from non-trivial combinatorial-geometric hypotheses (CAT(0) / non-positive curvature, "constructibility," shellability) on $K$ or on its thickenings.

**Best result.** Adiprasito–Benedetti and related work prove that, e.g., **CAT(0) cube complexes and many non-positively curved complexes are collapsible**, and that taking products or sufficiently fine subdivisions can manufacture collapsibility. These yield ZC-type conclusions for complexes admitting good metrics or after controlled subdivision.

**Barrier.** ZC as stated is about a *fixed* triangulation and a *single* interval factor — it forbids subdivision and forbids extra thickening. Discrete Morse methods typically need either subdivision (changing the complex) or curvature hypotheses that a general contractible $2$-complex need not satisfy. Bridging from "collapsible after subdivision/thickening" to "$K \times I$ collapsible" is exactly the gap.

## Special spines and standard polyhedra

**Core idea.** Restrict to **standard (special) $2$-polyhedra** — spines of $3$-manifolds with generic local structure. For these the cell structure is rigid enough to analyze collapses combinatorially, and ZC can be attacked class by class (by number of true vertices, by the structure of the singular graph).

**Best result.** ZC is **verified for broad families of special spines** and for $2$-complexes of low complexity; results by Gillman, Rolfsen, Cretu and others confirm the conjecture for spines satisfying explicit local conditions.

**Barrier.** Not every contractible $2$-complex is (or canonically becomes) a special spine of a contractible region, and the inductive control degrades as complexity grows. The families settled do not exhaust the contractible $2$-complexes.

## Negative / barrier results

- **No counterexample is known**, but ZC's strength means it is *false if AC is false*; the persistence of untrivialized $AK(n)$ presentations is the principal evidence that ZC could fail.
- Contractible-but-not-collapsible $2$-complexes ($D$, $H$) show the hypothesis cannot be weakened to "contractible $\Rightarrow$ collapsible."
- Collapsibility is **NP-hard / algorithmically delicate** in general (deciding collapsibility of complexes is hard), so a uniform efficient certificate for $K \times I$ is not expected, ruling out naive algorithmic resolution.
