# Sibling Control — running the machinery where the conjecture is false

_Created: 2026-07-01. Companion to `collatz_sibling_control.py`, `FRONTIER-GEOMETRY.md`, `CERTIFICATE-FRONTIER-THEOREMS.md`._
_Status: labels as in the companion docs — **Proved** / **Measured** / **Heuristic**. Nothing here proves the Collatz conjecture. What it proves is a constraint on how the Collatz conjecture can possibly be proved._

## The idea

Every instrument in this directory reads "clean" on 3n+1: no frontier-resident integers, vacuous thresholds, perfect word-model statistics. But an instrument's silence is only informative if we know what it sounds like when the disease is present. This lab runs the *identical* certificate machinery on the two natural siblings where the analogous conjecture **fails or is believed to fail**:

```text
T_{q,eps}(n) = n/2 (n even),  (q n + eps)/2 (n odd)

(3,+1)  Collatz            conjectured: everything reaches 1
(3,-1)  the 3n-1 system    FALSE analogue: nontrivial cycles at 5 and 17 exist
(5,+1)  the 5n+1 system    divergence-typical: almost all orbits believed divergent
```

All certificate notions generalize verbatim: `T^d(n) = (q^{o(d)} n + c_d)/2^d`, coefficient stopping time `tau` (least `d` with `q^{o(d)} < 2^d`), stopping time `sigma`, survivor set `S_{q,eps}` (never-certified 2-adic points), critical density `theta_q = log_q 2`.

## Theorem A (Proved). The sign of the intercept splits the world.

Every term of the accumulated intercept `c_d` carries the factor `eps`, so `sign(c_d) = eps` (and `c_d = 0` iff no odd step occurred). Three consequences, each one line:

