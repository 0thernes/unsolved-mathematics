module

-- SPDX-License-Identifier: MIT
public import FormalAtlas.Defs

/-!
# Challenge — Isolated Statement Specification for `lake comparator` (`v0.10.0`)

Contains ONLY the exact 74 headline theorem signatures across 8 open-problem domains
to be judged by `lake comparator --config comparator.json --paranoid` against `Solution.lean`.
All proofs live exclusively in `FormalAtlas.*` and are exported via `Solution.lean`.
-/

namespace FormalAtlas.Challenge

-- ============================================================================
-- I. Collatz Conjecture & 3n-1 Sibling Control (36 theorems)
-- ============================================================================

public theorem thm_collatz_cylinder_affine_law (d : Nat) (q r : Int) :
    iter T d ((2 : Int) ^ d * q + r) =
      (3 : Int) ^ (oddCount T d r) * q + iter T d r := sorry

public theorem thm_collatz_exact_intercept_law (d : Nat) (x : Int) :
    (2 : Int) ^ d * iter T d x =
      (3 : Int) ^ (oddCount T d x) * x + wordIntercept (parityWord T d x) := sorry

public theorem thm_terras_parity_word_bijection (d : Nat) :
    (∀ x y : Int, 0 ≤ x → x < (2 : Int) ^ d → 0 ≤ y → y < (2 : Int) ^ d →
      parityWord T d x = parityWord T d y → x = y) ∧
    (∀ w : List Bool, w.length = d →
      ∃ r : Int, 0 ≤ r ∧ r < (2 : Int) ^ d ∧ parityWord T d r = w) := sorry

public theorem thm_collatz_descent_certificate_sound (d : Nat) (q r : Int)
    (hsub : (3 : Int) ^ (oddCount T d r) < (2 : Int) ^ d)
    (hq : iter T d r - r < ((2 : Int) ^ d - (3 : Int) ^ (oddCount T d r)) * q) :
    iter T d ((2 : Int) ^ d * q + r) < (2 : Int) ^ d * q + r := sorry

public theorem thm_collatz_no_finite_subcritical_cover (d : Nat) :
    iter T d (-1) = -1 ∧
    oddCount T d (-1) = d ∧
    (2 : Int) ^ d ≤ (3 : Int) ^ (oddCount T d (-1)) := sorry

public theorem thm_collatz_spine_ladder_identity (d : Nat) (x : Int) :
    let o := oddCount T d x
    let c := wordIntercept (parityWord T d x)
    (2 : Int) ^ d * (((2 : Int) ^ d - (3 : Int) ^ o) * iter T d x - c) =
      (3 : Int) ^ o * (((2 : Int) ^ d - (3 : Int) ^ o) * x - c) := sorry

public theorem thm_collatz_positivity_localization (w : List Bool)
    (hsuper : (2 : Int) ^ w.length < (3 : Int) ^ wordOddCount w) :
    (3 : Int) ^ wordOddCount w - (2 : Int) ^ w.length ≤ wordIntercept w := sorry

public theorem thm_collatz_epsilon_invariance_barrier :
    (∀ d : Nat,
      (∀ x y : Int, 0 ≤ x → x < (2 : Int) ^ d → 0 ≤ y → y < (2 : Int) ^ d →
        parityWord TMinus d x = parityWord TMinus d y → x = y) ∧
      (∀ w : List Bool, w.length = d →
        ∃ r : Int, 0 ≤ r ∧ r < (2 : Int) ^ d ∧ parityWord TMinus d r = w)) ∧
    (iter TMinus 3 5 = 5 ∧ (2 : Int) ^ 3 < (3 : Int) ^ (oddCount TMinus 3 5)) ∧
    (iter TMinus 11 17 = 17 ∧ (2 : Int) ^ 11 < (3 : Int) ^ (oddCount TMinus 11 17)) := sorry

public theorem thm_collatz_cycle_equation (d : Nat) (x : Int) (hcyc : iter T d x = x) :
    ((2 : Int) ^ d - (3 : Int) ^ (oddCount T d x)) * x = wordIntercept (parityWord T d x) := sorry

