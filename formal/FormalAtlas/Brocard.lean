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

end FormalAtlas
