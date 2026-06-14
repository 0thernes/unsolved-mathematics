# Status & Frontier — Seymour's Second Neighborhood Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** The general conjecture — every oriented graph (no loops, no digons) has a **Seymour vertex** $v$ with $|N^{++}(v)| \ge |N^{+}(v)|$ — is unresolved as of this writing. It has been open since Seymour posed it around 1990.

## What is known (unconditional)

- **Tournament case — proved.** Every tournament has a Seymour vertex. First established by **Fisher (1996)** via a probabilistic argument, then re-proved combinatorially by **Havet and Thomassé (2000)** using **median orders**, who showed the feed vertex of a median order works and extended the result to tournaments missing a perfect matching.
- **Constant-factor bound — proved.** **Chen, Shen, and Yuster** proved every oriented graph has a vertex $v$ with $|N^{++}(v)| \ge \gamma\,|N^{+}(v)|$, where $\gamma \approx 0.6573$ is the real root of $2x^3 + x^2 - 1 = 0$. This is the strongest general result and the current ceiling.
- **Structured subclasses — proved.** Tournaments minus a star (Fidler–Yuster), rose tournaments (Dean–Latka), comparability-graph orientations and further families (Daamouch), various sink-free and degree-constrained classes (Ghazal), vertex-transitive/Cayley digraphs, and all sufficiently small digraphs by computer.

## What is known (conditional / heuristic)

- The **feed-vertex heuristic** suggests a *local certificate* should exist, but no median-order analogue is known to certify a Seymour vertex in sparse oriented graphs.
- The naive global identity $\sum_v |N^{++}(v)| \ge \sum_v |N^{+}(v)|$ is **false** (directed paths are counterexamples), so any proof must locate a single good vertex without averaging.

## What a full resolution requires

A complete proof must produce a Seymour vertex in the **adversarial regime**: digon-free, sparse oriented graphs in which out-degrees are small and balanced so that no vertex is locally forced to expand. Both winning techniques for tournaments — Fisher's weighting and the median-order feed vertex — exploit the completeness/density of tournaments and provably fail here. The crux is bridging the gap from the unconditional constant $\gamma \approx 0.657$ up to $\gamma = 1$, or finding an entirely new local invariant that survives sparsity.

## Plausible routes

1. **Strengthen the multiplicative bound** toward $\gamma = 1$ by sharpening the Chen–Shen–Yuster analysis or via a new potential function.
2. **A sparsity-robust median order**, i.e. a vertex-ordering whose final vertex certifies the inequality even without arcs between every pair.
3. **Structural reduction** showing every hard instance reduces to an already-settled class (tournament-like, comparability, regular, etc.).
4. **Weighted / fractional formulations** that interpolate between the tournament case and the general case and isolate the obstruction.

No accepted proof of the general case exists; claims to the contrary have not cleared peer review, and the conjecture is uniformly listed as open in current surveys.

## Related problems

- [Caccetta–Häggkvist Conjecture](../caccetta-haggkvist-conjecture/README.md)
- [Reconstruction Conjecture](../reconstruction-conjecture/README.md)
- [Cycle Double Cover Conjecture](../cycle-double-cover-conjecture/README.md)
- [Erdős–Hajnal Conjecture](../erdos-hajnal-conjecture/README.md)
- [Hadwiger Conjecture](../hadwiger-conjecture/README.md)
