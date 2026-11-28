# Statement Fidelity Audit — `FormalAtlas` (Lean 4.35.0, `v0.10.0`)

> **Purpose:** Machine-checked Lean proofs fail in the real world not because the kernel is wrong, but because a formal definition silently diverges from the mathematical literature (**representational mismatch**). This table maps every definition, headline theorem, non-vacuity witness, and adversarial refutation in [`FormalAtlas/Defs.lean`](FormalAtlas/Defs.lean), [`Challenge.lean`](Challenge.lean), [`NonVacuity.lean`](NonVacuity.lean), and [`Adversarial.lean`](Adversarial.lean) line-by-line to its primary mathematical source and exact epistemic boundary. Package compilation enforces `autoImplicit = false` in [`lakefile.toml`](lakefile.toml) on Lean 4.35.0 commit `eb6cafb7290e8bd5f2937522d8d804f58f02bafc`.

## 1. Trusted Definition Audit (`FormalAtlas/Defs.lean`, 202 LOC, Zero Mathlib)

| Lean Declaration | Informal Mathematical Object | Literature Anchor | Exactness / Fidelity Notes |
|---|---|---|---|
| `T : Int → Int` | Shortcut Collatz map $T(x) = x/2$ (even), $(3x+1)/2$ (odd) | Terras (1976), Lagarias (1985) | Defined over all $\mathbb{Z}$ using Euclidean `% 2` / `/ 2`; agrees on $\mathbb{Z}_{>0}$ and extends to negative cycles $\{-1, -5, -17\}$. |
| `TMinus : Int → Int` | Sibling $3n-1$ shortcut map $T_-(x) = x/2$ (even), $(3x-1)/2$ (odd) | Lagarias (1985); Atlas `SIBLING-CONTROL.md` | Exact $\varepsilon = -1$ control sharing identical parity-word combinatorics while admitting positive cycles $\{5,7,10\}$ and $\{17,\dots\}$. |
| `parityWord`, `oddCount` | Length-$d$ parity vector $w \in \{0,1\}^d$ and odd-step count $o(w)$ | Terras (1976) | `parityBit x := (x % 2 != 0)`; `wordOddCount` counts `true` bits identically. |
| `wordIntercept` | Exact affine intercept $c(w) \in \mathbb{Z}_{\ge 0}$ in $2^d T^d(x) = 3^o x + c(w)$ | Bernstein–Lagarias (1996); White Paper §4 | Proved exact in `thm_collatz_exact_intercept_law` for all $d \in \mathbb{N}, x \in \mathbb{Z}$. |
| `periodicBit`, `periodicPrefixFrom`, `periodicPrefix`, `spineDenom` | Infinite periodic word $w^\infty$ prefix of length $k$ and odd spine denominator $D(w) = 2^{|w|} - 3^{o(w)}$ | Fine–Wilf (1965); Bernstein–Lagarias (1996) | Exact cleared-denominator arithmetic for 2-adic periodic spine congruences and Odd-Unit-Lock valuation isometry. |
| `catCollatzStep` | Zero-workspace reversible catalytic register update computing $T^d(2^d q + r)$ | Buhrman–Cleve–Koucký–Loff–Speelman (2014) | Borrows arbitrary pre-filled `cat : Int`, adds $T^d(2^d q + r)$ into `acc`, and restores `cat` identically. |
| `IsErdosStrausSol n x y z` | Positive integers $x,y,z > 0$ solving $\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$ | Erdős (1950); Mordell (1967) | Exact denominator-cleared integer equation $4xyz = n(yz + xz + xy)$ with $x,y,z > 0$; equivalent over $\mathbb{Q}$ since $n,x,y,z > 0$. |
| `FarEnough m p q v` / `WithinDist m p q v` | Circular distance $\|(p/q)\cdot v\| \ge 1/m$ (resp. $\le 1/m$) on $\mathbb{R}/\mathbb{Z}$ | Wills (1967), Betke–Wills (1972), Cusick (1973) | Exact integer arithmetic via $r = (pv) \bmod q \in [0,q)$: $\min(r, q-r)/q \ge 1/m \iff q \le m r \land q \le m(q-r)$. Zero floating-point error. |
| `IsBrocardSol n m` | $n! + 1 = m^2$ over $\mathbb{N}$ | Brocard (1876), Ramanujan (1913) | Exact `Nat` equality `fact n + 1 = m * m`. |
| `IsPrime p` | Textbook prime: $p \ge 2 \land \forall d \mid p,\ d = 1 \lor d = p$ | Euclid (*Elements* VII, IX) | Literal divisibility definition over $\mathbb{N}$; computable `isPrimeBool` proved sound in `FormalAtlas/Primes.lean`. |
| `isqrt n`, `divSum n`, `IsPerfect n` | Exact floor square root $\lfloor\sqrt{n}\rfloor$, divisor sum $\sigma(n) = \sum_{d \mid n} d$, and $\sigma(n) = 2n$ ($n > 0$) | Euclid (*Elements* IX.36), Euler (1747) | `isqrt` binary search with fuel `n` is **proved unconditionally exact** for all $n \in \mathbb{N}$ (`isqrt_spec`), and `divSum n` is proved equal to direct linear divisor sum `divSumLin n n` for ALL $n \in \mathbb{N}$ (`divSum_eq_divSumLin` in `PerfectNumbers.lean`). |
| `HasMonoTriangle c`, `HasColorTriangle c col`, `HasColorK4 c col` | Monochromatic $K_3$, color-`col` $K_3$, and color-`col` $K_4$ in a 2-coloring of $K_k$ | Ramsey (1930); Greenwood–Gleason (1955) | Strict ascending vertex tuples (`a < b < d` or `a < b < d < e` in `Fin k`) with all pairwise edges equal to `col`. |

