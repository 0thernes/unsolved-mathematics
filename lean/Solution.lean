module

-- SPDX-License-Identifier: MIT
public import FormalAtlas.Defs
import FormalAtlas

/-!
# Solution — Zero-Sorry Proofs Matching `Challenge.lean` (`v0.5.0`)

Exports all 45 headline theorems across 8 open-problem domains in `FormalAtlas.Challenge`
with exact signature match for `lake comparator --config comparator.json --paranoid`.
-/

namespace FormalAtlas.Challenge

-- I. Collatz (14)
public theorem thm_collatz_cylinder_affine_law (d : Nat) (q r : Int) :
    iter T d ((2 : Int) ^ d * q + r) =
      (3 : Int) ^ (oddCount T d r) * q + iter T d r :=
  collatz_cylinder_affine_law d q r

public theorem thm_collatz_exact_intercept_law (d : Nat) (x : Int) :
    (2 : Int) ^ d * iter T d x =
      (3 : Int) ^ (oddCount T d x) * x + wordIntercept (parityWord T d x) :=
  collatz_exact_intercept_law d x

public theorem thm_terras_parity_word_bijection (d : Nat) :
    (∀ x y : Int, 0 ≤ x → x < (2 : Int) ^ d → 0 ≤ y → y < (2 : Int) ^ d →
      parityWord T d x = parityWord T d y → x = y) ∧
    (∀ w : List Bool, w.length = d →
      ∃ r : Int, 0 ≤ r ∧ r < (2 : Int) ^ d ∧ parityWord T d r = w) :=
  terras_parity_word_bijection d

public theorem thm_collatz_descent_certificate_sound (d : Nat) (q r : Int)
    (hsub : (3 : Int) ^ (oddCount T d r) < (2 : Int) ^ d)
    (hq : iter T d r - r < ((2 : Int) ^ d - (3 : Int) ^ (oddCount T d r)) * q) :
    iter T d ((2 : Int) ^ d * q + r) < (2 : Int) ^ d * q + r :=
  collatz_descent_certificate_sound d q r hsub hq

public theorem thm_collatz_no_finite_subcritical_cover (d : Nat) :
    iter T d (-1) = -1 ∧
    oddCount T d (-1) = d ∧
    (2 : Int) ^ d ≤ (3 : Int) ^ (oddCount T d (-1)) :=
  collatz_no_finite_subcritical_cover d

public theorem thm_collatz_spine_ladder_identity (d : Nat) (x : Int) :
    let o := oddCount T d x
    let c := wordIntercept (parityWord T d x)
    (2 : Int) ^ d * (((2 : Int) ^ d - (3 : Int) ^ o) * iter T d x - c) =
      (3 : Int) ^ o * (((2 : Int) ^ d - (3 : Int) ^ o) * x - c) :=
  collatz_spine_ladder_identity d x

public theorem thm_collatz_positivity_localization (w : List Bool)
    (hsuper : (2 : Int) ^ w.length < (3 : Int) ^ wordOddCount w) :
    (3 : Int) ^ wordOddCount w - (2 : Int) ^ w.length ≤ wordIntercept w :=
  collatz_positivity_localization w hsuper

public theorem thm_collatz_epsilon_invariance_barrier :
    (∀ d : Nat,
      (∀ x y : Int, 0 ≤ x → x < (2 : Int) ^ d → 0 ≤ y → y < (2 : Int) ^ d →
        parityWord TMinus d x = parityWord TMinus d y → x = y) ∧
      (∀ w : List Bool, w.length = d →
        ∃ r : Int, 0 ≤ r ∧ r < (2 : Int) ^ d ∧ parityWord TMinus d r = w)) ∧
    (iter TMinus 3 5 = 5 ∧ (2 : Int) ^ 3 < (3 : Int) ^ (oddCount TMinus 3 5)) ∧
    (iter TMinus 11 17 = 17 ∧ (2 : Int) ^ 11 < (3 : Int) ^ (oddCount TMinus 11 17)) :=
  collatz_epsilon_invariance_barrier

public theorem thm_collatz_cycle_equation (d : Nat) (x : Int) (hcyc : iter T d x = x) :
    ((2 : Int) ^ d - (3 : Int) ^ (oddCount T d x)) * x = wordIntercept (parityWord T d x) :=
  collatz_cycle_equation d x hcyc

public theorem thm_collatz_parity_word_append (f : Int → Int) (d1 d2 : Nat) (x : Int) :
    parityWord f (d1 + d2) x = parityWord f d1 x ++ parityWord f d2 (iter f d1 x) :=
  collatz_parity_word_append f d1 d2 x

