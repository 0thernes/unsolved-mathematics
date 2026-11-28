module

public import FormalAtlas.Defs

/-!
# FormalAtlas.Collatz — Machine-Checked Structural Core & Obstructions

Proves the foundational structural theorems, finite cycle exclusions, and `3n-1`
sibling-map comparison of the Collatz research program in pure Lean 4 (zero Mathlib,
zero `sorry` in proof modules, standard axioms only):
  1. `collatz_cylinder_affine_law` — `T^d(2^d q + r) = 3^o q + T^d(r)`
  2. `collatz_exact_intercept_law` — `2^d T^d(x) = 3^o x + c(w)`
  3. `terras_parity_word_bijection` — Terras (1976) injectivity & surjectivity mod `2^d`
  4. `collatz_descent_certificate_sound` — exact descent certificate criterion
  5. `collatz_no_finite_subcritical_cover` — all-ones fixed point `-1` obstruction
  6. `collatz_spine_ladder_identity` — cleared-denominator Spine Ladder linearization
  7. `collatz_positivity_localization` — every supercritical periodic spine satisfies `ρ_w ≤ -1`
     (exact integer form: `wordIntercept w ≥ 3^(wordOddCount w) - 2^(w.length)`)
  8. `collatz_epsilon_invariance_barrier` — `3n-1` sibling comparison: `TMinus` has the
     identical Terras bijection yet possesses positive supercritical cycles at `5` and `17`
     (note: the methodological "no-go barrier" reading is a heuristic, not a formalized
     meta-theorem; declaration name retained for backward compatibility).

Explicit non-claim: proves NO part of the Collatz Conjecture (status: OPEN).
-/

namespace FormalAtlas

theorem T_step_twice (x : Int) :
    2 * T x = if parityBit x then 3 * x + 1 else x := by
  unfold T parityBit
  by_cases h : x % 2 = 0
  · simp [h]; omega
  · have hb1 : (x % 2 == 0) = false := by
      cases hbeq : (x % 2 == 0)
      · rfl
      · exfalso; exact h (beq_iff_eq.mp hbeq)
    have hb2 : (x % 2 != 0) = true := by simp [bne, hb1]
    simp [hb1, hb2]; omega

theorem T_shift_one (k r : Int) :
    parityBit (2 * k + r) = parityBit r ∧
    T (2 * k + r) = (if parityBit r then 3 * k else k) + T r := by
  unfold parityBit T
  have hmod : (2 * k + r) % 2 = r % 2 := by omega
  by_cases h : r % 2 = 0
  · have h1 : (2 * k + r) % 2 = 0 := by omega
    simp [h, h1]; omega
  · have hb : (r % 2 == 0) = false := by
      cases hbeq : (r % 2 == 0)
      · rfl
      · exfalso; exact h (beq_iff_eq.mp hbeq)
    have hne : (r % 2 != 0) = true := by simp [bne, hb]
    simp [hmod, hb, hne]
    omega

theorem TMinus_shift_one (k r : Int) :
    parityBit (2 * k + r) = parityBit r ∧
    TMinus (2 * k + r) = (if parityBit r then 3 * k else k) + TMinus r := by
  unfold parityBit TMinus
  have hmod : (2 * k + r) % 2 = r % 2 := by omega
  by_cases h : r % 2 = 0
  · have h1 : (2 * k + r) % 2 = 0 := by omega
    simp [h, h1]; omega
  · have hb : (r % 2 == 0) = false := by
      cases hbeq : (r % 2 == 0)
      · rfl
      · exfalso; exact h (beq_iff_eq.mp hbeq)
    have hne : (r % 2 != 0) = true := by simp [bne, hb]
    simp [hmod, hb, hne]
    omega

theorem parityBit_eq_iff_mod (x y : Int) :
    parityBit x = parityBit y ↔ (x - y) % 2 = 0 := by
  unfold parityBit
  by_cases hx : x % 2 = 0 <;> by_cases hy : y % 2 = 0
  · simp [hx, hy]; omega
  · have hby : (y % 2 == 0) = false := by
      cases h : (y % 2 == 0)
      · rfl
      · exfalso; exact hy (beq_iff_eq.mp h)
    have hny : (y % 2 != 0) = true := by simp [bne, hby]
    simp [hx, hny]; omega
  · have hbx : (x % 2 == 0) = false := by
      cases h : (x % 2 == 0)
      · rfl
      · exfalso; exact hx (beq_iff_eq.mp h)
    have hnx : (x % 2 != 0) = true := by simp [bne, hbx]
    simp [hy, hnx]; omega
  · have hbx : (x % 2 == 0) = false := by
      cases h : (x % 2 == 0)
      · rfl
      · exfalso; exact hx (beq_iff_eq.mp h)
    have hby : (y % 2 == 0) = false := by
      cases h : (y % 2 == 0)
      · rfl
      · exfalso; exact hy (beq_iff_eq.mp h)
    have hnx : (x % 2 != 0) = true := by simp [bne, hbx]
    have hny : (y % 2 != 0) = true := by simp [bne, hby]
    simp [hnx, hny]; omega

theorem pow2_succ_mul (d : Nat) (q : Int) :
    (2 : Int) ^ (d + 1) * q = 2 * ((2 : Int) ^ d * q) := by
  rw [Int.pow_succ, Int.mul_comm ((2 : Int) ^ d) 2, Int.mul_assoc]

theorem pow2_pos (d : Nat) : (0 : Int) < (2 : Int) ^ d := by
  induction d with
  | zero => simp
  | succ d ih => rw [Int.pow_succ]; omega

theorem eq_zero_of_dvd_and_lt {d : Nat} {x y : Int}
    (hx0 : 0 ≤ x) (hxlt : x < (2 : Int) ^ d) (hy0 : 0 ≤ y) (hylt : y < (2 : Int) ^ d)
    (hdiv : (x - y) % ((2 : Int) ^ d) = 0) : x = y := by
  have ⟨q, hq⟩ := Int.dvd_of_emod_eq_zero hdiv
  have hpos := pow2_pos d
  by_cases hqp : 1 ≤ q
  · have h1 := Int.mul_le_mul_of_nonneg_left hqp (by omega : (0 : Int) ≤ (2 : Int) ^ d)
    rw [Int.mul_one] at h1
    omega
  · by_cases hqn : q ≤ -1
    · have h2 := Int.mul_le_mul_of_nonneg_left hqn (by omega : (0 : Int) ≤ (2 : Int) ^ d)
      have hm1 : (2 : Int) ^ d * (-1) = -((2 : Int) ^ d) := by omega
      rw [hm1] at h2
      omega
    · have hq0 : q = 0 := by omega
      rw [hq0, Int.mul_zero] at hq
      omega

-- ----------------------------------------------------------------------------
-- Theorem 1: Cylinder Affine Law (Theorem 3.1)
-- ----------------------------------------------------------------------------

public theorem collatz_cylinder_affine_and_word (d : Nat) (q r : Int) :
    parityWord T d ((2 : Int) ^ d * q + r) = parityWord T d r ∧
    iter T d ((2 : Int) ^ d * q + r) =
      (3 : Int) ^ (oddCount T d r) * q + iter T d r := by
  induction d generalizing q r with
  | zero =>
    simp [parityWord, iter, oddCount, wordOddCount]
  | succ d ih =>
    rw [pow2_succ_mul]
    have ⟨hbit, hT⟩ := T_shift_one ((2 : Int) ^ d * q) r
    simp only [parityWord, iter, oddCount, wordOddCount]
    rw [hbit, hT]
    by_cases hb : parityBit r = true
    · simp only [hb, ite_true]
      have harg : 3 * ((2 : Int) ^ d * q) + T r = (2 : Int) ^ d * (3 * q) + T r := by
        rw [Int.mul_left_comm]
      rw [harg]
      have ⟨hw, hi⟩ := ih (3 * q) (T r)
      refine ⟨congrArg (true :: ·) hw, ?_⟩
      rw [hi]
      unfold oddCount at hi ⊢
      have h3 : (3 : Int) ^ (1 + wordOddCount (parityWord T d (T r))) * q =
                (3 : Int) ^ (wordOddCount (parityWord T d (T r))) * (3 * q) := by
        rw [Nat.add_comm, Int.pow_succ, Int.mul_assoc]
      rw [h3]
    · simp only [hb, Bool.false_eq_true, ite_false]
      have ⟨hw, hi⟩ := ih q (T r)
      refine ⟨congrArg (false :: ·) hw, ?_⟩
      rw [hi]
      simp [oddCount]

/-- **Theorem 1 (Cylinder Affine Law).** -/
public theorem collatz_cylinder_affine_law (d : Nat) (q r : Int) :
    iter T d ((2 : Int) ^ d * q + r) =
      (3 : Int) ^ (oddCount T d r) * q + iter T d r :=
  (collatz_cylinder_affine_and_word d q r).2

-- ----------------------------------------------------------------------------
-- Theorem 2: Exact Intercept Law: 2^d * T^d(x) = 3^o * x + c(w)
-- ----------------------------------------------------------------------------

/-- **Theorem 2 (Exact Affine Intercept Law).** -/
public theorem collatz_exact_intercept_law (d : Nat) (x : Int) :
    (2 : Int) ^ d * iter T d x =
      (3 : Int) ^ (oddCount T d x) * x + wordIntercept (parityWord T d x) := by
  induction d generalizing x with
  | zero =>
    simp [iter, oddCount, parityWord, wordOddCount, wordIntercept]
  | succ d ih =>
    simp only [iter, oddCount, parityWord, wordOddCount]
    have hstep := T_step_twice x
    have hrec := ih (T x)
    unfold oddCount at hrec
    cases hb : parityBit x
    · simp only [hb, Bool.false_eq_true, ite_false, wordIntercept, Nat.zero_add] at hstep ⊢
      calc
        (2 : Int) ^ (d + 1) * iter T d (T x)
            = 2 * ((2 : Int) ^ d * iter T d (T x)) := pow2_succ_mul d _
        _   = 2 * ((3 : Int) ^ wordOddCount (parityWord T d (T x)) * T x +
                   wordIntercept (parityWord T d (T x))) := by rw [hrec]
        _   = (3 : Int) ^ wordOddCount (parityWord T d (T x)) * (2 * T x) +
              2 * wordIntercept (parityWord T d (T x)) := by
              rw [Int.mul_add, ← Int.mul_assoc, Int.mul_comm 2 ((3 : Int) ^ _), Int.mul_assoc]
        _   = (3 : Int) ^ wordOddCount (parityWord T d (T x)) * x +
              2 * wordIntercept (parityWord T d (T x)) := by rw [hstep]
    · simp only [hb, ite_true, wordIntercept] at hstep ⊢
      calc
        (2 : Int) ^ (d + 1) * iter T d (T x)
            = 2 * ((2 : Int) ^ d * iter T d (T x)) := pow2_succ_mul d _
        _   = 2 * ((3 : Int) ^ wordOddCount (parityWord T d (T x)) * T x +
                   wordIntercept (parityWord T d (T x))) := by rw [hrec]
        _   = (3 : Int) ^ wordOddCount (parityWord T d (T x)) * (2 * T x) +
              2 * wordIntercept (parityWord T d (T x)) := by
              rw [Int.mul_add, ← Int.mul_assoc, Int.mul_comm 2 ((3 : Int) ^ _), Int.mul_assoc]
        _   = (3 : Int) ^ wordOddCount (parityWord T d (T x)) * (3 * x + 1) +
              2 * wordIntercept (parityWord T d (T x)) := by rw [hstep]
        _   = (3 : Int) ^ (1 + wordOddCount (parityWord T d (T x))) * x +
              ((3 : Int) ^ wordOddCount (parityWord T d (T x)) +
               2 * wordIntercept (parityWord T d (T x))) := by
              rw [Int.mul_add, Int.mul_one, Nat.add_comm 1 _, Int.pow_succ, Int.mul_assoc,
                  Int.add_assoc]

-- ----------------------------------------------------------------------------
-- Theorem 3: Terras Parity-Word Bijection (1976) — for BOTH T and TMinus!
-- ----------------------------------------------------------------------------

theorem dvd_pow2_of_three_mul (m : Nat) :
    ∀ z : Int, (3 * z) % ((2 : Int) ^ m) = 0 → z % ((2 : Int) ^ m) = 0 := by
  induction m with
  | zero => intro z _; simp
  | succ m ihm =>
    intro z hz
    have hdiv : (2 : Int) ^ (m + 1) = 2 * (2 : Int) ^ m := by rw [Int.pow_succ, Int.mul_comm]
    have ⟨q, hq⟩ := Int.dvd_of_emod_eq_zero hz
    rw [hdiv] at hq
    have hz2 : (3 * z) % 2 = 0 := Int.emod_eq_zero_of_dvd ⟨(2 : Int) ^ m * q, by
      rw [hq, Int.mul_assoc]⟩
    have hz_even : z % 2 = 0 := by omega
    let z' := z / 2
    have hz_eq : z = 2 * z' := by omega
    have hq' : 3 * z' = (2 : Int) ^ m * q := by
      have h2eq : 2 * (3 * z') = 2 * ((2 : Int) ^ m * q) := by
        calc 2 * (3 * z') = 3 * (2 * z') := by omega
        _ = 3 * z := by rw [← hz_eq]
        _ = 2 * (2 : Int) ^ m * q := hq
        _ = 2 * ((2 : Int) ^ m * q) := Int.mul_assoc _ _ _
      omega
    have hz' : (3 * z') % ((2 : Int) ^ m) = 0 := Int.emod_eq_zero_of_dvd ⟨q, hq'⟩
    have ⟨q2, hq2⟩ := Int.dvd_of_emod_eq_zero (ihm z' hz')
    rw [hz_eq, hdiv]
    exact Int.emod_eq_zero_of_dvd ⟨q2, by rw [hq2, Int.mul_assoc]⟩

theorem terras_inj_general (f : Int → Int)
    (hshift : ∀ k r : Int, parityBit (2 * k + r) = parityBit r ∧
      f (2 * k + r) = (if parityBit r then 3 * k else k) + f r)
    (d : Nat) :
    ∀ x y : Int, parityWord f d x = parityWord f d y → (x - y) % ((2 : Int) ^ d) = 0 := by
  induction d with
  | zero => intro x y _; simp
  | succ d ih =>
    intro x y hword
    simp only [parityWord, List.cons.injEq] at hword
    have ⟨hbit, htail⟩ := hword
    have hmod2 : (x - y) % 2 = 0 := (parityBit_eq_iff_mod x y).mp hbit
    let k : Int := (x - y) / 2
    have hxy : x = 2 * k + y := by omega
    have hstep := (hshift k y).2
    rw [hxy, hstep] at htail
    have hrec := ih ((if parityBit y then 3 * k else k) + f y) (f y) htail
    have hsub : ((if parityBit y then 3 * k else k) + f y) - f y =
                (if parityBit y then 3 * k else k) := by omega
    rw [hsub] at hrec
    have hk_div : k % ((2 : Int) ^ d) = 0 := by
      by_cases hb : parityBit y = true
      · simp only [hb, ite_true] at hrec
        exact dvd_pow2_of_three_mul d k hrec
      · simp only [hb, Bool.false_eq_true, ite_false] at hrec
        exact hrec
    have ⟨q, hq⟩ := Int.dvd_of_emod_eq_zero hk_div
    have hpow : (2 : Int) ^ (d + 1) = 2 * (2 : Int) ^ d := by rw [Int.pow_succ, Int.mul_comm]
    rw [hpow]
    exact Int.emod_eq_zero_of_dvd ⟨q, by
      have : x - y = 2 * k := by omega
      rw [this, hq, Int.mul_assoc]⟩

