# The Spine Ladder — exact transient dynamics near supercritical periodic words

**Date:** 2026-07-01
**Instrument:** [`spine_ladder_lab.py`](spine_ladder_lab.py) → [`results/spine_ladder_lab.json`](results/spine_ladder_lab.json)
**Relation to prior in-repo work:** unifies the −1 identity of [`AFFINE-COCYCLE-CLAIM-AUDIT.md`](AFFINE-COCYCLE-CLAIM-AUDIT.md) (T(v)+1 = 3(v+1)/2) and the −5 repeat-gate law of [`LOW-ALIGNMENT-STRUCTURE.md`](LOW-ALIGNMENT-STRUCTURE.md) (T³(x)+5 = 9(x+5)/8, v₂ drop 3 on the `59 mod 64` gate) as the d = 1 and d = 3 cases of one lemma, and generalizes the audit's F2 counterexamples (−5, −17 cycles) into a structural picture. Everything here is elementary; the value is the unification, the positivity localization, and the precise statement of what remains open.

## Lemma (Spine Ladder)

Let w be a parity word of length d with o odd letters. There is a unique residue r_w mod 2^d such that x follows w for its first d shortcut steps iff x ≡ r_w (mod 2^d), and on that cylinder T^d is exactly affine:

> T^d(x) = (3^o·x + c(w)) / 2^d,  with c(w) built by c → 3c + 2^i at each odd step i.

Let ρ_w = c(w)/(2^d − 3^o) — a rational with **odd** denominator, hence a 2-adic integer. Then F_w(ρ_w) = ρ_w, ρ_w ≡ r_w (mod 2^d), and for **every** x ≡ r_w (mod 2^d), of either sign, integer or 2-adic:

> **T^d(x) − ρ_w = (3^o / 2^d) · (x − ρ_w).**

*Proof.* Existence and uniqueness of r_w is the standard parity-vector bijection (Terras 1976): by induction on d, each of x/2 ≡ r′ (mod 2^d) and (3x+1)/2 ≡ r′ (mod 2^d) has exactly one solution mod 2^(d+1) of the required parity. On the cylinder T^d is affine with slope 3^o/2^d and fixed point ρ_w, so T^d(x) − ρ_w = F_w(x) − F_w(ρ_w) = (3^o/2^d)(x − ρ_w). Cylinder membership of ρ_w (so that its genuine T-orbit applies exactly the letters of w): for 0 ≤ i < d let y_i = ρ_(σ^i w) be the algebraic fixed point of the i-th rotation of w; every rotation has the same (d, o), so each y_i has odd denominator 2^d − 3^o and lies in ℤ₂. Writing A_i for the affine step of letter w_i, we have F_(σ^(i+1)w) ∘ A_i = A_i ∘ F_(σ^i w), so A_i carries the unique fixed point of F_(σ^i w) to that of F_(σ^(i+1)w): A_i(y_i) = y_(i+1) (indices mod d). Since y_(i+1) ∈ ℤ₂, the parity of y_i is forced to equal w_i (y/2 ∈ ℤ₂ iff y is even; (3y+1)/2 ∈ ℤ₂ iff y is odd). Hence the genuine T-orbit of ρ_w applies exactly the letters of w, and by uniqueness of r_w, ρ_w ≡ r_w (mod 2^d). ∎

Immediate consequences, for x in the cylinder:

- **(L1) Ladder:** v₂(T^d(x) − ρ) = v₂(x − ρ) − d. Alignment to a spine is a resource burned at exactly d bits per block — equivalently one bit per step, measured against the phase-shifted spine points T^i(ρ) — deterministically.
- **(L2) Expulsion** (for real — in particular rational or integer — x in the cylinder): |T^d(x) − ρ| = (3^o/2^d)·|x − ρ|. On supercritical words (3^o > 2^d) the real distance to the spine grows by a fixed factor per block: any x ≠ ρ with v₂(x − ρ) = m finite (automatic for every positive x, since ρ ≤ −1 by Corollary 1) rides the spine for exactly ⌊m/d⌋ blocks and is expelled with distance multiplied by (3^o/2^d)^⌊m/d⌋.

