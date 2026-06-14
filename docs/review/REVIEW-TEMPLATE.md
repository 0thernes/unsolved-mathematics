# 🧾 AI Review Panel — Prompt & Record Template

Use this to complete the four-model panel for any `meta-analyses/<slug>.md`.
The **prompt is identical across models** (Grok, Gemini, GPT, Claude) so verdicts
are comparable. Claude's review is generated in-house by the repo workflow; run
the same prompt through the other three and record their verdicts.

---

## The reviewer prompt (paste verbatim into each model, with the document)

> You are a skeptical mathematics referee. You are reviewing an **AI-assisted
> meta-analysis** of an open problem — a survey/assessment, **not** a claim of a
> proof. Your job is to protect against the failure modes AI text is prone to.
>
> Review the document below and report:
> 1. **Overclaims** — any place it states or implies the problem is solved, a
>    barrier is overcome, or a result is stronger than it is. Quote them.
> 2. **Unsupported or suspect citations** — references that may not exist, are
>    misattributed, or whose stated content you doubt. List them.
> 3. **Errors of fact or logic** — incorrect statements, dates, attributions, or
>    reasoning gaps.
> 4. **Missing context** — important approaches, barriers, or recent work omitted.
> 5. **Verdict** — exactly one of: `accept`, `accept-with-revisions`,
>    `major-revisions`, `reject`. Default toward requiring revisions if uncertain.
>
> Be specific and quote the text. Do not rubber-stamp. End with a one-line verdict
> and a one-paragraph summary.

---

## Recording the result

Edit the document's YAML front matter `ai_review.<model>` block:

```yaml
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "Solid survey; flagged two citation DOIs to verify and softened one claim."
  gpt:
    verdict: pending          # -> fill after running the prompt through GPT
  gemini:
    verdict: pending
  grok:
    verdict: pending
```

Then append the full reviewer text under the document's `## AI Review Panel`
section, one subsection per model.

## Promotion rule

A meta-analysis earns the **"AI-Reviewed (4-model)"** badge only when:
- all four `verdict` values are recorded (none `pending`), **and**
- none is `reject`.

Split verdicts (e.g. three `accept`, one `major-revisions`) are shown in the
[register](REGISTER.md) as **split** — never hidden. Run
`python scripts/build_review_register.py` to refresh the register after recording
verdicts.
