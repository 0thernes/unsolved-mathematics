# Branch-Potential Stress

This note records an adversarial falsification pass for
[`BRANCH-POTENTIAL.md`](BRANCH-POTENTIAL.md).

The baseline branch-potential run checked the inherited million-start
population. This stress run instead generates starts that deliberately sit on
the two local grammar boundaries:

* low repeat spines: `x = 2^h q - 5`, forcing the `-5 mod 64` repeat gate;
* high ladders: `x = 2^a q - 1`, forcing `v2(x + 1)` boundary ladders;
* near powers of two up to `160` bits;
* fresh base-28 frontier-shadow offsets not used in the baseline run;
* random high-bit and biased boundary-random starts.

The goal is to break the proposed finite ledger:

```text
C_unit = sum_high_ladders(v2(x+1)-2)
       + count_low_repeat_gates(x == -5 mod 64)

R = ceil(max(0, max_t(odd_steps_t - theta*t) - 0.999)),
theta = log(2) / log(3).
```

A positive `R - C_unit` is a concrete counterexample to the candidate ledger.

## Instrument

Script:

```text
experiments/branch_potential_stress.py
```

Result:

```text
experiments/results/branch_potential_stress_20260702.json
```

Command:

```powershell
python experiments/branch_potential_stress.py --low-max-h 96 --high-max-a 96 --max-q 63 --max-bits 160 --boundary-width 63 --random-count 2000 --biased-count 2000 --frontier-base-depth 28 --frontier-max-depth 1024 --frontier-sample-stride 1024 --frontier-sample-offsets 128 384 640 896 --top-n 12 --output experiments/results/branch_potential_stress_20260702.json --quiet
```

## Result

Global result:

```text
total checked:                  33,132
uncertified:                         0
C_unit failures:                     0
C_rank failures:                     0
max unit-credit deficit:             0
min C_unit surplus:                  0
```

Class split:

```text
high-assisted descents:         23,957
low-direct descents:             7,201
low-repeat descents:             1,974
```

Group summary:

| Group | Count | Max Escape | Max Excess | C_unit Failures | Min C_unit Surplus |
|---|---:|---:|---:|---:|---:|
| hard records | `34` | `738` | `42.591094525` | `0` | `9` |
| low repeat spines | `2,912` | `230` | `9.014235382` | `0` | `1` |
| high ladder spines | `3,008` | `508` | `38.443078339` | `0` | `0` |
| near boundaries | `9,792` | `699` | `59.051239429` | `0` | `0` |
| fresh frontier shadows | `13,768` | `283` | `14.740041193` | `0` | `1` |
| random high bit | `2,000` | `189` | `5.822582568` | `0` | `0` |
| biased boundary random | `1,618` | `500` | `37.228656861` | `0` | `0` |

The largest excess stress case was a `160`-bit near-boundary integer:

```text
start:               1461501637330902918203684832716283019655932542975
bits:                160
escape depth:        666
max excess:          59.051239429
required credit:     59
high ladder credit:  222
low repeat gates:    5
C_unit:              227
C_unit surplus:      168
```

The longest escape in the stress run was still the inherited hard record:

```text
start:               2,358,909,599,867,980,429,759
bits:                71
escape depth:        738
max excess:          42.591094525
required credit:     42
C_unit:              200
C_unit surplus:      158
```

Tight cases still exist with zero surplus; the first tight stress example is:

```text
start:               39
group:               high_ladder_spines
bits:                6
escape depth:        8
max excess:          1.214421479
required credit:     1
C_unit:              1
C_unit surplus:      0
```

So the stress pass did not merely add large loose examples. It also preserved
sharp boundary equality cases.

## Reproducibility Repair

During this pass, the new branch-potential tools were made self-contained.
They no longer depend on the quarantined historical
`master_kick_rejection_lemma.py` module. The analyzer now carries its own
auditable copies of the small primitives it needs:

```text
v2
shortcut_step
odd3_macro_info
frontier enumeration / partitioning
hard-record list
parse helpers
```

The baseline result was regenerated after this change and reproduced the same
million-start class split and zero-failure counts.

## Honest Boundary

This stress run still does not prove Collatz. It strengthens the falsification
record:

```text
No checked adversarial family produced C_unit < R.
```

The universal theorem remains:

```text
Every positive finite shadow must satisfy C_unit >= R before first descent,
and the counted structural events must force actual height loss.
```
