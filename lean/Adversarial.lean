module

-- SPDX-License-Identifier: MIT
public import FormalAtlas

/-!
# Adversarial — Explicit Refutation of Weakened / False Variants (`v0.10.0`, Playbook #12)

Tests all 8 formal domains adversarially by proving 24 deliberately false, overclaimed,
or degenerately weakened statements are PROVABLY FALSE under our definitions.
-/

namespace FormalAtlas.Adversarial

/-- 1. Zero denominators are strictly excluded from `IsErdosStrausSol`. -/
public theorem adv_erdos_straus_zero_denom_blocked (n y z : Nat) :
    ¬ IsErdosStrausSol n 0 y z := by
  unfold IsErdosStrausSol
  omega

/-- 2. A false Erdős–Straus triple (`4/5 ≠ 1/2 + 1/3 + 1/6 = 1`) is refuted. -/
public theorem adv_erdos_straus_wrong_witness_refuted :
    ¬ IsErdosStrausSol 5 2 3 6 := by
  unfold IsErdosStrausSol
  decide

/-- 3. Single-step Collatz descent fails universally on positive integers (`T(3) = 5 ≥ 3`). -/
public theorem adv_collatz_no_universal_descent_d1 :
    ¬ (∀ x : Int, 0 < x → iter T 1 x < x) := by
  intro hall
  have h3 : iter T 1 3 < 3 := hall 3 (by decide)
  have hval : iter T 1 3 = 5 := by decide
  omega

/-- 4. Without `x > 0`, the Collatz no-nontrivial-cycle statement is FALSE (`x = -5`). -/
public theorem adv_collatz_positivity_required_for_no_nontrivial_cycles :
    ¬ (∀ x : Int, x ≠ 0 → x ≠ 1 → x ≠ 2 → iter T 3 x ≠ x) := by
  intro hall
  have h5 := hall (-5) (by decide) (by decide) (by decide)
  exact h5 (by decide)

/-- 5. Converse of positivity localization fails: `c(w) ≥ 3^o - 2^d` does NOT imply supercriticality. -/
public theorem adv_collatz_positivity_converse_false :
    ¬ (∀ w : List Bool,
      (3 : Int) ^ wordOddCount w - (2 : Int) ^ w.length ≤ wordIntercept w →
      (2 : Int) ^ w.length < (3 : Int) ^ wordOddCount w) := by
  intro hall
  have h := hall [true, false] (by decide)
  have hf : ¬ ((2 : Int) ^ ([true, false] : List Bool).length <
      (3 : Int) ^ wordOddCount [true, false]) := by decide
  exact hf h

/-- 6. Strict improvement over `1 / (n + 1)` in Lonely Runner is impossible for canonical speeds. -/
public theorem adv_lonely_runner_strict_threshold_fails :
    ¬ (∀ n : Nat, 1 ≤ n → ∃ p q : Int, 0 < q ∧
      ∀ i : Nat, 1 ≤ i → i ≤ n → ¬ WithinDist ((n : Int) + 1) p q (i : Int)) := by
  intro hall
  have ⟨p, q, hq, hstrict⟩ := hall 2 (by decide)
  have ⟨i, hi1, hi2, hwi⟩ := lonely_runner_sharpness_all_n 2 (by decide) p q hq
  exact hstrict i hi1 hi2 hwi

/-- 7. Time `t = 1/9` does NOT satisfy `FarEnough 3` for speed `v = 1` (`1/9 < 1/3`). -/
public theorem adv_lonely_runner_bad_time_refuted :
    ¬ FarEnough 3 1 9 1 := by
  unfold FarEnough
  decide

/-- 8. Non-Brown factorials near squares (`6!+1`, `8!+1`, `13!+1`, `16!+1`) are refuted. -/
public theorem adv_brocard_false_candidates_refuted :
    ¬ IsBrocardSol 6 26 ∧ ¬ IsBrocardSol 8 200 ∧ ¬ IsBrocardSol 13 78911 ∧ ¬ IsBrocardSol 16 4574143 := by
  unfold IsBrocardSol
  exact ⟨by decide, by decide, by decide, by decide⟩

/-- 9. `0` and `1` and composite `9 = 3 × 3` are strictly NOT prime under `IsPrime`. -/
public theorem adv_non_primes_refuted :
    ¬ IsPrime 0 ∧ ¬ IsPrime 1 ∧ ¬ IsPrime 9 := by
  refine ⟨fun h => by have := h.1; omega, fun h => by have := h.1; omega, ?_⟩
  intro h9
  have h3 : 3 ∣ 9 := ⟨3, rfl⟩
  have hc := h9.2 3 h3
  omega

/-- 10. Converse of Mersenne exponent necessity fails (`n = 11` is prime, yet `2^11 - 1 = 2047 = 23 × 89` is composite). -/
public theorem adv_mersenne_converse_false :
    IsPrime 11 ∧ ¬ IsPrime (2 ^ 11 - 1) := by
  refine ⟨isPrimeBool_sound 11 (by decide), ?_⟩
  intro hm
  have h23 : 23 ∣ 2 ^ 11 - 1 := ⟨89, by decide⟩
  have hc := hm.2 23 h23
  omega

