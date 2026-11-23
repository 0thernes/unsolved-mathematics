# Formalization Roadmap (`formal/ROADMAP.md`)

> **Status (`v0.3.0`, 2026-11-23):** Phase 1 is **complete and 6-kernel verified** in pure Lean 4.35.0 Core (zero Mathlib, zero `sorry`/`admit`/`native_decide`/custom `axiom`; axioms strictly within `{propext, Classical.choice, Quot.sound}`). See [`STATEMENT_FIDELITY.md`](STATEMENT_FIDELITY.md), [`Challenge.lean`](Challenge.lean), [`Solution.lean`](Solution.lean), [`NonVacuity.lean`](NonVacuity.lean), and [`VerifyAxioms.lean`](VerifyAxioms.lean).
>
> **Scope:** Trust infrastructure for The Unsolved Mathematics Atlas. This roadmap claims **no solution** to any open conjecture.

## Phase 1 — Completed & 6-Kernel Verified (`v0.3.0`)

### Collatz Structural Core & Obstructions ([`FormalAtlas/Collatz.lean`](FormalAtlas/Collatz.lean))
1. [x] **Shortcut map definitions** (`T`, `TMinus`, `iter`, `parityBit`, `parityWord`, `wordIntercept`) — [`FormalAtlas/Defs.lean`](FormalAtlas/Defs.lean).
2. [x] **Parity words and prefix cylinders** — `collatz_cylinder_affine_and_word`.
3. [x] **Cylinder affine law** — `thm_collatz_cylinder_affine_law`.
4. [x] **Exact affine intercept law** ($2^d T^d(x) = 3^o x + c(w)$) — `thm_collatz_exact_intercept_law`.
5. [x] **Terras parity-word bijection (1976)** — `thm_terras_parity_word_bijection`.
6. [x] **Descent certificate soundness** — `thm_collatz_descent_certificate_sound`.
7. [x] **No finite 2-adic subcritical cover via `-1`** — `thm_collatz_no_finite_subcritical_cover`.
8. [x] **Spine ladder identity (cleared denominators)** — `thm_collatz_spine_ladder_identity`.
9. [x] **Positivity localization for all supercritical words ($\rho_w \le -1$)** — `thm_collatz_positivity_localization`.
10. [x] **$\varepsilon$-Invariance / sign-blindness barrier ($3n - 1$ positive cycles at `5` and `17`)** — `thm_collatz_epsilon_invariance_barrier`.

### Multi-Problem Structural Core (`v0.3.0`)
11. [x] **Erdős–Straus Conjecture** ([`FormalAtlas/ErdosStraus.lean`](FormalAtlas/ErdosStraus.lean)): Mordell mod-840 modular reduction covering 834/840 residue classes (`99.286%`) — `thm_erdos_straus_mordell_840`.
12. [x] **Lonely Runner Conjecture** ([`FormalAtlas/LonelyRunner.lean`](FormalAtlas/LonelyRunner.lean)): All-$n$ sharpness bound $\delta \le 1/(n+1)$ and constructive base cases $n \in \{1, 2\}$ — `thm_lonely_runner_sharpness_all_n`, `thm_lonely_runner_n1`, `thm_lonely_runner_n2`.
13. [x] **Brocard's Problem** ([`FormalAtlas/Brocard.lean`](FormalAtlas/Brocard.lean)): Exact Brown-number solutions `(4,5)`, `(5,11)`, `(7,71)` and exhaustive classification for $n \le 12$ — `thm_brocard_brown_solutions`, `thm_brocard_exhaustive_le_12`.

## Phase 2 — Planned Next Targets (`v0.4.0+`)

1. [ ] **Collatz exact cycle product identity** (Böhm–Sontacchi / Steiner circuit inequalities).
2. [ ] **Continued-fraction lower-bound derivation** for nontrivial $3n+1$ cycle lengths (Eliahou 1993 / Hercher 2023).
3. [ ] **Lonely Runner $n = 3$ (4 runners)** constructive exact-rational proof in pure Lean Core.
4. [ ] **Optional Mathlib bridge package (`formal-mathlib/`):** Separate opt-in Lean sub-package (keeping `formal/` zero-Mathlib) for analytic/geometric definitions (Riemann $\zeta$ zero-free regions, Kakeya Besicovitch sets, Navier–Stokes scaling invariance).

## Non-Goals

- No formal proof of Collatz, Erdős–Straus, uniform Lonely Runner, or Brocard finiteness is implied.
- No infinite regeneration theorem is formalized.
- No stochastic or fitted-model heuristic counts as proof.

## Artifact Requirements (Enforced in CI)

Every formal artifact in `formal/` must ship with:
- Isolated theorem specification in `Challenge.lean` matching `comparator.json`;
- Zero-`sorry`, zero-`admit`, zero-`native_decide`, zero-custom-`axiom` proof in `Solution.lean`;
- Concrete non-vacuity witness in `NonVacuity.lean`;
- `#print axioms` audit in `VerifyAxioms.lean` strictly within `{propext, Classical.choice, Quot.sound}`;
- Definition-by-definition correspondence in `STATEMENT_FIDELITY.md`;
- Full `bwrap`-sandboxed 6-kernel replay (`lake check --paranoid` + `lake comparator --config comparator.json --paranoid`).
