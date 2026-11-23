module

/-!
# FormalAtlas.Defs — Minimal Trusted Definitions

Pure Lean 4 definitions (no Mathlib dependency) for the four unsolved-problem
structural cores formalized in The Unsolved Mathematics Atlas:
  1. Collatz Conjecture & 3n-1 Sibling Control
  2. Erdős–Straus Conjecture (4/n = 1/x + 1/y + 1/z)
  3. Lonely Runner Conjecture (exact rational circular distance)
  4. Brocard's Problem (n! + 1 = m²)

Every definition is intentionally elementary and `@[expose]`d so a mathematician
can audit statement fidelity against the published literature in under two minutes.
-/

namespace FormalAtlas

-- ============================================================================
-- 1. Collatz shortcut map T and sibling 3n-1 shortcut map TMinus
-- ============================================================================

/-- Shortcut Collatz map on `Int`: `x / 2` if even, `(3x + 1) / 2` if odd. -/
@[expose] public def T (x : Int) : Int :=
  if x % 2 == 0 then x / 2 else (3 * x + 1) / 2

/-- Sibling `3n - 1` shortcut map on `Int`: `x / 2` if even, `(3x - 1) / 2` if odd. -/
@[expose] public def TMinus (x : Int) : Int :=
  if x % 2 == 0 then x / 2 else (3 * x - 1) / 2

/-- `d`-fold iteration of a map `f : Int → Int`. -/
@[expose] public def iter (f : Int → Int) : Nat → Int → Int
  | 0, x => x
  | d + 1, x => iter f d (f x)

/-- Parity bit of an integer: `false` (0) if even, `true` (1) if odd. -/
@[expose] public def parityBit (x : Int) : Bool :=
  x % 2 != 0

/-- Length-`d` parity word of `x` under `f`: bit `i` is `parityBit (iter f i x)`. -/
@[expose] public def parityWord (f : Int → Int) : Nat → Int → List Bool
  | 0, _ => []
  | d + 1, x => parityBit x :: parityWord f d (f x)

/-- Count of odd steps (`true` bits) in a parity word. -/
@[expose] public def wordOddCount : List Bool → Nat
  | [] => 0
  | b :: bs => (if b then 1 else 0) + wordOddCount bs

/-- Number of odd steps in the first `d` iterates of `x` under `f`. -/
@[expose] public def oddCount (f : Int → Int) (d : Nat) (x : Int) : Nat :=
  wordOddCount (parityWord f d x)

/-- Exact affine intercept `c(w)` for a parity word `w` under `T`:
    satisfies `2^|w| · T^|w|(x) = 3^(wordOddCount w) · x + wordIntercept w`. -/
@[expose] public def wordIntercept : List Bool → Int
  | [] => 0
  | false :: ws => 2 * wordIntercept ws
  | true :: ws => (3 : Int) ^ (wordOddCount ws) + 2 * wordIntercept ws

/-- Rotate a parity word one step left: `b :: ws ↦ ws ++ [b]`. -/
@[expose] public def rotateWord : List Bool → List Bool
  | [] => []
  | b :: ws => ws ++ [b]

/-- `k`-fold rotation of a parity word. -/
@[expose] public def rotateWordN : Nat → List Bool → List Bool
  | 0, w => w
  | k + 1, w => rotateWordN k (rotateWord w)

-- ============================================================================
-- 2. Erdős–Straus Conjecture (exact denominator-cleared form)
-- ============================================================================

/-- Exact positive-integer witness for `4 / n = 1 / x + 1 / y + 1 / z`. -/
@[expose] public def IsErdosStrausSol (n x y z : Nat) : Prop :=
  0 < x ∧ 0 < y ∧ 0 < z ∧ 4 * x * y * z = n * (y * z + x * z + x * y)

/-- `n` admits an Erdős–Straus Egyptian-fraction decomposition. -/
@[expose] public def HasErdosStraus (n : Nat) : Prop :=
  ∃ x y z : Nat, IsErdosStrausSol n x y z

-- ============================================================================
-- 3. Lonely Runner Conjecture (exact rational circular distance)
-- ============================================================================

/-- Exact integer test that `‖ (p / q) · v ‖ ≥ 1 / m`, where `‖u‖ = min_{k∈ℤ} |u - k|`
    is distance to the nearest integer. -/
@[expose] public def FarEnough (m p q v : Int) : Prop :=
  let r := (p * v) % q
  q ≤ m * r ∧ q ≤ m * (q - r)

/-- Exact integer test that `‖ (p / q) · v ‖ ≤ 1 / m`. -/
@[expose] public def WithinDist (m p q v : Int) : Prop :=
  let r := (p * v) % q
  m * r ≤ q ∨ m * (q - r) ≤ q

-- ============================================================================
-- 4. Brocard's Problem (n! + 1 = m²)
-- ============================================================================

/-- Standard factorial `n!`. -/
@[expose] public def fact : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fact n

/-- `(n, m)` is a Brown-number solution to Brocard's equation `n! + 1 = m²`. -/
@[expose] public def IsBrocardSol (n m : Nat) : Prop :=
  fact n + 1 = m * m

end FormalAtlas
