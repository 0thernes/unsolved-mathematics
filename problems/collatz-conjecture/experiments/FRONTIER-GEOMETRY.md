# Frontier Geometry — the exact shape of the certificate obstruction

_Created: 2026-07-01. Companion to `CERTIFICATE-FRONTIER-THEOREMS.md` and `collatz_frontier_geometry.py`._
_Status: proved statements are labeled **Proved**; exact computations **Measured**; model-based statements **Heuristic**; statements resting on external computation **Conditional**. Nothing here is a proof of the Collatz conjecture._

## Why this document exists

`CERTIFICATE-FRONTIER-THEOREMS.md` ended at a wall: the finite-residue descent certificate can never cover all of the 2-adic integers, because the all-odd parity path (the 2-adic fixed point `-1`) survives every depth. The stated next step was:

> Separate positive integer orbits from the persistent high-odd 2-adic survivor set.

This document makes that survivor set an exact mathematical object. We compute its dimension, its exact density at every depth, the law relating it to stopping times, a localization theorem confining any counterexample orbit to it, and quantitative probes (records, Mersenne spine, equidistribution ratios) that would detect any anomalous adhesion of positive integers to it. All instruments are in `collatz_frontier_geometry.py`; every claim below is reproducible with the commands listed at the end.

## Definitions

Shortcut map: `T(n) = n/2` (n even), `(3n+1)/2` (n odd).

For the first `d` steps of `n`, let `o(d)` = number of odd steps. The affine law (proved in `CERTIFICATE-FRONTIER-THEOREMS.md`) gives `T^d(2^d q + r) = 3^{o} q + T^d(r)` with `o` and `T^d(r)` depending only on `r = n mod 2^d`, and

```text
T^d(n) = (3^{o(d)} n + c_d) / 2^d      with integers c_d >= 0.
```

- **Coefficient stopping time** `tau(n)` = least `d` with `3^{o(d)} < 2^d` (Terras 1976). This is exactly the certificate depth of `n`'s residue class in `collatz_residue_lab.py`.
- **Stopping time** `sigma(n)` = least `d` with `T^d(n) < n`.
- **Survivor set** `S` = the set of 2-adic integers with `3^{o(d)} >= 2^d` for every `d >= 1`, i.e. the points never certified at any finite depth. `S` is a nonempty closed subset of `Z_2` (it contains `-1`).
- `theta = log_3 2 = 0.630929753...` — the critical odd-step density: `3^{o} >= 2^d` iff `o >= theta d`.
- `H(theta) = -theta log2 theta - (1-theta) log2(1-theta) = 0.949955527...` — binary entropy at the critical density.

## Theorem 1 (Proved). Descent forces the coefficient down: `tau(n) <= sigma(n)`.

If `T^d(n) < n` then `(3^{o(d)} n + c_d)/2^d < n` with `c_d >= 0`, so `3^{o(d)} < 2^d`. Hence a coefficient drop happens no later than descent. The converse — whether `tau(n) = sigma(n)` for all `n > 1` — is Terras' **coefficient stopping time conjecture**, still open; it is exactly the statement that no integer sits below its class's certificate threshold at depth `tau`.

**Measured:** `tau(n) = sigma(n)` for every `1 < n <= 10^9` (zero counterexamples; see `results/tau_scan_1e9.json`). The scan's completion is simultaneously a re-verification that `sigma(n) < infinity` for all `n <= 10^9`.

## Theorem 2 (Proved). The frontier has box dimension `H(theta) = 0.9499555...`

Let `s(d)` = number of parity prefixes of length `d` alive at depth `d` (never certified). Then `S` is covered by exactly `s(d)` cylinders of depth `d`, and the uncertified density is `F(d) = s(d)/2^d`.

**Lower bound (rotation lemma).** Let `m = ceil(theta d) + 1`. Every rotation class of a length-`d` word with `m` ones contains at least one word all of whose prefixes satisfy `o(j) - theta j > 0` (rotate to start just after the global minimum of the prefix sums of `epsilon_i - theta`; the minimum is attained because `theta` is irrational, so prefix sums never repeat a value). Words with `o(j) > theta j` for all `j` are alive at all depths `<= d`. Rotation classes have size at most `d`, so

