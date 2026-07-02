# Regeneration Events at Scale — per-event alignment statistics (10⁷ starts)

**Date:** 2026-07-02
**Instrument:** [`regeneration_events_scan.py`](regeneration_events_scan.py) → [`results/regeneration_events_scan.json`](results/regeneration_events_scan.json)
**Context:** direct follow-up to [`SPINE-LADDER.md`](SPINE-LADDER.md), whose regeneration calibration was state-weighted (its code referee flagged decay-chain inheritance as an inflater). This memo measures the honest quantity: **fresh bits per event**.

## Definitions

Alignment-to-cycle, phase-correct (decays exactly 1 bit per shortcut step while riding, by the Spine Ladder Lemma applied to rotations): for the −1 spine, a(x) = v₂(x+1) on odd states; for the −5 cycle, a(x) = max(v₂(x+5), v₂(x+7)) on odd states and v₂(x+10) on even states (cycle points are 2-adically separated, so at most one phase is deep).

**Fresh bits at state t:** fresh_t = a_t − max(a_(t−1) − 1, 0), when positive. The subtraction removes exactly the ladder-inherited alignment; fresh_t counts regenerated low bits only. The iid coin model predicts P(fresh_t ≥ j) ≈ 2^(−j) per state. This baseline is phase-blind; for the −5 cycle, where a(x) maxes over two phases, it is only approximate at small j.

## Results (10,000,000 odd starts 3…2×10⁷; 1,123,358,725 orbit states; 553 s)

Per-state tail P(fresh ≥ j), with ratio to the coin model 2^(−j):

| j | −1 spine | ratio | −5 cycle | ratio | model |
|---|---|---|---|---|---|
| 4 | 3.20×10⁻² | 0.51 | 5.44×10⁻² | 0.87 | 6.25×10⁻² |
| 8 | 1.26×10⁻³ | 0.32 | 2.55×10⁻³ | 0.65 | 3.91×10⁻³ |
| 12 | 6.86×10⁻⁵ | 0.28 | 1.10×10⁻⁴ | 0.45 | 2.44×10⁻⁴ |
| 16 | 2.62×10⁻⁶ | 0.17 | 3.87×10⁻⁶ | 0.25 | 1.53×10⁻⁵ |
| 20 | 5.43×10⁻⁸ | 0.057 | 1.42×10⁻⁷ | 0.15 | 9.54×10⁻⁷ |

Event rates: 0.2508 events/state (−1), 0.5101 (−5) — against the coin model's P(fresh ≥ 1) = 1/2 these are 0.50× and 1.02×, i.e. at j = 1 the −5 cycle sits slightly above the model (see the scoping in the next section). Extremes: max single jump 23 bits (−1 spine, start 7,456,539) and 25 bits (−5 cycle, start 18,620,319); max per-orbit total fresh bits 261 (−1) and 442 (−5), both achieved by start 15,733,191, which also holds the worst per-orbit fresh(−1)-to-bitlength ratio (10.875 = 261/24 — a cumulative quantity over a very long orbit, not a per-step rate; the instrument tracks this ratio for the −1 spine only).

## Tail deficit vs the coin model (empirical, this dataset)

**At the five tabulated levels j = 4, 8, 12, 16, 20, on 1.12×10⁹ states, the coin model is an upper bound:** P(fresh ≥ j) ≤ 2^(−j), and along that grid the deficit widens as j grows. This is an empirical statement about this dataset, not a law. The full histograms (in the results JSON) show the −5 cycle slightly *above* the model at small j — ratios 1.02, 1.04, 1.03, 1.12 at j = 1, 2, 6, 7 — so the one-sided property holds at every measured j for the −1 spine but only for j ≥ 8 (and j = 3, 4, 5) for the −5 cycle. The excess replicates on a disjoint independent range (ratios 1.03, 1.05, 1.05, 1.17 at j = 1, 2, 6, 7 on a 1.7×10⁷-state referee re-implementation), so it is structural, not noise. An earlier revision of this memo attributed the j = 1, 2 part to the a₅ ≥ 2 odd-state floor (for odd x exactly one of x+5, x+7 is ≡ 0 mod 4 — true, exhaustively verified); **the null-model computation below falsifies that floor as an explanation** — the stationary model has the same floor and its one-step law is provably exactly geometric. The j = 6, 7 bump (jump counts barely decaying: 8.24M at j = 6 vs 7.00M at j = 7) was likewise never explained. Both excesses, and the large-j deficits, are now attributed to the same open question: how positive orbits sample shallow residues differently from the stationary measure (see "The correct null model"). The −1 spine satisfies P(fresh ≥ j) ≤ 2^(−j) at every measured j (max ratio 0.551).

