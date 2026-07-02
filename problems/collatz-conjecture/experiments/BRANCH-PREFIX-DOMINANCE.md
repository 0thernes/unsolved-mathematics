# Branch-Prefix Dominance

This note strengthens the branch-potential bridge from a terminal ledger to a
prefix-local ledger.

The previous branch-potential run asked:

```text
Does total structural credit before first descent pay total excess debt?
```

This run asks:

```text
At every prefix before first descent, has visible structural credit already
paid the excess debt seen so far?
```

That is a sharper and more proof-shaped question. It still is not a proof of
Collatz.

## Prefix Ledger

Use the shortcut Collatz map:

```text
T(n) = n/2            if n is even
T(n) = (3n + 1)/2    if n is odd
```

At time `t`, define:

```text
theta = log(2) / log(3)
E_t = odd_steps_t - theta * t
M_t = max_{s <= t} E_s
R_t = ceil(max(0, M_t - 0.999))
```

Credit is assigned at event entry:

```text
high ladder entry: x = 2^a q - 1, a >= 3  pays a - 2
low repeat entry:  x == -5 mod 64         pays 1
```

Let `C_t` be cumulative entry-visible credit through time `t`. The tested
prefix inequality is:

```text
C_t >= R_t
```

for every observed prefix up to first descent below the starting integer.

## Instrument

Script:

```text
experiments/branch_prefix_dominance_analyzer.py
```

Result:

```text
experiments/results/branch_prefix_dominance_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_dominance_analyzer.py --population combined --limit-scan 1000000 --frontier-base-depth 28 --frontier-max-depth 1024 --frontier-sample-stride 1024 --frontier-sample-offsets 0 256 512 768 --low-max-h 96 --high-max-a 96 --max-q 63 --max-bits 160 --boundary-width 63 --random-count 2000 --biased-count 2000 --stress-frontier-base-depth 28 --stress-frontier-max-depth 1024 --stress-frontier-sample-stride 1024 --stress-frontier-sample-offsets 128 384 640 896 --top-n 12 --output experiments/results/branch_prefix_dominance_20260702.json --quiet
```

The combined population includes the full branch-potential baseline plus the
adversarial stress families. Some starts are counted in more than one group.

## Result

Global summary:

```text
total checked:                1,046,948
unique starts checked:        1,044,917
uncertified:                          0
prefix C_unit failures:               0
max prefix deficit:                   0
min prefix surplus:                   0
max prefix required credit:          59
```

Class split:

```text
high-assisted descents:         305,711
low-direct descents:            710,326
low-repeat descents:             30,911
```

Group summary:

| Group | Count | Max Escape | Max Excess | Max Prefix Required | Prefix Failures |
|---|---:|---:|---:|---:|---:|
| baseline/initial_scan | `999,999` | `176` | `9.917458625` | `9` | `0` |
| baseline/hard_records | `34` | `738` | `42.591094525` | `42` | `0` |
| baseline/transfer_failure_starts | `15` | `260` | `7.191652814` | `7` | `0` |
| baseline/sampled_frontier_shadows | `13,768` | `249` | `11.061673411` | `11` | `0` |
| stress/hard_records | `34` | `738` | `42.591094525` | `42` | `0` |
| stress/low_repeat_spines | `2,912` | `230` | `9.014235382` | `9` | `0` |
| stress/high_ladder_spines | `3,008` | `508` | `38.443078339` | `38` | `0` |
| stress/near_boundaries | `9,792` | `699` | `59.051239429` | `59` | `0` |
| stress/fresh_frontier_shadows | `13,768` | `283` | `14.740041193` | `14` | `0` |
| stress/random_high_bit | `2,000` | `189` | `5.822582568` | `5` | `0` |
| stress/biased_boundary_random | `1,618` | `500` | `37.228656861` | `37` | `0` |

The result is sharp: `min prefix surplus = 0`. The instrument did not pass by
adding a loose buffer.

## Largest Prefix Pressure

The largest required prefix credit was the `160`-bit near-boundary case:

```text
start:                  1,461,501,637,330,902,918,203,684,832,716,283,019,655,932,542,975
bits:                   160
escape depth:           666
max excess:             59.051239429
max prefix required:    59
high ladder credit:     222
low repeat credit:      5
C_unit:                 227
max prefix deficit:     0
```

The longest escape remained the inherited hard record:

```text
start:                  2,358,909,599,867,980,429,759
bits:                   71
escape depth:           738
max excess:             42.591094525
max prefix required:    42
high ladder credit:     196
low repeat credit:      4
C_unit:                 200
max prefix deficit:     0
```

## Theorem Target

The sharper theorem target is now:

```text
For every positive integer n > 1, along the shortcut orbit before first descent
below n, the entry-visible structural credit

  C_t = sum_{high ladder entries <= t} (v2(x+1)-2)
      + count_{low repeat entries <= t}(x == -5 mod 64)

dominates

  R_t = ceil(max(0, max_{s<=t}(odd_steps_s - theta*s) - 0.999))

at every prefix t.
```

This target is stronger than the terminal branch-potential inequality because
it forbids temporary debt. It suggests a proof shape by induction on the
current visible event rather than by retrospective accounting.

## Honest Boundary

This does not solve Collatz. It says that a sharper, localized version of the
candidate potential survived:

* the full million-start baseline,
* inherited hard records and transfer failures,
* sampled base-28 frontier shadows,
* long low-repeat spines,
* long high-ladder spines,
* near-boundary starts up to `160` bits,
* fresh frontier offsets,
* random and biased high-bit starts.

The missing proof is still universal. One must show that every positive finite
shadow either receives visible entry credit before prefix excess can outrun it,
or drops into a low/direct descent class before any credit is needed.

## Exact Frontier Follow-Up

The companion exact-frontier pass is documented in
[`BRANCH-PREFIX-FRONTIER-EXACT.md`](BRANCH-PREFIX-FRONTIER-EXACT.md).

It checks every positive live residue in the exact base-24 certificate survivor
frontier:

```text
positive residues checked:      286,581
uncertified:                          0
prefix C_unit failures:               0
max prefix deficit:                   0
max prefix required credit:          13
```

The exact frontier split into `286,575` high-assisted descents and only `6`
low-repeat descents. This makes the next proof target more specific: show that
prefix dominance is preserved, or newly paid by visible branch credit, under
frontier lifts from depth `d` to deeper finite shadows.

The first exact lift audit, [`BRANCH-PREFIX-FRONTIER-LIFT.md`](BRANCH-PREFIX-FRONTIER-LIFT.md),
checks depths `24`, `25`, and `26`, totaling `1,897,117` live frontier rows
with `0` prefix failures and `0` orphan live children.
