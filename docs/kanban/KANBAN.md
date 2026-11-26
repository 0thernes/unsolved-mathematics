# 📋 Research Kanban — The Unsolved Mathematics Atlas (`v0.6.0`)

> Operational board tracking the atlas's verification, formalization, and curation workstreams.
> Updated `2026-11-26` for release `v0.6.0`.

**Legend:** 🟥 blocked · 🟧 needs-verification · 🟨 in-progress · 🟩 done · 🟦 backlog

---

## 🟦 Backlog

- [ ] **v0.5.0+ Collatz lab separation:** Extract the 58.5 MB `problems/collatz-conjecture/experiments/` laboratory into a dedicated sibling repo (`collatz-odd-unit-lock-lab`) while preserving concise atlas summary & cross-links (Dilemma D1).
- [ ] **v0.5.0+ Optional Mathlib bridge:** Add an opt-in Mathlib sub-package (`lean-mathlib/`) for analytic/geometric statements (RH zero-free regions, BSD rank definitions, Kakeya definitions) without bloating the zero-Mathlib `lean/` core.
- [ ] **v0.5.0+ Catalog broadening:** Address selection bias in `LIMITATIONS.md` (quantum complexity, modern Langlands, stochastic PDEs, homotopy type theory).

## 🟧 To Verify (Remaining Open Epistemic Gaps)

> Primary-source API verification status as of `2026-11-23` (`data/citation-verification-log.json`):
> **445 live API-verified identifiers** (arXiv + Crossref), **109 invalid/hallucinated identifiers purged** (downgraded to `—` / `needs-verification`), **~2,100 pre-DOI historical rows** still awaiting manual bibliographic verification. See [`docs/indexes/verification.md`](../indexes/verification.md).

- [ ] Manually research & add verified DOIs/arXiv IDs for the 109 stripped rows and ~2,100 pre-DOI historical citations (EPIC-2).
- [ ] Run remaining 3 of 4 independent AI model reviews (Gemini, GPT, Grok) across the 106 meta-analyses and log verifiable review records.
- [ ] Recruit independent human mathematician peer reviews across priority dossiers (currently `0/106` human-reviewed; see `SUBMISSIONS.md`).

## 🟨 In Progress

- [ ] Quarterly mathematical frontier tracking (monitoring late-2026 Lean-only GRH / Euler–NS claims until peer review settles; tracking Erdős Unit Distance `arXiv:2605.20695` peer review).

## 🟩 Done (`v0.1.0` – `v0.6.0`)

- [x] **Cycle 5 Bleeding-Edge Milestone (`v0.6.0`):** Enabled `autoImplicit = false` in `lean/lakefile.toml`, fixed `Defs.isqrt` fixed-32 fuel cap to unconditional `isqrt_spec` for all `n : Nat`, expanded `lean/` from `45 → 53` headline theorems (`69 → 81` audited declarations, 13 zero-axiom, 6/6 kernels PASS) adding **complete constructive Lonely Runner $n=3$ (all positive speed triples)**, **Euclid's general even perfect number theorem (all $p \ge 2$)**, **exact Ramsey $R(3,4)=9$** ($K_9$ Handshaking Lemma + $C_8(1,4,7)$), and 4 Collatz positive-cycle obstruction theorems; added 3-case live negative kernel rejection (`scripts/test_lean_negative.py`), dual DigiCert RFC 3161 (`.tsr`) + 3-calendar Bitcoin OpenTimestamps (`.ots`) manifest proofs (`scripts/timestamp_manifest.py`), Mega-Atlas `v2.7.0` sync (`0/1,900` retired across 16 archive entries / 76 public repos), visually verified white paper upgrade, and 70 passing verification-ladder tests (`v0.6.0`).

- [x] **Cycle 4 Deep Refinement & 8-Domain Expansion (`v0.5.0`):** Expanded `lean/` from `22 → 45` headline theorems across 8 domains (+ `10` witnesses + `14` adversarial refutations = `69` audited declarations, 6/6 kernels PASS), expanded AMS-LaTeX monograph to 10 pages with 15-field corruption TikZ chart & 8-domain DAG (0 warnings, visually verified), added FAIR RO-Crate 1.1 + Croissant 1.0 metadata, enabled live GitHub Pages auto-deploy, synchronized `unsolved-problems-mega-atlas v2.4.0` (`0/1,900` retired), fixed real Python `NameError` in `odd_unit_lock_bridge_refinement.py` + 18 stale `formal/` references (`v0.5.0`).

- [x] **Three-Cycle 10-Class Hardening, Build Standard `v1.2.0` & Playbook `v1.3` (`v0.4.0`):** Migrated `formal/` → `lean/` (`22` theorems + `6` non-vacuity witnesses + `8` adversarial false-variant refutations = `36` audited declarations, 6 independent kernels, verbatim `#print axioms` CI parity), live Crossref/DataCite retraction audit (`220/220` DOIs, `0` retracted, `3` publisher errata), 0-warning Tectonic AMS-LaTeX white paper PDF + clean-room arXiv tarball (`paper/`), interactive Proof Blueprint (`_site/blueprint.html`), `ERRATA.md`, `docs/CROSS_ATLAS_AUDIT_2026-11-25.md`, local machine-path privacy guard, LF normalization, and 55-test verification ladder (`v0.4.0`).
- [x] **Standalone Lean 4.35.0 formal core (`formal/` → `lean/`):** Initial 14 theorems across Collatz, Erdős–Straus, Lonely Runner, and Brocard; 6 non-vacuity witnesses; `VerifyAxioms.lean`; `Challenge.lean` + `comparator.json`; `STATEMENT_FIDELITY.md`; 6-kernel verification (`v0.3.0`–`v0.3.1`).
- [x] **Primary-source API citation audit (`scripts/verify_citations.py`):** 552 identifier-bearing rows checked with 0 network errors; 443 verified; 109 hallucinated/404 IDs purged (`v0.3.0`).
- [x] **Forensic & philosophical audit (`docs/reviews/2026-11-23-forensic-philosophical-audit.md`):** Complete 6-class taxonomy (7 bugs fixed, 6 errors fixed, 5 conflicts resolved, 4 dilemmas documented) + 5W1H + Deductive/Inductive/Abductive & Philosophy of Mathematics synthesis + 10-pass review log (`v0.3.0`).
- [x] **Verification test ladder (`tests/`):** Negative, bug-regression, golden determinism, schema contract, differential reference oracle, Hypothesis property-based, metamorphic, and 100%-kill mutation suite (`v0.3.0`).
- [x] **2024–2026 mathematical frontier update:** 14 live-verified arXiv preprints integrated across 11 dossiers (`v0.3.0`).
- [x] **Build Standard v1.1.0 governance, SHA-256 manifest, cross-platform CI & SLSA release workflow** (`v0.3.0`).
- [x] **Branch consolidation:** Rescued July 2–5 working tree, fast-forwarded `main` over all 30 commits from `codex/collatz-catalog-qa-routing` (PR #2), removed banned PR template, losslessly gzipped 38.6 MB JSON to 0.64 MB (`v0.3.0`).
- [x] **All 106 dossiers authored** (7 sections each, `3,763` unique RAG chunks, 106 Claude self-review meta-analyses) (`v0.1.0`–`v0.2.0`).