## 2. Headline Theorem Fidelity & Non-Vacuity Audit (`Challenge.lean` ↔ `Solution.lean`, 74 Theorems across 8 Domains)

### Domain I: Collatz Conjecture, Fine–Wilf 2-Adic Valuation Ceilings, Chiral/3-Adic Laws & Cycle Obstructions (`FormalAtlas/Collatz.lean`, 36 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 1 | `thm_collatz_cylinder_affine_law` | $T^d(2^d q + r) = 3^{o(r,d)} q + T^d(r)$ | Terras (1976) | Unconditional ($\forall d, q, r$) | **Exact match** |
| 2 | `thm_collatz_exact_intercept_law` | $2^d T^d(x) = 3^o x + c(w)$ | Bernstein–Lagarias (1996) | Unconditional ($\forall d, x$) | **Exact match** |
| 3 | `thm_terras_parity_word_bijection` | $r \mapsto w_d(r)$ bijects $\{0,\dots,2^d-1\} \leftrightarrow \{0,1\}^d$ | Terras (1976), Thm 1.1 | Unconditional ($\forall d$) | **Exact match** |
| 4 | `thm_collatz_descent_certificate_sound` | $3^o < 2^d \land (2^d-3^o)q > T^d(r)-r \implies T^d(2^dq+r) < 2^dq+r$ | Terras (1976) | `witness_descent_certificate`; `adv_collatz_no_universal_descent_d1` | **Exact match** |
| 5 | `thm_collatz_no_finite_subcritical_cover` | $T^d(-1) = -1$, $o(-1,d)=d$, $2^d \le 3^d$ | Elementary 2-adic fixed point | Unconditional ($\forall d$) | **Exact match** |
| 6 | `thm_collatz_spine_ladder_identity` | $2^d((2^d-3^o)T^d(x)-c) = 3^o((2^d-3^o)x-c)$ | White Paper §4 (cleared denominators) | Unconditional ($\forall d, x$) | **Exact match** |
| 7 | `thm_collatz_positivity_localization` | Every supercritical word ($3^o > 2^d$) satisfies $c(w) \ge 3^o - 2^d$ ($\rho_w \le -1$) | White Paper §4 (unconditional) | `witness_positivity_localization`; `witness_subcritical_positive_cycle`; `adv_collatz_positivity_converse_false` | **Exact match** |
| 8 | `thm_collatz_epsilon_invariance_barrier` | `3n-1` sibling comparison: $T_-$ shares exact Terras bijection yet admits positive supercritical cycles at $5$ (len 3) and $17$ (len 11); methodological no-go reading is a heuristic, not formalized | Atlas `SIBLING-CONTROL.md` | Explicit concrete cycles $T_-^3(5)=5$, $T_-^{11}(17)=17$ | **Exact match** |
| 9 | `thm_collatz_cycle_equation` | $T^d(x) = x \implies (2^d - 3^o)x = c(w)$ | Böhm–Sontacchi (1978) | Non-vacuous at $x \in \{1, -1, -5, -17\}$ | **Exact match** |
| 10 | `thm_collatz_parity_word_append` | $w_{d_1+d_2}(f, x) = w_{d_1}(f, x) \mathbin{\Vert} w_{d_2}(f, f^{d_1}(x))$ | Symbolic dynamics cocycle | Unconditional ($\forall f, d_1, d_2, x$) | **Exact match** |
| 11 | `thm_collatz_negative_cycles` | True $3n+1$ map $T$ has supercritical negative cycles at $-5$ (len 3) and $-17$ (len 11) | Lagarias (1985) | `adv_collatz_positivity_required_for_no_nontrivial_cycles` | **Exact match** |
| 12 | `thm_collatz_zero_fixed_point` | $\forall d,\ T^d(0) = 0 \land o(T, d, 0) = 0$ | Elementary fixed point | Unconditional ($\forall d$) | **Exact match** |
| 13 | `thm_collatz_intercept_nonneg` | $\forall w,\ 0 \le c(w)$ | Bernstein–Lagarias (1996) | Unconditional ($\forall w$) | **Exact match** |
| 14 | `thm_collatz_parity_word_length` | $\forall f, d, x,\ |w_d(f, x)| = d$ | Symbolic dynamics invariant | Unconditional ($\forall f, d, x$) | **Exact match** |
| 15 | `thm_collatz_positive_cycle_has_odd_step` | $d \ge 1 \land x > 0 \land T^d(x) = x \implies o(T, d, x) \ge 1$ | Böhm–Sontacchi (1978); Eliahou (1993) | Non-vacuous at $T^2(1)=1$ ($o=1$) | **Exact match** |
| 16 | `thm_collatz_positive_cycle_intercept_pos` | $d \ge 1 \land x > 0 \land T^d(x) = x \implies c(w_d(T, x)) > 0$ | Böhm–Sontacchi (1978) | Non-vacuous at $T^2(1)=1$ ($c=1$) | **Exact match** |
| 17 | `thm_collatz_positive_cycle_subcritical` | $d \ge 1 \land x > 0 \land T^d(x) = x \implies 3^o < 2^d \land 2^d - 3^o \le c(w)$ | Eliahou (1993) cycle subcriticality | Rules out every supercritical positive cycle ($2^d \le 3^o$) | **Exact match** |
| 18 | `thm_collatz_no_positive_cycle_d1` | $\forall x > 0,\ T(x) \ne x$ | Elementary $d=1$ exclusion | `adv_collatz_no_d1_positive_fixed_point` | **Exact match** |
| 19 | `thm_collatz_positive_cycle_one_odd` | $\forall d \ge 1, x > 0,\ T^d(x) = x \land o = 1 \implies d = 2 \land x \in \{1,2\}$ | Unconditional 1-odd-step cycle exclusion | `witness_subcritical_positive_cycle`; `adv_collatz_no_nontrivial_low_odd_cycle` | **Exact match (all $d \ge 1$)** |
| 20 | `thm_collatz_positive_cycle_two_odd` | $\forall d \ge 1, x > 0,\ T^d(x) = x \land o = 2 \implies d = 4 \land x \in \{1,2\}$ | Unconditional 2-odd-step cycle exclusion (Simons–de Weger $m \le 2$) | `witness_collatz_two_odd_trivial_cycle`; `adv_collatz_no_nontrivial_low_odd_cycle` | **Exact match (all $d \ge 1$)** |
| 21 | `thm_collatz_2adic_isometry` | $w_d(T, x) = w_d(T, y) \iff 2^d \mid (x - y)$ | Bernstein–Lagarias (1996) 2-adic conjugacy isometry | Unconditional ($\forall d, x, y$) | **Exact match** |
| 22 | `thm_collatz_periodic_spine_congruence` | $|w| \ge 1 \implies (2^k \mid (D(w)x - c(w)) \iff w_k(T, x) = \operatorname{pref}(w^\infty, k))$ | 2-adic periodic fixed-point congruence | Unconditional ($\forall w \ne [], k, x$) | **Exact match** |
| 23 | `thm_collatz_odd_unit_lock_valuation_isometry` | $2^k \mid (c(w)D(v) - c(v)D(w)) \iff \operatorname{pref}(w^\infty, k) = \operatorname{pref}(v^\infty, k)$ | Exact valuation isometry $v_2(\rho_w - \rho_v) = \operatorname{lcp}(w^\infty, v^\infty)$ | `witness_odd_unit_lock_fine_wilf` | **Exact match** |
| 24 | `thm_collatz_fine_wilf_spine_ceiling` | $c(w)D(v) \ne c(v)D(w) \implies 2^{|w|+|v|-\gcd(|w|,|v|)} \nmid (c(w)D(v) - c(v)D(w))$ | Fine–Wilf (1965) periodicity theorem on 2-adic spines | `witness_odd_unit_lock_fine_wilf` (sharp at $|w|=2, |v|=3$); `adv_collatz_distinct_spines_bounded_v2` | **Exact match (unconditional)** |
| 25 | `thm_collatz_trivial_cycle_orbit` | $T^{2k}(1)=1, T^{2k+1}(1)=2, T^{2k}(2)=2, T^{2k+1}(2)=1$ | Elementary trivial-orbit characterization | Unconditional ($\forall k$) | **Exact match** |
| 26 | `thm_collatz_no_nontrivial_positive_cycle_le_7` | $1 \le d \le 7 \land x > 0 \land T^d(x) = x \implies x \in \{1, 2\}$ | Exhaustive low-period positive-cycle classification | Zero `native_decide`; exhaustive over all $2^d$ words for $d \le 7$ | **Exact match** |
| 27 | `thm_collatz_no_positive_cycle_odd_le_7` | $1 \le d \le 7 \land d \equiv 1 \pmod 2 \land x > 0 \implies T^d(x) \ne x$ | Odd-period exclusion for $d \in \{1, 3, 5, 7\}$ | `adv_collatz_no_odd_period_le_7` | **Exact match** |
| 28 | `thm_collatz_catalytic_reversible_cylinder` | `catCollatzStep d q r acc cat = (acc + T^d(2^d q + r), cat)` | Buhrman et al. (2014) catalytic space | `witness_catalytic_cylinder` (`cat = 999` restored identically) | **Exact match** |
| 29 | `thm_collatz_positive_cycle_three_odd` | $\forall d \ge 1, x > 0,\ T^d(x) = x \land o = 3 \implies d = 6 \land x \in \{1, 2\}$ | Unconditional 3-odd-step cycle exclusion (Simons–de Weger $m \le 3$) | `witness_collatz_three_odd_trivial_cycle`; `adv_collatz_no_nontrivial_three_odd_cycle` | **Exact match (all $d \ge 1$)** |
| 30 | `thm_collatz_intercept_upper_bound` | $\forall w,\ c(w) \le 2^{|w| - o(w)}(3^{o(w)} - 2^{o(w)})$ | Sharp universal affine intercept ceiling | `witness_collatz_intercept_bound_sharp` (`[F,F,T,T]` attains `20 = 20`); `adv_collatz_intercept_bound_strict_false` | **Exact match (sharp $\forall w$)** |
| 31 | `thm_collatz_cycle_amplitude_ceiling` | $d \ge 1 \land x > 0 \land T^d(x) = x \implies (2^d - 3^o)x \le 2^{d - o}(3^o - 2^o)$ | Global Eliahou–Steiner Diophantine cycle amplitude bound | Direct corollary of `thm_collatz_cycle_equation` + `thm_collatz_intercept_upper_bound` | **Exact match (all positive cycles)** |
| 32 | `thm_collatz_sign_conjugacy` | $\forall d, x,\ T^d(-x) = -T_-^d(x) \land o(T,d,-x) = o(T_-,d,x)$ | Exact chiral involution between $3n+1$ ($\mathbb{Z}_{<0}$) and $3n-1$ ($\mathbb{Z}_{>0}$) | `witness_collatz_mod3_chiral_asymmetry` ($T^3(-5) = -T_-^3(5)$) | **Exact match ($\forall d, x$)** |
| 33 | `thm_collatz_mod3_chiral_asymmetry` | $\forall x,\ 2 \nmid x \implies T(x) \equiv 2 \pmod 3 \land T_-(x) \equiv 1 \pmod 3$ | Exact $\varepsilon$-sensitive mod-3 phase-lock asymmetry | `witness_collatz_mod3_chiral_asymmetry` ($T(5)=8\equiv 2, T_-(5)=7\equiv 1$) | **Exact match ($\forall$ odd $x$)** |
| 34 | `thm_collatz_intercept_not_div3` | $\forall w,\ o(w) \ge 1 \implies 3 \nmid c(w)$ | Universal 3-adic unit law for affine intercepts & spines | Unconditional ($\forall w$ with $o(w) \ge 1$) | **Exact match** |
| 35 | `thm_collatz_cycle_no_div3` | $\forall d \ge 1, x \ne 0,\ T^d(x) = x \implies 3 \nmid x$ | Global 3-adic exclusion of nonzero multiples of 3 from ALL Collatz cycles | `adv_collatz_no_mult3_nonzero_cycle` | **Exact match (all $d \ge 1, x \ne 0$)** |
| 36 | `thm_collatz_positive_cycle_four_odd` | $\forall d \ge 1, x > 0,\ T^d(x) = x \land o = 4 \implies d = 8 \land x \in \{1, 2\}$ | Unconditional 4-odd-step positive-cycle exclusion (odd-quotient elimination + 3-adic obstruction + 2-adic cascade mod 128) | `witness_collatz_four_odd_trivial_cycle`; `adv_collatz_no_nontrivial_four_odd_cycle` | **Exact match (all $d \ge 1$)** |

