# Roadmap

Tracks planned structural, formal, and verification milestones for **The Unsolved Mathematics Atlas**.

## Completed (`v0.1.0` → `v0.3.0`)

- [x] Single-source-of-truth registry (`data/problems.yaml`, 106 open problems across 38 fields) + JSON Schema validation (`v0.1.0`–`v0.2.0`).
- [x] Deterministic CSS ranking engine with explicit `(-css, slug)` tie-breaking, synchronized dossier headers across all 106 problems, and zero-drift `--check` verification (`v0.3.0`).
- [x] Deterministic RAG corpus (`rag/corpus.jsonl`) with globally unique chunk IDs (`v0.3.0`).
- [x] Standalone Lean 4.35.0 formal verification core (`formal/`) with 14 headline theorems across 4 open-problem programs (Collatz obstructions + $\varepsilon$-barrier, Erdős–Straus Mordell mod-840 reduction, Lonely Runner sharpness + $n \in \{1,2\}$, Brocard $n \le 12$), `Challenge.lean`/`Solution.lean` comparator isolation, `NonVacuity.lean` witnesses, `VerifyAxioms.lean` audit, and 6-kernel verification (`v0.3.0`).
- [x] Automated primary-source citation verifier (`scripts/verify_citations.py`) resolving arXiv and Crossref DOIs and purging confirmed AI-hallucinated identifiers (`v0.3.0`).
- [x] November 2026 mathematical frontier sweep (Guth–Maynard 2024, Baek 2024 + Trela 2026, Wang–Zahl 2025 + Guth–Wang–Zahl 2026 + Fields Medal 2026, Rosenfeld/Trakulthongchai/Sungkawichai Lonely Runner 8–13, Erdős Unit Distance disproof May 2026 `arXiv:2605.20695`, Norin–Steiner Linear Hadwiger, Bucić–He–Lee Erdős–Szemerédi Sunflower, Costa–Sadhu Union-Closed, Lorist–Schwenninger Crouzeix, Zhang/An Sendov, and Nov 2026 Lean-only RH/Navier–Stokes frontier watches).
- [x] Build Standard v1.1.0 compliance, full test ladder (unit, negative, regression, Hypothesis property-based, golden/determinism, differential, metamorphic, mutation), and cross-platform CI + SLSA release workflow (`v0.3.0`).

## Near-Term (`v0.4.0`)

- [ ] **Palomar Registry Submission:** Submit the pinned `v0.3.0` commit SHA of `formal/` (`Challenge.lean`, `Solution.lean`, `comparator.json`, `formalization.yaml`) to `submit.palomar-registry.org`.
- [ ] **Zenodo DOI & Software Heritage SWHID:** Mint versioned/concept DataCite DOIs via Zenodo GitHub integration (strictly compliant with Zenodo's April 2026 human-conducted-research depositor policy) and archive the release commit in Software Heritage (ISO/IEC 18670 SWHID).
- [ ] **Expand Primary-Source Citation Verification:** Resolve pre-DOI historical citations via zbMATH / MathSciNet / OpenAlex to push verified citation coverage past 50% and eliminate all `ai-suggested` leads.

## Mid-Term (`v0.5.0`+)

- [ ] **Decouple Collatz Experiment Lab (Architectural Dilemma D1):** Evaluate extracting the 58 MB `problems/collatz-conjecture/experiments/` laboratory into a dedicated sibling repo (`0thernes/collatz-obstruction-lab`) linked from the Collatz dossier so all 106 dossiers remain structurally balanced.
- [ ] **Expand Lean 4 Formal Core:** Formalize additional structural barriers across flagship problems (e.g., Baker–Gill–Solovay relativization toy oracle for P vs NP, Euclid's infinitude & Euler's even-perfect-number theorem for Odd Perfect Numbers, Lonely Runner $n=3$ case, and Collatz exact cycle product inequality).
- [ ] **Independent Human Meta-Analysis Reviews:** Replace single-model June 2026 self-reviews in `meta-analyses/` with genuine multi-model + human specialist reviews.
