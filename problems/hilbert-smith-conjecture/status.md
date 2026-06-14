# Status & Frontier — The Hilbert–Smith Conjecture

_Where the problem stands and what a resolution would require._

**Status: active progress, open in general.** The conjecture is established in several important regimes but remains open for arbitrary topological actions in dimension four and above. The sharp form under attack is:

> No $p$-adic integer group $\mathbb{Z}_p = \varprojlim \mathbb{Z}/p^n$ acts effectively by homeomorphisms on a connected topological manifold $M^n$.

By the Gleason–Montgomery–Zippin–Yamabe solution of Hilbert's fifth problem (1952–53), this $p$-adic statement is equivalent to the full conjecture that a locally compact group acting effectively on a connected manifold is a Lie group.

## What is known (unconditional)

- **Dimension 2:** True. No $\mathbb{Z}_p$-action on a surface.
- **Dimension 3:** True — **John Pardon**, _"The Hilbert–Smith conjecture for three-manifolds,"_ J. Amer. Math. Soc. (2013), arXiv:1112.2324. This is the strongest recent unconditional advance and the current high-water mark.
- **Smooth / real-analytic actions, all dimensions:** True classically (Bochner–Montgomery, Montgomery–Zippin): a compact group acting smoothly and effectively on a manifold is a Lie group.
- **Lipschitz and quasiconformal actions, all dimensions:** True — **Repovš–Ščepin** (1997) for Lipschitz actions on Riemannian manifolds; **Martin** for quasiconformal actions. These are full-dimension theorems but require regularity strictly stronger than continuity.

## What is known (conditional / partial)

- **Yang's dimension theory** shows any hypothetical effective $\mathbb{Z}_p$-action on $M^n$ would make the orbit space $M/\mathbb{Z}_p$ have cohomological dimension $n+2$ — a constraint sufficient to derive contradictions in low dimensions but not (yet) for $n\geq 4$.
- Various Hölder-regularity refinements of the Repovš–Ščepin method narrow the gap between Lipschitz and continuous actions without closing it.

## What a full resolution would require

A proof of the general case must convert the finite-stage obstructions (Newman's theorem, Smith theory, Yang's dimension estimates), each valid for the cyclic quotients $\mathbb{Z}/p^n$, into a contradiction that survives the **inverse limit** defining $\mathbb{Z}_p$ — and it must do so using genuine manifold structure (local Euclidean geometry, Poincaré duality) rather than any imposed metric regularity, since Dranishnikov-type dimension-raising maps show that pure dimension theory permits the pathology in general. Concretely, one needs either (i) a high-dimensional analogue of Pardon's $L^2$/cohomological-rigidity argument that no longer relies on a dimension coincidence special to $n=3$, or (ii) a way to manufacture, from a topological action, enough metric control to invoke the Repovš–Ščepin estimates.

## Plausible routes

1. **Extend Pardon's analytic method beyond $n=3$**, replacing the three-manifold cohomological coincidence with a duality-based estimate valid in all dimensions — currently the most-watched direction.
2. **Lower the regularity in the Repovš–Ščepin program** from Lipschitz/Hölder toward continuous, perhaps by averaging or smoothing a topological action into a controlled one.
3. **Sharpen cohomological dimension theory of $p$-adic quotients** to show $\dim(M/\mathbb{Z}_p)=n+2$ is incompatible with $M$ being a manifold for all $n$.

## Related problems

- [Hilbert's Sixteenth Problem](../hilbert-sixteenth-problem/README.md) — another still-open fragment of Hilbert's 1900 list.
- [Novikov Conjecture](../novikov-conjecture/README.md) — large-scale topology of manifolds and group actions.
- [Baum–Connes Conjecture](../baum-connes-conjecture/README.md) — actions of groups and the $K$-theory of their operator algebras.
- [Whitehead Asphericity Conjecture](../whitehead-asphericity-conjecture/README.md) — a deep open problem in geometric/algebraic topology.
