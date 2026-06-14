# Attempts — The Zeeman Conjecture

_Notable attempts, near-misses, retracted proofs._

## Foundational verification on the canonical examples

Zeeman's own 1964 paper supplies the first positive evidence: the **dunce hat** $D$, contractible and famously non-collapsible, satisfies $D \times I$ collapsible. The parallel computation for **Bing's house with two rooms** $H$ established a second independent contractible, non-collapsible $2$-complex whose product with $I$ collapses. These two examples remain the reference cases against which every general method is checked; any proposed proof of ZC must specialize correctly to them.

## Special-spine and low-complexity confirmations

A sustained line of work confirmed ZC for **standard / special $2$-polyhedra** and for $2$-complexes of bounded complexity. By organizing contractible $2$-complexes via their singular graphs and true vertices, one proves the product collapses for all complexes below a complexity threshold and for families satisfying explicit local conditions. **Gillman and Rolfsen** (1983) gave an influential treatment connecting ZC to the Poincaré conjecture and verifying it for large classes, and showing that the "standard spine" version of ZC is equivalent to the general one — a genuine structural reduction rather than a full proof.

## The Andrews–Curtis link and candidate counterexamples

The most consequential development is the recognition that **ZC implies Andrews–Curtis (AC)**. This reframed the search for a counterexample: any balanced presentation of the trivial group that is *not* AC-trivializable would refute ZC. The **Akbulut–Kirby presentations** $AK(n) = \langle x,y \mid x^n = y^{n+1},\, xyx = yxy \rangle$ for $n \ge 3$ are the celebrated candidates. $AK(2)$ was eventually shown trivializable, but $AK(3)$ resisted for decades and is widely regarded as the sharpest test; extensive computer searches (genetic algorithms, breadth-first and randomized search by Miasnikov, Bowman–McCaul, Havas–Ramsay, and later large-scale and reinforcement-learning attacks) have **neither trivialized nor refuted** the hardest cases. This leaves ZC in a peculiar state: its most natural potential counterexamples are exactly the open frontier of AC.

## Discrete Morse theory near-misses

Work by **Adiprasito, Benedetti** and collaborators (2010s) proved strong collapsibility theorems — collapsibility of CAT(0) and non-positively curved complexes, and product/subdivision constructions — that come close to ZC for metrically nice complexes. These are genuine advances on *collapsibility of products*, but they do not yield ZC as stated because they generally require subdivision or curvature hypotheses absent for an arbitrary contractible $2$-complex. They are best described as adjacent theorems rather than partial proofs of ZC.

## Disputed / retracted claims

ZC has not attracted a prominent published "proof" that was later retracted in the manner of some famous conjectures; the community's caution — driven by the AC obstruction — has kept claimed full proofs rare. Periodic informal announcements of resolutions (in both directions) circulate, but **no claimed proof or disproof of the general Zeeman conjecture has gained acceptance**, and none has been verified. The honest status is that ZC is open: confirmed on every example and family tested, blocked in general by the open Andrews–Curtis conjecture, with the $AK(n)$ presentations standing as the most credible — but unresolved — candidate counterexamples.
