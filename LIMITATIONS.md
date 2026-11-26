# Limitations & Real-vs-Metaphor Boundaries

> **Epistemic honesty is the primary asset of this repository.** Every boundary
> below is stated explicitly so readers, auditors, and automated systems know
> exactly what is mechanically verified, what is editorial curation, and what
> remains unverified or open.

## 1. Mathematical Scope — What This Repository Does NOT Prove

- **Zero open problems are solved by this repository.** Every open conjecture in `data/problems.yaml` (Collatz, Riemann Hypothesis, P vs NP, Hodge, BSD, Yang–Mills, Navier–Stokes, Goldbach, Erdős–Straus, Lonely Runner, Brocard, etc.) remains **OPEN** unless settled in the external mathematical literature with a verified resolving citation (currently: Connes Embedding 2020, Telescope Conjecture 2023, Erdős Unit Distance May 2026 `arXiv:2605.20695`).
- **`lean/` proves structural lemmas, classical foundations, modular reductions, sharpness bounds, finite exhaustions, adversarial refutations, and a $3n-1$ sibling-map comparison — NOT the open conjectures themselves:**
  - Collatz theorems (18 theorems: Terras bijection, affine & intercept laws, Böhm–Sontacchi cycle equation, parity-word cocycle, no finite 2-adic cover, positivity localization $\rho_w \le -1$, negative cycles $-5$/$-17$, the $3n-1$ sibling facts in `thm_collatz_epsilon_invariance_barrier` (same Terras bijection, positive cycles at $5$ and $17$; the inference that sign-blind arguments cannot settle $3n+1$ is a heuristic, not formalized), zero/intercept/length invariants, positive-cycle odd-step / positive-intercept / strict subcriticality $3^o < 2^d$, and $d=1$ positive fixed-point exclusion) are elementary / classical rediscovery-tier structure formalized for mechanical trustworthiness.
  - Erdős–Straus Mordell mod-840 covers 834/840 classes (99.29%) plus multiplicative closure, cyclic symmetry, $2 \le n \le 30$, and the 6 smallest exceptional squares $\{121, 169, 289, 361, 529, 841\}$, explicitly leaving general primes in $\{1, 121, 169, 289, 361, 529\} \pmod{840}$ open.
  - Lonely Runner formalizes all-$n$ sharpness of $\frac{1}{n+1}$ (over $\mathbb{Q}$), symmetry group (scaling, periodicity, time reversal), and complete constructive proofs through $n \le 3$ (2, 3, and 4 runners for all positive integer speed triples), NOT $n \ge 4$ or the general uniform conjecture. These cases are classical (the 4-runner case: Betke–Wills 1972; Cusick 1973). The conjecture is proved for up to 13 runners in recent preprints (Rosenfeld, arXiv:2509.14111, 8 runners; Trakulthongchai, arXiv:2511.22427, 9 and 10; Sungkawichai and Trakulthongchai, arXiv:2604.23906, 11 to 13), far beyond what is formalized here. The earlier `thm_lonely_runner_n3_nondiv4` covers 27 of the 64 speed-triple classes mod 4 with the single time $t = 1/4$, not "7/8" as some earlier prose stated.
  - Perfect-number theorems are statements about the computational `divSum`; no Lean lemma equates it with $\sum_{d \mid n} d$ (that link is checked in pytest).
  - Brocard formalizes mod-3/4/10 invariants and exhaustive check through $n \le 20$ ($20!+1 = 2.43 \times 10^{18}$), NOT finiteness.
  - Primes/Twins (Euclid, arbitrary prime gaps, oddness $\ge 3$, twin mod-6), Goldbach ($4 \le n \le 100$ + odd binary obstruction), Perfect/Mersenne (Mersenne exponent primality, Euclid's general even perfect number theorem for all $p \ge 2$, $\{6, 28, 496, 8128\}$, no odd perfect $\le 100$), and Ramsey ($R(3,3) = 6$, $R(3,4) = 9$) are classical foundations and finite exhaustions — Twin Primes, Goldbach, Odd Perfect Numbers, Mersenne Infinitude, and higher Ramsey numbers remain **OPEN**.
- **Audit scope:** the independent statement audit of 2026-11-26 ([audit log](https://github.com/0thernes/0thernes-research-archive/blob/main/docs/reviews/2026-11-26-statement-audit.md)) covered `v0.5.0` (commit `0604df5`, 69 declarations). The 12 declarations added in `v0.6.0` were not part of it. Six-kernel replay and `lake comparator` were not re-run by the auditor; the evidence for them is the Ubuntu CI log. `lean/Challenge.lean` deliberately contains `sorry`-stated specifications for the comparator; the proof modules contain none.
- **Finite computational certificates in `problems/collatz-conjecture/experiments/`** (e.g., Odd-Unit Lock Bridge Collapse Certificate) check finite parameter windows only and prove zero universal statements about Collatz.

## 2. Citation & Literature Verification Backlog

- **Not all ~2,650 citations across the 106 dossiers are human-verified.** Automated primary-source resolution (`scripts/verify_citations.py`) verified arXiv IDs and Crossref DOIs and purged confirmed AI-hallucinated identifiers (logged transparently in `data/citation-verification-log.json`).
- Historical pre-DOI citations (17th–20th century monographs, journal volumes without DOIs in the table) remain flagged `high-confidence`, `needs-verification`, or `ai-suggested`. Per [`docs/methodology/SOURCING.md`](docs/methodology/SOURCING.md), **only rows tagged `verified` may be cited directly as primary-source confirmed**; all other rows are research leads requiring source verification before downstream citation.

## 3. Meta-Analysis Panel Reality vs Design

- All 106 documents in `meta-analyses/` are **AI-generated surveys, NOT peer-reviewed**.
- **Honest gap:** While the framework in `docs/review/AI-META-REVIEW.md` defines a four-model AI review panel (Claude, GPT, Gemini, Grok) plus human academic review, **only Claude's in-house self-review ran on 2026-06-14** (under the non-canonical session label `claude-opus-4-8`); GPT, Gemini, Grok, and human review remain `pending` (`0/106` badged). Do NOT interpret `meta-analyses/` as multi-model-validated or human-peer-reviewed.

## 4. Real vs Metaphor Audit

| Term used in repo | Literal technical meaning (Real) | What it is NOT (Metaphor / Forbidden reading) |
|---|---|---|
| **Composite Severity Score (CSS)** | Deterministic weighted linear combination of 3 editorial 0–100 estimates + capped age | NOT an objective scientific measurement of mathematical difficulty |
| **ERP / Kanban** | File-based editorial workflow tracking dossier authoring & verification state | NOT an enterprise software system or live project-management backend |
| **Spine / Ghost Cycle / Lock** (Collatz) | Rational 2-adic fixed point $\rho_w = c(w)/(2^d-3^o)$ and residue congruence $v_2(T^t(x)-\eta)$ | NOT a physical force, dynamical barrier proving Collatz, or novel proof mechanism |
| **Multi-Kernel Verification** | Replaying Lean 4.35.0 proof terms through 6 independent type-checkers | NOT human peer review and NOT a substitute for auditing statement fidelity against the literature |
| **Frontier Watch (Nov 2026)** | Recording announced preprints / Lean-only proof claims pending community audit | NOT an endorsement or verdict that Millennium Problems (RH, Navier–Stokes) are solved |

## 5. Structural Imbalance & Environment Boundaries

- **Collatz footprint:** `problems/collatz-conjecture/` holds an extensive empirical & audit laboratory (~58 MB) alongside 105 concise survey dossiers (~30 KB median). This reflects the July 2026 case-study history and is tracked in `ROADMAP.md` as an architectural trade-off.
- **Windows vs Linux sandbox:** `lake check --paranoid` and `lake comparator --paranoid` require Linux `bubblewrap` (`bwrap`) for untrusted sandboxing. On Windows, local verification exports NDJSON via `leanexport` and replays all 6 kernels with `--inadvisably-no-sandbox`; full `bwrap`-sandboxed 6-kernel execution runs automatically in Ubuntu GitHub Actions CI.
- **Independent researcher status:** Alexander S. Donahue publishes as an independent researcher (`ORCID 0009-0006-8168-9648`). No LLC or institutional affiliation is claimed.
