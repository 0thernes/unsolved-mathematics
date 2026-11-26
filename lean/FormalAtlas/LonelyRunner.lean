module

-- SPDX-License-Identifier: MIT
public import FormalAtlas.Defs

/-!
# FormalAtlas.LonelyRunner — Global Sharpness, Symmetries & Complete Proofs for `n ∈ {1, 2, 3}`

Proves structural & full finite-runner theorems for the Lonely Runner Conjecture in pure Lean 4 Core:
  1. `lonely_runner_sharpness_all_n`: For EVERY `n ≥ 1` and EVERY rational time `t = p / q`,
     speeds `{1, …, n}` admit some runner `i` with `‖t · i‖ ≤ 1 / (n + 1)`.
  2. `lonely_runner_n1` & `lonely_runner_n2`: Constructive proofs for `n = 1` (2 runners)
     and `n = 2` (3 runners).
  3. `lonely_runner_speed_scaling`, `lonely_runner_period_shift`, `lonely_runner_neg_time`:
     Exact scaling, period-1 shift, and time-reversal symmetries.
  4. `lonely_runner_n3_nondiv4`: `t = 1/4` for all non-divisible-by-4 triples.
  5. `lonely_runner_n3`: **COMPLETE constructive proof of the Lonely Runner Conjecture for
     `n = 3` (4 runners — ALL positive integer speed triples `v₁, v₂, v₃ > 0`)** via 2-adic
     descent, quarter-circle shift counting, Bézout congruence, and `n = 2` rational nudging.

Explicit non-claim: proves NO general uniform resolution for arbitrary `n`
(status: active-progress; verified through 13 runners in the 2025–2026 literature).
-/

namespace FormalAtlas

theorem pigeonhole_fin (m : Nat) (f : Fin (m + 1) → Fin m) :
    ∃ i j : Fin (m + 1), i.val < j.val ∧ f i = f j := by
  induction m with
  | zero => exact Fin.elim0 (f ⟨0, by omega⟩)
  | succ m ih =>
    by_cases hlast : ∃ i j : Fin (m + 2), i.val < j.val ∧ (f i).val = m ∧ (f j).val = m
    · have ⟨i, j, hij, hi, hj⟩ := hlast
      exact ⟨i, j, hij, Fin.ext (by omega)⟩
    · by_cases hex : ∃ a : Fin (m + 2), (f a).val = m
      · have ⟨a, ha⟩ := hex
        let skip : Fin (m + 1) → Fin (m + 2) := fun k =>
          if h : k.val < a.val then ⟨k.val, by omega⟩ else ⟨k.val + 1, by omega⟩
        have hskip_val : ∀ k : Fin (m + 1),
            (skip k).val = if k.val < a.val then k.val else k.val + 1 := by
          intro k
          dsimp [skip]
          split <;> rfl
        have hskip_ne : ∀ k : Fin (m + 1), skip k ≠ a := by
          intro k hk
          have hv := congrArg Fin.val hk
          rw [hskip_val] at hv
          split at hv <;> omega
        have hskip_lt : ∀ k1 k2 : Fin (m + 1), k1.val < k2.val → (skip k1).val < (skip k2).val := by
          intro k1 k2 hlt
          rw [hskip_val, hskip_val]
          split <;> split <;> omega
        have hnotm : ∀ k : Fin (m + 1), (f (skip k)).val < m := by
          intro k
          have hlt := (f (skip k)).isLt
          apply Classical.byContradiction
          intro hge
          have heq : (f (skip k)).val = m := by omega
          have hne := hskip_ne k
          apply hlast
          by_cases hord : (skip k).val < a.val
          · exact ⟨skip k, a, hord, heq, ha⟩
          · have hgt : a.val < (skip k).val := by
              have : (skip k).val ≠ a.val := fun h => hne (Fin.ext h)
              omega
            exact ⟨a, skip k, hgt, ha, heq⟩
        let g : Fin (m + 1) → Fin m := fun k => ⟨(f (skip k)).val, hnotm k⟩
        have ⟨k1, k2, hlt, hgeq⟩ := ih g
        refine ⟨skip k1, skip k2, hskip_lt k1 k2 hlt, Fin.ext ?_⟩
        exact congrArg (fun x : Fin m => x.val) hgeq
      · have hnotm : ∀ k : Fin (m + 1), (f ⟨k.val, by omega⟩).val < m := by
          intro k
          have hlt := (f ⟨k.val, by omega⟩).isLt
          apply Classical.byContradiction
          intro hge
          exact hex ⟨⟨k.val, by omega⟩, by omega⟩
        let g : Fin (m + 1) → Fin m := fun k => ⟨(f ⟨k.val, by omega⟩).val, hnotm k⟩
        have ⟨k1, k2, hlt, hgeq⟩ := ih g
        refine ⟨⟨k1.val, by omega⟩, ⟨k2.val, by omega⟩, hlt, Fin.ext ?_⟩
        exact congrArg (fun x : Fin m => x.val) hgeq

theorem ediv_bounds (a q : Int) (hq : 0 < q) :
    (a / q) * q ≤ a ∧ a < (a / q + 1) * q := by
  have hde := Int.mul_ediv_add_emod a q
  have hmod0 : 0 ≤ a % q := Int.emod_nonneg a (by omega)
  have hmodq : a % q < q := Int.emod_lt_of_pos a hq
  rw [Int.mul_comm] at hde
  rw [Int.add_mul, Int.one_mul]
  omega

