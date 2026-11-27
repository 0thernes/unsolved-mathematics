module

-- SPDX-License-Identifier: MIT
public import FormalAtlas.Primes

/-!
# FormalAtlas.PerfectNumbers — Euclid–Euler Even-Perfect Characterization, Mersenne Divisors & Odd-Perfect Exclusion

Proves seven structural theorems for the Odd Perfect Numbers (Rank #8) and
Mersenne Primes Infinitude (Rank #9) open problems in pure Lean 4 Core:
  1. `mersenne_exponent_prime`: If `2^n - 1` is prime (`n ≥ 2`), then `n` is prime.
  2. `perfect_numbers_first_four`: `6`, `28`, `496`, and `8128` are all perfect (`σ(n) = 2n`).
  3. `no_odd_perfect_le_100`: No odd integer `n ≤ 100` is perfect.
  4. `euclid_even_perfect`: **Euclid's Even Perfect Number Theorem (Elements IX.36)** —
     for EVERY `p ≥ 2`, if `2^p - 1` is prime, then `2^(p-1) * (2^p - 1)` is perfect.
  5. `euler_even_perfect_converse`: **Euler's Even Perfect Number Converse (1747)** —
     every even perfect number has the form `2^(p-1) * (2^p - 1)` with `p ≥ 2` and `2^p - 1` prime.
  6. `euclid_euler_even_perfect_iff`: **Complete Euclid–Euler Theorem** —
     biconditional characterization of ALL even perfect numbers.
  7. `mersenne_prime_divisor_congruence`: **Euler's Mersenne Divisor Congruence (1750)** —
     for every odd prime `p ≥ 3` and prime `q ∣ (2^p - 1)`, `2 * p ∣ (q - 1)`.

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

-- ============================================================================
-- Euler's Even Perfect Number Converse (1747) & Complete Euclid–Euler Theorem
-- ============================================================================

/-- Direct linear divisor sum `∑_{1 ≤ d ≤ k, d ∣ n} d`. -/
def divSumLin (n : Nat) : Nat → Nat
  | 0 => 0
  | d + 1 => (if n % (d + 1) == 0 then d + 1 else 0) + divSumLin n d

/-- Sum of paired upper divisors `n / j` for `1 ≤ j ≤ k` satisfying `j ∣ n` and `lo < n / j ≤ hi`. -/
def pairedUpperSum (n lo hi : Nat) : Nat → Nat
  | 0 => 0
  | j + 1 =>
    let q := n / (j + 1)
    let contrib := if n % (j + 1) == 0 && lo < q && q ≤ hi then q else 0
    contrib + pairedUpperSum n lo hi j

/-- Split `divSumPairs n k` into lower divisors `≤ k` and paired upper divisors `> r` (when `k ≤ isqrt n`). -/
theorem divSumPairs_split (n r : Nat) (hsq : r * r ≤ n) (_hhi : n < (r + 1) * (r + 1)) :
    ∀ k : Nat, k ≤ r →
      divSumPairs n k = divSumLin n k + pairedUpperSum n r n k := by
  intro k
  induction k with
  | zero => intro _; rfl
  | succ j ih =>
    intro hle
    have hrec := ih (by omega)
    simp only [divSumPairs, divSumLin, pairedUpperSum]
    rw [hrec]
    by_cases hdiv : n % (j + 1) = 0
    · have hbeq : (n % (j + 1) == 0) = true := beq_iff_eq.mpr hdiv
      have hjj_le : (j + 1) * (j + 1) ≤ n :=
        Nat.le_trans (Nat.mul_le_mul hle hle) hsq
      have hmul : (j + 1) * (n / (j + 1)) = n := Nat.mul_div_cancel' (Nat.dvd_of_mod_eq_zero hdiv)
      have hq_le_n : n / (j + 1) ≤ n := Nat.div_le_self n (j + 1)
      by_cases heq_sq : (j + 1) * (j + 1) = n
      · have hsq_t : ((j + 1) * (j + 1) == n) = true := beq_iff_eq.mpr heq_sq
        have hq_eq : n / (j + 1) = j + 1 := by
          have : (j + 1) * (n / (j + 1)) = (j + 1) * (j + 1) := by rw [hmul, heq_sq]
          exact Nat.eq_of_mul_eq_mul_left (Nat.succ_pos j) this
        have hnot_gt : ¬ (r < n / (j + 1)) := by omega
        have hdec_f : decide (r < n / (j + 1)) = false := by simp [hnot_gt]
        simp only [hbeq, hsq_t, hdec_f, Bool.true_and, Bool.false_and, ite_true, Bool.false_eq_true, ite_false]
        omega
      · have hsq_f : ((j + 1) * (j + 1) == n) = false := by
          cases h : ((j + 1) * (j + 1) == n)
          · rfl
          · exact False.elim (heq_sq (beq_iff_eq.mp h))
        have hq_gt_r : r < n / (j + 1) := by
          by_cases hle_r : n / (j + 1) ≤ r
          · by_cases hlt_r : j + 1 < r
            · have hlt_sq : (j + 1) * (n / (j + 1)) < r * r := by
                have h1 : (j + 1) * (n / (j + 1)) ≤ (j + 1) * r := Nat.mul_le_mul_left (j + 1) hle_r
                have h2 : (j + 1) * r < r * r := Nat.mul_lt_mul_of_pos_right hlt_r (by omega)
                omega
              omega
            · have hjr : j + 1 = r := by omega
              rw [hjr] at hmul heq_sq hle_r
              have hle2 : r * (n / r) ≤ r * r := Nat.mul_le_mul_left r hle_r
              have heq2 : r * (n / r) = r * r := by omega
              have hnr : n / r = r := Nat.eq_of_mul_eq_mul_left (by omega) heq2
              rw [hnr] at hmul
              exact False.elim (heq_sq hmul)
          · omega
        have hdec1 : decide (r < n / (j + 1)) = true := by simp [hq_gt_r]
        have hdec2 : decide (n / (j + 1) ≤ n) = true := by simp [hq_le_n]
        simp only [hbeq, hsq_f, hdec1, hdec2, Bool.true_and, ite_true, Bool.false_eq_true, ite_false]
        omega
    · have hbeq : (n % (j + 1) == 0) = false := by
        cases h : (n % (j + 1) == 0)
        · rfl
        · exact False.elim (hdiv (beq_iff_eq.mp h))
      simp only [hbeq, Bool.false_eq_true, Bool.false_and, ite_false]
      omega

theorem pairedUpperSum_zero (n r k : Nat) : pairedUpperSum n r r k = 0 := by
  induction k with
  | zero => rfl
  | succ j ih =>
    simp only [pairedUpperSum, ih, Nat.add_zero]
    by_cases h : r < n / (j + 1) ∧ n / (j + 1) ≤ r
    · omega
    · have hf : (n % (j + 1) == 0 && decide (r < n / (j + 1)) && decide (n / (j + 1) ≤ r)) = false := by
        by_cases h1 : r < n / (j + 1)
        · have h2 : ¬ (n / (j + 1) ≤ r) := fun hle => h ⟨h1, hle⟩
          simp [h1, h2]
        · simp [h1]
      simp [hf]

theorem pairedUpperSum_step_nondiv (n r m : Nat) (hndiv : n % (m + 1) ≠ 0) :
    ∀ k : Nat, pairedUpperSum n r (m + 1) k = pairedUpperSum n r m k := by
  intro k
  induction k with
  | zero => rfl
  | succ j ih =>
    simp only [pairedUpperSum, ih]
    congr 1
    by_cases hdiv : n % (j + 1) = 0
    · have hne : n / (j + 1) ≠ m + 1 := by
        intro heq
        have hmul : (j + 1) * (m + 1) = n := by
          rw [← heq]; exact Nat.mul_div_cancel' (Nat.dvd_of_mod_eq_zero hdiv)
        have hdvd : (m + 1) ∣ n := ⟨j + 1, by rw [Nat.mul_comm, hmul]⟩
        exact hndiv (Nat.mod_eq_zero_of_dvd hdvd)
      have hiff : (n / (j + 1) ≤ m + 1) ↔ (n / (j + 1) ≤ m) := by omega
      have hb : decide (n / (j + 1) ≤ m + 1) = decide (n / (j + 1) ≤ m) := by
        by_cases hle : n / (j + 1) ≤ m
        · have hle' : n / (j + 1) ≤ m + 1 := by omega
          simp [hle, hle']
        · have hle' : ¬ (n / (j + 1) ≤ m + 1) := by omega
          simp [hle, hle']
      rw [hb]
    · have hbeq : (n % (j + 1) == 0) = false := by
        cases h : (n % (j + 1) == 0)
        · rfl
        · exact False.elim (hdiv (beq_iff_eq.mp h))
      simp [hbeq]

theorem pairedUpperSum_step_div (n r m : Nat) (hr : r ≤ m) (_hhi : n < (r + 1) * (r + 1))
    (hpos : 0 < n) (hdiv : n % (m + 1) = 0) :
    ∀ k : Nat, n / (m + 1) ≤ k →
      pairedUpperSum n r (m + 1) k = (m + 1) + pairedUpperSum n r m k := by
  intro k
  induction k with
  | zero =>
    intro hle
    have hq_pos : 0 < n / (m + 1) := by
      have hmul : (m + 1) * (n / (m + 1)) = n := Nat.mul_div_cancel' (Nat.dvd_of_mod_eq_zero hdiv)
      cases hq : n / (m + 1) with
      | zero => rw [hq, Nat.mul_zero] at hmul; omega
      | succ _ => exact Nat.succ_pos _
    omega
  | succ j ih =>
    intro hle
    have hmul_m : (m + 1) * (n / (m + 1)) = n := Nat.mul_div_cancel' (Nat.dvd_of_mod_eq_zero hdiv)
    by_cases heq : j + 1 = n / (m + 1)
    · -- Unique hit at j + 1 = n / (m + 1)
      have hdiv_j : n % (j + 1) = 0 := by
        have hd : (j + 1) ∣ n := ⟨m + 1, by rw [heq, Nat.mul_comm, hmul_m]⟩
        exact Nat.mod_eq_zero_of_dvd hd
      have hquot_j : n / (j + 1) = m + 1 := by
        have h1 : (j + 1) * (m + 1) = n := by rw [heq, Nat.mul_comm, hmul_m]
        rw [← h1, Nat.mul_div_cancel_left (m + 1) (Nat.succ_pos j)]
      -- For all smaller indices ≤ j, n / i ≠ m + 1
      have hbelow : ∀ t : Nat, t ≤ j → pairedUpperSum n r (m + 1) t = pairedUpperSum n r m t := by
        intro t
        induction t with
        | zero => intro _; rfl
        | succ u ihu =>
          intro hule
          simp only [pairedUpperSum, ihu (by omega)]
          congr 1
          by_cases hdu : n % (u + 1) = 0
          · have hne : n / (u + 1) ≠ m + 1 := by
              intro hqeq
              have hmul_u : (u + 1) * (m + 1) = n := by
                rw [← hqeq]; exact Nat.mul_div_cancel' (Nat.dvd_of_mod_eq_zero hdu)
              have : (u + 1) * (m + 1) = (j + 1) * (m + 1) := by rw [hmul_u, heq, Nat.mul_comm, hmul_m]
              have hu_eq : u + 1 = j + 1 := Nat.eq_of_mul_eq_mul_right (Nat.succ_pos m) this
              omega
            have hb : decide (n / (u + 1) ≤ m + 1) = decide (n / (u + 1) ≤ m) := by
              by_cases h1 : n / (u + 1) ≤ m
              · have h2 : n / (u + 1) ≤ m + 1 := by omega
                simp [h1, h2]
              · have h2 : ¬ (n / (u + 1) ≤ m + 1) := by omega
                simp [h1, h2]
            rw [hb]
          · have hbeq : (n % (u + 1) == 0) = false := by
              cases h : (n % (u + 1) == 0)
              · rfl
              · exact False.elim (hdu (beq_iff_eq.mp h))
            simp [hbeq]
      simp only [pairedUpperSum, hbelow j (Nat.le_refl j)]
      have hbeq : (n % (j + 1) == 0) = true := beq_iff_eq.mpr hdiv_j
      have hgt : r < m + 1 := by omega
      have hnotle : ¬ (m + 1 ≤ m) := by omega
      rw [hquot_j]
      have hd1 : decide (r < m + 1) = true := by simp [hgt]
      have hd2 : decide (m + 1 ≤ m + 1) = true := by simp
      have hd3 : decide (m + 1 ≤ m) = false := by simp [hnotle]
      simp only [hbeq, hd1, hd2, hd3, Bool.true_and, Bool.and_false, ite_true, Bool.false_eq_true, ite_false, Nat.zero_add]
    · -- j + 1 > n / (m + 1), so this index doesn't hit m + 1; recurse via ih
      have hrec := ih (by omega)
      simp only [pairedUpperSum, hrec]
      have hsame :
          (if (n % (j + 1) == 0 && decide (r < n / (j + 1)) && decide (n / (j + 1) ≤ m + 1)) = true
           then n / (j + 1) else 0) =
          (if (n % (j + 1) == 0 && decide (r < n / (j + 1)) && decide (n / (j + 1) ≤ m)) = true
           then n / (j + 1) else 0) := by
        by_cases hdiv_j : n % (j + 1) = 0
        · have hne : n / (j + 1) ≠ m + 1 := by
            intro hqeq
            have hmul_j : (j + 1) * (m + 1) = n := by
              rw [← hqeq]; exact Nat.mul_div_cancel' (Nat.dvd_of_mod_eq_zero hdiv_j)
            have : (j + 1) * (m + 1) = (n / (m + 1)) * (m + 1) := by
              rw [hmul_j, Nat.mul_comm, hmul_m]
            have := Nat.eq_of_mul_eq_mul_right (Nat.succ_pos m) this
            exact heq this
          have hb : decide (n / (j + 1) ≤ m + 1) = decide (n / (j + 1) ≤ m) := by
            by_cases h1 : n / (j + 1) ≤ m
            · have h2 : n / (j + 1) ≤ m + 1 := by omega
              simp [h1, h2]
            · have h2 : ¬ (n / (j + 1) ≤ m + 1) := by omega
              simp [h1, h2]
          rw [hb]
        · have hbeq : (n % (j + 1) == 0) = false := by
            cases h : (n % (j + 1) == 0)
            · rfl
            · exact False.elim (hdiv_j (beq_iff_eq.mp h))
          simp [hbeq]
      rw [hsame]
      omega

/-- Exact identity `divSum n = divSumLin n n` for EVERY `n : Nat`. -/
theorem divSum_eq_divSumLin (n : Nat) : divSum n = divSumLin n n := by
  cases n with
  | zero => unfold divSum isqrt divSumPairs divSumLin; rfl
  | succ m0 =>
    let N := m0 + 1
    have hpos : 0 < N := Nat.succ_pos m0
    have ⟨hsq, hhi⟩ := isqrt_spec N
    let r := isqrt N
    have hsplit : divSum N = divSumLin N r + pairedUpperSum N r N r := by
      unfold divSum
      exact divSumPairs_split N r hsq hhi r (Nat.le_refl r)
    have hr_le_N : r ≤ N := by
      by_cases hr0 : r = 0
      · omega
      · have h1 : r * 1 ≤ r * r := Nat.mul_le_mul_left r (by omega)
        have hsq' : r * r ≤ N := hsq
        omega
    have hind : ∀ t : Nat, r ≤ t → divSumLin N t = divSumLin N r + pairedUpperSum N r t r := by
      intro t
      induction t with
      | zero =>
        intro hr0
        have hr_eq : r = 0 := by omega
        rw [hr_eq, pairedUpperSum_zero, Nat.add_zero]
      | succ k ih =>
        intro hle
        by_cases heq : r = k + 1
        · rw [← heq, pairedUpperSum_zero, Nat.add_zero]
        · have hle_k : r ≤ k := by omega
          have hrec := ih hle_k
          simp only [divSumLin]
          rw [hrec]
          by_cases hdiv : N % (k + 1) = 0
          · have hq_le_r : N / (k + 1) ≤ r := by
              by_cases hgt : r < N / (k + 1)
              · have h1 : r + 1 ≤ k + 1 := by omega
                have h2 : r + 1 ≤ N / (k + 1) := by omega
                have hmul : (r + 1) * (r + 1) ≤ (k + 1) * (N / (k + 1)) := Nat.mul_le_mul h1 h2
                have heqN : (k + 1) * (N / (k + 1)) = N := Nat.mul_div_cancel' (Nat.dvd_of_mod_eq_zero hdiv)
                have hhi' : N < (r + 1) * (r + 1) := hhi
                omega
              · omega
            have hstep := pairedUpperSum_step_div N r k hle_k hhi hpos hdiv r hq_le_r
            have hbeq : (N % (k + 1) == 0) = true := beq_iff_eq.mpr hdiv
            simp only [hbeq, ite_true]
            omega
          · have hstep := pairedUpperSum_step_nondiv N r k hdiv r
            have hbeq : (N % (k + 1) == 0) = false := by
              cases h : (N % (k + 1) == 0)
              · rfl
              · exact False.elim (hdiv (beq_iff_eq.mp h))
            simp only [hbeq, Bool.false_eq_true, ite_false, Nat.zero_add]
            omega
    rw [hsplit, hind N hr_le_N]

/-- Odd/even partition sum up to `2 * b` for `divSumLin`. -/
def divSumOdd (M : Nat) : Nat → Nat
  | 0 => 0
  | b + 1 => (if M % (2 * b + 1) == 0 then 2 * b + 1 else 0) + divSumOdd M b

def divSumEven (M : Nat) : Nat → Nat
  | 0 => 0
  | b + 1 => (if M % (2 * (b + 1)) == 0 then 2 * (b + 1) else 0) + divSumEven M b

theorem divSumLin_two_mul_split (M : Nat) :
    ∀ b : Nat, divSumLin M (2 * b) = divSumOdd M b + divSumEven M b := by
  intro b
  induction b with
  | zero => rfl
  | succ b ih =>
    have h2 : 2 * (b + 1) = (2 * b + 1) + 1 := by omega
    rw [h2]
    simp only [divSumLin, divSumOdd, divSumEven]
    rw [ih]
    have hrew : 2 * b + 1 + 1 = 2 * (b + 1) := by omega
    rw [hrew]
    omega

theorem divSumEven_two_mul (N : Nat) :
    ∀ b : Nat, divSumEven (2 * N) b = 2 * divSumLin N b := by
  intro b
  induction b with
  | zero => rfl
  | succ b ih =>
    simp only [divSumEven, divSumLin, ih]
    have hmod : (2 * N) % (2 * (b + 1)) = 2 * (N % (b + 1)) := Nat.mul_mod_mul_left 2 N (b + 1)
    by_cases hdiv : N % (b + 1) = 0
    · have h1 : (N % (b + 1) == 0) = true := beq_iff_eq.mpr hdiv
      have h2 : ((2 * N) % (2 * (b + 1)) == 0) = true := by rw [hmod, hdiv]; rfl
      simp only [h1, h2, ite_true]
      omega
    · have h1 : (N % (b + 1) == 0) = false := by
        cases h : (N % (b + 1) == 0)
        · rfl
        · exact False.elim (hdiv (beq_iff_eq.mp h))
      have h2 : ((2 * N) % (2 * (b + 1)) == 0) = false := by
        cases h : ((2 * N) % (2 * (b + 1)) == 0)
        · rfl
        · have heq := beq_iff_eq.mp h; rw [hmod] at heq; omega
      simp only [h1, h2, Bool.false_eq_true, ite_false]
      omega

theorem odd_dvd_two_mul_iff (N d : Nat) (hodd : d % 2 = 1) :
    d ∣ (2 * N) ↔ d ∣ N := by
  constructor
  · intro hd
    have hcop : Nat.gcd d 2 = 1 := by
      have h2 : Nat.gcd d 2 ∣ 2 := Nat.gcd_dvd_right d 2
      have hdg : Nat.gcd d 2 ∣ d := Nat.gcd_dvd_left d 2
      have hpos : 0 < Nat.gcd d 2 := Nat.gcd_pos_of_pos_right d (by decide)
      have hle : Nat.gcd d 2 ≤ 2 := Nat.le_of_dvd (by decide) h2
      by_cases h2eq : Nat.gcd d 2 = 2
      · rw [h2eq] at hdg; have ⟨t, ht⟩ := hdg; omega
      · omega
    rw [Nat.mul_comm] at hd
    exact dvd_left_of_dvd_mul_coprime hd hcop
  · intro hd
    exact Nat.dvd_trans hd (Nat.dvd_mul_left N 2)

theorem odd_dvd_pow2_mul_iff (m d : Nat) (hodd : d % 2 = 1) :
    ∀ k : Nat, d ∣ (2 ^ k * m) ↔ d ∣ m := by
  intro k
  induction k with
  | zero => simp
  | succ k ih =>
    have hrew : 2 ^ (k + 1) * m = 2 * (2 ^ k * m) := by
      rw [Nat.pow_succ, Nat.mul_comm (2 ^ k) 2, Nat.mul_assoc]
    rw [hrew, odd_dvd_two_mul_iff (2 ^ k * m) d hodd, ih]

theorem divSumLin_ge_self (m : Nat) (hm : 0 < m) : ∀ b : Nat, m ≤ b → divSumLin m b = divSumLin m m := by
  intro b
  induction b with
  | zero => intro h; omega
  | succ k ih =>
    intro hle
    by_cases heq : m = k + 1
    · rw [heq]
    · have hlt : m < k + 1 := by omega
      have hndiv : m % (k + 1) ≠ 0 := by
        rw [Nat.mod_eq_of_lt hlt]; omega
      have hbeq : (m % (k + 1) == 0) = false := by
        cases h : (m % (k + 1) == 0)
        · rfl
        · exact False.elim (hndiv (beq_iff_eq.mp h))
      simp only [divSumLin, hbeq, Bool.false_eq_true, ite_false, Nat.zero_add]
      exact ih (by omega)

theorem divSumEven_of_odd (m : Nat) (hodd : m % 2 = 1) : ∀ b : Nat, divSumEven m b = 0 := by
  intro b
  induction b with
  | zero => rfl
  | succ b ih =>
    simp only [divSumEven, ih, Nat.add_zero]
    have hndiv : m % (2 * (b + 1)) ≠ 0 := by
      intro h0
      have ⟨q, hq⟩ := Nat.dvd_of_mod_eq_zero h0
      have h2 : m % 2 = 0 := Nat.mod_eq_zero_of_dvd ⟨(b + 1) * q, by rw [hq]; ac_rfl⟩
      omega
    have hbeq : (m % (2 * (b + 1)) == 0) = false := by
      cases h : (m % (2 * (b + 1)) == 0)
      · rfl
      · exact False.elim (hndiv (beq_iff_eq.mp h))
    simp [hbeq]

theorem divSumOdd_pow2_mul (m k : Nat) :
    ∀ b : Nat, divSumOdd (2 ^ k * m) b = divSumOdd m b := by
  intro b
  induction b with
  | zero => rfl
  | succ b ih =>
    simp only [divSumOdd, ih]
    congr 1
    have hodd_d : (2 * b + 1) % 2 = 1 := by omega
    have hiff := odd_dvd_pow2_mul_iff m (2 * b + 1) hodd_d k
    by_cases hd : (2 * b + 1) ∣ m
    · have h1 : (m % (2 * b + 1) == 0) = true := beq_iff_eq.mpr (Nat.mod_eq_zero_of_dvd hd)
      have h2 : ((2 ^ k * m) % (2 * b + 1) == 0) = true :=
        beq_iff_eq.mpr (Nat.mod_eq_zero_of_dvd (hiff.mpr hd))
      simp [h1, h2]
    · have h1 : (m % (2 * b + 1) == 0) = false := by
        cases h : (m % (2 * b + 1) == 0)
        · rfl
        · exact False.elim (hd (Nat.dvd_of_mod_eq_zero (beq_iff_eq.mp h)))
      have h2 : ((2 ^ k * m) % (2 * b + 1) == 0) = false := by
        cases h : ((2 ^ k * m) % (2 * b + 1) == 0)
        · rfl
        · exact False.elim (hd (hiff.mp (Nat.dvd_of_mod_eq_zero (beq_iff_eq.mp h))))
      simp [h1, h2]

/-- Exact 2-part multiplicativity of `divSumLin`: for odd `m`, `σ(2^k * m) = (2^(k+1) - 1) * σ(m)`. -/
theorem divSumLin_pow2_mul_odd (m : Nat) (hodd : m % 2 = 1) :
    ∀ k : Nat, divSumLin (2 ^ k * m) (2 ^ k * m) = (2 ^ (k + 1) - 1) * divSumLin m m := by
  intro k
  induction k with
  | zero =>
    simp only [Nat.pow_zero, Nat.one_mul]
    have : 2 ^ 1 - 1 = 1 := rfl
    rw [this, Nat.one_mul]
  | succ k ih =>
    have hrew : 2 ^ (k + 1) * m = 2 * (2 ^ k * m) := by
      rw [Nat.pow_succ, Nat.mul_comm (2 ^ k) 2, Nat.mul_assoc]
    rw [hrew, divSumLin_two_mul_split (2 * (2 ^ k * m)) (2 ^ k * m)]
    rw [divSumEven_two_mul (2 ^ k * m) (2 ^ k * m), ih]
    rw [← hrew, divSumOdd_pow2_mul m (k + 1) (2 ^ k * m)]
    have hm_pos : 0 < m := by omega
    have hm_le : m ≤ 2 * (2 ^ k * m) := by
      have hp : 1 ≤ 2 ^ k := pow2_nat_pos k
      have h1 : 1 * m ≤ 2 ^ k * m := Nat.mul_le_mul_right m hp
      rw [Nat.one_mul] at h1
      omega
    have hodd_eq : divSumOdd m (2 ^ k * m) = divSumLin m m := by
      have hsplit := divSumLin_two_mul_split m (2 ^ k * m)
      rw [divSumEven_of_odd m hodd (2 ^ k * m), Nat.add_zero] at hsplit
      rw [← hsplit, divSumLin_ge_self m hm_pos (2 * (2 ^ k * m)) hm_le]
    rw [hodd_eq]
    have hp1 : 1 ≤ 2 ^ (k + 1) := pow2_nat_pos (k + 1)
    have hpow2 : 2 ^ (k + 1 + 1) - 1 = 1 + 2 * (2 ^ (k + 1) - 1) := by
      rw [Nat.pow_succ]; omega
    rw [hpow2, Nat.add_mul, Nat.one_mul, Nat.mul_assoc]

/-- Factor out the exact power of 2 from any positive natural number. -/
theorem nat_factor_pow2 (n : Nat) (hpos : 0 < n) :
    ∃ k m : Nat, m % 2 = 1 ∧ n = 2 ^ k * m := by
  have hmain : ∀ n : Nat, 0 < n → ∃ k m : Nat, m % 2 = 1 ∧ n = 2 ^ k * m := by
    apply nat_strong_ind_pn (P := fun n => 0 < n → ∃ k m : Nat, m % 2 = 1 ∧ n = 2 ^ k * m)
    intro n ih hn
    by_cases hodd : n % 2 = 1
    · exact ⟨0, n, hodd, by simp⟩
    · have hhalf_pos : 0 < n / 2 := by omega
      have hhalf_lt : n / 2 < n := by omega
      have ⟨k, m, hm_odd, hm_eq⟩ := ih (n / 2) hhalf_lt hhalf_pos
      refine ⟨k + 1, m, hm_odd, ?_⟩
      rw [Nat.pow_succ, Nat.mul_comm (2 ^ k) 2, Nat.mul_assoc, ← hm_eq]
      omega
  exact hmain n hpos

theorem divSumLin_mono (m : Nat) : ∀ a b : Nat, a ≤ b → divSumLin m a ≤ divSumLin m b := by
  intro a b
  induction b with
  | zero =>
    intro h
    have ha0 : a = 0 := by omega
    subst ha0
    exact Nat.le_refl _
  | succ k ih =>
    intro hle
    by_cases heq : a = k + 1
    · subst heq; exact Nat.le_refl _
    · have hrec := ih (by omega)
      simp only [divSumLin]
      omega

/-- Any three strictly ordered divisors `1 < a < m` force `1 + a + m ≤ divSumLin m m`. -/
theorem divSumLin_ge_three_divisors (m a : Nat) (ha1 : 1 < a) (ham : a < m) (hdvd : a ∣ m) :
    1 + a + m ≤ divSumLin m m := by
  have hm_ge1 : 1 ≤ divSumLin m 1 := by
    have h1 : m % 1 = 0 := Nat.mod_one m
    simp [divSumLin, h1]
  have hstep_a : a + divSumLin m (a - 1) ≤ divSumLin m a := by
    have hraw : divSumLin m ((a - 1) + 1) =
        (if m % ((a - 1) + 1) == 0 then (a - 1) + 1 else 0) + divSumLin m (a - 1) := rfl
    have ha_eq : (a - 1) + 1 = a := by omega
    rw [ha_eq] at hraw
    have hbeq : (m % a == 0) = true := beq_iff_eq.mpr (Nat.mod_eq_zero_of_dvd hdvd)
    rw [hbeq] at hraw
    simp only [ite_true] at hraw
    omega
  have h1_le_am1 : divSumLin m 1 ≤ divSumLin m (a - 1) := divSumLin_mono m 1 (a - 1) (by omega)
  have hstep_m : m + divSumLin m (m - 1) ≤ divSumLin m m := by
    have hraw : divSumLin m ((m - 1) + 1) =
        (if m % ((m - 1) + 1) == 0 then (m - 1) + 1 else 0) + divSumLin m (m - 1) := rfl
    have hm_eq : (m - 1) + 1 = m := by omega
    rw [hm_eq] at hraw
    have hbeq : (m % m == 0) = true := beq_iff_eq.mpr (Nat.mod_self m)
    rw [hbeq] at hraw
    simp only [ite_true] at hraw
    omega
  have ha_le_mm1 : divSumLin m a ≤ divSumLin m (m - 1) := divSumLin_mono m a (m - 1) (by omega)
  omega

/-- **Euler's Even Perfect Number Converse (1747):**
    Every even perfect number has the form `2^(p-1) * (2^p - 1)` for some `p ≥ 2` with `2^p - 1` prime. -/
public theorem euler_even_perfect_converse (n : Nat) (heven : n % 2 = 0) (hperf : IsPerfect n) :
    ∃ p : Nat, 2 ≤ p ∧ IsPrime (2 ^ p - 1) ∧ n = 2 ^ (p - 1) * (2 ^ p - 1) := by
  have ⟨hn_pos, hsig⟩ := hperf
  have ⟨k, m, hm_odd, hn_eq⟩ := nat_factor_pow2 n hn_pos
  have hk_ge1 : 1 ≤ k := by
    cases k with
    | zero => simp at hn_eq; omega
    | succ _ => omega
  have hm_pos : 0 < m := by omega
  -- Evaluate divSum n via divSumLin_pow2_mul_odd
  have hlin : divSum n = (2 ^ (k + 1) - 1) * divSumLin m m := by
    rw [divSum_eq_divSumLin, hn_eq, divSumLin_pow2_mul_odd m hm_odd k]
  have h2n : 2 * n = 2 ^ (k + 1) * m := by
    rw [hn_eq, Nat.pow_succ, Nat.mul_comm (2 ^ k) 2, Nat.mul_assoc]
  have heq_main : (2 ^ (k + 1) - 1) * divSumLin m m = 2 ^ (k + 1) * m := by
    rw [← hlin, hsig, h2n]
  -- Coprimality of (2^(k+1) - 1) and 2^(k+1)
  have h2k1_ge4 : 4 ≤ 2 ^ (k + 1) := by
    have h1 : 2 ^ 2 ≤ 2 ^ (k + 1) := by
      by_cases hk1 : k = 1
      · rw [hk1]; exact Nat.le_refl _
      · exact Nat.le_of_lt (pow2_strictMono (by omega))
    exact h1
  have hcop : Nat.gcd (2 ^ (k + 1) - 1) (2 ^ (k + 1)) = 1 := by
    let g := Nat.gcd (2 ^ (k + 1) - 1) (2 ^ (k + 1))
    have hg1 : g ∣ (2 ^ (k + 1) - 1) := Nat.gcd_dvd_left _ _
    have hg2 : g ∣ 2 ^ (k + 1) := Nat.gcd_dvd_right _ _
    have hadd : (2 ^ (k + 1) - 1) + 1 = 2 ^ (k + 1) := by omega
    have hg2' : g ∣ (2 ^ (k + 1) - 1) + 1 := by rw [hadd]; exact hg2
    have hg_one : g ∣ 1 := (Nat.dvd_add_right hg1).mp hg2'
    exact Nat.eq_one_of_dvd_one hg_one
  have hdvd_prod : (2 ^ (k + 1) - 1) ∣ m * 2 ^ (k + 1) :=
    ⟨divSumLin m m, by rw [Nat.mul_comm m _, ← heq_main]⟩
  have hdvd_m : (2 ^ (k + 1) - 1) ∣ m := dvd_left_of_dvd_mul_coprime hdvd_prod hcop
  have ⟨q, hmq⟩ := hdvd_m
  have hq_pos : 0 < q := by
    cases q with
    | zero => simp at hmq; omega
    | succ _ => exact Nat.succ_pos _
  -- Cancel (2^(k+1) - 1) > 0 to get divSumLin m m = m + q
  have hsig_m : divSumLin m m = m + q := by
    have hmul_eq : (2 ^ (k + 1) - 1) * divSumLin m m = (2 ^ (k + 1) - 1) * (2 ^ (k + 1) * q) := by
      rw [heq_main, hmq]; ac_rfl
    have hdiv_eq : divSumLin m m = 2 ^ (k + 1) * q :=
      Nat.eq_of_mul_eq_mul_left (by omega : 0 < 2 ^ (k + 1) - 1) hmul_eq
    have hexp : 2 ^ (k + 1) * q = (2 ^ (k + 1) - 1) * q + q := by
      have h1 : (2 ^ (k + 1) - 1 + 1) * q = (2 ^ (k + 1) - 1) * q + q := by
        rw [Nat.add_mul, Nat.one_mul]
      have h2 : 2 ^ (k + 1) - 1 + 1 = 2 ^ (k + 1) := by omega
      rw [h2] at h1
      exact h1
    rw [hdiv_eq, hexp, ← hmq]
  -- Deduce q = 1 (else 1 < q < m gives 1 + q + m ≤ divSumLin m m = m + q)
  have hq_one : q = 1 := by
    by_cases hq1 : q = 1
    · exact hq1
    · exfalso
      have hq_gt1 : 1 < q := by omega
      have hq_lt_m : q < m := by
        have h1 : 3 * q ≤ (2 ^ (k + 1) - 1) * q := Nat.mul_le_mul_right q (by omega)
        omega
      have hq_dvd : q ∣ m := ⟨2 ^ (k + 1) - 1, by rw [hmq, Nat.mul_comm]⟩
      have h3 := divSumLin_ge_three_divisors m q hq_gt1 hq_lt_m hq_dvd
      omega
  have hm_eq : m = 2 ^ (k + 1) - 1 := by rw [hmq, hq_one, Nat.mul_one]
  -- Deduce IsPrime m from divSumLin m m = m + 1
  have hm_prime : IsPrime m := by
    refine ⟨by omega, ?_⟩
    intro d hd
    have hd_pos : 0 < d := by
      cases d with
      | zero => have ⟨t, ht⟩ := hd; simp at ht; omega
      | succ _ => exact Nat.succ_pos _
    have hd_le : d ≤ m := Nat.le_of_dvd hm_pos hd
    by_cases hd1 : d = 1
    · exact Or.inl hd1
    · by_cases hdm : d = m
      · exact Or.inr hdm
      · exfalso
        have h3 := divSumLin_ge_three_divisors m d (by omega) (by omega) hd
        omega
  refine ⟨k + 1, by omega, ?_, ?_⟩
  · rw [← hm_eq]; exact hm_prime
  · rw [hn_eq, hm_eq]
    have : k + 1 - 1 = k := by omega
    rw [this]

/-- **Complete Euclid–Euler Theorem:**
    An even natural number `n` is perfect if and only if `n = 2^(p-1) * (2^p - 1)` for some `p ≥ 2`
    with `2^p - 1` prime. -/
public theorem euclid_euler_even_perfect_iff (n : Nat) (heven : n % 2 = 0) :
    IsPerfect n ↔ ∃ p : Nat, 2 ≤ p ∧ IsPrime (2 ^ p - 1) ∧ n = 2 ^ (p - 1) * (2 ^ p - 1) := by
  constructor
  · exact euler_even_perfect_converse n heven
  · intro ⟨p, hp, hmp, hneq⟩
    rw [hneq]
    exact euclid_even_perfect p hp hmp

-- ============================================================================
-- Euler's Mersenne Prime Divisor Congruence (1750): p ≥ 3 prime, q prime, q ∣ 2^p - 1 → 2p ∣ q - 1
-- ============================================================================

/-- Euclid's Lemma for `IsPrime`: `p ∣ a * b → p ∣ a ∨ p ∣ b`. -/
theorem prime_dvd_mul {p a b : Nat} (hp : IsPrime p) (hdvd : p ∣ a * b) : p ∣ a ∨ p ∣ b := by
  by_cases hpb : p ∣ b
  · exact Or.inr hpb
  · left
    have hcop : Nat.gcd p b = 1 := by
      have hg_p : Nat.gcd p b ∣ p := Nat.gcd_dvd_left p b
      have hg_b : Nat.gcd p b ∣ b := Nat.gcd_dvd_right p b
      rcases hp.2 (Nat.gcd p b) hg_p with h1 | hfull
      · exact h1
      · rw [hfull] at hg_b; exact False.elim (hpb hg_b)
    exact dvd_left_of_dvd_mul_coprime hdvd hcop

theorem prime_not_dvd_fact_of_lt {q k : Nat} (hq : IsPrime q) (hlt : k < q) : ¬ (q ∣ fact k) := by
  induction k with
  | zero =>
    intro hd
    have hle : q ≤ 1 := Nat.le_of_dvd (by decide) hd
    have := hq.1
    omega
  | succ m ih =>
    intro hd
    simp only [fact] at hd
    rcases prime_dvd_mul hq hd with h1 | h2
    · have hle : q ≤ m + 1 := Nat.le_of_dvd (Nat.succ_pos m) h1
      omega
    · exact ih (by omega) h2

/-- Standard binomial coefficient `C(n, k)`. -/
def binom : Nat → Nat → Nat
  | _, 0 => 1
  | 0, _ + 1 => 0
  | n + 1, k + 1 => binom n k + binom n (k + 1)

theorem binom_self (n : Nat) : binom n n = 1 := by
  induction n with
  | zero => rfl
  | succ k ih =>
    have hzero : ∀ a b : Nat, a < b → binom a b = 0 := by
      intro a
      induction a with
      | zero => intro b hb; cases b with | zero => omega | succ _ => rfl
      | succ a iha =>
        intro b hb
        cases b with
        | zero => omega
        | succ b => simp only [binom, iha b (by omega), iha (b + 1) (by omega)]
    simp only [binom, ih, hzero k (k + 1) (by omega), Nat.add_zero]

theorem binom_fact_identity : ∀ n k : Nat, k ≤ n →
    binom n k * fact k * fact (n - k) = fact n := by
  intro n
  induction n with
  | zero =>
    intro k hk
    have : k = 0 := by omega
    subst this; rfl
  | succ n ih =>
    intro k hk
    cases k with
    | zero => simp [binom, fact]
    | succ k =>
      by_cases hkn : k + 1 = n + 1
      · have hkeq : k = n := by omega
        subst hkeq
        simp [binom_self, fact]
      · have hle1 : k ≤ n := by omega
        have hle2 : k + 1 ≤ n := by omega
        have h1 := ih k hle1
        have h2 := ih (k + 1) hle2
        have hsub1 : n - k = (n - (k + 1)) + 1 := by omega
        have hsub2 : n + 1 - (k + 1) = n - k := by omega
        rw [hsub2]
        simp only [binom, Nat.add_mul]
        -- Term 1: binom n k * fact (k+1) * fact (n - k) = (k + 1) * fact n
        have ht1 : binom n k * fact (k + 1) * fact (n - k) = (k + 1) * fact n := by
          calc binom n k * fact (k + 1) * fact (n - k)
              = binom n k * ((k + 1) * fact k) * fact (n - k) := rfl
          _   = (k + 1) * (binom n k * fact k * fact (n - k)) := by ac_rfl
          _   = (k + 1) * fact n := by rw [h1]
        -- Term 2: binom n (k+1) * fact (k+1) * fact (n - k) = (n - k) * fact n
        have ht2 : binom n (k + 1) * fact (k + 1) * fact (n - k) = (n - k) * fact n := by
          have hfnk : fact (n - k) = (n - k) * fact (n - (k + 1)) := by
            have hraw : fact (n - (k + 1) + 1) = (n - (k + 1) + 1) * fact (n - (k + 1)) := rfl
            rw [← hsub1] at hraw
            exact hraw
          calc binom n (k + 1) * fact (k + 1) * fact (n - k)
              = binom n (k + 1) * fact (k + 1) * ((n - k) * fact (n - (k + 1))) := by rw [hfnk]
          _   = (n - k) * (binom n (k + 1) * fact (k + 1) * fact (n - (k + 1))) := by ac_rfl
          _   = (n - k) * fact n := by rw [h2]
        rw [ht1, ht2, ← Nat.add_mul]
        have hsum : (k + 1) + (n - k) = n + 1 := by omega
        rw [hsum]; rfl

theorem prime_dvd_binom {q k : Nat} (hq : IsPrime q) (hk1 : 1 ≤ k) (hk2 : k < q) :
    q ∣ binom q k := by
  have hid := binom_fact_identity q k (by omega)
  have hq_fact : q ∣ fact q := dvd_fact_of_le q q (by have := hq.1; omega) (Nat.le_refl q)
  rw [← hid] at hq_fact
  have hnot_sub : ¬ (q ∣ fact (q - k)) := prime_not_dvd_fact_of_lt hq (by omega)
  have hnot_k : ¬ (q ∣ fact k) := prime_not_dvd_fact_of_lt hq hk2
  rcases prime_dvd_mul hq hq_fact with hleft | hright
  · rcases prime_dvd_mul hq hleft with hbin | hfk
    · exact hbin
    · exact False.elim (hnot_k hfk)
  · exact False.elim (hnot_sub hright)

/-- Partial binomial expansion sum `∑_{i=0}^{m} C(n, i) * a^i`. -/
def binomSum (n a : Nat) : Nat → Nat
  | 0 => binom n 0 * a ^ 0
  | m + 1 => binom n (m + 1) * a ^ (m + 1) + binomSum n a m

theorem binomSum_succ_expand (n a : Nat) :
    ∀ m : Nat, binomSum (n + 1) a (m + 1) = binomSum n a (m + 1) + a * binomSum n a m := by
  intro m
  induction m with
  | zero =>
    simp only [binomSum, binom, Nat.pow_zero, Nat.mul_one, Nat.pow_succ, Nat.one_mul]
    rw [Nat.add_mul, Nat.one_mul]
    omega
  | succ k ih =>
    simp only [binomSum] at ih ⊢
    rw [ih]
    have hpas : binom (n + 1) (k + 1 + 1) = binom n (k + 1) + binom n (k + 1 + 1) := rfl
    rw [hpas, Nat.add_mul, Nat.mul_add]
    have hpow : binom n (k + 1) * a ^ (k + 1 + 1) = a * (binom n (k + 1) * a ^ (k + 1)) := by
      have hp : a ^ (k + 1 + 1) = a ^ (k + 1) * a := Nat.pow_succ a (k + 1)
      rw [hp]; ac_rfl
    rw [hpow]
    omega

theorem binomial_theorem_one (n a : Nat) : (a + 1) ^ n = binomSum n a n := by
  induction n with
  | zero => simp [binomSum, binom]
  | succ k ih =>
    have hpow_step : (a + 1) ^ (k + 1) = (a + 1) ^ k * a + (a + 1) ^ k := by
      rw [Nat.pow_succ, Nat.mul_add, Nat.mul_one]
    rw [hpow_step, ih]
    cases k with
    | zero =>
      simp [binomSum, binom]
    | succ r =>
      have h1 := binomSum_succ_expand (r + 1) a r
      have htop : binomSum (r + 1 + 1) a (r + 1 + 1) =
          binom (r + 1 + 1) (r + 1 + 1) * a ^ (r + 1 + 1) + binomSum (r + 1 + 1) a (r + 1) := rfl
      rw [binom_self, Nat.one_mul] at htop
      rw [htop, h1]
      have hsplit : binomSum (r + 1) a (r + 1) =
          binom (r + 1) (r + 1) * a ^ (r + 1) + binomSum (r + 1) a r := rfl
      rw [binom_self, Nat.one_mul] at hsplit
      have hmul_a : binomSum (r + 1) a (r + 1) * a = a ^ (r + 1 + 1) + a * binomSum (r + 1) a r := by
        have hp : a ^ (r + 1) * a = a ^ (r + 1 + 1) := (Nat.pow_succ a (r + 1)).symm
        rw [hsplit, Nat.add_mul, hp, Nat.mul_comm (binomSum (r + 1) a r) a]
      rw [hmul_a]
      omega

theorem binomSum_dvd_prime (q a : Nat) (hq : IsPrime q) :
    ∀ m : Nat, m < q → (binomSum q a m) % q = 1 % q := by
  intro m
  induction m with
  | zero =>
    intro _
    simp [binomSum, binom]
  | succ k ih =>
    intro hlt
    simp only [binomSum]
    have hdvd : q ∣ binom q (k + 1) := prime_dvd_binom hq (by omega) hlt
    have hterm : q ∣ binom q (k + 1) * a ^ (k + 1) := Nat.dvd_mul_right_of_dvd hdvd _
    have hmod0 : (binom q (k + 1) * a ^ (k + 1)) % q = 0 := Nat.mod_eq_zero_of_dvd hterm
    rw [Nat.add_mod, hmod0, Nat.zero_add, Nat.mod_mod, ih (by omega)]

/-- **Fermat's Little Theorem (Freshman's Dream):** `a ^ q % q = a % q` for every prime `q`. -/
theorem fermat_little_mod (q : Nat) (hq : IsPrime q) :
    ∀ a : Nat, a ^ q % q = a % q := by
  intro a
  induction a with
  | zero =>
    have hq_pos : 0 < q := by have := hq.1; omega
    have h0 : 0 ^ q = 0 := Nat.zero_pow hq_pos
    rw [h0]
  | succ a ih =>
    rw [binomial_theorem_one q a]
    have hraw : binomSum q a ((q - 1) + 1) = binom q ((q - 1) + 1) * a ^ ((q - 1) + 1) + binomSum q a (q - 1) := rfl
    have hq_eq : (q - 1) + 1 = q := by have := hq.1; omega
    rw [hq_eq, binom_self, Nat.one_mul] at hraw
    rw [hraw]
    have htail : binomSum q a (q - 1) % q = 1 % q :=
      binomSum_dvd_prime q a hq (q - 1) (by have := hq.1; omega)
    rw [Nat.add_mod, ih, htail, ← Nat.add_mod]

/-- Euclidean descent on modular exponents of `2`: `2^a ≡ 1` and `2^b ≡ 1 (mod q)` imply `2^(gcd a b) ≡ 1`. -/
theorem pow2_mod_gcd_eq_one (q : Nat) (hq2 : 2 ≤ q) :
    ∀ b a : Nat, 2 ^ a % q = 1 → 2 ^ b % q = 1 → 2 ^ (Nat.gcd a b) % q = 1 := by
  apply nat_strong_ind_pn (P := fun b => ∀ a : Nat, 2 ^ a % q = 1 → 2 ^ b % q = 1 → 2 ^ (Nat.gcd a b) % q = 1)
  intro b ih a ha hb
  by_cases hb0 : b = 0
  · subst hb0; rw [Nat.gcd_zero_right]; exact ha
  · have hlt : a % b < b := Nat.mod_lt a (Nat.pos_of_ne_zero hb0)
    have hpow_mul : ∀ k : Nat, 2 ^ (b * k) % q = 1 := by
      intro k
      induction k with
      | zero =>
        simp only [Nat.mul_zero, Nat.pow_zero]
        exact Nat.mod_eq_of_lt (by omega)
      | succ k ihk =>
        rw [Nat.mul_succ, Nat.pow_add, Nat.mul_mod, ihk, hb, Nat.one_mul]
        exact Nat.mod_eq_of_lt (by omega)
    have hrem : 2 ^ (a % b) % q = 1 := by
      have hdiv : a = b * (a / b) + a % b := (Nat.div_add_mod a b).symm
      have ha' := ha
      rw [hdiv, Nat.pow_add, Nat.mul_mod, hpow_mul (a / b), Nat.one_mul, Nat.mod_mod] at ha'
      exact ha'
    have hgcd : Nat.gcd a b = Nat.gcd b (a % b) := by
      rw [Nat.gcd_comm a b, Nat.gcd_rec b a, Nat.gcd_comm]
    rw [hgcd]
    exact ih (a % b) hlt b hb hrem

/-- **Euler's Mersenne Prime Divisor Congruence (1750):**
    For every odd prime `p ≥ 3` and every prime `q ∣ (2^p - 1)`, `2 * p ∣ (q - 1)` (i.e. `q ≡ 1 (mod 2p)`). -/
public theorem mersenne_prime_divisor_congruence (p q : Nat)
    (hp : IsPrime p) (hp3 : 3 ≤ p) (hq : IsPrime q) (hdvd : q ∣ 2 ^ p - 1) :
    2 * p ∣ q - 1 := by
  have h2p_ge2 : 2 ≤ 2 ^ p := by
    have : 2 ^ 1 < 2 ^ p := pow2_strictMono (by omega)
    have : 2 ^ 1 = 2 := rfl
    omega
  -- q is odd (hence q ≥ 3) because 2^p - 1 is odd
  have hq_odd : q % 2 = 1 := by
    by_cases h2 : q % 2 = 0
    · exfalso
      have h2q : 2 ∣ q := Nat.dvd_of_mod_eq_zero h2
      have h2m : 2 ∣ 2 ^ p - 1 := Nat.dvd_trans h2q hdvd
      have h2pow : 2 ∣ 2 ^ p := by
        have : 2 ^ p = 2 ^ (p - 1) * 2 := by
          calc 2 ^ p = 2 ^ ((p - 1) + 1) := by congr 1; omega
          _ = 2 ^ (p - 1) * 2 := Nat.pow_succ 2 (p - 1)
        exact ⟨2 ^ (p - 1), by rw [this, Nat.mul_comm]⟩
      have hadd : (2 ^ p - 1) + 1 = 2 ^ p := by omega
      rw [← hadd] at h2pow
      have h2one : 2 ∣ 1 := (Nat.dvd_add_right h2m).mp h2pow
      have := Nat.le_of_dvd (by decide) h2one
      omega
    · omega
  have hq_ge3 : 3 ≤ q := by have := hq.1; omega
  -- 2^p % q = 1
  have h2p_mod : 2 ^ p % q = 1 := by
    have ⟨t, ht⟩ := hdvd
    have heq : 2 ^ p = q * t + 1 := by omega
    rw [heq, Nat.mul_add_mod]
    exact Nat.mod_eq_of_lt (by omega)
  -- Fermat's Little Theorem: 2^(q-1) % q = 1
  have hflt := fermat_little_mod q hq 2
  have h2q_dvd : q ∣ 2 * (2 ^ (q - 1) - 1) := by
    have hq_pos : 1 ≤ q := by omega
    have hpow_q : 2 ^ q = 2 * 2 ^ (q - 1) := by
      calc 2 ^ q = 2 ^ ((q - 1) + 1) := by congr 1; omega
      _ = 2 ^ (q - 1) * 2 := Nat.pow_succ 2 (q - 1)
      _ = 2 * 2 ^ (q - 1) := Nat.mul_comm _ _
    have h2qm1_pos : 1 ≤ 2 ^ (q - 1) := pow2_nat_pos (q - 1)
    have hsub_eq : 2 ^ q - 2 = 2 * (2 ^ (q - 1) - 1) := by rw [hpow_q]; omega
    rw [← hsub_eq]
    have h2mod : 2 % q = 2 := Nat.mod_eq_of_lt (by omega)
    rw [h2mod] at hflt
    have hdiv_step : 2 ^ q = q * (2 ^ q / q) + 2 := by
      have := (Nat.div_add_mod (2 ^ q) q).symm
      rw [hflt] at this; exact this
    exact ⟨2 ^ q / q, by omega⟩
  have h2qm1_dvd : q ∣ 2 ^ (q - 1) - 1 := by
    rcases prime_dvd_mul hq h2q_dvd with hq2 | hrest
    · have := Nat.le_of_dvd (by decide) hq2; omega
    · exact hrest
  have h2qm1_mod : 2 ^ (q - 1) % q = 1 := by
    have ⟨t, ht⟩ := h2qm1_dvd
    have hpos : 1 ≤ 2 ^ (q - 1) := pow2_nat_pos (q - 1)
    have heq : 2 ^ (q - 1) = q * t + 1 := by omega
    rw [heq, Nat.mul_add_mod]
    exact Nat.mod_eq_of_lt (by omega)
  -- Apply Euclidean exponent descent: 2^(gcd p (q - 1)) % q = 1
  have hgcd_mod : 2 ^ (Nat.gcd p (q - 1)) % q = 1 :=
    pow2_mod_gcd_eq_one q (by omega) (q - 1) p h2p_mod h2qm1_mod
  have hp_dvd : p ∣ q - 1 := by
    have hg_p : Nat.gcd p (q - 1) ∣ p := Nat.gcd_dvd_left p (q - 1)
    have hg_q : Nat.gcd p (q - 1) ∣ q - 1 := Nat.gcd_dvd_right p (q - 1)
    rcases hp.2 (Nat.gcd p (q - 1)) hg_p with h1 | hfull
    · rw [h1] at hgcd_mod
      have h21 : 2 ^ 1 = 2 := rfl
      rw [h21, Nat.mod_eq_of_lt (by omega : 2 < q)] at hgcd_mod
      omega
    · rw [hfull] at hg_q; exact hg_q
  -- Combine odd prime p ∣ (q - 1) with evenness 2 ∣ (q - 1) → 2 * p ∣ (q - 1)
  have hp_odd : p % 2 = 1 := prime_odd_ge_3 p hp hp3
  have ⟨k, hk⟩ := hp_dvd
  have hk_even : k % 2 = 0 := by
    by_cases hko : k % 2 = 1
    · have : (p * k) % 2 = 1 := by rw [Nat.mul_mod, hp_odd, hko]
      omega
    · omega
  refine ⟨k / 2, ?_⟩
  have hk2 : k = 2 * (k / 2) := by omega
  calc q - 1 = p * k := hk
  _ = p * (2 * (k / 2)) := by rw [← hk2]
  _ = 2 * p * (k / 2) := by ac_rfl

end FormalAtlas
