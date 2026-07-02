# Spine regeneration kernel — the pure spine is solved, the coupling is the wall

**Date:** 2026-07-02
**Instrument:** [`spine_regen_kernel.py`](spine_regen_kernel.py) → [`results/spine_regen_kernel.json`](results/spine_regen_kernel.json)
**Status:** structural localization of the open target named in [`SPINE-LADDER.md`](SPINE-LADDER.md). **Not a proof.**

## The open target (from SPINE-LADDER)

A positive integer rides a spine cylinder for `⌊m/d⌋` blocks and is then expelled; closing the divergence half by ladders needs control of its **regenerated 2-adic alignment**, which is `v₂` of an affine expression in `3^j`-multiples. This note resolves that expression on the pure spine and names exactly what remains.

## Two exact facts (verified)

1. **Structure.** `3` has multiplicative order `2^{k−2}` mod `2^k` (verified `k = 3…19`), i.e. `⟨3⟩` is the **index-2 subgroup** of `(ℤ/2^k)^×`. Powers of 3 sweep out half the odd residues, equidistributing over that subgroup.
2. **Pure spine solved.** On a pure spine (odd multiplier `q = 1` — the `−1` and `−5` fixed points), the regeneration is given exactly by **Lifting-the-Exponent**:
   ```
   v₂(3^j − 1) = 2 + v₂(j)  (j even),  = 1  (j odd)
   v₂(3^j + 1) = 2          (j odd),   = 1  (j even)
   ```
   Verified: 0 violations for `j = 1…4000`. The alignment distribution over even `j` is a clean geometric tail `{3:1000, 4:500, 5:250, 6:125, …}` (`= 3 + v₂(j)`). **So the pure-spine regeneration kernel is completely explicit.**

## What remains — the exact wall

The pure spine being solved is *why the conjecture isn't*: positives never sit on a pure spine (they visit spine cylinders only transiently — SPINE-LADDER), so their regeneration is the **coupled** quantity
```
v₂( 3^j · q ± c ),   with (j, q, c) selected by the dynamics, not free.
```
That is a **measure-zero subsequence** of `⟨3⟩ mod 2^k`, and controlling its `v₂` pointwise is an **effective equidistribution / discrepancy** statement for a *dynamically selected* orbit of powers of 3. This is the same **measure-1 vs measure-0** wall proved unavoidable in [`EPSILON-BARRIER.md`](EPSILON-BARRIER.md) and [`DIVERGENCE-DRIFT.md`](DIVERGENCE-DRIFT.md) — here in its sharpest, most concrete form, and tied once more to the Diophantine constant `log₂3` (via the order/equidistribution structure of `⟨3⟩`).

## Why this is progress (and why it isn't a proof)

It converts a vague "regeneration is hard" into a precise target object: *effective equidistribution of the dynamically-selected power-of-3 subsequence mod `2^k`*. A ladder-based divergence proof must produce exactly that; a pure-measure argument provably cannot (it lives on the measure-1 side). No claim about the conjecture is made — this maps the crux, it does not cross it. Reproduce: `python spine_regen_kernel.py`.
