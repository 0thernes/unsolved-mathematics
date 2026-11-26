# Statement Fidelity Audit — `FormalAtlas` (Lean 4.35.0, `v0.5.0`)

> **Purpose:** Machine-checked Lean proofs fail in the real world not because the kernel is wrong, but because a formal definition silently diverges from the mathematical literature (**representational mismatch**). This table maps every definition, headline theorem, non-vacuity witness, and adversarial refutation in [`FormalAtlas/Defs.lean`](FormalAtlas/Defs.lean), [`Challenge.lean`](Challenge.lean), [`NonVacuity.lean`](NonVacuity.lean), and [`Adversarial.lean`](Adversarial.lean) line-by-line to its primary mathematical source and exact epistemic boundary.

## 1. Trusted Definition Audit (`FormalAtlas/Defs.lean`, 161 LOC, Zero Mathlib)

| Lean Declaration | Informal Mathematical Object | Literature Anchor | Exactness / Fidelity Notes |
|---|---|---|---|
| `T : Int → Int` | Shortcut Collatz map $T(x) = x/2$ (even), $(3x+1)/2$ (odd) | Terras (1976), Lagarias (1985) | Defined over all $\mathbb{Z}$ using Euclidean `% 2` / `/ 2`; agrees on $\mathbb{Z}_{>0}$ and extends to negative cycles $\{-1, -5, -17\}$. |
| `TMinus : Int → Int` | Sibling $3n-1$ shortcut map $T_-(x) = x/2$ (even), $(3x-1)/2$ (odd) | Lagarias (1985); Atlas `SIBLING-CONTROL.md` | Exact $\varepsilon = -1$ control sharing identical parity-word combinatorics while admitting positive cycles $\{5,7,10\}$ and $\{17,\dots\}$. |
| `parityWord`, `oddCount` | Length-$d$ parity vector $w \in \{0,1\}^d$ and odd-step count $o(w)$ | Terras (1976) | `parityBit x := (x % 2 != 0)`; `wordOddCount` counts `true` bits identically. |
| `wordIntercept` | Exact affine intercept $c(w) \in \mathbb{Z}_{\ge 0}$ in $2^d T^d(x) = 3^o x + c(w)$ | Bernstein–Lagarias (1996); White Paper §4 | Proved exact in `thm_collatz_exact_intercept_law` for all $d \in \mathbb{N}, x \in \mathbb{Z}$. |
| `IsErdosStrausSol n x y z` | Positive integers $x,y,z > 0$ solving $\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$ | Erdős (1950); Mordell (1967) | Exact denominator-cleared integer equation $4xyz = n(yz + xz + xy)$ with $x,y,z > 0$; equivalent over $\mathbb{Q}$ since $n,x,y,z > 0$. |
| `FarEnough m p q v` / `WithinDist m p q v` | Circular distance $\|(p/q)\cdot v\| \ge 1/m$ (resp. $\le 1/m$) on $\mathbb{R}/\mathbb{Z}$ | Wills (1967), Cusick (1973) | Exact integer arithmetic via $r = (pv) \bmod q \in [0,q)$: $\min(r, q-r)/q \ge 1/m \iff q \le m r \land q \le m(q-r)$. Zero floating-point error. |
| `IsBrocardSol n m` | $n! + 1 = m^2$ over $\mathbb{N}$ | Brocard (1876), Ramanujan (1913) | Exact `Nat` equality `fact n + 1 = m * m`. |
| `IsPrime p` | Textbook prime: $p \ge 2 \land \forall d \mid p,\ d = 1 \lor d = p$ | Euclid (*Elements* VII, IX) | Literal divisibility definition over $\mathbb{N}$; computable `isPrimeBool` proved sound in `FormalAtlas/Primes.lean`. |
| `divSum n`, `IsPerfect n` | Divisor sum $\sigma(n) = \sum_{d \mid n} d$ and $\sigma(n) = 2n$ ($n > 0$) | Euclid (*Elements* IX.36), Euler | Structurally recursive divisor-pair sum over $1 \le d \le \lfloor\sqrt{n}\rfloor$; agrees identically with full divisor sum (checked differentially in pytest). |
| `HasMonoTriangle c` | Monochromatic $K_3$ in a 2-coloring of $K_k$ | Ramsey (1930) | $\exists a, b, d \in \mathrm{Fin}\ k,\ a < b \land b < d \land c(a,b) = c(b,d) = c(a,d)$. |

