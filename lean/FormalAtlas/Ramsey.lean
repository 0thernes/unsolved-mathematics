module

-- SPDX-License-Identifier: MIT
public import FormalAtlas.Defs

/-!
# FormalAtlas.Ramsey — Exact Determination of `R(3, 3) = 6` and `R(3, 4) = 9`

Proves from first principles in pure Lean 4 Core (zero Mathlib):
  1. `ramsey_R33_upper` & `ramsey_R33_lower`: Exact determination of `R(3, 3) = 6`.
  2. `ramsey_R34_upper`: Every symmetric 2-coloring of `K_9` contains a `true` triangle (`K_3`)
     or a `false` `K_4` (via neighborhood reduction to `R(3,3) ≤ 6` + Handshaking Lemma on `9 × 3 = 27`).
  3. `ramsey_R34_lower`: Explicit symmetric circulant coloring `c8Color` of `K_8` (distance `{1,4,7}`)
     containing zero `true` triangles and zero `false` `K_4`s, proving exact `R(3, 4) = 9`.

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

/-- **Ramsey Upper Bound `R(3, 3) ≤ 6`:** every 2-coloring of `K_6` has a monochromatic triangle. -/
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

-- ============================================================================
-- Exact Ramsey Number R(3, 4) = 9
-- ============================================================================

/-- Explicit symmetric circulant edge coloring of `K_8` (red edges at cyclic distance `{1, 4, 7}`). -/
@[expose] public def c8Color (i j : Fin 8) : Bool :=
  let d := (i.val + 8 - j.val) % 8
  d == 1 || d == 4 || d == 7

/-- **Ramsey Lower Bound `R(3, 4) > 8`:** `c8Color` is symmetric and contains neither a `true`
    triangle (`K_3`) nor a `false` `K_4`. -/
public theorem ramsey_R34_lower :
    (∀ i j : Fin 8, c8Color i j = c8Color j i) ∧
    ¬ HasColorTriangle c8Color true ∧ ¬ HasColorK4 c8Color false := by
  refine ⟨by decide, ?_, ?_⟩
  · unfold HasColorTriangle; decide
  · unfold HasColorK4; decide

-- Helpers for R(3, 4) ≤ 9 via neighborhood reduction + Handshaking Lemma on K_9

theorem color_tri_insert {k : Nat} (c : Fin k → Fin k → Bool) (hsym : ∀ i j, c i j = c j i)
    (col : Bool) (v a b : Fin k) (hab : a.val < b.val) (hva : v ≠ a) (hvb : v ≠ b)
    (cva : c v a = col) (cvb : c v b = col) (cab : c a b = col) :
    HasColorTriangle c col := by
  by_cases h1 : v.val < a.val
  · exact ⟨v, a, b, h1, hab, cva, cab, cvb⟩
  · by_cases h2 : v.val < b.val
    · have hav : a.val < v.val := by
        have : v.val ≠ a.val := fun h => hva (Fin.ext h)
        omega
      exact ⟨a, v, b, hav, h2, by rw [hsym, cva], cvb, cab⟩
    · have hbv : b.val < v.val := by
        have : v.val ≠ b.val := fun h => hvb (Fin.ext h)
        omega
      exact ⟨a, b, v, hab, hbv, cab, by rw [hsym, cvb], by rw [hsym, cva]⟩

