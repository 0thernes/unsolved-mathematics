module

public import FormalAtlas.Defs

/-!
# FormalAtlas.ErdosStraus — Mordell's 1967 Modular Reduction (834 / 840 classes)

Proves unconditionally in pure Lean 4 that for EVERY natural number `n ≥ 2`
whose residue modulo `840` is NOT one of Mordell's six quadratic-residue
obstruction classes `{1, 121, 169, 289, 361, 529}` (i.e., covering **834 of
840 residue classes = 99.29% of all natural numbers**), the Erdős–Straus
equation `4 / n = 1 / x + 1 / y + 1 / z` admits an explicit positive integer
solution `(x, y, z)`.

Explicit non-claim: proves NO resolution of the full Erdős–Straus Conjecture
(status: OPEN / active-progress).
-/

namespace FormalAtlas

theorem es_even (k : Nat) (hk : 0 < k) : HasErdosStraus (2 * k) := by
  refine ⟨k, 2 * k, 2 * k, hk, by omega, by omega, ?_⟩
  have h1 : 2 * k * (2 * k) + k * (2 * k) + k * (2 * k) = 8 * (k * k) := by
    have hk2 : k * (2 * k) = 2 * (k * k) := by
      rw [← Nat.mul_assoc, Nat.mul_comm k 2, Nat.mul_assoc]
    have hk4 : 2 * k * (2 * k) = 4 * (k * k) := by
      calc 2 * k * (2 * k) = 2 * (k * (2 * k)) := Nat.mul_assoc _ _ _
      _ = 2 * (2 * (k * k)) := by rw [hk2]
      _ = 4 * (k * k) := by omega
    omega
  rw [h1]
  have h2 : 4 * k * (2 * k) * (2 * k) = 16 * (k * (k * k)) := by
    calc 4 * k * (2 * k) * (2 * k)
        = (4 * k * 2) * k * (2 * k) := by rw [Nat.mul_assoc (4 * k) 2 k]
    _   = (8 * k) * k * (2 * k) := by
          have : 4 * k * 2 = 8 * k := by omega
          rw [this]
    _   = 8 * (k * k) * (2 * k) := by rw [Nat.mul_assoc 8 k k]
    _   = (8 * (k * k) * 2) * k := by rw [Nat.mul_assoc (8 * (k * k)) 2 k]
    _   = (16 * (k * k)) * k := by
          have : 8 * (k * k) * 2 = 16 * (k * k) := by omega
          rw [this]
    _   = 16 * (k * (k * k)) := by
          rw [Nat.mul_assoc 16 (k * k) k, Nat.mul_comm (k * k) k]
  have h3 : 2 * k * (8 * (k * k)) = 16 * (k * (k * k)) := by
    calc 2 * k * (8 * (k * k))
        = (2 * k * 8) * (k * k) := by rw [← Nat.mul_assoc]
    _   = (16 * k) * (k * k) := by
          have : 2 * k * 8 = 16 * k := by omega
          rw [this]
    _   = 16 * (k * (k * k)) := by rw [Nat.mul_assoc]
  rw [h2, h3]

/-- General linear-split algebraic identity:
    if `4 * x = n + d1 + d2` with `x = d1 * u` and `x = d2 * v` (all positive),
    then `(x, u * n, v * n)` solves `4 * x * y * z = n * (y * z + x * z + x * y)`. -/