## 2. Headline Theorem Fidelity & Non-Vacuity Audit (`Challenge.lean` ↔ `Solution.lean`, 45 Theorems across 8 Domains)

### Domain I: Collatz Conjecture & $3n-1$ Sibling Barrier (`FormalAtlas/Collatz.lean`, 14 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 1 | `thm_collatz_cylinder_affine_law` | $T^d(2^d q + r) = 3^{o(r,d)} q + T^d(r)$ | Terras (1976) | Unconditional ($\forall d, q, r$) | **Exact match** |
| 2 | `thm_collatz_exact_intercept_law` | $2^d T^d(x) = 3^o x + c(w)$ | Bernstein–Lagarias (1996) | Unconditional ($\forall d, x$) | **Exact match** |
| 3 | `thm_terras_parity_word_bijection` | $r \mapsto w_d(r)$ bijects $\{0,\dots,2^d-1\} \leftrightarrow \{0,1\}^d$ | Terras (1976), Thm 1.1 | Unconditional ($\forall d$) | **Exact match** |
| 4 | `thm_collatz_descent_certificate_sound` | $3^o < 2^d \land (2^d-3^o)q > T^d(r)-r \implies T^d(2^dq+r) < 2^dq+r$ | Terras (1976) | `witness_descent_certificate`; `adv_collatz_no_universal_descent_d1` | **Exact match** |
| 5 | `thm_collatz_no_finite_subcritical_cover` | $T^d(-1) = -1$, $o(-1,d)=d$, $2^d \le 3^d$ | Elementary 2-adic fixed point | Unconditional ($\forall d$) | **Exact match** |
| 6 | `thm_collatz_spine_ladder_identity` | $2^d((2^d-3^o)T^d(x)-c) = 3^o((2^d-3^o)x-c)$ | White Paper §4 (cleared denominators) | Unconditional ($\forall d, x$) | **Exact match** |
| 7 | `thm_collatz_positivity_localization` | Every supercritical word ($3^o > 2^d$) satisfies $c(w) \ge 3^o - 2^d$ ($\rho_w \le -1$) | White Paper §4 (unconditional) | `witness_positivity_localization`; `witness_subcritical_positive_cycle`; `adv_collatz_positivity_converse_false` | **Exact match** |
| 8 | `thm_collatz_epsilon_invariance_barrier` | $T_-$ shares exact Terras bijection yet admits positive supercritical cycles at $5$ (len 3) and $17$ (len 11) | Atlas `SIBLING-CONTROL.md` | Explicit concrete cycles $T_-^3(5)=5$, $T_-^{11}(17)=17$ | **Exact match** |
| 9 | `thm_collatz_cycle_equation` | $T^d(x) = x \implies (2^d - 3^o)x = c(w)$ | Böhm–Sontacchi (1978) | Non-vacuous at $x \in \{1, -1, -5, -17\}$ | **Exact match** |
| 10 | `thm_collatz_parity_word_append` | $w_{d_1+d_2}(f, x) = w_{d_1}(f, x) \mathbin{\Vert} w_{d_2}(f, f^{d_1}(x))$ | Symbolic dynamics cocycle | Unconditional ($\forall f, d_1, d_2, x$) | **Exact match** |
| 11 | `thm_collatz_negative_cycles` | True $3n+1$ map $T$ has supercritical negative cycles at $-5$ (len 3) and $-17$ (len 11) | Lagarias (1985) | `adv_collatz_positivity_required_for_no_nontrivial_cycles` | **Exact match** |
| 12 | `thm_collatz_zero_fixed_point` | $\forall d,\ T^d(0) = 0 \land o(T, d, 0) = 0$ | Elementary fixed point | Unconditional ($\forall d$) | **Exact match** |
| 13 | `thm_collatz_intercept_nonneg` | $\forall w,\ 0 \le c(w)$ | Bernstein–Lagarias (1996) | Unconditional ($\forall w$) | **Exact match** |
| 14 | `thm_collatz_parity_word_length` | $\forall f, d, x,\ |w_d(f, x)| = d$ | Symbolic dynamics invariant | Unconditional ($\forall f, d, x$) | **Exact match** |