## Corollary 1 (Positivity localization — proved, not just measured)

**Every supercritical spine satisfies ρ_w ≤ −1.** Hence no positive rational — in particular no positive integer — is a supercritical periodic point; positive integers can only *transiently* visit supercritical cylinders, with the exact bookkeeping (L1)–(L2).

*Proof.* c(w) > 0 (each odd step contributes 2^i·3^(odds after) ≥ 1, and supercriticality forces o ≥ 1) and 2^d − 3^o < 0, so ρ_w < 0. By the Lemma, ρ_w lies in its own cylinder, so it is a genuine T-periodic point and the orbit argument below applies to it. Suppose some supercritical periodic point ρ ∈ (−1, 0). For x ∈ (−1, 0), both step types strictly increase x (x/2 > x, and (3x+1)/2 − x = (x+1)/2 > 0), and neither exits downward (an even step lands in (−1/2, 0); an odd step from (−1, −1/3) lands in (−1, 0)). So while the orbit remains in (−1, 0) it is strictly increasing and therefore never revisits ρ. If it leaves upward it becomes nonnegative (an odd step from x ∈ [−1/3, 0) gives T(x) ∈ [0, ½); the endpoint x = −1/3 lands exactly on 0, which is a fixed point) — and T maps nonnegatives to nonnegatives, so it never returns to ρ < 0. In every case the orbit never revisits ρ, contradicting periodicity. Every rotation of a supercritical word is supercritical, so this covers every point of every supercritical cycle: all satisfy ρ ≤ −1. ∎

The bound is tight in a meaningful sense: over d ≤ 12 the extremal spine other than −1 itself is ρ = −175099/173051 ≈ −1.0118, so the (−1, 0)-exclusion step is load-bearing — negativity alone gives only ρ < 0.

This is where value-positivity — which the withdrawn affine-cocycle sketch invoked but never consumed — enters with actual content: **the only exact supercritical residents of ℤ are negative integer spine points.** The audit's F2 counterexamples (−5 and −17 cycles) are precisely such points; a positive integer at 2-adic distance m from any spine is expelled after ~m steps with its distance grown by (3^o/2^d)^(m/d).

## Corollary 2 (Spine-alignment barrier)

**Provable version.** Spine-alignment conditions are congruences modulo powers of 2, so a profile (m_ρ) over a finite spine set is realizable only if *consistent* (deep alignment to one spine forces shallow alignment to every other, since distinct spines are 2-adically separated). Any consistent finite profile determines a finite union of residue classes modulo a fixed power of 2, and every such class contains infinitely many positive **and** infinitely many negative integers. Hence **no predicate on spine-alignment profiles alone implies positivity of the orbit value**.

**Remark (informal barrier).** This generalizes the claim audit's F1/F2 barrier from the −1 ladder to all spine ladders at once, with a precision the negative cone imposes: the ladder identities hold verbatim on negatives, where nontrivial cycles exist — so any *cycle-exclusion* argument whose premises are ladder identities alone also "proves" a falsehood there. For the *divergence* half the identities are merely silent (negatives are believed non-divergent too), so a divergence proof is not refuted but must add something the ladders do not carry: control of the alignment *regenerated* after expulsion.

## Verification (instrument output)

- All **1,767** supercritical words of length ≤ 12 (**181** necklace classes): per-word checks (fixed point, 2-adic cylinder membership, ρ ≤ −1) on every word, plus per-start checks (cylinder simulation, exact ladder equality, v₂ drop) on **35,340** random integers of both signs — **0 failures**.
- Integer spines found for d ≤ 12: exactly {−1} ∪ {−5, −7, −10} ∪ {−17, −25, −37, −55, −82, −41, −61, −91, −136, −68, −34} — the members of the three known negative cycles and nothing else *at d ≤ 12*. (Every negative integer cycle is automatically supercritical — ρ < 0 forces 3^o > 2^d — so "no other integer spines at any d" is precisely the open no-further-negative-cycles question, not claimed here.)
- Expulsion bookkeeping exact at m = 24, 48, 96 on all three integer spines: blocks ridden = ⌊m/d⌋ and distance growth = (3^o/2^d)^blocks as exact rationals (e.g. the −17 spine expels slowly: factor 3^7/2^11 ≈ 1.0679 per 11-step block).

