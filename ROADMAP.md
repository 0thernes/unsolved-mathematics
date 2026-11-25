# Roadmap

Tracks completed and planned structural, formal, and verification milestones for **The Unsolved Mathematics Atlas**.

## Completed (`v0.1.0` → `v0.4.0`)

- [x] Single-source-of-truth registry (`data/problems.yaml`, 106 open problems across 38 fields) + mandatory JSON Schema validation (`v0.1.0`–`v0.3.0`).
- [x] Deterministic CSS ranking engine (`(-css, slug)` tie-breaking, `CURRENT_YEAR = 2026`), synchronized dossier headers across all 106 problems, LF-normalized cross-indexes, and zero-drift `--check` verification (`v0.3.0`–`v0.4.0`).
- [x] Deterministic RAG corpus (`rag/corpus.jsonl`, 3,763 globally unique chunk IDs) (`v0.3.0`).
- [x] **Standalone Lean 4.35.0 Multi-Kernel Formal Core (`lean/`):** 22 headline theorems across 4 open-problem programs (Collatz 11, Erdős–Straus 3, Lonely Runner 4, Brocard 4), 6 concrete non-vacuity witnesses (`NonVacuity.lean`), 8 explicit adversarial false-variant refutations (`Adversarial.lean`) = 36 audited declarations, `Challenge.lean`/`Solution.lean` comparator isolation, verbatim `#print axioms` parity in `README.md` (`scripts/check_readme_axioms.py`), and 6-kernel replay (`v0.3.0`–`v0.4.0`).
- [x] **Primary-Source Citation & Retraction Audit:** Live arXiv + Crossref API audit (`scripts/verify_citations.py`: 445 API-verified, 109 bad IDs stripped) plus live Crossref + DataCite retraction audit (`scripts/check_retractions.py`: 220/220 DOIs audited, 0 retractions, 3 publisher errata logged) (`v0.3.0`–`v0.4.0`).
- [x] **Publication-Grade AMS-LaTeX White Paper & Interactive Proof Blueprint:** Compiled 0-warning white paper PDF + clean-room-verified `paper/arxiv_submission.tar.gz` (`paper/`), interactive Proof Blueprint (`_site/blueprint.html`), `ERRATA.md`, and Cross-Atlas Audit (`docs/CROSS_ATLAS_AUDIT_2026-11-25.md`) (`v0.4.0`).
- [x] **Build Standard `v1.2.0` (10 finding classes) & Playbook `v1.3` Hardening:** Full 3-cycle audit, 55+ verification-ladder tests, 100% mutation kill rate, machine-path privacy guard, SHA-256 manifest (`data/MANIFEST.sha256`), cross-platform CI, and SLSA-attested GitHub Releases (`v0.3.0`–`v0.4.0`).

## Near-Term (`v0.5.0`)

- [ ] **Palomar Registry Submission:** Submit the pinned `v0.4.0` commit SHA of `lean/` (`Challenge.lean`, `Solution.lean`, `comparator.json`, `formalization.yaml`) to `submit.palomar-registry.org`.
- [ ] **Zenodo DOI & Software Heritage SWHID:** Mint versioned/concept DataCite DOIs via Zenodo GitHub integration (strictly compliant with Zenodo's April 2026 depositor policy) and archive the release commit in Software Heritage (ISO/IEC 18670 SWHID).
- [ ] **Expand Primary-Source Citation Verification:** Resolve pre-DOI historical citations via zbMATH / MathSciNet / OpenAlex to push verified citation coverage past 50% and eliminate all `ai-suggested` leads.

## Mid-Term (`v0.6.0`+)

- [ ] **Decouple Collatz Experiment Lab (Architectural Dilemma D1):** Evaluate extracting the 58 MB `problems/collatz-conjecture/experiments/` laboratory into a dedicated sibling repo (`0thernes/collatz-obstruction-lab`) linked from the Collatz dossier so all 106 dossiers remain structurally balanced.
- [ ] **Expand Lean 4 Formal Core:** Formalize additional structural barriers across flagship problems (e.g., Baker–Gill–Solovay relativization toy oracle for P vs NP, Euclid's infinitude & Euler's even-perfect-number theorem for Odd Perfect Numbers, Lonely Runner $n=3$ case, and Eliahou/Hercher cycle length lower-bound derivations).
- [ ] **Independent Human Meta-Analysis Reviews:** Replace single-model June 2026 self-reviews in `meta-analyses/` with genuine multi-model + independent human specialist reviews.
