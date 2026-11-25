module

public import FormalAtlas.Defs

/-!
# FormalAtlas.Brocard — Exact Verification of Brown Numbers & Exhaustive Check ≤ 12

Proves in pure Lean 4 (via kernel-checked arithmetic, zero `native_decide`):
  1. `brocard_brown_solutions`: `(4, 5)`, `(5, 11)`, and `(7, 71)` all satisfy `n! + 1 = m²`.
  2. `brocard_exhaustive_le_12`: For every `n ≤ 12` and every `m : Nat`,
     `n! + 1 = m²` implies `(n, m) ∈ {(4, 5), (5, 11), (7, 71)}`.

Explicit non-claim: proves NO finiteness result for Brocard's Problem (status: OPEN;
computational checks extend to `10^9`, and Overholt 1993 linked finiteness to the
abc conjecture).
-/

namespace FormalAtlas

/-- **Theorem 12a (Brown Number Solutions).**
    `4! + 1 = 5²`, `5! + 1 = 11²`, and `7! + 1 = 71²`. -/
public theorem brocard_brown_solutions :
    IsBrocardSol 4 5 ∧ IsBrocardSol 5 11 ∧ IsBrocardSol 7 71 := by
  unfold IsBrocardSol
  exact ⟨by decide, by decide, by decide⟩

/-- No square lies strictly between `k²` and `(k + 1)²`. -/
theorem no_square_between (k t m : Nat) (hlo : k * k < t) (hhi : t < (k + 1) * (k + 1)) :
    t ≠ m * m := by
  intro heq
  by_cases hm : m ≤ k
  · have : m * m ≤ k * k := Nat.mul_le_mul hm hm
    omega
  · have hm1 : k + 1 ≤ m := by omega
    have : (k + 1) * (k + 1) ≤ m * m := Nat.mul_le_mul hm1 hm1
    omega

/-- Unique square root on `Nat`: if `m² = r²`, then `m = r`. -/
theorem sq_eq_imp_eq (m r : Nat) (h : m * m = r * r) : m = r := by
  by_cases hlt : m < r
  · have : m * m < r * r := Nat.mul_lt_mul_of_lt_of_lt hlt hlt
    omega
  · by_cases hgt : r < m
    · have : r * r < m * m := Nat.mul_lt_mul_of_lt_of_lt hgt hgt
      omega
    · omega

/-- **Theorem 12b (Exhaustive Classification of Brocard Solutions for `n ≤ 12`).**
    For every `n ≤ 12` and every `m : Nat`, `n! + 1 = m²` implies
    `(n = 4 ∧ m = 5) ∨ (n = 5 ∧ m = 11) ∨ (n = 7 ∧ m = 71)`. -/
public theorem brocard_exhaustive_le_12 (n m : Nat) (hn : n ≤ 12) (h : IsBrocardSol n m) :
    (n = 4 ∧ m = 5) ∨ (n = 5 ∧ m = 11) ∨ (n = 7 ∧ m = 71) := by
  unfold IsBrocardSol at h
  match n with
  | 0 => exfalso; exact no_square_between 1 (fact 0 + 1) m (by decide) (by decide) h
  | 1 => exfalso; exact no_square_between 1 (fact 1 + 1) m (by decide) (by decide) h
  | 2 => exfalso; exact no_square_between 1 (fact 2 + 1) m (by decide) (by decide) h
  | 3 => exfalso; exact no_square_between 2 (fact 3 + 1) m (by decide) (by decide) h
  | 4 => left; exact ⟨rfl, sq_eq_imp_eq m 5 (by rw [← h]; decide)⟩
  | 5 => right; left; exact ⟨rfl, sq_eq_imp_eq m 11 (by rw [← h]; decide)⟩
  | 6 => exfalso; exact no_square_between 26 (fact 6 + 1) m (by decide) (by decide) h
  | 7 => right; right; exact ⟨rfl, sq_eq_imp_eq m 71 (by rw [← h]; decide)⟩
  | 8 => exfalso; exact no_square_between 200 (fact 8 + 1) m (by decide) (by decide) h
  | 9 => exfalso; exact no_square_between 602 (fact 9 + 1) m (by decide) (by decide) h
  | 10 => exfalso; exact no_square_between 1904 (fact 10 + 1) m (by decide) (by decide) h
  | 11 => exfalso; exact no_square_between 6317 (fact 11 + 1) m (by decide) (by decide) h
  | 12 => exfalso; exact no_square_between 21886 (fact 12 + 1) m (by decide) (by decide) h
  | n + 13 => omega

theorem fact_mod4_zero (n : Nat) (hn : 4 ≤ n) : fact n % 4 = 0 := by
  induction n with
  | zero => omega
  | succ k ih =>
    by_cases hk : k = 3
    · subst hk; decide
    · have hk4 : 4 ≤ k := by omega
      have h0 := ih hk4
      simp only [fact]
      rw [Nat.mul_mod, h0, Nat.mul_zero]

/-- **Theorem 21 (Brocard Mod-4 Structural Constraint).**
    For every `n ≥ 4`, `n! + 1 ≡ 1 (mod 4)`. Consequently, every Brown-number
    solution `(n, m)` with `n ≥ 4` must have odd `m`. -/
public theorem brocard_mod4_ge_4 (n : Nat) (hn : 4 ≤ n) :
    (fact n + 1) % 4 = 1 := by
  have h0 := fact_mod4_zero n hn
  omega

/-- **Theorem 22 (Exhaustive Classification of Brocard Solutions for `n ≤ 15`).**
    Extends `brocard_exhaustive_le_12` through `15! + 1 = 1,307,674,368,001` via
    kernel-checked square bracketing (`no_square_between`), confirming that
    `(4, 5)`, `(5, 11)`, and `(7, 71)` are the sole solutions for `n ≤ 15`. -/
public theorem brocard_exhaustive_le_15 (n m : Nat) (hn : n ≤ 15) (h : IsBrocardSol n m) :
    (n = 4 ∧ m = 5) ∨ (n = 5 ∧ m = 11) ∨ (n = 7 ∧ m = 71) := by
  by_cases h12 : n ≤ 12
  · exact brocard_exhaustive_le_12 n m h12 h
  · unfold IsBrocardSol at h
    match n with
    | 13 => exfalso; exact no_square_between 78911 (fact 13 + 1) m (by decide) (by decide) h
    | 14 => exfalso; exact no_square_between 295259 (fact 14 + 1) m (by decide) (by decide) h
    | 15 => exfalso; exact no_square_between 1143535 (fact 15 + 1) m (by decide) (by decide) h
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | _ + 16 => omega

end FormalAtlas