### Domain II: Erdős–Straus Conjecture (`FormalAtlas/ErdosStraus.lean`, 5 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 37 | `thm_erdos_straus_mordell_840` | $\forall n \ge 2$ with $n \bmod 840 \notin \{1,121,169,289,361,529\}$, `HasErdosStraus n` | Mordell (1967), ch. 30 | `witness_erdos_straus_hypotheses`; `adv_erdos_straus_zero_denom_blocked`; `adv_erdos_straus_wrong_witness_refuted` | **Exact match (834/840 = 99.29%)** |
| 38 | `thm_erdos_straus_multiplicative_closure` | `HasErdosStraus m → 0 < k → HasErdosStraus (m * k)` | Erdős (1950); Mordell (1967) | Used to prove Theorem 37 | **Exact match** |
| 39 | `thm_erdos_straus_mordell_exceptions_small` | `HasErdosStraus n` for all 6 smallest exceptional squares $\{121,169,289,361,529,841\}$ | Mordell (1967) | Concrete prime-square resolutions | **Exact match** |
| 40 | `thm_erdos_straus_symmetry` | `IsErdosStrausSol n x y z → IsErdosStrausSol n y z x` | Elementary cyclic symmetry | Unconditional ($\forall n, x, y, z$) | **Exact match** |
| 41 | `thm_erdos_straus_all_le_30` | $\forall n,\ 2 \le n \le 30 \implies \mathrm{HasErdosStraus}\ n$ | Finite base-range verification | Covers all $n \in [2, 30]$ | **Exact match** |

