module

-- SPDX-License-Identifier: MIT
public import FormalAtlas.Defs

/-!
# FormalAtlas.Primes — Euclid's Theorem, Arbitrary Prime Gaps & Twin-Prime Structure

Proves four foundational prime-distribution theorems in pure Lean 4 Core (zero Mathlib):
  1. `euclid_infinitely_many_primes`: For every `N : Nat`, there exists a prime `p > N`.
  2. `arbitrary_prime_gaps`: For every `k ≥ 1`, there exist `k` consecutive composite integers.
  3. `prime_odd_ge_3`: Every prime `p ≥ 3` is odd.
  4. `twin_prime_mod6`: Every twin-prime pair `(p, p + 2)` with `p ≥ 4` satisfies `p % 6 = 5`.

Explicit non-claim: proves NO resolution of the Twin Prime or Polignac conjectures (status: OPEN).
-/

namespace FormalAtlas

public theorem fact_pos (n : Nat) : 0 < fact n := by
  induction n with
  | zero => decide
  | succ k ih =>
    simp only [fact]
    exact Nat.mul_pos (Nat.succ_pos k) ih

public theorem dvd_fact_of_le (k n : Nat) (hk : 1 ≤ k) (hkn : k ≤ n) : k ∣ fact n := by
  induction n with
  | zero => omega
  | succ m ih =>
    simp only [fact]
    by_cases heq : k = m + 1
    · subst heq
      exact Nat.dvd_mul_right (m + 1) (fact m)
    · let ⟨q, hq⟩ := ih (by omega)
      exact ⟨(m + 1) * q, by rw [hq]; ac_rfl⟩

theorem exists_prime_dvd_aux : ∀ b m : Nat, m ≤ b → 2 ≤ m → ∃ p : Nat, IsPrime p ∧ p ∣ m := by
  intro b
  induction b with
  | zero => intro m hmb hm2; omega
  | succ b ih =>
    intro m hmb hm2
    by_cases hp : IsPrime m
    · exact ⟨m, hp, Nat.dvd_refl m⟩
    · have hex : ∃ d : Nat, d ∣ m ∧ d ≠ 1 ∧ d ≠ m := by
        apply Classical.byContradiction
        intro hno
        apply hp
        refine ⟨hm2, ?_⟩
        intro d hd
        apply Classical.byContradiction
        intro hne
        apply hno
        exact ⟨d, hd, fun h1 => hne (Or.inl h1), fun hm => hne (Or.inr hm)⟩
      have ⟨d, hdvd, hd1, hdm⟩ := hex
      have hd_pos : 0 < d := by
        cases d with
        | zero =>
          have ⟨q, hq⟩ := hdvd
          simp at hq
          omega
        | succ _ => exact Nat.succ_pos _
      have hd_le : d ≤ m := Nat.le_of_dvd (by omega) hdvd
      have ⟨p, hp_prime, hpd⟩ := ih d (by omega) (by omega)
      exact ⟨p, hp_prime, Nat.dvd_trans hpd hdvd⟩

public theorem exists_prime_dvd (m : Nat) (hm : 2 ≤ m) : ∃ p : Nat, IsPrime p ∧ p ∣ m :=
  exists_prime_dvd_aux m m (Nat.le_refl m) hm

/-- **Euclid's Theorem (Infinitude of Primes):** for every `N`, there exists a prime `p > N`. -/
public theorem euclid_infinitely_many_primes (N : Nat) :
    ∃ p : Nat, N < p ∧ IsPrime p := by
  have hf := fact_pos N
  have ⟨p, hp, hpdvd⟩ := exists_prime_dvd (fact N + 1) (by omega)
  refine ⟨p, ?_, hp⟩
  apply Classical.byContradiction
  intro hle
  have hple : p ≤ N := by omega
  have hp_fact : p ∣ fact N := dvd_fact_of_le p N (by have := hp.1; omega) hple
  have hp_one : p ∣ 1 := (Nat.dvd_add_right hp_fact).mp hpdvd
  have hp_le1 : p ≤ 1 := Nat.le_of_dvd (by decide) hp_one
  have := hp.1
  omega

/-- **Arbitrary Prime Gaps:** for every `k ≥ 1`, there exists `m ≥ 2` such that
    none of `m, m + 1, …, m + k - 1` is prime (`m = (k + 1)! + 2`). -/