The natural hypothesis for the widening is finite-size structure: a fresh jump of size j at state x requires j specific low bits of x, and orbit values here peak near 2³⁵–2³⁷. This is a hypothesis, not established; the falsification test is to rerun at larger starts and check whether the ratios at fixed j rise toward 1. (It also does not account for the flat ≈0.5 ratio of the −1 spine at small j, which is a phase effect: −1-events can fire only on odd states.) No positive-integer anomaly appears at the tabulated levels; there, positive orbits regenerate *less* alignment than random coins — though the deficit could itself be a finite-size artifact rather than a persistent property, and the −5 small-j excess (up to 1.12×) shows the sub-coin direction is not uniform in j.

## The correct null model: the one-step Haar law is exactly geometric (added 2026-07-02, same day)

**Instrument:** [`model_baseline_probe.py`](model_baseline_probe.py) → [`results/model_baseline_probe.json`](results/model_baseline_probe.json). The 2^(−j) baseline above is phase-blind, but fresh compares alignments of *consecutive* states, which T couples deterministically — so the honest null model is the one-step fresh law under the uniform (Haar) measure on ℤ₂, which T preserves. Measured by Monte Carlo at 10⁸ uniform 128-bit samples:

**P(fresh ≥ j) = 2^(−j) exactly — provable, not just measured** (MC at 10⁸ agrees at every j ∈ [1, 12]: ratios 0.9915–1.0013, every point within 1.7σ binomial of exact; events/state 0.50009). *Proof (referee's branch-mass derivation, verified exhaustively over all residues mod 2²², where #{fresh ≥ j} = 2^(22−j) exactly for j = 1..13):* odd +7-phase states (x ≡ 1 mod 4, Haar mass 1/4) produce fresh = 0 at every depth; deep states (a ≥ 3) produce fresh = 0 deterministically; the only firing states are even with a = 1 (mass 1/4), even with a = 2 (mass 1/8), and odd +5-phase with v₂(x+5) = 2 (mass 1/8), each firing with probability 1 with the identical conditional tail 2^(1−j); total mass 1/2 gives P(fresh ≥ j) = ½·2^(1−j) = 2^(−j). The derivation independently predicts the event phase split +10:+5:+7 = 2:1:1 at every j, which the scan's phase histogram matches to 4 decimals. The naive coin baseline is therefore exact as the stationary null — a small theorem, not an accident — and every ratio in this memo keeps its meaning unchanged.

Three consequences:

1. **The floor explanation is falsified.** The a₅ ≥ 2 odd-state floor exists in the stationary model too, and the stationary law is provably exactly geometric — so the floor cannot explain the orbit excess at j = 1, 2. The true stationary mechanism is the branch-mass structure above, not a floor effect.
2. **Freshness is a shallow-state phenomenon.** A state with a(x) ≥ 3 produces fresh = 0 *deterministically* (writing x = −5 + 2^m·k with k odd: a(Tx) = m − 1 exactly, and likewise for the +7 and +10 phases). The a = 2 boundary is mixed and sharp: the odd +7 sub-phase (v₂(x+7) = 2) is deterministic-zero, while even a ∈ {1, 2} and odd +5-phase a = 2 are deterministic-fire (fresh ≥ 1 with probability 1). All fresh events originate at these shallow firing states, where new low bits are genuinely undetermined. Deviations from geometric are therefore statements about the distribution of *shallow residues along positive orbits*.
3. **The deviations are orbit-sampling effects.** With the stationary law exactly geometric, any deviation measures how the sampled orbit-state ensemble differs from Haar — whether that reflects asymptotic orbit structure or start-set finiteness is open. Positive-orbit statistics sit above the stationary law at j = 1, 2, 6, 7 (−5 family) and below it at large j (both families). Neither direction is explained; the mechanism question — what biases the low bits of orbit states relative to Haar — is the sharpest open follow-up this memo produces. (Candidate contributors, untested: start-set finiteness for the deficits; arithmetic bias of (3x+1)/2 outputs for the excesses.)

## One provable bound (trivial but deterministic)

For positive x and any tracked cycle member μ < 0: 2^(v₂(x−μ)) divides the positive integer x − μ = x + |μ|, so v₂(x − μ) ≤ log₂(x + |μ|). Hence every single regeneration jump satisfies **fresh_t ≤ a_t ≤ log₂(x_t + 136) = bitlen(x_t) + O(1)** (|μ| ≤ 10 suffices for the cycles tracked here; 136 covers the −17 cycle for future use). The observed maxima (23, 25 bits) **saturate the per-state bound exactly**: referee recomputation of both witness orbits located the jump states, x = 8,388,607 with x+1 = 2²³ and x = 33,554,422 with x+10 = 2²⁵ — equality in v₂ = log₂(x+|μ|) — though both sit far below the orbit-peak bit-lengths (37 and 28). This bounds *jumps* by current value size; it does **not** bound per-orbit totals, which on the coin model grow linearly with orbit length; the observed per-orbit maxima are consistent with that, but no quantitative fit against orbit length was run.

## Refined open target

The target inequality the ladder approach points at is now empirically calibrated on both sides: any proof must be consistent with (i) the deterministic jump ceiling above, and (ii) the measured sub-coin tail — i.e., the target is P(fresh ≥ j) ≤ C·2^(−j) *uniformly for all positive orbits over any step window*, not just on average over starts (read at every j, this dataset forces C ≥ 1.13 and the referee's disjoint-range replication C ≥ 1.17, from the −5 excess; restricting to j ≥ 8, or to the −1 spine alone, allows C = 1). That uniform inequality is the precise "2-adic digits of 3^j-multiples" statement from SPINE-LADDER, and remains open. Even if proved, it would not by itself settle the divergence half: with C ≥ 1 it allows a mean regeneration budget of Σ_j C·2^(−j) ≥ 1 fresh bit per state, which arithmetically matches the 1-bit-per-step consumption of spine riding — the coin model itself satisfies the inequality and excludes divergence only via fluctuation arguments. Converting the tail bound into "no positive orbit sustains supercritical odd-density forever" still requires drift/union-bound machinery over windows and spine phases, per SPINE-LADDER's "would follow from" scoping. Nothing in this memo proves any of this; the memo pins down the inequality's empirical shape and finds no empirical obstruction at the measured levels.

## Non-claims

This document proves no part of the Collatz conjecture. It contributes calibration data at 1.12×10⁹-state scale under honest per-event accounting, one trivial deterministic jump bound, and a sharpened statement of the open uniform inequality.

## Reproduction

```
python experiments/regeneration_events_scan.py --starts 10000000   # ~9 min
```

## Cross-verification

- **Overclaim referee: FILE-WITH-FIXES, all fixes incorporated.** Its load-bearing catch: the original headline "at every measured level the coin model is an upper bound" was contradicted by the instrument's own full histograms — the tabulation grid (j = 4, 8, 12, 16, 20) happened to dodge all four −5 exceedances, repeating the exact failure mode this repo's earlier audits penalized. Also required: hypothesis-marking the finite-size explanation, the budget arithmetic showing a C ≥ 1 uniform tail bound alone cannot exclude sustained riding (supply ≥ 1 fresh bit/state matches the 1 bit/step ladder consumption — the coin model itself satisfies the inequality), and the model-side comparison of the raw event rates.
- **Null-model referee (third pass, on the Haar section): all items CONFIRMED, three wording fixes applied, and the exact-geometric law upgraded from measured to proved.** Independent rerun with a different seed (2×10⁷ samples: max |z| = 1.33 vs exact); original 10⁸ data max |z| = 1.70; measure-preservation of T on ℤ₂ verified (both preimage branches); 128-bit sampling error bounded ≤ 2^−100. Deep-state determinism confirmed exhaustively mod 2^20 with the a = 2 boundary resolved (mixed; a ≥ 3 sharp). The referee's branch-mass derivation proves P(fresh ≥ j) = 2^(−j) exactly and predicts the 2:1:1 phase split the scan's histogram matches to 4 decimals. It also caught this memo misquoting its own ratio range (0.9975 dodged j = 12's 0.9915) — the same cherry-pick failure mode penalized twice above, now fixed.
- **Data/code referee: code CONFIRMED faithful, no tail-affecting bugs** (inheritance branch exact; histogram caps non-binding or display-only; no double counting; seed exclusion correct); JSON internally consistent; all table values, extremes, and the 10.875 ratio reproduce exactly. Independent re-implementation on a disjoint range replicates event rates to 3 decimals and the −5 exceedances (1.169 at j = 7). Both max-jump witnesses recomputed exactly (23-bit jump at state 2²³−1; 25-bit jump at state with x+10 = 2²⁵ — per-state bound saturated with equality). Established the a₅ ≥ 2 odd-state floor (exhaustive to 10⁵) as the j = 1, 2 mechanism; flagged the j = 6, 7 bump as unexplained. Nits fixed: witness saturation wording, loose constant 136 noted, orbit-peak 2³⁶·⁵.
