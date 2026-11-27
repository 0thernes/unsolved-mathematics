---
title: "Meta-Analysis: The Erdős–Turán Conjecture on Additive Bases"
slug: erdos-turan-additive-bases
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: pending
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Erdős–Turán Conjecture on Additive Bases

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem added in Atlas `v0.8.0`; it makes no claim of a new result. All four AI review panel slots and human academic review remain `pending`. Citations carry primary-source verification flags (`verified` via live Crossref/arXiv APIs or `high-confidence` for pre-DOI classics) and require human source-checking before downstream quotation.

## Abstract

This survey summarizes the mathematical statement, historical lineage, principal lines of attack, structural barriers, and current frontier (as of November 2026) of **The Erdős–Turán Conjecture on Additive Bases** (`status: open`). Statement summary: If A is a subset of the natural numbers such that every sufficiently large integer can be written as a sum of two elements of A (an asymptotic additive basis of order 2), then the representation function r_A(n) = |{(a, b) in A x A : a + b = n}| must be unbounded. The problem is tracked formally in Lean 4 via `google-deepmind/formal-conjectures` / Left to Solve (`Erdos28.erdos_28`). This meta-analysis claims no proof, disproof, or new mathematical result.

## 1. Statement and significance

If A is a subset of the natural numbers such that every sufficiently large integer can be written as a sum of two elements of A (an asymptotic additive basis of order 2), then the representation function r_A(n) = |{(a, b) in A x A : a + b = n}| must be unbounded.

Within the Atlas taxonomy, The Erdős–Turán Conjecture on Additive Bases sits in **Number Theory** (Additive Number Theory, Additive Combinatorics, Analytic Number Theory) and represents a canonical open benchmark connecting concrete finite/analytic structures to deep structural barriers in modern mathematics. Readers should consult [`../problems/erdos-turan-additive-bases/history.md`](../problems/erdos-turan-additive-bases/history.md) and [`../problems/erdos-turan-additive-bases/status.md`](../problems/erdos-turan-additive-bases/status.md) for the complete timeline and technical formulation.

## 2. State of the art and principal barriers

The problem remains **open** (unresolved in full generality). Key partial results, quantitative bounds, and exact obstruction mechanisms are detailed in [`../problems/erdos-turan-additive-bases/approaches.md`](../problems/erdos-turan-additive-bases/approaches.md) and [`../problems/erdos-turan-additive-bases/attempts.md`](../problems/erdos-turan-additive-bases/attempts.md). In every case, existing partial theorems either settle bounded dimensions/cases, prove function-field or probabilistic analogues, or fall quantitatively short of the conjectured threshold by a structurally significant gap.

## 3. Critical assessment and verification boundaries

- **Epistemic boundary:** Zero open conjectures in this dossier are solved or claimed solved. Any linked external Lean target (`Erdos28.erdos_28`) is an identity-level crosswalk correspondence, not a statement-fidelity certification.
- **Citation provenance:** All DOI and arXiv identifiers in [`../problems/erdos-turan-additive-bases/papers.md`](../problems/erdos-turan-additive-bases/papers.md) tagged `verified` were checked directly against live Crossref and arXiv REST APIs in November 2026; pre-DOI classics carry `—` and `high-confidence` rather than invented identifiers.
- **Review status:** Because this dossier was newly added in `v0.8.0`, none of the four AI review panels (Claude, GPT, Gemini, Grok) nor human academic peer review has run yet (`pending`).

## AI Review Panel

### Claude (Anthropic) — pending
_Not yet run. To complete the panel, run the prompt in `docs/review/REVIEW-TEMPLATE.md` through Claude and record the verdict here and in the front matter._

### GPT (OpenAI) — pending
_Not yet run. See `docs/review/REVIEW-TEMPLATE.md`._

### Gemini (Google) — pending
_Not yet run. See `docs/review/REVIEW-TEMPLATE.md`._

### Grok (xAI) — pending
_Not yet run. See `docs/review/REVIEW-TEMPLATE.md`._

## Human verification

AI review is not human peer review. This document is offered for academic verification per `docs/review/ACADEMIC-REVIEW.md`: a domain specialist should independently audit the statement, bounds, barriers, and primary-source bibliography. Status: `human_review: pending`.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