### Domain III: Lonely Runner Conjecture (`FormalAtlas/LonelyRunner.lean`, 8 Theorems — Complete Through $n = 3$)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 42 | `thm_lonely_runner_sharpness_all_n` | $\forall n \ge 1, t = p/q$, speeds $\{1,\dots,n\}$ admit $i$ with $\|t\cdot i\| \le \frac{1}{n+1}$ | Wills (1967) sharpness | `witness_lonely_runner_concrete`; `adv_lonely_runner_strict_threshold_fails` | **Exact match (over $\mathbb{Q}$)** |
| 43 | `thm_lonely_runner_n1` | Lonely Runner holds for $n = 1$ (2 runners) | Wills (1967) | Explicit time $t = 1/(2v)$ | **Exact match** |
| 44 | `thm_lonely_runner_n2` | Lonely Runner holds for $n = 2$ (3 runners) | Wills (1967) | `witness_lonely_runner_concrete` ($v_1=3, v_2=10, t=1/6$) | **Exact match** |
| 45 | `thm_lonely_runner_speed_scaling` | `FarEnough m p q v → FarEnough m p (q * k) (v * k)` ($q, k > 0$) | Standard GCD reduction | `adv_lonely_runner_bad_time_refuted` | **Exact match** |
| 46 | `thm_lonely_runner_period_shift` | `FarEnough m p q v → FarEnough m (p + q) q v` ($q > 0$) | $\mathbb{R}/\mathbb{Z}$ periodicity | Unconditional ($\forall m, p, q > 0, v$) | **Exact match** |
| 47 | `thm_lonely_runner_neg_time` | `FarEnough m p q v → FarEnough m (-p) q v` ($q > 0$) | Time-reversal symmetry | Unconditional ($\forall m, p, q > 0, v$) | **Exact match** |
| 48 | `thm_lonely_runner_n3_nondiv4` | $n=3$ (4 runners): $\forall v_1, v_2, v_3$ with $4 \nmid v_i$, $t = 1/4$ achieves gap $\ge 1/4$ | 27 of 64 speed-triple residue classes mod 4 (no speed divisible by 4), witness $t = 1/4$ | `witness_lonely_runner_n3_concrete` ($v = (1, 2, 3), t = 1/4$) | **Exact match** |
| 49 | `thm_lonely_runner_n3` | **Complete $n = 3$ (4 runners):** $\forall v_1, v_2, v_3 > 0,\ \exists t = p/q,\ \min_i \|t v_i\| \ge 1/4$ | Betke–Wills (1972); Cusick (1973) | `witness_lonely_runner_n3_div4` ($v=(3,5,60), t=61/480$) | **Exact match (complete for ALL positive triples)** |