public theorem thm_collatz_negative_cycles :
    (iter T 3 (-5) = -5 ∧ (2 : Int) ^ 3 < (3 : Int) ^ (oddCount T 3 (-5))) ∧
    (iter T 11 (-17) = -17 ∧ (2 : Int) ^ 11 < (3 : Int) ^ (oddCount T 11 (-17))) :=
  collatz_negative_cycles

public theorem thm_collatz_zero_fixed_point (d : Nat) :
    iter T d 0 = 0 ∧ oddCount T d 0 = 0 :=
  collatz_zero_fixed_point d

public theorem thm_collatz_intercept_nonneg (w : List Bool) :
    0 ≤ wordIntercept w :=
  collatz_intercept_nonneg w

public theorem thm_collatz_parity_word_length (f : Int → Int) (d : Nat) (x : Int) :
    (parityWord f d x).length = d :=
  collatz_parity_word_length f d x

-- II. Erdős–Straus (5)
public theorem thm_erdos_straus_mordell_840 (n : Nat) (hn : 2 ≤ n)
    (h1 : n % 840 ≠ 1) (h2 : n % 840 ≠ 121) (h3 : n % 840 ≠ 169)
    (h4 : n % 840 ≠ 289) (h5 : n % 840 ≠ 361) (h6 : n % 840 ≠ 529) :
    HasErdosStraus n :=
  erdos_straus_mordell_840 n hn h1 h2 h3 h4 h5 h6

public theorem thm_erdos_straus_multiplicative_closure (m k : Nat) (hk : 0 < k)
    (hm : HasErdosStraus m) : HasErdosStraus (m * k) :=
  erdos_straus_multiplicative_closure m k hk hm

public theorem thm_erdos_straus_mordell_exceptions_small :
    HasErdosStraus 121 ∧ HasErdosStraus 169 ∧ HasErdosStraus 289 ∧
    HasErdosStraus 361 ∧ HasErdosStraus 529 ∧ HasErdosStraus 841 :=
  erdos_straus_mordell_exceptions_small

public theorem thm_erdos_straus_symmetry (n x y z : Nat) (h : IsErdosStrausSol n x y z) :
    IsErdosStrausSol n y z x :=
  erdos_straus_symmetry n x y z h

public theorem thm_erdos_straus_all_le_30 (n : Nat) (hlo : 2 ≤ n) (hhi : n ≤ 30) :
    HasErdosStraus n :=
  erdos_straus_all_le_30 n hlo hhi

-- III. Lonely Runner (7)
public theorem thm_lonely_runner_sharpness_all_n (n : Nat) (hn : 1 ≤ n) (p q : Int) (hq : 0 < q) :
    ∃ i : Nat, 1 ≤ i ∧ i ≤ n ∧ WithinDist ((n : Int) + 1) p q (i : Int) :=
  lonely_runner_sharpness_all_n n hn p q hq

public theorem thm_lonely_runner_n1 (v : Int) (hv : 0 < v) :
    ∃ p q : Int, 0 < q ∧ FarEnough 2 p q v :=
  lonely_runner_n1 v hv

public theorem thm_lonely_runner_n2 (v1 v2 : Int) (hv1 : 0 < v1) (hv2 : 0 < v2) :
    ∃ p q : Int, 0 < q ∧ FarEnough 3 p q v1 ∧ FarEnough 3 p q v2 :=
  lonely_runner_n2 v1 v2 hv1 hv2

public theorem thm_lonely_runner_speed_scaling (m p q v k : Int)
    (hq : 0 < q) (hk : 0 < k) (h : FarEnough m p q v) :
    FarEnough m p (q * k) (v * k) :=
  lonely_runner_speed_scaling m p q v k hq hk h

public theorem thm_lonely_runner_period_shift (m p q v : Int) (h : FarEnough m p q v) :
    FarEnough m (p + q) q v :=
  lonely_runner_period_shift m p q v h

public theorem thm_lonely_runner_neg_time (m p q v : Int) (hq : 0 < q) (h : FarEnough m p q v) :
    FarEnough m (-p) q v :=
  lonely_runner_neg_time m p q v hq h

public theorem thm_lonely_runner_n3_nondiv4 (v1 v2 v3 : Int)
    (h1 : v1 % 4 ≠ 0) (h2 : v2 % 4 ≠ 0) (h3 : v3 % 4 ≠ 0) :
    ∃ p q : Int, 0 < q ∧ FarEnough 4 p q v1 ∧ FarEnough 4 p q v2 ∧ FarEnough 4 p q v3 :=
  lonely_runner_n3_nondiv4 v1 v2 v3 h1 h2 h3

-- IV. Brocard (7)
public theorem thm_brocard_brown_solutions :
    IsBrocardSol 4 5 ∧ IsBrocardSol 5 11 ∧ IsBrocardSol 7 71 :=
  brocard_brown_solutions