### Domain II: Erdős–Straus Conjecture (`FormalAtlas/ErdosStraus.lean`, 5 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 15 | `thm_erdos_straus_mordell_840` | $\forall n \ge 2$ with $n \bmod 840 \notin \{1,121,169,289,361,529\}$, `HasErdosStraus n` | Mordell (1967), ch. 30 | `witness_erdos_straus_hypotheses`; `adv_erdos_straus_zero_denom_blocked`; `adv_erdos_straus_wrong_witness_refuted` | **Exact match (834/840 = 99.29%)** |
| 16 | `thm_erdos_straus_multiplicative_closure` | `HasErdosStraus m → 0 < k → HasErdosStraus (m * k)` | Erdős (1950); Mordell (1967) | Used to prove Theorem 17 | **Exact match** |
| 17 | `thm_erdos_straus_mordell_exceptions_small` | `HasErdosStraus n` for all 6 smallest exceptional squares $\{121,169,289,361,529,841\}$ | Mordell (1967) | Concrete prime-square resolutions | **Exact match** |
| 18 | `thm_erdos_straus_symmetry` | `IsErdosStrausSol n x y z → IsErdosStrausSol n y z x` | Elementary cyclic symmetry | Unconditional ($\forall n, x, y, z$) | **Exact match** |
| 19 | `thm_erdos_straus_all_le_30` | $\forall n,\ 2 \le n \le 30 \implies \mathrm{HasErdosStraus}\ n$ | Finite base-range verification | Covers all $n \in [2, 30]$ | **Exact match** |

### Domain III: Lonely Runner Conjecture (`FormalAtlas/LonelyRunner.lean`, 7 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 20 | `thm_lonely_runner_sharpness_all_n` | $\forall n \ge 1, t = p/q$, speeds $\{1,\dots,n\}$ admit $i$ with $\|t\cdot i\| \le \frac{1}{n+1}$ | Wills (1967) sharpness | `witness_lonely_runner_concrete`; `adv_lonely_runner_strict_threshold_fails` | **Exact match (over $\mathbb{Q}$)** |
| 21 | `thm_lonely_runner_n1` | Lonely Runner holds for $n = 1$ (2 runners) | Wills (1967) | Explicit time $t = 1/(2v)$ | **Exact match** |
| 22 | `thm_lonely_runner_n2` | Lonely Runner holds for $n = 2$ (3 runners) | Wills (1967) | `witness_lonely_runner_concrete` ($v_1=3, v_2=10, t=1/6$) | **Exact match** |
| 23 | `thm_lonely_runner_speed_scaling` | `FarEnough m p q v → FarEnough m p (q * k) (v * k)` ($q, k > 0$) | Standard GCD reduction | `adv_lonely_runner_bad_time_refuted` | **Exact match** |
| 24 | `thm_lonely_runner_period_shift` | `FarEnough m p q v → FarEnough m (p + q) q v` ($q > 0$) | $\mathbb{R}/\mathbb{Z}$ periodicity | Unconditional ($\forall m, p, q > 0, v$) | **Exact match** |
| 25 | `thm_lonely_runner_neg_time` | `FarEnough m p q v → FarEnough m (-p) q v` ($q > 0$) | Time-reversal symmetry | Unconditional ($\forall m, p, q > 0, v$) | **Exact match** |
| 26 | `thm_lonely_runner_n3_nondiv4` | $n=3$ (4 runners): $\forall v_1, v_2, v_3$ with $4 \nmid v_i$, $t = 1/4$ achieves gap $\ge 1/4$ | Elementary mod-4 coverage (7/8 classes) | `witness_lonely_runner_n3_concrete` ($v = (1, 2, 3), t = 1/4$) | **Exact match** |