### Domain IV: Brocard's Problem (`FormalAtlas/Brocard.lean`, 7 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 50 | `thm_brocard_brown_solutions` | $(4,5), (5,11), (7,71)$ solve $n!+1 = m^2$ | Brocard (1876), Ramanujan (1913) | Concrete Brown pairs | **Exact match** |
| 51 | `thm_brocard_exhaustive_le_12` | Sole solutions for $n \le 12$ are $(4,5), (5,11), (7,71)$ | Finite exhaustion | `witness_brocard_non_solution` ($6!+1 = 721$) | **Exact match** |
| 52 | `thm_brocard_mod4_ge_4` | $\forall n \ge 4,\ (n! + 1) \equiv 1 \pmod 4$ | Elementary modular constraint | Forces $m$ odd for $n \ge 4$ | **Exact match** |
| 53 | `thm_brocard_exhaustive_le_15` | Sole solutions for $n \le 15$ are $(4,5), (5,11), (7,71)$ | Finite exhaustion | `adv_brocard_false_candidates_refuted` | **Exact match** |
| 54 | `thm_brocard_not_div3_ge_3` | $\forall n \ge 3,\ (n! + 1) \equiv 1 \pmod 3$ | Elementary modular constraint | Excludes $3 \mid m$ for $n \ge 3$ | **Exact match** |
| 55 | `thm_brocard_mod10_ge_5` | $\forall n \ge 5,\ (n! + 1) \equiv 1 \pmod{10}$ | Elementary decimal-digit invariant | Forces $m \equiv \pm 1 \pmod{10}$ for $n \ge 5$ | **Exact match** |
| 56 | `thm_brocard_exhaustive_le_20` | Sole solutions for $n \le 20$ are $(4,5), (5,11), (7,71)$ ($20!+1 = 2.43\times 10^{18}$) | Finite exhaustion (square bracketing) | `adv_brocard_false_candidates_refuted` ($n \in \{6,8,13,16\}$) | **Exact match** |

