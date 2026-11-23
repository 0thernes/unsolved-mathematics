module

public import FormalAtlas.Defs
import FormalAtlas

/-!
# Solution — Zero-Sorry Proofs Matching `Challenge.lean`

Exports all 14 headline theorems in `FormalAtlas.Challenge` namespace with
exact signature match for `lake comparator --config comparator.json --paranoid`.
-/

namespace FormalAtlas.Challenge

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

public theorem thm_erdos_straus_mordell_840 (n : Nat) (hn : 2 ≤ n)
    (h1 : n % 840 ≠ 1) (h2 : n % 840 ≠ 121) (h3 : n % 840 ≠ 169)
    (h4 : n % 840 ≠ 289) (h5 : n % 840 ≠ 361) (h6 : n % 840 ≠ 529) :
    HasErdosStraus n :=
  erdos_straus_mordell_840 n hn h1 h2 h3 h4 h5 h6

public theorem thm_lonely_runner_sharpness_all_n (n : Nat) (hn : 1 ≤ n) (p q : Int) (hq : 0 < q) :
    ∃ i : Nat, 1 ≤ i ∧ i ≤ n ∧ WithinDist ((n : Int) + 1) p q (i : Int) :=
  lonely_runner_sharpness_all_n n hn p q hq

public theorem thm_lonely_runner_n1 (v : Int) (hv : 0 < v) :
    ∃ p q : Int, 0 < q ∧ FarEnough 2 p q v :=
  lonely_runner_n1 v hv

public theorem thm_lonely_runner_n2 (v1 v2 : Int) (hv1 : 0 < v1) (hv2 : 0 < v2) :
    ∃ p q : Int, 0 < q ∧ FarEnough 3 p q v1 ∧ FarEnough 3 p q v2 :=
  lonely_runner_n2 v1 v2 hv1 hv2

public theorem thm_brocard_brown_solutions :
    IsBrocardSol 4 5 ∧ IsBrocardSol 5 11 ∧ IsBrocardSol 7 71 :=
  brocard_brown_solutions

public theorem thm_brocard_exhaustive_le_12 (n m : Nat) (hn : n ≤ 12) (h : IsBrocardSol n m) :
    (n = 4 ∧ m = 5) ∨ (n = 5 ∧ m = 11) ∨ (n = 7 ∧ m = 71) :=
  brocard_exhaustive_le_12 n m hn h

end FormalAtlas.Challenge
