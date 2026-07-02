# 🤝 Contributing to the Unsolved Mathematics Atlas

Thank you for helping build a rigorous, honest map of mathematics' open
frontier. Contributions fall into four high-value categories — listed in
descending order of impact.

## 1. Verify a source (highest impact)
Promote an `ai-suggested` or `needs-verification` paper/person to `verified`.
1. Confirm the source exists (DOI resolves / arXiv id loads).
2. Confirm it says what the dossier claims.
3. Update the flag and add the identifier in `papers.md`.
4. Note the date in the PR. See [SOURCING.md](docs/methodology/SOURCING.md).

## 2. Author or deepen a dossier
Fill the eight section files of a `problems/<slug>/` folder with real,
flagged content. Remove the `<!-- DOSSIER:* -->` markers as you complete each
section. Targets: ≥25 papers, ≥10 mathematicians, with verification flags.

## 3. Add a problem
1. Append an entry to `data/problems.yaml` (must satisfy
   [`schema/problem.schema.json`](schema/problem.schema.json)).
2. Run `python scripts/generate.py` — this scaffolds the folder, recomputes the
   ranking, refreshes `RANKING.md`, `data/problems.json`, and the README table.
3. Run `python rag/build_corpus.py`.
4. Flesh out the new dossier. Open a PR.

## 4. Refine a ranking
Disagree with a score? Edit `difficulty` / `centrality` / `tractability` in the
registry, rerun the generator, and **justify the change in the PR body**. The
ranking is a falsifiable argument; make yours from the diff.

## Ground rules

- **Honesty is non-negotiable.** Never present an unverified citation as fact.
  A fabricated reference is the one unforgivable error here.
- **Generated files are off-limits to hand edits**: `data/problems.json`,
  `RANKING.md`, the README ranking block, and `metadata.json` are produced by
  the build. Edit the *source* and regenerate.
- **Keep prose dense and sourced.** This is an institute-grade reference, not a
  blog. Every nontrivial claim should be traceable.
- **Respect the schema and the invariants** in
  [DATA-MODEL.md](docs/architecture/DATA-MODEL.md).

## Local workflow

```bash
pip install -r requirements.txt
python scripts/generate.py            # build everything
python scripts/generate.py --check    # what CI runs: validate + ranking freshness
python rag/build_corpus.py            # rebuild retrieval corpus
python -m pytest -q                   # run tests (if present)
```

## Commit & PR conventions

- Branch off `main`. Keep PRs focused (one dossier, one verification batch, one
  registry change).
- Conventional-ish prefixes welcome: `dossier:`, `verify:`, `registry:`,
  `rag:`, `docs:`, `build:`.
- CI must be green: schema validation, ranking freshness, corpus build.

## Code of conduct

Be rigorous and be kind. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Commit conventions

- **Scoped commits:** one concern per commit (a dossier update, an instrument, a doc). No mixed multi-hundred-file drops.
- **Prefixes:** `docs:`, `collatz:`, `audit:`, `meta:`, `chore:`, `fix:`.
- **Branches:** work on `main` or short-lived `chore/*` / `codex/*` branches merged fast-forward; delete after merge.
- **Before pushing:** run `make sync` (kanban + corpus + validation gate) so public artifacts never lag the dossiers.
- **Claim files:** anything asserting progress on an open problem goes through the audit register, never straight to a dossier root.