/-- 11. Abundant number `12` (`σ(12) = 28 ≠ 24`) and deficient `15` are NOT perfect. -/
public theorem adv_non_perfect_refuted :
    ¬ IsPerfect 12 ∧ ¬ IsPerfect 15 := by
  unfold IsPerfect
  exact ⟨by decide, by decide⟩

/-- 12. Twin-prime mod-6 theorem strictly requires `p ≥ 4` (`p = 3` has `3 % 6 = 3 ≠ 5`). -/
public theorem adv_twin_prime_mod6_needs_ge_4 :
    IsPrime 3 ∧ IsPrime 5 ∧ 3 % 6 ≠ 5 := by
  exact ⟨isPrimeBool_sound 3 (by decide), isPrimeBool_sound 5 (by decide), by decide⟩

/-- 13. Ramsey bound `R(3, 3) ≤ 5` is FALSE (refuted directly by `ramsey_R33_lower`). -/
public theorem adv_ramsey_R33_not_le_5 :
    ¬ (∀ c : Fin 5 → Fin 5 → Bool, (∀ i j, c i j = c j i) → HasMonoTriangle c) := by
  intro hall
  exact ramsey_R33_lower.2 (hall c5Color ramsey_R33_lower.1)

/-- 14. Binary Goldbach fails on odd integer `11` (requires even hypothesis). -/
public theorem adv_goldbach_requires_even :
    ¬ (∀ n : Nat, 4 ≤ n → ∃ p q : Nat, IsPrime p ∧ IsPrime q ∧ p + q = n) := by
  intro hall
  exact goldbach_binary_fails_at_11 (hall 11 (by decide))

/-- 15. Ramsey bound `R(3, 4) ≤ 8` is FALSE (refuted directly by `ramsey_R34_lower`). -/
public theorem adv_ramsey_R34_not_le_8 :
    ¬ (∀ c : Fin 8 → Fin 8 → Bool, (∀ i j, c i j = c j i) →
      HasColorTriangle c true ∨ HasColorK4 c false) := by
  intro hall
  rcases hall c8Color ramsey_R34_lower.1 with h3 | h4
  · exact ramsey_R34_lower.2.1 h3
  · exact ramsey_R34_lower.2.2 h4

/-- 16. No positive integer is a length-1 Collatz fixed point (`∃ x > 0, T(x) = x` is FALSE). -/
public theorem adv_collatz_no_d1_positive_fixed_point :
    ¬ (∃ x : Int, 0 < x ∧ iter T 1 x = x) := by
  intro ⟨x, hx, hfix⟩
  exact collatz_no_positive_cycle_d1 x hx hfix

/-- 17. No nontrivial positive integer `x ≥ 3` can lie on ANY 1-odd-step or 2-odd-step Collatz cycle. -/
public theorem adv_collatz_no_nontrivial_low_odd_cycle :
    ¬ (∃ d : Nat, ∃ x : Int, 1 ≤ d ∧ 3 ≤ x ∧ iter T d x = x ∧
        (oddCount T d x = 1 ∨ oddCount T d x = 2)) := by
  intro ⟨d, x, hd, hx, hcyc, hcases⟩
  rcases hcases with h1 | h2
  · have ⟨_, hx12⟩ := collatz_positive_cycle_one_odd d x hd (by omega) hcyc h1
    omega
  · have ⟨_, hx12⟩ := collatz_positive_cycle_two_odd d x hd (by omega) hcyc h2
    omega

