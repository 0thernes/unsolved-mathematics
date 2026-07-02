# Alignment Dichotomy Repair

This note is a follow-up to `KICK-REPULSION-CLAIM-AUDIT.md`.

The audit found a real gap in the positive-kick proof claim: counted
high-alignment repulsions do not pay all excess debt for every checked start.
The failures were not Collatz counterexamples. They were quick descents with
`max_align <= 2`, meaning the orbit never entered the event regime where the
repulsion detector counts a high-alignment kick/carry break.

The repaired theorem target is a dichotomy:

```text
low alignment:   max_align < 3  -> prove quick descent / direct potential drop
high alignment:  max_align >= 3 -> prove kick/carry repulsion pays excess debt
```

Here `max_align` is the maximum `v2(x + 1)` alignment recorded by
`master_kick_rejection_lemma.py` at the start and before odd shortcut steps.
The existing counted repulsion events are triggered only in the high-alignment
regime, with `pre_align >= 3`.

This remains finite evidence, not a proof. The point is to turn a broken
single-mechanism claim into a falsifiable two-branch obligation.

## Instrument

Script:

```text
experiments/alignment_dichotomy_analyzer.py
```

Result:

```text
experiments/results/alignment_dichotomy_20260702.json
```

Command:

```powershell
python experiments/alignment_dichotomy_analyzer.py --limit-scan 1000000 --frontier-base-depth 28 --frontier-max-depth 1024 --frontier-sample-stride 1024 --frontier-sample-offsets 0 256 512 768 --top-n 12 --output experiments/results/alignment_dichotomy_20260702.json --quiet
```

Population checked:

```text
total starts checked:                 1,013,816
initial scan:                         999,999  (2..1,000,000)
hard records / hard seeds:                 34
base-29 transfer-failure starts:           15
sampled base-28 frontier shadows:      13,768
```

This is the same population used by the positive-kick claim audit.

## Results

Alignment split:

```text
low-alignment starts:                 732,062
high-alignment starts:                281,754
```

Low-alignment branch (`max_align < 3`):

```text
count:                                732,062
all certified descent:                true
max escape depth:                     32
max steps per bit:                    2.0
avg steps per bit:                    0.186753456
max excess:                           1.274194
violations of 2.0*bitlen + 16:         0
```

High-alignment branch (`max_align >= 3`):

```text
count:                                281,754
all certified descent:                true
all repulsions sufficient:            true
max escape depth:                     738
max steps per bit:                    14.4615
avg steps per bit:                    0.661209519
max excess:                           42.591095
repulsion-sufficiency failures:        0
```

Global checks:

```text
uncertified starts:                    0
gamma-bound violations:                0
high-alignment repulsion failures:     0
low-alignment quick-bound failures:    0
```

The broad gamma bound remains:

```text
escape_depth(n) <= 19.982226683919038 * bitlen(n) + 32
```

The low-alignment stress bound tested here is:

```text
escape_depth(n) <= 2.0 * bitlen(n) + 16
```

## Representative Edge Cases

Worst low-alignment escape cases:

| Start | Group | Bits | Escape Depth | Steps/Bit | Max Excess | Max Align | Counted Repulsions |
|---:|---|---:|---:|---:|---:|---:|---:|
| `174,522,363` | sampled frontier shadows | 28 | 32 | 1.1429 | 1.226756 | 2 | 0 |
| `112,451,579` | sampled frontier shadows | 27 | 31 | 1.1481 | 1.226756 | 2 | 0 |
| `678,907` | initial scan | 20 | 24 | 1.2000 | 1.119545 | 2 | 0 |

These are exactly the kind of cases that broke the old single-mechanism
claim: excess rises above `1`, but no high-alignment repulsion event is counted.
The repaired branch says they must be handled by a direct quick-descent lemma.

Worst high-alignment ratio cases:

| Start | Group | Bits | Escape Depth | Steps/Bit | Max Excess | Max Align | Counted Repulsions |
|---:|---|---:|---:|---:|---:|---:|---:|
| `63,728,127` | hard records | 26 | 376 | 14.4615 | 8.131880 | 9 | 85 |
| `217,740,015` | hard records | 28 | 395 | 14.1071 | 7.884256 | 10 | 98 |
| `13,421,671` | hard records | 24 | 287 | 11.9583 | 10.003801 | 12 | 88 |
| `26,716,671` | hard records | 25 | 298 | 11.9200 | 10.144215 | 12 | 78 |
| `56,924,955` | hard records | 26 | 308 | 11.8462 | 10.063574 | 12 | 84 |