theorem es_from_split (n x u v d1 d2 : Nat)
    (hn : 0 < n) (hu : 0 < u) (hv : 0 < v) (hd1 : 0 < d1)
    (hx1 : x = d1 * u) (hx2 : x = d2 * v) (hsum : 4 * x = n + d1 + d2) :
    HasErdosStraus n := by
  have hx : 0 < x := by rw [hx1]; exact Nat.mul_pos hd1 hu
  refine ⟨x, u * n, v * n, hx, Nat.mul_pos hu hn, Nat.mul_pos hv hn, ?_⟩
  have hlhs : 4 * x * (u * n) * (v * n) = (4 * x) * (u * v * n * n) := by
    calc 4 * x * (u * n) * (v * n)
        = (4 * x) * ((u * n) * (v * n)) := Nat.mul_assoc _ _ _
    _   = (4 * x) * (u * (n * (v * n))) := by rw [Nat.mul_assoc u n (v * n)]
    _   = (4 * x) * (u * (v * (n * n))) := by rw [Nat.mul_left_comm n v n]
    _   = (4 * x) * (u * v * n * n) := by
          rw [← Nat.mul_assoc u v (n * n), ← Nat.mul_assoc (u * v) n n]
  have hr1 : (u * n) * (v * n) = u * v * n * n := by
    calc (u * n) * (v * n)
        = u * (n * (v * n)) := Nat.mul_assoc _ _ _
    _   = u * (v * (n * n)) := by rw [Nat.mul_left_comm n v n]
    _   = u * v * n * n := by rw [← Nat.mul_assoc u v (n * n), ← Nat.mul_assoc (u * v) n n]
  have hr2 : x * (v * n) = d1 * (u * v * n) := by
    rw [hx1]
    calc d1 * u * (v * n)
        = d1 * (u * (v * n)) := Nat.mul_assoc _ _ _
    _   = d1 * (u * v * n) := by rw [← Nat.mul_assoc u v n]
  have hr3 : x * (u * n) = d2 * (u * v * n) := by
    rw [hx2]
    calc d2 * v * (u * n)
        = d2 * (v * (u * n)) := Nat.mul_assoc _ _ _
    _   = d2 * (u * (v * n)) := by rw [Nat.mul_left_comm v u n]
    _   = d2 * (u * v * n) := by rw [← Nat.mul_assoc u v n]
  rw [hlhs, hr1, hr2, hr3, hsum]
  calc (n + d1 + d2) * (u * v * n * n)
      = (n + (d1 + d2)) * ((u * v * n) * n) := by rw [Nat.add_assoc]
  _   = n * ((u * v * n) * n) + (d1 + d2) * ((u * v * n) * n) := Nat.add_mul _ _ _
  _   = n * (u * v * n * n) + n * ((d1 + d2) * (u * v * n)) := by
        rw [Nat.mul_comm (d1 + d2) ((u * v * n) * n), ← Nat.mul_assoc,
            Nat.mul_comm (u * v * n) n, Nat.mul_assoc n (u * v * n) (d1 + d2),
            Nat.mul_comm (u * v * n) (d1 + d2)]
  _   = n * (u * v * n * n + (d1 + d2) * (u * v * n)) := by rw [← Nat.mul_add]
  _   = n * (u * v * n * n + (d1 * (u * v * n) + d2 * (u * v * n))) := by rw [Nat.add_mul]
  _   = n * (u * v * n * n + d1 * (u * v * n) + d2 * (u * v * n)) := by rw [Nat.add_assoc]

/-- Odd-factor identity: if `(8 * d - 1) * a = 2 * n + 1`, then
    `(d * a, 2 * d * a * n, 2 * d * n)` solves `4 / n = 1 / x + 1 / y + 1 / z`. -/