## What remains open (the honest seam), stated exactly

(L1)–(L2) bound the *seed* supercritical time: a b-bit positive integer carries at most ~b bits of initial alignment to any one spine (finite 2-adic support). What nothing above bounds is **regeneration**: after expulsion, the orbit's alignment to a (possibly different) spine is

> v₂( 3^(ko)·2^(−kd)·(x − ρ) + (ρ − ρ′) ),  k = ⌊v₂(x − ρ)/d⌋ blocks ridden at expulsion

— valid at block boundaries while riding w; after further non-w steps the alignment takes the general form v₂(3^(o′)·2^(−m′)·(x − ρ) + δ) with δ a word-dependent rational constant. Either way it is a question about the low-order 2-adic digits of 3^j-multiples. The divergence half of Collatz **would follow from** a statement of this shape (regenerated alignment cannot sustain supercritical density forever); the converse direction — that a divergent orbit must exhibit unboundedly long supercritical windows, hence unbounded spine alignment — follows from the standard density argument but is not formalized here. The restriction to a fixed finite spine family matters, since every x is trivially d-aligned to the spine of whatever word it currently follows. This is a *2-adic digits of powers of 3* problem — a wall of the same flavor as the Erdős ternary-digit and Mahler Z-number problems (an analogy of difficulty class, not a reduction), here as an exact local law rather than a probabilistic heuristic.

Calibration data (49,999 odd starts ≤ 10^5, all orbit states pooled — state-weighted over ~3.7M visited states, excluding each seed's own state): max regenerated alignment to −1/−5/−17 is 17/16/16 (starts are ≤ 17 bits; the achieving starts' seed alignments are 3/2/8, so the maxima are genuinely regenerated); tail frequencies P(alignment ≥ m) sit within a factor ≈ 0.2–1.6 of the 2-adic model 2^−m at m = 8, 12 (e.g. −5 spine 1.5× above at m = 8); at m = 16 the raw counts are 2/8/44 states and fall at or below the model (down to 0.035× for −1) — small-count noise, with every deviation on the deficit side. Nothing sits above the model beyond 1.6×. Caveat: the tails include decay-chain states inherited from earlier high-alignment states, so they are not counts of independent events. No positive-integer anomaly is visible; no bound is claimed.

## Cross-verification

- **Mathematics referee (independent re-derivation, 60+ scratch checks, 0 failures): all three conclusions CONFIRMED**, including the non-integer spine −23/11 (word 1101: fixed point exact, cylinder residue 11 mod 16, ladder with v₂ drop 4 per block, expulsion after ⌊m/4⌋ blocks with growth (27/16)^blocks) and independent reproduction of the full d ≤ 12 sweep (1,767 words, 181 necklaces, the 15 integer spines, ρ ≤ −1 throughout). Proof-text repairs it required are incorporated above: the rotation-commutation argument for cylinder membership (replacing a circular sentence — without it the Lemma was instrument-backed only for d ≤ 12), the x = −1/3 boundary case (independently also patched by a concurrent session mid-review), the non-return rewording of the (−1, 0) argument, explicit exponents and block-boundary scoping in the regeneration formula, the provable CRT version of the barrier, and softening the divergence-half "equivalent to" to "would follow from". Bonus finding: the extremal non-(−1) spine at d ≤ 12 is ≈ −1.0118, so the interval-exclusion step is tight.
- **Code/overclaim referee: FILE-WITH-FIXES; all fixes incorporated above.** Zero major code defects: the 2-adic lifting in `word_data` re-derived and brute-forced against exhaustive residue enumeration for d ≤ 8 (0 mismatches); the 1,767 word count confirmed analytically (Σ C(d,o) over 3^o > 2^d = 1+1+4+5+6+22+29+37+130+176+562+794); expulsion block-counting proved correct in both d|m and d∤m cases; both regeneration caps (alignment 39, steps 5000) proved non-binding by rerun at higher caps (0 truncations). Instrument notes recorded: the fixed-point check is tautological given ρ's definition (it validates the code path, not the math), and the `all_rho_le_minus1` flag could read true vacuously in a failure world (immaterial at 0 failures). Overclaim fixes applied: tail-statistics sentence rewritten with measured ratios (the original "within small factors" was contradicted by its own m = 16 numbers), divergence-half claim scoped with the unformalized converse noted, Erdős/Mahler marked as difficulty-class analogy, barrier stated in its consistent-profile form (an earlier CRT phrasing was wrong: alignment conditions share the prime 2, so only consistent profiles are realizable), integer-spine list scoped to d ≤ 12 with the negative-cycle equivalence noted.

