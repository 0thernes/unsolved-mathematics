# Status & Frontier — The Andrews–Curtis Conjecture

_Where the problem stands and what a resolution would require._

**Status: open (active progress).** As of mid-2026 the Andrews–Curtis Conjecture is unresolved in both its **simple** form (AC', fixed generator count) and its **stable** form (with allowed stabilizations). There is no accepted proof and no accepted counterexample. What has changed over the last decade is not the truth value but the evidence base: a long parade of suspected counterexamples has been computationally trivialized, while a hardness theorem has shown that this evidence cannot, by itself, settle anything.

### What is known (unconditional)

- **The reformulation is exact.** AC is equivalent to the statement that every contractible finite $2$-complex $3$-deforms to a point; equivalently, every balanced presentation of $\{1\}$ is AC-reducible to the trivial presentation. This ties AC to the Zeeman conjecture and to simple-homotopy theory.
- **All sufficiently short balanced presentations of $\{1\}$ are AC-trivial**, verified by exhaustive search. Small cases offer no counterexample.
- **$AK(2)$ is AC-trivial.** The decades-long flagship candidate $\langle x,y\mid x^2=y^3,\,xyx=yxy\rangle$ was explicitly trivialized by large-scale search (Panteleev–Ushakov, 2019), overturning the prior expectation that it was a counterexample.
- **Large portions of the Miller–Schupp family are AC-trivial**, with reinforcement-learning agents (Shehper, Halverson, et al., 2024) extending the trivialized range well beyond classical search.
- **Hardness (Bridson).** There exist AC-trivial balanced presentations whose every trivialization passes through relators of non-elementary (tower-type) length. Consequently a finite failed search can never certify a counterexample.

### What is known (conditional / structural)

No deep conditional theorems of the form "if $X$ then AC" carry the field; the principal structural fact is negative — **no invariant is known that separates any balanced presentation of $\{1\}$ from the trivial one.** Standard invariants (abelianization, Euler characteristic, relevant torsion) vanish identically on this class, which is exactly why a counterexample, if it exists, would be so hard to recognize.

### What a full resolution would require

A **proof** would need a uniform reduction algorithm — or a non-constructive argument — guaranteeing that *every* balanced presentation of $\{1\}$ reduces to trivial under AC-moves, robust against Bridson's length explosion (so it cannot merely be a smarter search). A **disproof** would require either (i) an explicit balanced presentation of $\{1\}$ together with an invariant or rigorous combinatorial argument proving no AC-move sequence trivializes it, or (ii) a topological construction of a contractible $2$-complex that provably does not $3$-deform to a point. Note that the simple and stable conjectures could have different answers: a stabilization-allowing proof would not settle AC', and a counterexample to AC' might still be stably trivial.

### Plausible routes

1. **Resolve $AK(3)$** $\langle x,y\mid x^3=y^4,\,xyx=yxy\rangle$ — the canonical open test case — either by trivialization (further evidence for AC) or by a non-triviality obstruction (a counterexample).
2. **Find a separating invariant**, perhaps from representation/character varieties, $\pi_2$-module structure, or $K$-theoretic data, that is provably AC-invariant and non-trivial on some candidate.
3. **Topological resolution of Zeeman-type questions** that forces, or refutes, $3$-deformability for the relevant contractible complexes.
4. **AI-assisted discovery** of either very long trivializations (confirming AC on new families) or, conversely, structural patterns suggesting genuine irreducibility.

### Related problems

- [Poincaré-adjacent geometric questions — Hilbert's 16th Problem](../hilbert-sixteenth-problem/README.md)
- [Jacobian Conjecture](../jacobian-conjecture/README.md)
- [Invariant Subspace Problem](../invariant-subspace-problem/README.md)
- [P versus NP](../p-versus-np/README.md)
- [Hadwiger Conjecture](../hadwiger-conjecture/README.md)
