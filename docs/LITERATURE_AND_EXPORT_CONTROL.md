# Literature Search Audit Log & Export-Control Self-Screen

> **Defensible Independent AI Research Playbook `v1.3` Checklist Items #15 & #37.**

---

## 1. Dated Primary-Source Literature Search Audit Log (Playbook #15)

Every novel claim check, frontier update, and citation verification pass is logged below with exact date, databases queried, scope, and verifiable machine output:

| Date (UTC-8) | Database / Registry Queried | Query Scope | Machine-Logged Output | Outcome & Novelty Verdict |
|---|---|---|---|---|
| `2026-11-23` | `export.arxiv.org`, `api.crossref.org` | All **554** identifier-bearing rows across 106 `problems/*/papers.md` tables | `data/citation-verification-log.json` | **445 verified**, **109 invalid/404 identifiers purged** (`19.7%` corruption eliminated), `0` network errors. |
| `2026-11-23` | `export.arxiv.org` | 2024–2026 frontier status check across 11 priority conjectures (Unit Distance `2605.20695`, 3D Kakeya `2502.17655` / `2601.14411`, Guth–Maynard `2405.20552`, Lonely Runner $n=8\dots 13$, Moving Sofa, Hadwiger, Sunflower, Union-Closed, Crouzeix, Sendov) | `data/problems.yaml`, `meta-analyses/*.md` | 14 live-verified preprints integrated; `unit-distance-problem` updated to `recently-resolved` with peer-review caveat; 12 unrefereed Fall/Nov 2026 AI proof claims kept `open`. |
| `2026-11-25` | `api.crossref.org`, `api.datacite.org` | Retraction & publisher-erratum audit of all **220** API-verified DOIs (Crossref `updated-by` / `update-to` / Retraction Watch notices + DataCite `10.48550/*`) | `data/retraction-audit.json` | **0 retractions**, **3 publisher errata/corrections** logged transparently, `0` network errors. |
| `2026-11-26` | `api.crossref.org`, `export.arxiv.org` | Live BibTeX audit of all 28 primary references in `paper/references.bib` (including classical foundations: Euclid, Euler, Betke–Wills 1972, Cusick 1973, Eliahou 1993, Hercher 2023, de Moura 2026 #14576 postmortem) | Verified in Cycle 1 & Cycle 3 audit scripts | **100%** of DOI/arXiv entries resolve live with **0 retractions**. |
| `2026-11-26` | `0thernes/unsolved-problems-mega-atlas` (`v2.7.0`, `541f093`), `0thernes/0thernes-research-archive` | Cross-Atlas non-retirement audit across **1,900** macro problems and **16** companion archive entries (`76` public repos) | `docs/CROSS_ATLAS_AUDIT_2026-11-25.md` | **0 / 1,900** macro problems retired. **Zero mathematical novelty claimed** for any formalized theorem in `lean/` — all 58 headline theorems formalize classical foundations, modular reductions, finite exhaustions, or structural barriers. |

---

## 2. Export-Control Self-Screen (Playbook #37 — EAR / ITAR)

- **Repository subject matter:** Published pure mathematics (number theory, combinatorics, graph theory, discrete dynamical systems), machine-checked Lean 4.35.0 proofs of classical elementary theorems, bibliographic metadata verification scripts, and an offline BM25 text index.
- **EAR Fundamental Research Carve-Out (`15 CFR § 734.8` & `§ 734.7`):** All contents are publicly published, open-access (`CC BY 4.0` / `MIT`), fundamental mathematical research intended to be shared broadly with the scientific community, with zero proprietary or restricted funding restrictions.
- **Controlled-Technology Screen:**
  - Zero cryptographic implementation, key-exchange, cipher, or cryptanalysis source code (`ECCN 5D002` — N/A; SHA-256 and ASN.1 DER hashing in `scripts/build_data_manifest.py` and `scripts/timestamp_manifest.py` perform standard integrity hashing and public timestamp querying only, not encryption/confidentiality).
  - Zero offensive cybersecurity, exploit, weapons, nuclear, biological, aerospace, or dual-use hardware/control code (`ITAR 22 CFR 120` — N/A).
- **Disclaimer:** This is a researcher self-screen documenting the public fundamental-research posture of the repository; it is not formal legal advice.
