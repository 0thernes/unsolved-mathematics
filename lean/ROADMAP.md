# Formalization Roadmap (`lean/ROADMAP.md`)

> **Status (`v0.10.0`, 2026-11-27):** Phases 1, 2A, 2B, 3, and 4 are **complete and 6-kernel verified** in pure Lean 4.35.0 Core (`autoImplicit = false`, commit `eb6cafb7290e8bd5f2937522d8d804f58f02bafc`, zero Mathlib, zero `sorry`/`admit`/`native_decide`/custom `axiom` in all proof modules — `Challenge.lean` intentionally holds the 74 `sorry`-stated comparator specifications; axioms strictly within `{propext, Classical.choice, Quot.sound}`). **74 headline theorems + 20 non-vacuity witnesses + 24 adversarial false-variant refutations = 118 audited declarations across 8 open-problem domains** (16 zero-axiom), plus live negative kernel rejection (`scripts/test_lean_negative.py`). See [`STATEMENT_FIDELITY.md`](STATEMENT_FIDELITY.md), [`Challenge.lean`](Challenge.lean), [`Solution.lean`](Solution.lean), [`NonVacuity.lean`](NonVacuity.lean), [`Adversarial.lean`](Adversarial.lean), and [`VerifyAxioms.lean`](VerifyAxioms.lean).
>
> **Scope:** Trust infrastructure for The Unsolved Mathematics Atlas. This roadmap claims **no solution** to any open conjecture.

## Completed & 6-Kernel Verified (`v0.3.0` – `v0.10.0`)

### Domain I — Collatz Structural Core, Fine–Wilf 2-Adic Ceilings, Chiral/3-Adic Laws & Cycle Obstructions ([`FormalAtlas/Collatz.lean`](FormalAtlas/Collatz.lean)) — 36 Headline Theorems
1. [x] **Shortcut map & 2-adic definitions** (`T`, `TMinus`, `iter`, `parityBit`, `parityWord`, `wordIntercept`, `periodicBit`, `periodicPrefix`, `spineDenom`, `catCollatzStep`) — [`FormalAtlas/Defs.lean`](FormalAtlas/Defs.lean).
2. [x] **Cylinder affine law & exact intercept law** — `thm_collatz_cylinder_affine_law`, `thm_collatz_exact_intercept_law`.
3. [x] **Terras parity-word bijection (1976)** — `thm_terras_parity_word_bijection`.
4. [x] **Descent certificate soundness & no finite 2-adic subcritical cover** — `thm_collatz_descent_certificate_sound`, `thm_collatz_no_finite_subcritical_cover`.
5. [x] **Spine ladder identity & unconditional Positivity Localization ($\rho_w \le -1$)** — `thm_collatz_spine_ladder_identity`, `thm_collatz_positivity_localization`.
6. [x] **$3n - 1$ sibling-map comparison (same Terras bijection + positive cycles at `5` and `17`; heuristic reading, not a formal barrier theorem)** — `thm_collatz_epsilon_invariance_barrier`.
7. [x] **Böhm–Sontacchi cycle equation, cocycle append, negative cycles `-5`/`-17`** (`v0.4.0`) + **zero fixed point, intercept non-negativity, word length** (`v0.5.0`).
8. [x] **Positive-cycle obstruction foundations (`v0.6.0`):** `thm_collatz_positive_cycle_has_odd_step`, `thm_collatz_positive_cycle_intercept_pos`, `thm_collatz_positive_cycle_subcritical` ($3^o < 2^d \land 2^d - 3^o \le c(w)$), and `thm_collatz_no_positive_cycle_d1` ($\forall x > 0,\ T(x) \ne x$).
9. [x] **Unconditional 1- & 2-Odd-Step Positive-Cycle Exclusion for ALL $d \ge 1$ (`v0.7.0`):** `thm_collatz_positive_cycle_one_odd` and `thm_collatz_positive_cycle_two_odd` (proving $x \in \{1, 2\}$ for every positive cycle with $o \in \{1, 2\}$ of ANY period $d \ge 1$).
10. [x] **2-Adic Isometry, Odd-Unit-Lock Valuation Isometry & Unconditional Fine–Wilf Spine Ceiling (`v0.7.0`):** `thm_collatz_2adic_isometry`, `thm_collatz_periodic_spine_congruence`, `thm_collatz_odd_unit_lock_valuation_isometry` ($v_2(\rho_w - \rho_v) = \operatorname{lcp}(w^\infty, v^\infty)$), and `thm_collatz_fine_wilf_spine_ceiling` ($v_2(\rho_w - \rho_v) < |w| + |v| - \gcd(|w|, |v|)$ via first-principles Fine–Wilf periodicity theorem).
11. [x] **Exhaustive $d \le 7$ Positive-Cycle Classification & Catalytic Reversible Cylinder (`v0.7.0`):** `thm_collatz_trivial_cycle_orbit`, `thm_collatz_no_nontrivial_positive_cycle_le_7`, `thm_collatz_no_positive_cycle_odd_le_7`, and `thm_collatz_catalytic_reversible_cylinder`.
12. [x] **Unconditional 3-Odd-Step Exclusion, Sharp Intercept Ceiling & Global Eliahou–Steiner Cycle Amplitude Bound (`v0.9.0`):** `thm_collatz_positive_cycle_three_odd` ($o = 3 \implies d = 6 \land x \in \{1, 2\}$ for ALL $d \ge 1$), `thm_collatz_intercept_upper_bound` ($c(w) \le 2^{|w|-o}(3^o - 2^o)$ sharp $\forall w$), and `thm_collatz_cycle_amplitude_ceiling` ($(2^d - 3^o)x \le 2^{d-o}(3^o - 2^o)$ for ALL positive cycles).
13. [x] **Chiral Sign Conjugacy, Mod-3 Chiral Asymmetry, Global 3-Adic Cycle Exclusion & Unconditional 4-Odd-Step Exclusion (`v0.10.0`):** `thm_collatz_sign_conjugacy` ($T^d(-x) = -T_-^d(x)$), `thm_collatz_mod3_chiral_asymmetry` ($T(\text{odd}) \equiv 2, T_-(\text{odd}) \equiv 1 \pmod 3$), `thm_collatz_intercept_not_div3` ($3 \nmid c(w)$), `thm_collatz_cycle_no_div3` ($3 \nmid x$ on ALL nonzero cycles), and `thm_collatz_positive_cycle_four_odd` ($o = 4 \implies d = 8 \land x \in \{1, 2\}$ for ALL $d \ge 1$).

