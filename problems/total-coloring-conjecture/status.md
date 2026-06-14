# Status & Frontier — The Total Coloring Conjecture

_Where the problem stands and what a resolution would require._

**Status: open (active-progress).** The conjecture $\chi''(G)\le\Delta(G)+2$ remains unproved in general. It is supported by exact theorems in every case where it has been checked and by a strong asymptotic result, but no verified argument establishes it for all graphs.

## What is known unconditionally

- **Bounded slack.** The strongest general theorem is Molloy and Reed (1998): there is an absolute constant $C$ with $\chi''(G)\le\Delta+C$ for every graph $G$. The proof uses the Lovász Local Lemma and Talagrand concentration; the explicit constant is enormous ($C=10^{26}$). This reduces the open question to *tightening a known constant to $2$*, which is why the conjecture is widely believed. (Molloy & Reed, *Combinatorica* 18 (1998); DOI 10.1007/PL00009810.)
- **Small maximum degree.** TCC is a theorem for $\Delta\le 5$: $\Delta\le 2$ trivially, $\Delta=3$ (Rosenfeld; Vijayaditya, 1971), $\Delta=4$ and $\Delta=5$ (Kostochka, 1977–1996).
- **Dense graphs.** Verified when $\Delta$ is large relative to the order $n$ (Yap and collaborators), and exactly for $K_n$, $K_{m,n}$, cycles, and various products/joins, with full Type-1/Type-2 classification.
- **Planar graphs.** Proved for planar $G$ with $\Delta\ge 7$ (Borodin and successors) and, via the small-degree results, for $\Delta\le 5$. The single open planar degree is $\Delta=6$.
- **Sparse/structured classes.** Holds for graphs of bounded maximum average degree under mild conditions, $k$-degenerate graphs for small $k$, series-parallel, outerplanar, and $K_4$-minor-free graphs, often with exact Type classification.

## What is known conditionally / in strengthened form

- The **list** version is open at the same level: the List Total Coloring Conjecture (Borodin–Kostochka–Woodall, 1997) asks $\mathrm{ch}''(G)=\chi''(G)\le\Delta+2$, proved for the same small-$\Delta$ and large-$\Delta$ regimes and with a Molloy–Reed-type constant bound, but unproved in general.
- Deciding whether a given graph is Type 1 ($\chi''=\Delta+1$) or Type 2 ($\chi''=\Delta+2$) is **NP-hard**, so any clean structural characterization faces a complexity barrier.

## What a full resolution requires

A complete proof must do one of:
1. **Drive the additive constant to 2** — replace the lossy local-lemma completion in Molloy–Reed with a near-optimal argument (entropy compression, an algorithmic local lemma with negligible waste, or a structural completion theorem) that loses no more than $2$ colors over $\Delta$ for *every* graph, dense and sparse alike; or
2. **Find a uniform structural/inductive scheme** that does not degrade with $\Delta$ — none is currently known, since total colorings do not restrict cleanly to lower-degree subgraphs.

## Plausible routes

- **Sharpening the probabilistic constant** toward small explicit values, then closing the residual gap by ad-hoc analysis (most-pursued route).
- **Completing the planar program** by resolving $\Delta=6$ via refined discharging, removing the last planar exception.
- **Proving the list strengthening**, which would imply the ordinary conjecture.

No route has produced a verified general proof, and any announcement of an elementary full proof should be treated cautiously pending peer review.

## Related problems

- [Vizing's edge-coloring family / total list version](../hadwiger-conjecture/README.md) — coloring strengthenings in the same lineage.
- [Cycle Double Cover Conjecture](../cycle-double-cover-conjecture/README.md) — another structural graph conjecture resistant to general proof.
- [Graceful Tree Conjecture](../graceful-tree-conjecture/README.md) — a labeling/coloring problem with similar small-case-vs-general gaps.
- [Reconstruction Conjecture](../reconstruction-conjecture/README.md) — a long-standing open problem in structural graph theory.
- [Caccetta–Häggkvist Conjecture](../caccetta-haggkvist-conjecture/README.md) — degree-constrained conjecture attacked by analogous extremal/probabilistic methods.