public theorem thm_brocard_exhaustive_le_12 (n m : Nat) (hn : n ≤ 12) (h : IsBrocardSol n m) :
    (n = 4 ∧ m = 5) ∨ (n = 5 ∧ m = 11) ∨ (n = 7 ∧ m = 71) :=
  brocard_exhaustive_le_12 n m hn h

public theorem thm_brocard_mod4_ge_4 (n : Nat) (hn : 4 ≤ n) :
    (fact n + 1) % 4 = 1 :=
  brocard_mod4_ge_4 n hn

public theorem thm_brocard_exhaustive_le_15 (n m : Nat) (hn : n ≤ 15) (h : IsBrocardSol n m) :
    (n = 4 ∧ m = 5) ∨ (n = 5 ∧ m = 11) ∨ (n = 7 ∧ m = 71) :=
  brocard_exhaustive_le_15 n m hn h

public theorem thm_brocard_not_div3_ge_3 (n : Nat) (hn : 3 ≤ n) :
    (fact n + 1) % 3 = 1 :=
  brocard_not_div3_ge_3 n hn

public theorem thm_brocard_mod10_ge_5 (n : Nat) (hn : 5 ≤ n) :
    (fact n + 1) % 10 = 1 :=
  brocard_mod10_ge_5 n hn

public theorem thm_brocard_exhaustive_le_20 (n m : Nat) (hn : n ≤ 20) (h : IsBrocardSol n m) :
    (n = 4 ∧ m = 5) ∨ (n = 5 ∧ m = 11) ∨ (n = 7 ∧ m = 71) :=
  brocard_exhaustive_le_20 n m hn h

-- V. Primes & Twin Primes (4)
public theorem thm_euclid_infinitely_many_primes (N : Nat) :
    ∃ p : Nat, N < p ∧ IsPrime p :=
  euclid_infinitely_many_primes N

public theorem thm_arbitrary_prime_gaps (k : Nat) (hk : 1 ≤ k) :
    ∃ m : Nat, 2 ≤ m ∧ ∀ i : Nat, i < k → ¬ IsPrime (m + i) :=
  arbitrary_prime_gaps k hk

public theorem thm_prime_odd_ge_3 (p : Nat) (hp : IsPrime p) (h3 : 3 ≤ p) :
    p % 2 = 1 :=
  prime_odd_ge_3 p hp h3

public theorem thm_twin_prime_mod6 (p : Nat) (hp : IsPrime p) (hp2 : IsPrime (p + 2)) (h4 : 4 ≤ p) :
    p % 6 = 5 :=
  twin_prime_mod6 p hp hp2 h4

-- VI. Goldbach (3)
public theorem thm_goldbach_even_le_100 (n : Nat) (hlo : 4 ≤ n) (hhi : n ≤ 100) (heven : n % 2 = 0) :
    ∃ p q : Nat, IsPrime p ∧ IsPrime q ∧ p + q = n :=
  goldbach_even_le_100 n hlo hhi heven

public theorem thm_goldbach_odd_binary_obstruction (n p q : Nat)
    (hodd : n % 2 = 1) (hp : IsPrime p) (hq : IsPrime q) (hsum : p + q = n) :
    p = 2 ∨ q = 2 :=
  goldbach_odd_binary_obstruction n p q hodd hp hq hsum

public theorem thm_goldbach_binary_fails_at_11 :
    ¬ (∃ p q : Nat, IsPrime p ∧ IsPrime q ∧ p + q = 11) :=
  goldbach_binary_fails_at_11

-- VII. Odd Perfect & Mersenne (3)
public theorem thm_mersenne_exponent_prime (n : Nat) (hn : 2 ≤ n) (hm : IsPrime (2 ^ n - 1)) :
    IsPrime n :=
  mersenne_exponent_prime n hn hm

public theorem thm_perfect_numbers_first_four :
    IsPerfect 6 ∧ IsPerfect 28 ∧ IsPerfect 496 ∧ IsPerfect 8128 :=
  perfect_numbers_first_four

public theorem thm_no_odd_perfect_le_100 (n : Nat) (hle : n ≤ 100) (hodd : n % 2 = 1) :
    ¬ IsPerfect n :=
  no_odd_perfect_le_100 n hle hodd

-- VIII. Ramsey R(3,3) = 6 (2)
public theorem thm_ramsey_R33_upper (c : Fin 6 → Fin 6 → Bool) :
    HasMonoTriangle c :=
  ramsey_R33_upper c

public theorem thm_ramsey_R33_lower :
    ∃ c : Fin 5 → Fin 5 → Bool, (∀ i j : Fin 5, c i j = c j i) ∧ ¬ HasMonoTriangle c :=
  ⟨c5Color, ramsey_R33_lower⟩

end FormalAtlas.Challenge