### Domains II–IV — Erdős–Straus, Complete Lonely Runner ($n \le 3$) & Brocard (`v0.3.0` – `v0.6.0`) — 20 Headline Theorems
12. [x] **Erdős–Straus Conjecture** ([`FormalAtlas/ErdosStraus.lean`](FormalAtlas/ErdosStraus.lean), 5 thms): Mordell mod-840 reduction (`834/840 = 99.286%`), multiplicative closure, 6 smallest exceptional squares, cyclic symmetry, and all $2 \le n \le 30$.
13. [x] **Lonely Runner Conjecture** ([`FormalAtlas/LonelyRunner.lean`](FormalAtlas/LonelyRunner.lean), 8 thms): All-$n$ rational sharpness $\delta \le 1/(n+1)$, base cases $n \in \{1, 2\}$, symmetry group (speed scaling, period shift, time reversal), non-div-4 family, and **complete constructive `thm_lonely_runner_n3` for ALL positive integer speed triples** (`v0.6.0`).
14. [x] **Brocard's Problem** ([`FormalAtlas/Brocard.lean`](FormalAtlas/Brocard.lean), 7 thms): Brown solutions `(4,5), (5,11), (7,71)`, mod-3/4/10 invariants, and exhaustive classification through $n \le 20$ ($20!+1 = 2{,}432{,}902{,}008{,}176{,}640{,}001$).

