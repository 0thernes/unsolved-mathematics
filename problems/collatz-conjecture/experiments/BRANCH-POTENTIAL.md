# Branch Potential

This note joins the two exact local grammars:

* [`LOW-ALIGNMENT-STRUCTURE.md`](LOW-ALIGNMENT-STRUCTURE.md): the only
  low-alignment repeat gate is `x == -5 mod 64`, and each repeat lowers
  `v2(x + 5)` by exactly `3`.
* [`HIGH-ALIGNMENT-LADDER.md`](HIGH-ALIGNMENT-LADDER.md): an odd
  `x = 2^a q - 1`, `a >= 3`, begins a forced ladder and contributes exactly
  `a - 2` high-alignment credits.

The bridge question is whether those exact local credits pay the observed
excess debt together.

## Excess Ledger

Use the shortcut Collatz map:

```text
T(n) = n/2            if n is even
T(n) = (3n + 1)/2    if n is odd
```

Let

```text
theta = log(2) / log(3)
E_t = odd_steps_t - theta * t
Emax = max_t E_t
R = ceil(max(0, Emax - 0.999))
```

The integer `R` is the same coarse "minimum repulsion credit required" ledger
used by the kick-repulsion audit: if excess never reaches `1`, no structural
credit is demanded; above that line, each whole excess unit demands one
credit.

## Candidate Combined Credit

For one trajectory up to first certified descent below its start, define:

```text
high_ladder_credit = sum over high ladders (a_i - 2)
low_repeat_credit  = number of x == -5 mod 64 repeat gates
low_rank_credit    = 3 * low_repeat_credit
```

Two candidate bridge credits are tested:

```text
C_unit = high_ladder_credit + low_repeat_credit
C_rank = high_ladder_credit + low_rank_credit
```

`C_rank` records the exact `v2(x + 5)` drop. `C_unit` is stricter: it gives
only one credit per low repeat gate, even though that repeat burns three
minus-five rank bits.

## Instrument

Script:

```text
experiments/branch_potential_analyzer.py
```

Result:

```text
experiments/results/branch_potential_20260702.json
```

Command:

```powershell
python experiments/branch_potential_analyzer.py --limit-scan 1000000 --frontier-base-depth 28 --frontier-max-depth 1024 --frontier-sample-stride 1024 --frontier-sample-offsets 0 256 512 768 --top-n 12 --output experiments/results/branch_potential_20260702.json --quiet
```

The population is the same `1,013,816`-start population used by the
kick-repulsion, alignment-dichotomy, low-structure, and high-ladder runs:

```text
initial scan:                         999,999  (2..1,000,000)
hard records / hard seeds:                 34
base-29 transfer-failure starts:           15
sampled base-28 frontier shadows:      13,768
```

## Results

Global summary:

```text
total checked:                     1,013,816
uncertified:                               0
C_unit failures:                          0
C_rank failures:                          0
minimum C_unit surplus:                   0
minimum C_rank surplus:                   0
max excess:                       42.591094525
high ladder credit total:            888,579
low repeat gates:                    51,361
low rank drop credit:               154,083
```

Class split:

```text
high-assisted descents:              281,754
low-direct descents:                 703,125
low-repeat descents:                  28,937
```

Class summaries:

| Class | Count | Max Escape | Max Excess | High Credit | Low Repeat Credit | Unit Failures |
|---|---:|---:|---:|---:|---:|---:|
| high-assisted descent | `281,754` | `738` | `42.591094525` | `888,579` | `20,591` | `0` |
| low-direct descent | `703,125` | `5` | `0.738140493` | `0` | `0` | `0` |
| low-repeat descent | `28,937` | `32` | `1.274194189` | `0` | `30,770` | `0` |

The strict unit-credit ledger already passes. The rank-credit ledger passes
with more room, but it is not needed for the finite population.

Largest combined-credit case:

```text
start:                  2,358,909,599,867,980,429,759
bits:                   71
escape depth:           738
max excess:             42.591094525
required credit:        42
high ladder credit:     196
low repeat gates:       4
C_unit:                 200
C_unit surplus:         158
C_rank:                 208
C_rank surplus:         166
```

Tight examples have zero surplus. The first tight unit case in the result file:

