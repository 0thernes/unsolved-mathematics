module

public import FormalAtlas.Defs

/-!
# FormalAtlas.Collatz — Machine-Checked Structural Core & Obstructions

Proves the foundational structural theorems and no-go barriers of the Collatz
research program in pure Lean 4 (zero Mathlib, zero `sorry`, standard axioms only):
  1. `collatz_cylinder_affine_law` — `T^d(2^d q + r) = 3^o q + T^d(r)`
  2. `collatz_exact_intercept_law` — `2^d T^d(x) = 3^o x + c(w)`
  3. `terras_parity_word_bijection` — Terras (1976) injectivity & surjectivity mod `2^d`
  4. `collatz_descent_certificate_sound` — exact descent certificate criterion
  5. `collatz_no_finite_subcritical_cover` — all-ones fixed point `-1` obstruction
  6. `collatz_spine_ladder_identity` — cleared-denominator Spine Ladder linearization
  7. `collatz_positivity_localization` — every supercritical periodic spine satisfies `ρ_w ≤ -1`
     (exact integer form: `wordIntercept w ≥ 3^(wordOddCount w) - 2^(w.length)`)
  8. `collatz_epsilon_invariance_barrier` — sibling `3n-1` has identical Terras bijection
     yet possesses genuine positive supercritical cycles at `5` and `17`.

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
-- Theorem 8: ε-Invariance / Sign-Blindness Barrier (Sibling 3n-1)
-- ----------------------------------------------------------------------------

/-- **Theorem 8 (ε-Invariance / Sign-Blindness Barrier).** -/
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

end FormalAtlas
