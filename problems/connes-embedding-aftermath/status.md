# Status & Frontier — The Connes Embedding Problem (Resolved 2020)

_Where the problem stands and what a resolution would require._

## Resolved — negatively

The Connes Embedding Problem is **settled in the negative**. The resolving result is:

> Z. Ji, A. Natarajan, T. Vidick, J. Wright, H. Yuen, **"MIP\* = RE"**, 2020, **arXiv:2001.04383**.

By proving that the entangled-multiprover complexity class $\mathrm{MIP}^*$ equals $\mathrm{RE}$ (the recursively enumerable languages), the authors force the quantum tensor and quantum commuting correlation sets to differ, $C_{qa} \neq C_{qc}$. Via the equivalences of Tsirelson's problem (Junge–Navascués–Palazuelos–Pérez-García–Scholz–Werner 2011; Fritz 2011) and Kirchberg's QWEP reformulation (1993), this refutes the QWEP conjecture and, with it, CEP: **there exists a separable type II$_1$ factor that does not embed into any ultrapower $R^\omega$ of the hyperfinite factor.** Equivalently, **not every countable group is hyperlinear.** The result has been scrutinized by multiple expert groups and is accepted; it was honored across operator algebras, quantum information, and complexity theory.

## What is known (unconditional)

- $C_{qa} \neq C_{qc}$, and the gap is *robust* (it survives quantitative perturbation), not a boundary artifact.
- The universal/existential theory of II$_1$ factors is, as a consequence, complicated: $\mathrm{Th}(R^\omega)$ is **not computable** (Goldbring–Hart), so $R$ is not "co-r.e. axiomatizable" in continuous logic.
- Non-embeddable factors **exist** and non-hyperlinear groups **exist** — by an indirect, complexity-theoretic existence proof.

## What remains open (the live frontier)

The negative answer is *non-constructive in the witness*. The genuine open problems of the aftermath are:

1. **Explicit witness.** Exhibit a concrete, finitely presented group that is provably **not hyperlinear**, or a finitely describable II$_1$ factor that does not embed in $R^\omega$. None is known.
2. **Effective/quantitative non-embeddability.** Quantify *how badly* embedding fails — bounds on the correlation gap, on game sizes, or on moment-matching error.
3. **Soficity (open, related).** Whether every group is **sofic** remains *open*; soficity implies hyperlinearity, so a non-hyperlinear group would also be non-sofic — making the explicit-witness question a route to settling the sofic question too.
4. **Residual QWEP refinements.** Which $C^*$-algebras retain weak-expectation-type properties, now that the global conjecture is false.
5. **Logic of $R^\omega$.** Decidability fragments, model-theoretic stability, and the structure of the universal theory of tracial von Neumann algebras.

A full "resolution" of the *aftermath* would mean a constructive non-hyperlinear group or an effective separating correlation — converting the existence theorem into an exhibit. Plausible routes: derandomizing / making the MIP* construction explicit; group-theoretic constructions à la Slofstra pushed to non-hyperlinearity; or new free-probability/model-theoretic obstructions.

## Related problems

- [P versus NP](../p-versus-np/README.md) — the complexity-class framework ($\mathrm{MIP}^*=\mathrm{RE}$) that resolved CEP lives in this world.
- [Invariant Subspace Problem](../invariant-subspace-problem/README.md) — sibling deep open question in operator theory / functional analysis.
- [Andrews–Curtis Conjecture](../andrews-curtis-conjecture/README.md) — combinatorial group theory, akin to the explicit-group constructions sought for non-hyperlinearity.
- [Riemann Hypothesis](../riemann-hypothesis/README.md) — a benchmark "long-open" problem against which CEP's resolution is often contrasted.
