module

-- SPDX-License-Identifier: MIT
public import FormalAtlas.Defs

/-!
# Challenge — Isolated Statement Specification for `lake comparator`

Contains ONLY the exact 22 headline theorem signatures to be judged by
`lake comparator --config comparator.json --paranoid` against `Solution.lean`.
All proofs live exclusively in `FormalAtlas.*` and are exported via `Solution.lean`.
-/

namespace FormalAtlas.Challenge

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

public theorem thm_erdos_straus_mordell_840 (n : Nat) (hn : 2 ≤ n)
    (h1 : n % 840 ≠ 1) (h2 : n % 840 ≠ 121) (h3 : n % 840 ≠ 169)
    (h4 : n % 840 ≠ 289) (h5 : n % 840 ≠ 361) (h6 : n % 840 ≠ 529) :
    HasErdosStraus n := sorry

public theorem thm_erdos_straus_multiplicative_closure (m k : Nat) (hk : 0 < k)
    (hm : HasErdosStraus m) : HasErdosStraus (m * k) := sorry

public theorem thm_erdos_straus_mordell_exceptions_small :
    HasErdosStraus 121 ∧ HasErdosStraus 169 ∧ HasErdosStraus 289 ∧
    HasErdosStraus 361 ∧ HasErdosStraus 529 ∧ HasErdosStraus 841 := sorry

public theorem thm_lonely_runner_sharpness_all_n (n : Nat) (hn : 1 ≤ n) (p q : Int) (hq : 0 < q) :
    ∃ i : Nat, 1 ≤ i ∧ i ≤ n ∧ WithinDist ((n : Int) + 1) p q (i : Int) := sorry

public theorem thm_lonely_runner_n1 (v : Int) (hv : 0 < v) :
    ∃ p q : Int, 0 < q ∧ FarEnough 2 p q v := sorry

public theorem thm_lonely_runner_n2 (v1 v2 : Int) (hv1 : 0 < v1) (hv2 : 0 < v2) :
    ∃ p q : Int, 0 < q ∧ FarEnough 3 p q v1 ∧ FarEnough 3 p q v2 := sorry

public theorem thm_lonely_runner_speed_scaling (m p q v k : Int)
    (hq : 0 < q) (hk : 0 < k) (h : FarEnough m p q v) :
    FarEnough m p (q * k) (v * k) := sorry

public theorem thm_brocard_brown_solutions :
    IsBrocardSol 4 5 ∧ IsBrocardSol 5 11 ∧ IsBrocardSol 7 71 := sorry

public theorem thm_brocard_exhaustive_le_12 (n m : Nat) (hn : n ≤ 12) (h : IsBrocardSol n m) :
    (n = 4 ∧ m = 5) ∨ (n = 5 ∧ m = 11) ∨ (n = 7 ∧ m = 71) := sorry

public theorem thm_brocard_mod4_ge_4 (n : Nat) (hn : 4 ≤ n) :
    (fact n + 1) % 4 = 1 := sorry

public theorem thm_brocard_exhaustive_le_15 (n m : Nat) (hn : n ≤ 15) (h : IsBrocardSol n m) :
    (n = 4 ∧ m = 5) ∨ (n = 5 ∧ m = 11) ∨ (n = 7 ∧ m = 71) := sorry

end FormalAtlas.Challenge