### Domains V–VIII — Primes/Twins, Goldbach, Complete Euclid–Euler / Mersenne & Ramsey $R(3,3)=6$, $R(3,4)=9$ (`v0.5.0` – `v0.7.0`) — 18 Headline Theorems
15. [x] **Primes & Twin Primes** ([`FormalAtlas/Primes.lean`](FormalAtlas/Primes.lean), 4 thms): Euclid's infinitude of primes, arbitrary prime gaps via $(k+1)!+2$, oddness of primes $\ge 3$, and twin-prime mod-6 rigidity ($p \equiv 5 \pmod 6$ for $p \ge 4$).
16. [x] **Goldbach's Conjecture** ([`FormalAtlas/Goldbach.lean`](FormalAtlas/Goldbach.lean), 3 thms): Exhaustive verified decomposition for all even $4 \le n \le 100$, odd binary prime-sum obstruction ($p=2 \lor q=2$), and binary Goldbach failure at $11$.
17. [x] **Odd Perfect Numbers & Mersenne Primes** ([`FormalAtlas/PerfectNumbers.lean`](FormalAtlas/PerfectNumbers.lean), 7 thms): Unconditionally exact `isqrt_spec` and `divSum_eq_divSumLin`, algebraic Mersenne exponent primality, $\{6, 28, 496, 8128\}$, odd-perfect exclusion $n \le 100$, **Euclid's Even Perfect Theorem** (`v0.6.0`), **Euler's 1747 Converse & Complete Euclid–Euler Biconditional Theorem** (`thm_euler_even_perfect_converse`, `thm_euclid_euler_even_perfect_iff`, `v0.7.0`), and **Euler's 1750 Mersenne Prime Divisor Congruence** (`thm_mersenne_prime_divisor_congruence`: $2p \mid q - 1$ via Fermat's Little Theorem, `v0.7.0`).
18. [x] **Ramsey Theory** ([`FormalAtlas/Ramsey.lean`](FormalAtlas/Ramsey.lean), 4 thms): Exact first-principles determinations of **$R(3,3) = 6$** and **$R(3,4) = 9$**.
19. [x] **Non-Vacuity, Adversarial & Live Negative Rejection Suites** ([`NonVacuity.lean`](NonVacuity.lean), [`Adversarial.lean`](Adversarial.lean), `scripts/test_lean_negative.py`): 20 concrete witnesses + 24 false-variant refutations + 3 live negative kernel/axiom-gate rejections guarding every domain.

## Planned Next Targets (`v0.11.0+`)

1. [ ] **Continued-fraction & Baker-style lower bounds** for nontrivial positive $3n+1$ cycle lengths ($o \ge 5$, building on `thm_collatz_positive_cycle_four_odd`, `thm_collatz_cycle_no_div3`, and `thm_collatz_cycle_amplitude_ceiling` toward Eliahou 1993 / Hercher 2023).
2. [ ] **Lonely Runner $n = 4$** constructive proof and **Ramsey $R(3,5) = 14$ / $R(4,4) = 18$** (Paley graph $P_{17}$ lower bound) in pure Lean Core.
3. [ ] **Odd Perfect Number Euler Structure Theorem:** prove Euler's $N = p^\alpha m^2$ ($p \equiv \alpha \equiv 1 \pmod 4$) structural constraint for any odd perfect number in pure Lean Core.
4. [ ] **Optional Mathlib bridge package (`lean-mathlib/`):** Separate opt-in Lean sub-package (keeping `lean/` zero-Mathlib) for analytic/geometric definitions (Riemann $\zeta$ zero-free regions, Kakeya Besicovitch sets, Navier–Stokes scaling invariance).

## Non-Goals

- No formal proof of Collatz, Erdős–Straus, uniform Lonely Runner, Brocard finiteness, Twin Primes, Goldbach, Odd Perfect Numbers, Mersenne Infinitude, or higher Ramsey numbers is implied.
- No infinite regeneration theorem is formalized.
- No stochastic or fitted-model heuristic counts as proof.

## Artifact Requirements (Enforced in CI)

Every formal artifact in `lean/` must ship with:
- Strict `autoImplicit = false` in `lakefile.toml` and tracked `lake-manifest.json` with zero `.lean` symlinks;
- Isolated theorem specification in `Challenge.lean` matching `comparator.json` ($\le 1{,}000$ lines, $\le 100$ KiB, `module` header);
- Zero-`sorry`, zero-`admit`, zero-`native_decide`, zero-custom-`axiom`, zero-`implemented_by`/`@[extern]`/`@[csimp]` proof in `Solution.lean`;
- Concrete non-vacuity witnesses in `NonVacuity.lean`, adversarial refutations in `Adversarial.lean`, and live negative kernel rejection via `scripts/test_lean_negative.py`;
- `#print axioms` audit in `VerifyAxioms.lean` strictly within `{propext, Classical.choice, Quot.sound}` and mirrored verbatim in `README.md` (`scripts/check_readme_axioms.py`);
- Definition-by-definition correspondence in `STATEMENT_FIDELITY.md`;
- Full `bwrap`-sandboxed 6-kernel replay (`lake check --paranoid` + `lake comparator --config comparator.json --paranoid`).
