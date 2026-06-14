# Status & Frontier — The Union-Closed Sets Conjecture (Frankl)

_Where the problem stands and what a resolution would require._

**Status: open, with active progress.** The conjecture — that every finite union-closed family $\mathcal{F}$ (with a non-empty member) has an element lying in at least half of its $m$ sets — is *not* proved in general. What changed dramatically in late 2022 is that the problem moved from "no constant lower bound at all" to "a concrete constant fraction, provably."

## Strongest current results (unconditional)

The state of the art is the **entropy bound**. Justin Gilmer's November 2022 preprint *A constant lower bound for the union-closed sets conjecture* (arXiv:2211.09055) proved that some element appears in at least $c\,m$ sets with $c \approx 0.01$ — the first unconditional constant. Within weeks this was sharpened independently — by Will Sawin (arXiv:2211.11504), Zachary Chase and Shachar Lovett (arXiv:2211.11689), Ryan Alweiss–Yang Liu–Mehtaab Sawhney–Kewen Wu (arXiv:2211.11731), and Luke Pebody — to

$$\max_x d(x) \ \ge\ \frac{3-\sqrt5}{2}\,m \ \approx\ 0.3820\,m,$$

the natural optimum of Gilmer's single-step two-set entropy inequality. Will Sawin then obtained a small improvement strictly beyond $0.38$, showing the $0.38$ barrier is not absolute. (These arXiv identifiers are from the late-2022 burst and are flagged for verification in `papers.md`; the Gilmer paper itself is certain.)

Alongside the entropy bound stand robust **special-case** results, all accepted: the conjecture holds when $\mathcal{F}$ contains a set of size $1$ or $2$; for all ground sets with $|X| \le 12$ and all families with $m \le 50$ (computational, Bošnjak–Marković and predecessors); for "dense" families with $m \ge \tfrac{2}{3}2^{|X|}$ (Balla–Bollobás–Eccles); for the graph / size-$\le 2$ case (Bruhn–Charbit–Schaudt–Telle); and for modular, lower-semimodular, and relatively complemented lattices (Abe, Reinhold, Czédli–Schmidt).

## Conditional results

There is no widely-used hard conditional ("assuming X, the conjecture holds") that drives the field, unlike Riemann-hypothesis-style conditionals elsewhere. The "conditional" texture here is rather that the entropy bound improves under stronger forms of the two-set inequality or under non-uniform sampling assumptions, and that lattice cases follow from closure properties (modularity, semimodularity) the general family need not have.

## What a full resolution requires

A complete proof must produce, for *every* finite union-closed family, an element of frequency $\ge m/2$ — with no restriction on ground-set size, number of sets, lattice structure, or generator size. The known barriers are sharp: any **averaging** proof must evade the Sarvate–Renaud examples that refute natural strengthenings; any **single-step entropy** proof cannot exceed $\frac{3-\sqrt5}{2}$; any **graph reduction** must somehow extend past generators of size $2$; and any **lattice induction** must control numerous, uncorrelated join-irreducibles. The plausible routes are (i) a *multi-step* or *non-uniform* entropy argument that breaks the $0.38$ ceiling and reaches $1/2$, (ii) a structural reduction of the general case to a settled class, or (iii) a wholly new invariant. Most current optimism sits with the entropy programme, tempered by the recognition that the gap from $0.38$ to $0.5$ has resisted the very people who found the first $0.38$.

## Related problems

- [Erdős–Straus Conjecture](../erdos-straus-conjecture/README.md)
- [Hadwiger Conjecture](../hadwiger-conjecture/README.md)
- [Sendov's Conjecture](../sendov-conjecture/README.md)
- [Singmaster's Conjecture](../singmaster-conjecture/README.md)
- [Lonely Runner Conjecture](../lonely-runner-conjecture/README.md)
