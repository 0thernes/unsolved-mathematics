module

-- SPDX-License-Identifier: MIT
public import FormalAtlas

/-!
# NonVacuity — Concrete Witnesses Defeating Vacuous-Hypothesis Objections (`v0.7.0`)

Per the Defensible Independent AI Research Playbook v1.3, every conditional hypothesis
bundle in `Challenge.lean` across all 8 domains is paired with an explicit concrete
non-vacuity witness (16 witnesses total).
-/

namespace FormalAtlas.NonVacuity

/-- Witness 1: Collatz descent certificate (`d=2, r=1, q=1 => T²(5) = 4 < 5`). -/
public theorem witness_descent_certificate :
    (3 : Int) ^ (oddCount T 2 1) < (2 : Int) ^ 2 ∧
    iter T 2 1 - 1 < ((2 : Int) ^ 2 - (3 : Int) ^ (oddCount T 2 1)) * 1 ∧
    iter T 2 ((2 : Int) ^ 2 * 1 + 1) = 4 := by
  exact ⟨by decide, by decide, by decide⟩

/-- Witness 2: Supercritical parity word `[T, T, F]` (`c = 5 ≥ 1`, `ρ = -5`). -/
public theorem witness_positivity_localization :
    let w := [true, true, false]
    (2 : Int) ^ w.length < (3 : Int) ^ wordOddCount w ∧
    wordIntercept w = 5 ∧
    (3 : Int) ^ wordOddCount w - (2 : Int) ^ w.length = 1 := by
  exact ⟨by decide, by decide, by decide⟩

/-- Witness 3: Subcritical positive fixed point `1 → 2 → 1` (`[T, F]`). -/
public theorem witness_subcritical_positive_cycle :
    let w := [true, false]
    (3 : Int) ^ wordOddCount w < (2 : Int) ^ w.length ∧
    wordIntercept w = 1 ∧
    iter T 2 1 = 1 := by
  exact ⟨by decide, by decide, by decide⟩

/-- Witness 4: Erdős–Straus non-exceptional `97` and exceptional square `121`. -/
public theorem witness_erdos_straus_hypotheses :
    (2 ≤ 97 ∧ 97 % 840 ≠ 1 ∧ 97 % 840 ≠ 121 ∧ 97 % 840 ≠ 169 ∧
      97 % 840 ≠ 289 ∧ 97 % 840 ≠ 361 ∧ 97 % 840 ≠ 529) ∧
    IsErdosStrausSol 121 44 121 484 := by
  exact ⟨by decide, by unfold IsErdosStrausSol; decide⟩

/-- Witness 5: Lonely Runner `n=2` speeds `(3, 10)` at `t = 1/6` and sharpness at `1/3`. -/
public theorem witness_lonely_runner_concrete :
    FarEnough 3 1 6 3 ∧ FarEnough 3 1 6 10 ∧ WithinDist 3 1 3 1 := by
  unfold FarEnough WithinDist
  exact ⟨by decide, by decide, by decide⟩

/-- Witness 6: Brocard non-solution `6! + 1 = 721` (`26² < 721 < 27²`). -/
public theorem witness_brocard_non_solution : ¬ IsBrocardSol 6 26 ∧ ¬ IsBrocardSol 6 27 := by
  unfold IsBrocardSol
  exact ⟨by decide, by decide⟩

/-- Witness 7: Twin primes `(5, 7)` and `(11, 13)` satisfy `IsPrime` and `p % 6 = 5`. -/
public theorem witness_twin_primes_concrete :
    IsPrime 5 ∧ IsPrime 7 ∧ IsPrime 11 ∧ IsPrime 13 ∧ 5 % 6 = 5 ∧ 11 % 6 = 5 := by
  exact ⟨isPrimeBool_sound 5 (by decide), isPrimeBool_sound 7 (by decide),
         isPrimeBool_sound 11 (by decide), isPrimeBool_sound 13 (by decide),
         by decide, by decide⟩

/-- Witness 8: Goldbach witness `100 = 3 + 97` with both summands certified prime. -/
public theorem witness_goldbach_100 :
    IsPrime 3 ∧ IsPrime 97 ∧ 3 + 97 = 100 := by
  exact ⟨isPrimeBool_sound 3 (by decide), isPrimeBool_sound 97 (by decide), by decide⟩