```text
start:                  1,627
bits:                   11
escape depth:           16
max excess:             1.321632218
required credit:        1
high ladder credit:     1
low repeat gates:       0
C_unit surplus:         0
```

So the bridge is sharp. It is not an artifact of overly generous constants.

## Exact Local Lemmas Behind The Credit

Low repeat gate:

```text
x odd, x == 59 mod 64
T^3(x) = (9x + 5) / 8
v2(T^3(x) + 5) = v2(x + 5) - 3
```

Thus a pure low repeat spine has finite rank unless a later ordinary drop or
high-alignment transfer occurs.

High ladder:

```text
x = 2^a q - 1, q odd, a >= 3
T^k(x) = 3^k 2^(a-k) q - 1      for 0 <= k <= a
```

The ladder has exactly `a - 2` counted high-alignment odd steps.

## Theorem Target

The new proof target is a single branch-potential theorem:

```text
For every positive integer n > 1, before first descent below n,
the structural credit

  C(n) = sum_high_ladders (v2(x+1)-2)
       + count_low_repeat_gates(x == -5 mod 64)

dominates the positive excess debt

  R(n) = ceil(max(0, max_t(odd_steps_t - theta*t) - 0.999)).

Moreover, the same structural events force enough actual even insertion /
height loss that C(n) >= R(n) implies T^d(n) < n for some finite d.
```

The first sentence is the combinatorial credit inequality. The second sentence
is the dynamical realization lemma. Both are still universal proof obligations.

## Honest Boundary

This does not prove Collatz. It upgrades the prior proof frontier:

* before: high credit explained the high branch but failed on low cases;
* after: high ladder credit plus one unit per low `-5 mod 64` repeat has no
  failures on the same million-plus-start population;
* still missing: a proof that the credit inequality and height-loss realization
  hold for all positive finite shadows, not only checked starts.

The cleanest next formal move is to prove that an infinite counterexample
trajectory cannot keep `C_unit < R`: if it avoids high ladders, minus-five rank
must burn down to an ordinary drop; if it uses high ladders, each ladder pays
its own excess exposure.

## Stress Follow-Up

The companion stress pass is documented in
[`BRANCH-POTENTIAL-STRESS.md`](BRANCH-POTENTIAL-STRESS.md).

It attacks the same ledger with adversarial families:

```text
low repeat spines:     x = 2^h q - 5, h <= 96
high ladder spines:    x = 2^a q - 1, a <= 96
near-boundary starts:  up to 160 bits
fresh frontier offsets: 128,384,640,896 mod stride 1024
biased/random high-bit starts
```

Result:

```text
checked starts:            33,132
uncertified:                    0
C_unit failures:                0
C_rank failures:                0
max excess:             59.051239429
max unit-credit deficit:        0
```

The stress pass also forced a reproducibility repair: the branch-potential
tools are now self-contained and no longer import the quarantined historical
`master_kick_rejection_lemma.py` module.

## Prefix-Dominance Follow-Up

The next sharpening is documented in
[`BRANCH-PREFIX-DOMINANCE.md`](BRANCH-PREFIX-DOMINANCE.md).

Instead of checking only total credit before first descent, it checks every
prefix:

```text
C_t >= ceil(max(0, max_{s<=t}(odd_steps_s - theta*s) - 0.999))
```

with credit assigned when the structural event is visible at the current state.

Combined baseline plus stress result:

```text
checked rows:              1,046,948
unique starts:             1,044,917
uncertified:                       0
prefix C_unit failures:            0
max prefix deficit:                0
max prefix required credit:       59
```

This is a stronger theorem target: if it can be proved universally, the
potential never borrows from future unseen events.

The exact base-24 survivor frontier was then checked without stride sampling in
[`BRANCH-PREFIX-FRONTIER-EXACT.md`](BRANCH-PREFIX-FRONTIER-EXACT.md):
`286,581` positive live residues, `0` uncertified starts, `0` prefix failures,
and max prefix required credit `13`.

The first exact lift audit is
[`BRANCH-PREFIX-FRONTIER-LIFT.md`](BRANCH-PREFIX-FRONTIER-LIFT.md): depths
`24`, `25`, and `26`, `1,897,117` live frontier rows, `0` prefix failures, and
`0` orphan live children.
