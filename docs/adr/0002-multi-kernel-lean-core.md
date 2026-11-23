# ADR 0002: Standalone Multi-Kernel Lean 4.35.0 Formal Core (Zero Mathlib)

- **Status:** Accepted
- **Date:** 2026-11-23
- **Deciders:** Alexander S. Donahue

## Context

Prior to `v0.3.0`, `formal/` contained only `ROADMAP.md` — zero machine-checked proofs existed in the repository. Meanwhile, contemporary formal-verification standards (Lean 4.35.0 multi-kernel `lake check --paranoid` and `lake comparator --paranoid`) warn against three classic failure modes in AI-assisted mathematics:
1. Single-kernel trust (a subtle kernel bug or unsound metaprogramming bypass).
2. Statement-mutation / goalpost-moving (proving a weakened theorem instead of the stated challenge).
3. Vacuous truth (`False -> P` or uninhabited domain hypotheses).
4. Heavy dependency bloat (pulling multi-gigabyte Mathlib caches breaks fast reproducible builds and slows independent kernel replayers).

## Decision

1. Establish a **zero-Mathlib, pure Lean 4.35.0 Core** formal package under `formal/` (`formal/lean-toolchain` pinned to `leanprover/lean4:v4.35.0`).
2. Enforce a strict **Challenge / Solution / NonVacuity / VerifyAxioms** architecture:
   - `formal/Challenge.lean`: freezes the exact 14 theorem signatures (`sorry` permitted only here as specification stubs).
   - `formal/FormalAtlas/*.lean` & `formal/Solution.lean`: prove every signature with **zero `sorry`, zero `admit`, zero `native_decide`, zero custom `axiom`**.
   - `formal/NonVacuity.lean`: constructs 6 concrete computable witnesses proving every hypothesis class is inhabited.
   - `formal/VerifyAxioms.lean`: prints `#print axioms` for every theorem; CI fails if any axiom outside `{propext, Classical.choice, Quot.sound}` appears.
   - `formal/STATEMENT_FIDELITY.md`: documents definition-by-definition correspondence between textbook mathematics and Lean types.
3. Replay every exported theorem across **all 6 independent kernels** bundled in Lean 4.35.0 (`lean`, `leanchecker-paranoid`, `lean4lean`, `nanoda_bin`, `con-leche`, `con-ron`), running full `bwrap`-sandboxed `lake check --paranoid` and `lake comparator --config comparator.json --paranoid` in Ubuntu CI.

## Consequences

- **Positive:** Complete clean build + 6-kernel replay takes seconds instead of hours; zero Mathlib version-rot; cryptographically trustworthy statement-fidelity and axiom hygiene.
- **Negative / Trade-off:** Pure Lean Core restricts immediate formalization to elementary/combinatorial/number-theoretic statements (Collatz, Erdős–Straus, Lonely Runner, Brocard). Deeper analytic or algebraic geometry problems (RH, BSD, Hodge, Navier–Stokes) will require a separate opt-in Mathlib sub-package if added in a future release (`v0.4+`).
- **Platform Note:** On Windows, Lean 4.35.0's `lake check` currently has an upstream PATH lookup bug for `git` and lacks Linux `bubblewrap`; Windows local checks invoke the 6 kernel binaries directly while Ubuntu CI enforces the full sandboxed `lake check --paranoid` and `lake comparator --paranoid` gate.
