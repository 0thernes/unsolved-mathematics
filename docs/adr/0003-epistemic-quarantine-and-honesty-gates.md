# ADR 0003: Epistemic Quarantine, Proof-Claim Gates & Primary-Source Citation Verification

- **Status:** Accepted
- **Date:** 2026-07-02 (strengthened 2026-11-23 for `v0.3.0`)
- **Deciders:** Alexander S. Donahue

## Context

AI-assisted mathematical exploration naturally produces two high-risk failure modes:
1. **Epistemic overclaiming (crank drift):** Enthusiastic research notes, heuristic derivations, or broken proof sketches inadvertently assert that an open conjecture (notably Collatz) has been proved. In fact, our Nov 2026 audit uncovered a single-word hedge bypass in `scripts/proof_claim_sweep.py` that allowed a live refuted sketch (`PROOF-SKETCH-AFFINE-COCYCLE-RIGIDITY-2026.md`) to pass CI unchecked.
2. **Bibliographic hallucination:** LLM-drafted `papers.md` tables frequently attach plausible-looking DOIs or arXiv IDs to real papers that actually resolve to completely unrelated publications (e.g., economics, hardware arrays, or unrelated geometry papers) or return HTTP 404.

## Decision

1. **Tightened Proof-Claim Sweep:** `scripts/proof_claim_sweep.py` scans every active prose file outside `quarantine/`. Generic words (`candidate`, `heuristic`, `attempt`) no longer suppress proof-claim flags; only explicit retraction/negative-result qualifiers (`WITHDRAWN`, `REFUTED`, `does not prove`, `remains open`, etc.) exempt a match. Refuted sketches must either move to `quarantine/` or carry an explicit top-of-file **WITHDRAWN / REFUTED** banner.
2. **Primary-Source Identifier Gate:** No arXiv ID or DOI may be marked `verified` without live API confirmation against `export.arxiv.org` or `api.crossref.org` logged in `data/citation-verification-log.json` (`scripts/verify_citations.py`). Any identifier that returns 404 or mismatches author/title is **stripped** (replaced with `—` and downgraded to `needs-verification`) rather than left silently poisoned.
3. **Radical Provenance Transparency:** The repository explicitly states its current review state (1/4 AI self-review, 0/106 human mathematician reviews) in `README.md`, `CLAIMS.md`, and `LIMITATIONS.md`, and uses strictly `Alexander S. Donahue` (independent researcher, ORCID `0009-0006-8168-9648`) without citing any unformed legal entity.

## Consequences

- **Positive:** Caught and purged 109 hallucinated/mismatched identifiers and retracted 1 live refuted Collatz sketch before `v0.3.0`; dramatically lowers reputational and epistemic risk.
- **Negative / Trade-off:** Stripping bad identifiers increases the number of `—` (`needs-verification`) entries in `papers.md` until genuine DOIs/arXiv IDs are manually researched and verified — an intentional preference for **honest absence over confident falsehood**.
