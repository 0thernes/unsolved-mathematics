# Branch-Prefix Retimed Active High-Ladder Units

This note isolates the active high-ladder subset of the retimed pressure-unit
sweep. Together with the post-ladder and low-repeat notes, it accounts for
all above-parent pressure units in the checked retimed class.

This is finite theorem-discovery data only. It does not prove Collatz.

## Instrument

Script:

```text
experiments/branch_prefix_retimed_active_ladder_units.py
```

Combined result:

```text
experiments/results/branch_prefix_retimed_active_ladder_units_sweep_d18_d25_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_retimed_active_ladder_units.py --min-parent-depth 18 --max-parent-depth 25 --write-depth-cache --output experiments/results/branch_prefix_retimed_active_ladder_units_sweep_d18_d25_20260702.json
```

The script reuses the retimed-pressure condition:

```text
required_delta > 0
credit_delta < required_delta
```

Then it keeps all above-parent pressure units whose signature classifier is:

```text
high_inside_active_ladder
```

## Algebra Checked

For a high-ladder entry, write:

```text
x = 2^a q - 1,  a >= 3,  q odd.
```

The high-ladder identity gives, for `0 <= k <= a`:

```text
T^k(x) = 3^k 2^(a-k) q - 1.
```

The active-ladder analyzer checks every active pressure unit at lag `k` from
the ladder entry. In every checked case:

```text
1 <= k <= a
pressure event = high_ladder_step
pressure state = 3^k 2^(a-k) q - 1
shortcut word from x to the pressure state = O^k
v2(pressure_state + 1) = a - k
```

Thus the active class is exactly what its name suggests: the pressure event
appears while the high ladder is still burning alignment, including the
terminal `k = a` step where the remaining alignment is `0`.

All derived checks are true in the combined file:

```text
all active events are high-ladder steps:       true
all active ladder formulas checked:           true
all active parities are odd:                  true
all alignment burns checked:                  true
all lag simulations match pressure state:     true
all event indexes equal required-above-parent:true
```

## Combined Result

Across exact lifts `18 -> 19` through `25 -> 26`:

```text
retimed-pressure transitions:          13,856
above-parent pressure units:           16,085
active high-ladder pressure units:      15,259

pressure regimes:
  high_inside_active_ladder:            15,259
  high_after_ladder_window:                646
  low_repeat_prepaid:                      180
```

The active pressure units split by event index:

```text
event index 1:                        13,120
event index 2:                         1,835
event index 3:                           252
event index 4:                            45
event index 5:                             7
```

In every active pressure unit, event index equals the required-credit level
above the parent:

```text
1 -> 1: 13,120
2 -> 2:  1,835
3 -> 3:    252
4 -> 4:     45
5 -> 5:      7
```

Most active pressure units occur at the terminal high-ladder step, but a
substantial minority occur before the terminal:

```text
remaining alignment a-k:
   0: 9,889
   1: 3,332
   2: 1,243
   3:   505
   4:   184
   5:    62
   6:    26
   7:    11
   8:     4
   9:     2
  10:     1
```

The observed ladder-entry alignments are:

```text
a =  3: 2,972
a =  4: 3,204
a =  5: 2,779
a =  6: 2,030
a =  7: 1,449
a =  8: 1,069
a =  9:   658
a = 10:   387
a = 11:   305
a = 12:   188
a = 13:    78
a = 14:    41
a = 15:    34
a = 16:    29
a = 17:    12
a = 18:    10
a = 19:     8
a = 21:     2
a = 22:     4
```

Active pressure multiplicity is usually small:

```text
active units per retimed transition:
  1: 11,309
  2:  1,581
  3:    203
  4:     36
  5:      7

active ladders per retimed transition:
  1: 12,329
  2:    744
  3:     55
  4:      8

active units per individual high ladder:
  1: 12,858
  2:  1,074
  3:     75
  4:      7
```

## Depth Table

| Lift | Retimed | Pressure Units | Active Units | Event Index Counts | Offset Min | Offset Max |
|---|---:|---:|---:|---|---:|---:|
| `18 -> 19` | `166` | `178` | `156` | `1:144, 2:10, 3:2` | `1` | `37` |
| `19 -> 20` | `135` | `147` | `143` | `1:131, 2:10, 3:2` | `3` | `30` |
| `20 -> 21` | `253` | `288` | `277` | `1:247, 2:29, 3:1` | `2` | `32` |
| `21 -> 22` | `719` | `801` | `790` | `1:710, 2:70, 3:9, 4:1` | `1` | `45` |
| `22 -> 23` | `869` | `1,019` | `967` | `1:824, 2:116, 3:23, 4:4` | `3` | `57` |
| `23 -> 24` | `1,749` | `2,047` | `1,965` | `1:1684, 2:240, 3:35, 4:6` | `2` | `99` |
| `24 -> 25` | `4,288` | `4,953` | `4,766` | `1:4135, 2:548, 3:67, 4:14, 5:2` | `1` | `63` |
| `25 -> 26` | `5,677` | `6,652` | `6,195` | `1:5245, 2:812, 3:113, 4:20, 5:5` | `3` | `87` |

The global offset from parent depth ranges from `1` to `99`, so active
high-ladder pressure also is not a constant-window phenomenon.

## Pressure-State Residue Classifier Test

The active class is much more visible to pressure-state residue buckets than
the post-ladder or low-repeat classes, mostly because it is the dominant class.
It is still not perfectly isolated by a fixed low-residue table:

| Modulus | Active in Pure Buckets | Active Total | Pure Fraction | Pure Buckets | Mixed Buckets |
|---:|---:|---:|---:|---:|---:|
| `16` | `5,370` | `15,259` | `0.351923455` | `8` | `8` |
| `32` | `5,370` | `15,259` | `0.351923455` | `16` | `16` |
| `64` | `5,370` | `15,259` | `0.351923455` | `32` | `32` |
| `128` | `5,400` | `15,259` | `0.353889508` | `65` | `63` |
| `256` | `5,667` | `15,259` | `0.371387378` | `137` | `119` |
| `512` | `6,237` | `15,259` | `0.408742382` | `298` | `214` |
| `1024` | `7,427` | `15,259` | `0.486729143` | `674` | `346` |
| `4096` | `11,364` | `15,259` | `0.744740809` | `2,969` | `603` |
| `65536` | `14,914` | `15,259` | `0.977390393` | `11,978` | `241` |

So a large enough pressure-state table almost isolates the active class in
this finite window, but not completely. The theorem object remains the dynamic
high-ladder identity and the event-index law.

## Lemma Target

The finite data suggests the following local sublemma for the retimed-pressure
proof target:

```text
If an above-parent pressure unit is in the active high-ladder regime, then for
the most recent high-ladder credit event x = 2^a q - 1 and lag k, the pressure
state is exactly 3^k 2^(a-k)q - 1 with 1 <= k <= a. The pressure event is a
high_ladder_step, all intervening shortcuts are odd, v2(state+1)=a-k, and the
event index equals the required-credit level above the parent.
```

The missing proof obligation is to derive, from the live upper-lift transition
algebra, that every active pressure increase is caught inside this identity
before any deficit appears. Combined with the post-ladder `EOO` phase law and
the low-repeat `OO`/`OOEOO` repeat-gate law, this gives a finite three-regime
blueprint for the checked retimed-pressure class.
