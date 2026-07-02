# Branch-Prefix Tail Memory Cases

This note extracts the six post-ladder tail cases that the phase-spectrum audit
identified as non-terminal max-source cases.

The earlier spectrum result was:

```text
tail terminal-6 max source at terminal:   334 / 340
tail max source eight steps earlier:        6 / 340
```

These six cases are the only place in the exact `25 -> 26` retimed hard class
where the terminal phase gap remembers an earlier prefix maximum.

## Instrument

Script:

```text
experiments/branch_prefix_tail_memory_cases.py
```

Result:

```text
experiments/results/branch_prefix_tail_memory_cases_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_memory_cases.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_tail_memory_cases_d25_d26_20260702.json --quiet
```

The script recomputes the exact `25 -> 26` retimed class, filters to
post-ladder terminal-`6 mod 16` pressure units, and records only those whose
max excess at the ladder terminal is sourced before the terminal.

## Result

```text
terminal-6 post-ladder tail units: 340
memory-tail cases:                   6
source lag to terminal:              8 in all 6
terminal-to-event word:              EOO in all 6
source-to-terminal odd count:         5 in all 6
```

Pure finite claims:

```text
all memory-tail source lag is 8:             true
all memory records have positive max gap:    true
all memory records have positive terminal-current gap: true
single terminal-to-event word:               true
single source-to-terminal word:              false
```

The source-to-terminal word has two variants:

```text
EEOOEOOO: 5
EEOEOOOO: 1
```

Both have length `8` and `5` odd steps. Therefore the terminal current excess is
lower than the remembered source excess by:

```text
8*theta - 5 = 0.047438028571659496796216...
```

where `theta = log(2)/log(3)`.

## Common Phase Shape

All six memory cases have the same max-source phase form:

```text
27*theta - 17.001
= 0.034103346429350801687232...
```

All six also have the same positive terminal-current gap:

```text
35*theta - 22.001
= 0.081541375001010298483449...
```

So the memory subcase does not threaten the sign of the tail phase. It only
means that the actual threshold gap must be computed from the earlier source
maximum rather than from the terminal current excess.

## Local Residue Grammar

Five cases have high-ladder alignment `a = 3`; one has `a = 4`:

```text
a = 3, q mod 16 = 5: 5
a = 4, q mod 16 = 7: 1
```

The two source-to-terminal residue paths modulo `64` are:

```text
44 -> 54 -> 27 -> 9 -> 14 -> 39 -> 59 -> 25 -> 6/38
36 -> 18 -> 41 -> 30 -> 47 -> 39 -> 59 -> 25 -> 38
```

Both paths pass through the low-repeat gate residue `59 mod 64` just before
the final `25 -> terminal` pair.  This is a useful clue: the only remembered
tail maxes in this lift are coupled to the low-repeat residue grammar even
though the pressure unit itself is booked to the high ladder.

## Six Records

```text
parent    child     a  q mod16  source word  terminal mod64
2385767   35940199  3     5     EEOOEOOO     6
5953383   39507815  3     5     EEOOEOOO     38
7438031   40992463  3     5     EEOOEOOO     6
10625775  44180207  4     7     EEOEOOOO     38
16873919  50428351  3     5     EEOOEOOO     38
24446399  58000831  3     5     EEOOEOOO     38
```

## Theorem Signal

The phase-tail proof target can now split cleanly:

```text
1. Terminal-local tail cases:
   334 cases where terminal max excess is terminal current excess.

2. Memory-tail cases:
   6 cases where the max is sourced eight steps earlier, through one of two
   length-8, five-odd source-to-terminal words passing through 59 mod 64.
```

This remains finite evidence only. But the obstruction is now small enough to
state as a concrete lemma target: derive the two memory words from the
upper-child frontier hypotheses, prove their source gap is `27*theta - 17.001`,
and prove the terminal-to-event `EOO` carry still crosses exactly one new
required-credit level with positive surplus.

## Follow-Up: Exact Word Maps

The companion analyzer
[`branch_prefix_tail_memory_word_maps.py`](branch_prefix_tail_memory_word_maps.py)
computes exact affine maps and lifted source classes for the two memory words.
See
[`BRANCH-PREFIX-TAIL-MEMORY-WORD-MAPS.md`](BRANCH-PREFIX-TAIL-MEMORY-WORD-MAPS.md).

Result:

```text
experiments/results/branch_prefix_tail_memory_word_maps_d25_d26_20260702.json
```

Exact maps:

```text
EEOOEOOO: T^8(n) = (243*n + 1148)/256, source n == 108 mod 256
EEOEOOOO: T^8(n) = (243*n + 1364)/256, source n == 164 mod 256
```

Important correction: the raw modulo-`256` word cylinder does not itself force
the `59 mod 64` bridge.  The actual six memory records require the lifted
source classes modulo `16384`:

```text
EEOOEOOO: n == 6508 or 14700 mod 16384
EEOEOOOO: n == 10148 mod 16384
```

With that lift, every recorded path passes through:

```text
59 mod 64 -> 25 mod 64 -> terminal
```

So the honest local lemma target is now a lifted-residue statement: derive
those modulo-`16384` source classes from the upper-child frontier hypotheses,
then use the exact affine maps to connect the low-repeat gate to the
post-ladder tail.