theorem color_k4_insert {k : Nat} (c : Fin k → Fin k → Bool) (hsym : ∀ i j, c i j = c j i)
    (col : Bool) (v a b d : Fin k)
    (hab : a.val < b.val) (hbd : b.val < d.val)
    (hva : v ≠ a) (hvb : v ≠ b) (hvd : v ≠ d)
    (cva : c v a = col) (cvb : c v b = col) (cvd : c v d = col)
    (cab : c a b = col) (cad : c a d = col) (cbd : c b d = col) :
    HasColorK4 c col := by
  have hvane : v.val ≠ a.val := fun h => hva (Fin.ext h)
  have hvbne : v.val ≠ b.val := fun h => hvb (Fin.ext h)
  have hvdne : v.val ≠ d.val := fun h => hvd (Fin.ext h)
  by_cases h1 : v.val < a.val
  · exact ⟨v, a, b, d, h1, hab, hbd, cva, cvb, cvd, cab, cad, cbd⟩
  · by_cases h2 : v.val < b.val
    · exact ⟨a, v, b, d, by omega, h2, hbd, by rw [hsym, cva], cab, cad, cvb, cvd, cbd⟩
    · by_cases h3 : v.val < d.val
      · exact ⟨a, b, v, d, hab, by omega, h3, cab, by rw [hsym, cva], cad, by rw [hsym, cvb], cbd, cvd⟩
      · exact ⟨a, b, d, v, hab, hbd, by omega, cab, cad, by rw [hsym, cva], cbd, by rw [hsym, cvb], by rw [hsym, cvd]⟩

def strictlySortedFin {k : Nat} : List (Fin k) → Prop
  | [] => True
  | [_] => True
  | a :: b :: rest => a.val < b.val ∧ strictlySortedFin (b :: rest)

