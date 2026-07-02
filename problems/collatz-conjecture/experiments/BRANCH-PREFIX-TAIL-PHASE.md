# Branch-Prefix Tail Phase

This note audits the phase separator missing from the tail congruence note.

The previous result found:

```text
post-ladder tail terminal 6 mod 16:        340
active-ladder terminal 6 mod 16:           656
```

So terminal `6 mod 16` is necessary for the post-ladder tail but not sufficient
to identify it. The missing separator is phase: at the ladder terminal, has the
target required-credit threshold already been crossed?

## Instrument

Script:

```text
experiments/branch_prefix_tail_phase.py
```

Result:

```text
experiments/results/branch_prefix_tail_phase_d25_d26_20260702.json
```

Command:

```powershell
python experiments/branch_prefix_tail_phase.py --parent-depth 25 --max-depth 1024 --top-n 12 --output experiments/results/branch_prefix_tail_phase_d25_d26_20260702.json --quiet
```

The script recomputes the exact `25 -> 26` retimed hard class and replays each
trajectory using 80-digit Decimal arithmetic for the phase:

```text
odd_steps - (log 2 / log 3) * total_steps
```

It uses the same required-credit threshold convention as the branch-potential
ledger:

```text
R(M) = ceil(M - 0.999), for M >= 1
```

For a pressure event with required level `r`, define the lower threshold edge:

```text
L(1) = 1
L(r) = r - 0.001, for r >= 2
```

At the high-ladder terminal `y = 3^a q - 1`, define:

```text
terminal_gap = L(event_required) - max_excess_at_terminal
```

Positive gap means the target threshold is still ahead at ladder burnout.
Nonpositive gap means the target threshold has already been crossed by the
time the ladder terminal is reached.

## Result

```text
retimed transitions:                         5,677
above-parent pressure units:                 6,652
high-ladder pressure units:                  6,535
terminal-6 high-ladder pressure units:         996
```

The terminal-6 population splits exactly:

```text
post-ladder tail, positive terminal gap:      340
active ladder, nonpositive terminal gap:      656
```

Pure finite claims:

```text
terminal-6 phase sign classifies tail:        true
all tail terminal gaps positive:              true
all active terminal-6 gaps nonpositive:       true
all tail gaps are at most EOO gain:           true
all tail event margins positive:              true
all tail required_delta_from_terminal = 1:    true
terminal reconstruction misses:               0
```

## Numerical Separation

The three-step `EOO` carry gain is:

```text
2 - 3*log(2)/log(3)
= 0.107210739285627688701419...
```

Tail terminal gaps:

```text
count: 340
min:   0.021768664287042106578247...
max:   0.081541375001010298483449...
```

The tail event margin after the threshold crossing remains positive:

```text
min event margin: 0.025669364284617390217970...
max event margin: 0.085442074998585582123171...
```

Active terminal-6 gaps:

```text
count: 656
max:  -0.025669364284617390217970...
min:  -2.025669364284617390217970...
```

So there is a strict observed gap around zero in this exact lift:

```text
closest active terminal-6 case:  -0.025669364284617390217970...
closest tail terminal-6 case:    +0.021768664287042106578247...
```

## Interpretation

The congruence audit gave the residue half:

```text
3^a q - 1 == 6 mod 16
```

which forces the post-terminal parity word:

```text
E O O
```

The phase audit gives the timing half. Among terminal-6 high-ladder pressure
units:

```text
terminal_gap > 0
```

is exactly the finite separator for post-ladder pressure in the `25 -> 26`
retimed hard class. If the gap is nonpositive, the target threshold has already
been crossed inside the active ladder. If the gap is positive, the threshold is
still ahead at ladder burnout and the `EOO` carry crosses it three shortcut
steps later.

This is stronger than the congruence note but still not a proof. The remaining
theorem target is:

```text
Phase-tail lemma:
In the retimed upper-child hard class, a terminal-6 high-ladder pressure unit
appears after the ladder if and only if the terminal phase gap is positive.
Then the EOO carry crosses exactly one new required-credit level while keeping
positive surplus.
```

The finite data supports this lemma exactly for the audited lift. A proof would
still need to derive the phase sign from the lifted residue bit, the parent
frontier condition, and the low/high alignment grammar, without enumerating the
`25 -> 26` frontier.

## Spectrum Follow-Up

The phase-spectrum audit
[`BRANCH-PREFIX-TAIL-PHASE-SPECTRUM.md`](BRANCH-PREFIX-TAIL-PHASE-SPECTRUM.md)
checks whether the terminal gap is genuinely terminal-local.

Result:

```text
active terminal-6 max source at terminal: 656 / 656
tail terminal-6 max source at terminal:   334 / 340
tail max source eight steps earlier:        6 / 340
```

So the phase separator remains exact, but a proof cannot simply replace the
terminal max excess with terminal current excess in every tail case. Six tail
units remember an earlier max source.

The same audit compresses all positive tail gaps to four forms:

```text
27*theta - 17.001  count 275
35*theta - 22.001  count  57
46*theta - 29.001  count   5
54*theta - 34.001  count   3
```

where `theta = log(2)/log(3)`. This gives the next smaller target: prove those
four positive phase forms and explain the six earlier-source cases.
