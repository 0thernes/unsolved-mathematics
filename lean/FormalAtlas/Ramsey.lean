module

-- SPDX-License-Identifier: MIT
public import FormalAtlas.Defs

/-!
# FormalAtlas.Ramsey — Exact Determination of the Ramsey Number `R(3, 3) = 6`

Proves from first principles in pure Lean 4 Core (zero Mathlib):
  1. `ramsey_R33_upper`: Every symmetric 2-coloring of `K_6` contains a monochromatic triangle.
  2. `ramsey_R33_lower`: Explicit `C_5` symmetric 2-coloring of `K_5` containing zero monochromatic triangles.

Explicit non-claim: proves NO resolution of diagonal Ramsey asymptotics or `R(5, 5)` (status: OPEN).
-/

namespace FormalAtlas

theorem mono_tri_from_three (c : Fin 6 → Fin 6 → Bool) (col : Bool)
    (a b d : Fin 6) (h0a : (0 : Fin 6).val < a.val) (hab : a.val < b.val) (hbd : b.val < d.val)
    (ca : c 0 a = col) (cb : c 0 b = col) (cd : c 0 d = col) :
    HasMonoTriangle c := by
  by_cases h1 : c a b = col
  · exact ⟨0, a, b, h0a, hab, by rw [ca, h1], by rw [ca, cb]⟩
  · by_cases h2 : c a d = col
    · exact ⟨0, a, d, h0a, by omega, by rw [ca, h2], by rw [ca, cd]⟩
    · by_cases h3 : c b d = col
      · exact ⟨0, b, d, by omega, hbd, by rw [cb, h3], by rw [cb, cd]⟩
      · refine ⟨a, b, d, hab, hbd, ?_, ?_⟩
        · cases hab' : c a b <;> cases hbd' : c b d <;> cases col <;> simp_all
        · cases hab' : c a b <;> cases had' : c a d <;> cases col <;> simp_all

/-- **Ramsey Upper Bound `R(3, 3) ≤ 6`:** every symmetric 2-coloring of `K_6` has a monochromatic triangle. -/
public theorem ramsey_R33_upper (c : Fin 6 → Fin 6 → Bool) :
    HasMonoTriangle c := by
  cases h1 : c 0 1 <;> cases h2 : c 0 2 <;> cases h3 : c 0 3 <;> cases h4 : c 0 4 <;> cases h5 : c 0 5
  · exact mono_tri_from_three c false 1 2 3 (by decide) (by decide) (by decide) h1 h2 h3
  · exact mono_tri_from_three c false 1 2 3 (by decide) (by decide) (by decide) h1 h2 h3
  · exact mono_tri_from_three c false 1 2 3 (by decide) (by decide) (by decide) h1 h2 h3
  · exact mono_tri_from_three c false 1 2 3 (by decide) (by decide) (by decide) h1 h2 h3
  · exact mono_tri_from_three c false 1 2 4 (by decide) (by decide) (by decide) h1 h2 h4
  · exact mono_tri_from_three c false 1 2 4 (by decide) (by decide) (by decide) h1 h2 h4
  · exact mono_tri_from_three c false 1 2 5 (by decide) (by decide) (by decide) h1 h2 h5
  · exact mono_tri_from_three c true  3 4 5 (by decide) (by decide) (by decide) h3 h4 h5
  · exact mono_tri_from_three c false 1 3 4 (by decide) (by decide) (by decide) h1 h3 h4
  · exact mono_tri_from_three c false 1 3 4 (by decide) (by decide) (by decide) h1 h3 h4
  · exact mono_tri_from_three c false 1 3 5 (by decide) (by decide) (by decide) h1 h3 h5
  · exact mono_tri_from_three c true  2 4 5 (by decide) (by decide) (by decide) h2 h4 h5
  · exact mono_tri_from_three c false 1 4 5 (by decide) (by decide) (by decide) h1 h4 h5
  · exact mono_tri_from_three c true  2 3 5 (by decide) (by decide) (by decide) h2 h3 h5
  · exact mono_tri_from_three c true  2 3 4 (by decide) (by decide) (by decide) h2 h3 h4
  · exact mono_tri_from_three c true  2 3 4 (by decide) (by decide) (by decide) h2 h3 h4
  · exact mono_tri_from_three c false 2 3 4 (by decide) (by decide) (by decide) h2 h3 h4
  · exact mono_tri_from_three c false 2 3 4 (by decide) (by decide) (by decide) h2 h3 h4
  · exact mono_tri_from_three c false 2 3 5 (by decide) (by decide) (by decide) h2 h3 h5
  · exact mono_tri_from_three c true  1 4 5 (by decide) (by decide) (by decide) h1 h4 h5
  · exact mono_tri_from_three c false 2 4 5 (by decide) (by decide) (by decide) h2 h4 h5
  · exact mono_tri_from_three c true  1 3 5 (by decide) (by decide) (by decide) h1 h3 h5
  · exact mono_tri_from_three c true  1 3 4 (by decide) (by decide) (by decide) h1 h3 h4
  · exact mono_tri_from_three c true  1 3 4 (by decide) (by decide) (by decide) h1 h3 h4
  · exact mono_tri_from_three c false 3 4 5 (by decide) (by decide) (by decide) h3 h4 h5
  · exact mono_tri_from_three c true  1 2 5 (by decide) (by decide) (by decide) h1 h2 h5
  · exact mono_tri_from_three c true  1 2 4 (by decide) (by decide) (by decide) h1 h2 h4
  · exact mono_tri_from_three c true  1 2 4 (by decide) (by decide) (by decide) h1 h2 h4
  · exact mono_tri_from_three c true  1 2 3 (by decide) (by decide) (by decide) h1 h2 h3
  · exact mono_tri_from_three c true  1 2 3 (by decide) (by decide) (by decide) h1 h2 h3
  · exact mono_tri_from_three c true  1 2 3 (by decide) (by decide) (by decide) h1 h2 h3
  · exact mono_tri_from_three c true  1 2 3 (by decide) (by decide) (by decide) h1 h2 h3

/-- Explicit `C_5` edge coloring of `K_5`: edges of cyclic distance 1 or 4 are `true`,
    and edges of cyclic distance 2 or 3 are `false`. -/
@[expose] public def c5Color (i j : Fin 5) : Bool :=
  let d := (i.val + 5 - j.val) % 5
  d == 1 || d == 4

/-- **Ramsey Lower Bound `R(3, 3) > 5`:** `c5Color` is symmetric and has no monochromatic triangle. -/
public theorem ramsey_R33_lower :
    (∀ i j : Fin 5, c5Color i j = c5Color j i) ∧ ¬ HasMonoTriangle c5Color := by
  refine ⟨by decide, ?_⟩
  unfold HasMonoTriangle
  decide

end FormalAtlas