1. **`eps = +1` (Collatz, 5n+1): `tau <= sigma`.** Descent `T^d(n) < n` with `c_d >= 0` forces `q^o < 2^d`. Certificates *can* have threshold traps (`tau` fires, descent doesn't); Terras' conjecture (`tau = sigma`) is exactly "no traps."
2. **`eps = -1` (3n−1): `sigma <= tau`.** When `tau` fires, `T^tau(n) <= q^o n / 2^tau < n` because `c <= 0` — descent is *unconditional*. The 3n−1 certificate program has **no thresholds at all**; its only possible counterexample carrier is the frontier itself.
3. **Cycles sit on opposite sides of the critical line.** A positive cycle satisfies `x (2^d - q^o) = c_d`, so `eps = +1` forces `q^o < 2^d` (cycle **below** the line, in certified territory) and `eps = -1` forces `q^o > 2^d` (cycle **above** the line, **inside the survivor set**).

**Measured (`results/sibling_dichotomy.json`):** all seven known cycles across the three maps obey the sign rule. The margins are striking — nontrivial cycles hug the line from the side `eps` dictates:

| cycle | d | o | q^o vs 2^d | margin (bits/period) |
|---|---:|---:|---|---:|
| Collatz trivial (1) | 2 | 1 | 3 < 4 | −0.415 |
| 3n−1, min 1 | 1 | 1 | 3 > 2 | +0.585 |
| 3n−1, min 5 | 3 | 2 | 9 > 8 | **+0.170** |
| 3n−1, min 17 | 11 | 7 | 2187 > 2048 | **+0.095** |
| 5n+1, min 1 | 5 | 2 | 25 < 32 | −0.356 |
| 5n+1, min 13 | 7 | 3 | 125 < 128 | **−0.034** |
| 5n+1, min 17 | 7 | 3 | 125 < 128 | **−0.034** |

## Theorem B (Proved). The word system cannot see `eps`.

For every odd `q` and `eps = ±1`, the map `r mod 2^d -> (first d parities)` is a bijection: if two residues share a parity word, their difference has its 2-adic valuation reduced by exactly 1 per step (each step multiplies it by `q/2` or `1/2`), so a difference `!= 0 mod 2^d` forces a parity split within `d` steps. (Verified exhaustively to depth 10 for all three maps.)

Hence survivor counts `s(d)`, uncertified densities `F(d)`, the box dimension `H(theta_q)`, the word-model mean `E[tau] = sum F(d)`, tail statistics — **every parity-word statistic is identical for `(3,+1)` and `(3,-1)`**. Same Cantor set geometry, same `0.9499555...` dimension, same `2^{-0.0500444 d}` thinning, same `3.4926518...` mean.

## Theorem C (Proved). `S_{3,-1}` contains positive integers: exactly the cycle minima.

The all-odd universal survivor of `T_{q,eps}` is the 2-adic fixed point `x = -eps` (for 5n+1 it is `-1/3`). For Collatz that point is `-1` — not a positive integer, and the whole program survives. For 3n−1 it is `+1`. Moreover the cycle minima 5 and 17 sit above the line (Theorem A.3), and a one-period exact prefix check plus positive per-period surplus proves their whole parity history stays supercritical:

**Measured (`results/sibling_membership.json`):** `1, 5, 17 ∈ S_{3,-1}` with minimum prefix margins +0.585, +0.170, +0.095 bits. The frontier-separation statement `S ∩ Z_{>0} = ∅` — the exact reduction target identified in `FRONTIER-GEOMETRY.md` — is **FALSE for 3n−1** while its word statistics are indistinguishable from Collatz's.

## Corollary (Proved): the invariance barrier.

> **No argument whose hypotheses are invariant under `eps -> -eps` can prove `S_{3,+1} ∩ Z_{>0} = ∅`.** In particular, no proof of the divergence half of Collatz can rest solely on parity-word statistics — densities, entropy, dimension, survivor counts, stopping-time distributions, equidistribution rates — because `(3,-1)` realizes the identical statistics with a nonempty positive-integer survivor set.

Every measure-theoretic result in the literature (Terras, Everett, Krasikov–Lagarias in its density form, Tao's almost-all theorem) is, at the level of its *conclusion about the word system*, `eps`-invariant — which is a precise formalization of why "almost all" cannot become "all" along that axis. Any successful attack must consume the intercepts: the `c_d` terms, the certificate thresholds, the affine translation gaps — the quantities this repo's threshold measurements, repayment/motif suite, and escape-envelope records are built around. The barrier is not a reason to stop; it is a compass needle pointing at the `eps`-sensitive side of the theory.

(Known-in-spirit: the 3n−1 system as a cautionary example is classical folklore — see Lagarias' surveys. The sharp statement that its *certificate frontier statistics are literally identical* while the separation statement flips truth value, with machine-checked certificates on both sides, is what this lab adds.)

## The detector matrix (Measured). The machinery is exactly calibrated.

Theorem A gives each `eps` its unique counterexample carrier, so the scanner has two detectors: **threshold traps** (`tau` fires, no descent — possible only for `eps=+1`) and **frontier residents** (`tau = infinity`, proven for `eps=-1` via supercritical terminal cycles). Scanning all `n <= 10^7` for both `q=3` maps and `n <= 2*10^4` (cap 2048) for 5n+1:

| | (3,+1) Collatz | (3,−1) | (5,+1) |
|---|---|---|---|
| threshold-trap detector | fires on **{1}** = the trivial cycle minimum | **∅** (impossible, Theorem A.2) | cycles 1, 13, 17 live on this side |
| frontier-resident detector | **∅** up to 10^7 (and 10^9 via the main scan) | fires on **{1, 5, 17}** — all three cycle minima, nothing else | fires on **17.555%** of integers |
| verdict | silent everywhere except the trivial cycle | detects exactly its counterexamples | detects divergence-typicality |

- The three flagged 3n−1 integers in 10 million are precisely the three cycle minima — **zero false positives, zero false negatives**. The localization theorem of `FRONTIER-GEOMETRY.md` ("counterexample minima are frontier-pinned") is watched working, at scale, on a system where counterexamples exist.
- For 5n+1 the flagged density 0.17555 matches the word-model survival constant `F_5(infinity) = 0.1760258...` (exact DP, converged by depth 768; `results/sibling_rates5_4096.json`) to **0.3%** — the integers adhere to the divergence frontier at the uniform-mass rate, `E[tau_5] = sum F_5(d)` diverges (partial sum 48.8 at 256 terms and climbing linearly), and the first flagged integer is the canonical suspected-divergent start `n = 7`.
- Mean finite `tau`: 3.4908 for (3,+1) and 3.4940 for (3,−1) at `10^7` — both within 1.5e-3 of the shared word constant 3.4926518 (Theorem B in action: same constant, opposite truth values). For 5n+1: 5.70 and divergent in the limit.
- Deep-tail ratios for (3,−1) show a mild positive drift against the word model (+0.7% at depth 40, +1.5% at 60, +3.3% at 80 — 1.6σ, 2.0σ, 2.6σ — before thinning back into noise at 100), and its finite-`tau` record at `10^7` (273 at n = 5,960,769) exceeds Collatz's (246 at 8,088,063): integers riding near the above-line cycles hold supercritical prefixes slightly longer. Suggestive rather than conclusive at this sample size — but it is the only statistic in the whole suite where the two `q = 3` siblings differ at all, and the difference points at the intercepts, exactly where the barrier says the mathematics must live.

## What this changes for the program

1. **Silence is now evidence.** The instruments provably detect counterexample minima when they exist (3n−1: 3/3 found, nothing else flagged; 5n+1: divergence measured at the predicted density). Their emptiness on 3n+1 through `10^9` is a calibrated reading, not a tautology.
2. **The proof-search space is halved.** The invariance barrier retires every purely word-statistical strategy for the divergence half. What remains is the `eps`-sensitive layer: intercepts, thresholds, repayment structure, endpoint residues — precisely where the concurrent motif/endpoint/envelope labs are digging.
3. **The sharpest sentence version:** the survivor Cantor set is the same for both signs; the only mathematical difference is *which integer the universal all-odd survivor `-eps` is* and *which side of the critical line the attractors live on*. Collatz is the statement that for `eps = +1` nothing positive ever joins `-1` on the boundary. The sibling shows that when the boundary point is positive (`+1` for 3n−1), it and its cycle-mates are exactly what joins.

## Reproduce

```powershell
python experiments/collatz_sibling_control.py selftest
python experiments/collatz_sibling_control.py dichotomy  --out experiments/results/sibling_dichotomy.json
python experiments/collatz_sibling_control.py membership --out experiments/results/sibling_membership.json
python experiments/collatz_sibling_control.py rates --q 5 --max-depth 4096 --out experiments/results/sibling_rates5_4096.json
python experiments/collatz_sibling_control.py scan --q 3 --eps -1 --limit 10000000 --cap 4096 --out experiments/results/sibling_scan_3minus_1e7.json
python experiments/collatz_sibling_control.py scan --q 3 --eps 1  --limit 10000000 --cap 4096 --out experiments/results/sibling_scan_3plus_1e7.json
python experiments/collatz_sibling_control.py scan --q 5 --eps 1  --limit 20000 --cap 2048 --out experiments/results/sibling_scan_5plus_2e4.json
```

Self-test cross-validates: the residue-word bijection for all three maps (depth ≤ 10), the affine law with `eps`, cycle existence/minimality and the sign dichotomy, the `sigma`-vs-`tau` inequalities on 2000 starts per map, frontier residents of 3n−1 below 1000 being exactly {1, 5, 17}, membership certificates, DP vs brute enumeration for `q = 3` and `q = 5`, and agreement of the `q = 3` word system with the main instrument's depth-20/24/28 anchors.
