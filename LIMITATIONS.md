# Limitations & Real-vs-Metaphor Boundaries

> **Epistemic honesty is the primary asset of this repository.** Every boundary
> below is stated explicitly so readers, auditors, and automated systems know
> exactly what is mechanically verified, what is editorial curation, and what
> remains unverified or open.

## 1. Mathematical Scope — What This Repository Does NOT Prove

- **Zero open problems are solved by this repository.** Every open conjecture in `data/problems.yaml` (Collatz, Riemann Hypothesis, P vs NP, Hodge, BSD, Yang–Mills, Navier–Stokes, Goldbach, Erdős–Straus, Lonely Runner, Brocard, etc.) remains **OPEN** unless settled in the external mathematical literature with a verified resolving citation (currently: Connes Embedding 2020, Telescope Conjecture 2023, Erdős Unit Distance May 2026 `arXiv:2605.20695`).
- **`lean/` proves structural lemmas, modular reductions, sharpness bounds, adversarial refutations, and no-go barriers — NOT the open conjectures themselves:**
  - Collatz theorems (11 theorems: Terras bijection, affine & intercept laws, Böhm–Sontacchi cycle equation, parity-word cocycle, no finite 2-adic cover, positivity localization $\rho_w \le -1$, negative cycles $-5$/$-17$, $\varepsilon$-invariance $3n-1$ barrier) are elementary / classical rediscovery-tier structure formalized for mechanical trustworthiness.
  - Erdős–Straus Mordell mod-840 covers 834/840 classes (99.29%) plus multiplicative closure and the 6 smallest exceptional squares $\{121, 169, 289, 361, 529, 841\}$, explicitly leaving general primes in $\{1, 121, 169, 289, 361, 529\} \pmod{840}$ open.
  - Lonely Runner formalizes all-$n$ sharpness of $\frac{1}{n+1}$ (over $\mathbb{Q}$), speed-scaling invariance, and base cases $n \in \{1, 2\}$, NOT the general conjecture.
  - Brocard formalizes mod-4 parity constraint and exhaustive check through $n \le 15$, NOT finiteness.
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
