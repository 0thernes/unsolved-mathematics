# Repository Deep Audit — 2026-07-02

**Method:** 11-agent adversarial audit workflow (`wf_3a3b9b6b-005`, 1.16M tokens, 245 tool invocations, ~9 min) over ten dimensions plus a literature-calibration pass, combined with direct inventory measurement. Every finding cited below carries file-path evidence in the full findings JSON (session artifact). Scores are 0–10, 10 = exemplary.

**Headline:** the atlas skeleton is strong (106/106 registry parity; 105/106 dossiers pattern-perfect; catalog CI real and passing) — but the active research front operates **outside every quality gate the repo owns**, the collatz dossier has structurally blown out (23 non-standard root entries, two competing quarantines, three results directories), one day of research (79 untracked files) sits one `git clean` away from oblivion, and the research program's proved mathematics is largely honest rediscovery, not novelty. Mean dimension score: **5.3/10**.

## Dimension scores

| Dimension | Score | One-line verdict |
|---|---|---|
| Repo organization & structure | 6.0 | 9-grade skeleton dragged down by one dossier's sprawl |
| CI/CD + QA gates | 4.0 | Gates the museum catalog, not the laboratory |
| Collatz dossier consistency | 4.0 | External facts consistent; internal governance claims contradicted by the tree |
| Experiments suite code health | 5.5 | Bimodal: instrument-grade modern suite + 12 live theater scripts |
| Results & artifact hygiene | 3.5 | Evidence locker with 37 mysticism JSONs and 47 orphans inside |
| Claims integrity | 5.5 | Authoritative surfaces clean; tracked proof-claims leak outside quarantine |
| Cross-dossier quality (6 sampled) | 7.5 | High-quality surveys; one real math error found (Goldbach exponent) |
| Git & working-tree hygiene | 5.5 | Solid fundamentals; catastrophic uncommitted-mass exposure |
| Instrument efficiency | 6.0 | Sound algorithms; zero shared code across 93 scripts |
| PM / docs layer | 5.5 | Complete apparatus, frozen 18 days — a dead roadmap |
| Research program vs literature | 4.5 | Audit discipline exemplary; proved math is mostly rediscovery |

## The 25-point scrutiny

