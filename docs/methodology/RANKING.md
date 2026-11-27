# 📏 Ranking Methodology

The atlas orders problems by a **Composite Severity Score (CSS)** — a single
number, computed deterministically from the registry, that blends four axes.
Higher CSS ⇒ "harder + older + more central + further from resolution," which is
exactly the ordering the project targets: hardest and oldest at the top, most
tractable at the bottom.

## The formula

```
CSS = 0.40 · difficulty
    + 0.30 · centrality
    + 0.20 · age_score
    + 0.10 · (100 − tractability)

age_score = clamp( (2026 − year_posed) / 3 , 0 , 100 )
```

All inputs are on a 0–100 scale. `age_score` saturates at 100 for problems older
than ~300 years, so antiquity problems (odd perfect numbers, Euclid's primes)
do not infinitely dominate purely by age — difficulty and centrality still
decide the top. Ties in CSS are broken **deterministically** by ascending
alphabetical `slug` (`sorted(problems, key=lambda p: (-composite_severity(p), p["slug"]))`).

The reference year (2026, updated deliberately in `v0.3.0` from `2025`) is
**frozen** in code (`scripts/generate.py`, `CURRENT_YEAR`) so the ranking is
reproducible and does not silently drift day to day. Bump it deliberately when
you want age to re-weight.

## The four axes

| Axis | Weight | What it measures | How we estimate it |
|------|:------:|------------------|--------------------|
| **difficulty** | 0.40 | Intrinsic mathematical hardness — depth of machinery, known barrier results, how many great mathematicians have failed | Editorial, calibrated against expert consensus and the presence of formal barriers (e.g. relativization for P vs NP) |
| **centrality** | 0.30 | How load-bearing the problem is — how much of mathematics changes if it falls | Editorial, weighted by the number of results *conditional* on it (e.g. thousands of theorems assume RH) |
| **age_score** | 0.20 | How long it has resisted | Computed from `year_posed` |
| **tractability** | 0.10 | How close a resolution *feels* right now (higher = closer); enters as `100 − tractability` so closeness *lowers* CSS | Editorial, updated as breakthroughs land |

Weights reflect a deliberate stance: **difficulty and centrality dominate**;
age is a meaningful but secondary signal; tractability is a small corrective that
pulls "about to fall" problems toward the bottom.

## Why these weights

- A merely *old* but shallow curiosity should not outrank a *deep, central*
  modern problem. Hence difficulty + centrality = 0.70 of the score.
- Age earns real weight (0.20) because longevity under assault is itself
  evidence of difficulty — but it is capped to avoid antiquity bias.
- Tractability is intentionally light (0.10): "feels close" is the least
  reliable judgment in mathematics (every false dawn felt close), so it nudges
  rather than decides.

## Honesty clause

These four numbers are **curated editorial estimates**, not measurements. The
value of the system is not that the numbers are objectively correct — they are
not, and cannot be — but that they are:

1. **transparent** (the formula and every input are in the repo),
2. **reproducible** (same registry ⇒ same ranking, byte for byte),
3. **falsifiable** (disagree → edit the registry → rerun → argue from the diff).

If you think a problem is mis-ranked, that is a concrete finding: open a GitHub
issue proposing updated scores with justification (Build Standard R2 commits
directly to `main` rather than using pull requests).

## Status vocabulary

Independent of CSS, each problem carries a `status`:

| Status | Meaning |
|--------|---------|
| `open` | No accepted proof; no recent decisive movement |
| `active-progress` | Live frontier with recent partial results or breakthroughs |
| `disputed-claim` | A claimed proof exists but is not accepted by consensus |
| `conditionally-resolved` | Settled *assuming* another open conjecture |
| `recently-resolved` | Settled recently; included for its frontier and successor questions |
| `independent` | Proven independent of the standard axioms (e.g. CH of ZFC); the live work is deciding it on new principles |

## Worked example

The Riemann Hypothesis: difficulty 99, centrality 100, year 1859
(`age_score = clamp((2026 − 1859) / 3, 0, 100) = clamp(55.667, 0, 100) = 55.667`),
tractability 8:

```
CSS = 0.40·99 + 0.30·100 + 0.20·55.6667 + 0.10·(100−8)
    = 39.6 + 30.0 + 11.1333 + 9.2
    = 89.933
```

That matches `data/problems.json` and `RANKING.md` (`89.933`) verbatim, placing RH
at the summit — matching mathematical consensus about its difficulty and centrality.
