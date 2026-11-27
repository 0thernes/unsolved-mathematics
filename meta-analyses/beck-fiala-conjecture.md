---
title: "Meta-Analysis: The Beck–Fiala Conjecture"
slug: beck-fiala-conjecture
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

# Meta-Analysis: The Beck–Fiala Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem added in Atlas `v0.8.0`; it makes no claim of a new result. All four AI review panel slots and human academic review remain `pending`. Citations carry primary-source verification flags (`verified` via live Crossref/arXiv APIs or `high-confidence` for pre-DOI classics) and require human source-checking before downstream quotation.

## Abstract

This survey summarizes the mathematical statement, historical lineage, principal lines of attack, structural barriers, and current frontier (as of November 2026) of **The Beck–Fiala Conjecture** (`status: active-progress`). Statement summary: Given any finite hypergraph (set system) in which every element belongs to at most t sets (maximum degree t), there exists a red/blue coloring chi: V -> {-1, +1} such that every set S has discrepancy |sum_{v in S} chi(v)| = O(sqrt(t)) — independent of the number of elements n and sets m. The problem is tracked formally in Lean 4 via `google-deepmind/formal-conjectures` / Left to Solve (`BeckFiala.beck_fiala_conjecture`). This meta-analysis claims no proof, disproof, or new mathematical result.

## 1. Statement and significance

Given any finite hypergraph (set system) in which every element belongs to at most t sets (maximum degree t), there exists a red/blue coloring chi: V -> {-1, +1} such that every set S has discrepancy |sum_{v in S} chi(v)| = O(sqrt(t)) — independent of the number of elements n and sets m.

Within the Atlas taxonomy, The Beck–Fiala Conjecture sits in **Combinatorics** (Discrepancy Theory, Convex Geometry, Theoretical Computer Science) and represents a canonical open benchmark connecting concrete finite/analytic structures to deep structural barriers in modern mathematics. Readers should consult [`../problems/beck-fiala-conjecture/history.md`](../problems/beck-fiala-conjecture/history.md) and [`../problems/beck-fiala-conjecture/status.md`](../problems/beck-fiala-conjecture/status.md) for the complete timeline and technical formulation.

## 2. State of the art and principal barriers

The problem remains **active-progress** (unresolved in full generality). Key partial results, quantitative bounds, and exact obstruction mechanisms are detailed in [`../problems/beck-fiala-conjecture/approaches.md`](../problems/beck-fiala-conjecture/approaches.md) and [`../problems/beck-fiala-conjecture/attempts.md`](../problems/beck-fiala-conjecture/attempts.md). In every case, existing partial theorems either settle bounded dimensions/cases, prove function-field or probabilistic analogues, or fall quantitatively short of the conjectured threshold by a structurally significant gap.

## 3. Critical assessment and verification boundaries

- **Epistemic boundary:** Zero open conjectures in this dossier are solved or claimed solved. Any linked external Lean target (`BeckFiala.beck_fiala_conjecture`) is an identity-level crosswalk correspondence, not a statement-fidelity certification.
- **Citation provenance:** All DOI and arXiv identifiers in [`../problems/beck-fiala-conjecture/papers.md`](../problems/beck-fiala-conjecture/papers.md) tagged `verified` were checked directly against live Crossref and arXiv REST APIs in November 2026; pre-DOI classics carry `—` and `high-confidence` rather than invented identifiers.
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