### Domain V: Primes & Twin Prime Conjecture (`FormalAtlas/Primes.lean`, 4 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 57 | `thm_euclid_infinitely_many_primes` | $\forall N,\ \exists p > N,\ \mathrm{IsPrime}(p)$ | Euclid (*Elements* IX.20) | `adv_non_primes_refuted` ($0, 1, 9$) | **Exact match** |
| 58 | `thm_arbitrary_prime_gaps` | $\forall k \ge 1,\ \exists m \ge 2,\ \forall i < k,\ \neg\mathrm{IsPrime}(m+i)$ | Elementary $(k+1)! + 2$ construction | Unconditional ($\forall k \ge 1$) | **Exact match** |
| 59 | `thm_prime_odd_ge_3` | $\forall p \ge 3,\ \mathrm{IsPrime}(p) \implies p \equiv 1 \pmod 2$ | Elementary prime parity | `adv_non_primes_refuted` | **Exact match** |
| 60 | `thm_twin_prime_mod6` | $\forall p \ge 4,\ \mathrm{IsPrime}(p) \land \mathrm{IsPrime}(p+2) \implies p \equiv 5 \pmod 6$ | Elementary modular rigidity | `witness_twin_primes_concrete`; `adv_twin_prime_mod6_needs_ge_4` | **Exact match** |

### Domain VI: Goldbach's Conjecture (`FormalAtlas/Goldbach.lean`, 3 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 61 | `thm_goldbach_even_le_100` | Every even $4 \le n \le 100$ is a sum of two certified primes | Goldbach (1742) finite verification | `witness_goldbach_100` ($100 = 3 + 97$) | **Exact match** |
| 62 | `thm_goldbach_odd_binary_obstruction` | Any odd $n = p + q$ with $p, q$ prime satisfies $p = 2 \lor q = 2$ | Elementary parity obstruction | Paired with Theorem 63 | **Exact match** |
| 63 | `thm_goldbach_binary_fails_at_11` | $\neg \exists p, q,\ \mathrm{IsPrime}(p) \land \mathrm{IsPrime}(q) \land p + q = 11$ | Why Goldbach requires even $n$ | `adv_goldbach_requires_even` | **Exact match** |

### Domain VII: Odd Perfect Numbers & Mersenne Primes (`FormalAtlas/PerfectNumbers.lean`, 7 Theorems — Complete Euclid–Euler + Euler $2p \mid (q-1)$)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 64 | `thm_mersenne_exponent_prime` | $\forall n \ge 2,\ \mathrm{IsPrime}(2^n - 1) \implies \mathrm{IsPrime}(n)$ | Cataldi / Mersenne (1644) | `witness_mersenne_31`; `adv_mersenne_converse_false` ($2^{11}-1 = 23\times 89$) | **Exact match** |
| 65 | `thm_perfect_numbers_first_four` | $6, 28, 496, 8128$ are all perfect ($\sigma(n) = 2n$) | Euclid / Nicomachus | `adv_non_perfect_refuted` ($12, 15$) | **Exact match** |
| 66 | `thm_no_odd_perfect_le_100` | $\forall n \le 100,\ n \equiv 1 \pmod 2 \implies \neg\mathrm{IsPerfect}(n)$ | Finite odd-perfect exclusion | Exhaustive kernel check $1 \le n \le 100$ | **Exact match** |
| 67 | `thm_euclid_even_perfect` | $\forall p \ge 2,\ \mathrm{IsPrime}(2^p - 1) \implies \mathrm{IsPerfect}(2^{p-1}(2^p - 1))$ | Euclid (*Elements* IX.36) | `witness_euclid_perfect_28` | **Exact match (all $p \ge 2$)** |
| 68 | `thm_euler_even_perfect_converse` | $\forall n,\ 2 \mid n \land \mathrm{IsPerfect}(n) \implies \exists p \ge 2,\ \mathrm{IsPrime}(2^p - 1) \land n = 2^{p-1}(2^p - 1)$ | Euler (1747) even-perfect converse | `adv_even_non_mersenne_not_perfect` ($8 \cdot 15 = 120$ refuted via converse) | **Exact match (all even $n$)** |
| 69 | `thm_euclid_euler_even_perfect_iff` | $\forall n,\ 2 \mid n \implies (\mathrm{IsPerfect}(n) \iff \exists p \ge 2,\ \mathrm{IsPrime}(2^p - 1) \land n = 2^{p-1}(2^p - 1))$ | Complete Euclid–Euler Theorem | Biconditional combining Euclid IX.36 + Euler 1747 | **Exact match (complete iff)** |
| 70 | `thm_mersenne_prime_divisor_congruence` | $\forall p, q,\ \mathrm{IsPrime}(p) \land p \ge 3 \land \mathrm{IsPrime}(q) \land q \mid (2^p - 1) \implies 2p \mid (q - 1)$ | Euler (1750) Mersenne prime divisor theorem | `witness_mersenne_divisor_23_of_M11` ($23 \mid 2^{11}-1,\ 22 \mid 22$); proved via Fermat's Little Theorem + Euclidean exponent descent | **Exact match (all odd primes $p$)** |

