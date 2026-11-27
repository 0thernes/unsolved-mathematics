---
title: "Meta-Analysis: The Cohen–Lenstra Heuristics"
slug: cohen-lenstra-heuristics
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
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

# Meta-Analysis: The Cohen–Lenstra Heuristics

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem added in Atlas `v0.8.0`; it makes no claim of a new result. All four AI review panel slots and human academic review remain `pending`. Citations carry primary-source verification flags (`verified` via live Crossref/arXiv APIs or `high-confidence` for pre-DOI classics) and require human source-checking before downstream quotation.

## Abstract

This survey summarizes the mathematical statement, historical lineage, principal lines of attack, structural barriers, and current frontier (as of November 2026) of **The Cohen–Lenstra Heuristics** (`status: active-progress`). Statement summary: As K ranges over imaginary (or real) quadratic number fields ordered by discriminant, the odd part of the ideal class group Cl(K) is conjectured to be distributed like a random finite abelian group G weighted inversely by |Aut(G)| (for imaginary quadratic fields, u = 0) or by |G| * |Aut(G)| (for real quadratic fields, u = 1). The problem is tracked formally in Lean 4 via `google-deepmind/formal-conjectures` / Left to Solve (`CohenLenstraHeuristics.cohen_lenstra_imaginary_quadratic_p_sylow_conjecture`, `CohenLenstraHeuristics.cohen_lenstra_real_quadratic_p_sylow_conjecture`). This meta-analysis claims no proof, disproof, or new mathematical result.

## 1. Statement and significance

As K ranges over imaginary (or real) quadratic number fields ordered by discriminant, the odd part of the ideal class group Cl(K) is conjectured to be distributed like a random finite abelian group G weighted inversely by |Aut(G)| (for imaginary quadratic fields, u = 0) or by |G| * |Aut(G)| (for real quadratic fields, u = 1).

Within the Atlas taxonomy, The Cohen–Lenstra Heuristics sits in **Number Theory** (Algebraic Number Theory, Arithmetic Statistics, Class Groups) and represents a canonical open benchmark connecting concrete finite/analytic structures to deep structural barriers in modern mathematics. Readers should consult [`../problems/cohen-lenstra-heuristics/history.md`](../problems/cohen-lenstra-heuristics/history.md) and [`../problems/cohen-lenstra-heuristics/status.md`](../problems/cohen-lenstra-heuristics/status.md) for the complete timeline and technical formulation.

## 2. State of the art and principal barriers

The problem remains **active-progress** (unresolved in full generality). Key partial results, quantitative bounds, and exact obstruction mechanisms are detailed in [`../problems/cohen-lenstra-heuristics/approaches.md`](../problems/cohen-lenstra-heuristics/approaches.md) and [`../problems/cohen-lenstra-heuristics/attempts.md`](../problems/cohen-lenstra-heuristics/attempts.md). In every case, existing partial theorems either settle bounded dimensions/cases, prove function-field or probabilistic analogues, or fall quantitatively short of the conjectured threshold by a structurally significant gap.

## 3. Critical assessment and verification boundaries

- **Epistemic boundary:** Zero open conjectures in this dossier are solved or claimed solved. Any linked external Lean target (`CohenLenstraHeuristics.cohen_lenstra_imaginary_quadratic_p_sylow_conjecture`, `CohenLenstraHeuristics.cohen_lenstra_real_quadratic_p_sylow_conjecture`) is an identity-level crosswalk correspondence, not a statement-fidelity certification.
- **Citation provenance:** All DOI and arXiv identifiers in [`../problems/cohen-lenstra-heuristics/papers.md`](../problems/cohen-lenstra-heuristics/papers.md) tagged `verified` were checked directly against live Crossref and arXiv REST APIs in November 2026; pre-DOI classics carry `—` and `high-confidence` rather than invented identifiers.
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