public theorem thm_collatz_parity_word_append (f : Int → Int) (d1 d2 : Nat) (x : Int) :
    parityWord f (d1 + d2) x = parityWord f d1 x ++ parityWord f d2 (iter f d1 x) := sorry

public theorem thm_collatz_negative_cycles :
    (iter T 3 (-5) = -5 ∧ (2 : Int) ^ 3 < (3 : Int) ^ (oddCount T 3 (-5))) ∧
    (iter T 11 (-17) = -17 ∧ (2 : Int) ^ 11 < (3 : Int) ^ (oddCount T 11 (-17))) := sorry

public theorem thm_collatz_zero_fixed_point (d : Nat) :
    iter T d 0 = 0 ∧ oddCount T d 0 = 0 := sorry

public theorem thm_collatz_intercept_nonneg (w : List Bool) :
    0 ≤ wordIntercept w := sorry

public theorem thm_collatz_parity_word_length (f : Int → Int) (d : Nat) (x : Int) :
    (parityWord f d x).length = d := sorry

public theorem thm_collatz_positive_cycle_has_odd_step (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) :
    1 ≤ oddCount T d x := sorry

public theorem thm_collatz_positive_cycle_intercept_pos (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) :
    0 < wordIntercept (parityWord T d x) := sorry

public theorem thm_collatz_positive_cycle_subcritical (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) :
    (3 : Int) ^ (oddCount T d x) < (2 : Int) ^ d ∧
    (2 : Int) ^ d - (3 : Int) ^ (oddCount T d x) ≤ wordIntercept (parityWord T d x) := sorry

public theorem thm_collatz_no_positive_cycle_d1 (x : Int) (hx : 0 < x) :
    iter T 1 x ≠ x := sorry

public theorem thm_collatz_positive_cycle_one_odd (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) (ho : oddCount T d x = 1) :
    d = 2 ∧ (x = 1 ∨ x = 2) := sorry

public theorem thm_collatz_positive_cycle_two_odd (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) (ho : oddCount T d x = 2) :
    d = 4 ∧ (x = 1 ∨ x = 2) := sorry

public theorem thm_collatz_2adic_isometry (d : Nat) (x y : Int) :
    parityWord T d x = parityWord T d y ↔ (x - y) % ((2 : Int) ^ d) = 0 := sorry

public theorem thm_collatz_periodic_spine_congruence (w : List Bool) (k : Nat) (x : Int)
    (hw : 1 ≤ w.length) :
    (spineDenom w * x - wordIntercept w) % ((2 : Int) ^ k) = 0 ↔
      parityWord T k x = periodicPrefix w k := sorry

public theorem thm_collatz_odd_unit_lock_valuation_isometry (w v : List Bool) (k : Nat)
    (hw : 1 ≤ w.length) (hv : 1 ≤ v.length) :
    (wordIntercept w * spineDenom v - wordIntercept v * spineDenom w) % ((2 : Int) ^ k) = 0 ↔
      periodicPrefix w k = periodicPrefix v k := sorry

public theorem thm_collatz_fine_wilf_spine_ceiling (w v : List Bool)
    (hw : 1 ≤ w.length) (hv : 1 ≤ v.length)
    (hne : wordIntercept w * spineDenom v ≠ wordIntercept v * spineDenom w) :
    (wordIntercept w * spineDenom v - wordIntercept v * spineDenom w) %
      ((2 : Int) ^ (w.length + v.length - Nat.gcd w.length v.length)) ≠ 0 := sorry

public theorem thm_collatz_trivial_cycle_orbit (k : Nat) :
    iter T (2 * k) 1 = 1 ∧ iter T (2 * k + 1) 1 = 2 ∧
    iter T (2 * k) 2 = 2 ∧ iter T (2 * k + 1) 2 = 1 := sorry

public theorem thm_collatz_no_nontrivial_positive_cycle_le_7 (d : Nat) (x : Int)
    (hd1 : 1 ≤ d) (hd7 : d ≤ 7) (hx : 0 < x) (hcyc : iter T d x = x) :
    x = 1 ∨ x = 2 := sorry