theorem inv3_mod_pow2 (m : Nat) :
    ∃ u : Int, (3 * u) % ((2 : Int) ^ m) = 1 % ((2 : Int) ^ m) := by
  induction m with
  | zero => exact ⟨0, by simp⟩
  | succ m ihm =>
    have ⟨u, hu⟩ := ihm
    by_cases hgood : (3 * u - 1) % ((2 : Int) ^ (m + 1)) = 0
    · refine ⟨u, ?_⟩
      have ⟨q, hq⟩ := Int.dvd_of_emod_eq_zero hgood
      have h1 : 3 * u = (2 : Int) ^ (m + 1) * q + 1 := by omega
      rw [h1, Int.mul_comm ((2 : Int) ^ (m + 1)) q, Int.mul_add_emod_self_right]
    · refine ⟨u + (2 : Int) ^ m, ?_⟩
      have hmodm : (3 * u - 1) % ((2 : Int) ^ m) = 0 := by
        have hsub : (3 * u - 1) % ((2 : Int) ^ m) =
            ((3 * u) % ((2 : Int) ^ m) - 1 % ((2 : Int) ^ m)) % ((2 : Int) ^ m) := by
          rw [Int.sub_emod]
        rw [hsub, hu]; simp
      have ⟨q, hq⟩ := Int.dvd_of_emod_eq_zero hmodm
      have hpow : (2 : Int) ^ (m + 1) = 2 * (2 : Int) ^ m := by rw [Int.pow_succ, Int.mul_comm]
      have hq_odd : q % 2 ≠ 0 := by
        intro hqe
        apply hgood
        rw [hpow]
        refine Int.emod_eq_zero_of_dvd ⟨q / 2, ?_⟩
        have hq2 : q = 2 * (q / 2) := by omega
        calc
          3 * u - 1 = (2 : Int) ^ m * q := hq
          _ = (2 : Int) ^ m * (2 * (q / 2)) := by rw [← hq2]
          _ = 2 * (2 : Int) ^ m * (q / 2) := by
            rw [← Int.mul_assoc, Int.mul_comm ((2 : Int) ^ m) 2]
      have hdiv : (3 * (u + (2 : Int) ^ m) - 1) % ((2 : Int) ^ (m + 1)) = 0 := by
        rw [hpow]
        refine Int.emod_eq_zero_of_dvd ⟨(q + 3) / 2, ?_⟩
        have hqeq : q + 3 = 2 * ((q + 3) / 2) := by omega
        calc
          3 * (u + (2 : Int) ^ m) - 1
              = (3 * u - 1) + 3 * (2 : Int) ^ m := by omega
          _   = (2 : Int) ^ m * q + (2 : Int) ^ m * 3 := by
                rw [hq, Int.mul_comm 3 ((2 : Int) ^ m)]
          _   = (2 : Int) ^ m * (q + 3) := by rw [← Int.mul_add]
          _   = (2 : Int) ^ m * (2 * ((q + 3) / 2)) := by rw [← hqeq]
          _   = 2 * (2 : Int) ^ m * ((q + 3) / 2) := by
                rw [← Int.mul_assoc, Int.mul_comm ((2 : Int) ^ m) 2]
      have ⟨q2, hq2⟩ := Int.dvd_of_emod_eq_zero hdiv
      have h1 : 3 * (u + (2 : Int) ^ m) = (2 : Int) ^ (m + 1) * q2 + 1 := by omega
      rw [h1, Int.mul_comm ((2 : Int) ^ (m + 1)) q2, Int.mul_add_emod_self_right]