| # | Point | Score | Verdict |
|---|---|---|---|
| 1 | Atlas skeleton & registry parity | 9 | 106 = 106 exact; 105/106 dossiers byte-pattern-perfect |
| 2 | Collatz dossier structural discipline | 2 | 23 non-standard root entries; agent-runtime litter; stub .git |
| 3 | ARCHITECTURE.md accuracy | 4 | Omits meta-analyses/ (107 files) and the actual validation gate |
| 4 | Catalog CI (schema, drift, banners) | 7 | Real, layered, passing — auditor re-ran it locally |
| 5 | Research-front CI coverage | 0 | 93 scripts / 133 JSONs / 66 memos: zero gating anywhere |
| 6 | QA gate self-testing | 2 | The honesty gates themselves have no tests; lint non-blocking |
| 7 | External-fact consistency (Collatz core) | 8 | Bařina/Tao/Hercher layer consistent across all seven files |
| 8 | Governance-claim truthfulness | 2 | status.md says "never committed"; nine proof-claim files are tracked |
| 9 | status.md maintainability | 3 | Append-only route log; one bullet ships literally truncated |
| 10 | Modern instrument quality | 8 | Exact arithmetic, selftests, explicit non-claims, self-demoting audits |
| 11 | Theater-script containment | 2 | ~12 mysticism-era scripts live beside quarantined siblings |
| 12 | Code duplication risk | 3 | Shortcut map + v₂ re-implemented ~75× across 93 scripts |
| 13 | Instrument-output traceability | 6 | Core results cited and reproducible; no manifest |
| 14 | Artifact quarantine completeness | 1 | 16 p_*.json + 21 attractor JSONs tracked in live results/; a "…LFG" proof-claim MD inside results/ |
| 15 | Authoritative-surface integrity | 9 | All 106 statuses correct; RAG corpus clean (3,758 chunks, zero contamination) |
| 16 | Proof-claim containment | 2 | Two stray claim files at problems/ root; five P-*-RESOLUTION files tracked outside quarantine; refuted sketch un-bannered |
| 17 | Non-Collatz dossier accuracy | 8 | Six deep-read dossiers current and accurate — with one inverted Goldbach exponent to fix |
| 18 | Citation verification backlog | 3 | 0 of 145 sampled paper rows human-verified; 68 need-verification |
| 19 | Git fundamentals | 7 | Clean .gitignore/.gitattributes, synced main, small .git |
| 20 | Working-tree risk exposure | 1 | 79 untracked files (~4.4 MB) + 15 modified: one reset loses the research front; quarantine is self-ignoring and unversioned |
| 21 | Algorithmic soundness | 7 | Survivor DP is O(d²); big-int-safe logs; fastest pure-Python v₂ |
| 22 | Performance headroom | 4 | Measured: numpy only 2.1×; numba path (10–30×) absent; ~1.3× free from v₂ bit-trick in 10 files |
| 23 | PM apparatus completeness | 7 | Kanban, CHANGELOG, ERD, review register, outreach tracker all exist |
| 24 | PM freshness | 2 | Everything frozen 2026-06-14; the entire Collatz campaign unrecorded |
| 25 | Research-program honesty vs novelty | 4.5 | Discipline (audits, referees, withdrawals) exemplary and rare; proved content is Terras-1976-era rediscovery — spine-ladder = classical rational-cycle parametrization (Lagarias 1990, uncited until today's prior-art notice) |

## Critical findings (9)

1. **Research front 100% outside CI** — a broken instrument or false claim ships silently (dimension: CI/QA).
2. **Overclaim gate scans only meta-analyses/** — proof-claim language in experiments memos is ungated; quarantine is convention-only (CI/QA).
3. **Refuted proof-claim files are committed and live in experiments/**, contradicting status.md's own quarantine statement (consistency).
4. **Withdrawn affine-cocycle claim still asserted live in the dossier README**; the refuted sketch carries no retraction banner (consistency, claims).
5. **16 p_* mysticism JSONs still git-tracked in live results/** (hygiene).
6. **A git-tracked proof-claim markdown *inside results/*, ending "this proves the Collatz conjecture… LFG"** — missed by both quarantines (hygiene).
7. **Two stray proof-claim files at problems/ root**, outside any dossier (claims).
8. **Five P-*-RESOLUTION files tracked in experiments/** outside quarantine (claims).
9. **One day of research uncommitted** — 79 untracked files; a single `git reset --hard && git clean -fd` erases the front; the quarantine directory is unversioned by its own .gitignore (git).

## Real math errors found outside Collatz

- **Goldbach dossier**: exceptional-set exponent inverted — claims a result far beyond the state of the art; should read E(X) ≪ X^0.72 (status.md:11, approaches.md:30).
- Navier–Stokes: Escauriaza–Seregin–Šverák year wrong; several minor year drifts (Berry–Keating, GCT I, Selberg, Ford et al.).

## Prioritized fix list

**Do now (safe, high value):** commit the research front in 3–4 logical commits and push; force-add the quarantine manifest; fix the Goldbach exponent; fix README rank + truncated status.md bullet; add retraction banners to the refuted sketch files; prior-art citations for SPINE-LADDER (✔ applied 2026-07-02).
**Do next (mechanical, needs care with concurrent sessions):** merge `_quarantine/` into `experiments/unverified-claims/`; move the 12 theater scripts + 37 mysticism JSONs into quarantine; git rm the 15 debris files + extend .gitignore; consolidate the three results dirs; fix the nested experiments/experiments path bug.
**Do soon (structural):** CI step compiling experiments/*.py + running selftests + JSON-schema-validating results; extend the overclaim regex gate to experiments memos with a quarantine allowlist; `collatz_lib.py` shared module; session-branch workflow for concurrent AI editing; CHANGELOG [Unreleased] block + Kanban research-front card; citation-verification pass (0/145 verified today).

## Honest bottom line

This repo's genuinely rare asset is its **self-correction machinery** — claim audits that withdrew the repo's own headline results, referee waves that caught the auditors' own errors, a register that documents every demotion. No other amateur-or-AI Collatz effort the auditors know of does this. Its liabilities are the operational gap between that discipline and the infrastructure (nothing enforces the discipline; it lives in session convention), and the novelty gap between what the instruments measure well and what the mathematics actually contributes (rediscovery, honestly labeled as of today). The conjecture is **open**; nothing in this repo changes that; and the repo now says so accurately at every level checked.