public theorem thm_collatz_no_positive_cycle_odd_le_7 (d : Nat) (x : Int)
    (hd1 : 1 ≤ d) (hd7 : d ≤ 7) (hodd : d % 2 = 1) (hx : 0 < x) :
    iter T d x ≠ x := sorry

public theorem thm_collatz_catalytic_reversible_cylinder (d : Nat) (q r acc cat : Int) :
    catCollatzStep d q r acc cat = (acc + iter T d ((2 : Int) ^ d * q + r), cat) := sorry

public theorem thm_collatz_positive_cycle_three_odd (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) (ho : oddCount T d x = 3) :
    d = 6 ∧ (x = 1 ∨ x = 2) := sorry

public theorem thm_collatz_intercept_upper_bound (w : List Bool) :
    wordIntercept w ≤ (2 : Int) ^ (w.length - wordOddCount w) *
      ((3 : Int) ^ (wordOddCount w) - (2 : Int) ^ (wordOddCount w)) := sorry

public theorem thm_collatz_cycle_amplitude_ceiling (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) :
    let o := oddCount T d x
    ((2 : Int) ^ d - (3 : Int) ^ o) * x ≤
      (2 : Int) ^ (d - o) * ((3 : Int) ^ o - (2 : Int) ^ o) := sorry

public theorem thm_collatz_sign_conjugacy (d : Nat) (x : Int) :
    iter T d (-x) = - iter TMinus d x ∧ oddCount T d (-x) = oddCount TMinus d x := sorry

public theorem thm_collatz_mod3_chiral_asymmetry (x : Int) (hodd : x % 2 ≠ 0) :
    T x % 3 = 2 ∧ TMinus x % 3 = 1 := sorry

public theorem thm_collatz_intercept_not_div3 (w : List Bool) (ho : 1 ≤ wordOddCount w) :
    wordIntercept w % 3 ≠ 0 := sorry

public theorem thm_collatz_cycle_no_div3 (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : x ≠ 0) (hcyc : iter T d x = x) :
    x % 3 ≠ 0 := sorry

public theorem thm_collatz_positive_cycle_four_odd (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) (ho : oddCount T d x = 4) :
    d = 8 ∧ (x = 1 ∨ x = 2) := sorry

-- ============================================================================
-- II. Erdős–Straus Conjecture (5 theorems)
-- ============================================================================

public theorem thm_erdos_straus_mordell_840 (n : Nat) (hn : 2 ≤ n)
    (h1 : n % 840 ≠ 1) (h2 : n % 840 ≠ 121) (h3 : n % 840 ≠ 169)
    (h4 : n % 840 ≠ 289) (h5 : n % 840 ≠ 361) (h6 : n % 840 ≠ 529) :
    HasErdosStraus n := sorry

public theorem thm_erdos_straus_multiplicative_closure (m k : Nat) (hk : 0 < k)
    (hm : HasErdosStraus m) : HasErdosStraus (m * k) := sorry

public theorem thm_erdos_straus_mordell_exceptions_small :
    HasErdosStraus 121 ∧ HasErdosStraus 169 ∧ HasErdosStraus 289 ∧
    HasErdosStraus 361 ∧ HasErdosStraus 529 ∧ HasErdosStraus 841 := sorry

public theorem thm_erdos_straus_symmetry (n x y z : Nat) (h : IsErdosStrausSol n x y z) :
    IsErdosStrausSol n y z x := sorry

public theorem thm_erdos_straus_all_le_30 (n : Nat) (hlo : 2 ≤ n) (hhi : n ≤ 30) :
    HasErdosStraus n := sorry

-- ============================================================================
-- III. Lonely Runner Conjecture (8 theorems — complete through n = 3)
-- ============================================================================

public theorem thm_lonely_runner_sharpness_all_n (n : Nat) (hn : 1 ≤ n) (p q : Int) (hq : 0 < q) :
    ∃ i : Nat, 1 ≤ i ∧ i ≤ n ∧ WithinDist ((n : Int) + 1) p q (i : Int) := sorry

