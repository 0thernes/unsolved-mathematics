# 📚 Sourcing & Verification Standard

The atlas is research scaffolding. Its usefulness depends entirely on being
honest about how trustworthy each claim is. This document defines the rules.

## Verification flags

Every paper (`papers.md`) and, where relevant, every biographical claim carries
one of four flags:

| Flag | Meaning | May be cited as fact? |
|------|---------|:---------------------:|
| `verified` | A human checked the primary source (DOI / arXiv / published text) | ✅ Yes |
| `high-confidence` | Canonical, widely-known result; details (year, venue) align with standard references | ⚠️ With a spot-check |
| `needs-verification` | Plausible and probably real, but not yet checked against the source | ❌ Not yet |
| `ai-suggested` | Generated as a research lead; existence not confirmed | ❌ No — lead only |

**Default for newly generated content is `needs-verification` or
`ai-suggested`.** Promotion to `high-confidence` or `verified` requires a human
(or a tool-grounded check) to confirm the source exists and says what we claim.

## The cardinal rule

> **Never present an unverified citation as established fact.**

A fabricated DOI is worse than no citation. If a paper cannot be confirmed, it
stays flagged, or it is removed. This is the single non-negotiable rule of the
project, and CI is designed to make violations visible (see below).

## What "25 papers" and "10 mathematicians" mean

Each dossier targets **25 key papers** and **10 key mathematicians**. These are
*curated landmark lists*, not bibliographic completeness. Inclusion criteria:

- **Foundational** — the paper/person that created or reframed the problem.
- **Breakthrough** — moved the known frontier (e.g. Zhang 2013 for bounded gaps).
- **Survey** — the reference an expert sends a newcomer to.
- **Modern** — the current live frontier.
- **Negative / barrier** — results showing why standard methods *cannot* work.

A landmark list is more useful than an exhaustive one: it encodes the *shape* of
the field's effort.

## Preferred primary sources

1. Original published paper (journal DOI).
2. arXiv preprint (with arXiv id).
3. Author's collected works / official archive.
4. Peer-reviewed survey or Annals/Inventiones-level reference.
5. Reputable encyclopedic sources (Encyclopedia of Mathematics, MacTutor for
   biography) — acceptable for *historical/biographical* facts, flagged
   `high-confidence`, not for *mathematical* claims.

## Disputed results

Where the community has not reached consensus (e.g. Mochizuki's IUT proof of the
abc conjecture), the atlas:

- marks the problem `disputed-claim`,
- presents *both* the claim and the documented objections (e.g. the
  Scholze–Stix report) with sources,
- renders **no verdict** the field has not rendered.

## CI hooks for integrity

- `scripts/validate.py` checks that every entry in a `papers.md` table includes
  a verification flag and warns on `ai-suggested` items lacking a follow-up note.
- The build refuses to label any problem `recently-resolved` without a cited
  resolving paper in `status.md`.

## How to upgrade a flag

When you verify a source:
1. Confirm it exists (DOI resolves / arXiv id loads).
2. Confirm it says what the dossier claims.
3. Change the flag to `verified` and add the DOI/arXiv id.
4. Note the date and who/what verified it.

Verification is the highest-value contribution to this atlas. A single
`ai-suggested → verified` promotion, done correctly, is worth more than a
paragraph of new prose.
