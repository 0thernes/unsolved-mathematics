# Branch-Prefix Exact Frontier

This note checks prefix branch-potential dominance on the exact certificate
survivor frontier at base depth `24`.

The previous prefix-dominance run included sampled base-28 frontier slices. This
run instead checks every positive residue in the exact base-24 survivor set:

```text
286,581 live residues modulo 2^24
```

This is still finite evidence, not a proof of Collatz. Its value is that it
attacks the known certificate obstruction set without stride sampling.

## Instrument

Script:

```text
experiments/branch_prefix_frontier_exact.py
```

Result:

```text
experiments/results/branch_prefix_frontier_exact_d24_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_frontier_exact.py --base-depth 24 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_frontier_exact_d24_20260702.json --quiet
```

## Prefix Condition

The checked inequality is the entry-credit prefix condition:

```text
C_t >= R_t

R_t = ceil(max(0, max_{s<=t}(odd_steps_s - theta*s) - 0.999))

C_t = sum_{high ladder entries <= t}(v2(x+1)-2)
    + count_{low repeat entries <= t}(x == -5 mod 64)
```

High-ladder credit is assigned when the odd state has visible form
`x = 2^a q - 1`, `a >= 3`. Low-repeat credit is assigned when the odd state is
visible as `x == -5 mod 64`.

## Exact Base-24 Frontier Result

Global summary:

```text
frontier count:                 286,581
frontier fraction:              0.01708155870437622
positive residues checked:      286,581
uncertified:                          0
prefix C_unit failures:               0
max prefix deficit:                   0
min prefix surplus:                   0
max prefix required credit:          13
```

Class split:

```text
high-assisted descents:         286,575
low-repeat descents:                  6
low-direct descents:                  0
```

Class summaries:

| Class | Count | Max Escape | Max Excess | Max Prefix Required | Prefix Failures |
|---|---:|---:|---:|---:|---:|
| high-assisted descent | `286,575` | `287` | `13.954462671` | `13` | `0` |
| low-repeat descent | `6` | `27` | `1.488615668` | `1` | `0` |

The exact frontier is almost entirely high-assisted after its base-24 survivor
prefix. Only six representatives descend through low-repeat behavior without
entering a counted high ladder.

## Odd-Count Slices

The base-24 survivor frontier has odd counts `16..24`. Every slice passed.

| Base-24 odd count | Count | Max Escape | Max Excess | Max Prefix Required | Prefix Failures |
|---:|---:|---:|---:|---:|---:|
| `16` | `108,950` | `213` | `9.418408975` | `9` | `0` |
| `17` | `94,555` | `287` | `10.251425525` | `10` | `0` |
| `18` | `53,020` | `224` | `11.632830454` | `11` | `0` |
| `19` | `21,725` | `229` | `13.954462671` | `13` | `0` |
| `20` | `6,608` | `249` | `13.740041193` | `13` | `0` |
| `21` | `1,472` | `246` | `11.478181686` | `11` | `0` |
| `22` | `228` | `154` | `10.500950350` | `10` | `0` |
| `23` | `22` | `175` | `10.298863554` | `10` | `0` |
| `24` | `1` | `113` | `8.857685914` | `8` | `0` |

## Largest Pressure Cases

Largest excess:

```text
start:                  6,631,675
bits:                   23
frontier odd count:     19
escape depth:           222
max excess:             13.954462671
max prefix required:    13
high ladder credit:     59
low repeat credit:      3
C_unit:                 62
max prefix deficit:     0
```

Longest escape:

```text
start:                  13,421,671
bits:                   24
frontier odd count:     17
escape depth:           287
max excess:             10.003801400
max prefix required:    10
high ladder credit:     88
low repeat credit:      0
C_unit:                 88
max prefix deficit:     0
```

## Theorem Signal

For this exact frontier, prefix debt is not merely repaid by the end. It never
goes positive at all under entry-visible credit.

This supports the sharper proof target:

```text
Every positive finite shadow of the surviving 2-adic boundary either receives
visible branch credit before prefix excess can outrun it, or descends before
credit is needed.
```

The missing step is to replace the base-24 exact audit with a lift theorem from
depth `d` to depth `d + k`, controlling how new frontier children inherit or
receive visible credit.

## Lift Follow-Up

The first multi-depth lift audit is documented in
[`BRANCH-PREFIX-FRONTIER-LIFT.md`](BRANCH-PREFIX-FRONTIER-LIFT.md).

It checks exact survivor frontiers at depths `24`, `25`, and `26`:

```text
frontier rows checked:          1,897,117
uncertified:                            0
prefix C_unit failures:                 0
max prefix deficit:                     0
max prefix required credit:            14
orphan live children:                   0
live parents without children:          0
```

The lift `24 -> 25` doubled every live parent. The lift `25 -> 26` kept every
parent alive with either one or two live children. This supports, but does not
prove, a local induction lemma for frontier refinement.
