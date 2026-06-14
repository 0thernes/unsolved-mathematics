# 🧪 The AI-Reviewed Meta-Analysis Process

> How meta-analyses in this atlas are produced, reviewed by a multi-model AI
> panel, and prepared for human academic verification — and, just as importantly,
> what that review **does and does not** certify.

## What a "meta-analysis" is here

A **meta-analysis** in this atlas is a curated, structured *survey and assessment*
of an open problem: its statement and significance, the state of the art, the
principal lines of attack and their barriers, what a resolution would require, and
an honest appraisal of where the frontier stands. It synthesizes the per-problem
[dossier](../../problems/) into a publishable-format document.

It is **not** a claim of a new theorem, a proof, or a solution. The atlas never
asserts a problem is solved unless it is, with a citation. A meta-analysis that
crossed that line would be a defect, caught by `scripts/check_papers.py`.

## What "AI-Reviewed" means — and does not mean

**Means:** the document has been read and critiqued by a panel of frontier AI
models, each asked to act as a skeptical referee — to find overclaims,
unsupported citations, logical gaps, missing context, and errors of fact — and to
record a verdict and required revisions.

**Does NOT mean:**
- ❌ human peer review,
- ❌ that the cited papers have been verified against primary sources (that is the
  separate, citation-level [verification flag](../methodology/SOURCING.md) work),
- ❌ that the mathematics is endorsed by the community,
- ❌ accreditation by any journal, university, or institute.

AI review is a **quality and integrity filter**, not a certification of truth. Its
value is catching the failure modes AI text is prone to (overconfidence,
plausible-but-wrong citations, missing caveats) *before* a human expert spends
time. It raises the floor; it does not certify the ceiling.

## The four-model panel

Each meta-analysis is reviewed by four independent frontier models so that no
single model's blind spots dominate:

| Model | Vendor | Role on the panel |
|-------|--------|-------------------|
| **Claude** | Anthropic | In-house reviewer (run within this repo's tooling) |
| **GPT** | OpenAI | Independent referee |
| **Gemini** | Google | Independent referee |
| **Grok** | xAI | Independent referee |

Using four vendors is deliberate: agreement across architecturally and
organizationally independent models is stronger evidence than one model's say-so,
and disagreement flags exactly the passages a human should scrutinize first.

## The review record

Every meta-analysis carries a review block (and a machine record validated by
[`schema/review.schema.json`](../../schema/review.schema.json)) with, per model:

- **verdict** — `accept` · `accept-with-revisions` · `major-revisions` · `reject`
- **summary** — one paragraph
- **concerns** — specific, actionable (overclaim, unsupported citation, gap, …)
- **date / model-version**

A meta-analysis is labeled **"AI-Reviewed (4-model)"** only when all four panel
verdicts are recorded and none is `reject`. Split verdicts are surfaced, not
hidden — the register shows them.

> **Running the panel.** Claude's review is produced in-house by this repo's
> workflow. To complete the panel, paste the document and the prompt in
> [`REVIEW-TEMPLATE.md`](REVIEW-TEMPLATE.md) into GPT, Gemini, and Grok, and
> record each verdict in the meta-analysis's review block. The prompt is identical
> across models so the reviews are comparable.

## From AI review to human verification

AI review is the **first** gate, not the last. The pipeline is:

```
curate meta-analysis ─▶ 4-model AI review ─▶ citation verification (EPIC-2)
        ─▶ request human academic review ─▶ (optional) submission / preprint
```

The human step is the one that matters for scholarly credit, and it is invited
openly — see [ACADEMIC-REVIEW.md](ACADEMIC-REVIEW.md). The author, **Alexander
Donahue**, is the human-in-the-loop who curates, accredits, and routes each
meta-analysis through this pipeline.

## Integrity guarantees (enforced)

`scripts/check_papers.py` (run in CI) rejects any meta-analysis that:
- claims a problem is "solved/proved" when its registry status says otherwise,
- omits the AI-generation / not-peer-reviewed banner,
- omits the author/accreditation line or the review block.

These are mechanical invariants: honesty is not left to good intentions.
