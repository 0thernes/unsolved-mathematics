# Formalization Roadmap (`lean/ROADMAP.md`)

> **Status (`v0.4.0`, 2026-11-25):** Phases 1 and 2A are **complete and 6-kernel verified** in pure Lean 4.35.0 Core (zero Mathlib, zero `sorry`/`admit`/`native_decide`/custom `axiom`; axioms strictly within `{propext, Classical.choice, Quot.sound}`). **22 headline theorems + 6 non-vacuity witnesses + 8 adversarial false-variant refutations = 36 audited declarations.** See [`STATEMENT_FIDELITY.md`](STATEMENT_FIDELITY.md), [`Challenge.lean`](Challenge.lean), [`Solution.lean`](Solution.lean), [`NonVacuity.lean`](NonVacuity.lean), [`Adversarial.lean`](Adversarial.lean), and [`VerifyAxioms.lean`](VerifyAxioms.lean).
>
> **Scope:** Trust infrastructure for The Unsolved Mathematics Atlas. This roadmap claims **no solution** to any open conjecture.

## Completed & 6-Kernel Verified (`v0.3.0` – `v0.4.0`)

### Collatz Structural Core & Obstructions ([`FormalAtlas/Collatz.lean`](FormalAtlas/Collatz.lean)) — 11 Headline Theorems
1. [x] **Shortcut map definitions** (`T`, `TMinus`, `iter`, `parityBit`, `parityWord`, `wordIntercept`) — [`FormalAtlas/Defs.lean`](FormalAtlas/Defs.lean).
2. [x] **Cylinder affine law** — `thm_collatz_cylinder_affine_law`.
3. [x] **Exact affine intercept law** ($2^d T^d(x) = 3^o x + c(w)$) — `thm_collatz_exact_intercept_law`.
4. [x] **Terras parity-word bijection (1976)** — `thm_terras_parity_word_bijection`.
5. [x] **Descent certificate soundness** — `thm_collatz_descent_certificate_sound`.
6. [x] **No finite 2-adic subcritical cover via `-1`** — `thm_collatz_no_finite_subcritical_cover`.
7. [x] **Spine ladder identity (cleared denominators)** — `thm_collatz_spine_ladder_identity`.
8. [x] **Positivity localization for all supercritical words ($\rho_w \le -1$)** — `thm_collatz_positivity_localization`.
9. [x] **$\varepsilon$-Invariance / sign-blindness barrier ($3n - 1$ positive cycles at `5` and `17`)** — `thm_collatz_epsilon_invariance_barrier`.
10. [x] **Böhm–Sontacchi exact cycle equation** ($(2^d - 3^o)x = c(w)$) — `thm_collatz_cycle_equation` (`v0.4.0`).
11. [x] **Parity-word composition / cocycle identity** — `thm_collatz_parity_word_append` (`v0.4.0`).
12. [x] **Non-trivial negative integer cycles of true `3n + 1` (`-5`, `-17`)** — `thm_collatz_negative_cycles` (`v0.4.0`).

### Multi-Problem Structural Core (`v0.3.0` – `v0.4.0`) — 11 Headline Theorems
13. [x] **Erdős–Straus Conjecture** ([`FormalAtlas/ErdosStraus.lean`](FormalAtlas/ErdosStraus.lean)): Mordell mod-840 reduction (834/840 classes = `99.286%`), multiplicative closure (prime reduction), and certified resolution of the 6 smallest exceptional squares $\{121, 169, 289, 361, 529, 841\}$ (`v0.4.0`).
14. [x] **Lonely Runner Conjecture** ([`FormalAtlas/LonelyRunner.lean`](FormalAtlas/LonelyRunner.lean)): All-$n$ sharpness bound $\delta \le 1/(n+1)$, base cases $n \in \{1, 2\}$, and exact rational speed-scaling invariance (`v0.4.0`).
15. [x] **Brocard's Problem** ([`FormalAtlas/Brocard.lean`](FormalAtlas/Brocard.lean)): Exact Brown-number solutions `(4,5)`, `(5,11)`, `(7,71)`, mod-4 structural constraint ($n \ge 4 \Rightarrow n!+1 \equiv 1 \pmod 4$), and exhaustive classification through $n \le 15$ (`v0.4.0`).
16. [x] **Adversarial False-Variant Suite** ([`Adversarial.lean`](Adversarial.lean)): 8 explicit negative refutation theorems guarding against vacuous hypotheses and degenerate definitions (`v0.4.0`).

## Planned Next Targets (`v0.5.0+`)

1. [ ] **Continued-fraction lower-bound derivation** for nontrivial $3n+1$ cycle lengths (Eliahou 1993 / Hercher 2023).
2. [ ] **Lonely Runner $n = 3$ (4 runners)** constructive exact-rational proof in pure Lean Core.
3. [ ] **Optional Mathlib bridge package (`lean-mathlib/`):** Separate opt-in Lean sub-package (keeping `lean/` zero-Mathlib) for analytic/geometric definitions (Riemann $\zeta$ zero-free regions, Kakeya Besicovitch sets, Navier–Stokes scaling invariance).

## Non-Goals

- No formal proof of Collatz, Erdős–Straus, uniform Lonely Runner, or Brocard finiteness is implied.
- No infinite regeneration theorem is formalized.
- No stochastic or fitted-model heuristic counts as proof.

## Artifact Requirements (Enforced in CI)

Every formal artifact in `lean/` must ship with:
- Isolated theorem specification in `Challenge.lean` matching `comparator.json` (≤ 1,000 lines, ≤ 100 KiB, `module` header);
- Zero-`sorry`, zero-`admit`, zero-`native_decide`, zero-custom-`axiom` proof in `Solution.lean`;
- Concrete non-vacuity witnesses in `NonVacuity.lean` and adversarial refutations in `Adversarial.lean`;
- `#print axioms` audit in `VerifyAxioms.lean` strictly within `{propext, Classical.choice, Quot.sound}` and mirrored verbatim in `README.md` (`scripts/check_readme_axioms.py`);
- Definition-by-definition correspondence in `STATEMENT_FIDELITY.md`;
- Full `bwrap`-sandboxed 6-kernel replay (`lake check --paranoid` + `lake comparator --config comparator.json --paranoid`).