### Domain IV: Brocard's Problem (`FormalAtlas/Brocard.lean`, 7 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 27 | `thm_brocard_brown_solutions` | $(4,5), (5,11), (7,71)$ solve $n!+1 = m^2$ | Brocard (1876), Ramanujan (1913) | Concrete Brown pairs | **Exact match** |
| 28 | `thm_brocard_exhaustive_le_12` | Sole solutions for $n \le 12$ are $(4,5), (5,11), (7,71)$ | Finite exhaustion | `witness_brocard_non_solution` ($6!+1 = 721$) | **Exact match** |
| 29 | `thm_brocard_mod4_ge_4` | $\forall n \ge 4,\ (n! + 1) \equiv 1 \pmod 4$ | Elementary modular constraint | Forces $m$ odd for $n \ge 4$ | **Exact match** |
| 30 | `thm_brocard_exhaustive_le_15` | Sole solutions for $n \le 15$ are $(4,5), (5,11), (7,71)$ | Finite exhaustion | `adv_brocard_false_candidates_refuted` | **Exact match** |
| 31 | `thm_brocard_not_div3_ge_3` | $\forall n \ge 3,\ (n! + 1) \equiv 1 \pmod 3$ | Elementary modular constraint | Excludes $3 \mid m$ for $n \ge 3$ | **Exact match** |
| 32 | `thm_brocard_mod10_ge_5` | $\forall n \ge 5,\ (n! + 1) \equiv 1 \pmod{10}$ | Elementary decimal-digit invariant | Forces $m \equiv \pm 1 \pmod{10}$ for $n \ge 5$ | **Exact match** |
| 33 | `thm_brocard_exhaustive_le_20` | Sole solutions for $n \le 20$ are $(4,5), (5,11), (7,71)$ ($20!+1 = 2.43\times 10^{18}$) | Finite exhaustion (square bracketing) | `adv_brocard_false_candidates_refuted` ($n \in \{6,8,13,16\}$) | **Exact match** |

### Domain V: Primes & Twin Prime Conjecture (`FormalAtlas/Primes.lean`, 4 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 34 | `thm_euclid_infinitely_many_primes` | $\forall N,\ \exists p > N,\ \mathrm{IsPrime}(p)$ | Euclid (*Elements* IX.20) | `adv_non_primes_refuted` ($0, 1, 4, 9, 15, 21$) | **Exact match** |
| 35 | `thm_arbitrary_prime_gaps` | $\forall k \ge 1,\ \exists m \ge 2,\ \forall i < k,\ \neg\mathrm{IsPrime}(m+i)$ | Elementary $(k+1)! + 2$ construction | Unconditional ($\forall k \ge 1$) | **Exact match** |
| 36 | `thm_prime_odd_ge_3` | $\forall p \ge 3,\ \mathrm{IsPrime}(p) \implies p \equiv 1 \pmod 2$ | Elementary prime parity | `adv_non_primes_refuted` | **Exact match** |
| 37 | `thm_twin_prime_mod6` | $\forall p \ge 4,\ \mathrm{IsPrime}(p) \land \mathrm{IsPrime}(p+2) \implies p \equiv 5 \pmod 6$ | Elementary modular rigidity | `witness_twin_primes_concrete` ($(5,7), (11,13), (17,19)$); `adv_twin_prime_mod6_needs_ge_4` ($(3,5)$) | **Exact match** |

### Domain VI: Goldbach's Conjecture (`FormalAtlas/Goldbach.lean`, 3 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 38 | `thm_goldbach_even_le_100` | Every even $4 \le n \le 100$ is a sum of two certified primes | Goldbach (1742) finite verification | `witness_goldbach_100` ($100 = 3 + 97 = 47 + 53$) | **Exact match** |
| 39 | `thm_goldbach_odd_binary_obstruction` | Any odd $n = p + q$ with $p, q$ prime satisfies $p = 2 \lor q = 2$ | Elementary parity obstruction | Paired with Theorem 40 | **Exact match** |
| 40 | `thm_goldbach_binary_fails_at_11` | $\neg \exists p, q,\ \mathrm{IsPrime}(p) \land \mathrm{IsPrime}(q) \land p + q = 11$ | Why Goldbach requires even $n$ | `adv_goldbach_requires_even` ($n = 11$ and $n = 27$) | **Exact match** |

