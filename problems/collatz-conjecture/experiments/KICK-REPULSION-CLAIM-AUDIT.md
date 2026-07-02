# Kick Repulsion Claim Audit

This audit checks the current "positive kick repulsion" proof-claim artifacts
against the executable definition in
[`kick_repulsion_claim_audit.py`](kick_repulsion_claim_audit.py).

It does **not** try to prove or disprove Collatz. It asks a narrower question:
are the finite subclaims currently used by the proof-claim notes already false
on tested starts?

## Command

```powershell
python experiments/kick_repulsion_claim_audit.py --limit-scan 1000000 --frontier-base-depth 28 --frontier-max-depth 1024 --frontier-sample-stride 1024 --frontier-sample-offsets 0 256 512 768 --top-n 12 --output experiments/results/kick_repulsion_claim_audit_20260702.json --quiet
```

## Population

```text
total starts checked:                 1,013,816
initial scan:                         999,999  (2..1,000,000)
hard records / hard seeds:                 34
base-29 transfer-failure starts:           15
sampled base-28 frontier shadows:      13,768
```

The sampled base-28 frontier shadows came from the exact base-28 frontier
(`3,524,586` representatives), partitioned with stride `1024` at offsets
`0`, `256`, `512`, and `768` (`3,442` starts per offset).

## What Passed

No checked start violated the broad empirical descent bounds:

```text
uncertified starts:                       0
gamma-bound violations:                   0
better-bound violations:                  0
```

The tested gamma bound was:

```text
escape_depth(n) <= 19.982226683919038 * bitlen(n) + 32
```

The tested stronger empirical bound was:

```text
escape_depth(n) <= 14.56 * bitlen(n) + 32
```

Worst checked ratios:

| Start | Bits | Escape Depth | Steps/Bit | Group |
|---:|---:|---:|---:|---|
| `63,728,127` | 26 | 376 | 14.4615 | hard records |
| `217,740,015` | 28 | 395 | 14.1071 | hard records |
| `13,421,671` | 24 | 287 | 11.9583 | hard records |
| `26,716,671` | 25 | 298 | 11.9200 | hard records |
| `56,924,955` | 26 | 308 | 11.8462 | hard records |

Largest checked escape depths:

| Start | Bits | Escape Depth | Steps/Bit | Repulsions |
|---:|---:|---:|---:|---:|
| `2,358,909,599,867,980,429,759` | 71 | 738 | 10.3944 | 196 |
| `2,416,326,538,309,822,975` | 62 | 509 | 8.2097 | 138 |
| `217,740,015` | 28 | 395 | 14.1071 | 98 |

## What Failed

The stronger mechanism statement

```text
repulsion count >= minimum repulsions required by max excess
```

failed on `199` checked starts.

This does not produce Collatz counterexamples: all `199` still certified
descent. It does mean the current proof-claim wording is too broad. Some starts
descend by ordinary dynamics before the high-alignment repulsion detector fires.

Representative failures:

| Start | Group | Bits | Escape Depth | Max Excess | Required Repulsions | Counted Repulsions | Max Alignment |
|---:|---|---:|---:|---:|---:|---:|---:|
| `524,283` | initial scan | 19 | 21 | 1.274194 | 1 | 0 | 2 |
| `262,139` | initial scan | 18 | 20 | 1.274194 | 1 | 0 | 2 |
| `174,522,363` | sampled base-28 frontier | 28 | 32 | 1.226756 | 1 | 0 | 2 |
| `112,451,579` | sampled base-28 frontier | 27 | 31 | 1.226756 | 1 | 0 | 2 |

The common pattern is `max_align = 2`, so the current event definition
(`pre_align >= 3`) records no repulsion even when the excess briefly exceeds
`1`. These starts still descend quickly, but not by the counted repulsion
mechanism.

## Audit Conclusion

The audit supports a weaker empirical statement:

```text
All checked starts descend within the tested linear bounds.
```

It does **not** support the current proof-claim statement:

```text
The counted high-alignment repulsion events alone always pay the excess debt.
```

Therefore the "Collatz resolved" proof-claim documents are not yet
mathematically defensible. The remaining obligations are:

1. Formalize the exact 2-adic carry lemma: alignment plus positive affine defect
   forces a quantified even insertion.
2. Prove a uniform lower bound on repulsion frequency for every positive
   frontier shadow, or broaden the potential so low-alignment quick descents
   are covered separately.
3. Show the combined potential decreases enough to imply certificate descent.
4. Close the induction from finite-bit support to all bit lengths with explicit
   constants.
5. Integrate sibling controls so the argument uses the `epsilon = +1` intercept
   sign and cannot also prove false sibling maps.

The kick idea remains a useful candidate mechanism. The audit turns it from a
declaration into a theorem-obligation ledger.
