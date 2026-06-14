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

> Dossiers with content but `needs-verification` / `ai-suggested` papers/people.

- [ ] All 40 dossiers: promote `ai-suggested` → `verified` per
      [SOURCING.md](../methodology/SOURCING.md)
- [ ] Cross-check every `year_posed` and originator attribution
- [ ] Confirm resolving citations for `recently-resolved` entries

## 🟨 In Progress (actively being authored)

- [ ] Tier-S dossiers (ranks 1–6, Millennium problems): deepen `approaches.md`
- [ ] Wire RAG corpus build into release process

## 🟩 Done

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