### Domain VII: Odd Perfect Numbers & Mersenne Primes (`FormalAtlas/PerfectNumbers.lean`, 3 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 41 | `thm_mersenne_exponent_prime` | $\forall n \ge 2,\ \mathrm{IsPrime}(2^n - 1) \implies \mathrm{IsPrime}(n)$ | Cataldi / Mersenne (1644) | `witness_mersenne_31` ($2^5-1=31$); `adv_mersenne_converse_false` ($2^{11}-1 = 23\times 89$) | **Exact match** |
| 42 | `thm_perfect_numbers_first_four` | $6, 28, 496, 8128$ are all perfect ($\sigma(n) = 2n$) | Euclid / Nicomachus | `adv_non_perfect_refuted` ($1, 2, 12, 15, 24$) | **Exact match** |
| 43 | `thm_no_odd_perfect_le_100` | $\forall n \le 100,\ n \equiv 1 \pmod 2 \implies \neg\mathrm{IsPerfect}(n)$ | Finite odd-perfect exclusion | Exhaustive kernel check $1 \le n \le 100$ | **Exact match** |

### Domain VIII: Ramsey Theory (`FormalAtlas/Ramsey.lean`, 2 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 44 | `thm_ramsey_R33_upper` | Every 2-coloring of $K_6$ contains a monochromatic triangle | Ramsey (1930); Greenwood–Gleason (1955) | Exact $K_6$ pigeonhole upper bound $R(3,3) \le 6$ | **Exact match** |
| 45 | `thm_ramsey_R33_lower` | Explicit symmetric $C_5$ coloring of $K_5$ has zero monochromatic triangles | Greenwood–Gleason (1955) | `adv_ramsey_R33_not_le_5` — establishes exact $R(3,3) = 6$ | **Exact match** |

## 3. Explicitly NOT Proved (Hard Epistemic Boundary)

- **Collatz Conjecture (`OPEN`):** Proved NO convergence, NO divergence exclusion, and NO positive-cycle exclusion for $3n+1$.
- **Erdős–Straus Conjecture (`OPEN` / `active-progress`):** The six quadratic-residue classes $\{1, 121, 169, 289, 361, 529\} \pmod{840}$ remain uncovered for general primes; the full conjecture is NOT proved.
- **Lonely Runner Conjecture (`active-progress`):** Only global sharpness (all $n$), symmetry group, base cases $n \in \{1, 2\}$, and the $4 \nmid v_i$ parity family for $n = 3$ are formalized here; general uniform proof for all $n$ remains OPEN.
- **Brocard's Problem (`OPEN`):** Only $n \le 20$ and mod-3/4/10 constraints are proved here; finiteness for all $n$ remains OPEN.
- **Twin Prime Conjecture (`active-progress`):** Infinitely many primes, arbitrary prime gaps, and mod-6 rigidity are classical; infinitely many twin primes remains OPEN.
- **Goldbach's Conjecture (`OPEN`):** Only even $4 \le n \le 100$ and the odd binary obstruction are proved here; Goldbach for all even $n \ge 4$ remains OPEN.
- **Odd Perfect Numbers & Infinitude of Mersenne Primes (`OPEN`):** Only Mersenne exponent necessity, the first four even perfect numbers, and odd-perfect exclusion $n \le 100$ are proved here; both conjectures remain OPEN.
- **Ramsey Theory (`OPEN`):** Exact $R(3,3) = 6$ is classical; $R(5,5)$ and diagonal asymptotics remain OPEN.

## 4. Exact Verbatim `#print axioms` Output (`VerifyAxioms.lean`, Lean 4.35.0)

Every one of the **69 audited declarations** (45 headline theorems, 10 non-vacuity witnesses, 14 adversarial false-variant refutations) depends strictly on subsets of `{propext, Classical.choice, Quot.sound}` (**12 declarations require zero axioms**):

