# Status & Frontier — The 1/3–2/3 Conjecture

_Where the problem stands and what a resolution would require._

**Status: open (active progress).** The conjecture — that every finite non-chain poset $P$ has an incomparable pair $(x,y)$ with $\Pr[x\prec y]\in[\tfrac13,\tfrac23]$ over the uniform distribution on linear extensions — is unproven in general and has no known counterexample. It has stood since its 1968 root (Kislitsyn) and 1984 modern formulation (Linial).

## What is known (unconditional)

- **Universal balance constant $\approx 0.276$.** Every non-chain poset has a pair with $\Pr[x\prec y]\in\bigl[\tfrac12-\tfrac{\sqrt5}{10},\,\tfrac12+\tfrac{\sqrt5}{10}\bigr]$, i.e. balance parameter $\ge \tfrac12-\tfrac{\sqrt5}{10}\approx 0.2764$. This follows from Kahn–Saks (1991), who first proved $[\tfrac{3}{11},\tfrac{8}{11}]$, refined by Brightwell–Felsner–Trotter (1995). This is the best general bound and is **below** the target $1/3\approx 0.333$.
- **Sharp constant on key classes.** The full conjecture holds for posets of **width 2** (Linial, 1984, with the sharp golden-ratio constant), **height 2**, **semiorders**, **$N$-free** and **series–parallel** posets, and all **small posets** by computation. The width-2 extremal constant equals the universal record, which is why width-2 is the canonical tight case.
- **Algorithmic payoff settled.** Kahn–Kim (1994) give a polynomial-time comparison achieving a constant-factor reduction in the number of consistent extensions, so *sorting under partial information* needs $O(\log_2 e(P))$ comparisons; Cardinal–Fiorini–Joret–Jungers–Munro made this fully algorithmic. The conjecture's information-theoretic consequence is therefore essentially true even though the exact $1/3$ is open.

## What is known (conditional / structural)

There is no major *conditional* resolution (no "the conjecture follows from X"). The class results are unconditional but partial; the obstruction is that they exploit structure (chain decomposition, forbidden subposet, recursion) absent in a generic wide, tall, tangled poset.

## What a full resolution requires

Closing the gap from $0.2764$ to $1/3$ for **arbitrary** finite non-chain posets. The two analytic engines — Brunn–Minkowski log-concavity (Kahn–Saks) and graph/poset entropy (Kahn–Kim) — both plateau below $1/3$ and are believed structurally incapable of reaching it, because they control a single element's position distribution or an averaged quantity rather than the *worst incomparable pair* against its extremal V/Λ configuration. A proof likely needs either a sharper geometric inequality whose extremizer is exactly the conjectured tight family, a tailored entropy with the correct extremal poset, or a global structural dichotomy that handles the generic case directly. The constant $1/3$ being best possible (tight on the 3-element V-poset) means any successful method must be exact, not merely "constant-yielding."

## Plausible routes

1. **A stronger correlation/convexity inequality** sensitive to pairs, sharpening the Brunn–Minkowski step from $0.276$ to $1/3$.
2. **Resolve forests/trees** (currently a focused sub-front, Zaguia et al.) as a stepping stone, then attack general posets by decomposition.
3. **Entropy refinement** with the correct extremizer.
4. **Computer-assisted extremal analysis** to discover a new tight family that reveals the right invariant — so far none has surfaced beyond the known V/Λ gadgets.

## Related problems

- [Union-Closed Sets Conjecture](../union-closed-sets-conjecture/README.md) — another combinatorial conjecture about an unavoidable "balanced" element, recently cracked open by entropy methods.
- [Sunflower Conjecture](../sunflower-conjecture/README.md) — extremal set theory where probabilistic/entropy techniques drive progress.
- [Erdős–Hajnal Conjecture](../erdos-hajnal-conjecture/README.md) — structure-forcing in ordered/graph settings, sibling in the extremal-combinatorics program.
- [Reconstruction Conjecture](../reconstruction-conjecture/README.md) — a long-open structural conjecture verified on many classes but resistant in general, like this one.
