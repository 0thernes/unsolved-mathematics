# Changelog

All notable changes to The Unsolved Mathematics Atlas are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/); versions follow
[SemVer](https://semver.org/) on the *structure/schema* (content grows
continuously between structural versions).

## [0.2.0] — 2026-06-14
### Added
- **Authorship & accreditation to Alexander Donahue** (human-in-the-loop):
  copyright holder on CC BY 4.0 content + MIT code, `CITATION.cff`, `AUTHORS.md`,
  and README credit.
- **AI-Reviewed Meta-Analysis framework**: a four-model AI review panel (Grok,
  Gemini, GPT, Claude) with an honest process spec
  ([docs/review/AI-META-REVIEW.md](docs/review/AI-META-REVIEW.md)), review record
  schema, panel prompt/record template, and an auto-generated review register.
- **Academic-review option**: how-to and responsible-outreach protocol
  ([docs/review/ACADEMIC-REVIEW.md](docs/review/ACADEMIC-REVIEW.md)), an
  academic-review issue template, and an outreach tracker (`SUBMISSIONS.md`).
- **`meta-analyses/`**: AI-assisted meta-analysis write-ups (one per problem),
  each accredited to the author, AI-reviewed in-house by Claude with pending
  slots for GPT/Gemini/Grok, and clearly labeled AI-generated / not peer-reviewed.
- **Integrity gate** `scripts/check_papers.py` (CI-enforced): rejects any
  meta-analysis lacking the honesty banner, accreditation, or review block, or
  containing a "solved" overclaim. Repository made **public**.

## [Unreleased]
### Added
- **Expanded to 106 problems** (wave 4 — crossed 100): added 21 spanning harmonic
  analysis (restriction, Bochner–Riesz), ergodic theory (Furstenberg ×2×3),
  dynamics (Palis, Arnold diffusion), model theory (Cherlin–Zilber),
  combinatorics (Ryser), discrete geometry (Hadwiger covering, Kelvin),
  probability/statistical mechanics (self-avoiding walk, KPZ universality),
  number theory (Carmichael totient, Giuga, Pillai), complex analysis (Brennan),
  algebra (Dixmier), Diophantine geometry (Zilber–Pink), anabelian geometry
  (Grothendieck's section conjecture), Galois representations (Fontaine–Mazur),
  Iwasawa theory (Greenberg), and chromatic homotopy (the telescope conjecture,
  disproved 2023) — each fully authored. RAG corpus now **3,754 chunks
  (~765k tokens)**; **~2,650 flagged citations** (968 high-confidence,
  1,406 needs-verification, 271 ai-suggested, 0 yet human-verified).
- **Expanded to 85 problems** (wave 3): added 25 spanning analytic number theory
  (Grand RH, Elliott–Halberstam, Chowla, Sarnak–Möbius), Diophantine geometry
  (Vojta, Bombieri–Lang, Hall), complex dynamics (MLC), dynamical systems
  (Birkhoff billiards), symplectic/contact (Weinstein), 4-manifolds (smooth
  Poincaré), geometric topology (Borel, Zeeman, Eilenberg–Ganea), knot theory
  (volume, slice–ribbon), graph theory (Erdős–Hajnal, Seymour 2nd neighborhood,
  total coloring), order theory (1/3–2/3), algebraic geometry (Zariski
  cancellation), ring theory (Köthe), model theory (Vaught), modular forms
  (Lehmer τ), and aliquot sequences (Catalan–Dickson) — each fully authored.
  RAG corpus now **3,027 chunks (~617k tokens)**; **~2,120 flagged citations**
  (776 high-confidence, 1,113 needs-verification, 231 ai-suggested, 0 yet human-verified).
- **Expanded to 60 problems** (wave 2): added 20 spanning set theory (Continuum
  Hypothesis, with a new `independent` status), arithmetic geometry (Tate),
  topology / K-theory (Novikov, Baum–Connes, Whitehead, Hilbert–Smith),
  complexity (Unique Games), graph theory (reconstruction, cycle double cover,
  graceful trees, Caccetta–Häggkvist), geometry (moving sofa, unit distance,
  Falconer), algebra (inverse Galois), and number theory (Schinzel H, Artin
  primitive root, Lehmer–Mahler, four exponentials) — each fully authored.
  RAG corpus now **2,106 chunks (~434k tokens)**; **~1,500 flagged citations**
  (525 high-confidence, 760 needs-verification, 210 ai-suggested, 0 yet human-verified).
- **Full dossiers authored for all 40 problems** (EPIC-1): every problem now has
  history, originator biography, attack strategies, notable attempts, **25 key
  papers** and **10 key mathematicians** (each citation verification-flagged),
  and a live-frontier status with cross-links.
- Cross-cutting indexes (`docs/indexes/`): by field, by status, by era,
  originators index, and a **verification dashboard** (1,000 citations:
  357 high-confidence, 501 needs-verification, 142 ai-suggested, 0 yet human-verified).
- Glossary of recurring concepts (`docs/GLOSSARY.md`).
- RAG corpus expanded to **1,403 chunks (~289k tokens)** of real content.
- `scripts/build_indexes.py` and `scripts/check_dossiers.py`; `Makefile` + `build.ps1`.
- Initial repository architecture and single-source-of-truth registry
  (`data/problems.yaml`) with 40 ranked open problems.
- Deterministic ranking engine (`scripts/generate.py`) computing the Composite
  Severity Score (CSS) and scaffolding per-problem dossiers.
- JSON Schemas for problems, papers, and people.
- RAG pipeline: heading/token-aware chunker, zero-dependency BM25 retriever,
  optional sentence-transformers dense index.
- Documentation suite: README, ARCHITECTURE, PHILOSOPHY, ranking methodology,
  sourcing standard, ER model, data model, and the research Kanban board.
- CI/CD workflows (validation, ranking freshness, corpus build) and
  issue/PR templates.

### Pending
- Verification pass on all paper/person citations (EPIC-2) — promote
  `needs-verification` / `ai-suggested` flags to `verified` against primary sources.
- Dense index productionization + optional MCP retrieval server (EPIC-3).
- Breadth expansion to 100+ problems (EPIC-4).

## [0.1.0] — 2026-06-14
- Project genesis. Scaffold, registry, ranking engine, RAG layer, and docs.