```text
s(d) >= C(d, ceil(theta d) + 1) / d.
```

**Upper bound (union bound).** Any live prefix has final odd count `o >= ceil(theta d) > d/2`, and `C(d, o)` is decreasing in `o` on that range, so

```text
s(d) <= (d + 1) * C(d, ceil(theta d)).
```

By Stirling, both bounds give `(1/d) log2 s(d) -> H(theta)`. Hence the box-counting dimension of `S` (base-2 cylinders) is exactly `H(theta) = 0.9499555271...`, and

```text
F(d) = 2^{ -(1 - H(theta)) d + O(log d) },     1 - H(theta) = 0.05004447...
```

The frontier is a Cantor set of full topological complexity but of measure zero, thinning at only ~0.05 bits per level — this is the precise sense in which the certificate program "almost" closes and never closes.

**Measured (exact bigint DP, 2.5 s, `results/rates_8192.json`):** the DP reproduces the residue miner's frontier counts exactly (27,328 at depth 20; 286,581 at depth 24; 3,524,586 at depth 28 — and log2 F(128) = −13.8069, matching the earlier log's `2^-13.807`) and extends the exactly-known range from enumeration depth 28 to depth 8192:

| depth d | log2 F(d) | local rate −log2F/d | rate − 0.0500444 |
|---:|---:|---:|---:|
| 128 | −13.807 | 0.107866 | +0.057822 |
| 512 | −35.849 | 0.070018 | +0.019974 |
| 1024 | −62.910 | 0.061436 | +0.011391 |
| 2048 | −115.605 | 0.056448 | +0.006403 |
| 4096 | −219.577 | 0.053608 | +0.003563 |
| 8192 | −426.005 | 0.052003 | +0.001958 |

The local rate decreases monotonically toward `1 − H(theta) = 0.0500444...` with the predicted `O(log d / d)` finite-size correction (still +0.0020 at depth 8192; successive halvings of the gap per doubling of depth are visible across the table). At depth 8192 the uncertified fraction is `2^-426 ≈ 10^-128`: the certificate program covers all but one part in `10^128` of every congruence block — and still, by Theorem 3 of `CERTIFICATE-FRONTIER-THEOREMS.md`, can never finish.

## Theorem 3 (Proved). Localization: any counterexample orbit lives on the frontier.

Let an orbit be a **counterexample** if it never reaches 1. Every counterexample orbit has a minimal element `m` (a nontrivial cycle attains its minimum; a non-periodic counterexample visits infinitely many distinct integers, is unbounded, and still attains its infimum). That minimum satisfies `sigma(m) = infinity`.

**(i) If `tau(m) = t < infinity`,** then `T^t(m) >= m` forces `m` below its class threshold: writing `m = 2^t q + r`,

```text
q <= (T^t(r) - r) / (2^t - 3^{o}),   i.e.   m <= maxTheta(t) := max class threshold at depth <= t.
```

**(ii) If `tau(m) > d` for a chosen depth `d`,** then `m` lies in one of the `s(d)` frontier residue classes mod `2^d`.

**Corollary (Measured, fully self-contained).** The depth-28 mining run (`results/residue_lab_28.json`) measures, over **all 502,524 certified leaves of depth `<= 28`**, a maximum threshold of `q_0 = 1`, attained by exactly two leaves, whose sole sub-threshold members are `n = 0` and `n = 1` (`max_q_threshold = 1`, `finite_q_exceptions_upper_bound = 2`, `max_direct_check_n = 1`). `n = 1` is the trivial cycle (`1 -> 2 -> 1` never descends below 1), so case (i) is empty for every `m >= 2`. Therefore, **unconditionally and using nothing outside this repository**:

> **The minimal element of any counterexample orbit — nontrivial cycle or divergent — satisfies `tau(m) > 28`, hence is congruent mod `2^28` to one of the 3,524,586 frontier residues (1.31% of residue classes).** Adding Barina's published verification, it also exceeds `2^71`.

