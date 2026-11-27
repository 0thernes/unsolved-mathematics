module

-- SPDX-License-Identifier: MIT

/-!
# FormalAtlas.Defs — Minimal Trusted Definitions

Pure Lean 4 definitions (no Mathlib dependency) for the eight open-problem
structural cores formalized in The Unsolved Mathematics Atlas (`v0.7.0`):
  1. Collatz Conjecture & 3n-1 Sibling Control
  2. Erdős–Straus Conjecture (4/n = 1/x + 1/y + 1/z)
  3. Lonely Runner Conjecture (exact rational circular distance)
  4. Brocard's Problem (n! + 1 = m²)
  5. Prime Infinitude, Prime Gaps & Twin Primes (`IsPrime`)
  6. Goldbach's Conjecture (binary prime sums)
  7. Odd Perfect Numbers & Mersenne Primes (`divSum`, `IsPerfect`)
  8. Ramsey Theory (`HasMonoTriangle`, `HasColorTriangle`, `HasColorK4` on `K_k`)

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

/-- `i`-th bit of the infinite periodic extension `w^∞` (`false` fallback if `w = []`). -/
@[expose] public def periodicBit (w : List Bool) (i : Nat) : Bool :=
  w.getD (i % w.length) false

/-- Length-`k` slice of the infinite periodic word `w^∞` starting at offset `start`. -/
@[expose] public def periodicPrefixFrom (w : List Bool) (start : Nat) : Nat → List Bool
  | 0 => []
  | k + 1 => periodicBit w start :: periodicPrefixFrom w (start + 1) k

/-- Length-`k` prefix of the infinite periodic parity word `w^∞`. -/
@[expose] public def periodicPrefix (w : List Bool) (k : Nat) : List Bool :=
  periodicPrefixFrom w 0 k

/-- Exact cleared-denominator periodic spine denominator `D(w) = 2^|w| - 3^(o(w))`
    (strictly odd whenever `|w| ≥ 1`). -/
@[expose] public def spineDenom (w : List Bool) : Int :=
  (2 : Int) ^ w.length - (3 : Int) ^ (wordOddCount w)

/-- Zero-workspace reversible catalytic register evaluation of the Collatz cylinder affine law:
    borrows an arbitrary pre-filled catalyst `cat`, accumulates `T^d(2^d q + r)` into `acc`,
    and uncomputes `cat` identically back to its initial value. -/
@[expose] public def catCollatzStep (d : Nat) (q r acc cat : Int) : Int × Int :=
  let c1 := cat + (3 : Int) ^ (oddCount T d r) * q
  let c2 := c1 + iter T d r
  let acc1 := acc + c2
  let acc2 := acc1 - cat
  let c3 := c2 - iter T d r
  let c4 := c3 - (3 : Int) ^ (oddCount T d r) * q
  (acc2, c4)

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

-- ============================================================================
-- 5. Primality, Divisors, Perfect Numbers & Graph Ramsey Colorings
-- ============================================================================

/-- Textbook primality: `p ≥ 2` and its only natural divisors are `1` and `p`. -/
@[expose] public def IsPrime (p : Nat) : Prop :=
  2 ≤ p ∧ ∀ d : Nat, d ∣ p → d = 1 ∨ d = p

/-- Structurally recursive binary-search integer square root `⌊√n⌋`, exact for all `n : Nat`. -/
@[expose] public def isqrtAux (n lo hi : Nat) : Nat → Nat
  | 0 => lo
  | fuel + 1 =>
    if hi ≤ lo + 1 then lo
    else
      let mid := (lo + hi) / 2
      if mid * mid ≤ n then isqrtAux n mid hi fuel
      else isqrtAux n lo mid fuel

@[expose] public def isqrt (n : Nat) : Nat :=
  if n == 0 then 0 else isqrtAux n 1 (n + 1) n

/-- Sum of all positive divisors `σ(n) = ∑_{d ∣ n} d`, computed over divisor pairs
    `1 ≤ d ≤ ⌊√n⌋` (`d` and `n / d`, counting `d` once when `d * d = n`). -/
@[expose] public def divSumPairs (n : Nat) : Nat → Nat
  | 0 => 0
  | d + 1 =>
    let k := d + 1
    let contrib :=
      if n % k == 0 then
        if k * k == n then k else k + n / k
      else 0
    contrib + divSumPairs n d

@[expose] public def divSum (n : Nat) : Nat :=
  divSumPairs n (isqrt n)

/-- Textbook perfect number: `n > 0` and `σ(n) = 2n`. -/
@[expose] public def IsPerfect (n : Nat) : Prop :=
  0 < n ∧ divSum n = 2 * n

/-- A 2-coloring `c : Fin k → Fin k → Bool` of `K_k` contains a monochromatic triangle. -/
@[expose] public def HasMonoTriangle {k : Nat} (c : Fin k → Fin k → Bool) : Prop :=
  ∃ a b d : Fin k, a.val < b.val ∧ b.val < d.val ∧ c a b = c b d ∧ c a b = c a d

/-- A 2-coloring `c` of `K_k` contains a triangle (`K_3`) of specific color `col`. -/
@[expose] public def HasColorTriangle {k : Nat} (c : Fin k → Fin k → Bool) (col : Bool) : Prop :=
  ∃ a b d : Fin k, a.val < b.val ∧ b.val < d.val ∧
    c a b = col ∧ c b d = col ∧ c a d = col

/-- A 2-coloring `c` of `K_k` contains a monochromatic `K_4` of specific color `col`. -/
@[expose] public def HasColorK4 {k : Nat} (c : Fin k → Fin k → Bool) (col : Bool) : Prop :=
  ∃ a b d e : Fin k, a.val < b.val ∧ b.val < d.val ∧ d.val < e.val ∧
    c a b = col ∧ c a d = col ∧ c a e = col ∧
    c b d = col ∧ c b e = col ∧ c d e = col

end FormalAtlas
