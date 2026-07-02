# Branch-Prefix Tail Phase Spectrum

This note compresses the terminal-6 phase separator from a decimal audit into a
smaller symbolic spectrum.

The previous phase audit showed:

```text
terminal-6 high-ladder pressure units: 996
post-ladder tail, positive gap:        340
active ladder, nonpositive gap:        656
```

This follow-up asks where the maximum excess used in that terminal gap comes
from. If it always comes from the ladder terminal itself, the phase separator is
terminal-local. If it sometimes comes from an earlier prefix, the proof must
carry a small amount of phase memory.

## Instrument

Script:

```text
experiments/branch_prefix_tail_phase_spectrum.py
```

Result:

```text
experiments/results/branch_prefix_tail_phase_spectrum_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_phase_spectrum.py --parent-depth 25 --max-depth 1024 --top-n 12 --hist-top-n 32 --output experiments/results/branch_prefix_tail_phase_spectrum_d25_d26_20260702.json --quiet
```

For a pressure event with required level `r`, the gap has the form:

```text
gap = L(r) - max_excess
    = constant + theta * source_step
```

where:

```text
theta = log(2) / log(3)
```

and `source_step` is the prefix step that realizes the max excess at ladder
burnout.

## Result

```text
terminal-6 high-ladder pressure units: 996
source misses:                         0
phase sign still classifies tail:      true
```

Max-source locality:

```text
active terminal-6, max at terminal:    656 / 656
tail terminal-6, max at terminal:      334 / 340
tail terminal-6, earlier max source:     6 / 340
```

The six non-terminal tail cases all use a max source eight shortcut steps before
the ladder terminal:

```text
tail source lag 0: 334
tail source lag 8:   6
```

So the phase separator is almost terminal-local, but not completely. A proof
must either explain the six memory-tail cases separately or carry a max-source
prefix witness in the phase lemma.

## Tail Forms

All `340` positive tail gaps collapse to four integer-linear forms:

```text
27*theta - 17.001 = 0.034103346429350801687232...  count 275
35*theta - 22.001 = 0.081541375001010298483449...  count  57
46*theta - 29.001 = 0.021768664287042106578247...  count   5
54*theta - 34.001 = 0.069206692858701603374464...  count   3
```

This is a useful compression: the entire post-ladder terminal-6 phase-positive
side in the exact `25 -> 26` lift reduces to four explicit inequalities in
`theta`.

## Active Forms

The active-ladder terminal-6 side remains negative:

```text
active terminal-6 gap sign: negative 656 / 656
```

The active side has more variety: the full terminal-6 population has `49`
distinct displayed phase forms, of which the four positive forms above are the
tail forms and the remaining forms are active negative forms.

The closest active gap remains:

```text
-0.025669364284617390217970...
```

## Theorem Signal

The previous phase-tail target can now be sharpened:

```text
Phase-spectrum lemma:
In the retimed upper-child hard class, terminal-6 high-ladder pressure units
fall into a finite phase spectrum. The post-ladder tail side is exactly the
four positive forms

  27*theta - 17.001,
  35*theta - 22.001,
  46*theta - 29.001,
  54*theta - 34.001,

while the active side has nonpositive phase gap.
```

This is not a proof of Collatz and not yet a universal lift lemma. It is a
more compact finite target: prove why the upper-child frontier hypotheses force
only these positive phase forms after ladder burnout, and prove why the six
memory-tail cases source their max exactly eight steps before the terminal.

## Memory-Case Follow-Up

The extractor
[`BRANCH-PREFIX-TAIL-MEMORY-CASES.md`](BRANCH-PREFIX-TAIL-MEMORY-CASES.md)
identifies the six memory-tail records explicitly.

Summary:

```text
source lag to terminal:        8 in all 6
source-to-terminal words:      EEOOEOOO (5), EEOEOOOO (1)
terminal-to-event word:        EOO in all 6
max-source gap:                27*theta - 17.001
terminal-current gap:          35*theta - 22.001
```

Both source-to-terminal words pass through `59 mod 64`, the low-repeat gate
residue.  Thus the memory subcase is not just "earlier max source"; it is an
explicit two-word bridge between the low-repeat residue grammar and the
post-ladder high-tail carry.
