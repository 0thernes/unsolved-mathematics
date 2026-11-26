module

-- SPDX-License-Identifier: MIT
public import FormalAtlas.Primes

/-!
# FormalAtlas.PerfectNumbers — Mersenne Primes, Euclid Even-Perfect Theorem & Odd-Perfect Exclusion

Proves four structural theorems for the Odd Perfect Numbers (Rank #8) and
Mersenne Primes Infinitude (Rank #9) open problems in pure Lean 4 Core:
  1. `mersenne_exponent_prime`: If `2^n - 1` is prime (`n ≥ 2`), then `n` is prime.
  2. `perfect_numbers_first_four`: `6`, `28`, `496`, and `8128` are all perfect (`σ(n) = 2n`).
  3. `no_odd_perfect_le_100`: No odd integer `n ≤ 100` is perfect.
  4. `euclid_even_perfect`: **Euclid's Even Perfect Number Theorem (Elements IX.36)** —
     for EVERY `p ≥ 2`, if `2^p - 1` is prime, then `2^(p-1) * (2^p - 1)` is perfect
     (proved directly against `divSum`/`IsPerfect` via unconditional exactness of `isqrt`).

Explicit non-claim: proves NO resolution of Odd Perfect Numbers or Mersenne Infinitude (both OPEN).
-/

namespace FormalAtlas

theorem pow2_nat_pos (n : Nat) : 1 ≤ 2 ^ n := by
  induction n with
  | zero => decide
  | succ k ih =>
    have : 2 ^ (k + 1) = 2 ^ k * 2 := Nat.pow_succ 2 k
    omega

theorem pow2_strictMono {a b : Nat} (h : a < b) : 2 ^ a < 2 ^ b := by
  induction b with
  | zero => omega
  | succ k ih =>
    rw [Nat.pow_succ]
    by_cases heq : a = k
    · subst heq
      have := pow2_nat_pos a
      omega
    · have hlt := ih (by omega)
      omega

theorem pow2_sub_one_dvd (a b : Nat) : (2 ^ a - 1) ∣ (2 ^ (a * b) - 1) := by
  induction b with
  | zero =>
    simp only [Nat.mul_zero, Nat.pow_zero, Nat.sub_self]
    exact Nat.dvd_zero _
  | succ k ih =>
    have hmul : a * (k + 1) = a * k + a := Nat.mul_succ a k
    rw [hmul, Nat.pow_add]
    have hp1 : 1 ≤ 2 ^ (a * k) := pow2_nat_pos (a * k)
    have hp2 : 1 ≤ 2 ^ a := pow2_nat_pos a
    have hsplit : 2 ^ (a * k) * 2 ^ a - 1 =
        2 ^ (a * k) * (2 ^ a - 1) + (2 ^ (a * k) - 1) := by
      have hdist : 2 ^ (a * k) * (2 ^ a - 1) + 2 ^ (a * k) = 2 ^ (a * k) * 2 ^ a := by
        calc 2 ^ (a * k) * (2 ^ a - 1) + 2 ^ (a * k)
            = 2 ^ (a * k) * (2 ^ a - 1) + 2 ^ (a * k) * 1 := by rw [Nat.mul_one]
        _   = 2 ^ (a * k) * ((2 ^ a - 1) + 1) := by rw [← Nat.mul_add]
        _   = 2 ^ (a * k) * 2 ^ a := by
              have : (2 ^ a - 1) + 1 = 2 ^ a := by omega
              rw [this]
      omega
    rw [hsplit]
    exact Nat.dvd_add (Nat.dvd_mul_left (2 ^ a - 1) (2 ^ (a * k))) ih

/-- **Mersenne Prime Exponent Necessity:** if `2^n - 1` is prime (`n ≥ 2`), then `n` is prime. -/
public theorem mersenne_exponent_prime (n : Nat) (hn : 2 ≤ n) (hm : IsPrime (2 ^ n - 1)) :
    IsPrime n := by
  refine ⟨hn, ?_⟩
  intro a ha
  have ⟨b, hnb⟩ := ha
  have hdvd : (2 ^ a - 1) ∣ (2 ^ n - 1) := by
    rw [hnb]
    exact pow2_sub_one_dvd a b
  have hcases := hm.2 (2 ^ a - 1) hdvd
  rcases hcases with h1 | hfull
  · left
    by_cases ha0 : a = 0
    · subst ha0; simp at h1
    · by_cases ha1 : a = 1
      · exact ha1
      · have hgt : 2 ^ 1 < 2 ^ a := pow2_strictMono (by omega)
        have : 2 ^ 1 = 2 := rfl
        omega
  · right
    have hpa : 1 ≤ 2 ^ a := pow2_nat_pos a
    have hpn : 1 ≤ 2 ^ n := pow2_nat_pos n
    have heq : 2 ^ a = 2 ^ n := by omega
    by_cases hlt : a < n
    · have := pow2_strictMono hlt; omega
    · by_cases hgt : n < a
      · have := pow2_strictMono hgt; omega
      · omega

/-- **First Four Even Perfect Numbers:** `6`, `28`, `496`, and `8128` all satisfy `σ(n) = 2n`. -/
public theorem perfect_numbers_first_four :
    IsPerfect 6 ∧ IsPerfect 28 ∧ IsPerfect 496 ∧ IsPerfect 8128 := by
  unfold IsPerfect
  exact ⟨⟨by decide, by decide⟩, ⟨by decide, by decide⟩, ⟨by decide, by decide⟩, ⟨by decide, by decide⟩⟩

theorem no_odd_perfect_fin50 : ∀ k : Fin 50, divSum (2 * k.val + 1) ≠ 2 * (2 * k.val + 1) := by
  decide

/-- **Finite Odd Perfect Exclusion (`n ≤ 100`):** no odd integer `n ≤ 100` is perfect. -/
public theorem no_odd_perfect_le_100 (n : Nat) (hle : n ≤ 100) (hodd : n % 2 = 1) :
    ¬ IsPerfect n := by
  intro ⟨_, hsig⟩
  have hk : n / 2 < 50 := by omega
  have hne := no_odd_perfect_fin50 ⟨n / 2, hk⟩
  have heq : 2 * (n / 2) + 1 = n := by omega
  rw [heq] at hne
  exact hne hsig

-- ============================================================================
-- Euclid's Even Perfect Number Theorem (Elements IX.36) — ALL p ≥ 2
-- ============================================================================

theorem nat_le_pow2 (n : Nat) : n ≤ 2 ^ n := by
  induction n with
  | zero => decide
  | succ k ih =>
    have hpos : 1 ≤ 2 ^ k := pow2_nat_pos k
    rw [Nat.pow_succ]
    omega

theorem isqrtAux_spec (n fuel : Nat) :
    ∀ lo hi : Nat, lo * lo ≤ n → n < hi * hi → lo < hi → hi - lo ≤ 2 ^ fuel →
      let r := isqrtAux n lo hi fuel
      r * r ≤ n ∧ n < (r + 1) * (r + 1) := by
  induction fuel with
  | zero =>
    intro lo hi hlo hhi hlt hspan
    have heq : hi = lo + 1 := by
      have : 2 ^ 0 = 1 := rfl
      omega
    subst heq
    exact ⟨hlo, hhi⟩
  | succ f ih =>
    intro lo hi hlo hhi hlt hspan
    simp only [isqrtAux]
    split
    · have heq : hi = lo + 1 := by omega
      subst heq
      exact ⟨hlo, hhi⟩
    · have hpow : 2 ^ (f + 1) = 2 ^ f * 2 := Nat.pow_succ 2 f
      have hmid_gt : lo < (lo + hi) / 2 := by omega
      have hmid_lt : (lo + hi) / 2 < hi := by omega
      split
      · rename_i hle
        exact ih ((lo + hi) / 2) hi hle hhi hmid_lt (by omega)
      · rename_i hgt
        exact ih lo ((lo + hi) / 2) hlo (by omega) hmid_gt (by omega)

/-- Unconditional exactness of `isqrt n` for EVERY `n : Nat`. -/
theorem isqrt_spec (n : Nat) :
    isqrt n * isqrt n ≤ n ∧ n < (isqrt n + 1) * (isqrt n + 1) := by
  cases n with
  | zero => unfold isqrt; decide
  | succ m =>
    unfold isqrt
    have hne : ((m + 1 == 0) : Bool) = false := rfl
    simp only [hne, Bool.false_eq_true, ite_false]
    have h1 : 1 * 1 ≤ m + 1 := by omega
    have h2 : m + 1 < (m + 2) * (m + 2) := by
      have hmul : 1 * (m + 2) ≤ (m + 2) * (m + 2) := Nat.mul_le_mul_right (m + 2) (by omega)
      omega
    exact isqrtAux_spec (m + 1) (m + 1) 1 (m + 2) h1 h2 (by omega) (by
      have := nat_le_pow2 (m + 1); omega)

theorem nat_strong_ind_pn {P : Nat → Prop} (step : ∀ n, (∀ m, m < n → P m) → P n) : ∀ n, P n := by
  have hall : ∀ k m, m < k → P m := by
    intro k
    induction k with
    | zero => intro m hm; omega
    | succ k ih =>
      intro m hm
      exact step m (fun j hj => ih j (by omega))
  intro n
  exact hall (n + 1) n (by omega)

theorem nat_bezout_pn (a b : Nat) :
    ∃ x y : Int, (a : Int) * x + (b : Int) * y = (Nat.gcd a b : Int) := by
  have hmain : ∀ b a : Nat, ∃ x y : Int, (a : Int) * x + (b : Int) * y = (Nat.gcd a b : Int) := by
    apply nat_strong_ind_pn (P := fun b => ∀ a : Nat, ∃ x y : Int, (a : Int) * x + (b : Int) * y = (Nat.gcd a b : Int))
    intro b ih a
    by_cases hb : b = 0
    · subst hb; refine ⟨1, 0, ?_⟩; simp [Nat.gcd_zero_right]
    · have hlt : a % b < b := Nat.mod_lt a (Nat.pos_of_ne_zero hb)
      have ⟨x', y', hxy⟩ := ih (a % b) hlt b
      have hgcd : Nat.gcd b (a % b) = Nat.gcd a b := by
        rw [Nat.gcd_comm b (a % b), ← Nat.gcd_rec b a, Nat.gcd_comm]
      rw [hgcd] at hxy
      have hdiv : a = b * (a / b) + a % b := (Nat.div_add_mod a b).symm
      have hmod_int : ((a % b : Nat) : Int) = (a : Int) - (b : Int) * ((a / b : Nat) : Int) := by
        omega
      refine ⟨y', x' - ((a / b : Nat) : Int) * y', ?_⟩
      rw [hmod_int] at hxy
      have hexp : (a : Int) * y' + (b : Int) * (x' - ((a / b : Nat) : Int) * y') =
          (b : Int) * x' + ((a : Int) - (b : Int) * ((a / b : Nat) : Int)) * y' := by
        rw [Int.mul_sub, Int.sub_mul, ← Int.mul_assoc]; omega
      rw [hexp, hxy]
  exact hmain b a

/-- Euclid's coprime divisibility lemma: `d ∣ a * b` and `gcd d b = 1` implies `d ∣ a`. -/
theorem dvd_left_of_dvd_mul_coprime {d a b : Nat} (hdvd : d ∣ a * b) (hcop : Nat.gcd d b = 1) :
    d ∣ a := by
  have ⟨x, y, hxy⟩ := nat_bezout_pn d b
  rw [hcop] at hxy
  have hxy1 : (d : Int) * x + (b : Int) * y = 1 := hxy
  have ⟨k, hk⟩ := hdvd
  have hint : (a : Int) = (d : Int) * ((a : Int) * x + (k : Int) * y) := by
    have hab : (a : Int) * (b : Int) = (d : Int) * (k : Int) := by
      rw [← Int.natCast_mul, ← Int.natCast_mul, hk]
    calc (a : Int)
        = (a : Int) * 1 := (Int.mul_one _).symm
    _   = (a : Int) * ((d : Int) * x + (b : Int) * y) := by rw [← hxy1]
    _   = (d : Int) * ((a : Int) * x) + ((a : Int) * (b : Int)) * y := by
          rw [Int.mul_add, Int.mul_left_comm (a : Int) (d : Int) x, Int.mul_assoc (a : Int) (b : Int) y]
    _   = (d : Int) * ((a : Int) * x) + ((d : Int) * (k : Int)) * y := by rw [hab]
    _   = (d : Int) * ((a : Int) * x + (k : Int) * y) := by
          rw [Int.mul_assoc (d : Int) (k : Int) y, ← Int.mul_add]
  have hmod0 : ((a % d : Nat) : Int) = 0 := by
    have h1 : ((a % d : Nat) : Int) = (a : Int) % (d : Int) := rfl
    rw [h1, hint, Int.mul_emod_right]
  have hnat0 : a % d = 0 := by omega
  exact Nat.dvd_of_mod_eq_zero hnat0

/-- Every positive divisor of `2 ^ k` is `2 ^ j` for some `j ≤ k`. -/
theorem dvd_pow2_eq_pow2 : ∀ k d : Nat, d ∣ 2 ^ k → ∃ j : Nat, j ≤ k ∧ d = 2 ^ j := by
  intro k
  induction k with
  | zero =>
    intro d hd
    have hd1 : d = 1 := Nat.eq_one_of_dvd_one hd
    exact ⟨0, by omega, hd1⟩
  | succ k ih =>
    intro d hd
    by_cases hodd : d % 2 = 1
    · have hcop : Nat.gcd d 2 = 1 := by
        have h2 : Nat.gcd d 2 ∣ 2 := Nat.gcd_dvd_right d 2
        have hd_g : Nat.gcd d 2 ∣ d := Nat.gcd_dvd_left d 2
        have hpos : 0 < Nat.gcd d 2 := Nat.gcd_pos_of_pos_right d (by decide)
        have hle : Nat.gcd d 2 ≤ 2 := Nat.le_of_dvd (by decide) h2
        by_cases h2eq : Nat.gcd d 2 = 2
        · rw [h2eq] at hd_g
          have ⟨t, ht⟩ := hd_g
          omega
        · omega
      rw [Nat.pow_succ] at hd
      have hd_k : d ∣ 2 ^ k := dvd_left_of_dvd_mul_coprime hd hcop
      have ⟨j, hjle, hdj⟩ := ih d hd_k
      exact ⟨j, by omega, hdj⟩
    · have heven : d = 2 * (d / 2) := by omega
      rw [heven, Nat.pow_succ, Nat.mul_comm (2 ^ k) 2] at hd
      have hd' : d / 2 ∣ 2 ^ k := (Nat.mul_dvd_mul_iff_left (by decide : 0 < 2)).mp hd
      have ⟨j, hjle, hdj⟩ := ih (d / 2) hd'
      refine ⟨j + 1, by omega, ?_⟩
      rw [Nat.pow_succ, Nat.mul_comm (2 ^ j) 2, ← hdj]
      exact heven

/-- Skipping a range `(a, b]` with zero divisors leaves `divSumPairs` unchanged. -/
theorem divSumPairs_skip (n a b : Nat) (hab : a ≤ b)
    (hnone : ∀ m : Nat, a < m → m ≤ b → n % m ≠ 0) :
    divSumPairs n b = divSumPairs n a := by
  induction b with
  | zero =>
    have ha0 : a = 0 := by omega
    subst ha0; rfl
  | succ k ih =>
    by_cases hle : a ≤ k
    · have hne : n % (k + 1) ≠ 0 := hnone (k + 1) (by omega) (by omega)
      have hbeq : (n % (k + 1) == 0) = false := by
        cases h : (n % (k + 1) == 0)
        · rfl
        · exact False.elim (hne (beq_iff_eq.mp h))
      simp only [divSumPairs, hbeq, Bool.false_eq_true, ite_false, Nat.zero_add]
      exact ih hle (fun m hm1 hm2 => hnone m hm1 (by omega))
    · have ha_eq : a = k + 1 := by omega
      subst ha_eq; rfl

/-- **Euclid's Even Perfect Number Theorem (Elements IX.36):**
    For EVERY `p ≥ 2`, if `2^p - 1` is prime, then `2^(p-1) * (2^p - 1)` is perfect (`σ(N) = 2N`). -/
public theorem euclid_even_perfect (p : Nat) (hp : 2 ≤ p) (hmp : IsPrime (2 ^ p - 1)) :
    IsPerfect (2 ^ (p - 1) * (2 ^ p - 1)) := by
  let q := 2 ^ p - 1
  let N := 2 ^ (p - 1) * q
  have h2p_eq : 2 ^ p = 2 ^ (p - 1) * 2 := by
    calc 2 ^ p = 2 ^ ((p - 1) + 1) := by congr 1; omega
    _ = 2 ^ (p - 1) * 2 := Nat.pow_succ 2 (p - 1)
  have hp1_pos : 1 ≤ 2 ^ (p - 1) := pow2_nat_pos (p - 1)
  have hp1_ge2 : 2 ≤ 2 ^ (p - 1) := by
    have : 2 ^ 1 ≤ 2 ^ (p - 1) := by
      by_cases heq : p - 1 = 1
      · rw [heq]; exact Nat.le_refl _
      · exact Nat.le_of_lt (pow2_strictMono (by omega))
    exact this
  have hq_gt_half : 2 ^ (p - 1) < q := by dsimp only [q]; omega
  have hN_pos : 0 < N := Nat.mul_pos (by omega) (by omega)
  -- Exact characterization of every divisor m of N with 1 ≤ m < q: m = 2^j with j ≤ p - 1
  have hdvd_lt_q : ∀ m : Nat, 1 ≤ m → m < q → N % m = 0 →
      ∃ j : Nat, j ≤ p - 1 ∧ m = 2 ^ j := by
    intro m hm1 hmq hmod0
    have hmdvd : m ∣ 2 ^ (p - 1) * q := Nat.dvd_of_mod_eq_zero hmod0
    have hcop : Nat.gcd m q = 1 := by
      have hg_q : Nat.gcd m q ∣ q := Nat.gcd_dvd_right m q
      have hg_m : Nat.gcd m q ∣ m := Nat.gcd_dvd_left m q
      rcases hmp.2 (Nat.gcd m q) hg_q with h1 | hfull
      · exact h1
      · have hfull' : Nat.gcd m q = q := hfull
        have hle : q ≤ m := by rw [← hfull']; exact Nat.le_of_dvd (by omega) hg_m
        omega
    have hm_pow : m ∣ 2 ^ (p - 1) := dvd_left_of_dvd_mul_coprime hmdvd hcop
    exact dvd_pow2_eq_pow2 (p - 1) m hm_pow
  -- Bound isqrt N strictly between 2^(p-1) and q
  have ⟨hsq_lo, hsq_hi⟩ := isqrt_spec N
  have hsq_ge : 2 ^ (p - 1) ≤ isqrt N := by
    by_cases hlt : isqrt N < 2 ^ (p - 1)
    · have hle : isqrt N + 1 ≤ 2 ^ (p - 1) := by omega
      have hsq : (isqrt N + 1) * (isqrt N + 1) ≤ 2 ^ (p - 1) * 2 ^ (p - 1) :=
        Nat.mul_le_mul hle hle
      have hltN : 2 ^ (p - 1) * 2 ^ (p - 1) < N :=
        Nat.mul_lt_mul_of_pos_left hq_gt_half (by omega)
      omega
    · omega
  have hsq_lt_q : isqrt N < q := by
    by_cases hge : q ≤ isqrt N
    · have hsq : q * q ≤ isqrt N * isqrt N := Nat.mul_le_mul hge hge
      have hNlt : N < q * q := Nat.mul_lt_mul_of_pos_right hq_gt_half (by omega)
      omega
    · omega
  -- Step 1: No divisors in (2^(p-1), isqrt N], so divSum N = divSumPairs N (2^(p-1))
  have hdrop_top : divSum N = divSumPairs N (2 ^ (p - 1)) := by
    unfold divSum
    apply divSumPairs_skip N (2 ^ (p - 1)) (isqrt N) hsq_ge
    intro m hm_gt hm_le hmod0
    have ⟨j, hjle, hmj⟩ := hdvd_lt_q m (by omega) (by omega) hmod0
    have hle_p : 2 ^ j ≤ 2 ^ (p - 1) := by
      by_cases heq : j = p - 1
      · rw [heq]; exact Nat.le_refl _
      · exact Nat.le_of_lt (pow2_strictMono (by omega))
    omega
  -- Step 2: Closed-form induction for divSumPairs N (2 ^ k) for all k ≤ p - 1
  have hpow_sum : ∀ k : Nat, k ≤ p - 1 →
      divSumPairs N (2 ^ k) = (2 ^ (k + 1) - 1) + (2 ^ p - 2 ^ (p - 1 - k)) * q := by
    intro k
    induction k with
    | zero =>
      intro _
      have h20 : 2 ^ 0 = 1 := rfl
      rw [h20]
      simp only [divSumPairs, Nat.zero_add, Nat.mod_one, beq_self_eq_true, ite_true, Nat.div_one, Nat.add_zero]
      have h1ne : (1 * 1 == N) = false := by
        have hN_ge : 6 ≤ N := by
          have : 2 * 3 ≤ 2 ^ (p - 1) * q := Nat.mul_le_mul hp1_ge2 (by omega)
          exact this
        cases h : (1 * 1 == N)
        · rfl
        · have := beq_iff_eq.mp h; omega
      simp only [h1ne, Bool.false_eq_true, ite_false]
      have hsub0 : p - 1 - 0 = p - 1 := by omega
      rw [hsub0]
      have hdiff : 2 ^ p - 2 ^ (p - 1) = 2 ^ (p - 1) := by omega
      rw [hdiff]
    | succ k ih =>
      intro hk_le
      have hk_prev : k ≤ p - 1 := by omega
      have hih := ih hk_prev
      have h2k_pos : 1 ≤ 2 ^ k := pow2_nat_pos k
      have h2k1_pos : 1 ≤ 2 ^ (k + 1) := pow2_nat_pos (k + 1)
      -- Evaluate step at m = 2 ^ (k + 1)
      have hstep : divSumPairs N (2 ^ (k + 1)) =
          (2 ^ (k + 1) + 2 ^ (p - 1 - (k + 1)) * q) + divSumPairs N (2 ^ (k + 1) - 1) := by
        have hhead : divSumPairs N (2 ^ (k + 1)) = divSumPairs N ((2 ^ (k + 1) - 1) + 1) := by
          have : 2 ^ (k + 1) = (2 ^ (k + 1) - 1) + 1 := by omega
          rw [← this]
        rw [hhead]
        simp only [divSumPairs]
        have hback : 2 ^ (k + 1) - 1 + 1 = 2 ^ (k + 1) := by omega
        rw [hback]
        have hN_fact : N = 2 ^ (k + 1) * (2 ^ (p - 1 - (k + 1)) * q) := by
          dsimp only [N]
          rw [← Nat.mul_assoc, ← Nat.pow_add]
          have hadd : k + 1 + (p - 1 - (k + 1)) = p - 1 := by omega
          rw [hadd]
        have hmod0 : (N % 2 ^ (k + 1) == 0) = true := by
          rw [hN_fact, Nat.mul_mod_right]; rfl
        have hsq_ne : (2 ^ (k + 1) * 2 ^ (k + 1) == N) = false := by
          have hle_half : 2 ^ (k + 1) ≤ 2 ^ (p - 1) := by
            by_cases heq : k + 1 = p - 1
            · rw [heq]; exact Nat.le_refl _
            · exact Nat.le_of_lt (pow2_strictMono (by omega))
          have hsq_lt : 2 ^ (k + 1) * 2 ^ (k + 1) < N := by
            calc 2 ^ (k + 1) * 2 ^ (k + 1)
                ≤ 2 ^ (p - 1) * 2 ^ (p - 1) := Nat.mul_le_mul hle_half hle_half
            _   < 2 ^ (p - 1) * q := Nat.mul_lt_mul_of_pos_left hq_gt_half (by omega)
          cases h : (2 ^ (k + 1) * 2 ^ (k + 1) == N)
          · rfl
          · have := beq_iff_eq.mp h; omega
        have hdiv_eq : N / 2 ^ (k + 1) = 2 ^ (p - 1 - (k + 1)) * q := by
          rw [hN_fact, Nat.mul_div_cancel_left _ (by omega)]
        simp only [hmod0, ite_true, hsq_ne, Bool.false_eq_true, ite_false, hdiv_eq]
      -- Skip open interval (2^k, 2^(k+1) - 1]
      have hskip : divSumPairs N (2 ^ (k + 1) - 1) = divSumPairs N (2 ^ k) := by
        apply divSumPairs_skip N (2 ^ k) (2 ^ (k + 1) - 1) (by rw [Nat.pow_succ]; omega)
        intro m hm_gt hm_le hmod0
        have hm_lt_q : m < q := by
          have hle_half : 2 ^ (k + 1) ≤ 2 ^ (p - 1) := by
            by_cases heq : k + 1 = p - 1
            · rw [heq]; exact Nat.le_refl _
            · exact Nat.le_of_lt (pow2_strictMono (by omega))
          omega
        have ⟨j, _, hmj⟩ := hdvd_lt_q m (by omega) hm_lt_q hmod0
        by_cases hj : j ≤ k
        · have : 2 ^ j ≤ 2 ^ k := by
            by_cases heq : j = k
            · rw [heq]; exact Nat.le_refl _
            · exact Nat.le_of_lt (pow2_strictMono (by omega))
          omega
        · have : 2 ^ (k + 1) ≤ 2 ^ j := by
            by_cases heq : k + 1 = j
            · rw [heq]; exact Nat.le_refl _
            · exact Nat.le_of_lt (pow2_strictMono (by omega))
          omega
      rw [hstep, hskip, hih]
      -- Combine algebraically
      have hpow_step1 : 2 ^ (k + 1 + 1) - 1 = 2 ^ (k + 1) + (2 ^ (k + 1) - 1) := by
        rw [Nat.pow_succ]; omega
      have hpow_rem : 2 ^ (p - 1 - k) = 2 ^ (p - 1 - (k + 1)) * 2 := by
        calc 2 ^ (p - 1 - k) = 2 ^ ((p - 1 - (k + 1)) + 1) := by congr 1; omega
        _ = 2 ^ (p - 1 - (k + 1)) * 2 := Nat.pow_succ 2 _
      have hle_rem : 2 ^ (p - 1 - k) ≤ 2 ^ p := by
        exact Nat.le_of_lt (pow2_strictMono (by omega))
      have hpow_step2 : (2 ^ p - 2 ^ (p - 1 - (k + 1))) * q =
          2 ^ (p - 1 - (k + 1)) * q + (2 ^ p - 2 ^ (p - 1 - k)) * q := by
        rw [← Nat.add_mul]
        congr 1
        omega
      rw [hpow_step1, hpow_step2]
      omega
  -- Finale: plug k = p - 1
  refine ⟨hN_pos, ?_⟩
  rw [hdrop_top, hpow_sum (p - 1) (Nat.le_refl _)]
  have h1 : p - 1 + 1 = p := by omega
  have h2 : p - 1 - (p - 1) = 0 := by omega
  rw [h1, h2]
  have h20 : 2 ^ 0 = 1 := rfl
  rw [h20]
  have hq_def : 2 ^ p - 1 = q := rfl
  rw [hq_def]
  calc q + q * q
      = 1 * q + q * q := by rw [Nat.one_mul]
  _   = (1 + q) * q := (Nat.add_mul 1 q q).symm
  _   = 2 ^ p * q := by congr 1; dsimp only [q]; omega
  _   = (2 * 2 ^ (p - 1)) * q := by rw [h2p_eq, Nat.mul_comm (2 ^ (p - 1)) 2]
  _   = 2 * (2 ^ (p - 1) * q) := Nat.mul_assoc 2 _ _

end FormalAtlas
