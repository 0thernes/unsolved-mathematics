module

-- SPDX-License-Identifier: MIT
public import FormalAtlas.Primes

/-!
# FormalAtlas.Goldbach — Finite Binary Goldbach (`4..100`) & Odd Parity Obstruction

Proves three structural theorems for Goldbach's Conjecture in pure Lean 4 Core:
  1. `goldbach_even_le_100`: Every even integer `4 ≤ n ≤ 100` is a sum of two primes.
  2. `goldbach_odd_binary_obstruction`: If an odd integer equals `p + q` with `p, q` prime,
     then `p = 2 ∨ q = 2`.
  3. `goldbach_binary_fails_at_11`: `11` cannot be written as the sum of two primes.

Explicit non-claim: proves NO resolution of Goldbach's Strong Conjecture (status: OPEN).
-/

namespace FormalAtlas

def findGoldbachPrime (n : Nat) : Nat → Option Nat
  | 0 => none
  | k + 1 =>
    if isPrimeBool (k + 1) && isPrimeBool (n - (k + 1)) && (k + 1) ≤ n then
      some (k + 1)
    else
      findGoldbachPrime n k

theorem findGoldbachPrime_sound (n : Nat) : ∀ k p : Nat,
    findGoldbachPrime n k = some p → IsPrime p ∧ IsPrime (n - p) ∧ p ≤ n := by
  intro k
  induction k with
  | zero => intro p h; simp [findGoldbachPrime] at h
  | succ m ih =>
    intro p h
    simp only [findGoldbachPrime] at h
    split at h
    · rename_i hcond
      injection h with hpeq
      subst hpeq
      simp only [Bool.and_eq_true, decide_eq_true_eq] at hcond
      exact ⟨isPrimeBool_sound _ hcond.1.1, isPrimeBool_sound _ hcond.1.2, hcond.2⟩
    · exact ih p h

def hasGoldbachBool (n : Nat) : Bool :=
  (findGoldbachPrime n n).isSome

theorem hasGoldbachBool_sound (n : Nat) (h : hasGoldbachBool n = true) :
    ∃ p q : Nat, IsPrime p ∧ IsPrime q ∧ p + q = n := by
  unfold hasGoldbachBool at h
  cases hopt : findGoldbachPrime n n with
  | none => rw [hopt] at h; cases h
  | some p =>
    have ⟨hp, hq, hle⟩ := findGoldbachPrime_sound n n p hopt
    exact ⟨p, n - p, hp, hq, by omega⟩

theorem goldbach_fin49 : ∀ k : Fin 49, hasGoldbachBool (2 * k.val + 4) = true := by
  decide

/-- **Finite Strong Goldbach (`4 ≤ n ≤ 100`):** every even `n ∈ [4, 100]` is `p + q` for primes `p, q`. -/
public theorem goldbach_even_le_100 (n : Nat) (hlo : 4 ≤ n) (hhi : n ≤ 100) (heven : n % 2 = 0) :
    ∃ p q : Nat, IsPrime p ∧ IsPrime q ∧ p + q = n := by
  have hk : (n - 4) / 2 < 49 := by omega
  have hb := goldbach_fin49 ⟨(n - 4) / 2, hk⟩
  have heq : 2 * ((n - 4) / 2) + 4 = n := by omega
  rw [heq] at hb
  exact hasGoldbachBool_sound n hb

/-- **Odd Binary Goldbach Obstruction:** if an odd integer equals `p + q` with `p, q` prime,
    then one of `p, q` must be `2`. -/
public theorem goldbach_odd_binary_obstruction (n p q : Nat)
    (hodd : n % 2 = 1) (hp : IsPrime p) (hq : IsPrime q) (hsum : p + q = n) :
    p = 2 ∨ q = 2 := by
  by_cases hp2 : p = 2
  · exact Or.inl hp2
  · by_cases hq2 : q = 2
    · exact Or.inr hq2
    · exfalso
      have hpo := prime_odd_ge_3 p hp (by have := hp.1; omega)
      have hqo := prime_odd_ge_3 q hq (by have := hq.1; omega)
      omega

/-- **Concrete Odd Binary Failure (`11`):** `11` is not the sum of two primes (since `9 = 3 × 3`). -/
public theorem goldbach_binary_fails_at_11 :
    ¬ (∃ p q : Nat, IsPrime p ∧ IsPrime q ∧ p + q = 11) := by
  intro ⟨p, q, hp, hq, hsum⟩
  have h2 := goldbach_odd_binary_obstruction 11 p q (by decide) hp hq hsum
  rcases h2 with rfl | rfl
  · have hq9 : q = 9 := by omega
    subst hq9
    have h3 : 3 ∣ 9 := ⟨3, rfl⟩
    have hc := hq.2 3 h3
    omega
  · have hp9 : p = 9 := by omega
    subst hp9
    have h3 : 3 ∣ 9 := ⟨3, rfl⟩
    have hc := hp.2 3 h3
    omega

end FormalAtlas
