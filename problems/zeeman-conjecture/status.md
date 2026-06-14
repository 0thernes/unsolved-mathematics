# Status & Frontier — The Zeeman Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** The Zeeman conjecture (ZC) — for every contractible compact $2$-complex $K$, the product $K \times [0,1]$ is collapsible — has been neither proved nor disproved in full generality since Zeeman posed it in 1964. No claimed proof or counterexample has been accepted by the community.

## What is known (unconditional)

- The conjecture holds on the **canonical hard cases**: the dunce hat $D$ and Bing's house with two rooms $H$, both contractible and non-collapsible, satisfy $K \times I$ collapsible.
- ZC is verified for large structured families: many **standard / special $2$-polyhedra**, $2$-complexes of bounded complexity, and complexes admitting suitable discrete Morse functions or non-positive curvature.
- The hypothesis is **sharp**: contractibility alone does not give collapsibility ($D$, $H$), so the extra interval factor is essential and cannot be dropped.
- **Reduction theorem (Gillman–Rolfsen, 1983):** the Zeeman conjecture for standard spines is equivalent to the general Zeeman conjecture, and historically was tied to the (now-proved) $3$-dimensional Poincaré conjecture.

## What is known (conditional)

- **ZC $\Rightarrow$ Poincaré$^3$** and **ZC $\Rightarrow$ Andrews–Curtis (AC)**. The first implication is now subsumed by Perelman's 2003 proof of Poincaré, so ZC is at least *consistent* with that theorem.
- The second implication is the live constraint: **ZC is logically stronger than AC**, so ZC is true only if AC is true. Equivalently, **any non–AC-trivializable balanced presentation of the trivial group refutes ZC**.

## What a full resolution requires

A **proof** would need a uniform argument producing a collapse of $K \times I$ for *arbitrary* contractible $K$ with a fixed triangulation and a single interval factor — no subdivision, no extra thickening. The existing discrete-Morse and curvature results fall short precisely because they relax one of these constraints. A **disproof** would, by the AC link, most plausibly come from establishing that a candidate presentation — chiefly the **Akbulut–Kirby presentations $AK(n)$, $n \ge 3$** — is genuinely not AC-trivializable, yielding a contractible $2$-complex whose product with $I$ does not collapse.

## Plausible routes

1. **Settle Andrews–Curtis.** A proof of AC would remove the main obstruction (necessary, not sufficient, for ZC); a disproof of AC via $AK(n)$ would likely refute ZC outright.
2. **Computational frontier.** Large-scale and reinforcement-learning search (e.g., the 2020s RL attacks on $AK(n)$) aims to trivialize or certify the resistance of the hardest presentations.
3. **Discrete Morse / metric combinatorics.** Strengthen Adiprasito–Benedetti–type collapsibility results to dispense with subdivision and curvature hypotheses for $2$-complex thickenings.
4. **Special-spine induction.** Extend the Matveev–Gillman–Rolfsen program to remove the complexity bounds.

The honest summary: ZC is confirmed everywhere it has been tested and is blocked in general by an open problem (AC) that supplies its own most credible candidate counterexamples. There is no consensus on which way it will resolve.

## Related problems

- [Andrews–Curtis Conjecture](../andrews-curtis-conjecture/README.md) — implied by Zeeman; the principal obstruction and source of candidate counterexamples.
- [Whitehead Asphericity Conjecture](../whitehead-asphericity-conjecture/README.md) — sibling problem on contractible/aspherical $2$-complexes.
- [Eilenberg–Ganea Conjecture](../eilenberg-ganea-conjecture/README.md) — adjacent question on dimensions of $2$-complexes and $K(\pi,1)$'s.
- [Smooth 4-Dimensional Poincaré Conjecture](../smooth-4d-poincare-conjecture/README.md) — the surviving open Poincaré-type problem; AC counterexamples bear on potential exotic $4$-spheres.