public theorem thm_lonely_runner_n1 (v : Int) (hv : 0 < v) :
    ∃ p q : Int, 0 < q ∧ FarEnough 2 p q v := sorry

public theorem thm_lonely_runner_n2 (v1 v2 : Int) (hv1 : 0 < v1) (hv2 : 0 < v2) :
    ∃ p q : Int, 0 < q ∧ FarEnough 3 p q v1 ∧ FarEnough 3 p q v2 := sorry

public theorem thm_lonely_runner_speed_scaling (m p q v k : Int)
    (hq : 0 < q) (hk : 0 < k) (h : FarEnough m p q v) :
    FarEnough m p (q * k) (v * k) := sorry

public theorem thm_lonely_runner_period_shift (m p q v : Int) (h : FarEnough m p q v) :
    FarEnough m (p + q) q v := sorry

public theorem thm_lonely_runner_neg_time (m p q v : Int) (hq : 0 < q) (h : FarEnough m p q v) :
    FarEnough m (-p) q v := sorry

public theorem thm_lonely_runner_n3_nondiv4 (v1 v2 v3 : Int)
    (h1 : v1 % 4 ≠ 0) (h2 : v2 % 4 ≠ 0) (h3 : v3 % 4 ≠ 0) :
    ∃ p q : Int, 0 < q ∧ FarEnough 4 p q v1 ∧ FarEnough 4 p q v2 ∧ FarEnough 4 p q v3 := sorry

public theorem thm_lonely_runner_n3 (v1 v2 v3 : Int) (hv1 : 0 < v1) (hv2 : 0 < v2) (hv3 : 0 < v3) :
    ∃ p q : Int, 0 < q ∧ FarEnough 4 p q v1 ∧ FarEnough 4 p q v2 ∧ FarEnough 4 p q v3 := sorry

-- ============================================================================
-- IV. Brocard's Problem (7 theorems)
-- ============================================================================

public theorem thm_brocard_brown_solutions :
    IsBrocardSol 4 5 ∧ IsBrocardSol 5 11 ∧ IsBrocardSol 7 71 := sorry

public theorem thm_brocard_exhaustive_le_12 (n m : Nat) (hn : n ≤ 12) (h : IsBrocardSol n m) :
    (n = 4 ∧ m = 5) ∨ (n = 5 ∧ m = 11) ∨ (n = 7 ∧ m = 71) := sorry

public theorem thm_brocard_mod4_ge_4 (n : Nat) (hn : 4 ≤ n) :
    (fact n + 1) % 4 = 1 := sorry

public theorem thm_brocard_exhaustive_le_15 (n m : Nat) (hn : n ≤ 15) (h : IsBrocardSol n m) :
    (n = 4 ∧ m = 5) ∨ (n = 5 ∧ m = 11) ∨ (n = 7 ∧ m = 71) := sorry

public theorem thm_brocard_not_div3_ge_3 (n : Nat) (hn : 3 ≤ n) :
    (fact n + 1) % 3 = 1 := sorry

public theorem thm_brocard_mod10_ge_5 (n : Nat) (hn : 5 ≤ n) :
    (fact n + 1) % 10 = 1 := sorry

public theorem thm_brocard_exhaustive_le_20 (n m : Nat) (hn : n ≤ 20) (h : IsBrocardSol n m) :
    (n = 4 ∧ m = 5) ∨ (n = 5 ∧ m = 11) ∨ (n = 7 ∧ m = 71) := sorry

-- ============================================================================
-- V. Prime Infinitude, Prime Gaps & Twin Primes (4 theorems)
-- ============================================================================

public theorem thm_euclid_infinitely_many_primes (N : Nat) :
    ∃ p : Nat, N < p ∧ IsPrime p := sorry

public theorem thm_arbitrary_prime_gaps (k : Nat) (hk : 1 ≤ k) :
    ∃ m : Nat, 2 ≤ m ∧ ∀ i : Nat, i < k → ¬ IsPrime (m + i) := sorry