/-- Witness 9: Mersenne prime `2^5 - 1 = 31` has prime exponent `5`. -/
public theorem witness_mersenne_31 :
    IsPrime (2 ^ 5 - 1) ∧ IsPrime 5 := by
  exact ⟨isPrimeBool_sound 31 (by decide), isPrimeBool_sound 5 (by decide)⟩

/-- Witness 10: Lonely Runner `n=3` non-div-4 triple `(1, 2, 3)` achieves `≥ 1/4` at `t = 1/4`. -/
public theorem witness_lonely_runner_n3_concrete :
    FarEnough 4 1 4 1 ∧ FarEnough 4 1 4 2 ∧ FarEnough 4 1 4 3 := by
  unfold FarEnough
  exact ⟨by decide, by decide, by decide⟩

/-- Witness 11: Lonely Runner `n=3` Subcase 3c triple `(3, 5, 60)` (`4*3 ∣ 60` and `4*5 ∣ 60`)
    achieves exact circular separation `≥ 1/4` at `t = 61 / 480`. -/
public theorem witness_lonely_runner_n3_div4 :
    FarEnough 4 61 480 3 ∧ FarEnough 4 61 480 5 ∧ FarEnough 4 61 480 60 := by
  unfold FarEnough
  exact ⟨by decide, by decide, by decide⟩

/-- Witness 12: Euclid even-perfect instantiation at `p = 3` (`2^3 - 1 = 7` prime → `28` perfect). -/
public theorem witness_euclid_perfect_28 :
    IsPrime (2 ^ 3 - 1) ∧ IsPerfect (2 ^ (3 - 1) * (2 ^ 3 - 1)) := by
  exact ⟨isPrimeBool_sound 7 (by decide), euclid_even_perfect 3 (by decide) (isPrimeBool_sound 7 (by decide))⟩

/-- Witness 13: Euler Mersenne divisor instantiation at `p = 11`, `q = 23` (`23 ∣ 2^11 - 1`, `22 ∣ 23 - 1`). -/
public theorem witness_mersenne_divisor_23_of_M11 :
    IsPrime 11 ∧ IsPrime 23 ∧ 23 ∣ 2 ^ 11 - 1 ∧ 2 * 11 ∣ 23 - 1 := by
  exact ⟨isPrimeBool_sound 11 (by decide), isPrimeBool_sound 23 (by decide),
         ⟨89, by decide⟩, ⟨1, by decide⟩⟩

/-- Witness 14: Trivial 2-odd-step Collatz cycle `1 → 2 → 1 → 2 → 1` (`d = 4`, `o = 2`). -/
public theorem witness_collatz_two_odd_trivial_cycle :
    iter T 4 1 = 1 ∧ oddCount T 4 1 = 2 ∧ iter T 4 2 = 2 ∧ oddCount T 4 2 = 2 := by
  exact ⟨by decide, by decide, by decide, by decide⟩

/-- Witness 15: Odd-unit-lock Fine–Wilf sharpness on `w = [T, F]` vs `v = [T, F, T]`:
    distinct rational spines (`1` vs `-5`) agree on 3 bits (`2^3 | sep`), fail at `2^4` (`|w|+|v|-gcd = 4`). -/
public theorem witness_odd_unit_lock_fine_wilf :
    let w := [true, false]
    let v := [true, false, true]
    wordIntercept w * spineDenom v ≠ wordIntercept v * spineDenom w ∧
    (wordIntercept w * spineDenom v - wordIntercept v * spineDenom w) % ((2 : Int) ^ 3) = 0 ∧
    (wordIntercept w * spineDenom v - wordIntercept v * spineDenom w) % ((2 : Int) ^ 4) ≠ 0 := by
  exact ⟨by decide, by decide, by decide⟩

/-- Witness 16: Catalytic zero-workspace reversible cylinder evaluation at `d=2, q=1, r=1, acc=10, cat=999`. -/
public theorem witness_catalytic_cylinder :
    catCollatzStep 2 1 1 10 999 = (14, 999) := by
  decide

end FormalAtlas.NonVacuity
