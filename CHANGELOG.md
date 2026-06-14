# Changelog

All notable changes to The Unsolved Mathematics Atlas are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/); versions follow
[SemVer](https://semver.org/) on the *structure/schema* (content grows
continuously between structural versions).

## [Unreleased]
### Added
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