theorem terras_surj_general (f : Int → Int)
    (hshift : ∀ k r : Int, parityBit (2 * k + r) = parityBit r ∧
      f (2 * k + r) = (if parityBit r then 3 * k else k) + f r)
    (hstep_par : ∀ b : Bool, ∃ r0 : Int, 0 ≤ r0 ∧ r0 < 2 ∧ parityBit r0 = b) :
    ∀ w : List Bool, ∃ r : Int, 0 ≤ r ∧ r < (2 : Int) ^ w.length ∧
      parityWord f w.length r = w := by
  have hword_mod : ∀ d : Nat, ∀ q x : Int,
      parityWord f d ((2 : Int) ^ d * q + x) = parityWord f d x := by
    intro d
    induction d with
    | zero => intro q x; rfl
    | succ d ihd =>
      intro q x
      rw [pow2_succ_mul]
      have ⟨hb, hf⟩ := hshift ((2 : Int) ^ d * q) x
      simp only [parityWord, hb, hf]
      by_cases hbx : parityBit x = true
      · simp only [hbx, ite_true]
        have harg : 3 * ((2 : Int) ^ d * q) + f x = (2 : Int) ^ d * (3 * q) + f x := by
          rw [Int.mul_left_comm]
        rw [harg, ihd]
      · simp only [hbx, Bool.false_eq_true, ite_false]
        rw [ihd]
  intro w
  induction w with
  | nil => exact ⟨0, by omega, by simp, rfl⟩
  | cons b ws ih =>
    have ⟨r', hr'0, hr'lt, hr'w⟩ := ih
    have ⟨r0, hr0_0, hr0_lt, hr0_b⟩ := hstep_par b
    have hpow_pos := pow2_pos ws.length
    have ⟨u, hu⟩ := inv3_mod_pow2 ws.length
    let k : Int := (if b then u * (r' - f r0) else (r' - f r0)) % ((2 : Int) ^ ws.length)
    have hk0 : 0 ≤ k := Int.emod_nonneg _ (by omega)
    have hklt : k < (2 : Int) ^ ws.length := Int.emod_lt_of_pos _ hpow_pos
    refine ⟨2 * k + r0, by omega, ?_, ?_⟩
    · have : (2 : Int) ^ (b :: ws).length = 2 * (2 : Int) ^ ws.length := by
        simp [List.length_cons, Int.pow_succ, Int.mul_comm]
      omega
    · simp only [List.length_cons, parityWord]
      have ⟨hbit, hf⟩ := hshift k r0
      rw [hbit, hr0_b, hf, hr0_b]
      refine congrArg (b :: ·) ?_
      have hcong : ((if b then 3 * k else k) + f r0 - r') % ((2 : Int) ^ ws.length) = 0 := by
        cases b
        · simp only [Bool.false_eq_true, ite_false]
          have hkdef : k = (r' - f r0) % ((2 : Int) ^ ws.length) := rfl
          rw [hkdef]
          have hstep : ((r' - f r0) % ((2 : Int) ^ ws.length) + f r0 - r') % ((2 : Int) ^ ws.length) =
              ((r' - f r0) % ((2 : Int) ^ ws.length) - (r' - f r0)) % ((2 : Int) ^ ws.length) := by
            congr 1; omega
          rw [hstep, Int.sub_emod, Int.emod_emod]; simp
        · simp only [ite_true]
          have hkdef : k = (u * (r' - f r0)) % ((2 : Int) ^ ws.length) := rfl
          rw [hkdef]
          have h1 : (3 * ((u * (r' - f r0)) % ((2 : Int) ^ ws.length))) % ((2 : Int) ^ ws.length) =
              (3 * (u * (r' - f r0))) % ((2 : Int) ^ ws.length) := by
            rw [Int.mul_emod, Int.emod_emod, ← Int.mul_emod]
          have h2 : (3 * (u * (r' - f r0))) % ((2 : Int) ^ ws.length) =
              (r' - f r0) % ((2 : Int) ^ ws.length) := by
            rw [← Int.mul_assoc, Int.mul_emod, hu, ← Int.mul_emod, Int.one_mul]
          have h3 : (3 * ((u * (r' - f r0)) % ((2 : Int) ^ ws.length)) + f r0 - r') % ((2 : Int) ^ ws.length) =
              ((3 * ((u * (r' - f r0)) % ((2 : Int) ^ ws.length))) % ((2 : Int) ^ ws.length) -
                (r' - f r0) % ((2 : Int) ^ ws.length)) % ((2 : Int) ^ ws.length) := by
            have : 3 * ((u * (r' - f r0)) % ((2 : Int) ^ ws.length)) + f r0 - r' =
                3 * ((u * (r' - f r0)) % ((2 : Int) ^ ws.length)) - (r' - f r0) := by omega
            rw [this, Int.sub_emod]
          rw [h3, h1, h2]; simp
      have ⟨q, hq⟩ := Int.dvd_of_emod_eq_zero hcong
      have heq : (if b then 3 * k else k) + f r0 = (2 : Int) ^ ws.length * q + r' := by omega
      rw [heq, hword_mod, hr'w]

theorem parity_exists (b : Bool) : ∃ r0 : Int, 0 ≤ r0 ∧ r0 < 2 ∧ parityBit r0 = b := by
  cases b
  · exact ⟨0, by omega, by omega, rfl⟩
  · exact ⟨1, by omega, by omega, rfl⟩

/-- **Theorem 3 (Terras Parity-Word Bijection, 1976).** -/
public theorem terras_parity_word_bijection (d : Nat) :
    (∀ x y : Int, 0 ≤ x → x < (2 : Int) ^ d → 0 ≤ y → y < (2 : Int) ^ d →
      parityWord T d x = parityWord T d y → x = y) ∧
    (∀ w : List Bool, w.length = d →
      ∃ r : Int, 0 ≤ r ∧ r < (2 : Int) ^ d ∧ parityWord T d r = w) := by
  constructor
  · intro x y hx0 hxlt hy0 hylt hw
    exact eq_zero_of_dvd_and_lt hx0 hxlt hy0 hylt (terras_inj_general T T_shift_one d x y hw)
  · intro w hlen
    subst hlen
    exact terras_surj_general T T_shift_one parity_exists w

-- ----------------------------------------------------------------------------
-- Theorem 4: Soundness of Descent Certificates (Theorem 3.3)
-- ----------------------------------------------------------------------------

/-- **Theorem 4 (Descent Certificate Soundness).** -/
public theorem collatz_descent_certificate_sound (d : Nat) (q r : Int)
    (_hsub : (3 : Int) ^ (oddCount T d r) < (2 : Int) ^ d)
    (hq : iter T d r - r < ((2 : Int) ^ d - (3 : Int) ^ (oddCount T d r)) * q) :
    iter T d ((2 : Int) ^ d * q + r) < (2 : Int) ^ d * q + r := by
  rw [collatz_cylinder_affine_law d q r]
  have hmul : ((2 : Int) ^ d - (3 : Int) ^ (oddCount T d r)) * q =
      (2 : Int) ^ d * q - (3 : Int) ^ (oddCount T d r) * q := Int.sub_mul _ _ _
  omega

-- ----------------------------------------------------------------------------
-- Theorem 5: No Finite 2-Adic Subcritical Cover Obstruction (Theorem 3.4)
-- ----------------------------------------------------------------------------

/-- **Theorem 5 (No Finite Subcritical Cover).** -/
public theorem collatz_no_finite_subcritical_cover (d : Nat) :
    iter T d (-1) = -1 ∧
    oddCount T d (-1) = d ∧
    (2 : Int) ^ d ≤ (3 : Int) ^ (oddCount T d (-1)) := by
  have hTneg1 : T (-1) = -1 := by decide
  have hbitneg1 : parityBit (-1) = true := by decide
  have hiter : ∀ n : Nat, iter T n (-1) = -1 := by
    intro n; induction n with
    | zero => rfl
    | succ n ih => rw [iter, hTneg1, ih]
  have hodd : ∀ n : Nat, oddCount T n (-1) = n := by
    intro n; induction n with
    | zero => rfl
    | succ n ih =>
      unfold oddCount at ih ⊢
      rw [parityWord, hbitneg1, hTneg1, wordOddCount]
      simp [ih]; omega
  have hpow : ∀ n : Nat, (2 : Int) ^ n ≤ (3 : Int) ^ n := by
    intro n; induction n with
    | zero => simp
    | succ n ih =>
      rw [Int.pow_succ, Int.pow_succ]
      have hpos := pow2_pos n
      omega
  refine ⟨hiter d, hodd d, ?_⟩
  rw [hodd d]
  exact hpow d

-- ----------------------------------------------------------------------------
-- Theorem 6: Exact Spine Ladder Linearization (Lemma 4.1)
-- ----------------------------------------------------------------------------

/-- **Theorem 6 (Spine Ladder Identity, cleared of denominators).** -/
public theorem collatz_spine_ladder_identity (d : Nat) (x : Int) :
    let o := oddCount T d x
    let c := wordIntercept (parityWord T d x)
    (2 : Int) ^ d * (((2 : Int) ^ d - (3 : Int) ^ o) * iter T d x - c) =
      (3 : Int) ^ o * (((2 : Int) ^ d - (3 : Int) ^ o) * x - c) := by
  intro o c
  have hlaw : (2 : Int) ^ d * iter T d x = (3 : Int) ^ o * x + c :=
    collatz_exact_intercept_law d x
  let A : Int := (2 : Int) ^ d
  let B : Int := (3 : Int) ^ o
  let Y : Int := iter T d x
  change A * ((A - B) * Y - c) = B * ((A - B) * x - c)
  have hlaw' : A * Y = B * x + c := hlaw
  have hL : A * ((A - B) * Y - c) = A * (B * x) - B * (B * x) - B * c := by
    calc A * ((A - B) * Y - c)
        = (A - B) * (A * Y) - A * c := by
          rw [Int.mul_sub, ← Int.mul_assoc, Int.mul_comm A (A - B), Int.mul_assoc]
    _   = (A - B) * (B * x + c) - A * c := by rw [hlaw']
    _   = (A * (B * x) - B * (B * x)) + (A * c - B * c) - A * c := by
          rw [Int.mul_add, Int.sub_mul, Int.sub_mul]
    _   = A * (B * x) - B * (B * x) - B * c := by omega
  have hR : B * ((A - B) * x - c) = A * (B * x) - B * (B * x) - B * c := by
    rw [Int.mul_sub, Int.sub_mul, Int.mul_sub]
    have hcomm : B * (A * x) = A * (B * x) := by
      rw [← Int.mul_assoc, Int.mul_comm B A, Int.mul_assoc]
    rw [hcomm]
  rw [hL, hR]

-- ----------------------------------------------------------------------------
-- Theorem 7: Positivity Localization (Corollary 4.2 — exact integer proof!)
-- ----------------------------------------------------------------------------

theorem wordOddCount_append (u v : List Bool) :
    wordOddCount (u ++ v) = wordOddCount u + wordOddCount v := by
  induction u with
  | nil => simp [wordOddCount]
  | cons b us ih =>
    simp only [List.cons_append, wordOddCount, ih]
    omega

theorem wordOddCount_rotate (w : List Bool) :
    wordOddCount (rotateWord w) = wordOddCount w := by
  cases w with
  | nil => rfl
  | cons b ws =>
    simp only [rotateWord, wordOddCount_append, wordOddCount]
    omega

theorem length_rotate (w : List Bool) : (rotateWord w).length = w.length := by
  cases w with
  | nil => rfl
  | cons b ws => simp [rotateWord]

theorem wordIntercept_nonneg (w : List Bool) : 0 ≤ wordIntercept w := by
  induction w with
  | nil => simp [wordIntercept]
  | cons b ws ih =>
    cases b
    · simp only [wordIntercept]; omega
    · simp only [wordIntercept]
      have h3 : (0 : Int) ≤ (3 : Int) ^ wordOddCount ws := by
        clear ih
        induction (wordOddCount ws) with
        | zero => simp
        | succ n ihn => rw [Int.pow_succ]; omega
      omega

theorem wordIntercept_append_false (ws : List Bool) :
    wordIntercept (ws ++ [false]) = wordIntercept ws := by
  induction ws with
  | nil => rfl
  | cons b ts ih =>
    cases b
    · simp only [List.cons_append, wordIntercept, ih]
    · simp only [List.cons_append, wordIntercept, wordOddCount_append, wordOddCount, ih]
      simp

theorem wordIntercept_append_true (ws : List Bool) :
    wordIntercept (ws ++ [true]) = 3 * wordIntercept ws + (2 : Int) ^ ws.length := by
  induction ws with
  | nil => simp [wordIntercept, wordOddCount]
  | cons b ts ih =>
    cases b
    · simp only [List.cons_append, wordIntercept, ih, List.length_cons]
      rw [Int.pow_succ]
      omega
    · simp only [List.cons_append, wordIntercept, wordOddCount_append, wordOddCount, ih,
        List.length_cons, ↓reduceIte, Nat.add_zero]
      rw [Int.pow_succ, Int.pow_succ]
      omega

theorem rotateWordN_full (w : List Bool) : rotateWordN w.length w = w := by
  have hgen : ∀ (u v : List Bool), rotateWordN u.length (u ++ v) = v ++ u := by
    intro u
    induction u with
    | nil => intro v; simp [rotateWordN]
    | cons b us ih =>
      intro v
      simp only [List.length_cons, List.cons_append, rotateWordN, rotateWord]
      have h := ih (v ++ [b])
      rw [List.append_assoc] at h ⊢
      exact h
  have h := hgen w []
  simp only [List.append_nil, List.nil_append] at h
  exact h

/-- One-step integer recursion for `c(rotateWord w)` under rotation of `w`. -/
theorem wordIntercept_rotate_step (b : Bool) (ws : List Bool) :
    2 * wordIntercept (rotateWord (b :: ws)) =
      if b then
        3 * wordIntercept (b :: ws) - ((3 : Int) ^ wordOddCount (b :: ws) - (2 : Int) ^ (b :: ws).length)
      else wordIntercept (b :: ws) := by
  cases b
  · simp only [Bool.false_eq_true, ite_false, rotateWord, wordIntercept,
      wordIntercept_append_false]
  · simp only [ite_true, rotateWord, wordIntercept, wordIntercept_append_true,
      wordOddCount, List.length_cons]
    rw [Nat.add_comm 1 _, Int.pow_succ, Int.pow_succ]
    omega

/-- **Theorem 7 (Positivity Localization — Corollary 4.2, unconditional for all depths).** -/
public theorem collatz_positivity_localization (w : List Bool)
    (hsuper : (2 : Int) ^ w.length < (3 : Int) ^ wordOddCount w) :
    (3 : Int) ^ wordOddCount w - (2 : Int) ^ w.length ≤ wordIntercept w := by
  let D : Int := (3 : Int) ^ wordOddCount w - (2 : Int) ^ w.length
  have hD_pos : 0 < D := by omega
  apply Classical.byContradiction
  intro hlt
  have hcw_lt : wordIntercept w < D := by omega
  have hcomm : ∀ m : Nat, ∀ u : List Bool,
      rotateWordN (m + 1) u = rotateWord (rotateWordN m u) := by
    intro m
    induction m with
    | zero => intro u; rfl
    | succ m ihm => intro u; exact ihm (rotateWord u)
  have hrot_inv : ∀ k : Nat,
      wordOddCount (rotateWordN k w) = wordOddCount w ∧
      (rotateWordN k w).length = w.length := by
    intro k
    induction k with
    | zero => exact ⟨rfl, rfl⟩
    | succ k ih =>
      rw [hcomm k w, wordOddCount_rotate, length_rotate]
      exact ih
  have hmono : ∀ k : Nat, wordIntercept (rotateWordN k w) ≤ wordIntercept w := by
    intro k
    induction k with
    | zero => exact Int.le_refl _
    | succ k ih =>
      rw [hcomm k w]
      have ⟨ho, hl⟩ := hrot_inv k
      cases hu : rotateWordN k w with
      | nil => simp [rotateWord, wordIntercept]; exact wordIntercept_nonneg w
      | cons b ts =>
        have hstep := wordIntercept_rotate_step b ts
        have hDk : (3 : Int) ^ wordOddCount (b :: ts) - (2 : Int) ^ (b :: ts).length = D := by
          rw [← hu, ho, hl]
        rw [hDk] at hstep
        have hcu_le : wordIntercept (b :: ts) ≤ wordIntercept w := by rw [← hu]; exact ih
        cases b
        · simp only [Bool.false_eq_true, ite_false] at hstep
          have hnn : 0 ≤ wordIntercept (rotateWord (false :: ts)) := wordIntercept_nonneg _
          omega
        · simp only [ite_true] at hstep
          omega
  have hex_true : ∃ k : Nat, k < w.length ∧ ∃ ts : List Bool, rotateWordN k w = true :: ts := by
    have haux : ∀ (u v : List Bool), 0 < wordOddCount u →
        ∃ k : Nat, k < u.length ∧ ∃ ts : List Bool, rotateWordN k (u ++ v) = true :: ts := by
      intro u
      induction u with
      | nil => intro _ h0; simp [wordOddCount] at h0
      | cons b us ihu =>
        intro v h0
        cases b
        · simp only [wordOddCount, Bool.false_eq_true, ite_false, Nat.zero_add] at h0
          have ⟨k, hk, ts, hts⟩ := ihu (v ++ [false]) h0
          refine ⟨k + 1, by simp; omega, ts, ?_⟩
          simp only [List.cons_append, rotateWordN, rotateWord]
          rw [← List.append_assoc] at hts
          exact hts
        · exact ⟨0, by simp, us ++ v, rfl⟩
    have ho_pos : 0 < wordOddCount w := by
      apply Classical.byContradiction
      intro h0
      have ho0 : wordOddCount w = 0 := by omega
      rw [ho0] at hsuper
      have h2pos := pow2_pos w.length
      simp at hsuper
      omega
    have ⟨k, hk, ts, hts⟩ := haux w [] ho_pos
    simp only [List.append_nil] at hts
    exact ⟨k, hk, ts, hts⟩
  have ⟨k, hklt, ts, hk_eq⟩ := hex_true
  have hstrict_k1 : wordIntercept (rotateWordN (k + 1) w) < wordIntercept w := by
    rw [hcomm k w, hk_eq]
    have ⟨ho, hl⟩ := hrot_inv k
    have hstep := wordIntercept_rotate_step true ts
    have hDk : (3 : Int) ^ wordOddCount (true :: ts) - (2 : Int) ^ (true :: ts).length = D := by
      rw [← hk_eq, ho, hl]
    rw [hDk] at hstep
    simp only [ite_true] at hstep
    have hle := hmono k
    rw [hk_eq] at hle
    omega
  have hprop : ∀ m : Nat, wordIntercept (rotateWordN (k + 1 + m) w) < wordIntercept w := by
    intro m
    induction m with
    | zero => exact hstrict_k1
    | succ m ihm =>
      have hidx : k + 1 + (m + 1) = (k + 1 + m) + 1 := by omega
      rw [hidx, hcomm (k + 1 + m) w]
      have ⟨ho, hl⟩ := hrot_inv (k + 1 + m)
      cases hu : rotateWordN (k + 1 + m) w with
      | nil =>
        rw [hu] at ihm
        simp [rotateWord, wordIntercept] at ihm ⊢
        exact ihm
      | cons b rs =>
        have hstep := wordIntercept_rotate_step b rs
        have hDk : (3 : Int) ^ wordOddCount (b :: rs) - (2 : Int) ^ (b :: rs).length = D := by
          rw [← hu, ho, hl]
        rw [hDk] at hstep
        rw [hu] at ihm
        cases b
        · simp only [Bool.false_eq_true, ite_false] at hstep
          have hnn := wordIntercept_nonneg (rotateWord (false :: rs))
          omega
        · simp only [ite_true] at hstep
          omega
  have hfinal := hprop (w.length - (k + 1))
  have hsum : k + 1 + (w.length - (k + 1)) = w.length := by omega
  rw [hsum, rotateWordN_full] at hfinal
  omega

-- ----------------------------------------------------------------------------
-- Theorem 8: 3n-1 Sibling Comparison (declaration name kept for compatibility)
-- ----------------------------------------------------------------------------

/-- **Theorem 8 (`3n-1` Sibling Comparison).**
    The sibling map `TMinus` (`3n-1`) shares the identical Terras parity-word bijection
    with `T` yet has positive supercritical cycles at `5` (period 3) and `17` (period 11).
    (The inference that arguments blind to the sign of `ε = ±1` cannot settle `3n+1` is a
    methodological heuristic, not a formalized meta-theorem.) -/
public theorem collatz_epsilon_invariance_barrier :
    (∀ d : Nat,
      (∀ x y : Int, 0 ≤ x → x < (2 : Int) ^ d → 0 ≤ y → y < (2 : Int) ^ d →
        parityWord TMinus d x = parityWord TMinus d y → x = y) ∧
      (∀ w : List Bool, w.length = d →
        ∃ r : Int, 0 ≤ r ∧ r < (2 : Int) ^ d ∧ parityWord TMinus d r = w)) ∧
    (iter TMinus 3 5 = 5 ∧ (2 : Int) ^ 3 < (3 : Int) ^ (oddCount TMinus 3 5)) ∧
    (iter TMinus 11 17 = 17 ∧ (2 : Int) ^ 11 < (3 : Int) ^ (oddCount TMinus 11 17)) := by
  refine ⟨?_, ⟨by decide, by decide⟩, ⟨by decide, by decide⟩⟩
  intro d
  constructor
  · intro x y hx0 hxlt hy0 hylt hw
    exact eq_zero_of_dvd_and_lt hx0 hxlt hy0 hylt
      (terras_inj_general TMinus TMinus_shift_one d x y hw)
  · intro w hlen
    subst hlen
    exact terras_surj_general TMinus TMinus_shift_one parity_exists w

-- ----------------------------------------------------------------------------
-- Theorem 15: Exact Böhm–Sontacchi Cycle Numerator Equation
-- ----------------------------------------------------------------------------

/-- **Theorem 15 (Exact Cycle Equation).**
    Every integer cycle `T^d(x) = x` satisfies `(2^d - 3^o) · x = c(w)`. -/
public theorem collatz_cycle_equation (d : Nat) (x : Int) (hcyc : iter T d x = x) :
    ((2 : Int) ^ d - (3 : Int) ^ (oddCount T d x)) * x = wordIntercept (parityWord T d x) := by
  have h := collatz_exact_intercept_law d x
  rw [hcyc] at h
  rw [Int.sub_mul]
  omega

-- ----------------------------------------------------------------------------
-- Theorem 16: Parity-Word Composition / Cocycle Identity
-- ----------------------------------------------------------------------------

/-- **Theorem 16 (Parity-Word Composition Law).**
    For any map `f : Int → Int`, the length-`(d₁ + d₂)` parity word equals the
    concatenation of the length-`d₁` word from `x` and the length-`d₂` word from `f^{d₁}(x)`. -/
public theorem collatz_parity_word_append (f : Int → Int) (d1 d2 : Nat) (x : Int) :
    parityWord f (d1 + d2) x = parityWord f d1 x ++ parityWord f d2 (iter f d1 x) := by
  induction d1 generalizing x with
  | zero =>
    simp [parityWord, iter]
  | succ d1 ih =>
    have hadd : d1 + 1 + d2 = (d1 + d2) + 1 := by omega
    rw [hadd]
    simp only [parityWord, iter, List.cons_append]
    rw [ih (f x)]

-- ----------------------------------------------------------------------------
-- Theorem 17: Non-Trivial Negative Integer Cycles of True Collatz Map T
-- ----------------------------------------------------------------------------

/-- **Theorem 17 (Non-Trivial Negative Cycles of `3n + 1`).**
    Under the true Collatz shortcut map `T` on `Int`, both `x = -5` (period 3, 2 odd steps)
    and `x = -17` (period 11, 7 odd steps) form genuine supercritical cycles, certifying
    that the Collatz no-nontrivial-cycle conjecture fails on `Int` without `x > 0`. -/
public theorem collatz_negative_cycles :
    (iter T 3 (-5) = -5 ∧ (2 : Int) ^ 3 < (3 : Int) ^ (oddCount T 3 (-5))) ∧
    (iter T 11 (-17) = -17 ∧ (2 : Int) ^ 11 < (3 : Int) ^ (oddCount T 11 (-17))) := by
  exact ⟨⟨by decide, by decide⟩, ⟨by decide, by decide⟩⟩

/-- **Zero fixed point:** `T^d(0) = 0` and `oddCount T d 0 = 0` for all `d`. -/
public theorem collatz_zero_fixed_point (d : Nat) :
    iter T d 0 = 0 ∧ oddCount T d 0 = 0 := by
  induction d with
  | zero => exact ⟨rfl, rfl⟩
  | succ d ih =>
    have h0 : T 0 = 0 := by decide
    have hb0 : parityBit 0 = false := by decide
    constructor
    · simp only [iter, h0]; exact ih.1
    · simp only [oddCount, parityWord, hb0, h0, wordOddCount, Bool.false_eq_true, ite_false, Nat.zero_add]
      exact ih.2

/-- **Non-negativity of affine intercept:** `0 ≤ wordIntercept w` for every parity word `w`. -/
public theorem collatz_intercept_nonneg (w : List Bool) :
    0 ≤ wordIntercept w :=
  wordIntercept_nonneg w

/-- **Parity-word length invariant:** `(parityWord f d x).length = d` for arbitrary `f`. -/
public theorem collatz_parity_word_length (f : Int → Int) (d : Nat) (x : Int) :
    (parityWord f d x).length = d := by
  induction d generalizing x with
  | zero => rfl
  | succ d ih => simp only [parityWord, List.length_cons, ih]

-- ----------------------------------------------------------------------------
-- v0.6.0 Cycle Lower-Bound Foundations (Eliahou / Steiner / Hercher prerequisite)
-- ----------------------------------------------------------------------------

theorem wordIntercept_zero_of_oddCount_zero (w : List Bool) (hz : wordOddCount w = 0) :
    wordIntercept w = 0 := by
  induction w with
  | nil => rfl
  | cons b ws ih =>
    cases b
    · simp only [wordOddCount, Bool.false_eq_true, ite_false, Nat.zero_add] at hz
      simp only [wordIntercept, ih hz]; omega
    · simp only [wordOddCount, ite_true] at hz; omega

theorem pow3_pos (n : Nat) : (1 : Int) ≤ (3 : Int) ^ n := by
  induction n with
  | zero => decide
  | succ k ih => rw [Int.pow_succ]; omega

theorem wordIntercept_pos_of_oddCount_pos (w : List Bool) (hp : 0 < wordOddCount w) :
    0 < wordIntercept w := by
  induction w with
  | nil => simp [wordOddCount] at hp
  | cons b ws ih =>
    cases b
    · simp only [wordOddCount, Bool.false_eq_true, ite_false, Nat.zero_add] at hp
      have hws := ih hp
      simp only [wordIntercept]; omega
    · simp only [wordIntercept]
      have h3 : (1 : Int) ≤ (3 : Int) ^ wordOddCount ws := pow3_pos (wordOddCount ws)
      have hnn : 0 ≤ wordIntercept ws := wordIntercept_nonneg ws
      omega

theorem pow2_ge_two_of_pos (d : Nat) (hd : 1 ≤ d) : (2 : Int) ≤ (2 : Int) ^ d := by
  cases d with
  | zero => omega
  | succ k =>
    have hpos : (1 : Int) ≤ (2 : Int) ^ k := pow2_pos k
    rw [Int.pow_succ]
    omega

/-- **Positive-cycle odd-step necessity:** every positive Collatz cycle `T^d(x) = x` (`d ≥ 1, x > 0`)
    must contain at least one odd step (`oddCount T d x ≥ 1`). -/
public theorem collatz_positive_cycle_has_odd_step (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) :
    1 ≤ oddCount T d x := by
  have heq := collatz_cycle_equation d x hcyc
  by_cases ho : oddCount T d x = 0
  · have hc0 : wordIntercept (parityWord T d x) = 0 :=
      wordIntercept_zero_of_oddCount_zero (parityWord T d x) ho
    rw [ho, hc0] at heq
    have hpow : (2 : Int) ≤ (2 : Int) ^ d := pow2_ge_two_of_pos d hd
    have h30 : (3 : Int) ^ 0 = 1 := rfl
    rw [h30] at heq
    have hpos_prod : 0 < ((2 : Int) ^ d - 1) * x := Int.mul_pos (by omega) hx
    omega
  · omega

/-- **Positive-cycle strict intercept positivity:** every positive Collatz cycle `T^d(x) = x`
    (`d ≥ 1, x > 0`) has strictly positive affine intercept `0 < c(w_d(T, x))`. -/
public theorem collatz_positive_cycle_intercept_pos (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) :
    0 < wordIntercept (parityWord T d x) := by
  have ho := collatz_positive_cycle_has_odd_step d x hd hx hcyc
  exact wordIntercept_pos_of_oddCount_pos (parityWord T d x) ho

/-- **Positive-cycle subcriticality & denominator bound (Eliahou / Steiner / Hercher foundation):**
    Every positive Collatz cycle `T^d(x) = x` (`d ≥ 1, x > 0`) is strictly subcritical
    (`3^o < 2^d`, equivalently `o / d < log₂(2) / log₂(3)`) and satisfies `2^d - 3^o ≤ c(w)`. -/
public theorem collatz_positive_cycle_subcritical (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) :
    (3 : Int) ^ (oddCount T d x) < (2 : Int) ^ d ∧
    (2 : Int) ^ d - (3 : Int) ^ (oddCount T d x) ≤ wordIntercept (parityWord T d x) := by
  have heq := collatz_cycle_equation d x hcyc
  have hcpos := collatz_positive_cycle_intercept_pos d x hd hx hcyc
  have hsub : (3 : Int) ^ (oddCount T d x) < (2 : Int) ^ d := by
    by_cases hle : (2 : Int) ^ d ≤ (3 : Int) ^ (oddCount T d x)
    · have hnp : ((2 : Int) ^ d - (3 : Int) ^ (oddCount T d x)) * x ≤ 0 :=
        Int.mul_nonpos_of_nonpos_of_nonneg (by omega) (by omega)
      omega
    · omega
  refine ⟨hsub, ?_⟩
  have hmul : ((2 : Int) ^ d - (3 : Int) ^ (oddCount T d x)) * 1 ≤
      ((2 : Int) ^ d - (3 : Int) ^ (oddCount T d x)) * x :=
    Int.mul_le_mul_of_nonneg_left (by omega) (by omega)
  rw [Int.mul_one] at hmul
  omega

/-- **No length-1 positive Collatz cycle:** no positive integer `x > 0` is a fixed point of `T`. -/
public theorem collatz_no_positive_cycle_d1 (x : Int) (hx : 0 < x) :
    iter T 1 x ≠ x := by
  simp only [iter, T]
  split
  · omega
  · omega

-- ----------------------------------------------------------------------------
-- v0.7.0 Deep Collatz Frontier: 2-Adic Isometry, Odd-Unit-Lock Periodic-Echo
-- Valuation Law, Unconditional Fine–Wilf Spine Ceiling, Cycle Eliminations
-- through d ≤ 7, and Catalytic Reversible Cylinder Evaluation
-- ----------------------------------------------------------------------------

/-- **2-Adic Cylinder Isometry:** for all integers `x, y` and depths `d`,
    `parityWord T d x = parityWord T d y ↔ (x - y) % 2^d = 0`. -/
public theorem collatz_2adic_isometry (d : Nat) (x y : Int) :
    parityWord T d x = parityWord T d y ↔ (x - y) % ((2 : Int) ^ d) = 0 := by
  constructor
  · exact terras_inj_general T T_shift_one d x y
  · intro hdiv
    have ⟨q, hq⟩ := Int.dvd_of_emod_eq_zero hdiv
    have hxy : x = (2 : Int) ^ d * q + y := by omega
    rw [hxy]
    exact (collatz_cylinder_affine_and_word d q y).1

theorem dvd_pow2_of_odd_mul (m : Nat) (D : Int) (hodd : D % 2 ≠ 0) :
    ∀ z : Int, (D * z) % ((2 : Int) ^ m) = 0 → z % ((2 : Int) ^ m) = 0 := by
  induction m with
  | zero => intro z _; simp
  | succ m ihm =>
    intro z hz
    have hdiv : (2 : Int) ^ (m + 1) = 2 * (2 : Int) ^ m := by rw [Int.pow_succ, Int.mul_comm]
    have ⟨q, hq⟩ := Int.dvd_of_emod_eq_zero hz
    rw [hdiv] at hq
    have hDz2 : (D * z) % 2 = 0 := Int.emod_eq_zero_of_dvd ⟨(2 : Int) ^ m * q, by
      rw [hq, Int.mul_assoc]⟩
    have hDm : D % 2 = 1 := by omega
    have hz_even : z % 2 = 0 := by
      have hmul : (D * z) % 2 = ((D % 2) * (z % 2)) % 2 := Int.mul_emod D z 2
      rw [hDm, Int.one_mul] at hmul
      omega
    let z' := z / 2
    have hz_eq : z = 2 * z' := by omega
    have hq' : D * z' = (2 : Int) ^ m * q := by
      have h2eq : 2 * (D * z') = 2 * ((2 : Int) ^ m * q) := by
        calc 2 * (D * z') = D * (2 * z') := by rw [← Int.mul_assoc, Int.mul_comm 2 D, Int.mul_assoc]
        _ = D * z := by rw [← hz_eq]
        _ = 2 * (2 : Int) ^ m * q := hq
        _ = 2 * ((2 : Int) ^ m * q) := Int.mul_assoc _ _ _
      omega
    have hz' : (D * z') % ((2 : Int) ^ m) = 0 := Int.emod_eq_zero_of_dvd ⟨q, hq'⟩
    have ⟨q2, hq2⟩ := Int.dvd_of_emod_eq_zero (ihm z' hz')
    rw [hz_eq, hdiv]
    exact Int.emod_eq_zero_of_dvd ⟨q2, by rw [hq2, Int.mul_assoc]⟩

theorem pow3_odd (n : Nat) : ((3 : Int) ^ n) % 2 = 1 := by
  induction n with
  | zero => decide
  | succ k ih =>
    rw [Int.pow_succ, Int.mul_emod, ih]
    decide

theorem spineDenom_odd (w : List Bool) (hw : 1 ≤ w.length) :
    spineDenom w % 2 ≠ 0 := by
  unfold spineDenom
  cases hlen : w.length with
  | zero => omega
  | succ m =>
    have h2 : ((2 : Int) ^ (m + 1)) % 2 = 0 := by
      rw [Int.pow_succ]
      exact Int.emod_eq_zero_of_dvd ⟨(2 : Int) ^ m, by rw [Int.mul_comm]⟩
    have h3 : ((3 : Int) ^ wordOddCount w) % 2 = 1 := pow3_odd (wordOddCount w)
    have hsub := Int.sub_emod ((2 : Int) ^ (m + 1)) ((3 : Int) ^ wordOddCount w) 2
    rw [h2, h3] at hsub
    omega

theorem periodicPrefixFrom_length (w : List Bool) (start k : Nat) :
    (periodicPrefixFrom w start k).length = k := by
  induction k generalizing start with
  | zero => rfl
  | succ k ih => simp [periodicPrefixFrom, ih]

theorem periodicPrefix_length (w : List Bool) (k : Nat) :
    (periodicPrefix w k).length = k :=
  periodicPrefixFrom_length w 0 k

theorem periodicPrefixFrom_append (w : List Bool) (start k1 k2 : Nat) :
    periodicPrefixFrom w start (k1 + k2) =
      periodicPrefixFrom w start k1 ++ periodicPrefixFrom w (start + k1) k2 := by
  induction k1 generalizing start with
  | zero => simp [periodicPrefixFrom]
  | succ k1 ih =>
    have hadd : k1 + 1 + k2 = (k1 + k2) + 1 := by omega
    rw [hadd]
    simp only [periodicPrefixFrom, List.cons_append]
    have hst : start + 1 + k1 = start + (k1 + 1) := by omega
    rw [ih (start + 1), hst]

theorem periodicBit_add_len (w : List Bool) (i : Nat) :
    periodicBit w (i + w.length) = periodicBit w i := by
  unfold periodicBit
  rw [Nat.add_mod_right]

theorem periodicPrefixFrom_add_len (w : List Bool) (start k : Nat) :
    periodicPrefixFrom w (start + w.length) k = periodicPrefixFrom w start k := by
  induction k generalizing start with
  | zero => rfl
  | succ k ih =>
    simp only [periodicPrefixFrom, periodicBit_add_len]
    have hst : start + w.length + 1 = (start + 1) + w.length := by omega
    rw [hst, ih (start + 1)]

theorem periodicPrefix_self (w : List Bool) :
    periodicPrefix w w.length = w := by
  have haux : ∀ (u v : List Bool),
      periodicPrefixFrom (u ++ v) u.length v.length = v := by
    intro u v
    induction v generalizing u with
    | nil => rfl
    | cons b vs ih =>
      simp only [List.length_cons, periodicPrefixFrom]
      have hbit : periodicBit (u ++ b :: vs) u.length = b := by
        unfold periodicBit
        have hlt : u.length < (u ++ b :: vs).length := by simp
        rw [Nat.mod_eq_of_lt hlt]
        have hget : (u ++ b :: vs).getD u.length false = b := by
          clear ih hlt
          induction u with
          | nil => rfl
          | cons a us ihu =>
            simp only [List.cons_append, List.length_cons, List.getD_cons_succ]
            exact ihu
        exact hget
      rw [hbit]
      have hrec := ih (u ++ [b])
      have hcat : (u ++ [b]) ++ vs = u ++ (b :: vs) := by
        rw [List.append_assoc]; rfl
      have hlen : (u ++ [b]).length = u.length + 1 := by simp
      rw [hcat, hlen] at hrec
      rw [hrec]
  have h := haux [] w
  simp only [List.nil_append, List.length_nil] at h
  exact h

theorem list_append_inj_of_len {α : Type} {a b c d : List α}
    (hlen : a.length = c.length) (heq : a ++ b = c ++ d) : a = c ∧ b = d := by
  induction a generalizing c with
  | nil =>
    cases c with
    | nil => exact ⟨rfl, heq⟩
    | cons _ _ => simp at hlen
  | cons x xs ih =>
    cases c with
    | nil => simp at hlen
    | cons y ys =>
      simp only [List.length_cons, List.cons_append, List.cons.injEq] at hlen heq
      have ⟨h1, h2⟩ := ih (by omega) heq.2
      exact ⟨by rw [heq.1, h1], h2⟩

theorem periodicPrefix_congruence_forward (w : List Bool) (k : Nat) (x : Int)
    (hword : parityWord T k x = periodicPrefix w k) :
    (spineDenom w * x - wordIntercept w) % ((2 : Int) ^ k) = 0 := by
  -- Lift to depth w.length + k via Terras surjectivity
  have ⟨y, _, _, hyw⟩ := (terras_parity_word_bijection (w.length + k)).2
    (periodicPrefix w (w.length + k)) (periodicPrefix_length w (w.length + k))
  have hsplit_p : periodicPrefix w (w.length + k) = w ++ periodicPrefix w k := by
    unfold periodicPrefix
    rw [periodicPrefixFrom_append, periodicPrefixFrom_add_len]
    have hself : periodicPrefixFrom w 0 w.length = w := periodicPrefix_self w
    rw [hself]
  have hsplit_y : parityWord T (w.length + k) y =
      parityWord T w.length y ++ parityWord T k (iter T w.length y) :=
    collatz_parity_word_append T w.length k y
  rw [hsplit_y, hsplit_p] at hyw
  have ⟨hy_head, hy_tail⟩ := list_append_inj_of_len (collatz_parity_word_length T w.length y) hyw
  -- Also first k bits of y match periodicPrefix w k = parityWord T k x
  have hy_pref_k : parityWord T k y = periodicPrefix w k := by
    have hsplit_y2 : parityWord T (k + w.length) y =
        parityWord T k y ++ parityWord T w.length (iter T k y) :=
      collatz_parity_word_append T k w.length y
    have hsplit_p2 : periodicPrefix w (k + w.length) =
        periodicPrefix w k ++ periodicPrefixFrom w k w.length := by
      unfold periodicPrefix
      rw [periodicPrefixFrom_append, Nat.zero_add]
    have hcomm : k + w.length = w.length + k := Nat.add_comm k w.length
    have hyw2 : parityWord T (k + w.length) y = periodicPrefix w (k + w.length) := by
      rw [hcomm, hsplit_y, hsplit_p]
      exact hyw
    rw [hsplit_y2, hsplit_p2] at hyw2
    have hlen_k : (parityWord T k y).length = (periodicPrefix w k).length := by
      rw [collatz_parity_word_length, periodicPrefix_length]
    exact (list_append_inj_of_len hlen_k hyw2).1
  -- Since parityWord T k (T^|w|(y)) = periodicPrefix w k = parityWord T k y, 2^k ∣ (T^|w|(y) - y)
  have hshift_eq : parityWord T k (iter T w.length y) = parityWord T k y := by
    rw [hy_tail, hy_pref_k]
  have hdvd_step : (iter T w.length y - y) % ((2 : Int) ^ k) = 0 :=
    (collatz_2adic_isometry k (iter T w.length y) y).mp hshift_eq
  have ⟨q1, hq1⟩ := Int.dvd_of_emod_eq_zero hdvd_step
  -- Exact intercept law on y at depth |w|: 2^|w| * T^|w|(y) = 3^o * y + c(w)
  have hlaw := collatz_exact_intercept_law w.length y
  unfold oddCount at hlaw
  rw [hy_head] at hlaw
  have hy_cong : (spineDenom w * y - wordIntercept w) % ((2 : Int) ^ k) = 0 := by
    unfold spineDenom
    refine Int.emod_eq_zero_of_dvd ⟨-((2 : Int) ^ w.length * q1), ?_⟩
    have hmul : (2 : Int) ^ w.length * (iter T w.length y - y) =
        (2 : Int) ^ w.length * ((2 : Int) ^ k * q1) := by rw [hq1]
    have h1 : (2 : Int) ^ w.length * (iter T w.length y - y) =
        (2 : Int) ^ w.length * iter T w.length y - (2 : Int) ^ w.length * y := Int.mul_sub _ _ _
    have h2 : ((2 : Int) ^ w.length - (3 : Int) ^ wordOddCount w) * y =
        (2 : Int) ^ w.length * y - (3 : Int) ^ wordOddCount w * y := Int.sub_mul _ _ _
    have h3 : (2 : Int) ^ w.length * ((2 : Int) ^ k * q1) =
        (2 : Int) ^ k * ((2 : Int) ^ w.length * q1) := by
      rw [← Int.mul_assoc, Int.mul_comm ((2 : Int) ^ w.length) ((2 : Int) ^ k), Int.mul_assoc]
    have h4 : (2 : Int) ^ k * -((2 : Int) ^ w.length * q1) =
        -((2 : Int) ^ k * ((2 : Int) ^ w.length * q1)) := Int.mul_neg _ _
    omega
  -- Finally x ≡ y (mod 2^k) since parityWord T k x = periodicPrefix w k = parityWord T k y
  have hxy_dvd : (x - y) % ((2 : Int) ^ k) = 0 :=
    (collatz_2adic_isometry k x y).mp (by rw [hword, hy_pref_k])
  have ⟨q2, hq2⟩ := Int.dvd_of_emod_eq_zero hxy_dvd
  have ⟨q3, hq3⟩ := Int.dvd_of_emod_eq_zero hy_cong
  refine Int.emod_eq_zero_of_dvd ⟨spineDenom w * q2 + q3, ?_⟩
  have hdiff : spineDenom w * x - wordIntercept w =
      spineDenom w * (x - y) + (spineDenom w * y - wordIntercept w) := by
    rw [Int.mul_sub]; omega
  rw [hdiff, hq2, hq3, Int.mul_add]
  have hcomm : spineDenom w * ((2 : Int) ^ k * q2) = (2 : Int) ^ k * (spineDenom w * q2) := by
    rw [← Int.mul_assoc, Int.mul_comm (spineDenom w) ((2 : Int) ^ k), Int.mul_assoc]
  rw [hcomm]

/-- **Periodic Spine Congruence Theorem:** for every non-empty parity word `w`,
    every precision `k`, and every integer `x`,
    `(D(w) * x - c(w)) % 2^k = 0 ↔ parityWord T k x = periodicPrefix w k`. -/
public theorem collatz_periodic_spine_congruence (w : List Bool) (k : Nat) (x : Int)
    (hw : 1 ≤ w.length) :
    (spineDenom w * x - wordIntercept w) % ((2 : Int) ^ k) = 0 ↔
      parityWord T k x = periodicPrefix w k := by
  constructor
  · intro hcong
    have ⟨y, _, _, hyw⟩ := (terras_parity_word_bijection k).2
      (periodicPrefix w k) (periodicPrefix_length w k)
    have hy_cong := periodicPrefix_congruence_forward w k y hyw
    have ⟨q1, hq1⟩ := Int.dvd_of_emod_eq_zero hcong
    have ⟨q2, hq2⟩ := Int.dvd_of_emod_eq_zero hy_cong
    have hDxy : (spineDenom w * (x - y)) % ((2 : Int) ^ k) = 0 := by
      refine Int.emod_eq_zero_of_dvd ⟨q1 - q2, ?_⟩
      rw [Int.mul_sub, Int.mul_sub]
      omega
    have hxy := dvd_pow2_of_odd_mul k (spineDenom w) (spineDenom_odd w hw) (x - y) hDxy
    have hpw := (collatz_2adic_isometry k x y).mpr hxy
    rw [hpw, hyw]
  · exact periodicPrefix_congruence_forward w k x

/-- **Odd-Unit-Lock Exact Periodic-Echo Valuation Isometry:**
    For ANY two non-empty parity words `w, v` and ANY 2-adic precision `k`,
    the cleared-denominator spine separation `c(w) D(v) - c(v) D(w)` is divisible by `2^k`
    if and only if the infinite periodic parity words `w^∞` and `v^∞` agree on their first `k` bits.
    Equivalently: `v₂(ρ_w - ρ_v) = lcp(w^∞, v^∞)`. -/
public theorem collatz_odd_unit_lock_valuation_isometry (w v : List Bool) (k : Nat)
    (hw : 1 ≤ w.length) (hv : 1 ≤ v.length) :
    (wordIntercept w * spineDenom v - wordIntercept v * spineDenom w) % ((2 : Int) ^ k) = 0 ↔
      periodicPrefix w k = periodicPrefix v k := by
  have ⟨x, _, _, hxw⟩ := (terras_parity_word_bijection k).2
    (periodicPrefix w k) (periodicPrefix_length w k)
  have ⟨y, _, _, hyv⟩ := (terras_parity_word_bijection k).2
    (periodicPrefix v k) (periodicPrefix_length v k)
  have hx_cong := periodicPrefix_congruence_forward w k x hxw
  have hy_cong := periodicPrefix_congruence_forward v k y hyv
  have ⟨qx, hqx⟩ := Int.dvd_of_emod_eq_zero hx_cong
  have ⟨qy, hqy⟩ := Int.dvd_of_emod_eq_zero hy_cong
  -- Identity: c(w)*D(v) - c(v)*D(w) = D(w)*D(v)*(x - y) - D(v)*(D(w)*x - c(w)) + D(w)*(D(v)*y - c(v))
  have hid : wordIntercept w * spineDenom v - wordIntercept v * spineDenom w =
      (spineDenom w * spineDenom v) * (x - y) -
      spineDenom v * (spineDenom w * x - wordIntercept w) +
      spineDenom w * (spineDenom v * y - wordIntercept v) := by
    have h1 : (spineDenom w * spineDenom v) * (x - y) =
        spineDenom w * spineDenom v * x - spineDenom w * spineDenom v * y := Int.mul_sub _ _ _
    have h2 : spineDenom v * (spineDenom w * x - wordIntercept w) =
        spineDenom v * (spineDenom w * x) - spineDenom v * wordIntercept w := Int.mul_sub _ _ _
    have h3 : spineDenom w * (spineDenom v * y - wordIntercept v) =
        spineDenom w * (spineDenom v * y) - spineDenom w * wordIntercept v := Int.mul_sub _ _ _
    have hc1 : spineDenom v * (spineDenom w * x) = spineDenom w * spineDenom v * x := by
      rw [← Int.mul_assoc, Int.mul_comm (spineDenom v) (spineDenom w)]
    have hc2 : spineDenom w * (spineDenom v * y) = spineDenom w * spineDenom v * y := by
      rw [← Int.mul_assoc]
    have hc3 : spineDenom v * wordIntercept w = wordIntercept w * spineDenom v := Int.mul_comm _ _
    have hc4 : spineDenom w * wordIntercept v = wordIntercept v * spineDenom w := Int.mul_comm _ _
    omega
  have hDprod_odd : (spineDenom w * spineDenom v) % 2 ≠ 0 := by
    have hwo := spineDenom_odd w hw
    have hvo := spineDenom_odd v hv
    have hw1 : spineDenom w % 2 = 1 := by omega
    have hv1 : spineDenom v % 2 = 1 := by omega
    rw [Int.mul_emod, hw1, hv1]
    decide
  constructor
  · intro hsep
    have ⟨qs, hqs⟩ := Int.dvd_of_emod_eq_zero hsep
    have hprod_dvd : ((spineDenom w * spineDenom v) * (x - y)) % ((2 : Int) ^ k) = 0 := by
      refine Int.emod_eq_zero_of_dvd ⟨qs + spineDenom v * qx - spineDenom w * qy, ?_⟩
      have hrhs : (2 : Int) ^ k * (qs + spineDenom v * qx - spineDenom w * qy) =
          (2 : Int) ^ k * qs + (2 : Int) ^ k * (spineDenom v * qx) -
          (2 : Int) ^ k * (spineDenom w * qy) := by
        rw [Int.mul_sub, Int.mul_add]
      have ha : (2 : Int) ^ k * (spineDenom v * qx) = spineDenom v * ((2 : Int) ^ k * qx) := by
        rw [← Int.mul_assoc, Int.mul_comm ((2 : Int) ^ k) (spineDenom v), Int.mul_assoc]
      have hb : (2 : Int) ^ k * (spineDenom w * qy) = spineDenom w * ((2 : Int) ^ k * qy) := by
        rw [← Int.mul_assoc, Int.mul_comm ((2 : Int) ^ k) (spineDenom w), Int.mul_assoc]
      rw [hrhs, ha, hb, ← hqx, ← hqy, ← hqs]
      omega
    have hxy := dvd_pow2_of_odd_mul k (spineDenom w * spineDenom v) hDprod_odd (x - y) hprod_dvd
    have hpw := (collatz_2adic_isometry k x y).mpr hxy
    rw [← hxw, ← hyv, hpw]
  · intro hpref
    have hpw : parityWord T k x = parityWord T k y := by rw [hxw, hyv, hpref]
    have hxy := (collatz_2adic_isometry k x y).mp hpw
    have ⟨qxy, hqxy⟩ := Int.dvd_of_emod_eq_zero hxy
    refine Int.emod_eq_zero_of_dvd ⟨(spineDenom w * spineDenom v) * qxy - spineDenom v * qx + spineDenom w * qy, ?_⟩
    rw [hid, hqxy, hqx, hqy, Int.mul_add, Int.mul_sub]
    have ha : (2 : Int) ^ k * ((spineDenom w * spineDenom v) * qxy) =
        (spineDenom w * spineDenom v) * ((2 : Int) ^ k * qxy) := by
      rw [← Int.mul_assoc, Int.mul_comm ((2 : Int) ^ k) _, Int.mul_assoc]
    have hb : (2 : Int) ^ k * (spineDenom v * qx) = spineDenom v * ((2 : Int) ^ k * qx) := by
      rw [← Int.mul_assoc, Int.mul_comm ((2 : Int) ^ k) _, Int.mul_assoc]
    have hc : (2 : Int) ^ k * (spineDenom w * qy) = spineDenom w * ((2 : Int) ^ k * qy) := by
      rw [← Int.mul_assoc, Int.mul_comm ((2 : Int) ^ k) _, Int.mul_assoc]
    rw [ha, hb, hc]

-- ----------------------------------------------------------------------------
-- Fine–Wilf Periodicity Theorem & Unconditional Odd-Unit-Lock Valuation Ceiling
-- ----------------------------------------------------------------------------

theorem periodicPrefixFrom_eq_iff (w v : List Bool) (start k : Nat) :
    periodicPrefixFrom w start k = periodicPrefixFrom v start k ↔
      ∀ i : Nat, i < k → periodicBit w (start + i) = periodicBit v (start + i) := by
  induction k generalizing start with
  | zero =>
    constructor
    · intro _ i hi; omega
    · intro _; rfl
  | succ k ih =>
    simp only [periodicPrefixFrom, List.cons.injEq]
    constructor
    · intro ⟨h0, htail⟩ i hi
      cases i with
      | zero => simpa using h0
      | succ j =>
        have hj : j < k := by omega
        have hstep := (ih (start + 1)).mp htail j hj
        have hidx : start + 1 + j = start + (j + 1) := by omega
        rw [← hidx]; exact hstep
    · intro hall
      refine ⟨by simpa using hall 0 (by omega), (ih (start + 1)).mpr ?_⟩
      intro j hj
      have hidx : start + 1 + j = start + (j + 1) := by omega
      rw [hidx]
      exact hall (j + 1) (by omega)

theorem nat_gcd_sub_right (p q : Nat) (hpq : p ≤ q) :
    Nat.gcd p (q - p) = Nat.gcd p q := by
  have h1 : Nat.gcd p (q - p) = Nat.gcd (q - p) p := Nat.gcd_comm p (q - p)
  have h2 : Nat.gcd q p = Nat.gcd p q := Nat.gcd_comm q p
  rw [h1, ← h2]
  have hadd : (q - p) + p = q := by omega
  have hstep : Nat.gcd (q - p) p = Nat.gcd ((q - p) + p) p := (Nat.gcd_add_self_left p (q - p)).symm
  rw [hadd] at hstep
  exact hstep

theorem fine_wilf_periodic_aux :
    ∀ (s p q : Nat) (f g : Nat → Bool),
      p + q ≤ s → 1 ≤ p → 1 ≤ q →
      (∀ i, f (i + p) = f i) → (∀ i, g (i + q) = g i) →
      (∀ i, i < p + q - Nat.gcd p q → f i = g i) →
      ∀ i, f i = g i := by
  intro s
  induction s with
  | zero => intro p q _ _ hs hp _ _ _ _; omega
  | succ s ih =>
    intro p q f g hs hp hq hf hg hagree
    have hmod_f : ∀ i : Nat, f i = f (i % p) := by
      intro i
      have hdiv : i = i % p + p * (i / p) := by
        have := Nat.div_add_mod i p; omega
      have hmul : ∀ m r : Nat, f (r + p * m) = f r := by
        intro m
        induction m with
        | zero => intro r; simp
        | succ m ihm =>
          intro r
          have hstep : r + p * (m + 1) = (r + p * m) + p := by
            rw [Nat.mul_add, Nat.mul_one, Nat.add_assoc]
          rw [hstep, hf, ihm]
      have hres := hmul (i / p) (i % p)
      rw [← hdiv] at hres
      exact hres
    have hmod_g : ∀ i : Nat, g i = g (i % q) := by
      intro i
      have hdiv : i = i % q + q * (i / q) := by
        have := Nat.div_add_mod i q; omega
      have hmul : ∀ m r : Nat, g (r + q * m) = g r := by
        intro m
        induction m with
        | zero => intro r; simp
        | succ m ihm =>
          intro r
          have hstep : r + q * (m + 1) = (r + q * m) + q := by
            rw [Nat.mul_add, Nat.mul_one, Nat.add_assoc]
          rw [hstep, hg, ihm]
      have hres := hmul (i / q) (i % q)
      rw [← hdiv] at hres
      exact hres
    by_cases heq : p = q
    · subst heq
      intro i
      rw [hmod_f i, hmod_g i]
      have hlt : i % p < p := Nat.mod_lt i (by omega)
      have hgcd : Nat.gcd p p = p := Nat.gcd_self p
      exact hagree (i % p) (by omega)
    · have hstep : ∀ (a b : Nat) (u v : Nat → Bool),
          a + b ≤ s + 1 → 1 ≤ a → a < b →
          (∀ i, u (i + a) = u i) → (∀ i, v (i + b) = v i) →
          (∀ i, i < a + b - Nat.gcd a b → u i = v i) →
          ∀ i, u i = v i := by
        intro a b u v hab ha hlt hu hv huv
        let b' := b - a
        let h : Nat → Bool := fun i => v (i % b')
        have hb'pos : 1 ≤ b' := by omega
        have hh_per : ∀ i, h (i + b') = h i := by
          intro i; simp only [h, Nat.add_mod_right]
        have hgcd_eq : Nat.gcd a b' = Nat.gcd a b := nat_gcd_sub_right a b (by omega)
        have hgcd_le_a : Nat.gcd a b ≤ a := Nat.gcd_le_left b (by omega)
        have huh_aux : ∀ m : Nat, ∀ i : Nat, i ≤ m → i < b - Nat.gcd a b → u i = h i := by
          intro m
          induction m with
          | zero =>
            intro i hi _
            have hi0 : i = 0 := by omega
            subst hi0
            simp only [h, Nat.zero_mod]
            exact huv 0 (by omega)
          | succ m ihm =>
            intro i him hi
            by_cases hic : i < b'
            · simp only [h, Nat.mod_eq_of_lt hic]
              exact huv i (by omega)
            · let j := i - b'
              have hji : j ≤ m := by omega
              have hjlt : j < b - Nat.gcd a b := by omega
              have hj_eq : u j = h j := ihm j hji hjlt
              have hij_mod : i % b' = j % b' := by
                have hadd : i = j + b' := by omega
                rw [hadd, Nat.add_mod_right]
              have hjp : j + b = i + a := by omega
              have h1 : u i = u (i + a) := (hu i).symm
              have h2 : u (i + a) = v (i + a) := huv (i + a) (by omega)
              have h3 : v (i + a) = v (j + b) := by rw [hjp]
              have h4 : v (j + b) = v j := hv j
              have h5 : v j = u j := (huv j (by omega)).symm
              have h6 : h j = h i := by simp only [h, hij_mod]
              rw [h1, h2, h3, h4, h5, hj_eq, h6]
        have huh : ∀ i, i < a + b' - Nat.gcd a b' → u i = h i := by
          intro i hi
          rw [hgcd_eq] at hi
          exact huh_aux i i (Nat.le_refl i) (by omega)
        have hu_eq_h : ∀ i, u i = h i :=
          ih a b' u h (by omega) ha hb'pos hu hh_per huh
        have hu_per_b : ∀ i, u (i + b) = u i := by
          intro i
          have hsplit : i + b = (i + a) + b' := by omega
          rw [hsplit, hu_eq_h ((i + a) + b'), hh_per (i + a), ← hu_eq_h (i + a), hu i]
        have hmod_u : ∀ i : Nat, u i = u (i % b) := by
          intro i
          have hdiv : i = i % b + b * (i / b) := by
            have := Nat.div_add_mod i b; omega
          have hmul : ∀ m r : Nat, u (r + b * m) = u r := by
            intro m
            induction m with
            | zero => intro r; simp
            | succ m ihm =>
              intro r
              have hst : r + b * (m + 1) = (r + b * m) + b := by
                rw [Nat.mul_add, Nat.mul_one, Nat.add_assoc]
              rw [hst, hu_per_b, ihm]
          have hres := hmul (i / b) (i % b)
          rw [← hdiv] at hres
          exact hres
        have hmod_v : ∀ i : Nat, v i = v (i % b) := by
          intro i
          have hdiv : i = i % b + b * (i / b) := by
            have := Nat.div_add_mod i b; omega
          have hmul : ∀ m r : Nat, v (r + b * m) = v r := by
            intro m
            induction m with
            | zero => intro r; simp
            | succ m ihm =>
              intro r
              have hst : r + b * (m + 1) = (r + b * m) + b := by
                rw [Nat.mul_add, Nat.mul_one, Nat.add_assoc]
              rw [hst, hv, ihm]
          have hres := hmul (i / b) (i % b)
          rw [← hdiv] at hres
          exact hres
        intro i
        rw [hmod_u i, hmod_v i]
        have hlt_b : i % b < b := Nat.mod_lt i (by omega)
        exact huv (i % b) (by omega)
      by_cases hlt : p < q
      · exact hstep p q f g hs hp hlt hf hg hagree
      · intro i
        have hqlt : q < p := by omega
        have hagree' : ∀ j, j < q + p - Nat.gcd q p → g j = f j := by
          intro j hj
          rw [Nat.gcd_comm] at hj
          exact (hagree j (by omega)).symm
        exact (hstep q p g f (by omega) hq hqlt hg hf hagree' i).symm

theorem int_zero_of_dvd_all_pow2 (z : Int) (hall : ∀ k : Nat, z % ((2 : Int) ^ k) = 0) : z = 0 := by
  have hbound : ∀ n : Nat, (n : Int) < (2 : Int) ^ n := by
    intro n
    induction n with
    | zero => decide
    | succ n ih =>
      rw [Int.pow_succ]
      have hpos := pow2_pos n
      omega
  let k := z.natAbs + 1
  have hdiv := hall k
  have ⟨q, hq⟩ := Int.dvd_of_emod_eq_zero hdiv
  have hlt : (z.natAbs : Int) < (2 : Int) ^ k := by
    have hb := hbound k
    omega
  have hpos := pow2_pos k
  by_cases hqp : 1 ≤ q
  · have h1 := Int.mul_le_mul_of_nonneg_left hqp (by omega : (0 : Int) ≤ (2 : Int) ^ k)
    rw [Int.mul_one] at h1
    omega
  · by_cases hqn : q ≤ -1
    · have h2 := Int.mul_le_mul_of_nonneg_left hqn (by omega : (0 : Int) ≤ (2 : Int) ^ k)
      have hm1 : (2 : Int) ^ k * (-1) = -((2 : Int) ^ k) := by omega
      rw [hm1] at h2
      omega
    · have hq0 : q = 0 := by omega
      rw [hq0, Int.mul_zero] at hq
      exact hq

/-- **Unconditional Fine–Wilf Odd-Unit-Lock Spine Valuation Ceiling:**
    For ANY two non-empty parity words `w, v` with distinct rational periodic spines
    (`c(w) D(v) ≠ c(v) D(w)`), the cleared-denominator spine separation is NOT divisible by
    `2^(|w| + |v| - gcd(|w|, |v|))`. Equivalently:
    `v₂(ρ_w - ρ_v) ≤ |w| + |v| - gcd(|w|, |v|) - 1`. -/
public theorem collatz_fine_wilf_spine_ceiling (w v : List Bool)
    (hw : 1 ≤ w.length) (hv : 1 ≤ v.length)
    (hne : wordIntercept w * spineDenom v ≠ wordIntercept v * spineDenom w) :
    (wordIntercept w * spineDenom v - wordIntercept v * spineDenom w) %
      ((2 : Int) ^ (w.length + v.length - Nat.gcd w.length v.length)) ≠ 0 := by
  intro hdiv
  let L := w.length + v.length - Nat.gcd w.length v.length
  have hpref : periodicPrefix w L = periodicPrefix v L :=
    (collatz_odd_unit_lock_valuation_isometry w v L hw hv).mp hdiv
  have hagree : ∀ i, i < L → periodicBit w i = periodicBit v i := by
    intro i hi
    have h := (periodicPrefixFrom_eq_iff w v 0 L).mp hpref i hi
    simpa using h
  have hall_bits : ∀ i, periodicBit w i = periodicBit v i :=
    fine_wilf_periodic_aux (w.length + v.length) w.length v.length
      (periodicBit w) (periodicBit v) (Nat.le_refl _) hw hv
      (periodicBit_add_len w) (periodicBit_add_len v) hagree
  have hall_div : ∀ k : Nat,
      (wordIntercept w * spineDenom v - wordIntercept v * spineDenom w) % ((2 : Int) ^ k) = 0 := by
    intro k
    apply (collatz_odd_unit_lock_valuation_isometry w v k hw hv).mpr
    apply (periodicPrefixFrom_eq_iff w v 0 k).mpr
    intro i _
    exact hall_bits (0 + i)
  have hzero := int_zero_of_dvd_all_pow2 _ hall_div
  omega

-- ----------------------------------------------------------------------------
-- Exact Low-Period Positive Cycle Eliminations (d ≤ 7) & Trivial Cycle Orbit
-- ----------------------------------------------------------------------------

/-- **Exact Trivial Cycle Orbit (`1 ↔ 2`):** for all `k : Nat`,
    `T^(2k)(1) = 1`, `T^(2k+1)(1) = 2`, `T^(2k)(2) = 2`, and `T^(2k+1)(2) = 1`. -/
public theorem collatz_trivial_cycle_orbit (k : Nat) :
    iter T (2 * k) 1 = 1 ∧ iter T (2 * k + 1) 1 = 2 ∧
    iter T (2 * k) 2 = 2 ∧ iter T (2 * k + 1) 2 = 1 := by
  have hT1 : T 1 = 2 := by decide
  have hT2 : T 2 = 1 := by decide
  induction k with
  | zero => exact ⟨rfl, hT1, rfl, hT2⟩
  | succ k ih =>
    have he1 : 2 * (k + 1) = 2 * k + 2 := by omega
    have ho1 : 2 * (k + 1) + 1 = (2 * k + 1) + 2 := by omega
    have hstep2 : ∀ m x, iter T (m + 2) x = iter T m (T (T x)) := by
      intro m x; rfl
    have hTT1 : T (T 1) = 1 := by rw [hT1, hT2]
    have hTT2 : T (T 2) = 2 := by rw [hT2, hT1]
    refine ⟨?_, ?_, ?_, ?_⟩
    · rw [he1, hstep2, hTT1]; exact ih.1
    · rw [ho1, hstep2, hTT1]; exact ih.2.1
    · rw [he1, hstep2, hTT2]; exact ih.2.2.1
    · rw [ho1, hstep2, hTT2]; exact ih.2.2.2

def allBoolWords : Nat → List (List Bool)
  | 0 => [[]]
  | d + 1 => (allBoolWords d).map (false :: ·) ++ (allBoolWords d).map (true :: ·)

theorem mem_allBoolWords (w : List Bool) : w ∈ allBoolWords w.length := by
  induction w with
  | nil => simp [allBoolWords]
  | cons b ws ih =>
    simp only [List.length_cons, allBoolWords, List.mem_append, List.mem_map]
    cases b
    · exact Or.inl ⟨ws, ih, rfl⟩
    · exact Or.inr ⟨ws, ih, rfl⟩

def isOnlyTrivialCycleWord (w : List Bool) : Bool :=
  let D := spineDenom w
  let c := wordIntercept w
  !(decide (0 < D ∧ 0 < c ∧ c % D = 0 ∧ c ≠ D ∧ c ≠ 2 * D))

theorem no_nontrivial_cycle_of_check (d : Nat) (hd : 1 ≤ d)
    (hchk : (allBoolWords d).all isOnlyTrivialCycleWord = true) :
    ∀ x : Int, 0 < x → iter T d x = x → x = 1 ∨ x = 2 := by
  intro x hx hcyc
  let w := parityWord T d x
  have hlen : w.length = d := collatz_parity_word_length T d x
  have hmem : w ∈ allBoolWords d := by rw [← hlen]; exact mem_allBoolWords w
  have hok : isOnlyTrivialCycleWord w = true := List.all_eq_true.mp hchk w hmem
  have heq := collatz_cycle_equation d x hcyc
  have hcpos := collatz_positive_cycle_intercept_pos d x hd hx hcyc
  have hsub := (collatz_positive_cycle_subcritical d x hd hx hcyc).1
  have hD_eq : spineDenom w = (2 : Int) ^ d - (3 : Int) ^ (oddCount T d x) := by
    unfold spineDenom oddCount
    rw [hlen]
  have hD_pos : 0 < spineDenom w := by omega
  have hdiv : wordIntercept w % spineDenom w = 0 := by
    refine Int.emod_eq_zero_of_dvd ⟨x, ?_⟩
    rw [hD_eq]
    exact heq.symm
  have hDx : spineDenom w * x = wordIntercept w := by
    rw [hD_eq]; exact heq
  unfold isOnlyTrivialCycleWord at hok
  simp only [Bool.not_eq_true', decide_eq_false_iff_not] at hok
  by_cases h1 : wordIntercept w = spineDenom w
  · left
    have hmul : spineDenom w * (x - 1) = 0 := by rw [Int.mul_sub, Int.mul_one, hDx, h1]; omega
    rcases Int.mul_eq_zero.mp hmul with hDz | hx1
    · omega
    · omega
  · by_cases h2 : wordIntercept w = 2 * spineDenom w
    · right
      have hmul : spineDenom w * (x - 2) = 0 := by
        rw [Int.mul_sub, hDx, h2]
        have : spineDenom w * 2 = 2 * spineDenom w := Int.mul_comm _ _
        omega
      rcases Int.mul_eq_zero.mp hmul with hDz | hx2
      · omega
      · omega
    · exfalso
      exact hok ⟨hD_pos, hcpos, hdiv, h1, h2⟩

/-- **Exhaustive Low-Period Positive Cycle Classification (`1 ≤ d ≤ 7`):**
    Every positive integer `x > 0` satisfying `T^d(x) = x` for `1 ≤ d ≤ 7` lies on the
    trivial cycle `x ∈ {1, 2}` (pure kernel verification, zero `native_decide`). -/
public theorem collatz_no_nontrivial_positive_cycle_le_7 (d : Nat) (x : Int)
    (hd1 : 1 ≤ d) (hd7 : d ≤ 7) (hx : 0 < x) (hcyc : iter T d x = x) :
    x = 1 ∨ x = 2 := by
  have hd_cases : d = 1 ∨ d = 2 ∨ d = 3 ∨ d = 4 ∨ d = 5 ∨ d = 6 ∨ d = 7 := by omega
  rcases hd_cases with rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · exact absurd hcyc (collatz_no_positive_cycle_d1 x hx)
  · exact no_nontrivial_cycle_of_check 2 (by decide) (by decide) x hx hcyc
  · exact no_nontrivial_cycle_of_check 3 (by decide) (by decide) x hx hcyc
  · exact no_nontrivial_cycle_of_check 4 (by decide) (by decide) x hx hcyc
  · exact no_nontrivial_cycle_of_check 5 (by decide) (by decide) x hx hcyc
  · exact no_nontrivial_cycle_of_check 6 (by decide) (by decide) x hx hcyc
  · exact no_nontrivial_cycle_of_check 7 (by decide) (by decide) x hx hcyc

/-- **No Odd-Period Positive Collatz Cycles Through `d ≤ 7`:**
    No positive integer `x > 0` satisfies `T^d(x) = x` for any odd period `d ∈ {1, 3, 5, 7}`. -/
public theorem collatz_no_positive_cycle_odd_le_7 (d : Nat) (x : Int)
    (hd1 : 1 ≤ d) (hd7 : d ≤ 7) (hodd : d % 2 = 1) (hx : 0 < x) :
    iter T d x ≠ x := by
  intro hcyc
  have hk : d = 2 * (d / 2) + 1 := by omega
  have h12 := collatz_no_nontrivial_positive_cycle_le_7 d x hd1 hd7 hx hcyc
  have horb := collatz_trivial_cycle_orbit (d / 2)
  rcases h12 with rfl | rfl
  · rw [hk, horb.2.1] at hcyc; omega
  · rw [hk, horb.2.2.2] at hcyc; omega

-- ----------------------------------------------------------------------------
-- Catalytic Zero-Workspace Reversible Register Evaluation of Collatz Cylinder
-- ----------------------------------------------------------------------------

/-- **Catalytic Reversible Cylinder Theorem:**
    Starting from any accumulator `acc` and ANY arbitrary pre-filled catalyst register `cat`,
    the reversible register sequence `catCollatzStep d q r acc cat` cleanly adds
    `T^d(2^d q + r)` into `acc` while restoring `cat` identically (zero clean workspace). -/
public theorem collatz_catalytic_reversible_cylinder (d : Nat) (q r acc cat : Int) :
    catCollatzStep d q r acc cat = (acc + iter T d ((2 : Int) ^ d * q + r), cat) := by
  dsimp only [catCollatzStep]
  rw [collatz_cylinder_affine_law d q r]
  refine Prod.ext ?_ ?_ <;> omega


-- ----------------------------------------------------------------------------
-- v0.7.0 Unconditional 1-Odd-Step & 2-Odd-Step Positive Cycle Exclusion (All d ≥ 1)
-- ----------------------------------------------------------------------------

theorem wordIntercept_of_oddCount_one (w : List Bool) (ho : wordOddCount w = 1) :
    ∃ a : Nat, a < w.length ∧ wordIntercept w = (2 : Int) ^ a := by
  induction w with
  | nil => simp [wordOddCount] at ho
  | cons b ws ih =>
    cases b
    · simp only [wordOddCount, Bool.false_eq_true, ite_false, Nat.zero_add] at ho
      have ⟨a, ha_lt, ha_eq⟩ := ih ho
      refine ⟨a + 1, by simp; omega, ?_⟩
      simp only [wordIntercept, ha_eq]
      rw [Int.pow_succ, Int.mul_comm]
    · simp only [wordOddCount, ite_true] at ho
      have hws0 : wordOddCount ws = 0 := by omega
      have hcw0 : wordIntercept ws = 0 := wordIntercept_zero_of_oddCount_zero ws hws0
      refine ⟨0, by simp, ?_⟩
      simp only [wordIntercept, hws0, hcw0]
      rfl

theorem wordIntercept_of_oddCount_two (w : List Bool) (ho : wordOddCount w = 2) :
    ∃ a b : Nat, a < b ∧ b < w.length ∧
      wordIntercept w = 3 * (2 : Int) ^ a + (2 : Int) ^ b := by
  induction w with
  | nil => simp [wordOddCount] at ho
  | cons c ws ih =>
    cases c
    · simp only [wordOddCount, Bool.false_eq_true, ite_false, Nat.zero_add] at ho
      have ⟨a, b, hab, hblt, heq⟩ := ih ho
      refine ⟨a + 1, b + 1, by omega, by simp; omega, ?_⟩
      simp only [wordIntercept, heq]
      rw [Int.mul_add, Int.pow_succ, Int.pow_succ]
      omega
    · simp only [wordOddCount, ite_true] at ho
      have hws1 : wordOddCount ws = 1 := by omega
      have ⟨c0, hc0_lt, hc0_eq⟩ := wordIntercept_of_oddCount_one ws hws1
      refine ⟨0, c0 + 1, by omega, by simp; omega, ?_⟩
      simp only [wordIntercept, hws1, hc0_eq]
      rw [Int.pow_zero, Int.pow_one, Int.mul_one, Int.pow_succ, Int.mul_comm ((2 : Int) ^ c0) 2]

theorem odd_dvd_pow2_mul_nat (u : Nat) (hu_odd : u % 2 = 1) :
    ∀ a m : Nat, u ∣ 2 ^ a * m → u ∣ m := by
  intro a
  induction a with
  | zero => intro m h; simpa using h
  | succ a ih =>
    intro m ⟨k, hk⟩
    have hpow : 2 ^ (a + 1) * m = 2 * (2 ^ a * m) := by
      rw [Nat.pow_succ, Nat.mul_comm (2 ^ a) 2, Nat.mul_assoc]
    rw [hpow] at hk
    have hk_even : k % 2 = 0 := by
      by_cases hko : k % 2 = 1
      · have : (u * k) % 2 = 1 := by rw [Nat.mul_mod, hu_odd, hko]
        omega
      · omega
    have hk2 : k = 2 * (k / 2) := by omega
    have hcancel : 2 ^ a * m = u * (k / 2) := by
      have : 2 * (2 ^ a * m) = 2 * (u * (k / 2)) := by
        calc 2 * (2 ^ a * m) = u * k := hk
        _ = u * (2 * (k / 2)) := by rw [← hk2]
        _ = 2 * (u * (k / 2)) := by ac_rfl
      omega
    exact ih m ⟨k / 2, hcancel⟩

theorem pow2_nat_mono_collatz {a b : Nat} (h : a ≤ b) : 2 ^ a ≤ 2 ^ b := by
  induction b with
  | zero =>
    have ha0 : a = 0 := by omega
    subst ha0
    exact Nat.le_refl 1
  | succ k ih =>
    by_cases heq : a = k + 1
    · subst heq; exact Nat.le_refl _
    · have hrec := ih (by omega)
      rw [Nat.pow_succ]
      omega

theorem pow2_nat_ge_of_ge (d : Nat) (hd : 5 ≤ d) : 16 ≤ 2 ^ (d - 1) := by
  have : 2 ^ 4 ≤ 2 ^ (d - 1) := pow2_nat_mono_collatz (by omega)
  have h16 : 2 ^ 4 = 16 := rfl
  omega

/-- **Unconditional 1-Odd-Step Positive-Cycle Exclusion (all periods `d ≥ 1`):**
    The ONLY positive Collatz cycle with `oddCount T d x = 1` is the trivial cycle `1 ↔ 2` (`d = 2`). -/
public theorem collatz_positive_cycle_one_odd (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) (ho : oddCount T d x = 1) :
    d = 2 ∧ (x = 1 ∨ x = 2) := by
  have heq := collatz_cycle_equation d x hcyc
  have hsub := (collatz_positive_cycle_subcritical d x hd hx hcyc).1
  have hlen : (parityWord T d x).length = d := collatz_parity_word_length T d x
  have ⟨a, ha_lt, ha_eq⟩ := wordIntercept_of_oddCount_one (parityWord T d x) ho
  rw [hlen] at ha_lt
  rw [ho] at heq hsub
  rw [ha_eq] at heq
  have h31 : (3 : Int) ^ 1 = 3 := rfl
  rw [h31] at heq hsub
  -- Cast to Nat: (2^d - 3) * x.toNat = 2^a
  have hd_ge2 : 2 ≤ d := by
    by_cases hlt : d < 2
    · have hd1 : d = 1 := by omega
      subst hd1; simp at hsub
    · omega
  have hpow2_d : ((2 ^ d : Nat) : Int) = (2 : Int) ^ d := by simp
  have hpow2_a : ((2 ^ a : Nat) : Int) = (2 : Int) ^ a := by simp
  have h2d_ge4 : 4 ≤ 2 ^ d := by
    have : 2 ^ 2 ≤ 2 ^ d := pow2_nat_mono_collatz hd_ge2
    exact this
  let u : Nat := 2 ^ d - 3
  have hu_cast : (u : Int) = (2 : Int) ^ d - 3 := by dsimp only [u]; omega
  have hx_cast : (x.toNat : Int) = x := by omega
  have hnat_eq : u * x.toNat = 2 ^ a := by
    have hint : ((u * x.toNat : Nat) : Int) = ((2 ^ a : Nat) : Int) := by
      rw [Int.natCast_mul, hu_cast, hx_cast, hpow2_a, heq]
    exact Int.ofNat.inj hint
  have hu_odd : u % 2 = 1 := by
    have h2d_even : 2 ^ d % 2 = 0 := by
      have : 2 ^ d = 2 ^ (d - 1) * 2 := by
        calc 2 ^ d = 2 ^ ((d - 1) + 1) := by congr 1; omega
        _ = 2 ^ (d - 1) * 2 := Nat.pow_succ 2 (d - 1)
      rw [this]; omega
    dsimp only [u]; omega
  have hu_dvd1 : u ∣ 1 := odd_dvd_pow2_mul_nat u hu_odd a 1 (by
    rw [Nat.mul_one]; exact ⟨x.toNat, hnat_eq.symm⟩)
  have hu1 : u = 1 := Nat.eq_one_of_dvd_one hu_dvd1
  have h2d4 : 2 ^ d = 4 := by dsimp only [u] at hu1; omega
  have hd2 : d = 2 := by
    by_cases hge3 : 3 ≤ d
    · have : 2 ^ 3 ≤ 2 ^ d := pow2_nat_mono_collatz hge3
      have h8 : 2 ^ 3 = 8 := rfl
      omega
    · omega
  refine ⟨hd2, ?_⟩
  rw [hu1, Nat.one_mul] at hnat_eq
  have ha_lt2 : a < 2 := by omega
  by_cases ha0 : a = 0
  · left
    rw [ha0] at hnat_eq
    have h1 : (2 : Nat) ^ 0 = 1 := rfl
    rw [h1] at hnat_eq
    omega
  · right
    have ha1 : a = 1 := by omega
    rw [ha1] at hnat_eq
    have h2 : (2 : Nat) ^ 1 = 2 := rfl
    rw [h2] at hnat_eq
    omega

/-- **Unconditional 2-Odd-Step Positive-Cycle Exclusion (all periods `d ≥ 1`):**
    The ONLY positive Collatz cycle with `oddCount T d x = 2` is the twice-traversed trivial cycle
    `1 → 2 → 1 → 2 → 1` (`d = 4`, `x ∈ {1, 2}`). -/
public theorem collatz_positive_cycle_two_odd (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) (ho : oddCount T d x = 2) :
    d = 4 ∧ (x = 1 ∨ x = 2) := by
  have heq := collatz_cycle_equation d x hcyc
  have hsub := (collatz_positive_cycle_subcritical d x hd hx hcyc).1
  have hlen : (parityWord T d x).length = d := collatz_parity_word_length T d x
  have ⟨a, b, hab, hblt, hab_eq⟩ := wordIntercept_of_oddCount_two (parityWord T d x) ho
  rw [hlen] at hblt
  rw [ho] at heq hsub
  rw [hab_eq] at heq
  have h32 : (3 : Int) ^ 2 = 9 := rfl
  rw [h32] at heq hsub
  -- Deduce d ≥ 4 from 9 < 2^d
  have hd_ge4 : 4 ≤ d := by
    by_cases hlt : d < 4
    · have hle3 : 2 ^ d ≤ 2 ^ 3 := pow2_nat_mono_collatz (by omega)
      have h8 : 2 ^ 3 = 8 := rfl
      have hcast : ((2 ^ d : Nat) : Int) = (2 : Int) ^ d := by simp
      omega
    · omega
  have h2d_ge16 : 16 ≤ 2 ^ d := by
    have : 2 ^ 4 ≤ 2 ^ d := pow2_nat_mono_collatz hd_ge4
    exact this
  let u : Nat := 2 ^ d - 9
  let m : Nat := b - a
  have hm_ge1 : 1 ≤ m := by omega
  have hm_le : m ≤ d - 1 := by omega
  have hba : b = a + m := by omega
  have hpow2_d : ((2 ^ d : Nat) : Int) = (2 : Int) ^ d := by simp
  have hu_cast : (u : Int) = (2 : Int) ^ d - 9 := by dsimp only [u]; omega
  have hx_cast : (x.toNat : Int) = x := by omega
  have hnat_eq : u * x.toNat = 2 ^ a * (3 + 2 ^ m) := by
    have hint : ((u * x.toNat : Nat) : Int) = ((2 ^ a * (3 + 2 ^ m) : Nat) : Int) := by
      rw [Int.natCast_mul, hu_cast, hx_cast, heq]
      rw [hba, Int.pow_add]
      push_cast
      rw [Int.mul_add, Int.mul_comm ((2 : Int) ^ a) 3]
    exact Int.ofNat.inj hint
  have hu_odd : u % 2 = 1 := by
    have h2d_even : 2 ^ d % 2 = 0 := by
      have : 2 ^ d = 2 ^ (d - 1) * 2 := by
        calc 2 ^ d = 2 ^ ((d - 1) + 1) := by congr 1; omega
        _ = 2 ^ (d - 1) * 2 := Nat.pow_succ 2 (d - 1)
      rw [this]; omega
    dsimp only [u]; omega
  have hu_dvd : u ∣ 3 + 2 ^ m :=
    odd_dvd_pow2_mul_nat u hu_odd a (3 + 2 ^ m) ⟨x.toNat, hnat_eq.symm⟩
  have hpos_rhs : 0 < 3 + 2 ^ m := Nat.add_pos_left (by decide) (2 ^ m)
  have hu_le : u ≤ 3 + 2 ^ m := Nat.le_of_dvd hpos_rhs hu_dvd
  -- Rule out d ≥ 5: 2^d - 9 > 3 + 2^(d-1) ≥ 3 + 2^m
  have hd4 : d = 4 := by
    by_cases hge5 : 5 ≤ d
    · exfalso
      have h16 : 16 ≤ 2 ^ (d - 1) := pow2_nat_ge_of_ge d hge5
      have hm_pow : 2 ^ m ≤ 2 ^ (d - 1) := pow2_nat_mono_collatz hm_le
      have h2d_split : 2 ^ d = 2 ^ (d - 1) * 2 := by
        calc 2 ^ d = 2 ^ ((d - 1) + 1) := by congr 1; omega
        _ = 2 ^ (d - 1) * 2 := Nat.pow_succ 2 (d - 1)
      dsimp only [u] at hu_le
      omega
    · omega
  refine ⟨hd4, ?_⟩
  -- For d = 4: u = 7, m ∈ {1, 2, 3}, only m = 2 gives 7 ∣ (3 + 2^m)
  have hu7 : u = 7 := by dsimp only [u]; rw [hd4]
  rw [hu7] at hu_dvd hnat_eq
  have hm2 : m = 2 := by
    by_cases hm1 : m = 1
    · rw [hm1] at hu_dvd; have := Nat.mod_eq_zero_of_dvd hu_dvd; simp at this
    · by_cases hm2' : m = 2
      · exact hm2'
      · have hm3 : m = 3 := by omega
        rw [hm3] at hu_dvd; have := Nat.mod_eq_zero_of_dvd hu_dvd; simp at this
  rw [hm2] at hnat_eq
  have h7 : 3 + 2 ^ 2 = 7 := rfl
  rw [h7, Nat.mul_comm (2 ^ a) 7] at hnat_eq
  have hx_pow : x.toNat = 2 ^ a := Nat.eq_of_mul_eq_mul_left (by decide : 0 < 7) hnat_eq
  have ha_lt2 : a < 2 := by omega
  by_cases ha0 : a = 0
  · left
    rw [ha0] at hx_pow
    have h1 : (2 : Nat) ^ 0 = 1 := rfl
    rw [h1] at hx_pow
    omega
  · right
    have ha1 : a = 1 := by omega
    rw [ha1] at hx_pow
    have h2 : (2 : Nat) ^ 1 = 2 := rfl
    rw [h2] at hx_pow
    omega

-- ----------------------------------------------------------------------------
-- v0.9.0 Unconditional 3-Odd-Step Positive-Cycle Exclusion (All d ≥ 1),
-- Universal Intercept Upper Bound, and Global Eliahou–Steiner Amplitude Ceiling
-- ----------------------------------------------------------------------------

theorem wordOddCount_le_length (w : List Bool) : wordOddCount w ≤ w.length := by
  induction w with
  | nil => simp [wordOddCount]
  | cons b ws ih =>
    cases b <;> simp [wordOddCount] <;> omega

theorem wordIntercept_of_oddCount_three (w : List Bool) (ho : wordOddCount w = 3) :
    ∃ a b c : Nat, a < b ∧ b < c ∧ c < w.length ∧
      wordIntercept w = 9 * (2 : Int) ^ a + 3 * (2 : Int) ^ b + (2 : Int) ^ c := by
  induction w with
  | nil => simp [wordOddCount] at ho
  | cons bit ws ih =>
    cases bit
    · simp only [wordOddCount, Bool.false_eq_true, ite_false, Nat.zero_add] at ho
      have ⟨a, b, c, hab, hbc, hclt, heq⟩ := ih ho
      refine ⟨a + 1, b + 1, c + 1, by omega, by omega, by simp; omega, ?_⟩
      simp only [wordIntercept, heq]
      rw [Int.mul_add, Int.mul_add, Int.pow_succ, Int.pow_succ, Int.pow_succ]
      omega
    · simp only [wordOddCount, ite_true] at ho
      have hws2 : wordOddCount ws = 2 := by omega
      have ⟨b0, c0, hbc, hclt, heq⟩ := wordIntercept_of_oddCount_two ws hws2
      refine ⟨0, b0 + 1, c0 + 1, by omega, by omega, by simp; omega, ?_⟩
      simp only [wordIntercept, hws2, heq]
      have h32 : (3 : Int) ^ 2 = 9 := rfl
      rw [h32, Int.pow_zero, Int.mul_one, Int.mul_add, Int.pow_succ, Int.pow_succ]
      omega

theorem pow2_nat_ge_128_of_ge7 (d : Nat) (hd : 7 ≤ d) : 128 ≤ 2 ^ d := by
  have h := pow2_nat_mono_collatz hd
  have h128 : 2 ^ 7 = 128 := rfl
  omega

/-- **Unconditional 3-Odd-Step Positive-Cycle Exclusion (all periods `d ≥ 1`):**
    The ONLY positive Collatz cycle with `oddCount T d x = 3` is the thrice-traversed
    trivial cycle `1 ↔ 2` (`d = 6`, `x ∈ {1, 2}`). -/
public theorem collatz_positive_cycle_three_odd (d : Nat) (x : Int)
    (hd : 1 ≤ d) (hx : 0 < x) (hcyc : iter T d x = x) (ho : oddCount T d x = 3) :
    d = 6 ∧ (x = 1 ∨ x = 2) := by
  have heq := collatz_cycle_equation d x hcyc
  have hsub := (collatz_positive_cycle_subcritical d x hd hx hcyc).1
  have hlen : (parityWord T d x).length = d := collatz_parity_word_length T d x
  have ⟨a, b, c, hab, hbc, hclt, habc_eq⟩ := wordIntercept_of_oddCount_three (parityWord T d x) ho
  rw [hlen] at hclt
  rw [ho] at heq hsub
  rw [habc_eq] at heq
  have h33 : (3 : Int) ^ 3 = 27 := rfl
  rw [h33] at heq hsub
  -- Deduce d ≥ 5 from 27 < 2^d
  have hd_ge5 : 5 ≤ d := by
    by_cases hlt : d < 5
    · have hle4 : 2 ^ d ≤ 2 ^ 4 := pow2_nat_mono_collatz (by omega)
      have h16 : 2 ^ 4 = 16 := rfl
      have hcast : ((2 ^ d : Nat) : Int) = (2 : Int) ^ d := by simp
      omega
    · omega
  -- If d ≤ 7, apply our exhaustive kernel-checked d ≤ 7 classification
  by_cases hdle7 : d ≤ 7
  · have h12 := collatz_no_nontrivial_positive_cycle_le_7 d x hd hdle7 hx hcyc
    by_cases hd6 : d = 6
    · exact ⟨hd6, h12⟩
    · exfalso
      have hodd : d % 2 = 1 := by omega
      exact collatz_no_positive_cycle_odd_le_7 d x hd hdle7 hodd hx hcyc
  · -- For d ≥ 8 (in fact d ≥ 7): 9 + 3*2^m + 2^n < 2*(2^d - 27), forcing quotient = 1
    exfalso
    have hd_ge7 : 7 ≤ d := by omega
    have h2d_ge128 : 128 ≤ 2 ^ d := pow2_nat_ge_128_of_ge7 d hd_ge7
    let u : Nat := 2 ^ d - 27
    let m : Nat := b - a
    let n : Nat := c - a
    have hm_ge1 : 1 ≤ m := by omega
    have hmn : m < n := by omega
    have hn_le : n ≤ d - 1 := by omega
    have hm_le : m ≤ d - 2 := by omega
    have hba : b = a + m := by omega
    have hca : c = a + n := by omega
    have hpow2_d : ((2 ^ d : Nat) : Int) = (2 : Int) ^ d := by simp
    have hu_cast : (u : Int) = (2 : Int) ^ d - 27 := by dsimp only [u]; omega
    have hx_cast : (x.toNat : Int) = x := by omega
    have hnat_eq : u * x.toNat = 2 ^ a * (9 + 3 * 2 ^ m + 2 ^ n) := by
      have hint : ((u * x.toNat : Nat) : Int) =
          ((2 ^ a * (9 + 3 * 2 ^ m + 2 ^ n) : Nat) : Int) := by
        rw [Int.natCast_mul, hu_cast, hx_cast, heq, hba, hca, Int.pow_add, Int.pow_add]
        push_cast
        rw [Int.mul_add, Int.mul_add, Int.mul_comm ((2 : Int) ^ a) 9]
        have hmid : (3 : Int) * ((2 : Int) ^ a * (2 : Int) ^ m) =
            (2 : Int) ^ a * (3 * (2 : Int) ^ m) := by
          rw [← Int.mul_assoc, Int.mul_comm 3 ((2 : Int) ^ a), Int.mul_assoc]
        rw [hmid]
      exact Int.ofNat.inj hint
    have hu_odd : u % 2 = 1 := by
      have h2d_even : 2 ^ d % 2 = 0 := by
        have : 2 ^ d = 2 ^ (d - 1) * 2 := by
          calc 2 ^ d = 2 ^ ((d - 1) + 1) := by congr 1; omega
          _ = 2 ^ (d - 1) * 2 := Nat.pow_succ 2 (d - 1)
        rw [this]; omega
      dsimp only [u]; omega
    have hu_dvd : u ∣ 9 + 3 * 2 ^ m + 2 ^ n :=
      odd_dvd_pow2_mul_nat u hu_odd a (9 + 3 * 2 ^ m + 2 ^ n) ⟨x.toNat, hnat_eq.symm⟩
    have ⟨q, hq⟩ := hu_dvd
    have hq_pos : 1 ≤ q := by
      by_cases hq0 : q = 0
      · rw [hq0, Nat.mul_zero] at hq
        have h9 : 9 ≤ 9 + 3 * 2 ^ m + 2 ^ n :=
          Nat.le_trans (Nat.le_add_right 9 _) (Nat.le_add_right _ _)
        omega
      · omega
    -- Show 9 + 3*2^m + 2^n < 2*u, so q = 1
    have h2d_split : 2 ^ d = 4 * 2 ^ (d - 2) := by
      have h1 : d = (d - 2) + 2 := by omega
      calc 2 ^ d = 2 ^ ((d - 2) + 2) := by rw [← h1]
      _ = 2 ^ (d - 2) * 2 ^ 2 := Nat.pow_add 2 (d - 2) 2
      _ = 4 * 2 ^ (d - 2) := by rw [Nat.mul_comm]
    have h2n_le : 2 ^ n ≤ 2 * 2 ^ (d - 2) := by
      have h1 : 2 ^ n ≤ 2 ^ (d - 1) := pow2_nat_mono_collatz hn_le
      have h2 : 2 ^ (d - 1) = 2 * 2 ^ (d - 2) := by
        have : d - 1 = (d - 2) + 1 := by omega
        rw [this, Nat.pow_succ, Nat.mul_comm]
      omega
    have h2m_le : 2 ^ m ≤ 2 ^ (d - 2) := pow2_nat_mono_collatz hm_le
    have hrhs_lt_2u : 9 + 3 * 2 ^ m + 2 ^ n < 2 * u := by
      dsimp only [u]; omega
    have hq1 : q = 1 := by
      by_cases hq2 : 2 ≤ q
      · have hge : u * 2 ≤ u * q := Nat.mul_le_mul_left u hq2
        omega
      · omega
    rw [hq1, Nat.mul_one] at hq
    -- Exact equation: 2^d = 36 + 3*2^m + 2^n (with d ≥ 7 => 8 ∣ 2^d)
    have hsum : 2 ^ d = 36 + 3 * 2 ^ m + 2 ^ n := by dsimp only [u] at hq; omega
    have h2d_mod8 : 2 ^ d % 8 = 0 := by
      have h1 : d = (d - 3) + 3 := by omega
      have h2 : 2 ^ d = 2 ^ (d - 3) * 8 := by
        calc 2 ^ d = 2 ^ ((d - 3) + 3) := by rw [← h1]
        _ = 2 ^ (d - 3) * 2 ^ 3 := Nat.pow_add 2 (d - 3) 3
      rw [h2]; omega
    -- Case split on m: m = 1, m = 2, or m ≥ 3
    by_cases hm1 : m = 1
    · -- m = 1 => 2^d = 42 + 2^n, n ≥ 2 => 4 ∣ 2^d and 4 ∣ 2^n, contradiction with 42 % 4 = 2
      have h2n_mod4 : 2 ^ n % 4 = 0 := by
        have h1 : n = (n - 2) + 2 := by omega
        have h2 : 2 ^ n = 2 ^ (n - 2) * 4 := by
          calc 2 ^ n = 2 ^ ((n - 2) + 2) := by rw [← h1]
          _ = 2 ^ (n - 2) * 2 ^ 2 := Nat.pow_add 2 (n - 2) 2
        rw [h2]; omega
      rw [hm1] at hsum
      have h21 : 2 ^ 1 = 2 := rfl
      rw [h21] at hsum
      omega
    · by_cases hm2 : m = 2
      · -- m = 2 => 2^d = 48 + 2^n => 2^n * (2^(d-n) - 1) = 48 = 16 * 3
        rw [hm2] at hsum
        have h22 : 2 ^ 2 = 4 := rfl
        rw [h22] at hsum
        -- Since n ≥ 3: if n = 3 => 2^d = 56 (not pow2); if n = 4 => 2^d = 64 < 128; if n ≥ 5 => 32 ∣ 2^d, 32 ∣ 2^n, 32 ∤ 48!
        by_cases hn3 : n = 3
        · rw [hn3] at hsum; have h8 : 2 ^ 3 = 8 := rfl; rw [h8] at hsum; omega
        · by_cases hn4 : n = 4
          · rw [hn4] at hsum; have h16 : 2 ^ 4 = 16 := rfl; rw [h16] at hsum; omega
          · have hn5 : 5 ≤ n := by omega
            have h2d_mod32 : 2 ^ d % 32 = 0 := by
              have h1 : d = (d - 5) + 5 := by omega
              have h2 : 2 ^ d = 2 ^ (d - 5) * 32 := by
                calc 2 ^ d = 2 ^ ((d - 5) + 5) := by rw [← h1]
                _ = 2 ^ (d - 5) * 2 ^ 5 := Nat.pow_add 2 (d - 5) 5
              rw [h2]; omega
            have h2n_mod32 : 2 ^ n % 32 = 0 := by
              have h1 : n = (n - 5) + 5 := by omega
              have h2 : 2 ^ n = 2 ^ (n - 5) * 32 := by
                calc 2 ^ n = 2 ^ ((n - 5) + 5) := by rw [← h1]
                _ = 2 ^ (n - 5) * 2 ^ 5 := Nat.pow_add 2 (n - 5) 5
              rw [h2]; omega
            omega
      · -- m ≥ 3 => n ≥ 4 => 8 ∣ 2^m and 8 ∣ 2^n and 8 ∣ 2^d, contradicting 36 % 8 = 4
        have hm3 : 3 ≤ m := by omega
        have hn4 : 4 ≤ n := by omega
        have h2m_mod8 : 2 ^ m % 8 = 0 := by
          have h1 : m = (m - 3) + 3 := by omega
          have h2 : 2 ^ m = 2 ^ (m - 3) * 8 := by
            calc 2 ^ m = 2 ^ ((m - 3) + 3) := by rw [← h1]
            _ = 2 ^ (m - 3) * 2 ^ 3 := Nat.pow_add 2 (m - 3) 3
          rw [h2]; omega
        have h2n_mod8 : 2 ^ n % 8 = 0 := by
          have h1 : n = (n - 3) + 3 := by omega
          have h2 : 2 ^ n = 2 ^ (n - 3) * 8 := by
            calc 2 ^ n = 2 ^ ((n - 3) + 3) := by rw [← h1]
            _ = 2 ^ (n - 3) * 2 ^ 3 := Nat.pow_add 2 (n - 3) 3
          rw [h2]; omega
        omega

/-- **Universal Affine Intercept Upper Bound (Sharp):**
    For EVERY parity word `w` of length `d` and odd-step count `o = wordOddCount w`,
    `wordIntercept w ≤ 2^(d - o) · (3^o - 2^o)` (attained on `false^(d - o) ++ true^o`). -/
public theorem collatz_intercept_upper_bound (w : List Bool) :
    wordIntercept w ≤ (2 : Int) ^ (w.length - wordOddCount w) *
      ((3 : Int) ^ (wordOddCount w) - (2 : Int) ^ (wordOddCount w)) := by
  induction w with
  | nil => simp [wordIntercept, wordOddCount]
  | cons b ws ih =>
    have hle : wordOddCount ws ≤ ws.length := wordOddCount_le_length ws
    cases b
    · simp only [wordIntercept, List.length_cons, wordOddCount, Bool.false_eq_true, ite_false,
        Nat.zero_add]
      have hsub : ws.length + 1 - wordOddCount ws = (ws.length - wordOddCount ws) + 1 := by omega
      rw [hsub, Int.pow_succ, Int.mul_comm ((2 : Int) ^ _) 2, Int.mul_assoc]
      omega
    · simp only [wordIntercept, List.length_cons, wordOddCount, ite_true]
      have hsub : ws.length + 1 - (1 + wordOddCount ws) = ws.length - wordOddCount ws := by omega
      rw [hsub, Nat.add_comm 1 (wordOddCount ws), Int.pow_succ, Int.pow_succ]
      let e : Int := (2 : Int) ^ (ws.length - wordOddCount ws)
      have he_ge1 : (1 : Int) ≤ e := pow2_pos (ws.length - wordOddCount ws)
      have h3pos : (1 : Int) ≤ (3 : Int) ^ wordOddCount ws := pow3_pos (wordOddCount ws)
      have h1 : (3 : Int) ^ wordOddCount ws ≤ e * (3 : Int) ^ wordOddCount ws := by
        have := Int.mul_le_mul_of_nonneg_right he_ge1 (by omega : (0 : Int) ≤ (3 : Int) ^ wordOddCount ws)
        simpa using this
      have hsplit : e * ((3 : Int) ^ wordOddCount ws * 3 - (2 : Int) ^ wordOddCount ws * 2) =
          e * (3 : Int) ^ wordOddCount ws +
          2 * (e * ((3 : Int) ^ wordOddCount ws - (2 : Int) ^ wordOddCount ws)) := by
        rw [Int.mul_sub, Int.mul_sub]
        have ha : e * ((3 : Int) ^ wordOddCount ws * 3) =
            e * (3 : Int) ^ wordOddCount ws + 2 * (e * (3 : Int) ^ wordOddCount ws) := by
          rw [← Int.mul_assoc, Int.mul_comm (e * (3 : Int) ^ wordOddCount ws) 3]; omega
        have hb : e * ((2 : Int) ^ wordOddCount ws * 2) =
            2 * (e * (2 : Int) ^ wordOddCount ws) := by
          rw [← Int.mul_assoc, Int.mul_comm (e * (2 : Int) ^ wordOddCount ws) 2]
        rw [ha, hb]; omega
      change (3 : Int) ^ wordOddCount ws + 2 * wordIntercept ws ≤
        e * ((3 : Int) ^ wordOddCount ws * 3 - (2 : Int) ^ wordOddCount ws * 2)
      rw [hsplit]
      change wordIntercept ws ≤ e * ((3 : Int) ^ wordOddCount ws - (2 : Int) ^ wordOddCount ws) at ih
      omega

/-- **Global Positive-Cycle Amplitude Ceiling (Eliahou–Steiner Diophantine Bound):**
    Every positive integer `x > 0` lying on a Collatz cycle `T^d(x) = x` (`d ≥ 1`) satisfies
    `(2^d - 3^o) · x ≤ 2^(d - o) · (3^o - 2^o)`, linking any computational convergence floor
    `x ≥ M` directly to the linear form `2^d - 3^o`. -/
public theorem collatz_cycle_amplitude_ceiling (d : Nat) (x : Int)
    (_hd : 1 ≤ d) (_hx : 0 < x) (hcyc : iter T d x = x) :
    let o := oddCount T d x
    ((2 : Int) ^ d - (3 : Int) ^ o) * x ≤
      (2 : Int) ^ (d - o) * ((3 : Int) ^ o - (2 : Int) ^ o) := by
  intro o
  have heq := collatz_cycle_equation d x hcyc
  have hub := collatz_intercept_upper_bound (parityWord T d x)
  have hlen : (parityWord T d x).length = d := collatz_parity_word_length T d x
  rw [hlen] at hub
  change ((2 : Int) ^ d - (3 : Int) ^ o) * x = wordIntercept (parityWord T d x) at heq
  rw [heq]
  exact hub

end FormalAtlas
