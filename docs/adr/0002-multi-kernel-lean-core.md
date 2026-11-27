# ADR 0002: Standalone Multi-Kernel Lean 4.35.0 Formal Core (Zero Mathlib)

- **Status:** Accepted
- **Date:** 2026-11-23 (amended 2026-11-26 for `v0.7.0`)
- **Deciders:** Alexander S. Donahue

## Context

Prior to `v0.3.0`, the initial directory stub contained only `ROADMAP.md` — zero machine-checked proofs existed in the repository. Meanwhile, contemporary formal-verification standards (Lean 4.35.0 multi-kernel `lake check --paranoid` and `lake comparator --paranoid`) warn against four classic failure modes in AI-assisted mathematics:
1. Single-kernel trust (a subtle kernel bug or unsound metaprogramming bypass).
2. Statement-mutation / goalpost-moving (proving a weakened theorem instead of the stated challenge).
3. Vacuous truth (`False -> P` or uninhabited domain hypotheses).
4. Heavy dependency bloat (pulling multi-gigabyte Mathlib caches breaks fast reproducible builds and slows independent kernel replayers).

## Decision

1. Establish a **zero-Mathlib, pure Lean 4.35.0 Core** formal package under `lean/` (`autoImplicit = false`, `lean/lean-toolchain` pinned to `leanprover/lean4:v4.35.0`, `lean/lake-manifest.json` committed per Palomar rules).
2. Enforce a strict **Challenge / Solution / NonVacuity / Adversarial / VerifyAxioms + Live Negative Rejection** architecture:
   - `lean/Challenge.lean`: freezes the exact headline theorem signatures (`sorry` permitted only here as specification stubs; strictly ≤ 1,000 lines and ≤ 100 KiB per Palomar limits).
   - `lean/FormalAtlas/*.lean` & `lean/Solution.lean`: prove every signature across 8 open-problem domains (Collatz, Erdős–Straus, Lonely Runner, Brocard, Primes/Twin Primes, Goldbach, Perfect/Mersenne Numbers, Ramsey Theory) with **zero `sorry`, zero `admit`, zero `native_decide`, zero custom/private `axiom`, zero `implemented_by`/`@[extern]`**.
   - `lean/NonVacuity.lean`: constructs concrete computable witnesses proving every hypothesis class is inhabited.
   - `lean/Adversarial.lean`: proves `¬ P` for deliberately false or weakened variants to defeat vacuous/degenerate definitions.
   - `lean/VerifyAxioms.lean` + `scripts/test_lean_negative.py`: prints `#print axioms` for every audited declaration strictly within `{propext, Classical.choice, Quot.sound}` (mirrored verbatim in `README.md` via `scripts/check_readme_axioms.py`) and runs a live 3-case negative kernel & axiom-gate rejection test in CI.
   - `lean/STATEMENT_FIDELITY.md`: documents definition-by-definition correspondence between textbook mathematics and Lean types.
3. Replay every exported theorem across **all 6 independent kernels** bundled in Lean 4.35.0 (`lean`, `leanchecker-paranoid`, `lean4lean`, `nanoda_bin`, `con-leche`, `con-ron`), running full `bwrap`-sandboxed `lake check --paranoid` and `lake comparator --config comparator.json --paranoid` in Ubuntu CI.

## Consequences

- **Positive:** Complete clean build + 6-kernel replay takes seconds instead of hours; zero Mathlib version-rot; cryptographically trustworthy statement-fidelity and axiom hygiene.
- **Negative / Trade-off:** Pure Lean Core restricts immediate formalization to elementary, combinatorial, and number-theoretic statements across the eight current domains. Deeper analytic or algebraic geometry problems (RH, BSD, Hodge, Navier–Stokes) will require a separate opt-in Mathlib sub-package (`lean-mathlib/`) if added in a future release.
- **Platform Note:** On Windows, Lean 4.35.0's `lake check` currently has an upstream PATH lookup bug for `git` and lacks Linux `bubblewrap`; Windows local checks invoke the 6 kernel binaries directly while Ubuntu CI enforces the full sandboxed `lake check --paranoid` and `lake comparator --paranoid` gate.
