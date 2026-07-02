# Branch-Prefix Tail Child-Lift Stratifier

This note explains the extra child bit behind the separator found in
[`BRANCH-PREFIX-TAIL-DICHOTOMY-CLASSIFIER.md`](BRANCH-PREFIX-TAIL-DICHOTOMY-CLASSIFIER.md).

It does not solve Collatz. It is a finite theorem-target extraction for the
exact `25 -> 26` retimed hard lift.

## Instrument

Script:

```text
experiments/branch_prefix_tail_child_lift_stratifier.py
```

Result:

```text
experiments/results/branch_prefix_tail_child_lift_stratifier_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_child_lift_stratifier.py --parent-depth 25 --max-depth 1024 --lower-modulus 2048 --upper-modulus 4096 --timing-feature event_step --output experiments/results/branch_prefix_tail_child_lift_stratifier_d25_d26_20260702.json --quiet
```

The script recomputes the same `340` post-ladder tail cases and then compares
`child mod 2048 + event_step` against `child mod 4096 + event_step`.

## Claims Checked

```text
population is 340:                               true
memory record count is 6:                        true
lower modulus + timing is not pure:              true
lower mixed memory bucket count is 2:            true
lower terminal collision count is 3:             true
upper modulus + timing pure on memory buckets:   true
upper memory residues are expected five:         true
timing value is 38 for all memory records:       true
mixed lower buckets split purely by lift bit:    true
```

## The Exact Failure at 2048

At `child mod 2048 + event_step`, the six memory records occupy five lower
buckets. Three are already memory-only:

```text
1471|38 : memory 1
 447|38 : memory 1
 751|38 : memory 1
```

Two lower buckets are mixed:

```text
1743|38 : memory 1, terminal-local 2
1895|38 : memory 2, terminal-local 1
```

This is the whole finite obstruction to using `2048` instead of `4096`.

## The Extra Bit That Fixes It

Passing from `2048` to `4096` adds one child lift bit. That bit splits both
mixed lower buckets into pure upper buckets:

```text
lower 1743|38:
  child mod 4096 = 1743, lift bit 0 : terminal-local 2
  child mod 4096 = 3791, lift bit 1 : memory 1

lower 1895|38:
  child mod 4096 = 1895, lift bit 0 : memory 2
  child mod 4096 = 3943, lift bit 1 : terminal-local 1
```

The five memory-bearing upper buckets are therefore:

```text
 751|38 : memory 1
1471|38 : memory 1
1895|38 : memory 2
2495|38 : memory 1
3791|38 : memory 1
```

No terminal-local record occupies any of those five `child mod 4096 +
event_step` buckets.

## Memory Records

```text
child mod 4096  lower  lift  word       source mod 16384  q mod 64  terminal
 751             751     0    EEOEOOOO   10148             55        38
1471            1471     0    EEOOEOOO    6508             37        38
1895            1895     0    EEOOEOOO    6508             37        38
1895            1895     0    EEOOEOOO   14700              5         6
2495             447     1    EEOOEOOO    6508             37        38
3791            1743     1    EEOOEOOO   14700              5         6
```

All six memory cases have `event_step = 38`, `terminal_step = 35`, and
`terminal_current_gap = 35*theta - 22.001`.

## Theorem Signal

The next local proof target is no longer a vague residue observation. It is the
two-bucket lift rule:

```text
At event_step 38:
  lower class 1743 mod 2048 is terminal-local on lift bit 0 and memory on bit 1.
  lower class 1895 mod 2048 is memory on lift bit 0 and terminal-local on bit 1.
```

Together with the three already-pure lower buckets, this is exactly equivalent
to the five `child mod 4096` timing buckets in this finite lift. A proof must
derive that lift-bit assignment from the upper-child frontier hypotheses, not
from post-hoc enumeration. The necessity of the extra bit is isolated further
in [`BRANCH-PREFIX-TAIL-LIFT-BIT-WITNESS.md`](BRANCH-PREFIX-TAIL-LIFT-BIT-WITNESS.md),
which gives one memory record and one terminal-local record with the same
`2048` bucket and the same visible terminal phase.