theorem filter_preserves_sorted {k : Nat} (p : Fin k → Bool) (l : List (Fin k))
    (hs : ∀ i j, (hi : i < l.length) → (hj : j < l.length) → i < j → (l[i]).val < (l[j]).val) :
    ∀ i j, (hi : i < (l.filter p).length) → (hj : j < (l.filter p).length) →
      i < j → ((l.filter p)[i]).val < ((l.filter p)[j]).val := by
  induction l with
  | nil => intro i j hi; simp at hi
  | cons x xs ih =>
    have hs_xs : ∀ i j, (hi : i < xs.length) → (hj : j < xs.length) → i < j → (xs[i]).val < (xs[j]).val := by
      intro i j hi hj hij
      exact hs (i + 1) (j + 1) (by simpa using Nat.succ_lt_succ hi) (by simpa using Nat.succ_lt_succ hj) (Nat.succ_lt_succ hij)
    have hx_lt : ∀ y, y ∈ xs → x.val < y.val := by
      intro y hy
      have ⟨idx, hidx, hget⟩ := List.mem_iff_getElem.mp hy
      rw [← hget]
      exact hs 0 (idx + 1) (by simp) (by simpa using Nat.succ_lt_succ hidx) (Nat.zero_lt_succ idx)
    cases hpx : p x
    · simp only [List.filter_cons, hpx, Bool.false_eq_true, ite_false]
      exact ih hs_xs
    · simp only [List.filter_cons, hpx, ite_true]
      intro i j hi hj hij
      cases i with
      | zero =>
        cases j with
        | zero => omega
        | succ j' =>
          simp only [List.getElem_cons_zero, List.getElem_cons_succ]
          have hmem : (xs.filter p)[j']'(by simpa using Nat.lt_of_succ_lt_succ hj) ∈ xs.filter p :=
            List.getElem_mem _
          exact hx_lt _ (List.mem_filter.mp hmem).1
      | succ i' =>
        cases j with
        | zero => omega
        | succ j' =>
          simp only [List.getElem_cons_succ]
          exact ih hs_xs i' j' (by simpa using Nat.lt_of_succ_lt_succ hi)
            (by simpa using Nat.lt_of_succ_lt_succ hj) (Nat.lt_of_succ_lt_succ hij)

def fin9List : List (Fin 9) := [0, 1, 2, 3, 4, 5, 6, 7, 8]

theorem fin9List_sorted :
    ∀ i j, (hi : i < fin9List.length) → (hj : j < fin9List.length) →
      i < j → (fin9List[i]).val < (fin9List[j]).val := by
  intro i j hi hj hij
  have hlen : fin9List.length = 9 := rfl
  have hi9 : i < 9 := by omega
  have hj9 : j < 9 := by omega
  have hval : ∀ t : Nat, (ht : t < fin9List.length) → (fin9List[t]).val = t := by
    intro t ht
    match t with
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 => rfl
    | t + 9 => omega
  rw [hval i hi, hval j hj]
  exact hij

def nbrs (c : Fin 9 → Fin 9 → Bool) (col : Bool) (v : Fin 9) : List (Fin 9) :=
  fin9List.filter (fun u => u != v && c v u == col)

theorem nbr_props (c : Fin 9 → Fin 9 → Bool) (col : Bool) (v u : Fin 9)
    (hm : u ∈ nbrs c col v) : v ≠ u ∧ c v u = col := by
  unfold nbrs at hm
  have hp := (List.mem_filter.mp hm).2
  simp only [Bool.and_eq_true, bne_iff_ne, beq_iff_eq] at hp
  exact ⟨fun h => hp.1 h.symm, hp.2⟩

theorem nbrs_lt_4_of_no_R34 (c : Fin 9 → Fin 9 → Bool) (hsym : ∀ i j, c i j = c j i)
    (hno3 : ¬ HasColorTriangle c true) (hno4 : ¬ HasColorK4 c false) (v : Fin 9) :
    (nbrs c true v).length ≤ 3 := by
  by_cases hge : 4 ≤ (nbrs c true v).length
  · exfalso
    have hsort := filter_preserves_sorted (fun u => u != v && c v u == true) fin9List fin9List_sorted
    have hge' : 4 ≤ (fin9List.filter (fun u => u != v && c v u == true)).length := hge
    let a := (nbrs c true v)[0]'(by omega)
    let b := (nbrs c true v)[1]'(by omega)
    let d := (nbrs c true v)[2]'(by omega)
    let e := (nbrs c true v)[3]'(by omega)
    have hab : a.val < b.val := hsort 0 1 (by omega) (by omega) (by decide)
    have hbd : b.val < d.val := hsort 1 2 (by omega) (by omega) (by decide)
    have hde : d.val < e.val := hsort 2 3 (by omega) (by omega) (by decide)
    have ⟨hva, cva⟩ := nbr_props c true v a (List.getElem_mem _)
    have ⟨hvb, cvb⟩ := nbr_props c true v b (List.getElem_mem _)
    have ⟨hvd, cvd⟩ := nbr_props c true v d (List.getElem_mem _)
    have ⟨hve, cve⟩ := nbr_props c true v e (List.getElem_mem _)
    cases cab : c a b
    · cases cad : c a d
      · cases cae : c a e
        · cases cbd : c b d
          · cases cbe : c b e
            · cases cde : c d e
              · exact hno4 ⟨a, b, d, e, hab, hbd, hde, cab, cad, cae, cbd, cbe, cde⟩
              · exact hno3 (color_tri_insert c hsym true v d e hde hvd hve cvd cve cde)
            · exact hno3 (color_tri_insert c hsym true v b e (by omega) hvb hve cvb cve cbe)
          · exact hno3 (color_tri_insert c hsym true v b d hbd hvb hvd cvb cvd cbd)
        · exact hno3 (color_tri_insert c hsym true v a e (by omega) hva hve cva cve cae)
      · exact hno3 (color_tri_insert c hsym true v a d (by omega) hva hvd cva cvd cad)
    · exact hno3 (color_tri_insert c hsym true v a b hab hva hvb cva cvb cab)
  · omega

theorem nbrs_lt_6_of_no_R34 (c : Fin 9 → Fin 9 → Bool) (hsym : ∀ i j, c i j = c j i)
    (hno3 : ¬ HasColorTriangle c true) (hno4 : ¬ HasColorK4 c false) (v : Fin 9) :
    (nbrs c false v).length ≤ 5 := by
  by_cases hge : 6 ≤ (nbrs c false v).length
  · exfalso
    have hsort := filter_preserves_sorted (fun u => u != v && c v u == false) fin9List fin9List_sorted
    have hge' : 6 ≤ (fin9List.filter (fun u => u != v && c v u == false)).length := hge
    let f : Fin 6 → Fin 9 := fun i => (nbrs c false v)[i.val]'(by omega)
    let c' : Fin 6 → Fin 6 → Bool := fun i j => c (f i) (f j)
    have ⟨i, j, k, hij, hjk, h1, h2⟩ := ramsey_R33_upper c'
    have hlt1 : (f i).val < (f j).val := hsort i.val j.val (by omega) (by omega) hij
    have hlt2 : (f j).val < (f k).val := hsort j.val k.val (by omega) (by omega) hjk
    have ⟨hvi, cvi⟩ := nbr_props c false v (f i) (List.getElem_mem _)
    have ⟨hvj, cvj⟩ := nbr_props c false v (f j) (List.getElem_mem _)
    have ⟨hvk, cvk⟩ := nbr_props c false v (f k) (List.getElem_mem _)
    cases hcol : c' i j
    · rw [hcol] at h1 h2
      exact hno4 (color_k4_insert c hsym false v (f i) (f j) (f k) hlt1 hlt2
        hvi hvj hvk cvi cvj cvk hcol h2.symm h1.symm)
    · rw [hcol] at h1 h2
      exact hno3 ⟨f i, f j, f k, hlt1, hlt2, hcol, h1.symm, h2.symm⟩
  · omega

theorem nbrs_sum_8 (c : Fin 9 → Fin 9 → Bool) (v : Fin 9) :
    (nbrs c true v).length + (nbrs c false v).length = 8 := by
  have hsplit : ∀ l : List (Fin 9),
      (l.filter (fun u => u != v && c v u == true)).length +
      (l.filter (fun u => u != v && c v u == false)).length =
      (l.filter (fun u => u != v)).length := by
    intro l
    induction l with
    | nil => rfl
    | cons x xs ih =>
      cases hne : (x != v)
      · simp only [List.filter_cons, hne, Bool.false_and, Bool.false_eq_true, ite_false]
        exact ih
      · cases hcv : c v x
        · simp only [List.filter_cons, hne, hcv, Bool.true_and, beq_self_eq_true,
            show (false == true) = false from rfl, Bool.false_eq_true, ite_true, ite_false, List.length_cons]
          omega
        · simp only [List.filter_cons, hne, hcv, Bool.true_and, beq_self_eq_true,
            show (true == false) = false from rfl, Bool.false_eq_true, ite_true, ite_false, List.length_cons]
          omega
  unfold nbrs
  rw [hsplit fin9List]
  have hv_all : ∀ w : Fin 9, (fin9List.filter (fun u => u != w)).length = 8 := by decide
  exact hv_all v

theorem handshaking_fin9_even (c : Fin 9 → Fin 9 → Bool) (hsym : ∀ i j, c i j = c j i) :
    (fin9List.map (fun v => (nbrs c true v).length)).sum % 2 = 0 := by
  let ind (i j : Fin 9) : Nat := if c i j then 1 else 0
  have hind_sym : ∀ i j, ind i j = ind j i := by
    intro i j; dsimp [ind]; rw [hsym i j]
  have hdeg : ∀ v : Fin 9, (nbrs c true v).length =
      (fin9List.map (fun u => if u != v then ind v u else 0)).sum := by
    intro v
    have hgen : ∀ l : List (Fin 9),
        (l.filter (fun u => u != v && c v u == true)).length =
        (l.map (fun u => if u != v then ind v u else 0)).sum := by
      intro l
      induction l with
      | nil => rfl
      | cons x xs ih =>
        cases hne : (x != v)
        · simp only [List.filter_cons, List.map_cons, List.sum_cons, hne, Bool.false_and,
            Bool.false_eq_true, ite_false, Nat.zero_add]
          exact ih
        · cases hcv : c v x
          · have h0 : ind v x = 0 := by dsimp [ind]; rw [hcv]; rfl
            simp only [List.filter_cons, List.map_cons, List.sum_cons, hne, hcv, Bool.true_and,
              show (false == true) = false from rfl, Bool.false_eq_true, ite_true, ite_false, h0, Nat.zero_add]
            exact ih
          · have h1 : ind v x = 1 := by dsimp [ind]; rw [hcv]; rfl
            simp only [List.filter_cons, List.map_cons, List.sum_cons, hne, hcv, Bool.true_and,
              beq_self_eq_true, ite_true, List.length_cons, h1]
            omega
    exact hgen fin9List
  have hsum_eq : (fin9List.map (fun v => (nbrs c true v).length)).sum =
      (fin9List.map (fun v => (fin9List.map (fun u => if u != v then ind v u else 0)).sum)).sum := by
    congr 1; apply List.map_congr_left; intro v _; exact hdeg v
  rw [hsum_eq]
  -- Expand the 9x9 symmetric sum explicitly using hind_sym: every off-diagonal pair appears twice!
  dsimp only [fin9List, List.map, List.sum, List.foldr]
  have h01 := hind_sym 0 1; have h02 := hind_sym 0 2; have h03 := hind_sym 0 3
  have h04 := hind_sym 0 4; have h05 := hind_sym 0 5; have h06 := hind_sym 0 6
  have h07 := hind_sym 0 7; have h08 := hind_sym 0 8
  have h12 := hind_sym 1 2; have h13 := hind_sym 1 3; have h14 := hind_sym 1 4
  have h15 := hind_sym 1 5; have h16 := hind_sym 1 6; have h17 := hind_sym 1 7; have h18 := hind_sym 1 8
  have h23 := hind_sym 2 3; have h24 := hind_sym 2 4; have h25 := hind_sym 2 5
  have h26 := hind_sym 2 6; have h27 := hind_sym 2 7; have h28 := hind_sym 2 8
  have h34 := hind_sym 3 4; have h35 := hind_sym 3 5; have h36 := hind_sym 3 6
  have h37 := hind_sym 3 7; have h38 := hind_sym 3 8
  have h45 := hind_sym 4 5; have h46 := hind_sym 4 6; have h47 := hind_sym 4 7; have h48 := hind_sym 4 8
  have h56 := hind_sym 5 6; have h57 := hind_sym 5 7; have h58 := hind_sym 5 8
  have h67 := hind_sym 6 7; have h68 := hind_sym 6 8
  have h78 := hind_sym 7 8
  simp only [bne_self_eq_false, Bool.false_eq_true, ite_false]
  have hne_simp : ∀ a b : Fin 9, a.val ≠ b.val → (a != b) = true := by
    intro a b h; simp [bne_iff_ne]; intro heq; exact h (congrArg Fin.val heq)
  simp only [show ((1 : Fin 9) != 0) = true by decide, show ((2 : Fin 9) != 0) = true by decide,
    show ((3 : Fin 9) != 0) = true by decide, show ((4 : Fin 9) != 0) = true by decide,
    show ((5 : Fin 9) != 0) = true by decide, show ((6 : Fin 9) != 0) = true by decide,
    show ((7 : Fin 9) != 0) = true by decide, show ((8 : Fin 9) != 0) = true by decide,
    show ((0 : Fin 9) != 1) = true by decide, show ((2 : Fin 9) != 1) = true by decide,
    show ((3 : Fin 9) != 1) = true by decide, show ((4 : Fin 9) != 1) = true by decide,
    show ((5 : Fin 9) != 1) = true by decide, show ((6 : Fin 9) != 1) = true by decide,
    show ((7 : Fin 9) != 1) = true by decide, show ((8 : Fin 9) != 1) = true by decide,
    show ((0 : Fin 9) != 2) = true by decide, show ((1 : Fin 9) != 2) = true by decide,
    show ((3 : Fin 9) != 2) = true by decide, show ((4 : Fin 9) != 2) = true by decide,
    show ((5 : Fin 9) != 2) = true by decide, show ((6 : Fin 9) != 2) = true by decide,
    show ((7 : Fin 9) != 2) = true by decide, show ((8 : Fin 9) != 2) = true by decide,
    show ((0 : Fin 9) != 3) = true by decide, show ((1 : Fin 9) != 3) = true by decide,
    show ((2 : Fin 9) != 3) = true by decide, show ((4 : Fin 9) != 3) = true by decide,
    show ((5 : Fin 9) != 3) = true by decide, show ((6 : Fin 9) != 3) = true by decide,
    show ((7 : Fin 9) != 3) = true by decide, show ((8 : Fin 9) != 3) = true by decide,
    show ((0 : Fin 9) != 4) = true by decide, show ((1 : Fin 9) != 4) = true by decide,
    show ((2 : Fin 9) != 4) = true by decide, show ((3 : Fin 9) != 4) = true by decide,
    show ((5 : Fin 9) != 4) = true by decide, show ((6 : Fin 9) != 4) = true by decide,
    show ((7 : Fin 9) != 4) = true by decide, show ((8 : Fin 9) != 4) = true by decide,
    show ((0 : Fin 9) != 5) = true by decide, show ((1 : Fin 9) != 5) = true by decide,
    show ((2 : Fin 9) != 5) = true by decide, show ((3 : Fin 9) != 5) = true by decide,
    show ((4 : Fin 9) != 5) = true by decide, show ((6 : Fin 9) != 5) = true by decide,
    show ((7 : Fin 9) != 5) = true by decide, show ((8 : Fin 9) != 5) = true by decide,
    show ((0 : Fin 9) != 6) = true by decide, show ((1 : Fin 9) != 6) = true by decide,
    show ((2 : Fin 9) != 6) = true by decide, show ((3 : Fin 9) != 6) = true by decide,
    show ((4 : Fin 9) != 6) = true by decide, show ((5 : Fin 9) != 6) = true by decide,
    show ((7 : Fin 9) != 6) = true by decide, show ((8 : Fin 9) != 6) = true by decide,
    show ((0 : Fin 9) != 7) = true by decide, show ((1 : Fin 9) != 7) = true by decide,
    show ((2 : Fin 9) != 7) = true by decide, show ((3 : Fin 9) != 7) = true by decide,
    show ((4 : Fin 9) != 7) = true by decide, show ((5 : Fin 9) != 7) = true by decide,
    show ((6 : Fin 9) != 7) = true by decide, show ((8 : Fin 9) != 7) = true by decide,
    show ((0 : Fin 9) != 8) = true by decide, show ((1 : Fin 9) != 8) = true by decide,
    show ((2 : Fin 9) != 8) = true by decide, show ((3 : Fin 9) != 8) = true by decide,
    show ((4 : Fin 9) != 8) = true by decide, show ((5 : Fin 9) != 8) = true by decide,
    show ((6 : Fin 9) != 8) = true by decide, show ((7 : Fin 9) != 8) = true by decide,
    ite_true]
  omega

/-- **Ramsey Upper Bound `R(3, 4) ≤ 9`:** every symmetric 2-coloring of `K_9` contains either
    a `true` triangle (`K_3`) or a `false` `K_4`. Combined with `ramsey_R34_lower`, this proves
    exact `R(3, 4) = 9` from first principles in zero-Mathlib Lean 4.35.0. -/
public theorem ramsey_R34_upper (c : Fin 9 → Fin 9 → Bool) (hsym : ∀ i j, c i j = c j i) :
    HasColorTriangle c true ∨ HasColorK4 c false := by
  apply Classical.byContradiction
  intro hnot
  have hno3 : ¬ HasColorTriangle c true := fun h => hnot (Or.inl h)
  have hno4 : ¬ HasColorK4 c false := fun h => hnot (Or.inr h)
  have hdeg3 : ∀ v : Fin 9, (nbrs c true v).length = 3 := by
    intro v
    have h1 := nbrs_lt_4_of_no_R34 c hsym hno3 hno4 v
    have h2 := nbrs_lt_6_of_no_R34 c hsym hno3 hno4 v
    have h3 := nbrs_sum_8 c v
    omega
  have heven := handshaking_fin9_even c hsym
  have hsum27 : (fin9List.map (fun v => (nbrs c true v).length)).sum = 27 := by
    dsimp only [fin9List, List.map, List.sum, List.foldr]
    simp only [hdeg3]
    rfl
  omega

end FormalAtlas