theorem es_from_odd_factor (n d a : Nat)
    (hn : 0 < n) (hd : 0 < d) (ha : 0 < a)
    (heq : (8 * d - 1) * a = 2 * n + 1) :
    HasErdosStraus n := by
  refine ⟨d * a, 2 * d * a * n, 2 * d * n,
    Nat.mul_pos hd ha,
    Nat.mul_pos (Nat.mul_pos (Nat.mul_pos (by omega) hd) ha) hn,
    Nat.mul_pos (Nat.mul_pos (by omega) hd) hn, ?_⟩
  have h8d : 8 * d * a = 2 * n + 1 + a := by
    have : 8 * d = (8 * d - 1) + 1 := by omega
    rw [this, Nat.add_mul, Nat.one_mul, heq]
  let P : Nat := 2 * d * d * a * n * n
  have h82 : 8 * 2 = 16 := rfl
  have hlhs : 4 * (d * a) * (2 * d * a * n) * (2 * d * n) = (8 * d * a) * P := by
    have h4 : 4 * (d * a) * (2 * d * a * n) * (2 * d * n) =
        16 * (d * d * d * a * a * n * n) := by
      have h422 : 4 * 2 * 2 = 16 := rfl
      calc 4 * (d * a) * (2 * d * a * n) * (2 * d * n)
          = (4 * 2 * 2) * (d * d * d * a * a * n * n) := by
            simp only [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
      _   = 16 * (d * d * d * a * a * n * n) := by rw [h422]
    have hp : (8 * d * a) * P = 16 * (d * d * d * a * a * n * n) := by
      calc (8 * d * a) * P
          = (8 * 2) * (d * d * d * a * a * n * n) := by
            simp only [P, Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
      _   = 16 * (d * d * d * a * a * n * n) := by rw [h82]
    rw [h4, hp]
  have hr1 : n * ((2 * d * a * n) * (2 * d * n)) = (2 * n) * P := by
    dsimp only [P]; ac_rfl
  have hr2 : n * ((d * a) * (2 * d * n)) = 1 * P := by
    rw [Nat.one_mul]; dsimp only [P]; ac_rfl
  have hr3 : n * ((d * a) * (2 * d * a * n)) = a * P := by
    dsimp only [P]; ac_rfl
  rw [hlhs, h8d, Nat.mul_add, Nat.mul_add, hr1, hr2, hr3]
  rw [Nat.add_mul, Nat.add_mul]

/-- Scaling lemma: if `HasErdosStraus m`, then `HasErdosStraus (m * k)` for every `k > 0`. -/
theorem es_scale (m k : Nat) (hk : 0 < k) (hm : HasErdosStraus m) :
    HasErdosStraus (m * k) := by
  have ⟨x, y, z, hx, hy, hz, heq⟩ := hm
  refine ⟨x * k, y * k, z * k, Nat.mul_pos hx hk, Nat.mul_pos hy hk, Nat.mul_pos hz hk, ?_⟩
  have hl : 4 * (x * k) * (y * k) * (z * k) = (4 * x * y * z) * (k * k * k) := by
    simp only [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
  have hr : (m * k) * ((y * k) * (z * k) + (x * k) * (z * k) + (x * k) * (y * k)) =
      (m * (y * z + x * z + x * y)) * (k * k * k) := by
    have h1 : (y * k) * (z * k) = (y * z) * (k * k) := by
      simp only [Nat.mul_left_comm, Nat.mul_comm]
    have h2 : (x * k) * (z * k) = (x * z) * (k * k) := by
      simp only [Nat.mul_left_comm, Nat.mul_comm]
    have h3 : (x * k) * (y * k) = (x * y) * (k * k) := by
      simp only [Nat.mul_left_comm, Nat.mul_comm]
    rw [h1, h2, h3, ← Nat.add_mul, ← Nat.add_mul]
    simp only [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
  rw [hl, hr, heq]

/-- **Theorem 9 (Erdős–Straus Mordell Modular Reduction, 1967).**
    For every `n ≥ 2` with `n % 840 ∉ {1, 121, 169, 289, 361, 529}`
    (834 of 840 residue classes = 99.29% of all natural numbers),
    `4 / n = 1 / x + 1 / y + 1 / z` has a positive integer solution. -/
public theorem erdos_straus_mordell_840 (n : Nat) (hn : 2 ≤ n)
    (h1 : n % 840 ≠ 1) (h2 : n % 840 ≠ 121) (h3 : n % 840 ≠ 169)
    (h4 : n % 840 ≠ 289) (h5 : n % 840 ≠ 361) (h6 : n % 840 ≠ 529) :
    HasErdosStraus n := by
  by_cases hm2 : n % 2 = 0
  · have hEq : n = 2 * (n / 2) := by omega
    rw [hEq]; exact es_even (n / 2) (by omega)
  by_cases hm4 : n % 4 = 3
  · let k := (n - 3) / 4
    let A := k + 1
    have h4A : 4 * A = n + 1 := by omega
    refine ⟨A, 2 * A * n, 2 * A * n, by omega,
      Nat.mul_pos (by omega) (by omega), Nat.mul_pos (by omega) (by omega), ?_⟩
    have h22 : 2 * 2 = 4 := rfl
    have hlhs : 4 * A * (2 * A * n) * (2 * A * n) = (4 * A) * (4 * A * A * n * n) := by
      calc 4 * A * (2 * A * n) * (2 * A * n)
          = (4 * A) * ((2 * 2) * (A * A * n * n)) := by
            simp only [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
      _   = (4 * A) * (4 * A * A * n * n) := by
            rw [h22]; simp only [Nat.mul_assoc]
    have hrhs : n * (2 * A * n * (2 * A * n) + A * (2 * A * n) + A * (2 * A * n)) =
        (n + 1) * (4 * A * A * n * n) := by
      have t1 : 2 * A * n * (2 * A * n) = n * (4 * A * A * n) := by
        calc 2 * A * n * (2 * A * n)
            = n * ((2 * 2) * (A * A * n)) := by
              simp only [Nat.mul_assoc, Nat.mul_left_comm, Nat.mul_comm]
        _   = n * (4 * A * A * n) := by rw [h22]; simp only [Nat.mul_assoc]
      have t2 : A * (2 * A * n) + A * (2 * A * n) = 4 * A * A * n := by
        have ha1 : A * (2 * A * n) = 2 * (A * A * n) := by
          simp only [Nat.mul_left_comm, Nat.mul_comm]
        have ha2 : 4 * A * A * n = 4 * (A * A * n) := by
          simp only [Nat.mul_assoc]
        rw [ha1, ha2]; omega
      rw [Nat.add_assoc, t1, t2]
      calc n * (n * (4 * A * A * n) + 4 * A * A * n)
          = n * ((n + 1) * (4 * A * A * n)) := by rw [Nat.add_mul, Nat.one_mul]
      _   = (n + 1) * (4 * A * A * n * n) := by ac_rfl
    rw [hlhs, hrhs, h4A]
  by_cases hm30 : n % 3 = 0
  · have hEq : n = 3 * (n / 3) := by omega
    rw [hEq]
    have h3 : HasErdosStraus 3 := ⟨1, 6, 6, by omega, by omega, by omega, by decide⟩
    exact es_scale 3 (n / 3) (by omega) h3
  by_cases hm32 : n % 3 = 2
  · let k := (n - 2) / 3
    let A := k + 1
    refine ⟨A, n, A * n, by omega, by omega, Nat.mul_pos (by omega) (by omega), ?_⟩
    have hlhs : 4 * A * n * (A * n) = (4 * A) * (A * n * n) := by ac_rfl
    have hrhs : n * (n * (A * n) + A * (A * n) + A * n) = (n + A + 1) * (A * n * n) := by
      calc n * (n * (A * n) + A * (A * n) + A * n)
          = n * (n * (A * n) + A * (A * n) + 1 * (A * n)) := by rw [Nat.one_mul]
      _   = n * ((n + A + 1) * (A * n)) := by rw [← Nat.add_mul, ← Nat.add_mul]
      _   = (n + A + 1) * (A * n * n) := by ac_rfl
    rw [hlhs, hrhs]
    have h4eq : 4 * A = n + A + 1 := by omega
    rw [h4eq]
  by_cases hm85 : n % 8 = 5
  · let k := (n - 5) / 8
    exact es_from_split n (2 * (k + 1)) (k + 1) (2 * (k + 1)) 2 1
      (by omega) (by omega) (by omega) (by omega) rfl (by omega) (by omega)
  -- Collapse the five residue facts into a single `n % 24 = 1` and clear them so `omega` stays O(1)!
  have h24 : n % 24 = 1 := by omega
  clear hm2 hm4 hm30 hm32 hm85
  by_cases hm50 : n % 5 = 0
  · have hEq : n = 5 * (n / 5) := by omega
    rw [hEq]
    have h5 : HasErdosStraus 5 := ⟨2, 4, 20, by omega, by omega, by omega, by decide⟩
    exact es_scale 5 (n / 5) (by omega) h5
  by_cases hm52 : n % 5 = 2
  · clear h1 h2 h3 h4 h5 h6
    let a := (2 * n + 1) / 15
    exact es_from_odd_factor n 2 a (by omega) (by omega) (by omega) (by omega)
  by_cases hm53 : n % 5 = 3
  · clear h1 h2 h3 h4 h5 h6 hm50 hm52
    let k := (n - 73) / 120
    exact es_from_split n (30 * k + 20) (15 * k + 10) (6 * k + 4) 2 5
      (by omega) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
  have hm5c : n % 5 = 1 ∨ n % 5 = 4 := by omega
  clear hm50 hm52 hm53
  by_cases hm70 : n % 7 = 0
  · have hEq : n = 7 * (n / 7) := by omega
    rw [hEq]
    have h7 : HasErdosStraus 7 := ⟨2, 28, 28, by omega, by omega, by omega, by decide⟩
    exact es_scale 7 (n / 7) (by omega) h7
  by_cases hm73 : n % 7 = 3
  · clear h1 h2 h3 h4 h5 h6 hm5c hm70
    let a := (2 * n + 1) / 7
    exact es_from_odd_factor n 1 a (by omega) (by omega) (by omega) (by omega)
  by_cases hm75 : n % 7 = 5
  · clear h1 h2 h3 h4 h5 h6 hm5c hm70 hm73
    let k := (n - 145) / 168
    exact es_from_split n (42 * k + 42) (21 * k + 21) (2 * k + 2) 2 21
      (by omega) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
  by_cases hm76 : n % 7 = 6
  · clear h1 h2 h3 h4 h5 h6 hm5c hm70 hm73 hm75
    let k := (n - 97) / 168
    exact es_from_split n (42 * k + 28) (3 * k + 2) (42 * k + 28) 14 1
      (by omega) (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
  -- Chinese Remainder Theorem on mod 24, mod 5, mod 7: only the 6 squares survive!
  exfalso
  have hm7c : n % 7 = 1 ∨ n % 7 = 2 ∨ n % 7 = 4 := by omega
  clear hm70 hm73 hm75 hm76
  rcases hm5c with r5 | r5 <;> rcases hm7c with r7 | r7 | r7
  · exact h1 (by clear h2 h3 h4 h5 h6; omega)
  · exact h2 (by clear h1 h3 h4 h5 h6; omega)
  · exact h5 (by clear h1 h2 h3 h4 h6; omega)
  · exact h3 (by clear h1 h2 h4 h5 h6; omega)
  · exact h4 (by clear h1 h2 h3 h5 h6; omega)
  · exact h6 (by clear h1 h2 h3 h4 h5; omega)

end FormalAtlas
