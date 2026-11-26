# Formalization Roadmap (`lean/ROADMAP.md`)

> **Status (`v0.6.0`, 2026-11-26):** Phases 1, 2A, 2B, and 3 are **complete and 6-kernel verified** in pure Lean 4.35.0 Core (`autoImplicit = false`, zero Mathlib, zero `sorry`/`admit`/`native_decide`/custom `axiom`; axioms strictly within `{propext, Classical.choice, Quot.sound}`). **53 headline theorems + 12 non-vacuity witnesses + 16 adversarial false-variant refutations = 81 audited declarations across 8 open-problem domains**, plus live negative kernel rejection (`scripts/test_lean_negative.py`). See [`STATEMENT_FIDELITY.md`](STATEMENT_FIDELITY.md), [`Challenge.lean`](Challenge.lean), [`Solution.lean`](Solution.lean), [`NonVacuity.lean`](NonVacuity.lean), [`Adversarial.lean`](Adversarial.lean), and [`VerifyAxioms.lean`](VerifyAxioms.lean).
>
> **Scope:** Trust infrastructure for The Unsolved Mathematics Atlas. This roadmap claims **no solution** to any open conjecture.

## Completed & 6-Kernel Verified (`v0.3.0` – `v0.6.0`)

### Domain I — Collatz Structural Core & Positive-Cycle Obstructions ([`FormalAtlas/Collatz.lean`](FormalAtlas/Collatz.lean)) — 18 Headline Theorems
1. [x] **Shortcut map definitions** (`T`, `TMinus`, `iter`, `parityBit`, `parityWord`, `wordIntercept`) — [`FormalAtlas/Defs.lean`](FormalAtlas/Defs.lean).
2. [x] **Cylinder affine law & exact intercept law** — `thm_collatz_cylinder_affine_law`, `thm_collatz_exact_intercept_law`.
3. [x] **Terras parity-word bijection (1976)** — `thm_terras_parity_word_bijection`.
4. [x] **Descent certificate soundness & no finite 2-adic subcritical cover** — `thm_collatz_descent_certificate_sound`, `thm_collatz_no_finite_subcritical_cover`.
5. [x] **Spine ladder identity & unconditional Positivity Localization ($\rho_w \le -1$)** — `thm_collatz_spine_ladder_identity`, `thm_collatz_positivity_localization`.
6. [x] **$\varepsilon$-Invariance / sign-blindness barrier ($3n - 1$ positive cycles at `5` and `17`)** — `thm_collatz_epsilon_invariance_barrier`.
7. [x] **Böhm–Sontacchi cycle equation, cocycle append, negative cycles `-5`/`-17`** (`v0.4.0`) + **zero fixed point, intercept non-negativity, word length** (`v0.5.0`).
8. [x] **Positive-cycle obstruction foundations (`v0.6.0`):** `thm_collatz_positive_cycle_has_odd_step`, `thm_collatz_positive_cycle_intercept_pos`, `thm_collatz_positive_cycle_subcritical` ($3^o < 2^d \land 2^d - 3^o \le c(w)$), and `thm_collatz_no_positive_cycle_d1` ($\forall x > 0,\ T(x) \ne x$).

### Domains II–IV — Erdős–Straus, Complete Lonely Runner ($n \le 3$) & Brocard (`v0.3.0` – `v0.6.0`) — 20 Headline Theorems
9. [x] **Erdős–Straus Conjecture** ([`FormalAtlas/ErdosStraus.lean`](FormalAtlas/ErdosStraus.lean), 5 thms): Mordell mod-840 reduction (`834/840 = 99.286%`), multiplicative closure, 6 smallest exceptional squares, cyclic symmetry, and all $2 \le n \le 30$.
10. [x] **Lonely Runner Conjecture** ([`FormalAtlas/LonelyRunner.lean`](FormalAtlas/LonelyRunner.lean), 8 thms): All-$n$ rational sharpness $\delta \le 1/(n+1)$, base cases $n \in \{1, 2\}$, symmetry group (speed scaling, period shift, time reversal), non-div-4 family, and **complete constructive `thm_lonely_runner_n3` for ALL positive integer speed triples** (`v0.6.0`, via 2-adic strong induction, quarter-shift counting, Bézout congruence, and rational nudging).
11. [x] **Brocard's Problem** ([`FormalAtlas/Brocard.lean`](FormalAtlas/Brocard.lean), 7 thms): Brown solutions `(4,5), (5,11), (7,71)`, mod-3/4/10 invariants, and exhaustive classification through $n \le 20$ ($20!+1 = 2{,}432{,}902{,}008{,}176{,}640{,}001$).