Largest counted-repulsion case:

```text
start:                  2,358,909,599,867,980,429,759
bits:                   71
escape depth:           738
steps per bit:          10.3944
max excess:             42.591095
max align:              12
minimum repulsions:     42
counted repulsions:     196
```

## Theorem Target

The single sentence proof target is now:

```text
For every positive integer n, either the shortcut orbit remains low-alignment
and descends within O(bitlen(n)) by a direct low-alignment potential, or it
enters the high-alignment regime often enough that the positive-kick/carry
repulsion count pays the excess debt and forces certified descent.
```

The missing mathematical work is therefore split into two explicit lemmas:

1. Low-alignment lemma: if `max_align < 3` until descent, prove a bound of the
   form `escape_depth <= C_low * bitlen(n) + A_low`. The run supports the very
   strong candidate `C_low = 2`, `A_low = 16` on the checked population.
2. High-alignment lemma: if `max_align >= 3`, prove that the counted kick/carry
   repulsion events lower the relevant excess/potential enough to force
   descent. The run found zero failures of this branch on the checked
   population.

This repairs the audit gap without pretending the conjecture is solved. The
next proof attempt should formalize these two lemmas and then connect them to
the certificate-frontier induction.

## Low-Alignment Follow-Up

The low branch now has its own structural analyzer:

```text
experiments/low_alignment_structure_analyzer.py
experiments/results/low_alignment_structure_20260702.json
```

The exact local mechanism is:

```text
odd x == 1 or 5 mod 8:     T^2(x) = (3x+1)/4 < x
odd x == 3 mod 8:          T^3(x) = (9x+5)/8
repeat gate:               x == 59 mod 64
repeat rank drop:          v2(T^3(x)+5) = v2(x+5) - 3
```

On the same `1,013,816` checked starts, the analyzer found `0` repeat-law
failures, max low escape depth `32`, max low repeat-gate count `6`, and max
observed low `v2(x+5)` of `19`. See
[`LOW-ALIGNMENT-STRUCTURE.md`](LOW-ALIGNMENT-STRUCTURE.md).

## High-Alignment Follow-Up

The high branch now has its own structural analyzer:

```text
experiments/high_alignment_ladder_analyzer.py
experiments/results/high_alignment_ladder_20260702.json
```

The exact local mechanism is:

```text
odd x = 2^a q - 1, a >= 3:
T^k(x) = 3^k 2^(a-k) q - 1      for 0 <= k <= a
ladder credit = a - 2
```

On the same `1,013,816` checked starts, the analyzer found `281,754` high
descents, `428,318` high ladders, total ladder credit `888,579`, `0` formula
failures, `0` alignment-burn failures, and `0` high-branch credit failures.
See [`HIGH-ALIGNMENT-LADDER.md`](HIGH-ALIGNMENT-LADDER.md).

## Branch-Potential Bridge

The two local grammars now have a combined bridge analyzer:

```text
experiments/branch_potential_analyzer.py
experiments/results/branch_potential_20260702.json
```

The tested credit is:

```text
C_unit = sum_high_ladders(v2(x+1)-2)
       + count_low_repeat_gates(x == -5 mod 64)
```

against the observed excess requirement

```text
R = ceil(max(0, max_t(odd_steps_t - theta*t) - 0.999)),
theta = log(2) / log(3).
```

On the same `1,013,816` checked starts, the analyzer found `0` uncertified
starts, `0` `C_unit` failures, and `0` rank-credit failures. The class split
was:

```text
high-assisted descents:       281,754
low-direct descents:          703,125
low-repeat descents:           28,937
```

This turns the dichotomy into one branch-potential theorem target:

```text
Prove universally that high ladder credits plus one unit per low -5 mod 64
repeat dominate positive excess debt, and prove those credits realize enough
height loss to force descent below the starting integer.
```

See [`BRANCH-POTENTIAL.md`](BRANCH-POTENTIAL.md).
