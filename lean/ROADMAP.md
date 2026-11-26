# Formalization Roadmap (`lean/ROADMAP.md`)

> **Status (`v0.5.0`, 2026-11-25):** Phases 1, 2A, and 2B are **complete and 6-kernel verified** in pure Lean 4.35.0 Core (zero Mathlib, zero `sorry`/`admit`/`native_decide`/custom `axiom`; axioms strictly within `{propext, Classical.choice, Quot.sound}`). **45 headline theorems + 10 non-vacuity witnesses + 14 adversarial false-variant refutations = 69 audited declarations across 8 open-problem domains.** See [`STATEMENT_FIDELITY.md`](STATEMENT_FIDELITY.md), [`Challenge.lean`](Challenge.lean), [`Solution.lean`](Solution.lean), [`NonVacuity.lean`](NonVacuity.lean), [`Adversarial.lean`](Adversarial.lean), and [`VerifyAxioms.lean`](VerifyAxioms.lean).
>
> **Scope:** Trust infrastructure for The Unsolved Mathematics Atlas. This roadmap claims **no solution** to any open conjecture.

## Completed & 6-Kernel Verified (`v0.3.0` – `v0.5.0`)

### Domain I — Collatz Structural Core & Obstructions ([`FormalAtlas/Collatz.lean`](FormalAtlas/Collatz.lean)) — 14 Headline Theorems
1. [x] **Shortcut map definitions** (`T`, `TMinus`, `iter`, `parityBit`, `parityWord`, `wordIntercept`) — [`FormalAtlas/Defs.lean`](FormalAtlas/Defs.lean).
2. [x] **Cylinder affine law & exact intercept law** — `thm_collatz_cylinder_affine_law`, `thm_collatz_exact_intercept_law`.
3. [x] **Terras parity-word bijection (1976)** — `thm_terras_parity_word_bijection`.
4. [x] **Descent certificate soundness & no finite 2-adic subcritical cover** — `thm_collatz_descent_certificate_sound`, `thm_collatz_no_finite_subcritical_cover`.
5. [x] **Spine ladder identity & unconditional Positivity Localization ($\rho_w \le -1$)** — `thm_collatz_spine_ladder_identity`, `thm_collatz_positivity_localization`.
6. [x] **$\varepsilon$-Invariance / sign-blindness barrier ($3n - 1$ positive cycles at `5` and `17`)** — `thm_collatz_epsilon_invariance_barrier`.
7. [x] **Böhm–Sontacchi cycle equation, cocycle append, negative cycles `-5`/`-17`** (`v0.4.0`) + **zero fixed point, intercept non-negativity, word length** (`v0.5.0`).

### Domains II–IV — Erdős–Straus, Lonely Runner & Brocard (`v0.3.0` – `v0.5.0`) — 19 Headline Theorems
8. [x] **Erdős–Straus Conjecture** ([`FormalAtlas/ErdosStraus.lean`](FormalAtlas/ErdosStraus.lean), 5 thms): Mordell mod-840 reduction (`834/840 = 99.286%`), multiplicative closure, 6 smallest exceptional squares, cyclic symmetry (`v0.5.0`), and all $2 \le n \le 30$ (`v0.5.0`).
9. [x] **Lonely Runner Conjecture** ([`FormalAtlas/LonelyRunner.lean`](FormalAtlas/LonelyRunner.lean), 7 thms): All-$n$ rational sharpness $\delta \le 1/(n+1)$, base cases $n \in \{1, 2\}$, symmetry group (speed scaling, period shift, time reversal), and $n = 3$ (4 runners) for all triples with $4 \nmid v_i$ (`v0.5.0`).
10. [x] **Brocard's Problem** ([`FormalAtlas/Brocard.lean`](FormalAtlas/Brocard.lean), 7 thms): Brown solutions `(4,5), (5,11), (7,71)`, mod-3/4/10 invariants, and exhaustive classification through $n \le 20$ ($20!+1 = 2{,}432{,}902{,}008{,}176{,}640{,}001$, `v0.5.0`).

