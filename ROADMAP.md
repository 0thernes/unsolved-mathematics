# Roadmap

Tracks completed and planned structural, formal, and verification milestones for **The Unsolved Mathematics Atlas**.

## Completed (`v0.1.0` → `v0.5.0`)

- [x] Single-source-of-truth registry (`data/problems.yaml`, 106 open problems across 38 fields) + mandatory JSON Schema validation (`v0.1.0`–`v0.3.0`).
- [x] Deterministic CSS ranking engine (`(-css, slug)` tie-breaking, `CURRENT_YEAR = 2026`), synchronized dossier headers across all 106 problems, LF-normalized cross-indexes, and zero-drift `--check` verification (`v0.3.0`–`v0.5.0`).
- [x] Deterministic RAG corpus (`rag/corpus.jsonl`, 3,763 globally unique chunk IDs) (`v0.3.0`).
- [x] **Standalone Eight-Domain Lean 4.35.0 Multi-Kernel Formal Core (`lean/`):** **45 headline theorems** across **8 open-problem domains** (Collatz 14, Erdős–Straus 5, Lonely Runner 7 incl. $n=3$ non-div-4, Brocard 7 incl. $n \le 20$, Primes/Twins 4, Goldbach 3 incl. $4 \le n \le 100$, Odd Perfect/Mersenne 3, Ramsey $R(3,3)=6$ 2), **10 concrete non-vacuity witnesses**, and **14 adversarial false-variant refutations** = **69 audited declarations**, verbatim `#print axioms` parity in `README.md`, and 6-kernel replay (`v0.3.0`–`v0.5.0`).
- [x] **Primary-Source Citation & Retraction Audit:** Live arXiv + Crossref API audit (`scripts/verify_citations.py`: 445 API-verified, 109 bad IDs stripped) plus live Crossref + DataCite retraction audit (`scripts/check_retractions.py`: 220/220 DOIs audited, 0 retractions, 3 publisher errata logged) (`v0.3.0`–`v0.4.0`).
- [x] **Publication-Grade 10-Page AMS-LaTeX White Paper, FAIR Metadata & Live GitHub Pages Blueprint:** Compiled 0-warning 10-page white paper PDF + clean-room-verified `paper/arxiv_submission.tar.gz`, RO-Crate 1.1 (`ro-crate-metadata.json`), MLCommons Croissant 1.0 (`croissant.json`), live GitHub Pages (`_site/index.html` + 8-domain `_site/blueprint.html`), `ERRATA.md`, and synchronized Mega-Atlas `v2.4.0` Cross-Atlas Audit (`docs/CROSS_ATLAS_AUDIT_2026-11-25.md`) (`v0.4.0`–`v0.5.0`).
- [x] **Build Standard `v1.2.0` (100.0% `68/68`) & Playbook `v1.3` Hardening:** Four-cycle 10-class hardening audit, 65+ verification-ladder tests, 100% mutation kill rate, machine-path privacy guard, `ruff E9/F82` Collatz experiment guard, SHA-256 manifest (`data/MANIFEST.sha256`, 40 files), cross-platform CI, and SLSA-attested GitHub Releases (`v0.3.0`–`v0.5.0`).

## Near-Term (`v0.6.0`)

- [ ] **Palomar Registry Submission:** Submit the pinned `v0.5.0` commit SHA of `lean/` (`Challenge.lean`, `Solution.lean`, `comparator.json`, `formalization.yaml`) to `submit.palomar-registry.org`.
- [ ] **Zenodo DOI & Software Heritage SWHID:** Mint versioned/concept DataCite DOIs via Zenodo GitHub integration (strictly compliant with Zenodo's April 2026 depositor policy) and archive the release commit in Software Heritage (ISO/IEC 18670 SWHID).
- [ ] **Expand Primary-Source Citation Verification:** Resolve pre-DOI historical citations via zbMATH / MathSciNet / OpenAlex to push verified citation coverage past 50% and eliminate all `ai-suggested` leads.

## Mid-Term (`v0.7.0`+)

- [ ] **Decouple Collatz Experiment Lab (Architectural Dilemma D1):** Evaluate extracting the 58 MB `problems/collatz-conjecture/experiments/` laboratory into a dedicated sibling repo (`0thernes/collatz-obstruction-lab`) linked from the Collatz dossier so all 106 dossiers remain structurally balanced.
- [ ] **Expand Lean 4 Formal Core:** Formalize full Lonely Runner $n=3$ (all speed triples via 2-adic reduction), Ramsey $R(3,4) = 9$, Euler's even-perfect characterization, Eliahou/Hercher cycle lower bounds, and an opt-in `lean-mathlib/` bridge package.
- [ ] **Independent Human Meta-Analysis Reviews:** Replace single-model June 2026 self-reviews in `meta-analyses/` with genuine multi-model + independent human specialist reviews.
