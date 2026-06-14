# Attempts — The Eilenberg–Ganea Conjecture

_Notable attempts, near-misses, retracted proofs._

## Settling the neighbouring dimensions (the near-misses that worked)

The conjecture survives only because of how cleanly its neighbours fell.

- **Dimensions $\ge 3$ (1957).** Eilenberg and Ganea themselves proved $\operatorname{cd}(G)=n \Rightarrow \operatorname{gd}(G)=n$ for $n\ge 3$ by explicit cell attachment. This is the "$+1$ slack" theorem: above dimension $2$ there is enough room to kill higher homotopy without raising dimension. The same argument visibly fails at $n=2$.
- **Dimension $1$ (Stallings 1968, Swan 1969).** Stallings proved every finitely generated group of cohomological dimension $1$ is free; Swan removed finite generation. Hence $\operatorname{cd}(G)=1 \iff \operatorname{gd}(G)=1$. This is the strongest evidence *for* Eilenberg–Ganea: both boundary cases that have been resolved show no gap. It is also a warning — the dimension-$1$ proof needs Stallings' ends-of-groups theorem, with no dimension-$2$ analogue.

## The Bestvina–Brady dichotomy (1997)

The single most consequential partial result. Using Morse theory on cube complexes, Bestvina and Brady constructed groups $H_L$ with prescribed finiteness properties. They proved:

> Not both the Eilenberg–Ganea conjecture and the Whitehead asphericity conjecture can be true.

This is a genuine theorem, not a counterexample: it relocates the difficulty. Their $H_L$ for $L$ acyclic-but-not-simply-connected has $\operatorname{cd}=2$ and is $\mathrm{FP}_2$ but **not finitely presented**, so it does not by itself refute the finitely-presented form of Eilenberg–Ganea. The near-miss is that one of two famous conjectures must fall here, yet the construction does not tell us which, and does not produce a finitely presented witness.

## Verifications on broad classes (genuine partial results)

- **One-relator groups.** Torsion-free one-relator groups have aspherical presentation $2$-complexes (Lyndon, building on the Identity Theorem), so $\operatorname{gd}=2$ whenever $\operatorname{cd}=2$; Eilenberg–Ganea holds for them.
- **Surface and $\mathrm{PD}_2$ groups.** Two-dimensional Poincaré-duality groups are surface groups (Eckmann–Müller–Linnell and related work), realized by surfaces, hence $\operatorname{gd}=2$.
- **$F.E.A.\ Johnson's $D(2)$ programme.** Johnson reformulated the problem via the $D(2)$-property and verified it for many groups, tying Eilenberg–Ganea to concrete module-theoretic computations over $\mathbb{Z}G$. No counterexample emerged, but no general theorem either.

## Disputed and folkloric claims

- **Occasional claimed proofs.** Over the decades several manuscripts and preprints have claimed to settle Eilenberg–Ganea (in one direction or the other), typically by asserting that a stably-free relation module can always be de-stabilized to a free one, or by proposing a specific Bestvina–Brady group as a finitely-presented counterexample. None has been accepted by the community. The standard objection is uniform: the proposed free-replacement step is exactly the $D(2)$-realization problem, which is *not* known to hold in general, so such arguments assume what must be proved. We record these neutrally — no widely circulated claim has survived refereeing, and the problem is universally regarded as open.
- **The Whitehead-conjecture entanglement.** Because of the Bestvina–Brady dichotomy, a "proof" of Eilenberg–Ganea would, if correct, force a disproof of the Whitehead asphericity conjecture (or vice versa). Any claimed resolution that does not engage this entanglement is treated with immediate skepticism.

## Status of the attempts

Every verified case shares one feature: the relation module is provably free and the presentation $2$-complex is provably aspherical. Every counterexample candidate fails finite presentability or stalls at computing the exact geometric dimension. The two obstructions are the two horns of the Bestvina–Brady dichotomy, which is why six decades of attempts have produced rich partial results but no resolution.
