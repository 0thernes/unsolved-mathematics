# Stochastic-Model Check — Collatz Dossier Computational Appendix

_Created: 2026-07-01. Status: verification/exploration instrument, not proof._

Companion to [`FABLE5-ULTRACODE-COLLATZ-LOG.md`](FABLE5-ULTRACODE-COLLATZ-LOG.md)
(residue-descent certificates). That instrument probes the **certificate**
side of the problem; this one probes the **stochastic model** — the
Lagarias–Weiss random-walk heuristic that underlies every density result from
Terras (1976) to Tao (2019). If integer trajectories deviated measurably from
the model, that would be news. They don't; the value of recording this is
(a) reproducibility, (b) an exact cross-check between two independent
implementations in this repo, and (c) keeping the honest boundary visible:
distributional agreement is *evidence about typicality*, and typicality is
precisely what the open problem is **not** about.

## What was run

```powershell
python experiments/stochastic_model_check.py --limit 1000000 --depth 24
python experiments/stochastic_model_check.py --limit 5000000 --depth 28
```

Runtime: under 3 s each (single memoized pass; each `n` is walked only to its
first descent, then composed with cached results).

## Results (2026-07-01)

| Quantity | Model prediction | Measured (N = 10⁶) | Measured (N = 5·10⁶) |
|---|---:|---:|---:|
| Mean total stopping time / ln n (shortcut steps) | 2/ln(4/3) ≈ 6.9521 | 6.8526 | 6.8583 |
| Odd-step fraction along complete trajectories | → 1/2 | 0.49652 | 0.49681 |
| Descent-time distribution, max deviation from exact prefix count (k ≤ depth) | 0 (Terras equidistribution) | 2.38×10⁻⁵ | 2.21×10⁻⁵ |
| Undecided-within-depth fraction | 0.01708155870437622 (d=24) / 0.013130106031894684 (d=28) | 0.017083 | 0.013147 |

Path records (classic map) within range reproduce the known record-holder
sequence (OEIS A006884): …, 159487, 270271, 665215, 704511, 1042431, 1212415,
1441407, … with matching peaks (e.g. 9663 → 27,114,424; 704511 → 56,991,483,520).

## Cross-validation between the two instruments

The parity-prefix DP in `stochastic_model_check.py` (survivors of
`3^o ≥ 2^k`) and the residue enumeration in `collatz_residue_lab.py` /
`collatz_survivor_dp.py` are independent implementations of logically
equivalent counts. They agree to full float precision:

| Depth | This DP: model undecided fraction | Residue lab: frontier fraction |
|---:|---:|---:|
| 24 | 0.01708155870437622 | 0.01708155870437622 |
| 28 | 0.013130106031894684 | 0.013130106031894684 |

This is expected (both count parity prefixes above the `o ≥ k·log₃2` line,
by Terras equidistribution) but worth pinning: it certifies that the two
instruments implement the same mathematics without shared code.

## Extreme-value check (gamma records)

Lagarias–Weiss (*Ann. Appl. Prob.* **2** (1992) 229–261) predict
limsup γ(n) = σ∞(n)/ln n → **41.677647** (shortcut steps), attained along
trajectories with odd-step ratio → **0.609091** (note 1/(ln 2 − 0.609091·ln 3) ≈ 41.68).
Measured record sequence to N = 5·10⁶ — which reproduces the known
total-stopping-time record holders (e.g. 837799: σ∞ = 329 shortcut = 524
classic steps):

| n | σ∞ (shortcut) | γ(n) | ones-ratio |
|---:|---:|---:|---:|
| 27 | 70 | 21.24 | 0.5857 |
| 230631 | 278 | 22.51 | 0.5899 |
| 626331 | 319 | 23.90 | 0.5925 |
| 837799 | 329 | 24.12 | 0.5927 |
| 1723519 | 349 | 24.30 | 0.5931 |
| 3732423 | 374 | 24.71 | 0.5936 |

Two honest readings: (a) the record trajectories' ones-ratios climb exactly
along the predicted extremal profile toward 0.609 — the model is confirmed
even in its large-deviations regime, as far as we can see; (b) the record γ
(24.7) is still far below the predicted limsup (41.68), and closes the gap
only logarithmically in N — the true extreme tail, the only place a
counterexample could live, is computationally unreachable. Both readings are
the same fact.

## Cross-verification of the frontier-escape claim, and the two extremal slopes

Independent re-computation (2026-07-01, separate code path from
`frontier_escape_analyzer.py`) confirms the companion suite's headline
number: the depth-28 worst frontier representative **217,740,015** attains
its first usable certificate at shortcut depth **395** (odd count 249, image
171,507,217 < n), with the coefficient condition and true descent coinciding
at that depth.

The check exposes a clean structural distinction between the two suites'
extremal statistics:

- **Survival slope.** A frontier survivor must keep `3^o ≥ 2^d` at every
  prefix, i.e. ones-ratio ≥ log₃2 ≈ **0.63093** throughout; at first
  crossing the ratio sits just below it (measured for the representative:
  0.6304, with d/ln n ≈ 20.6).
- **Record slope.** Total-stopping-time record trajectories (γ records
  above) average ones-ratio → **0.609091**, the Lagarias–Weiss extremal
  profile for reaching 1 as slowly as possible.

The survival line is strictly steeper than the record line: staying above
your starting value costs more odd steps per step than merely descending
slowly. Survivor mass accordingly thins like the measured DP decay
(≈ 2^(−13.8) at depth 128) yet never vanishes (the all-odd path). Both
slopes are now measured in-repo and agree with the random-walk model; as
always, this constrains where hardness can live without proving it lives
nowhere.

## Honest interpretation

- **What agrees:** drift constant, stopping-time scaling, odd-step fraction,
  descent-time distribution, record structure. The integers behave, in every
  measured aggregate, exactly like the random model predicts — consistent
  with 90 years of experience.
- **What this cannot show:** anything about individual exceptional orbits.
  The conjecture fails only on a (possibly empty) set that all of these
  statistics are blind to. Perfect distributional agreement is fully
  compatible with the conjecture being false.
- **The one structural fact worth carrying forward** (from the companion
  log, reproduced here independently): the surviving prefix set thins like
  ~2^{-0.108 d} (depth-128 survivor fraction ≈ 2^{-13.8}) but never empties —
  the all-odd path survives every depth because it shadows the 2-adic fixed
  point −1. A descent-cover proof must separate ℤ⁺ from that boundary set;
  no amount of computation along these lines can do it.
