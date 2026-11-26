module

-- SPDX-License-Identifier: MIT
public import FormalAtlas.Primes

/-!
# FormalAtlas.PerfectNumbers — Mersenne Exponent Necessity & Perfect Numbers

Proves three structural theorems for the Odd Perfect Numbers (Rank #8) and
Mersenne Primes Infinitude (Rank #9) open problems in pure Lean 4 Core:
  1. `mersenne_exponent_prime`: If `2^n - 1` is prime (`n ≥ 2`), then `n` is prime.
  2. `perfect_numbers_first_four`: `6`, `28`, `496`, and `8128` are all perfect (`σ(n) = 2n`).
  3. `no_odd_perfect_le_100`: No odd integer `n ≤ 100` is perfect.

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

end FormalAtlas