Equivalently: for every residue class certified at depth `<= 28`, *every* member `>= 2` genuinely descends at its certificate depth — the certificate thresholds, which in principle could have trapped counterexamples beneath them, are empirically vacuous through depth 28. The same argument at any depth `d` confines counterexample minima to a set of density `F(d) -> 0` (Theorem 2), provided the thresholds at that depth are re-measured; deeper leaves sit closer to the critical line `3^o ≈ 2^d`, where thresholds can in principle blow up. This turns Theorem 3 of `CERTIFICATE-FRONTIER-THEOREMS.md` from an obstruction ("the frontier never empties") into a weapon ("everything bad is trapped on the frontier").

**(iii) If `m` is in `S` itself (`tau(m) = infinity`),** then `T^d(m) >= (3^{o(d)}/2^d) m >= m` for all `d`, and the orbit cannot be eventually periodic: a cycle with `o_c` odd steps in `d_c` satisfies `x(2^{d_c} - 3^{o_c}) = c > 0`, so `3^{o_c} < 2^{d_c}`, making the long-run odd density `o_c/d_c < theta` and eventually violating `3^{o(d)} >= 2^d`. So a positive integer in `S` would have an unbounded, never-descending orbit.

**Remark (Proved): what Terras' coefficient conjecture would settle.** The periodicity computation in (iii) shows every cycle minimum `m` has `tau(m) < infinity` while `sigma(m) = infinity`. Hence:

1. **Terras' conjecture (`tau = sigma` for all `n >= 2`) already implies the full no-nontrivial-cycle half of Collatz** — a cycle minimum would have `tau(m)` finite and `sigma(m)` infinite, contradicting equality. (The trivial cycle survives only because `n = 1` is excluded: `tau(1) = 2`, `sigma(1) = infinity`.)
2. Under Terras, case (i) is empty, so **divergent orbits exist iff `S` contains a positive integer**.

So the entire conjecture reduces, modulo Terras' conjecture, to `S ∩ Z_{>0} = ∅` — the frontier-separation statement. The threshold measurements below are exactly the depth-by-depth finite verification of Terras' conjecture: `tau(n) = sigma(n)` holds for every `n >= 2` with `tau(n) <= 28` (all classes, all members, no exceptions), and the direct scan confirms it pointwise for all `n <= 10^9`.

## Theorem 4 (Proved identity + Heuristic slope). The Mersenne spine is the integer shadow of `-1`.

`2^j - 1 ≡ -1 mod 2^j` is the depth-`j` integer truncation of the surviving 2-adic fixed point. The identity

```text
T^k(2^j - 1) = 3^k 2^{j-k} - 1,   0 <= k <= j
```

(proved by induction; verified in the selftest) shows the first `j` steps are forced odd, giving an odd-count surplus of `j(1 - theta)` bits over the critical line. If the continuation behaves measure-typically (odd density 1/2 < theta), the deficit is repaid at rate `theta - 1/2` per step, predicting

```text
tau(2^j - 1) ~ j / (2 theta - 1) = 3.8188416... j.
```

**Measured (`results/mersenne_1024.json`):** over `j` in the upper half of `[1, 1024]`, `tau(2^j - 1)/j` has mean **3.7719** (min 3.4157, max 4.2250) against the predicted **3.8188** — the integer approximants to `-1` detach from the frontier at the model rate. No anomalous adhesion: the deepest positive-integer corridor of the frontier currently shows *zero* measurable extra structure. A persistent excess here would have been the first quantitative sign of an integer orbit tracking the `-1` boundary; the measurement says the boundary repels integers exactly as fast as coin-flipping predicts.

## Theorem 5 (Heuristic ceiling + Measured records). The record constant `1/(1 - H(theta)) = 19.9822...`

`tau(n) > gamma log2 n` means `n` lies in the frontier at depth `gamma log2 n`, an event of density `F(gamma log2 n) ≈ n^{-gamma (1 - H(theta))}`. Summing over `n`: the expected number of such `n` is finite iff `gamma > 1/(1 - H(theta)) = 19.98222668...`. Borel–Cantelli then predicts

```text
limsup_n  tau(n) / log2 n  =  19.9822...      (random model)
```

An integer family beating this ceiling infinitely often would be genuine positive-integer structure inside the frontier; an integer with `tau = infinity` would be a divergent orbit (Theorem 3(iii)). The concurrently developed `ESCAPE-ENVELOPE.md` reaches the same constant from the other side, as the slope `c*` of the first-moment envelope `D_1(b) ~ 19.982 b` for worst certificate depth over `b`-bit starts — the limsup form here and the envelope form there are the same conjectural law.