## Reproduction

```
python experiments/spine_ladder_lab.py   # ~2 min; writes experiments/results/spine_ladder_lab.json
```

## Lemma (Forward seam): divergence forces infinite supercritical regeneration

**Statement.** Let n > 0 have an unbounded shortcut orbit. Then for **every** window length L >= 1 there are infinitely many indices k with

> T^k(n) >= 6^L  and  T^{k+L}(n) >= T^k(n),

and every such window realizes a **supercritical** parity word (3^o > 2^L). Consequently, by (L1)-(L2) and Corollary 1, a divergent positive orbit must enter supercritical cylinders of every depth infinitely often, each entry carrying finite 2-adic alignment to some (negative) spine and ending in expulsion - i.e., divergence requires infinitely many distinct regeneration events. (This proves the *forward* half of the seam; the converse - that controlling the regeneration functional excludes divergence - is the open content.)

**Proof.** Two ingredients.

*(a) Non-descending high windows are supercritical.* Write the window's affine form T^L(x) = (3^o x + c)/2^L with c = sum over odd steps i of 3^{(odds after i)} 2^i, so 0 <= c < 3^o 2^L <= 6^L. If o = 0 the window is pure halving and descends, so a non-descending window has o >= 1. If the word were subcritical (3^o < 2^L, hence 2^L - 3^o >= 1), then T^L(x) >= x gives (2^L - 3^o)x <= c < 6^L, so x < 6^L. Contrapositive: x >= 6^L and T^L(x) >= x force 3^o > 2^L (equality impossible mod 2). QED (a)

*(b) Such windows occur infinitely often.* Suppose not: there is K such that for all k >= K, T^k(n) >= 6^L implies T^{k+L}(n) < T^k(n). Note T(x) <= (3x+1)/2 <= 2x for x >= 1: one step at most doubles. Take any m > K + L with T^m(n) > 2^{L+1} 6^L. The orbit cannot satisfy T^k(n) >= 6^L for all k in [K, m]: otherwise the L subsequences k = r (mod L) would each be strictly decreasing sequences of positive integers on [K, m], forcing values below 6^L in finitely many steps. So let s be the largest index < m with T^s(n) < 6^L. Then T^{s+1}(n) < 2*6^L, and every index in (s, m] has value >= 6^L. Partition (s, m] into consecutive length-L windows starting at s+1: each window start has value >= 6^L, so by assumption the window-start values are strictly decreasing, hence all < 2*6^L; and any index inside a window exceeds its window start by at most a factor 2^L (at most L doublings). Hence T^m(n) < 2^{L+1} 6^L - contradiction. So the orbit is bounded by max(max_{k<=K+L} T^k(n), 2^{L+1} 6^L), contradicting unboundedness. QED (b)

**Honest tier.** Elementary (a specialist would call it routine); its value is upgrading the seam from "suggested reformulation" to a one-directional theorem with an explicit quantitative threshold (6^L), leaving the open problem stated as a clean converse.

## Non-claims

This document proves no part of the Collatz conjecture. It contributes: (i) one lemma unifying previously separate in-repo identities, with exhaustive verification; (ii) a proved localization of value-positivity (all supercritical spines ≤ −1) replacing the withdrawn sketch's unconsumed gesture at it; (iii) a barrier corollary; (iv) an exact statement of the open regeneration problem that any ladder-based approach must face. The *converse* regeneration statement remains a target; the forward direction (divergence forces infinite supercritical regeneration) is proved above.