### Domain VIII: Ramsey Theory — Exact $R(3,3) = 6$ and $R(3,4) = 9$ (`FormalAtlas/Ramsey.lean`, 4 Theorems)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity / Adversarial Guard | Status |
|---|---|---|---|---|---|
| 71 | `thm_ramsey_R33_upper` | Every 2-coloring of $K_6$ contains a monochromatic triangle | Ramsey (1930); Greenwood–Gleason (1955) | Exact $K_6$ pigeonhole upper bound $R(3,3) \le 6$ | **Exact match** |
| 72 | `thm_ramsey_R33_lower` | Explicit symmetric $C_5$ coloring of $K_5$ has zero monochromatic triangles | Greenwood–Gleason (1955) | `adv_ramsey_R33_not_le_5` — establishes exact $R(3,3) = 6$ | **Exact match** |
| 73 | `thm_ramsey_R34_upper` | Every symmetric 2-coloring of $K_9$ has a red $K_3$ or a blue $K_4$ | Greenwood–Gleason (1955) | Handshaking Lemma ($9 \times 3 = 27$ odd) — proves $R(3,4) \le 9$ | **Exact match** |
| 74 | `thm_ramsey_R34_lower` | Explicit symmetric circulant $C_8(1,4,7)$ coloring of $K_8$ has no red $K_3$ and no blue $K_4$ | Greenwood–Gleason (1955) | `adv_ramsey_R34_not_le_8` — establishes exact $R(3,4) = 9$ | **Exact match** |

## 3. Explicitly NOT Proved (Hard Epistemic Boundary)

- **Collatz Conjecture (`OPEN`):** Proved NO convergence, NO divergence exclusion, and NO general nontrivial positive-cycle exclusion for $o \ge 5, d \ge 9$ (only $o \in \{1, 2, 3, 4\}$ for all $d \ge 1$, $1 \le d \le 7$, $3 \nmid x$ for all nonzero cycles, all supercritical $2^d \le 3^o$ words, and the global Eliahou–Steiner amplitude ceiling $(2^d - 3^o)x \le 2^{d-o}(3^o - 2^o)$ are proved here).
- **Erdős–Straus Conjecture (`OPEN` / `active-progress`):** The six quadratic-residue classes $\{1, 121, 169, 289, 361, 529\} \pmod{840}$ remain uncovered for general primes; the full conjecture is NOT proved.
- **Lonely Runner Conjecture (`active-progress`):** Complete proofs through $n \le 3$ (2, 3, and 4 runners — classical: Betke–Wills 1972; Cusick 1973), global sharpness (all $n$), and the symmetry group are formalized here; not formalized here for $n \ge 4$; proved in the literature for up to 13 runners in recent preprints (`arXiv:2509.14111`, `arXiv:2511.22427`, `arXiv:2604.23906`); open in general.
- **Brocard's Problem (`OPEN`):** Only $n \le 20$ and mod-3/4/10 constraints are proved here; finiteness for all $n$ remains OPEN.
- **Twin Prime Conjecture (`active-progress`):** Infinitely many primes, arbitrary prime gaps, and mod-6 rigidity are classical; infinitely many twin primes remains OPEN.
- **Goldbach's Conjecture (`OPEN`):** Only even $4 \le n \le 100$ and the odd binary obstruction are proved here; Goldbach for all even $n \ge 4$ remains OPEN.
- **Odd Perfect Numbers & Infinitude of Mersenne Primes (`OPEN`):** Complete Euclid–Euler characterization of even perfect numbers, Euler's $2p \mid (q - 1)$ Mersenne divisor congruence, Mersenne exponent necessity, $\{6, 28, 496, 8128\}$, and odd-perfect exclusion $n \le 100$ are proved here; existence of odd perfect numbers and infinitude of Mersenne primes remain OPEN.
- **Ramsey Theory (`OPEN`):** Exact $R(3,3) = 6$ and $R(3,4) = 9$ are classical; $R(5,5)$ and diagonal asymptotics remain OPEN.

