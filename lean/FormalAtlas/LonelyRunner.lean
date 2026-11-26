module

public import FormalAtlas.Defs

/-!
# FormalAtlas.LonelyRunner — Global Sharpness & Base Cases

Proves two structural results for the Lonely Runner Conjecture in pure Lean 4:
  1. `lonely_runner_sharpness_all_n`: For EVERY `n ≥ 1` and EVERY rational time
     `t = p / q` (`q > 0`), the canonical speed tuple `v_i = i` (`1 ≤ i ≤ n`)
     has at least one runner `i ∈ {1, …, n}` with circular distance `‖t · i‖ ≤ 1 / (n + 1)`.
  2. `lonely_runner_n1` & `lonely_runner_n2`: Direct constructive proofs of the
     Lonely Runner Conjecture for `n = 1` (2 runners) and `n = 2` (3 runners).

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

/-- **Theorem 10 (Global Sharpness of the Lonely Runner Constant `1 / (n + 1)`).**
    For every `n ≥ 1` and every rational time `p / q` (`q > 0`), the speed set
    `{1, 2, …, n}` has some runner `i ∈ {1, …, n}` with `‖(p / q) · i‖ ≤ 1 / (n + 1)`. -/
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

/-- **Theorem 20 (Exact Rational Speed-Scaling Invariance).**
    Scaling both a runner's speed `v` and the time denominator `q` by any positive
    integer factor `k > 0` preserves `FarEnough m`. Hence any common divisor of
    runner speeds can be factored out without altering the Lonely Runner property. -/
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

/-- **Lonely Runner `n = 3` (4 runners) across all non-divisible-by-4 speed triples:**
    Whenever `v₁, v₂, v₃ > 0` have none divisible by `4` (covering 7 of 8 mod-4 parity classes),
    time `t = 1/4` achieves exact circular separation `≥ 1/4` for all three moving runners. -/
public theorem lonely_runner_n3_nondiv4 (v1 v2 v3 : Int)
    (h1 : v1 % 4 ≠ 0) (h2 : v2 % 4 ≠ 0) (h3 : v3 % 4 ≠ 0) :
    ∃ p q : Int, 0 < q ∧ FarEnough 4 p q v1 ∧ FarEnough 4 p q v2 ∧ FarEnough 4 p q v3 := by
  refine ⟨1, 4, by omega, ?_, ?_, ?_⟩
  · unfold FarEnough; rw [Int.one_mul]; have := Int.emod_nonneg v1 (by omega : (4 : Int) ≠ 0); have := Int.emod_lt_of_pos v1 (by omega : (0 : Int) < 4); omega
  · unfold FarEnough; rw [Int.one_mul]; have := Int.emod_nonneg v2 (by omega : (4 : Int) ≠ 0); have := Int.emod_lt_of_pos v2 (by omega : (0 : Int) < 4); omega
  · unfold FarEnough; rw [Int.one_mul]; have := Int.emod_nonneg v3 (by omega : (4 : Int) ≠ 0); have := Int.emod_lt_of_pos v3 (by omega : (0 : Int) < 4); omega

end FormalAtlas