### Domains V–VIII — Primes/Twins, Goldbach, Perfect/Mersenne & Ramsey $R(3,3)=6$ (`v0.5.0`) — 12 Headline Theorems
11. [x] **Primes & Twin Primes** ([`FormalAtlas/Primes.lean`](FormalAtlas/Primes.lean), 4 thms): Euclid's infinitude of primes, arbitrary prime gaps via $(k+1)!+2$, oddness of primes $\ge 3$, and twin-prime mod-6 rigidity ($p \equiv 5 \pmod 6$ for $p \ge 4$).
12. [x] **Goldbach's Conjecture** ([`FormalAtlas/Goldbach.lean`](FormalAtlas/Goldbach.lean), 3 thms): Exhaustive verified decomposition for all even $4 \le n \le 100$, odd binary prime-sum obstruction ($p=2 \lor q=2$), and binary Goldbach failure at $11$.
13. [x] **Odd Perfect Numbers & Mersenne Primes** ([`FormalAtlas/PerfectNumbers.lean`](FormalAtlas/PerfectNumbers.lean), 3 thms): Pure algebraic proof of Mersenne exponent primality ($2^a - 1 \mid 2^{ab} - 1$), first four even perfect numbers $\{6, 28, 496, 8128\}$, and exhaustive odd-perfect exclusion $n \le 100$.
14. [x] **Ramsey Theory** ([`FormalAtlas/Ramsey.lean`](FormalAtlas/Ramsey.lean), 2 thms): Exact first-principles determination of $R(3,3) = 6$ (upper bound on $K_6$ + explicit $C_5$ lower-bound coloring on $K_5$).
15. [x] **Non-Vacuity & Adversarial Refutation Suites** ([`NonVacuity.lean`](NonVacuity.lean), [`Adversarial.lean`](Adversarial.lean)): 10 concrete witnesses + 14 false-variant refutations guarding every domain against vacuous hypotheses and broken definitions.

## Planned Next Targets (`v0.6.0+`)

1. [ ] **Continued-fraction lower-bound derivation** for nontrivial $3n+1$ cycle lengths (Eliahou 1993 / Hercher 2023).
2. [ ] **Full Lonely Runner $n = 3$ (all integer speed triples)** constructive exact-rational proof in pure Lean Core (extending `thm_lonely_runner_n3_nondiv4` via 2-adic reduction).
3. [ ] **Ramsey $R(3,4) = 9$ and Euler's even-perfect characterization** in pure Lean Core.
4. [ ] **Optional Mathlib bridge package (`lean-mathlib/`):** Separate opt-in Lean sub-package (keeping `lean/` zero-Mathlib) for analytic/geometric definitions (Riemann $\zeta$ zero-free regions, Kakeya Besicovitch sets, Navier–Stokes scaling invariance).

## Non-Goals

- No formal proof of Collatz, Erdős–Straus, uniform Lonely Runner, Brocard finiteness, Twin Primes, Goldbach, Odd Perfect Numbers, Mersenne Infinitude, or higher Ramsey numbers is implied.
- No infinite regeneration theorem is formalized.
- No stochastic or fitted-model heuristic counts as proof.

## Artifact Requirements (Enforced in CI)

Every formal artifact in `lean/` must ship with:
- Isolated theorem specification in `Challenge.lean` matching `comparator.json` ($\le 1{,}000$ lines, $\le 100$ KiB, `module` header);
- Zero-`sorry`, zero-`admit`, zero-`native_decide`, zero-custom-`axiom` proof in `Solution.lean`;
- Concrete non-vacuity witnesses in `NonVacuity.lean` and adversarial refutations in `Adversarial.lean`;
- `#print axioms` audit in `VerifyAxioms.lean` strictly within `{propext, Classical.choice, Quot.sound}` and mirrored verbatim in `README.md` (`scripts/check_readme_axioms.py`);
- Definition-by-definition correspondence in `STATEMENT_FIDELITY.md`;
- Full `bwrap`-sandboxed 6-kernel replay (`lake check --paranoid` + `lake comparator --config comparator.json --paranoid`).