## 4. Exact Verbatim `#print axioms` Output (`VerifyAxioms.lean`, Lean 4.35.0)

Every one of the **118 audited declarations** (74 headline theorems, 20 non-vacuity witnesses, 24 adversarial false-variant refutations) depends strictly on subsets of `{propext, Classical.choice, Quot.sound}` (**16 declarations require zero axioms**):

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
'FormalAtlas.Challenge.thm_collatz_positive_cycle_has_odd_step' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positive_cycle_intercept_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positive_cycle_subcritical' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_no_positive_cycle_d1' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positive_cycle_one_odd' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positive_cycle_two_odd' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_2adic_isometry' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_periodic_spine_congruence' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_odd_unit_lock_valuation_isometry' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_fine_wilf_spine_ceiling' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_trivial_cycle_orbit' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_no_nontrivial_positive_cycle_le_7' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_no_positive_cycle_odd_le_7' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_catalytic_reversible_cylinder' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positive_cycle_three_odd' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_intercept_upper_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_cycle_amplitude_ceiling' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_sign_conjugacy' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_mod3_chiral_asymmetry' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_intercept_not_div3' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_cycle_no_div3' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positive_cycle_four_odd' depends on axioms: [propext, Classical.choice, Quot.sound]
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
'FormalAtlas.Challenge.thm_lonely_runner_n3' depends on axioms: [propext, Classical.choice, Quot.sound]
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
'FormalAtlas.Challenge.thm_euclid_even_perfect' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_euler_even_perfect_converse' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_euclid_euler_even_perfect_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_mersenne_prime_divisor_congruence' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_ramsey_R33_upper' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_ramsey_R33_lower' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_ramsey_R34_upper' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_ramsey_R34_lower' depends on axioms: [propext, Quot.sound]
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
'FormalAtlas.NonVacuity.witness_lonely_runner_n3_div4' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_euclid_perfect_28' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.NonVacuity.witness_mersenne_divisor_23_of_M11' depends on axioms: [propext, Quot.sound]
'FormalAtlas.NonVacuity.witness_collatz_two_odd_trivial_cycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.NonVacuity.witness_odd_unit_lock_fine_wilf' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_catalytic_cylinder' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.NonVacuity.witness_collatz_three_odd_trivial_cycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.NonVacuity.witness_collatz_intercept_bound_sharp' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_collatz_mod3_chiral_asymmetry' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.NonVacuity.witness_collatz_four_odd_trivial_cycle' depends on axioms: [propext, Classical.choice, Quot.sound]
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
'FormalAtlas.Adversarial.adv_ramsey_R34_not_le_8' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_no_d1_positive_fixed_point' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_no_nontrivial_low_odd_cycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_even_non_mersenne_not_perfect' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_no_odd_period_le_7' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_distinct_spines_bounded_v2' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_no_nontrivial_three_odd_cycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_intercept_bound_strict_false' does not depend on any axioms
'FormalAtlas.Adversarial.adv_collatz_no_mult3_nonzero_cycle' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Adversarial.adv_collatz_no_nontrivial_four_odd_cycle' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## 5. Multi-Kernel Replay Verdict (6/6 Independent Kernels + Live Negative Rejection)

All 74 challenge/solution theorem signatures, 20 non-vacuity witnesses, and 24 adversarial refutations (**118 declarations total**) pass all six independent Lean 4.35.0 kernels (full replay log in [`six_kernel_audit.txt`](six_kernel_audit.txt), plus `bubblewrap`-sandboxed `lake check --paranoid`, `lake comparator --config comparator.json --paranoid`, and live negative kernel rejection via `scripts/test_lean_negative.py` in Ubuntu GitHub Actions CI):
1. `lean` (C++ reference kernel, `autoImplicit = false`, commit `eb6cafb7`) — **ACCEPT**
2. `leanchecker-paranoid --fresh` — **ACCEPT**
3. `lean4lean --import` (Lean-in-Lean verified kernel) — **ACCEPT**
4. `nanoda_bin` (Rust independent kernel, strict `{propext, Classical.choice, Quot.sound}` whitelist; zero `sorryAx` even declared in minimal proof cones) — **ACCEPT**
5. `con-leche --verified` (verified Lean kernel) — **ACCEPT**
6. `con-ron --verified` (Rust arena checker) — **ACCEPT**
7. `scripts/test_lean_negative.py` (live negative kernel & axiom-gate test) — **PASS (3/3)**: actively rejects false Brocard `6!+1 = 27^2`, false Lonely Runner `1/9 >= 1/3`, and `sorry`-tampered `sorryAx` probes.