```text
'FormalAtlas.Challenge.thm_collatz_cylinder_affine_law' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_exact_intercept_law' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_terras_parity_word_bijection' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_descent_certificate_sound' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_no_finite_subcritical_cover' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_spine_ladder_identity' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positivity_localization' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_epsilon_invariance_barrier' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_cycle_equation' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_parity_word_append' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_negative_cycles' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_zero_fixed_point' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_intercept_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_parity_word_length' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_erdos_straus_mordell_840' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_erdos_straus_multiplicative_closure' depends on axioms: [propext]
'FormalAtlas.Challenge.thm_erdos_straus_mordell_exceptions_small' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_erdos_straus_symmetry' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_erdos_straus_all_le_30' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_sharpness_all_n' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_n1' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_n2' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_speed_scaling' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_period_shift' depends on axioms: [propext]
'FormalAtlas.Challenge.thm_lonely_runner_neg_time' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_n3_nondiv4' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_brocard_brown_solutions' does not depend on any axioms
'FormalAtlas.Challenge.thm_brocard_exhaustive_le_12' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_brocard_mod4_ge_4' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_brocard_exhaustive_le_15' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_brocard_not_div3_ge_3' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_brocard_mod10_ge_5' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_brocard_exhaustive_le_20' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_euclid_infinitely_many_primes' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_arbitrary_prime_gaps' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_prime_odd_ge_3' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_twin_prime_mod6' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_goldbach_even_le_100' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_goldbach_odd_binary_obstruction' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_goldbach_binary_fails_at_11' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_mersenne_exponent_prime' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_perfect_numbers_first_four' does not depend on any axioms
'FormalAtlas.Challenge.thm_no_odd_perfect_le_100' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_ramsey_R33_upper' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_ramsey_R33_lower' depends on axioms: [propext, Quot.sound]
'FormalAtlas.NonVacuity.witness_descent_certificate' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.NonVacuity.witness_positivity_localization' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_subcritical_positive_cycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.NonVacuity.witness_erdos_straus_hypotheses' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_lonely_runner_concrete' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_brocard_non_solution' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_twin_primes_concrete' depends on axioms: [propext, Quot.sound]
'FormalAtlas.NonVacuity.witness_goldbach_100' depends on axioms: [propext, Quot.sound]
'FormalAtlas.NonVacuity.witness_mersenne_31' depends on axioms: [propext, Quot.sound]
'FormalAtlas.NonVacuity.witness_lonely_runner_n3_concrete' does not depend on any axioms
'FormalAtlas.Adversarial.adv_erdos_straus_zero_denom_blocked' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Adversarial.adv_erdos_straus_wrong_witness_refuted' does not depend on any axioms
'FormalAtlas.Adversarial.adv_collatz_no_universal_descent_d1' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_positivity_required_for_no_nontrivial_cycles' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_positivity_converse_false' does not depend on any axioms
'FormalAtlas.Adversarial.adv_lonely_runner_strict_threshold_fails' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_lonely_runner_bad_time_refuted' does not depend on any axioms
'FormalAtlas.Adversarial.adv_brocard_false_candidates_refuted' does not depend on any axioms
'FormalAtlas.Adversarial.adv_non_primes_refuted' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Adversarial.adv_mersenne_converse_false' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Adversarial.adv_non_perfect_refuted' does not depend on any axioms
'FormalAtlas.Adversarial.adv_twin_prime_mod6_needs_ge_4' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Adversarial.adv_ramsey_R33_not_le_5' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Adversarial.adv_goldbach_requires_even' depends on axioms: [propext, Quot.sound]
```

## 5. Multi-Kernel Replay Verdict (6/6 Independent Kernels)

All 45 challenge/solution theorem signatures, 10 non-vacuity witnesses, and 14 adversarial refutations (69 declarations total) pass all six independent Lean 4.35.0 kernels (full replay log in [`six_kernel_audit.txt`](six_kernel_audit.txt), plus `bubblewrap`-sandboxed `lake check --paranoid` and `lake comparator --config comparator.json --paranoid` in Ubuntu GitHub Actions CI):
1. `lean` (C++ reference kernel) — **ACCEPT**
2. `leanchecker-paranoid --fresh` — **ACCEPT**
3. `lean4lean --import` (Lean-in-Lean verified kernel) — **ACCEPT**
4. `nanoda_bin` (Rust independent kernel, strict `{propext, Classical.choice, Quot.sound}` whitelist; zero `sorryAx` even declared in minimal proof cones) — **ACCEPT**
5. `con-leche --verified` (verified Lean kernel) — **ACCEPT**
6. `con-ron --verified` (Rust arena checker) — **ACCEPT**
