# 📋 Research Kanban — The Unsolved Mathematics Atlas

> The operational board for building and maintaining the atlas. This is the
> "ERP" of the project: the process layer that turns the data model into work.
> Columns flow left → right. A problem dossier moves across the board one card
> at a time. Card id = problem slug.

**Legend:** 🟥 blocked · 🟧 needs-verification · 🟨 in-progress · 🟩 done · 🟦 backlog
**WIP limit** on `In Progress`: 6 dossiers.

---

## 🟦 Backlog (registry only — dossier not yet authored)

> Problems present in `data/problems.yaml` whose `*.md` files are still templates.

_(Auto-trackable: a dossier is "authored" when its section files no longer
contain the `<!-- DOSSIER:* -->` placeholder markers.)_

- [ ] Expand registry beyond 40 (candidate pool below)
- [ ] Candidate problems to add: Continuum-Hypothesis-relatives, Hilbert's 16th,
      Goldbach-weak (verify resolved), Riemann-for-function-fields context,
      Sarnak's conjecture, Unique Games Conjecture, Hadamard maximal determinant,
      Casas-Alvero conjecture, Littlewood conjecture, Schinzel's Hypothesis H,
      Carmichael totient, Catalan–Dickson (aliquot sequences), Erdős–Moser,
      Agoh–Giuga, Cramér's conjecture, n! + 1 generalizations.

## 🟧 To Verify (drafted, citations need checking)

> All 85 dossiers are authored; **~2,120 citations** await a human source check.
> Current flag split: 776 `high-confidence`, 1,113 `needs-verification`,
> 231 `ai-suggested`, 0 `verified`. See [verification dashboard](../indexes/verification.md).

- [ ] Promote `ai-suggested` → `needs-verification` → `verified` per
      [SOURCING.md](../methodology/SOURCING.md) (EPIC-2)
- [ ] Cross-check every `year_posed` and originator attribution
- [x] Confirm resolving citation for the `recently-resolved` entry (Connes/MIP\*=RE)

## 🟨 In Progress (actively being authored)

- [ ] Verification sweep (EPIC-2) — highest-impact remaining work
- [ ] Optional: dense embedding index + MCP retrieval server (EPIC-3)

## 🟩 Done

- [x] **All 85 dossiers authored** (history, originator, approaches, attempts,
      25 papers, 10 mathematicians, status) — EPIC-1 complete, EPIC-4 to 85
- [x] Cross-cutting indexes + verification dashboard + glossary
- [x] RAG corpus built (3,027 chunks) and retrieval verified end-to-end
- [x] Repository architecture + single-source-of-truth registry (`data/problems.yaml`)
- [x] Deterministic ranking engine (`scripts/generate.py`)
- [x] JSON Schemas (problem, paper, person)
- [x] RAG pipeline: chunker, BM25 retriever, optional dense index
- [x] Methodology docs (ranking, sourcing) + Philosophy + Architecture
- [x] ER model / data model documentation
- [x] CI/CD workflows + issue/PR templates
- [x] Initial 40-problem registry, ranked

---

## Epics

### EPIC-1 · Corpus completeness
Every one of the 40 dossiers has all eight section files authored with real,
flagged content. **Definition of done:** no `<!-- DOSSIER:* -->` markers remain;
each `papers.md` has ≥25 entries; each `mathematicians.md` has ≥10.

### EPIC-2 · Verification pass
Every paper/person flag is `verified` or `high-confidence` with a resolving
identifier (DOI/arXiv). **DoD:** zero `ai-suggested` flags in the published set.

### EPIC-3 · RAG productionization
Dense index built and benchmarked; retrieval quality spot-checked on 20 seed
questions; optional MCP server exposing `retriever.BM25`.

### EPIC-4 · Breadth expansion
Grow from 40 → 100+ problems, preserving dossier quality and the ranking
invariant. **DoD:** registry ≥100, CI green, ranking stable.

### EPIC-5 · Living frontier
Quarterly sweep: update `status.md` and `tractability` scores as breakthroughs
land (e.g. Kakeya 3D, union-closed sets, Sendov). **DoD:** changelog entry per sweep.

---

## Process (the "ERP" workflow)

```
 add to registry ─▶ generate scaffold ─▶ author dossier ─▶ verify sources
        │                                                        │
        └──────────────── re-rank & rebuild corpus ◀────────────┘
                                   │
                              CI green ─▶ merge to main ─▶ changelog
```

Each transition maps to a column move. The board is the human-facing view of the
[data model](../architecture/DATA-MODEL.md); the registry is the database.
