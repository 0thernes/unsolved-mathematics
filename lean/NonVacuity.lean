module

public import FormalAtlas

/-!
# NonVacuity — Concrete Witnesses Defeating Vacuous-Hypothesis Objections

Per the Defensible Independent AI Research Playbook (§1 & Gold Checklist #6, #9),
every hypothesis bundle in `Challenge.lean` is paired with an explicit concrete
non-vacuity witness plus negative sanity checks.
-/

namespace FormalAtlas.NonVacuity

/-- Witness for `collatz_descent_certificate_sound`: `d = 2, r = 1, q = 1`
    satisfies `3^1 < 2^2` and `T^2(1) - 1 = 0 < (4 - 3) * 1`, certifying `T^2(5) = 4 < 5`. -/
public theorem witness_descent_certificate :
    (3 : Int) ^ (oddCount T 2 1) < (2 : Int) ^ 2 ∧
    iter T 2 1 - 1 < ((2 : Int) ^ 2 - (3 : Int) ^ (oddCount T 2 1)) * 1 ∧
    iter T 2 ((2 : Int) ^ 2 * 1 + 1) = 4 := by
  exact ⟨by decide, by decide, by decide⟩

/-- Witness for `collatz_positivity_localization`: the length-3 word `[true, true, false]`
    is supercritical (`2^3 = 8 < 9 = 3^2`) with exact intercept `c = 5 ≥ 1 = 9 - 8`,
    matching the negative integer cycle `ρ = -5`. -/
public theorem witness_positivity_localization :
    let w := [true, true, false]
    (2 : Int) ^ w.length < (3 : Int) ^ wordOddCount w ∧
    wordIntercept w = 5 ∧
    (3 : Int) ^ wordOddCount w - (2 : Int) ^ w.length = 1 := by
  exact ⟨by decide, by decide, by decide⟩

/-- Negative sanity check for `collatz_positivity_localization`: a subcritical word
    (`1 → 2 → 1`, word `[true, false]`) has `3^1 = 3 < 4 = 2^2` and positive fixed point `+1`. -/
public theorem witness_subcritical_positive_cycle :
    let w := [true, false]
    (3 : Int) ^ wordOddCount w < (2 : Int) ^ w.length ∧
    wordIntercept w = 1 ∧
    iter T 2 1 = 1 := by
  exact ⟨by decide, by decide, by decide⟩

/-- Witness for `erdos_straus_mordell_840`: concrete non-exceptional input `n = 97`
    satisfies all six mod-840 hypotheses, while the exceptional square `n = 121`
    still admits the concrete decomposition `4 / 121 = 1 / 44 + 1 / 121 + 1 / 484`
    (`(11 + 4 + 1) / 484 = 16 / 484 = 4 / 121`). -/
public theorem witness_erdos_straus_hypotheses :
    (2 ≤ 97 ∧ 97 % 840 ≠ 1 ∧ 97 % 840 ≠ 121 ∧ 97 % 840 ≠ 169 ∧
      97 % 840 ≠ 289 ∧ 97 % 840 ≠ 361 ∧ 97 % 840 ≠ 529) ∧
    IsErdosStrausSol 121 44 121 484 := by
  exact ⟨by decide, by unfold IsErdosStrausSol; decide⟩

/-- Witness for `lonely_runner_sharpness_all_n` & `lonely_runner_n2`:
    at `n = 2`, speeds `(1, 2)` meet the sharpness bound `1/3` at `t = 1/3`,
    and non-trivial speeds `(3, 10)` satisfy `FarEnough 3` at `t = 1/6`
    (`‖3/6‖ = 1/2 ≥ 1/3` and `‖10/6‖ = 1/3 ≥ 1/3`). -/
public theorem witness_lonely_runner_concrete :
    FarEnough 3 1 6 3 ∧ FarEnough 3 1 6 10 ∧ WithinDist 3 1 3 1 := by
  unfold FarEnough WithinDist
  exact ⟨by decide, by decide, by decide⟩

/-- Negative sanity check for `IsBrocardSol`: `6! + 1 = 721` is NOT a square (`26² < 721 < 27²`). -/
public theorem witness_brocard_non_solution : ¬ IsBrocardSol 6 26 ∧ ¬ IsBrocardSol 6 27 := by
  unfold IsBrocardSol
  exact ⟨by decide, by decide⟩

end FormalAtlas.NonVacuity
