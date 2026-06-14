# History — The 1/3–2/3 Conjecture

_Origin, formulation, and timeline._

## Origin

The 1/3–2/3 Conjecture lives at the intersection of order theory and the theory of sorting under partial information. Fix a finite poset $P = (X, \prec)$ that is not a total order (a *chain*). A *linear extension* of $P$ is a total order on $X$ refining $\prec$; write $e(P)$ for their number. For an ordered pair $(x,y)$ of incomparable elements, let
$$
\Pr[x \prec y] = \frac{\#\{\text{linear extensions in which } x \text{ precedes } y\}}{e(P)}.
$$
A pair is **balanced** with parameter $\delta$ if $\Pr[x \prec y] \in [\delta, 1-\delta]$. The conjecture asserts that every non-chain poset contains a pair with
$$
\tfrac{1}{3} \le \Pr[x \prec y] \le \tfrac{2}{3}.
$$
The constant $1/3$ is best possible: the three-element poset with a single relation $a \prec b$ (and $c$ incomparable to both) achieves exactly $1/3$ and $2/3$ at every incomparable pair, and disjoint unions of such "V/Λ" gadgets recur as the extremal family.

**Algorithmic reading.** A balanced pair lets a comparison-based sorting algorithm query $x{:}y$ and roughly halve the number of consistent linear extensions regardless of the answer. The conjecture would imply that any partial order can be completed to a total order using close to the information-theoretic minimum $\lceil\log_2 e(P)\rceil$ of comparisons in the worst case — a clean statement about sorting with partial information.

## Formulation and reformulations

The probabilistic statement above is standard. An equivalent **information-theoretic** form bounds $\max_{x \parallel y}\min(\Pr[x\prec y], \Pr[y\prec x])$ from below by $1/3$. A **polytope** reformulation places the betweenness probabilities as coordinates of a point in the order polytope, and the Kahn–Saks attack recasts balance as a convexity/log-concavity statement about counts of linear extensions sliced by the position of an element. For width-2 posets the conjecture reduces to a statement about lattice (ballot) paths, which is how the exact constant $\tfrac{1}{2}-\tfrac{\sqrt5}{10}$ enters.

## Timeline

**1968** — Sergei S. Kislitsyn poses the problem in a Russian-language paper, framing it as a question about "finishing numbers" of partial orders; this is the historical root, long overlooked in the West.

**1976** — Michael Fredman, in work on the information-theoretic lower bound for sorting and merging, independently raises the balanced-pair question in the algorithmic setting.

**1984** — Nathan (Nati) Linial, in *The information-theoretic bound is good for merging* (SIAM J. Comput.), states the conjecture in its now-standard form, proves it for **width-2 posets** with the optimal constant $\tfrac{1}{2}-\tfrac{\sqrt5}{10}\approx 0.276$ (a golden-ratio value), and popularizes it. The conjecture is thereafter attached to Kislitsyn, Fredman, and Linial.

**1991** — Jeff Kahn and Michael Saks prove the first unconditional balance bound for *all* posets: every non-chain poset has a pair with probability in $\left[\tfrac{3}{11}, \tfrac{8}{11}\right]$, via a Brunn–Minkowski / log-concavity argument on linear-extension counts. This is the landmark breakthrough that took the constant off $0$.

**1994** — Jeff Kahn and Jeong Han Kim relate balanced pairs to the entropy of the comparability graph, yielding a polynomial-time algorithm that finds a comparison reducing the number of extensions by a constant factor.

**1995** — Graham Brightwell, Stefan Felsner, and William T. Trotter sharpen the universal constant to $\tfrac{1}{2}-\tfrac{\sqrt5}{10}\approx 0.2764$, matching Linial's width-2 value, and verify the full conjecture for several classes (height-2 posets, semiorders). This $\approx 0.276$ bound is still the best known for general posets.

**1999** — Graham Brightwell's survey *Balanced pairs in partial orders* (Discrete Math.) consolidates the field and lists the major open sub-cases.

**2000s–2010s** — The conjecture is confirmed for further classes: posets of **width 2**, **height 2**, **semiorders**, **$N$-free** and **series–parallel** posets, and small posets by exhaustive computation. Trees and forests draw sustained attention (Zaguia and collaborators), partly because the natural balanced pair is harder to pin down there.

**2018–2021** — Renewed activity on **forests** and on posets from combinatorial families; Olson–Sagan and others study the property for specific lattices and interval families. The universal constant $\approx 0.276$ remains unbeaten.

**Present frontier** — The full conjecture (constant $1/3$ for all finite non-chain posets) remains **open**. The best general lower bound on the balance parameter is still $\tfrac{1}{2}-\tfrac{\sqrt5}{10}\approx 0.2764$ from the early-1990s convex-geometry line. Closing the gap from $0.276$ to $1/3$ for arbitrary posets is the central problem.
