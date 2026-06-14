# Status & Frontier — The Caccetta–Häggkvist Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** The Caccetta–Häggkvist conjecture is unproved in every nontrivial case $k \ge 3$, and even its flagship instance — the triangle case $k=3$ — remains open. No accepted proof or disproof exists; all confirmed results are strictly partial.

## What is known

**The general statement, up to an additive constant.** The strongest *general* result is the theorem of Chvátal and Szemerédi (1985): every digraph on $n$ vertices with minimum out-degree $d \ge 1$ contains a directed cycle of length at most $n/d + c$ for an absolute constant $c$ (originally $2500$, since improved). This confirms the conjectured linear scaling $k \approx n/d$ but leaves an additive slack that the conjecture forbids.

**The triangle case ($k=3$).** The conjecture predicts that minimum out-degree $\ge n/3$ forces a directed triangle. The best **unconditional** result establishes this under the stronger hypothesis of minimum out-degree $\ge \beta n$ with $\beta \approx 0.3465$, obtained by Hladký, Král', and Norin via flag algebras / semidefinite programming, improving Shen Jian's earlier $0.3532\,n$ (2003). The gap between $0.3465$ and the conjectured $0.3333\ldots$ is the central open quantity.

**Settled relaxations (high confidence).**
- The **fractional** version of the triangle case holds with the exact constant $1/3$.
- The conjecture holds for **vertex-transitive** and **Cayley digraphs** via additive-combinatorial arguments.
- Small-order cases are confirmed by computer search.

These give strong evidence that the conjecture is *true*, localizing the difficulty to the absence of structure in general digraphs rather than to the threshold itself.

## What a full resolution would require

A proof of the triangle case must close the $\sim 0.013\,n$ gap left by every local method. The principal obstruction is that flag-algebra and averaging certificates use only **bounded-size local density information**, and there is good reason to think no finite local certificate can reach exactly $1/3$ — the extremal example $\vec{C}_n$ is "barely" triangle-free and only its **global** cyclic structure rules out a denser configuration. A resolution therefore likely needs a genuinely global or structural argument, or a new algebraic encoding that transcends the local-certificate ceiling. The general case $k \ge 4$ would, in addition, require removing the additive constant from the Chvátal–Szemerédi bound — converting an asymptotic statement into an exact threshold.

## Plausible routes

1. **A global flag-algebra-plus-structure hybrid**, combining semidefinite certificates with a structural classification of near-extremal triangle-free digraphs.
2. **Additive-combinatorial transfer**, exporting the rigidity available for Cayley digraphs to general out-regular digraphs.
3. **Progress on the Second Neighbourhood Conjecture**, which is closely linked and might, if proved, illuminate the triangle case.
4. **New entropy / compression bounds** sharp enough to eliminate additive slack.

The realistic assessment is that the problem is hard for structural reasons; incremental constant-pushing continues, but a decisive idea has not yet appeared.

## Related problems

- [Reconstruction Conjecture](../reconstruction-conjecture/README.md)
- [Cycle Double Cover Conjecture](../cycle-double-cover-conjecture/README.md)
- [Hadwiger Conjecture](../hadwiger-conjecture/README.md)
- [Graceful Tree Conjecture](../graceful-tree-conjecture/README.md)
- [Union-Closed Sets Conjecture](../union-closed-sets-conjecture/README.md)
