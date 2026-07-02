# Low-Alignment Structure

This note refines the low branch of
[`ALIGNMENT-DICHOTOMY.md`](ALIGNMENT-DICHOTOMY.md).

The dichotomy run showed that every checked `max_align < 3` start descends
quickly. This file records the exact residue mechanism behind that behavior.

All maps below use the shortcut Collatz map:

```text
T(n) = n/2            if n is even
T(n) = (3n + 1)/2    if n is odd
```

## Exact Local Grammar

Low alignment means no checked odd iterate has `v2(x + 1) >= 3`, i.e. no odd
iterate is `7 mod 8` before descent.

For odd `x == 1 mod 4`, two shortcut steps drop:

```text
T^2(x) = (3x + 1) / 4 < x    for x > 1.
```

The only locally dangerous odd class is `x == 3 mod 8`. For that class:

```text
T^3(x) = (9x + 5) / 8.
```

The residue table modulo `64` is:

| `x mod 64` | `T^3(x) mod 8` | Local branch |
|---:|---:|---|
| `3` | `4` | even exit; one more halving drops below `x` |
| `11` | `5` | odd `1/5` exit; two more steps drop below `x` |
| `19` | `6` | even exit; one more halving drops below `x` |
| `27` | `7` | high-alignment transfer |
| `35` | `0` | even exit; one more halving drops below `x` |
| `43` | `1` | odd `1/5` exit; two more steps drop below `x` |
| `51` | `2` | even exit; one more halving drops below `x` |
| `59` | `3` | repeat gate |

So the only low-alignment local growth state that reproduces another odd
`3 mod 8` state is:

```text
x == 59 mod 64, equivalently x == -5 mod 64.
```

On that gate, if `A(x) = T^3(x) = (9x + 5) / 8`, then:

```text
A(x) + 5 = 9(x + 5) / 8
v2(A(x) + 5) = v2(x + 5) - 3.
```

This gives a concrete local rank:

```text
h(x) = v2(x + 5).
```

Every repeat of the `-5 mod 64` growth gate lowers `h` by exactly `3`. When
the local odd-`3` spine exits with `h == 3` or `h == 4`, it falls into an
ordinary descent branch. When it exits with `h == 5`, it transfers to the
high-alignment branch (`7 mod 8`) if the original orbit has not already
certified descent.

## Instrument

Script:

```text
experiments/low_alignment_structure_analyzer.py
```

Result:

```text
experiments/results/low_alignment_structure_20260702.json
```

Command:

```powershell
python experiments/low_alignment_structure_analyzer.py --limit-scan 1000000 --frontier-base-depth 28 --frontier-max-depth 1024 --frontier-sample-stride 1024 --frontier-sample-offsets 0 256 512 768 --top-n 12 --output experiments/results/low_alignment_structure_20260702.json --quiet
```

The population is the same as the kick audit and the alignment-dichotomy run:

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
low descent before high alignment:     732,062
entered high alignment first:          281,754
uncertified:                                 0
```

Low branch summary:

```text
count:                                732,062
max escape depth:                     32
max steps per bit:                    2.0
max minus-five alignment v2(x+5):     19
max repeat-gate macros:               6
repeat-law failures:                  0
```

Low-branch local macro counts:

```text
even halvings:                        1,604,817
odd 1/5 drops:                          720,562
odd3 even exits:                        133,970
odd3 odd-1/5 exits:                      66,905
odd3 repeat -5 mod 64 gates:             30,770
odd3 latent high-transfer exits:          15,625
```

The `15,625` latent high-transfer exits are not failures of the low branch.
They mean the local odd-`3` macro would produce an odd `7 mod 8` state, but
the orbit had already dropped below its original start before that high state
needed to be processed.

The `2,232` low-branch repeat events with `h mod 3 == 2` have the same
interpretation: the local repeat spine would eventually exit through `h == 5`,
but for these starts descent relative to the original occurs first.

Worst low-branch examples:

| Start | Group | Bits | Escape Depth | Steps/Bit | Repeat Gates | Max `v2(x+5)` |
|---:|---|---:|---:|---:|---:|---:|
| `174,522,363` | sampled frontier shadows | 28 | 32 | 1.142857143 | 6 | 16 |
| `112,451,579` | sampled frontier shadows | 27 | 31 | 1.148148148 | 6 | 13 |
| `678,907` | initial scan | 20 | 24 | 1.2 | 5 | 12 |
| `524,283` | initial scan | 19 | 21 | 1.105263158 | 5 | 19 |
| `262,139` | initial scan | 18 | 20 | 1.111111111 | 5 | 18 |

These include the representative failures from the kick-repulsion audit. The
new explanation is precise: they do not need high-alignment repulsion because
their low branch is a short sequence of `-5 mod 64` repeat gates and ordinary
drop exits.

## Theorem Target

The low-alignment proof obligation is now:

```text
Decompose every low-alignment positive shortcut segment into the exact macro
table above. Prove that regenerated -5 mod 64 repeat gates are bounded by a
linear function of bit length, because each repeat lowers the local h = v2(x+5)
by three and every nonrepeat exit has contraction slope at most 27/32 before
another growth spine can matter.
```

The missing piece is not the local algebra; that part is exact. The missing
piece is the global induction controlling regenerated repeat gates after an
ordinary drop. Once that is formalized, the low branch of the alignment
dichotomy has a plausible direct proof independent of counted high-alignment
repulsion.
