module

public import FormalAtlas

/-!
# Adversarial — Explicit Refutation of Weakened / False Variants (Playbook v1.3 #12)

Tests the formal definitions in `FormalAtlas.Defs` adversarially by proving that
deliberately false, overclaimed, or degenerately weakened statements are PROVABLY
FALSE under our definitions (guarding against vacuous hypotheses, degenerate
denominators, and accidental trivialization).
-/

namespace FormalAtlas.Adversarial

/-- Zero denominators are strictly excluded from `IsErdosStrausSol`. -/
public theorem adv_erdos_straus_zero_denom_blocked (n y z : Nat) :
    ¬ IsErdosStrausSol n 0 y z := by
  unfold IsErdosStrausSol
  omega

/-- A false Erdős–Straus triple (`4/5 ≠ 1/2 + 1/3 + 1/6 = 1`) is refuted. -/
public theorem adv_erdos_straus_wrong_witness_refuted :
    ¬ IsErdosStrausSol 5 2 3 6 := by
  unfold IsErdosStrausSol
  decide

/-- Single-step Collatz descent fails universally on positive integers (`T(3) = 5 ≥ 3`). -/
public theorem adv_collatz_no_universal_descent_d1 :
    ¬ (∀ x : Int, 0 < x → iter T 1 x < x) := by
  intro hall
  have h3 : iter T 1 3 < 3 := hall 3 (by decide)
  have hval : iter T 1 3 = 5 := by decide
  omega

/-- Without `x > 0`, the Collatz no-nontrivial-cycle statement is FALSE (`x = -5`). -/
public theorem adv_collatz_positivity_required_for_no_nontrivial_cycles :
    ¬ (∀ x : Int, x ≠ 0 → x ≠ 1 → x ≠ 2 → iter T 3 x ≠ x) := by
  intro hall
  have h5 := hall (-5) (by decide) (by decide) (by decide)
  exact h5 (by decide)

/-- Converse of positivity localization fails: `c(w) ≥ 3^o - 2^d` does NOT imply supercriticality. -/
public theorem adv_collatz_positivity_converse_false :
    ¬ (∀ w : List Bool,
      (3 : Int) ^ wordOddCount w - (2 : Int) ^ w.length ≤ wordIntercept w →
      (2 : Int) ^ w.length < (3 : Int) ^ wordOddCount w) := by
  intro hall
  have h := hall [true, false] (by decide)
  have hf : ¬ ((2 : Int) ^ ([true, false] : List Bool).length <
      (3 : Int) ^ wordOddCount [true, false]) := by decide
  exact hf h

/-- Strict improvement over `1 / (n + 1)` in Lonely Runner is impossible for canonical speeds. -/
public theorem adv_lonely_runner_strict_threshold_fails :
    ¬ (∀ n : Nat, 1 ≤ n → ∃ p q : Int, 0 < q ∧
      ∀ i : Nat, 1 ≤ i → i ≤ n → ¬ WithinDist ((n : Int) + 1) p q (i : Int)) := by
  intro hall
  have ⟨p, q, hq, hstrict⟩ := hall 2 (by decide)
  have ⟨i, hi1, hi2, hwi⟩ := lonely_runner_sharpness_all_n 2 (by decide) p q hq
  exact hstrict i hi1 hi2 hwi

/-- Time `t = 1/9` does NOT satisfy `FarEnough 3` for speed `v = 1` (`1/9 < 1/3`). -/
public theorem adv_lonely_runner_bad_time_refuted :
    ¬ FarEnough 3 1 9 1 := by
  unfold FarEnough
  decide

/-- Non-Brown factorials near squares (`6!+1`, `8!+1`, `13!+1`) are refuted as Brocard solutions. -/
public theorem adv_brocard_false_candidates_refuted :
    ¬ IsBrocardSol 6 26 ∧ ¬ IsBrocardSol 8 200 ∧ ¬ IsBrocardSol 13 78911 := by
  unfold IsBrocardSol
  exact ⟨by decide, by decide, by decide⟩

end FormalAtlas.Adversarial