public theorem thm_prime_odd_ge_3 (p : Nat) (hp : IsPrime p) (h3 : 3 ≤ p) :
    p % 2 = 1 := sorry

public theorem thm_twin_prime_mod6 (p : Nat) (hp : IsPrime p) (hp2 : IsPrime (p + 2)) (h4 : 4 ≤ p) :
    p % 6 = 5 := sorry

-- ============================================================================
-- VI. Goldbach's Conjecture (3 theorems)
-- ============================================================================

public theorem thm_goldbach_even_le_100 (n : Nat) (hlo : 4 ≤ n) (hhi : n ≤ 100) (heven : n % 2 = 0) :
    ∃ p q : Nat, IsPrime p ∧ IsPrime q ∧ p + q = n := sorry

public theorem thm_goldbach_odd_binary_obstruction (n p q : Nat)
    (hodd : n % 2 = 1) (hp : IsPrime p) (hq : IsPrime q) (hsum : p + q = n) :
    p = 2 ∨ q = 2 := sorry

public theorem thm_goldbach_binary_fails_at_11 :
    ¬ (∃ p q : Nat, IsPrime p ∧ IsPrime q ∧ p + q = 11) := sorry

-- ============================================================================
-- VII. Odd Perfect Numbers & Mersenne Primes (7 theorems)
-- ============================================================================

public theorem thm_mersenne_exponent_prime (n : Nat) (hn : 2 ≤ n) (hm : IsPrime (2 ^ n - 1)) :
    IsPrime n := sorry

public theorem thm_perfect_numbers_first_four :
    IsPerfect 6 ∧ IsPerfect 28 ∧ IsPerfect 496 ∧ IsPerfect 8128 := sorry

public theorem thm_no_odd_perfect_le_100 (n : Nat) (hle : n ≤ 100) (hodd : n % 2 = 1) :
    ¬ IsPerfect n := sorry

public theorem thm_euclid_even_perfect (p : Nat) (hp : 2 ≤ p) (hmp : IsPrime (2 ^ p - 1)) :
    IsPerfect (2 ^ (p - 1) * (2 ^ p - 1)) := sorry

public theorem thm_euler_even_perfect_converse (n : Nat) (heven : n % 2 = 0) (hperf : IsPerfect n) :
    ∃ p : Nat, 2 ≤ p ∧ IsPrime (2 ^ p - 1) ∧ n = 2 ^ (p - 1) * (2 ^ p - 1) := sorry

public theorem thm_euclid_euler_even_perfect_iff (n : Nat) (heven : n % 2 = 0) :
    IsPerfect n ↔ ∃ p : Nat, 2 ≤ p ∧ IsPrime (2 ^ p - 1) ∧ n = 2 ^ (p - 1) * (2 ^ p - 1) := sorry

public theorem thm_mersenne_prime_divisor_congruence (p q : Nat)
    (hp : IsPrime p) (hp3 : 3 ≤ p) (hq : IsPrime q) (hdvd : q ∣ 2 ^ p - 1) :
    2 * p ∣ q - 1 := sorry

-- ============================================================================
-- VIII. Ramsey Theory — Exact R(3, 3) = 6 and R(3, 4) = 9 (4 theorems)
-- ============================================================================

public theorem thm_ramsey_R33_upper (c : Fin 6 → Fin 6 → Bool) :
    HasMonoTriangle c := sorry

public theorem thm_ramsey_R33_lower :
    ∃ c : Fin 5 → Fin 5 → Bool, (∀ i j : Fin 5, c i j = c j i) ∧ ¬ HasMonoTriangle c := sorry

public theorem thm_ramsey_R34_upper (c : Fin 9 → Fin 9 → Bool) (hsym : ∀ i j, c i j = c j i) :
    HasColorTriangle c true ∨ HasColorK4 c false := sorry

public theorem thm_ramsey_R34_lower :
    ∃ c : Fin 8 → Fin 8 → Bool, (∀ i j : Fin 8, c i j = c j i) ∧
      ¬ HasColorTriangle c true ∧ ¬ HasColorK4 c false := sorry

end FormalAtlas.Challenge