/-- 18. Even integers of Euclid shape with composite `2^p - 1` (`p = 4`: `8 * 15 = 120`) are NOT perfect. -/
public theorem adv_even_non_mersenne_not_perfect :
    ¬ IsPerfect (2 ^ (4 - 1) * (2 ^ 4 - 1)) := by
  intro hperf
  have ⟨p, hp2, hmp, heq⟩ := euler_even_perfect_converse 120 (by decide) hperf
  have h120 : 2 ^ (p - 1) * (2 ^ p - 1) = 120 := heq.symm
  have hmono : ∀ a b : Nat, a ≤ b → 2 ^ a ≤ 2 ^ b := by
    intro a b
    induction b with
    | zero =>
      intro h
      have ha0 : a = 0 := by omega
      subst ha0
      exact Nat.le_refl 1
    | succ k ih =>
      intro h
      by_cases he : a = k + 1
      · subst he; exact Nat.le_refl _
      · have := ih (by omega); rw [Nat.pow_succ]; omega
  -- p ≥ 5 forces 2^(p-1) * (2^p - 1) ≥ 16 * 31 = 496 > 120
  have hple4 : p ≤ 4 := by
    by_cases hge5 : 5 ≤ p
    · have h1 : 2 ^ 4 ≤ 2 ^ (p - 1) := hmono 4 (p - 1) (by omega)
      have h2 : 2 ^ 5 ≤ 2 ^ p := hmono 5 p hge5
      have hprod : 16 * 31 ≤ 2 ^ (p - 1) * (2 ^ p - 1) := Nat.mul_le_mul (by omega) (by omega)
      omega
    · omega
  by_cases hp2' : p = 2
  · rw [hp2'] at h120; simp at h120
  · by_cases hp3' : p = 3
    · rw [hp3'] at h120; simp at h120
    · have hp4' : p = 4 := by omega
      rw [hp4'] at hmp
      have h3 : 3 ∣ 2 ^ 4 - 1 := ⟨5, by decide⟩
      have hc := hmp.2 3 h3
      omega

/-- 19. No positive integer lies on ANY odd-period Collatz cycle through `d ≤ 7` (`d ∈ {1, 3, 5, 7}`). -/
public theorem adv_collatz_no_odd_period_le_7 :
    ¬ (∃ d : Nat, ∃ x : Int, 1 ≤ d ∧ d ≤ 7 ∧ d % 2 = 1 ∧ 0 < x ∧ iter T d x = x) := by
  intro ⟨d, x, hd1, hd7, hodd, hx, hcyc⟩
  exact collatz_no_positive_cycle_odd_le_7 d x hd1 hd7 hodd hx hcyc

/-- 20. Distinct periodic Collatz spines CANNOT match to 2-adic precision `|w| + |v| - gcd(|w|, |v|)`. -/
public theorem adv_collatz_distinct_spines_bounded_v2 :
    ¬ (∃ w v : List Bool, 1 ≤ w.length ∧ 1 ≤ v.length ∧
        wordIntercept w * spineDenom v ≠ wordIntercept v * spineDenom w ∧
        (wordIntercept w * spineDenom v - wordIntercept v * spineDenom w) %
          ((2 : Int) ^ (w.length + v.length - Nat.gcd w.length v.length)) = 0) := by
  intro ⟨w, v, hw, hv, hne, hdiv⟩
  exact collatz_fine_wilf_spine_ceiling w v hw hv hne hdiv

/-- 21. No nontrivial positive integer `x ≥ 3` can lie on ANY 3-odd-step Collatz cycle (all `d ≥ 1`). -/
public theorem adv_collatz_no_nontrivial_three_odd_cycle :
    ¬ (∃ d : Nat, ∃ x : Int, 1 ≤ d ∧ 3 ≤ x ∧ iter T d x = x ∧ oddCount T d x = 3) := by
  intro ⟨d, x, hd, hx, hcyc, ho⟩
  have ⟨_, hx12⟩ := collatz_positive_cycle_three_odd d x hd (by omega) hcyc ho
  omega

/-- 22. The universal affine intercept ceiling `2^(d - o) * (3^o - 2^o)` CANNOT be tightened to `<`
    even for nonempty words (`w = [F, F, T, T]` achieves exact equality `20 = 20`). -/
public theorem adv_collatz_intercept_bound_strict_false :
    ¬ (∀ w : List Bool, 1 ≤ w.length →
        wordIntercept w < (2 : Int) ^ (w.length - wordOddCount w) *
          ((3 : Int) ^ (wordOddCount w) - (2 : Int) ^ (wordOddCount w))) := by
  intro hall
  have h := hall [false, false, true, true] (by decide)
  have hne : ¬ (wordIntercept [false, false, true, true] <
      (2 : Int) ^ (([false, false, true, true] : List Bool).length -
        wordOddCount [false, false, true, true]) *
      ((3 : Int) ^ wordOddCount [false, false, true, true] -
        (2 : Int) ^ wordOddCount [false, false, true, true])) := by decide
  exact hne h

/-- 23. No nonzero multiple of 3 can EVER lie on ANY positive or negative Collatz cycle (`d ≥ 1`). -/
public theorem adv_collatz_no_mult3_nonzero_cycle :
    ¬ (∃ d : Nat, ∃ x : Int, 1 ≤ d ∧ x ≠ 0 ∧ x % 3 = 0 ∧ iter T d x = x) := by
  intro ⟨d, x, hd, hx, hdiv3, hcyc⟩
  exact collatz_cycle_no_div3 d x hd hx hcyc hdiv3

/-- 24. No nontrivial positive integer `x ≥ 3` can lie on ANY 4-odd-step Collatz cycle (all `d ≥ 1`). -/
public theorem adv_collatz_no_nontrivial_four_odd_cycle :
    ¬ (∃ d : Nat, ∃ x : Int, 1 ≤ d ∧ 3 ≤ x ∧ iter T d x = x ∧ oddCount T d x = 4) := by
  intro ⟨d, x, hd, hx, hcyc, ho⟩
  have ⟨_, hx12⟩ := collatz_positive_cycle_four_odd d x hd (by omega) hcyc ho
  omega

end FormalAtlas.Adversarial
