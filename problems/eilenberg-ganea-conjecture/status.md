# Status & Frontier — The Eilenberg–Ganea Conjecture

_Where the problem stands and what a resolution would require._

**Status: open** (posed 1957; no resolution in either direction). The question is whether $\operatorname{cd}(G)=2 \Rightarrow \operatorname{gd}(G)=2$ for every group $G$. By the Eilenberg–Ganea theorem (for $n\ge3$) together with the general bound, $\operatorname{cd}(G)=2$ forces $\operatorname{gd}(G)\in\{2,3\}$, so a counterexample is a group with $\operatorname{cd}=2$ and $\operatorname{gd}=3$.

## What is known unconditionally

- **Boundary cases agree.** $\operatorname{cd}=\operatorname{gd}$ in dimensions $0,1$ (Stallings 1968, Swan 1969) and in all dimensions $\ge 3$ (Eilenberg–Ganea 1957). Only $\operatorname{cd}=2$ is open.
- **Large classes satisfy it.** Torsion-free one-relator groups, surface groups and $2$-dimensional Poincaré-duality groups, and all groups with $\widetilde{K}_0(\mathbb{Z}G)=0$ and trivial $D(2)$-obstruction have $\operatorname{gd}=2$ whenever $\operatorname{cd}=2$.
- **No counterexample exists in the literature.** No group has been exhibited with $\operatorname{cd}=2$ and $\operatorname{gd}=3$.

## What is known conditionally

- **Bestvina–Brady dichotomy (1997).** *At least one* of the Eilenberg–Ganea conjecture and the Whitehead asphericity conjecture is false. Hence Eilenberg–Ganea cannot be proved by any method that simultaneously establishes Whitehead asphericity; the two are logically opposed under their constructions. The natural candidate counterexamples — Bestvina–Brady groups $H_L$ with $L$ acyclic but not simply connected — have $\operatorname{cd}=2$ but are **not finitely presented**, so they do not refute the finitely-presented form of the conjecture.

## What a full resolution requires

To **prove** it: a structure theorem for $\mathbb{Z}G$-modules of projective dimension $2$ strong enough to force a stably-free relation module to be realized by an aspherical presentation $2$-complex — an affirmative answer to the $D(2)$-problem in this generality. This is the missing dimension-$2$ analogue of Stallings–Swan.

To **disprove** it: a finitely presented group $G$ with $\operatorname{cd}(G)=2$ and a proof that $\operatorname{gd}(G)=3$, i.e. that no $2$-dimensional aspherical model exists — requiring a genuine, computable obstruction to de-stabilization. By the dichotomy this would leave the Whitehead conjecture as the survivor.

## Plausible routes

1. **$D(2)$ / stable-module programme** (Johnson, Mannan): resolve the realization obstruction in $\widetilde{K}_0(\mathbb{Z}G)$ for ever-larger classes, aiming at a general theorem.
2. **Cube-complex / Morse-theory engineering**: search Bestvina–Brady-type and RAAG-subgroup constructions for a *finitely presented* $\operatorname{cd}=2$ group whose geometric dimension can be pinned to $3$.
3. **Duality and $\ell^2$ obstructions**: develop an invariant sensitive to the $\operatorname{gd}=2$ vs. $3$ distinction (current $\ell^2$-Betti and deficiency invariants are not).

The community consensus leans toward the conjecture being **true**, but with no decisive technique and the Whitehead entanglement acting as a hard structural barrier.

## Related problems

- [Whitehead Asphericity Conjecture](../whitehead-asphericity-conjecture/README.md) — logically entangled via the Bestvina–Brady dichotomy.
- [Zeeman Conjecture](../zeeman-conjecture/README.md) — collapsibility of contractible $2$-complexes, same two-dimensional homotopy circle.
- [Andrews–Curtis Conjecture](../andrews-curtis-conjecture/README.md) — presentations and transformations of balanced $2$-complexes.
- [Borel Conjecture](../borel-conjecture/README.md) — rigidity of aspherical manifolds, the higher-dimensional rigidity cousin.
- [Novikov Conjecture](../novikov-conjecture/README.md) — homotopy invariance for aspherical spaces and group (co)homology.