public theorem arbitrary_prime_gaps (k : Nat) (_hk : 1 ≤ k) :
    ∃ m : Nat, 2 ≤ m ∧ ∀ i : Nat, i < k → ¬ IsPrime (m + i) := by
  refine ⟨fact (k + 1) + 2, by have := fact_pos (k + 1); omega, ?_⟩
  intro i hi hpr
  let d := i + 2
  have hd_fact : d ∣ fact (k + 1) := dvd_fact_of_le d (k + 1) (by omega) (by omega)
  have hsum : fact (k + 1) + 2 + i = fact (k + 1) + d := by omega
  have hd_dvd : d ∣ fact (k + 1) + 2 + i := by
    rw [hsum]
    exact Nat.dvd_add hd_fact (Nat.dvd_refl d)
  have hcases := hpr.2 d hd_dvd
  have hf := fact_pos (k + 1)
  omega

/-- **Oddness of Primes ≥ 3:** every prime `p ≥ 3` satisfies `p % 2 = 1`. -/
public theorem prime_odd_ge_3 (p : Nat) (hp : IsPrime p) (h3 : 3 ≤ p) :
    p % 2 = 1 := by
  by_cases h2 : p % 2 = 0
  · have hdvd : 2 ∣ p := Nat.dvd_of_mod_eq_zero h2
    have hcases := hp.2 2 hdvd
    omega
  · omega

/-- **Twin-Prime Mod-6 Structure:** every twin prime pair `(p, p + 2)` with `p ≥ 4`
    satisfies `p % 6 = 5` (equivalently `6 ∣ (p + 1)`). -/
public theorem twin_prime_mod6 (p : Nat) (hp : IsPrime p) (hp2 : IsPrime (p + 2)) (h4 : 4 ≤ p) :
    p % 6 = 5 := by
  have hodd : p % 2 = 1 := prime_odd_ge_3 p hp (by omega)
  have hnot3 : p % 3 ≠ 0 := by
    intro h0
    have hdvd : 3 ∣ p := Nat.dvd_of_mod_eq_zero h0
    have hcases := hp.2 3 hdvd
    omega
  have hnot3_2 : (p + 2) % 3 ≠ 0 := by
    intro h0
    have hdvd : 3 ∣ p + 2 := Nat.dvd_of_mod_eq_zero h0
    have hcases := hp2.2 3 hdvd
    omega
  have hp3 : p % 3 = 2 := by omega
  omega

-- Computable verified primality helper used by Goldbach & NonVacuity
@[expose] public def noDivLoop (p : Nat) : Nat → Bool
  | 0 => true
  | 1 => true
  | d + 2 => if p % (d + 2) == 0 then false else noDivLoop p (d + 1)

@[expose] public def isPrimeBool (p : Nat) : Bool :=
  if p < 2 then false else noDivLoop p (p - 1)

theorem noDivLoop_sound (p : Nat) : ∀ k : Nat, noDivLoop p k = true →
    ∀ d : Nat, 2 ≤ d → d ≤ k → p % d ≠ 0 := by
  intro k
  induction k with
  | zero => intro _ d hd hle; omega
  | succ m ih =>
    cases m with
    | zero => intro _ d hd hle; omega
    | succ r =>
      intro hok d hd hle
      simp only [noDivLoop] at hok
      split at hok
      · cases hok
      · rename_i hdiv
        by_cases heq : d = r + 2
        · subst heq
          intro hzero
          apply hdiv
          simp [hzero]
        · exact ih hok d hd (by omega)

public theorem isPrimeBool_sound (p : Nat) (h : isPrimeBool p = true) : IsPrime p := by
  unfold isPrimeBool at h
  split at h
  · cases h
  · rename_i hge
    refine ⟨by omega, ?_⟩
    intro d hdvd
    have hd_pos : 0 < d := by
      cases d with
      | zero =>
        have ⟨q, hq⟩ := hdvd; simp at hq; omega
      | succ _ => exact Nat.succ_pos _
    have hd_le : d ≤ p := Nat.le_of_dvd (by omega) hdvd
    by_cases h1 : d = 1
    · exact Or.inl h1
    · by_cases hp : d = p
      · exact Or.inr hp
      · exfalso
        have hnz := noDivLoop_sound p (p - 1) h d (by omega) (by omega)
        exact hnz (Nat.mod_eq_zero_of_dvd hdvd)

end FormalAtlas
