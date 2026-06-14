# Approaches — The Caccetta–Häggkvist Conjecture

_Major strategies, partial results, and barriers._

The conjecture has been attacked from extremal, additive, probabilistic, algebraic, and computational directions. Almost all heavy effort concentrates on the **triangle case** $k=3$ (minimum out-degree $\ge n/3$ forces a directed triangle), since it is widely believed to contain the full difficulty and yields the cleanest extremal statement. Below are the principal lines of attack.

## Direct counting / averaging arguments

**Core idea.** Suppose $D$ has minimum out-degree $d$ and no short directed cycle. Count walks, common out-neighbours, or in/out-neighbourhood overlaps to derive a contradiction when $d$ is large relative to $n$. The earliest bounds came from such averaging: if out-neighbourhoods are large and no triangle exists, the second out-neighbourhoods must spread, bounding $n$ from below in terms of $d$.

**Best result.** This style underlies the foundational partial bounds and the chain of improvements for $k=3$, getting the required out-degree down from $cn$ with $c$ near $1/2$ toward $1/3$. Shen Jian's $0.3532\,n$ bound (2003) is the high-water mark of essentially combinatorial counting.

**Barrier.** Pure averaging loses a constant factor that resists removal: the extremal $\vec{C}_n$ is "barely" triangle-free, so any argument that does not see the global cyclic structure leaves an irreducible gap above $1/3$.

## Flag algebras (Razborov's method)

**Core idea.** Encode densities of small sub-digraphs as variables and impose all valid linear/semidefinite relations among them; a semidefinite program then certifies the best constant achievable by "local" density inequalities. Applied to the triangle case, one optimizes over densities of out-stars and triangles.

**Best result.** **Hladký, Král', and Norin** used flag-algebra/semidefinite techniques to prove the triangle case under minimum out-degree $\ge \beta n$ with $\beta \approx 0.3465$ — the **best known unconditional bound** for $k=3$, replacing the previous $0.3532$.

**Barrier.** Flag algebras certify only inequalities provable from local (bounded-size) configuration densities. There is reason to believe the true constant $1/3$ is **not** reachable by any finite local certificate of this kind; the method appears to plateau strictly above $1/3$, so closing the last gap likely needs a genuinely global argument.

## Additive combinatorics and Cayley digraphs

**Core idea.** The triangle case has a sharp formulation for **Cayley digraphs** of abelian groups: if $S \subseteq \mathbb{Z}_n$ generates short sums, the absence of a directed triangle corresponds to a sum-free-type condition $S$ with $|S| \ge n/3$. This connects the conjecture to the structure of sum-free sets and to additive number theory.

**Best result.** The conjecture is **known to hold** for vertex-transitive and Cayley digraphs in many settings, where additive structure forces the threshold to behave as predicted. These cases give strong evidence for the truth of the general statement.

**Barrier.** General digraphs lack the algebraic rigidity of Cayley graphs; the additive techniques do not transfer to arbitrary out-degree-regular digraphs, so this line confirms rather than resolves the conjecture.

## Probabilistic and entropy / compression methods

**Core idea.** Use random sampling of vertices or random "shifts" to find a short cycle with positive probability, or apply entropy-compression to bound the number of long-girth digraphs. Probabilistic deletion and dependent random choice have been deployed to locate short cycles when degrees are large.

**Best result.** These methods recover the Chvátal–Szemerédi additive-constant theorem and variants — every digraph with minimum out-degree $d$ has a directed cycle of length $\le n/d + c$ — and yield clean asymptotic statements, but with additive slack rather than the exact $n/k$.

**Barrier.** The exact threshold is a zero-error statement; probabilistic methods naturally produce error terms or additive constants and have not been sharpened to the precise constant.

## Local / structural and Second-Neighbourhood connections

**Core idea.** Replace the global condition by a *local* one ("every out-neighbourhood spans no triangle") or study the closely related **Second Neighbourhood Conjecture** (every oriented graph has a vertex whose second out-neighbourhood is at least as large as its first). Structural decompositions of triangle-free digraphs constrain how extremal examples can look.

**Best result.** **Chudnovsky, Seymour, and Sullivan** proved nontrivial structural and local results, including bounds on the number of edges needed to make a triangle-free digraph acyclic, and partial cases of the second-neighbourhood statement. Fisher and others verified the *fractional* relaxation of the triangle case.

**Barrier.** The local-to-global passage is exactly where the difficulty lives; local hypotheses are strictly weaker, and the Second Neighbourhood Conjecture, while suggestive, is itself open and not known to imply Caccetta–Häggkvist.

## Computer-assisted verification

**Core idea.** Exhaustively or heuristically search digraphs of small order to confirm the conjecture and to test whether the extremal example is essentially unique. SDP solvers also supply the numerical certificates underlying the flag-algebra bounds.

**Best result.** Small-case verification supports the conjecture across the accessible range and confirms $\vec{C}_n$-type configurations as the extremal family; numerical SDPs deliver the $0.3465$ constant.

**Barrier.** Search space grows super-exponentially; computation extends confidence but cannot reach the asymptotic statement, and SDP certificates inherit the local-certificate ceiling described above.
