# Redirect: `formal/` → `lean/`

As of `v0.4.0` (`2026-11-25`), the standalone Lean 4.35.0 6-kernel formal verification
package moved from `formal/` to **[`lean/`](../lean/)** to align with Build Standard
`v1.2.0` (`B22`) and sibling `0thernes` research repositories.

- Formal package overview & roadmap: [`lean/ROADMAP.md`](../lean/ROADMAP.md)
- Statement fidelity audit & verbatim axioms: [`lean/STATEMENT_FIDELITY.md`](../lean/STATEMENT_FIDELITY.md)
- Isolated theorem specification (`lake comparator`): [`lean/Challenge.lean`](../lean/Challenge.lean)
- Zero-sorry proofs: [`lean/Solution.lean`](../lean/Solution.lean)
- Non-vacuity witnesses: [`lean/NonVacuity.lean`](../lean/NonVacuity.lean)
- Adversarial false-variant refutations: [`lean/Adversarial.lean`](../lean/Adversarial.lean)
