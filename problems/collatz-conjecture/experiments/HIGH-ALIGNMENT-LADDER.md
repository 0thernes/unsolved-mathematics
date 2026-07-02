# High-Alignment Ladder

This note refines the high branch of
[`ALIGNMENT-DICHOTOMY.md`](ALIGNMENT-DICHOTOMY.md).

The low branch has an exact `-5 mod 64` repeat gate. The high branch has an
exact boundary-alignment ladder.

All maps below use the shortcut Collatz map:

```text
T(n) = n/2            if n is even
T(n) = (3n + 1)/2    if n is odd
```

## Exact Ladder Law

Suppose an odd value is aligned to the `2`-adic boundary:

```text
x = 2^a q - 1,      q odd,      a = v2(x + 1) >= 3.
```

Then the next `a` shortcut steps are forced:

```text
T^k(x) = 3^k 2^(a-k) q - 1      for 0 <= k <= a.
```

For `0 <= k < a`, the value remains odd and its alignment burns down exactly:

```text
v2(T^k(x) + 1) = a - k.
```

At `k = a`, the ladder hits the forced even terminal:

```text
T^a(x) = 3^a q - 1.
```

The existing kick-repulsion counter records one event for every odd step with
pre-alignment at least `3`. Therefore one ladder beginning at alignment `a`
contributes exactly:

```text
ladder credit = a - 2.
```

This is the arithmetic core of the high-alignment branch. It is not an
analogy: it is an exact identity.

## Instrument

Script:

```text
experiments/high_alignment_ladder_analyzer.py
```

Result:

```text
experiments/results/high_alignment_ladder_20260702.json
```

Command:

```powershell
python experiments/high_alignment_ladder_analyzer.py --limit-scan 1000000 --frontier-base-depth 28 --frontier-max-depth 1024 --frontier-sample-stride 1024 --frontier-sample-offsets 0 256 512 768 --top-n 12 --output experiments/results/high_alignment_ladder_20260702.json --quiet
```

The population is the same as the kick audit and alignment-dichotomy run:

```text
total starts checked:                 1,013,816
initial scan:                         999,999  (2..1,000,000)
hard records / hard seeds:                 34
base-29 transfer-failure starts:           15
sampled base-28 frontier shadows:      13,768
```

## Results

Class split:

```text
high descents:                        281,754
low descents:                         732,062
uncertified:                                0
```

High-branch summary:

```text
high starts:                          281,754
high ladders checked:                 428,318
total ladder credit:                  888,579
credit failures:                            0
formula failures:                           0
alignment-burn failures:                    0
min credit surplus:                         0
max escape depth:                         738
max steps per bit:                    14.461538462
max excess:                           42.591094525
max ladder alignment:                         47
max forced even-chain length:                 17
```

The low branch still has `199` credit failures if one tries to use high-ladder
credit there. That is expected and matches the kick audit: those are precisely
the cases handled by the low-alignment `-5 mod 64` structure instead.

High ladder alignment counts:

```text
a=3:   206,970
a=4:   106,604
a=5:    54,915
a=6:    28,776
a=7:    14,993
a=8:     7,812
a=9:     3,925
a=10:    2,127
a=11:    1,074
a=12:      545
tail:      sparse through a=47
```

Forced even-chain counts:

```text
e=1:   220,980
e=2:   106,180
e=3:    51,303
e=4:    25,258
e=5:    12,195
e=6:     6,240
tail:    sparse through e=17
```

Worst high-branch ratio examples:

| Start | Group | Bits | Escape Depth | Steps/Bit | Max Excess | Ladders | Credit | Required | Surplus |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `63,728,127` | hard records | 26 | 376 | 14.461538462 | 8.131880104 | 37 | 85 | 8 | 77 |
| `217,740,015` | hard records | 28 | 395 | 14.107142857 | 7.884255979 | 39 | 98 | 7 | 91 |
| `13,421,671` | hard records | 24 | 287 | 11.958333333 | 10.003801400 | 28 | 88 | 10 | 78 |
| `26,716,671` | hard records | 25 | 298 | 11.920000000 | 10.144214786 | 29 | 78 | 10 | 68 |
| `56,924,955` | hard records | 26 | 308 | 11.846153846 | 10.063574111 | 28 | 84 | 10 | 74 |

Largest high-credit example:

```text
start:                  2,358,909,599,867,980,429,759
bits:                   71
escape depth:           738
max excess:             42.591094525
ladder count:           69
ladder credit:          196
required credit:        42
credit surplus:         154
max ladder alignment:   12
```

Largest single alignment examples are Mersenne-type starts. For example:

```text
start:                  140,737,488,355,327 = 2^47 - 1
initial alignment:      47
ladder count:           6
ladder credit:          54
required credit:        17
credit surplus:         37
escape depth:           143
```

## Theorem Target

The high-alignment proof obligation is now:

```text
Decompose every high-alignment positive shortcut segment into exact ladders.
Each ladder beginning at v2(x+1)=a contributes a-2 forced high-alignment
credits before a forced even terminal. Prove these credits dominate the
positive excess debt and feed a descending potential until certificate descent.
```

The local algebra is exact. The remaining proof work is global:

1. Formalize the potential whose debt is paid by ladder credit.
2. Prove that every positive orbit with sustained excess must either fall into
   the low-alignment structure or accumulate enough high-ladder credit.
3. Connect the branch potential to the certificate-frontier induction so that
   descent below the starting integer follows uniformly.

Together with [`LOW-ALIGNMENT-STRUCTURE.md`](LOW-ALIGNMENT-STRUCTURE.md), this
turns the kick-repulsion audit gap into two exact local grammars plus one
global induction problem.