### Domains V–VIII — Primes/Twins, Goldbach, Euclid Even-Perfect & Ramsey $R(3,3)=6$, $R(3,4)=9$ (`v0.5.0` – `v0.6.0`) — 15 Headline Theorems
12. [x] **Primes & Twin Primes** ([`FormalAtlas/Primes.lean`](FormalAtlas/Primes.lean), 4 thms): Euclid's infinitude of primes, arbitrary prime gaps via $(k+1)!+2$, oddness of primes $\ge 3$, and twin-prime mod-6 rigidity ($p \equiv 5 \pmod 6$ for $p \ge 4$).
13. [x] **Goldbach's Conjecture** ([`FormalAtlas/Goldbach.lean`](FormalAtlas/Goldbach.lean), 3 thms): Exhaustive verified decomposition for all even $4 \le n \le 100$, odd binary prime-sum obstruction ($p=2 \lor q=2$), and binary Goldbach failure at $11$.
14. [x] **Odd Perfect Numbers & Mersenne Primes** ([`FormalAtlas/PerfectNumbers.lean`](FormalAtlas/PerfectNumbers.lean), 4 thms): Unconditionally exact `isqrt_spec` for all $n \in \mathbb{N}$ (`v0.6.0`), algebraic Mersenne exponent primality, first four even perfect numbers $\{6, 28, 496, 8128\}$, odd-perfect exclusion $n \le 100$, and **full Euclid's Even Perfect Number Theorem** (`thm_euclid_even_perfect`, all $p \ge 2$, `v0.6.0`).
15. [x] **Ramsey Theory** ([`FormalAtlas/Ramsey.lean`](FormalAtlas/Ramsey.lean), 4 thms): Exact first-principles determination of **$R(3,3) = 6$** (`v0.5.0`) and **$R(3,4) = 9$** (`v0.6.0`, Handshaking Lemma upper bound on $K_9$ + explicit circulant $C_8(1,4,7)$ coloring on $K_8$).
16. [x] **Non-Vacuity, Adversarial & Live Negative Rejection Suites** ([`NonVacuity.lean`](NonVacuity.lean), [`Adversarial.lean`](Adversarial.lean), `scripts/test_lean_negative.py`): 12 concrete witnesses + 16 false-variant refutations + 3 live negative kernel/axiom-gate rejections guarding every domain.

## Planned Next Targets (`v0.7.0+`)

1. [ ] **Continued-fraction & Baker-style lower bounds** for nontrivial positive $3n+1$ cycle lengths (building on `thm_collatz_positive_cycle_subcritical` toward Eliahou 1993 / Hercher 2023).
2. [ ] **Euler's converse for even perfect numbers** (every even perfect number has the form $2^{p-1}(2^p - 1)$ with $2^p - 1$ prime) and **Lonely Runner $n = 4$** constructive proof in pure Lean Core.
3. [ ] **Ramsey $R(3,5) = 14$ or $R(4,4) = 18$** (Paley graph $P_{17}$ lower bound) in pure Lean Core.
4. [ ] **Optional Mathlib bridge package (`lean-mathlib/`):** Separate opt-in Lean sub-package (keeping `lean/` zero-Mathlib) for analytic/geometric definitions (Riemann $\zeta$ zero-free regions, Kakeya Besicovitch sets, Navier–Stokes scaling invariance).

## Non-Goals

- No formal proof of Collatz, Erdős–Straus, uniform Lonely Runner, Brocard finiteness, Twin Primes, Goldbach, Odd Perfect Numbers, Mersenne Infinitude, or higher Ramsey numbers is implied.
- No infinite regeneration theorem is formalized.
- No stochastic or fitted-model heuristic counts as proof.

## Artifact Requirements (Enforced in CI)

Every formal artifact in `lean/` must ship with:
- Strict `autoImplicit = false` in `lakefile.toml`;
- Isolated theorem specification in `Challenge.lean` matching `comparator.json` ($\le 1{,}000$ lines, $\le 100$ KiB, `module` header);
- Zero-`sorry`, zero-`admit`, zero-`native_decide`, zero-custom-`axiom` proof in `Solution.lean`;
- Concrete non-vacuity witnesses in `NonVacuity.lean`, adversarial refutations in `Adversarial.lean`, and live negative kernel rejection via `scripts/test_lean_negative.py`;
- `#print axioms` audit in `VerifyAxioms.lean` strictly within `{propext, Classical.choice, Quot.sound}` and mirrored verbatim in `README.md` (`scripts/check_readme_axioms.py`);
- Definition-by-definition correspondence in `STATEMENT_FIDELITY.md`;
- Full `bwrap`-sandboxed 6-kernel replay (`lake check --paranoid` + `lake comparator --config comparator.json --paranoid`).