/-- **Theorem 10 (Global Sharpness of the Lonely Runner Constant `1 / (n + 1)`).** -/
public theorem lonely_runner_sharpness_all_n (n : Nat) (hn : 1 ≤ n) (p q : Int) (hq : 0 < q) :
    ∃ i : Nat, 1 ≤ i ∧ i ≤ n ∧ WithinDist ((n : Int) + 1) p q (i : Int) := by
  by_cases hhit : ∃ i : Nat, 1 ≤ i ∧ i ≤ n ∧ WithinDist ((n : Int) + 1) p q (i : Int)
  · exact hhit
  · exfalso
    have hbucket : ∀ k : Fin n,
        1 ≤ (((n : Int) + 1) * ((p * ((k.val + 1 : Nat) : Int)) % q)) / q ∧
        (((n : Int) + 1) * ((p * ((k.val + 1 : Nat) : Int)) % q)) / q < (n : Int) := by
      intro k
      have hnot : ¬ WithinDist ((n : Int) + 1) p q ((k.val + 1 : Nat) : Int) := fun hw =>
        hhit ⟨k.val + 1, by omega, by omega, hw⟩
      unfold WithinDist at hnot
      have h1 : q < ((n : Int) + 1) * ((p * ((k.val + 1 : Nat) : Int)) % q) := by
        apply Classical.byContradiction
        intro hle; apply hnot; left; omega
      have h2 : q < ((n : Int) + 1) * (q - (p * ((k.val + 1 : Nat) : Int)) % q) := by
        apply Classical.byContradiction
        intro hle; apply hnot; right; omega
      have hmr_lt : ((n : Int) + 1) * ((p * ((k.val + 1 : Nat) : Int)) % q) < (n : Int) * q := by
        have hsub : ((n : Int) + 1) * (q - (p * ((k.val + 1 : Nat) : Int)) % q) =
            ((n : Int) + 1) * q - ((n : Int) + 1) * ((p * ((k.val + 1 : Nat) : Int)) % q) :=
          Int.mul_sub _ _ _
        have hmq : ((n : Int) + 1) * q = (n : Int) * q + q := by
          rw [Int.add_mul, Int.one_mul]
        omega
      constructor
      · have hle1 : 1 * q ≤ ((n : Int) + 1) * ((p * ((k.val + 1 : Nat) : Int)) % q) := by omega
        have hdiv := Int.ediv_le_ediv hq hle1
        rw [Int.mul_ediv_cancel 1 (by omega)] at hdiv
        exact hdiv
      · apply Classical.byContradiction
        intro hge
        have hge' : (n : Int) ≤ (((n : Int) + 1) * ((p * ((k.val + 1 : Nat) : Int)) % q)) / q := by
          omega
        have hmul := Int.mul_le_mul_of_nonneg_right hge' (by omega : (0 : Int) ≤ q)
        have hlo := (ediv_bounds (((n : Int) + 1) * ((p * ((k.val + 1 : Nat) : Int)) % q)) q hq).1
        omega
    let f : Fin ((n - 1) + 1) → Fin (n - 1) := fun k =>
      let k' : Fin n := ⟨k.val, by omega⟩
      have hb := hbucket k'
      ⟨((((n : Int) + 1) * ((p * ((k'.val + 1 : Nat) : Int)) % q)) / q - 1).toNat, by omega⟩
    have ⟨k1, k2, hlt, hfeq⟩ := pigeonhole_fin (n - 1) f
    have hb1 := hbucket ⟨k1.val, by omega⟩
    have hb2 := hbucket ⟨k2.val, by omega⟩
    have hbeq :
        (((n : Int) + 1) * ((p * ((k1.val + 1 : Nat) : Int)) % q)) / q =
        (((n : Int) + 1) * ((p * ((k2.val + 1 : Nat) : Int)) % q)) / q := by
      have hval := congrArg (fun x : Fin (n - 1) => x.val) hfeq
      dsimp only [f] at hval
      dsimp only at hb1 hb2 hval
      omega
    have ⟨hr1_lo, hr1_hi⟩ := ediv_bounds (((n : Int) + 1) * ((p * ((k1.val + 1 : Nat) : Int)) % q)) q hq
    have ⟨hr2_lo, hr2_hi⟩ := ediv_bounds (((n : Int) + 1) * ((p * ((k2.val + 1 : Nat) : Int)) % q)) q hq
    rw [← hbeq] at hr2_lo hr2_hi
    have hstep_q :
        ((((n : Int) + 1) * ((p * ((k1.val + 1 : Nat) : Int)) % q)) / q + 1) * q =
        ((((n : Int) + 1) * ((p * ((k1.val + 1 : Nat) : Int)) % q)) / q) * q + q := by
      rw [Int.add_mul, Int.one_mul]
    rw [hstep_q] at hr1_hi hr2_hi
    have hdiff_hi :
        ((n : Int) + 1) * (((p * ((k2.val + 1 : Nat) : Int)) % q) -
                           ((p * ((k1.val + 1 : Nat) : Int)) % q)) < q := by
      rw [Int.mul_sub]; omega
    have hdiff_lo :
        -q < ((n : Int) + 1) * (((p * ((k2.val + 1 : Nat) : Int)) % q) -
                                ((p * ((k1.val + 1 : Nat) : Int)) % q)) := by
      rw [Int.mul_sub]; omega
    let d : Nat := (k2.val + 1) - (k1.val + 1)
    have hpd : (p * (d : Int)) % q =
        (((p * ((k2.val + 1 : Nat) : Int)) % q) -
         ((p * ((k1.val + 1 : Nat) : Int)) % q)) % q := by
      have hdeq : (d : Int) = ((k2.val + 1 : Nat) : Int) - ((k1.val + 1 : Nat) : Int) := by omega
      rw [hdeq, Int.mul_sub, Int.sub_emod]
    have hr1_0 : 0 ≤ (p * ((k1.val + 1 : Nat) : Int)) % q := Int.emod_nonneg _ (by omega)
    have hr1_q : (p * ((k1.val + 1 : Nat) : Int)) % q < q := Int.emod_lt_of_pos _ hq
    have hr2_0 : 0 ≤ (p * ((k2.val + 1 : Nat) : Int)) % q := Int.emod_nonneg _ (by omega)
    have hr2_q : (p * ((k2.val + 1 : Nat) : Int)) % q < q := Int.emod_lt_of_pos _ hq
    apply hhit
    refine ⟨d, by omega, by omega, ?_⟩
    unfold WithinDist
    rw [hpd]
    by_cases hge : (p * ((k1.val + 1 : Nat) : Int)) % q ≤ (p * ((k2.val + 1 : Nat) : Int)) % q
    · left
      have hmod : (((p * ((k2.val + 1 : Nat) : Int)) % q) -
                   ((p * ((k1.val + 1 : Nat) : Int)) % q)) % q =
                  ((p * ((k2.val + 1 : Nat) : Int)) % q) -
                  ((p * ((k1.val + 1 : Nat) : Int)) % q) :=
        Int.emod_eq_of_lt (by omega) (by omega)
      rw [hmod]; omega
    · right
      have hmod : (((p * ((k2.val + 1 : Nat) : Int)) % q) -
                   ((p * ((k1.val + 1 : Nat) : Int)) % q)) % q =
                  ((p * ((k2.val + 1 : Nat) : Int)) % q) -
                  ((p * ((k1.val + 1 : Nat) : Int)) % q) + q := by
        have h1 : (((p * ((k2.val + 1 : Nat) : Int)) % q) -
                   ((p * ((k1.val + 1 : Nat) : Int)) % q) + q) % q =
                  (((p * ((k2.val + 1 : Nat) : Int)) % q) -
                   ((p * ((k1.val + 1 : Nat) : Int)) % q)) % q :=
          Int.add_emod_right _ _
        rw [← h1]
        exact Int.emod_eq_of_lt (by omega) (by omega)
      rw [hmod]
      have hneg :
          q - (((p * ((k2.val + 1 : Nat) : Int)) % q) -
               ((p * ((k1.val + 1 : Nat) : Int)) % q) + q) =
          -(((p * ((k2.val + 1 : Nat) : Int)) % q) -
            ((p * ((k1.val + 1 : Nat) : Int)) % q)) := by omega
      rw [hneg, Int.mul_neg]
      omega

/-- **Theorem 11a (Lonely Runner Conjecture, `n = 1` / 2 runners).** -/
public theorem lonely_runner_n1 (v : Int) (hv : 0 < v) :
    ∃ p q : Int, 0 < q ∧ FarEnough 2 p q v := by
  refine ⟨1, 2 * v, by omega, ?_⟩
  unfold FarEnough
  have hmod : (1 * v) % (2 * v) = v := by
    rw [Int.one_mul]
    exact Int.emod_eq_of_lt (by omega) (by omega)
  rw [hmod]
  omega

/-- **Theorem 11b (Lonely Runner Conjecture, `n = 2` / 3 runners).** -/
public theorem lonely_runner_n2 (v1 v2 : Int) (hv1 : 0 < v1) (hv2 : 0 < v2) :
    ∃ p q : Int, 0 < q ∧ FarEnough 3 p q v1 ∧ FarEnough 3 p q v2 := by
  have hordered : ∀ a b : Int, 0 < a → a ≤ b →
      ∃ p q : Int, 0 < q ∧ FarEnough 3 p q a ∧ FarEnough 3 p q b := by
    intro a b ha hab
    by_cases hclose : b ≤ 2 * a
    · refine ⟨1, a + b, by omega, ?_, ?_⟩
      · unfold FarEnough
        have hma : (1 * a) % (a + b) = a := by
          rw [Int.one_mul]; exact Int.emod_eq_of_lt (by omega) (by omega)
        rw [hma]; omega
      · unfold FarEnough
        have hmb : (1 * b) % (a + b) = b := by
          rw [Int.one_mul]; exact Int.emod_eq_of_lt (by omega) (by omega)
        rw [hmb]; omega
    · have hdiv : (3 * a) * (b / (3 * a)) + (b % (3 * a)) = b := Int.mul_ediv_add_emod b (3 * a)
      have hr0 : 0 ≤ b % (3 * a) := Int.emod_nonneg _ (by omega)
      have hrlt : b % (3 * a) < 3 * a := Int.emod_lt_of_pos _ (by omega)
      by_cases hmid : a ≤ b % (3 * a) ∧ b % (3 * a) ≤ 2 * a
      · refine ⟨1, 3 * a, by omega, ?_, ?_⟩
        · unfold FarEnough
          have hma : (1 * a) % (3 * a) = a := by
            rw [Int.one_mul]; exact Int.emod_eq_of_lt (by omega) (by omega)
          rw [hma]; omega
        · unfold FarEnough
          have hmb : (1 * b) % (3 * a) = b % (3 * a) := by rw [Int.one_mul]
          rw [hmb]; omega
      · by_cases hlo : b % (3 * a) < a
        · refine ⟨3 * (b / (3 * a)) + 1, 3 * b, by omega, ?_, ?_⟩
          · unfold FarEnough
            have hnum : (3 * (b / (3 * a)) + 1) * a = (3 * a) * (b / (3 * a)) + a := by
              rw [Int.add_mul, Int.one_mul, Int.mul_right_comm]
            have hma : ((3 * (b / (3 * a)) + 1) * a) % (3 * b) = (3 * a) * (b / (3 * a)) + a := by
              rw [hnum]
              exact Int.emod_eq_of_lt (by omega) (by omega)
            rw [hma]; omega
          · unfold FarEnough
            have hmb : ((3 * (b / (3 * a)) + 1) * b) % (3 * b) = b := by
              have : (3 * (b / (3 * a)) + 1) * b = (b / (3 * a)) * (3 * b) + b := by
                rw [Int.add_mul, Int.one_mul, Int.mul_assoc, Int.mul_left_comm 3 (b / (3 * a)) b]
              rw [this, Int.mul_add_emod_self_right]
              exact Int.emod_eq_of_lt (by omega) (by omega)
            rw [hmb]; omega
        · refine ⟨3 * (b / (3 * a)) + 4, 3 * b, by omega, ?_, ?_⟩
          · unfold FarEnough
            have hnum : (3 * (b / (3 * a)) + 4) * a = (3 * a) * (b / (3 * a)) + 4 * a := by
              rw [Int.add_mul, Int.mul_right_comm]
            have hma : ((3 * (b / (3 * a)) + 4) * a) % (3 * b) = (3 * a) * (b / (3 * a)) + 4 * a := by
              rw [hnum]
              exact Int.emod_eq_of_lt (by omega) (by omega)
            rw [hma]; omega
          · unfold FarEnough
            have hmb : ((3 * (b / (3 * a)) + 4) * b) % (3 * b) = b := by
              have : (3 * (b / (3 * a)) + 4) * b = ((b / (3 * a)) + 1) * (3 * b) + b := by
                rw [Int.add_mul, Int.add_mul, Int.one_mul, Int.mul_assoc,
                    Int.mul_left_comm 3 (b / (3 * a)) b]
                omega
              rw [this, Int.mul_add_emod_self_right]
              exact Int.emod_eq_of_lt (by omega) (by omega)
            rw [hmb]; omega
  by_cases hle : v1 ≤ v2
  · exact hordered v1 v2 hv1 hle
  · have ⟨p, q, hq, h2, h1⟩ := hordered v2 v1 hv2 (by omega)
    exact ⟨p, q, hq, h1, h2⟩

/-- **Theorem 20 (Exact Rational Speed-Scaling Invariance).** -/
public theorem lonely_runner_speed_scaling (m p q v k : Int)
    (hq : 0 < q) (hk : 0 < k) (h : FarEnough m p q v) :
    FarEnough m p (q * k) (v * k) := by
  unfold FarEnough at h ⊢
  have hde := Int.mul_ediv_add_emod (p * v) q
  have hr0 : 0 ≤ (p * v) % q := Int.emod_nonneg _ (by omega)
  have hrq : (p * v) % q < q := Int.emod_lt_of_pos _ hq
  have hmod_scale : (p * (v * k)) % (q * k) = ((p * v) % q) * k := by
    have hmul : p * (v * k) = (q * k) * ((p * v) / q) + ((p * v) % q) * k := by
      calc p * (v * k)
          = (p * v) * k := by rw [Int.mul_assoc]
      _   = (q * ((p * v) / q) + (p * v) % q) * k := by rw [hde]
      _   = (q * ((p * v) / q)) * k + ((p * v) % q) * k := Int.add_mul _ _ _
      _   = (q * k) * ((p * v) / q) + ((p * v) % q) * k := by
            rw [Int.mul_right_comm q ((p * v) / q) k]
    rw [hmul, Int.mul_add_emod_self_left]
    have hlo : 0 ≤ ((p * v) % q) * k := Int.mul_nonneg hr0 (by omega)
    have hhi : ((p * v) % q) * k < q * k := Int.mul_lt_mul_of_pos_right hrq hk
    exact Int.emod_eq_of_lt hlo hhi
  rw [hmod_scale]
  have ⟨h1, h2⟩ := h
  constructor
  · have h1k := Int.mul_le_mul_of_nonneg_right h1 (by omega : (0 : Int) ≤ k)
    rw [Int.mul_assoc] at h1k
    exact h1k
  · have h2k := Int.mul_le_mul_of_nonneg_right h2 (by omega : (0 : Int) ≤ k)
    rw [Int.mul_assoc, Int.sub_mul] at h2k
    exact h2k

/-- **Time-periodicity mod 1:** shifting `p/q` by `+1` preserves `FarEnough`. -/
public theorem lonely_runner_period_shift (m p q v : Int) (h : FarEnough m p q v) :
    FarEnough m (p + q) q v := by
  unfold FarEnough at h ⊢
  have hmod : ((p + q) * v) % q = (p * v) % q := by
    rw [Int.add_mul, Int.add_comm, Int.mul_add_emod_self_left]
  rw [hmod]
  exact h

/-- **Time-reversal symmetry (`t ↦ -t`):** `FarEnough m p q v` implies `FarEnough m (-p) q v`. -/
public theorem lonely_runner_neg_time (m p q v : Int) (hq : 0 < q) (h : FarEnough m p q v) :
    FarEnough m (-p) q v := by
  unfold FarEnough at h ⊢
  have ⟨h1, h2⟩ := h
  have hr0 : 0 ≤ (p * v) % q := Int.emod_nonneg _ (by omega)
  have hrq : (p * v) % q < q := Int.emod_lt_of_pos _ hq
  by_cases hz : (p * v) % q = 0
  · rw [hz] at h1; omega
  · have hneg : ((-p) * v) % q = q - (p * v) % q := by
      have hde := Int.mul_ediv_add_emod (p * v) q
      have hrew : (-p) * v = q * (-( (p * v) / q ) - 1) + (q - (p * v) % q) := by
        rw [Int.neg_mul, Int.mul_sub, Int.mul_neg, Int.mul_one]
        omega
      rw [hrew, Int.mul_add_emod_self_left]
      exact Int.emod_eq_of_lt (by omega) (by omega)
    rw [hneg]
    dsimp only
    have hsub : q - (q - (p * v) % q) = (p * v) % q := by omega
    rw [hsub]
    exact ⟨h2, h1⟩

/-- **Lonely Runner `n = 3` (4 runners) across all non-divisible-by-4 speed triples.** -/
public theorem lonely_runner_n3_nondiv4 (v1 v2 v3 : Int)
    (h1 : v1 % 4 ≠ 0) (h2 : v2 % 4 ≠ 0) (h3 : v3 % 4 ≠ 0) :
    ∃ p q : Int, 0 < q ∧ FarEnough 4 p q v1 ∧ FarEnough 4 p q v2 ∧ FarEnough 4 p q v3 := by
  refine ⟨1, 4, by omega, ?_, ?_, ?_⟩
  · unfold FarEnough; rw [Int.one_mul]; have := Int.emod_nonneg v1 (by omega : (4 : Int) ≠ 0); have := Int.emod_lt_of_pos v1 (by omega : (0 : Int) < 4); omega
  · unfold FarEnough; rw [Int.one_mul]; have := Int.emod_nonneg v2 (by omega : (4 : Int) ≠ 0); have := Int.emod_lt_of_pos v2 (by omega : (0 : Int) < 4); omega
  · unfold FarEnough; rw [Int.one_mul]; have := Int.emod_nonneg v3 (by omega : (4 : Int) ≠ 0); have := Int.emod_lt_of_pos v3 (by omega : (0 : Int) < 4); omega

-- ============================================================================
-- COMPLETE Constructive Proof of the Lonely Runner Conjecture for n = 3 (4 Runners)
-- ============================================================================

theorem farEnough_3_to_4 (p q v : Int) (hq : 0 < q) (h : FarEnough 3 p q v) :
    FarEnough 4 p q v := by
  unfold FarEnough at h ⊢
  have hr0 : 0 ≤ (p * v) % q := Int.emod_nonneg _ (by omega)
  have hrq : (p * v) % q < q := Int.emod_lt_of_pos _ hq
  omega

/-- Quarter-circle shift `t ↦ t + k / 4` leaves any speed `v` with `4 ∣ v` invariant. -/
theorem quarter_shift_div4 (p q v k : Int) (hq : 0 < q) (hdiv : v % 4 = 0)
    (h : FarEnough 4 p q v) :
    FarEnough 4 (4 * p + k * q) (4 * q) v := by
  unfold FarEnough at h ⊢
  have hde := Int.mul_ediv_add_emod (p * v) q
  have hr0 : 0 ≤ (p * v) % q := Int.emod_nonneg _ (by omega)
  have hrq : (p * v) % q < q := Int.emod_lt_of_pos _ hq
  have hv4 : 4 * (v / 4) = v := by
    have := Int.mul_ediv_add_emod v 4; omega
  have hkv : k * q * v = (4 * q) * (k * (v / 4)) := by
    calc k * q * v
        = k * q * (4 * (v / 4)) := by rw [hv4]
    _   = (4 * q) * (k * (v / 4)) := by
          rw [Int.mul_assoc k q, Int.mul_left_comm q 4, ← Int.mul_assoc k 4,
              Int.mul_comm k 4, Int.mul_assoc 4 k, Int.mul_left_comm k q, ← Int.mul_assoc 4 q]
  have hnum : (4 * p + k * q) * v = (4 * q) * ((p * v) / q + k * (v / 4)) + 4 * ((p * v) % q) := by
    calc (4 * p + k * q) * v
        = 4 * (p * v) + k * q * v := by rw [Int.add_mul, Int.mul_assoc]
    _   = 4 * (q * ((p * v) / q) + (p * v) % q) + (4 * q) * (k * (v / 4)) := by rw [hde, hkv]
    _   = (4 * q) * ((p * v) / q) + 4 * ((p * v) % q) + (4 * q) * (k * (v / 4)) := by
          rw [Int.mul_add, ← Int.mul_assoc 4 q]
    _   = (4 * q) * ((p * v) / q + k * (v / 4)) + 4 * ((p * v) % q) := by
          rw [Int.mul_add]; omega
  rw [hnum, Int.mul_add_emod_self_left, Int.emod_eq_of_lt (by omega) (by omega)]
  omega

/-- Exact formula for `((4 * p + k * q) * u) % (4 * q)` in terms of `r = (p * u) % q` and `u % 4`. -/
theorem quarter_shift_rem (p q u k : Int) :
    ((4 * p + k * q) * u) % (4 * q) = (4 * ((p * u) % q) + (k * (u % 4)) * q) % (4 * q) := by
  have hde := Int.mul_ediv_add_emod (p * u) q
  have hu4 := Int.mul_ediv_add_emod u 4
  have hnum : (4 * p + k * q) * u =
      (4 * q) * ((p * u) / q + k * (u / 4)) + (4 * ((p * u) % q) + (k * (u % 4)) * q) := by
    calc (4 * p + k * q) * u
        = 4 * (p * u) + k * q * u := by rw [Int.add_mul, Int.mul_assoc]
    _   = 4 * (q * ((p * u) / q) + (p * u) % q) + k * q * (4 * (u / 4) + u % 4) := by
          rw [hde, hu4]
    _   = (4 * q) * ((p * u) / q) + 4 * ((p * u) % q) +
          ((4 * q) * (k * (u / 4)) + (k * (u % 4)) * q) := by
          rw [Int.mul_add, Int.mul_add, ← Int.mul_assoc 4 q,
              show k * q * (4 * (u / 4)) = (4 * q) * (k * (u / 4)) by
                rw [Int.mul_assoc k q, Int.mul_left_comm q 4, ← Int.mul_assoc k 4,
                    Int.mul_comm k 4, Int.mul_assoc 4 k, Int.mul_left_comm k q, ← Int.mul_assoc 4 q],
              show k * q * (u % 4) = (k * (u % 4)) * q by rw [Int.mul_right_comm]]
    _   = (4 * q) * ((p * u) / q + k * (u / 4)) + (4 * ((p * u) % q) + (k * (u % 4)) * q) := by
          rw [Int.mul_add]; omega
  rw [hnum, Int.mul_add_emod_self_left]

/-- Exact quarter-circle goodness predicate `q ≤ rem ≤ 3q` for `rem = (4r + j*q) % (4q)`. -/
def qGood (q r j : Int) : Prop :=
  let rem := (4 * r + j * q) % (4 * q)
  q ≤ rem ∧ rem ≤ 3 * q

theorem farEnough_of_qGood (p q u k : Int)
    (h : qGood q ((p * u) % q) (k * (u % 4))) :
    FarEnough 4 (4 * p + k * q) (4 * q) u := by
  unfold FarEnough
  rw [quarter_shift_rem p q u k]
  unfold qGood at h
  omega

theorem qGood_mod4 (q r j1 j2 : Int) (hmod : j1 % 4 = j2 % 4) :
    qGood q r j1 ↔ qGood q r j2 := by
  have hdvd : ∃ t : Int, j1 - j2 = 4 * t := by
    have h1 := Int.mul_ediv_add_emod j1 4
    have h2 := Int.mul_ediv_add_emod j2 4
    exact ⟨j1 / 4 - j2 / 4, by rw [Int.mul_sub]; omega⟩
  have ⟨t, ht⟩ := hdvd
  have heq : (4 * r + j1 * q) % (4 * q) = (4 * r + j2 * q) % (4 * q) := by
    have hrew : 4 * r + j1 * q = (4 * q) * t + (4 * r + j2 * q) := by
      have hj : j1 = j2 + 4 * t := by omega
      rw [hj, Int.add_mul, show (4 * t) * q = (4 * q) * t by rw [Int.mul_right_comm]]
      omega
    rw [hrew, Int.mul_add_emod_self_left]
  unfold qGood
  rw [heq]

theorem qGood_rem_eval (q r j : Int) (hq : 0 < q) (hr0 : 0 ≤ r) (hrq : r < q)
    (hj0 : 0 ≤ j) (hj4 : j < 4) :
    (4 * r + j * q) % (4 * q) =
      if 4 * r + j * q < 4 * q then 4 * r + j * q else 4 * r + j * q - 4 * q := by
  have hj_le : j * q ≤ 3 * q := by
    have := Int.mul_le_mul_of_nonneg_right (by omega : j ≤ 3) (by omega : 0 ≤ q)
    omega
  have hj_ge : 0 ≤ j * q := Int.mul_nonneg hj0 (by omega)
  split
  · exact Int.emod_eq_of_lt (by omega) (by omega)
  · have hlo : 0 ≤ 4 * r + j * q - 4 * q := by omega
    have hhi : 4 * r + j * q - 4 * q < 4 * q := by omega
    calc (4 * r + j * q) % (4 * q)
        = ((4 * q) * 1 + (4 * r + j * q - 4 * q)) % (4 * q) := by congr 1; omega
    _   = (4 * r + j * q - 4 * q) % (4 * q) := Int.mul_add_emod_self_left _ _ _
    _   = 4 * r + j * q - 4 * q := Int.emod_eq_of_lt hlo hhi

/-- For any `0 ≤ r < q`, among `j ∈ {0, 1, 2, 3}`, at least one of `{0, 2}` and one of `{1, 3}`
    satisfy `qGood q r j`, AND at least two distinct indices in `{0, 1, 2, 3}` satisfy `qGood`. -/
theorem qGood_pairs (q r : Int) (hq : 0 < q) (hr0 : 0 ≤ r) (hrq : r < q) :
    (qGood q r 0 ∨ qGood q r 2) ∧ (qGood q r 1 ∨ qGood q r 3) := by
  have h0 := qGood_rem_eval q r 0 hq hr0 hrq (by decide) (by decide)
  have h1 := qGood_rem_eval q r 1 hq hr0 hrq (by decide) (by decide)
  have h2 := qGood_rem_eval q r 2 hq hr0 hrq (by decide) (by decide)
  have h3 := qGood_rem_eval q r 3 hq hr0 hrq (by decide) (by decide)
  unfold qGood
  rw [h0, h1, h2, h3]
  constructor
  · by_cases ha : q ≤ 4 * r ∧ 4 * r ≤ 3 * q
    · left; split <;> omega
    · right; split <;> omega
  · by_cases hb : 4 * r ≤ 2 * q
    · left; split <;> omega
    · right; split <;> omega

/-- When `4 * r ∈ {0, q, 2q, 3q}`, AT LEAST THREE of `{0, 1, 2, 3}` satisfy `qGood q r j`! -/
theorem qGood_three_of_quarter (q r : Int) (hq : 0 < q) (hr0 : 0 ≤ r) (hrq : r < q)
    (h4 : 4 * r = 0 ∨ 4 * r = q ∨ 4 * r = 2 * q ∨ 4 * r = 3 * q) :
    (qGood q r 0 ∧ qGood q r 1 ∧ qGood q r 2) ∨
    (qGood q r 0 ∧ qGood q r 1 ∧ qGood q r 3) ∨
    (qGood q r 0 ∧ qGood q r 2 ∧ qGood q r 3) ∨
    (qGood q r 1 ∧ qGood q r 2 ∧ qGood q r 3) := by
  have h0 := qGood_rem_eval q r 0 hq hr0 hrq (by decide) (by decide)
  have h1 := qGood_rem_eval q r 1 hq hr0 hrq (by decide) (by decide)
  have h2 := qGood_rem_eval q r 2 hq hr0 hrq (by decide) (by decide)
  have h3 := qGood_rem_eval q r 3 hq hr0 hrq (by decide) (by decide)
  unfold qGood
  rw [h0, h1, h2, h3]
  rcases h4 with h | h | h | h
  · right; right; right; refine ⟨?_, ?_, ?_⟩ <;> split <;> omega
  · left; refine ⟨?_, ?_, ?_⟩ <;> split <;> omega
  · right; left; refine ⟨?_, ?_, ?_⟩ <;> split <;> omega
  · right; right; left; refine ⟨?_, ?_, ?_⟩ <;> split <;> omega

/-- Mapping `j ↦ k` for odd `u`: `(k * (u % 4)) % 4` permutes `{0,1,2,3}` (preserving `{0,2}` and `{1,3}`). -/
theorem odd_quarter_pairs (p q u : Int) (hq : 0 < q) (hodd : u % 2 = 1) :
    (FarEnough 4 (4 * p + 0 * q) (4 * q) u ∨ FarEnough 4 (4 * p + 2 * q) (4 * q) u) ∧
    (FarEnough 4 (4 * p + 1 * q) (4 * q) u ∨ FarEnough 4 (4 * p + 3 * q) (4 * q) u) := by
  have hr0 : 0 ≤ (p * u) % q := Int.emod_nonneg _ (by omega)
  have hrq : (p * u) % q < q := Int.emod_lt_of_pos _ hq
  have ⟨h02, h13⟩ := qGood_pairs q ((p * u) % q) hq hr0 hrq
  have hu4_lo : 0 ≤ u % 4 := Int.emod_nonneg u (by omega)
  have hu4_hi : u % 4 < 4 := Int.emod_lt_of_pos u (by omega)
  have hu4_odd : u % 4 = 1 ∨ u % 4 = 3 := by omega
  constructor
  · rcases h02 with h0 | h2
    · left; apply farEnough_of_qGood p q u 0
      exact (qGood_mod4 q _ 0 (0 * (u % 4)) (by omega)).mp h0
    · right; apply farEnough_of_qGood p q u 2
      rcases hu4_odd with hu | hu <;> rw [hu]
      · exact (qGood_mod4 q _ 2 (2 * 1) (by decide)).mp h2
      · exact (qGood_mod4 q _ 2 (2 * 3) (by decide)).mp h2
  · rcases h13 with h1 | h3
    · rcases hu4_odd with hu | hu
      · left; apply farEnough_of_qGood p q u 1; rw [hu]
        exact (qGood_mod4 q _ 1 (1 * 1) (by decide)).mp h1
      · right; apply farEnough_of_qGood p q u 3; rw [hu]
        exact (qGood_mod4 q _ 1 (3 * 3) (by decide)).mp h1
    · rcases hu4_odd with hu | hu
      · right; apply farEnough_of_qGood p q u 3; rw [hu]
        exact (qGood_mod4 q _ 3 (3 * 1) (by decide)).mp h3
      · left; apply farEnough_of_qGood p q u 1; rw [hu]
        exact (qGood_mod4 q _ 3 (1 * 3) (by decide)).mp h3

/-- If `u` and `v` are both odd and `u` sits on a quarter-point (`(4 * ((p * u) % q)) % q = 0`),
    then one of the four shifts `k ∈ {0, 1, 2, 3}` satisfies `FarEnough 4` for BOTH `u` and `v`! -/
theorem odd_quarter_pigeonhole_two (p q u v : Int) (hq : 0 < q)
    (hu_odd : u % 2 = 1) (hv_odd : v % 2 = 1)
    (hu_qtr : 4 * ((p * u) % q) = 0 ∨ 4 * ((p * u) % q) = q ∨
              4 * ((p * u) % q) = 2 * q ∨ 4 * ((p * u) % q) = 3 * q) :
    ∃ k : Int, FarEnough 4 (4 * p + k * q) (4 * q) u ∧ FarEnough 4 (4 * p + k * q) (4 * q) v := by
  have ⟨hv02, hv13⟩ := odd_quarter_pairs p q v hq hv_odd
  have hr0 : 0 ≤ (p * u) % q := Int.emod_nonneg _ (by omega)
  have hrq : (p * u) % q < q := Int.emod_lt_of_pos _ hq
  have hu3 := qGood_three_of_quarter q ((p * u) % q) hq hr0 hrq hu_qtr
  have hu4_lo : 0 ≤ u % 4 := Int.emod_nonneg u (by omega)
  have hu4_hi : u % 4 < 4 := Int.emod_lt_of_pos u (by omega)
  have hu4_odd : u % 4 = 1 ∨ u % 4 = 3 := by omega
  have h_lift : ∀ k j : Int, (k * (u % 4)) % 4 = j % 4 → qGood q ((p * u) % q) j →
      FarEnough 4 (4 * p + k * q) (4 * q) u := fun k j hmod hgj =>
    farEnough_of_qGood p q u k ((qGood_mod4 q _ j (k * (u % 4)) hmod.symm).mp hgj)
  -- At most one k ∈ {0,1,2,3} fails for u, while v succeeds in BOTH {0,2} AND {1,3}!
  have hu_all_but_one :
      (FarEnough 4 (4 * p + 0 * q) (4 * q) u ∧ FarEnough 4 (4 * p + 2 * q) (4 * q) u) ∨
      (FarEnough 4 (4 * p + 1 * q) (4 * q) u ∧ FarEnough 4 (4 * p + 3 * q) (4 * q) u) := by
    rcases hu4_odd with hu | hu
    · rcases hu3 with ⟨g0, _, g2⟩ | ⟨_, g1, g3⟩ | ⟨g0, g2, _⟩ | ⟨g1, _, g3⟩
      · left; exact ⟨h_lift 0 0 (by rw [hu]; decide) g0, h_lift 2 2 (by rw [hu]; decide) g2⟩
      · right; exact ⟨h_lift 1 1 (by rw [hu]; decide) g1, h_lift 3 3 (by rw [hu]; decide) g3⟩
      · left; exact ⟨h_lift 0 0 (by rw [hu]; decide) g0, h_lift 2 2 (by rw [hu]; decide) g2⟩
      · right; exact ⟨h_lift 1 1 (by rw [hu]; decide) g1, h_lift 3 3 (by rw [hu]; decide) g3⟩
    · rcases hu3 with ⟨g0, _, g2⟩ | ⟨_, g1, g3⟩ | ⟨g0, g2, _⟩ | ⟨g1, _, g3⟩
      · left; exact ⟨h_lift 0 0 (by rw [hu]; decide) g0, h_lift 2 2 (by rw [hu]; decide) g2⟩
      · right; exact ⟨h_lift 1 3 (by rw [hu]; decide) g3, h_lift 3 1 (by rw [hu]; decide) g1⟩
      · left; exact ⟨h_lift 0 0 (by rw [hu]; decide) g0, h_lift 2 2 (by rw [hu]; decide) g2⟩
      · right; exact ⟨h_lift 1 3 (by rw [hu]; decide) g3, h_lift 3 1 (by rw [hu]; decide) g1⟩
  rcases hu_all_but_one with ⟨u0, u2⟩ | ⟨u1, u3⟩
  · rcases hv02 with v0 | v2
    · exact ⟨0, u0, v0⟩
    · exact ⟨2, u2, v2⟩
  · rcases hv13 with v1 | v3
    · exact ⟨1, u1, v1⟩
    · exact ⟨3, u3, v3⟩

theorem nat_strong_ind_lr {P : Nat → Prop} (step : ∀ n, (∀ m, m < n → P m) → P n) : ∀ n, P n := by
  have hall : ∀ k m, m < k → P m := by
    intro k
    induction k with
    | zero => intro m hm; omega
    | succ k ih => intro m hm; exact step m (fun j hj => ih j (by omega))
  intro n
  exact hall (n + 1) n (by omega)

/-- Self-contained Bézout's identity for `Nat` via strong induction on `b`. -/
theorem nat_bezout (a b : Nat) :
    ∃ x y : Int, (a : Int) * x + (b : Int) * y = (Nat.gcd a b : Int) := by
  have hmain : ∀ b a : Nat, ∃ x y : Int, (a : Int) * x + (b : Int) * y = (Nat.gcd a b : Int) := by
    apply nat_strong_ind_lr (P := fun b => ∀ a : Nat, ∃ x y : Int, (a : Int) * x + (b : Int) * y = (Nat.gcd a b : Int))
    intro b ih a
    by_cases hb : b = 0
    · subst hb
      refine ⟨1, 0, ?_⟩
      simp [Nat.gcd_zero_right]
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
        rw [Int.mul_sub, Int.sub_mul, ← Int.mul_assoc]
        omega
      rw [hexp, hxy]
  exact hmain b a

/-- Subcase 3a: `u` odd, `v ≡ 2 (mod 4)`, `4 ∣ w`, `w > 0`. -/
theorem lonely_runner_n3_case3a (u v w : Int) (hw : 0 < w)
    (hu : u % 2 = 1) (hv : v % 4 = 2) (hw4 : w % 4 = 0) :
    ∃ p q : Int, 0 < q ∧ FarEnough 4 p q u ∧ FarEnough 4 p q v ∧ FarEnough 4 p q w := by
  have hw_base : FarEnough 4 1 (2 * w) w := by
    unfold FarEnough
    rw [Int.one_mul, Int.emod_eq_of_lt (by omega) (by omega)]
    omega
  have hw_shift : ∀ k : Int, FarEnough 4 (4 * 1 + k * (2 * w)) (4 * (2 * w)) w := fun k =>
    quarter_shift_div4 1 (2 * w) w k (by omega) hw4 hw_base
  have ⟨hu02, hu13⟩ := odd_quarter_pairs 1 (2 * w) u (by omega) hu
  have hr0 : 0 ≤ (1 * v) % (2 * w) := Int.emod_nonneg _ (by omega)
  have hrq : (1 * v) % (2 * w) < 2 * w := Int.emod_lt_of_pos _ (by omega)
  have ⟨hv02, _⟩ := qGood_pairs (2 * w) ((1 * v) % (2 * w)) (by omega) hr0 hrq
  rcases hv02 with hv0 | hv2
  · have hfv0 : FarEnough 4 (4 * 1 + 0 * (2 * w)) (4 * (2 * w)) v :=
      farEnough_of_qGood 1 (2 * w) v 0
        ((qGood_mod4 (2 * w) _ 0 (0 * (v % 4)) (by omega)).mp hv0)
    have hfv2 : FarEnough 4 (4 * 1 + 2 * (2 * w)) (4 * (2 * w)) v :=
      farEnough_of_qGood 1 (2 * w) v 2
        ((qGood_mod4 (2 * w) _ 0 (2 * (v % 4)) (by rw [hv]; decide)).mp hv0)
    rcases hu02 with hu0 | hu2
    · exact ⟨4 * 1 + 0 * (2 * w), 4 * (2 * w), by omega, hu0, hfv0, hw_shift 0⟩
    · exact ⟨4 * 1 + 2 * (2 * w), 4 * (2 * w), by omega, hu2, hfv2, hw_shift 2⟩
  · have hfv1 : FarEnough 4 (4 * 1 + 1 * (2 * w)) (4 * (2 * w)) v :=
      farEnough_of_qGood 1 (2 * w) v 1
        ((qGood_mod4 (2 * w) _ 2 (1 * (v % 4)) (by rw [hv]; decide)).mp hv2)
    have hfv3 : FarEnough 4 (4 * 1 + 3 * (2 * w)) (4 * (2 * w)) v :=
      farEnough_of_qGood 1 (2 * w) v 3
        ((qGood_mod4 (2 * w) _ 2 (3 * (v % 4)) (by rw [hv]; decide)).mp hv2)
    rcases hu13 with hu1 | hu3
    · exact ⟨4 * 1 + 1 * (2 * w), 4 * (2 * w), by omega, hu1, hfv1, hw_shift 1⟩
    · exact ⟨4 * 1 + 3 * (2 * w), 4 * (2 * w), by omega, hu3, hfv3, hw_shift 3⟩

/-- Subcase 3b: `u, v` both odd, `4 ∣ w`, `0 < u`, `0 < w`, and `(w / 4) % u ≠ 0`. -/
theorem lonely_runner_n3_case3b (u v w : Int) (hu_pos : 0 < u) (hw_pos : 0 < w)
    (hu_odd : u % 2 = 1) (hv_odd : v % 2 = 1) (hw4 : w % 4 = 0)
    (hndvd : (w / 4) % u ≠ 0) :
    ∃ p q : Int, 0 < q ∧ FarEnough 4 p q u ∧ FarEnough 4 p q v ∧ FarEnough 4 p q w := by
  let wp : Nat := (w / 4).toNat
  let un : Nat := u.toNat
  have hwp_int : (wp : Int) = w / 4 := by omega
  have hun_int : (un : Int) = u := by omega
  have hw_eq : w = 4 * (wp : Int) := by omega
  let d : Nat := Nat.gcd wp un
  have hd_pos : 0 < d := Nat.gcd_pos_of_pos_right wp (by omega)
  have hd_wp : d ∣ wp := Nat.gcd_dvd_left wp un
  have hd_un : d ∣ un := Nat.gcd_dvd_right wp un
  let w0 : Nat := wp / d
  let u0 : Nat := un / d
  have hwp_eq : d * w0 = wp := Nat.mul_div_cancel' hd_wp
  have hun_eq : d * u0 = un := Nat.mul_div_cancel' hd_un
  have hu_du : u = (d : Int) * (u0 : Int) := by
    rw [← hun_int, ← hun_eq, Int.natCast_mul]
  have hwp_dw : (wp : Int) = (d : Int) * (w0 : Int) := by
    rw [← hwp_eq, Int.natCast_mul]
  have hu0_odd : u0 % 2 = 1 := by
    have hun_odd : un % 2 = 1 := by omega
    rw [← hun_eq, Nat.mul_mod] at hun_odd
    have : u0 % 2 = 0 ∨ u0 % 2 = 1 := by omega
    rcases this with h0 | h1
    · rw [h0] at hun_odd; simp at hun_odd
    · exact h1
  have hu0_pos : 1 ≤ u0 := by
    by_cases h0 : u0 = 0
    · rw [h0, Nat.mul_zero] at hun_eq; omega
    · exact Nat.pos_of_ne_zero h0
  have hu0_ge3 : 3 ≤ u0 := by
    by_cases h1 : u0 = 1
    · rw [h1, Nat.mul_one] at hun_eq
      have hdiv_nat : un ∣ wp := by rw [← hun_eq]; exact hd_wp
      have ⟨t, ht⟩ := hdiv_nat
      have : (w / 4) % u = 0 := by
        have h1' : w / 4 = u * (t : Int) := by
          rw [← hwp_int, ← hun_int, ht, Int.natCast_mul]
        rw [h1', Int.mul_emod_right]
      exact False.elim (hndvd this)
    · have hne2 : u0 ≠ 2 := by intro h2; rw [h2] at hu0_odd; exact absurd hu0_odd (by decide)
      clear hu_pos hw_pos hu_odd hv_odd hw4 hndvd hwp_int hun_int hw_eq hd_pos hd_wp hd_un hwp_eq hun_eq hu_du hwp_dw
      omega
  have hcop : Nat.gcd w0 u0 = 1 := by
    have hmul : d * Nat.gcd w0 u0 = d * 1 := by
      calc d * Nat.gcd w0 u0
          = Nat.gcd (d * w0) (d * u0) := (Nat.gcd_mul_left d w0 u0).symm
      _   = Nat.gcd wp un := by rw [hwp_eq, hun_eq]
      _   = d := rfl
      _   = d * 1 := (Nat.mul_one d).symm
    exact Nat.eq_of_mul_eq_mul_left hd_pos hmul
  have ⟨bx, by_, hbez⟩ := nat_bezout w0 u0
  rw [hcop] at hbez
  let t : Nat := (u0 - 1) / 2
  have ht_eq : 2 * t + 1 = u0 := by omega
  let m : Int := (t : Int) * bx
  have hu_qtr :
      4 * ((m * u) % (4 * u)) = 0 ∨ 4 * ((m * u) % (4 * u)) = 4 * u ∨
      4 * ((m * u) % (4 * u)) = 2 * (4 * u) ∨ 4 * ((m * u) % (4 * u)) = 3 * (4 * u) := by
    have hmod_mu : (m * u) % (4 * u) = (m % 4) * u := by
      have hde := Int.mul_ediv_add_emod m 4
      have hrew : m * u = (4 * u) * (m / 4) + (m % 4) * u := by
        calc m * u = (4 * (m / 4) + m % 4) * u := by rw [hde]
        _   = (4 * (m / 4)) * u + (m % 4) * u := Int.add_mul _ _ _
        _   = (4 * u) * (m / 4) + (m % 4) * u := by rw [Int.mul_right_comm 4]
      rw [hrew, Int.mul_add_emod_self_left]
      have hm0 : 0 ≤ m % 4 := Int.emod_nonneg m (by omega)
      have hm4 : m % 4 < 4 := Int.emod_lt_of_pos m (by omega)
      exact Int.emod_eq_of_lt (Int.mul_nonneg hm0 (by omega))
        (Int.mul_lt_mul_of_pos_right hm4 hu_pos)
    rw [hmod_mu]
    have hm0 : 0 ≤ m % 4 := Int.emod_nonneg m (by omega)
    have hm4 : m % 4 < 4 := Int.emod_lt_of_pos m (by omega)
    have : m % 4 = 0 ∨ m % 4 = 1 ∨ m % 4 = 2 ∨ m % 4 = 3 := by omega
    rcases this with h | h | h | h
    · left; rw [h]; omega
    · right; left; rw [h]; omega
    · right; right; left; rw [h]; omega
    · right; right; right; rw [h]; omega
  have hw_base : FarEnough 4 m (4 * u) w := by
    unfold FarEnough
    have hrem : (m * w) % (4 * u) = 4 * (d : Int) * (t : Int) := by
      have hmw : m * w = (4 * u) * (-((t : Int) * by_)) + 4 * (d : Int) * (t : Int) := by
        have hstep1 : (w0 : Int) * bx = 1 - (u0 : Int) * by_ := by omega
        calc m * w
            = (t : Int) * bx * (4 * ((d : Int) * (w0 : Int))) := by rw [hw_eq, hwp_dw]
        _   = (4 * (d : Int) * (t : Int)) * ((w0 : Int) * bx) := by
              rw [Int.mul_assoc (t : Int) bx, Int.mul_comm bx,
                  show 4 * ((d : Int) * (w0 : Int)) * bx = (4 * (d : Int)) * ((w0 : Int) * bx) by
                    rw [← Int.mul_assoc 4, Int.mul_assoc (4 * (d : Int))],
                  ← Int.mul_assoc (t : Int), Int.mul_comm (t : Int) (4 * (d : Int))]
        _   = (4 * (d : Int) * (t : Int)) * (1 - (u0 : Int) * by_) := by rw [hstep1]
        _   = 4 * (d : Int) * (t : Int) - (4 * (d : Int) * (t : Int)) * ((u0 : Int) * by_) := by
              rw [Int.mul_sub, Int.mul_one]
        _   = (4 * ((d : Int) * (u0 : Int))) * (-((t : Int) * by_)) + 4 * (d : Int) * (t : Int) := by
              rw [Int.mul_neg]
              have hprod : (4 * (d : Int) * (t : Int)) * ((u0 : Int) * by_) =
                  (4 * ((d : Int) * (u0 : Int))) * ((t : Int) * by_) := by
                rw [← Int.mul_assoc 4 (d : Int) (u0 : Int),
                    Int.mul_assoc (4 * (d : Int)) (t : Int),
                    Int.mul_assoc (4 * (d : Int)) (u0 : Int),
                    Int.mul_left_comm (t : Int) (u0 : Int) by_]
              rw [hprod]; omega
        _   = (4 * u) * (-((t : Int) * by_)) + 4 * (d : Int) * (t : Int) := by rw [← hu_du]
      rw [hmw, Int.mul_add_emod_self_left]
      have hlo : 0 ≤ 4 * (d : Int) * (t : Int) := Int.mul_nonneg (by omega) (by omega)
      have hhi : 4 * (d : Int) * (t : Int) < 4 * u := by
        rw [hu_du, ← Int.mul_assoc 4]
        exact Int.mul_lt_mul_of_pos_left (by omega : (t : Int) < (u0 : Int)) (by omega)
      exact Int.emod_eq_of_lt hlo hhi
    rw [hrem, hu_du]
    have h4t_ge : (u0 : Int) ≤ 4 * (t : Int) := by omega
    constructor
    · have hmul := Int.mul_le_mul_of_nonneg_left h4t_ge (by omega : 0 ≤ 4 * (d : Int))
      calc 4 * ((d : Int) * (u0 : Int))
          = (4 * (d : Int)) * (u0 : Int) := (Int.mul_assoc 4 _ _).symm
      _   ≤ (4 * (d : Int)) * (4 * (t : Int)) := hmul
      _   = 4 * (4 * (d : Int) * (t : Int)) := (Int.mul_left_comm 4 (4 * (d : Int)) (t : Int)).symm
    · have hsub : 4 * ((d : Int) * (u0 : Int)) - 4 * (d : Int) * (t : Int) =
          (4 * (d : Int)) * ((u0 : Int) - (t : Int)) := by
        rw [Int.mul_sub, Int.mul_assoc 4 (d : Int) (u0 : Int), Int.mul_assoc 4 (d : Int) (t : Int)]
      rw [hsub]
      have hmul := Int.mul_le_mul_of_nonneg_left (by omega : (u0 : Int) ≤ 4 * ((u0 : Int) - (t : Int)))
        (by omega : 0 ≤ 4 * (d : Int))
      calc 4 * ((d : Int) * (u0 : Int))
          = (4 * (d : Int)) * (u0 : Int) := (Int.mul_assoc 4 _ _).symm
      _   ≤ (4 * (d : Int)) * (4 * ((u0 : Int) - (t : Int))) := hmul
      _   = 4 * ((4 * (d : Int)) * ((u0 : Int) - (t : Int))) := (Int.mul_left_comm 4 (4 * (d : Int)) _).symm
  have ⟨k, hku, hkv⟩ := odd_quarter_pigeonhole_two m (4 * u) u v (by omega) hu_odd hv_odd hu_qtr
  have hkw := quarter_shift_div4 m (4 * u) w k (by omega) hw4 hw_base
  exact ⟨4 * m + k * (4 * u), 4 * (4 * u), by omega, hku, hkv, hkw⟩

/-- Subcase 3c nudge lemma: if `4 * u ≤ w`, `4 * v ≤ w`, and `(p, q)` gives `FarEnough 3`
    for `u` and `v`, nudging `p/q` by at most `1 / (4w)` achieves `FarEnough 4` for `u, v, w`. -/
theorem lonely_runner_n3_case3c (u v w : Int) (hu : 0 < u) (hv : 0 < v) (hw : 0 < w)
    (h4u : 4 * u ≤ w) (h4v : 4 * v ≤ w) :
    ∃ p q : Int, 0 < q ∧ FarEnough 4 p q u ∧ FarEnough 4 p q v ∧ FarEnough 4 p q w := by
  have ⟨p, q, hq, h3u, h3v⟩ := lonely_runner_n2 u v hu hv
  by_cases h4w : FarEnough 4 p q w
  · exact ⟨p, q, hq, farEnough_3_to_4 p q u hq h3u, farEnough_3_to_4 p q v hq h3v, h4w⟩
  · let rw_ := (p * w) % q
    have hrw0 : 0 ≤ rw_ := Int.emod_nonneg _ (by omega)
    have hrwq : rw_ < q := Int.emod_lt_of_pos _ hq
    have hfail : 4 * rw_ < q ∨ 4 * (q - rw_) < q := by
      unfold FarEnough at h4w
      by_cases ha : q ≤ 4 * rw_
      · right; omega
      · left; omega
    have hnudge_pos : ∀ (x : Int) (δ : Int), 0 < x → 4 * x ≤ w → 0 < δ → δ ≤ q →
        FarEnough 3 p q x → FarEnough 4 (4 * p * w + δ) (4 * q * w) x := by
      intro x δ hx h4x hδ0 hδq h3x
      unfold FarEnough at h3x ⊢
      have hde := Int.mul_ediv_add_emod (p * x) q
      have hrx0 : 0 ≤ (p * x) % q := Int.emod_nonneg _ (by omega)
      have hrxq : (p * x) % q < q := Int.emod_lt_of_pos _ hq
      have hnum : (4 * p * w + δ) * x =
          (4 * q * w) * ((p * x) / q) + (4 * w * ((p * x) % q) + δ * x) := by
        calc (4 * p * w + δ) * x
            = 4 * w * (p * x) + δ * x := by
              rw [Int.add_mul, show 4 * p * w * x = 4 * w * (p * x) by
                rw [Int.mul_right_comm 4 p w, Int.mul_assoc (4 * w)]]
        _   = 4 * w * (q * ((p * x) / q) + (p * x) % q) + δ * x := by rw [hde]
        _   = (4 * q * w) * ((p * x) / q) + (4 * w * ((p * x) % q) + δ * x) := by
              rw [Int.mul_add, ← Int.mul_assoc (4 * w) q, Int.mul_right_comm 4 w q]; omega
      let R := 4 * w * ((p * x) % q) + δ * x
      have hdx_pos : 0 ≤ δ * x := Int.mul_nonneg (by omega) (by omega)
      have hdx_hi : 4 * (δ * x) ≤ q * w := by
        calc 4 * (δ * x) = δ * (4 * x) := by rw [Int.mul_left_comm]
        _   ≤ q * (4 * x) := Int.mul_le_mul_of_nonneg_right hδq (by omega)
        _   ≤ q * w := Int.mul_le_mul_of_nonneg_left h4x (by omega)
      have h3r_lo : q * w ≤ 3 * (w * ((p * x) % q)) := by
        have := Int.mul_le_mul_of_nonneg_left h3x.1 (by omega : 0 ≤ w)
        rw [Int.mul_comm w q, ← Int.mul_assoc w 3, Int.mul_comm w 3, Int.mul_assoc 3] at this
        exact this
      have h3r_hi : 3 * (w * ((p * x) % q)) ≤ 2 * (q * w) := by
        have h2q : 3 * ((p * x) % q) ≤ 2 * q := by omega
        have := Int.mul_le_mul_of_nonneg_left h2q (by omega : 0 ≤ w)
        rw [← Int.mul_assoc w 3, Int.mul_comm w 3, Int.mul_assoc 3,
            ← Int.mul_assoc w 2, Int.mul_comm w 2, Int.mul_assoc 2, Int.mul_comm w q] at this
        exact this
      have h4qw : 4 * q * w = 4 * (q * w) := Int.mul_assoc 4 q w
      have h4wr : 4 * w * ((p * x) % q) = 4 * (w * ((p * x) % q)) := Int.mul_assoc 4 w _
      have hqw_pos : 0 < q * w := Int.mul_pos hq hw
      have hR_lo : 4 * q * w ≤ 4 * R := by dsimp only [R]; omega
      have hR_hi : 4 * R ≤ 3 * (4 * q * w) := by dsimp only [R]; omega
      have hR_lt : R < 4 * q * w := by dsimp only [R]; omega
      have hR_nn : 0 ≤ R := by dsimp only [R]; omega
      rw [hnum, Int.mul_add_emod_self_left, Int.emod_eq_of_lt hR_nn hR_lt]
      omega
    have hnudge_neg : ∀ (x : Int) (δ : Int), 0 < x → 4 * x ≤ w → 0 < δ → δ ≤ q →
        FarEnough 3 p q x → FarEnough 4 (4 * p * w - δ) (4 * q * w) x := by
      intro x δ hx h4x hδ0 hδq h3x
      unfold FarEnough at h3x ⊢
      have hde := Int.mul_ediv_add_emod (p * x) q
      have hrx0 : 0 ≤ (p * x) % q := Int.emod_nonneg _ (by omega)
      have hrxq : (p * x) % q < q := Int.emod_lt_of_pos _ hq
      have hnum : (4 * p * w - δ) * x =
          (4 * q * w) * ((p * x) / q) + (4 * w * ((p * x) % q) - δ * x) := by
        calc (4 * p * w - δ) * x
            = 4 * w * (p * x) - δ * x := by
              rw [Int.sub_mul, show 4 * p * w * x = 4 * w * (p * x) by
                rw [Int.mul_right_comm 4 p w, Int.mul_assoc (4 * w)]]
        _   = 4 * w * (q * ((p * x) / q) + (p * x) % q) - δ * x := by rw [hde]
        _   = (4 * q * w) * ((p * x) / q) + (4 * w * ((p * x) % q) - δ * x) := by
              rw [Int.mul_add, ← Int.mul_assoc (4 * w) q, Int.mul_right_comm 4 w q]; omega
      let R := 4 * w * ((p * x) % q) - δ * x
      have hdx_pos : 0 ≤ δ * x := Int.mul_nonneg (by omega) (by omega)
      have hdx_hi : 4 * (δ * x) ≤ q * w := by
        calc 4 * (δ * x) = δ * (4 * x) := by rw [Int.mul_left_comm]
        _   ≤ q * (4 * x) := Int.mul_le_mul_of_nonneg_right hδq (by omega)
        _   ≤ q * w := Int.mul_le_mul_of_nonneg_left h4x (by omega)
      have h3r_lo : q * w ≤ 3 * (w * ((p * x) % q)) := by
        have := Int.mul_le_mul_of_nonneg_left h3x.1 (by omega : 0 ≤ w)
        rw [Int.mul_comm w q, ← Int.mul_assoc w 3, Int.mul_comm w 3, Int.mul_assoc 3] at this
        exact this
      have h3r_hi : 3 * (w * ((p * x) % q)) ≤ 2 * (q * w) := by
        have h2q : 3 * ((p * x) % q) ≤ 2 * q := by omega
        have := Int.mul_le_mul_of_nonneg_left h2q (by omega : 0 ≤ w)
        rw [← Int.mul_assoc w 3, Int.mul_comm w 3, Int.mul_assoc 3,
            ← Int.mul_assoc w 2, Int.mul_comm w 2, Int.mul_assoc 2, Int.mul_comm w q] at this
        exact this
      have h4qw : 4 * q * w = 4 * (q * w) := Int.mul_assoc 4 q w
      have h4wr : 4 * w * ((p * x) % q) = 4 * (w * ((p * x) % q)) := Int.mul_assoc 4 w _
      have hqw_pos : 0 < q * w := Int.mul_pos hq hw
      have hR_lo : 4 * q * w ≤ 4 * R := by dsimp only [R]; omega
      have hR_hi : 4 * R ≤ 3 * (4 * q * w) := by dsimp only [R]; omega
      have hR_lt : R < 4 * q * w := by dsimp only [R]; omega
      have hR_nn : 0 ≤ R := by dsimp only [R]; omega
      rw [hnum, Int.mul_add_emod_self_left, Int.emod_eq_of_lt hR_nn hR_lt]
      omega
    have h4qw : 4 * q * w = 4 * (q * w) := Int.mul_assoc 4 q w
    rcases hfail with hlo | hhi
    · let δ := q - 4 * rw_
      refine ⟨4 * p * w + δ, 4 * q * w, Int.mul_pos (by omega) hw,
        hnudge_pos u δ hu h4u (by omega) (by omega) h3u,
        hnudge_pos v δ hv h4v (by omega) (by omega) h3v, ?_⟩
      unfold FarEnough
      have hde := Int.mul_ediv_add_emod (p * w) q
      have hnum : (4 * p * w + δ) * w = (4 * q * w) * ((p * w) / q) + q * w := by
        calc (4 * p * w + δ) * w
            = 4 * w * (p * w) + (q - 4 * rw_) * w := by
              rw [Int.add_mul, show 4 * p * w * w = 4 * w * (p * w) by
                rw [Int.mul_right_comm 4 p w, Int.mul_assoc (4 * w)]]
        _   = 4 * w * (q * ((p * w) / q) + rw_) + (q * w - 4 * rw_ * w) := by
              rw [hde, Int.sub_mul]
        _   = (4 * q * w) * ((p * w) / q) + q * w := by
              rw [Int.mul_add, ← Int.mul_assoc (4 * w) q, Int.mul_right_comm 4 w q,
                  show 4 * w * rw_ = 4 * rw_ * w by rw [Int.mul_right_comm]]
              omega
      have hqw_pos : 0 < q * w := Int.mul_pos hq hw
      rw [hnum, Int.mul_add_emod_self_left, Int.emod_eq_of_lt (by omega) (by omega)]
      omega
    · let δ := q - 4 * (q - rw_)
      refine ⟨4 * p * w - δ, 4 * q * w, Int.mul_pos (by omega) hw,
        hnudge_neg u δ hu h4u (by omega) (by omega) h3u,
        hnudge_neg v δ hv h4v (by omega) (by omega) h3v, ?_⟩
      unfold FarEnough
      have hde := Int.mul_ediv_add_emod (p * w) q
      have hnum : (4 * p * w - δ) * w = (4 * q * w) * ((p * w) / q) + 3 * (q * w) := by
        have h4qrw : 4 * (q - rw_) * w = 4 * (q * w) - 4 * (rw_ * w) := by
          rw [Int.mul_sub, Int.sub_mul, Int.mul_assoc 4 q, Int.mul_assoc 4 rw_]
        have h4wrw : 4 * w * rw_ = 4 * (rw_ * w) := by
          rw [Int.mul_assoc, Int.mul_comm w rw_]
        calc (4 * p * w - δ) * w
            = 4 * w * (p * w) - (q - 4 * (q - rw_)) * w := by
              rw [Int.sub_mul, show 4 * p * w * w = 4 * w * (p * w) by
                rw [Int.mul_right_comm 4 p w, Int.mul_assoc (4 * w)]]
        _   = 4 * w * (q * ((p * w) / q) + rw_) - (q * w - 4 * (q - rw_) * w) := by
              rw [hde, Int.sub_mul]
        _   = (4 * q * w) * ((p * w) / q) + 3 * (q * w) := by
              rw [Int.mul_add, ← Int.mul_assoc (4 * w) q, Int.mul_right_comm 4 w q, h4wrw, h4qrw]
              omega
      have hqw_pos : 0 < q * w := Int.mul_pos hq hw
      rw [hnum, Int.mul_add_emod_self_left, Int.emod_eq_of_lt (by omega) (by omega)]
      omega

/-- Core `n = 3` proof when the first speed `u` is odd. -/
theorem lonely_runner_n3_first_odd (u a b : Int) (hu : 0 < u) (ha : 0 < a) (hb : 0 < b)
    (hu_odd : u % 2 = 1) :
    ∃ p q : Int, 0 < q ∧ FarEnough 4 p q u ∧ FarEnough 4 p q a ∧ FarEnough 4 p q b := by
  by_cases ha4 : a % 4 = 0
  · by_cases hb4 : b % 4 = 0
    · -- Case 2: both a, b divisible by 4; apply n=2 to (a, b) and quarter-shift for odd u
      have ⟨p, q, hq, h3a, h3b⟩ := lonely_runner_n2 a b ha hb
      have ⟨hu02, _⟩ := odd_quarter_pairs p q u hq hu_odd
      have hfa := fun k => quarter_shift_div4 p q a k hq ha4 (farEnough_3_to_4 p q a hq h3a)
      have hfb := fun k => quarter_shift_div4 p q b k hq hb4 (farEnough_3_to_4 p q b hq h3b)
      rcases hu02 with hu0 | hu2
      · exact ⟨4 * p + 0 * q, 4 * q, by omega, hu0, hfa 0, hfb 0⟩
      · exact ⟨4 * p + 2 * q, 4 * q, by omega, hu2, hfa 2, hfb 2⟩
    · -- Case 3 with w = a (4 ∣ a) and v = b (4 ∤ b)
      have hb_rem : b % 4 = 1 ∨ b % 4 = 2 ∨ b % 4 = 3 := by
        have := Int.emod_nonneg b (by omega : (4 : Int) ≠ 0)
        have := Int.emod_lt_of_pos b (by omega : (0 : Int) < 4)
        omega
      rcases hb_rem with hb1 | hb2 | hb3
      · by_cases hnd1 : (a / 4) % u ≠ 0
        · have ⟨p, q, hq, hfu, hfb, hfa⟩ := lonely_runner_n3_case3b u b a hu ha hu_odd (by omega) ha4 hnd1
          exact ⟨p, q, hq, hfu, hfa, hfb⟩
        · by_cases hnd2 : (a / 4) % b ≠ 0
          · have ⟨p, q, hq, hfb, hfu, hfa⟩ := lonely_runner_n3_case3b b u a hb ha (by omega) hu_odd ha4 hnd2
            exact ⟨p, q, hq, hfu, hfa, hfb⟩
          · have h4u : 4 * u ≤ a := by
              have hq_pos : 1 ≤ (a / 4) / u := by
                have hde := Int.mul_ediv_add_emod (a / 4) u
                have hrem0 : (a / 4) % u = 0 := by omega
                rw [hrem0, Int.add_zero] at hde
                by_cases hle : (a / 4) / u ≤ 0
                · have := Int.mul_nonpos_of_nonneg_of_nonpos (by omega : 0 ≤ u) hle; omega
                · omega
              have hmul := Int.mul_le_mul_of_nonneg_left hq_pos (by omega : 0 ≤ u)
              have hde := Int.mul_ediv_add_emod (a / 4) u
              omega
            have h4b : 4 * b ≤ a := by
              have hq_pos : 1 ≤ (a / 4) / b := by
                have hde := Int.mul_ediv_add_emod (a / 4) b
                have hrem0 : (a / 4) % b = 0 := by omega
                rw [hrem0, Int.add_zero] at hde
                by_cases hle : (a / 4) / b ≤ 0
                · have := Int.mul_nonpos_of_nonneg_of_nonpos (by omega : 0 ≤ b) hle; omega
                · omega
              have hmul := Int.mul_le_mul_of_nonneg_left hq_pos (by omega : 0 ≤ b)
              have hde := Int.mul_ediv_add_emod (a / 4) b
              omega
            have ⟨p, q, hq, hfu, hfb, hfa⟩ := lonely_runner_n3_case3c u b a hu hb ha h4u h4b
            exact ⟨p, q, hq, hfu, hfa, hfb⟩
      · have ⟨p, q, hq, hfu, hfb, hfa⟩ := lonely_runner_n3_case3a u b a ha hu_odd hb2 ha4
        exact ⟨p, q, hq, hfu, hfa, hfb⟩
      · by_cases hnd1 : (a / 4) % u ≠ 0
        · have ⟨p, q, hq, hfu, hfb, hfa⟩ := lonely_runner_n3_case3b u b a hu ha hu_odd (by omega) ha4 hnd1
          exact ⟨p, q, hq, hfu, hfa, hfb⟩
        · by_cases hnd2 : (a / 4) % b ≠ 0
          · have ⟨p, q, hq, hfb, hfu, hfa⟩ := lonely_runner_n3_case3b b u a hb ha (by omega) hu_odd ha4 hnd2
            exact ⟨p, q, hq, hfu, hfa, hfb⟩
          · have h4u : 4 * u ≤ a := by
              have hq_pos : 1 ≤ (a / 4) / u := by
                have hde := Int.mul_ediv_add_emod (a / 4) u
                have hrem0 : (a / 4) % u = 0 := by omega
                rw [hrem0, Int.add_zero] at hde
                by_cases hle : (a / 4) / u ≤ 0
                · have := Int.mul_nonpos_of_nonneg_of_nonpos (by omega : 0 ≤ u) hle; omega
                · omega
              have hmul := Int.mul_le_mul_of_nonneg_left hq_pos (by omega : 0 ≤ u)
              have hde := Int.mul_ediv_add_emod (a / 4) u
              omega
            have h4b : 4 * b ≤ a := by
              have hq_pos : 1 ≤ (a / 4) / b := by
                have hde := Int.mul_ediv_add_emod (a / 4) b
                have hrem0 : (a / 4) % b = 0 := by omega
                rw [hrem0, Int.add_zero] at hde
                by_cases hle : (a / 4) / b ≤ 0
                · have := Int.mul_nonpos_of_nonneg_of_nonpos (by omega : 0 ≤ b) hle; omega
                · omega
              have hmul := Int.mul_le_mul_of_nonneg_left hq_pos (by omega : 0 ≤ b)
              have hde := Int.mul_ediv_add_emod (a / 4) b
              omega
            have ⟨p, q, hq, hfu, hfb, hfa⟩ := lonely_runner_n3_case3c u b a hu hb ha h4u h4b
            exact ⟨p, q, hq, hfu, hfa, hfb⟩
  · by_cases hb4 : b % 4 = 0
    · -- Symmetric to Case 3 with w = b (4 ∣ b) and v = a (4 ∤ a)
      have ha_rem : a % 4 = 1 ∨ a % 4 = 2 ∨ a % 4 = 3 := by
        have := Int.emod_nonneg a (by omega : (4 : Int) ≠ 0)
        have := Int.emod_lt_of_pos a (by omega : (0 : Int) < 4)
        omega
      rcases ha_rem with ha1 | ha2 | ha3
      · by_cases hnd1 : (b / 4) % u ≠ 0
        · exact lonely_runner_n3_case3b u a b hu hb hu_odd (by omega) hb4 hnd1
        · by_cases hnd2 : (b / 4) % a ≠ 0
          · have ⟨p, q, hq, hfa, hfu, hfb⟩ := lonely_runner_n3_case3b a u b ha hb (by omega) hu_odd hb4 hnd2
            exact ⟨p, q, hq, hfu, hfa, hfb⟩
          · have h4u : 4 * u ≤ b := by
              have hq_pos : 1 ≤ (b / 4) / u := by
                have hde := Int.mul_ediv_add_emod (b / 4) u
                have hrem0 : (b / 4) % u = 0 := by omega
                rw [hrem0, Int.add_zero] at hde
                by_cases hle : (b / 4) / u ≤ 0
                · have := Int.mul_nonpos_of_nonneg_of_nonpos (by omega : 0 ≤ u) hle; omega
                · omega
              have hmul := Int.mul_le_mul_of_nonneg_left hq_pos (by omega : 0 ≤ u)
              have hde := Int.mul_ediv_add_emod (b / 4) u
              omega
            have h4a : 4 * a ≤ b := by
              have hq_pos : 1 ≤ (b / 4) / a := by
                have hde := Int.mul_ediv_add_emod (b / 4) a
                have hrem0 : (b / 4) % a = 0 := by omega
                rw [hrem0, Int.add_zero] at hde
                by_cases hle : (b / 4) / a ≤ 0
                · have := Int.mul_nonpos_of_nonneg_of_nonpos (by omega : 0 ≤ a) hle; omega
                · omega
              have hmul := Int.mul_le_mul_of_nonneg_left hq_pos (by omega : 0 ≤ a)
              have hde := Int.mul_ediv_add_emod (b / 4) a
              omega
            exact lonely_runner_n3_case3c u a b hu ha hb h4u h4a
      · exact lonely_runner_n3_case3a u a b hb hu_odd ha2 hb4
      · by_cases hnd1 : (b / 4) % u ≠ 0
        · exact lonely_runner_n3_case3b u a b hu hb hu_odd (by omega) hb4 hnd1
        · by_cases hnd2 : (b / 4) % a ≠ 0
          · have ⟨p, q, hq, hfa, hfu, hfb⟩ := lonely_runner_n3_case3b a u b ha hb (by omega) hu_odd hb4 hnd2
            exact ⟨p, q, hq, hfu, hfa, hfb⟩
          · have h4u : 4 * u ≤ b := by
              have hq_pos : 1 ≤ (b / 4) / u := by
                have hde := Int.mul_ediv_add_emod (b / 4) u
                have hrem0 : (b / 4) % u = 0 := by omega
                rw [hrem0, Int.add_zero] at hde
                by_cases hle : (b / 4) / u ≤ 0
                · have := Int.mul_nonpos_of_nonneg_of_nonpos (by omega : 0 ≤ u) hle; omega
                · omega
              have hmul := Int.mul_le_mul_of_nonneg_left hq_pos (by omega : 0 ≤ u)
              have hde := Int.mul_ediv_add_emod (b / 4) u
              omega
            have h4a : 4 * a ≤ b := by
              have hq_pos : 1 ≤ (b / 4) / a := by
                have hde := Int.mul_ediv_add_emod (b / 4) a
                have hrem0 : (b / 4) % a = 0 := by omega
                rw [hrem0, Int.add_zero] at hde
                by_cases hle : (b / 4) / a ≤ 0
                · have := Int.mul_nonpos_of_nonneg_of_nonpos (by omega : 0 ≤ a) hle; omega
                · omega
              have hmul := Int.mul_le_mul_of_nonneg_left hq_pos (by omega : 0 ≤ a)
              have hde := Int.mul_ediv_add_emod (b / 4) a
              omega
            exact lonely_runner_n3_case3c u a b hu ha hb h4u h4a
    · -- Case 1: none divisible by 4!
      exact lonely_runner_n3_nondiv4 u a b (by omega) ha4 hb4

/-- **COMPLETE Lonely Runner Conjecture for `n = 3` (4 runners, ALL positive integer triples):**
    For EVERY triple of positive integer speeds `v₁, v₂, v₃ > 0`, there exists an exact
    rational time `t = p / q` (`q > 0`) at which all three moving runners are at circular
    distance `≥ 1/4` from the stationary runner. -/
public theorem lonely_runner_n3 (v1 v2 v3 : Int) (hv1 : 0 < v1) (hv2 : 0 < v2) (hv3 : 0 < v3) :
    ∃ p q : Int, 0 < q ∧ FarEnough 4 p q v1 ∧ FarEnough 4 p q v2 ∧ FarEnough 4 p q v3 := by
  have hstrong : ∀ s : Nat, ∀ a b c : Int,
      0 < a → 0 < b → 0 < c → (a + b + c).toNat ≤ s →
      ∃ p q : Int, 0 < q ∧ FarEnough 4 p q a ∧ FarEnough 4 p q b ∧ FarEnough 4 p q c := by
    apply nat_strong_ind_lr (P := fun s => ∀ a b c : Int,
      0 < a → 0 < b → 0 < c → (a + b + c).toNat ≤ s →
      ∃ p q : Int, 0 < q ∧ FarEnough 4 p q a ∧ FarEnough 4 p q b ∧ FarEnough 4 p q c)
    intro s ih a b c ha hb hc hsum
    by_cases ha_odd : a % 2 = 1
    · exact lonely_runner_n3_first_odd a b c ha hb hc ha_odd
    · by_cases hb_odd : b % 2 = 1
      · have ⟨p, q, hq, hfb, hfa, hfc⟩ := lonely_runner_n3_first_odd b a c hb ha hc hb_odd
        exact ⟨p, q, hq, hfa, hfb, hfc⟩
      · by_cases hc_odd : c % 2 = 1
        · have ⟨p, q, hq, hfc, hfa, hfb⟩ := lonely_runner_n3_first_odd c a b hc ha hb hc_odd
          exact ⟨p, q, hq, hfa, hfb, hfc⟩
        · have ha2 : (a / 2) * 2 = a := by omega
          have hb2 : (b / 2) * 2 = b := by omega
          have hc2 : (c / 2) * 2 = c := by omega
          have hlt : (a / 2 + b / 2 + c / 2).toNat < s := by omega
          have ⟨p, q, hq, hf1, hf2, hf3⟩ := ih (a / 2 + b / 2 + c / 2).toNat hlt
            (a / 2) (b / 2) (c / 2) (by omega) (by omega) (by omega) (Nat.le_refl _)
          refine ⟨p, q * 2, by omega, ?_, ?_, ?_⟩
          · rw [← ha2]; exact lonely_runner_speed_scaling 4 p q (a / 2) 2 hq (by decide) hf1
          · rw [← hb2]; exact lonely_runner_speed_scaling 4 p q (b / 2) 2 hq (by decide) hf2
          · rw [← hc2]; exact lonely_runner_speed_scaling 4 p q (c / 2) 2 hq (by decide) hf3
  exact hstrong (v1 + v2 + v3).toNat v1 v2 v3 hv1 hv2 hv3 (Nat.le_refl _)

end FormalAtlas