**Measured (`results/tau_scan_1e9.json`, 392 s):** the `tau`-record holders up to `10^9` are exactly the classical stopping-time record integers — 27, 703, 10087, 35655, 270271, 362343, 381727, 626331, 1027431, 1126015, 8088063, 13421671, 20638335, 26716671, 56924955, 63728127, 217740015 — an independent reproduction of the known record table. Record `gamma`: 12.408 at `n = 27`, then 12.12 (13,421,671), **14.503 (63,728,127)**, 14.26 at the deepest record `n = 217,740,015` (`tau = sigma = 395`). All records have `tau = sigma` exactly. The records crawl toward the `19.982` ceiling from below and remain far from it, consistent with the extreme-value prediction (convergence is `O(log log n / log n)`-slow).

## Theorem 6 (Proved, Conditional on the verification floor). In-repo cycle floor: `>= 1.28 x 10^11` standard steps.

For a nontrivial cycle of the Syracuse (odd-to-odd) form with odd elements `a_1, ..., a_o` and `d` total shortcut steps, multiplying the cycle relations gives the exact product formula

```text
2^d / 3^o = prod_i (1 + 1/(3 a_i)),   hence   0 < d ln2 - o ln3 < o / (3 n_min),
```

where `n_min` is the least cycle element. Dividing by `o ln 2`:

```text
0 < d/o - log2 3 < 1/(3 n_min ln 2) <= 1/(3 B ln 2) =: eps,    B = 2^71 (Barina 2025).
```

If `o <= o* := floor(sqrt(3 B ln2 / 2))` then `eps < 1/(2 o^2)`, and Legendre's criterion forces `d/o` (in lowest terms) to be a continued fraction convergent of `log2 3` lying above it. The instrument computes an **interval-certified** continued fraction of `log2 3` from exact integer arithmetic (atanh series for `ln 2`, `ln 3` with explicit floor/tail error budgets — no floating point anywhere in the chain), certifies 300+ partial quotients, and checks every convergent `p/q` above `log2 3` with `q <= o*`:

**Measured (`results/cycle_floor_71.json`):** the cap is `o* = 49,547,666,543`, and every above-side convergent with `q <= o*` (q = 1, 5, 41, 306, 15601, 79335, 190537, 10781274, 397573379, 6586818670) has `p/q - log2 3` at least `2.217 x 10^-21` — **10.9x the allowed `eps = 2.037 x 10^-22`** — so all are excluded, no qualifying convergent exists below the cap, and therefore:

> Every nontrivial Collatz cycle has at least **49,547,666,544 odd steps**, at least **78,531,193,471 shortcut steps**, hence at least **128,078,860,015 standard Collatz steps**.

This is weaker than Hercher 2023 (`>= 1.375 x 10^11` odd terms via exclusion of all `m <= 91`-cycles) but is proved end-to-end inside this repo from: (a) the product formula, (b) Legendre's theorem, (c) exact interval arithmetic, (d) the published verification floor. Nothing else. The near-miss convergent is instructive: `q = 6,586,818,670` fails by a factor of 10.9 — the entire cycle problem below `o*` hinges on `log2 3` refusing to have an unusually good rational approximant at that scale, which is exactly the transcendence-theoretic wall `approaches.md` describes.

Note: the concurrently developed `CYCLE-BOUND-LAB.md` derives a sharper in-repo floor (`>= 65,470,613,321` odd steps) from the same `2^71` input using the three-distance best-approximation inequality `||k log2 3|| > 1/(q_j + q_{j+1})` instead of Legendre's criterion — it climbs one further rung of the same convergent ladder (its binding denominator `q = 65,470,613,321` is the convergent right after this instrument's cap). The two derivations are independent implementations and their agreement on the ladder structure is itself a check.

## Theorem 7 (Proved identity + Measured match). The mean of `tau` is an exact frontier sum.

Since `P(tau > d)` over a full period `2^d` is exactly `F(d)`:

```text
E[tau] = sum_{d >= 0} F(d)  =  3.49265182...   (exact DP, 400 terms)
```

**Measured:** mean of `tau(n)` is **3.492657** over `n <= 10^8` and **3.492689** over `n <= 10^9` — agreement with the exact 2-adic constant to `~4 x 10^-5`, a five-significant-digit consistency lock between the abstract model and the integers (the residual is the finite-`N` boundary term from depths `2^d > N`).

## Equidistribution ratios (Measured): where integer-vs-shadow structure would first appear.

For depths `2^d > N`, the ratio `#{n <= N : tau(n) > d} / (N F(d))` is not forced to 1; it measures whether the first `N` integers occupy the frontier cylinders like uniform 2-adic mass. At `N = 10^9` (`2^d/N` up to `10^39`):

| depth | observed | expected `N·F(d)` | ratio |
|---:|---:|---:|---:|
| 40 | 5,823,631 | 5,823,344.5 | 1.000049 |
| 60 | 1,922,785 | 1,922,190.7 | 1.000309 |
| 80 | 664,945 | 664,399.7 | 1.000821 |
| 100 | 239,273 | 238,678.3 | 1.002492 |
| 120 | 99,023 | 98,794.9 | 1.002309 |
| 140 | 39,396 | 39,629.5 | 0.994107 |
| 160 | 16,998 | 17,257.7 | 0.984949 |

Every ratio through depth 160 sits within ~1.5% of 1 (within ~2 standard deviations of the correlated-cluster fluctuation scale). The integers thread a Cantor set 39 orders of magnitude sparser than their own range at the exact uniform-mass rate. Any *systematic, growing* departure at depths far beyond `log2 N` is the falsifiable signature this instrument is designed to catch; none is present.

## What this adds up to

1. The certificate program's obstruction is now an exactly-known object: a Cantor set of box dimension `0.9499555...`, density `2^{-0.05 d}` at depth `d`, mean-field constant `E[tau] = 3.4926518...` — all three confirmed against the integers to 5+ digits.
2. Any counterexample orbit is **provably pinned** to that set (Theorem 3): its minimum exceeds `2^71` and lies in an explicit 1.31%-density residue set mod `2^28`, with the density shrinking exponentially as the pinning depth grows.
3. The two live probes for *positive-integer* anomalies — the Mersenne spine hugging `-1`, and the record constant `19.9822...` — both currently read "measure-typical, no structure," to the resolution measured.
4. The cycle half is reproduced in-repo at `1.28 x 10^11` standard steps with a fully certified arithmetic chain, exhibiting concretely that the wall is the quality of rational approximations to `log2 3`.

The honest summary is unchanged in kind but sharpened in degree: every measurable statistic of the integers matches the measure model to the precision measured, while both open halves (divergence, cycles) are confined to explicitly computable, exponentially thin exceptional sets. The missing mathematics is a mechanism that forbids a *single* integer from living in a set whose every statistic says it is empty of integers — precisely the distributional-to-pointwise gap the literature identifies as the heart of the problem.

## Reproduce everything

```powershell
python experiments/collatz_frontier_geometry.py selftest
python experiments/collatz_frontier_geometry.py constants
python experiments/collatz_frontier_geometry.py rates --max-depth 8192 --out experiments/results/rates_8192.json
python experiments/collatz_frontier_geometry.py tau-scan --limit 1000000000 --tails 10,20,26,30,34,40,60,80,100,120,140,160 --out experiments/results/tau_scan_1e9.json
python experiments/collatz_frontier_geometry.py mersenne --max-j 1024 --out experiments/results/mersenne_1024.json
python experiments/collatz_frontier_geometry.py cycle-floor --verified-bits 71 --digits 320 --out experiments/results/cycle_floor_71.json
python experiments/collatz_residue_lab.py --max-depth 28 --sample-limit 4 > experiments/results/residue_lab_28.json
```

The selftest cross-validates: DP vs brute enumeration (depth 14), DP vs the residue miner's logged frontier counts (depths 20/24/28), `tau`/`sigma` vs brute force (`n <= 3000`), `tau(27) = sigma(27) = 59`, the Mersenne identity, the interval `ln` bounds and continued fraction prefix, and the rotation-lemma/union-bound sandwich (depths 6–20).
