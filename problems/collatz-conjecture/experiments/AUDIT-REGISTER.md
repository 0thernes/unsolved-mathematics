# Audit Register — Collatz Dossier & Experiments Suite

_Run: 2026-07-01, multi-agent adversarial audit (workflow `wf_4e9d67a5-9fd`, 220 agents dispatched, ~1.47M tokens). Status: **PARTIAL — terminated by account spend limit.**_

## Scope and outcome

- **Inventory (complete):** 6 parallel readers swept all ten documents (five dossier files, papers.md, the research log, the theorems file, both lab reports, the meta-analysis) and extracted **189 unique objectively checkable claims** after deduplication.
- **Verification (partial):** independent adversarial verifiers — each instructed to treat its claim as wrong until direct evidence said otherwise, with primary-source web access and script re-execution — completed for the **first 10 claims (all core dossier claims). Verdict: 10 confirmed, 0 refuted, 0 unverifiable.** The remaining ~150 verifier agents, the 24-skeptic theorem panel, and the synthesis agent all failed on the account's monthly spend limit and produced no verdicts.
- **Resumable:** the workflow journal caches all completed work; re-running the same script with `resumeFromRunId: wf_4e9d67a5-9fd` re-executes only the unfinished agents.

## Verified claims (10/189)

| # | Claim (from status.md core) | Verdict | Evidence highlights |
|---|---|---|---|
| 1 | Verification limit $n < 2^{71} \approx 2.36\times10^{21}$ (Bařina 2025) | confirmed | $2^{71}$ re-computed exactly; project page milestone (2025-01-15) and *J. Supercomput.* **81**:810 both fetched |
| 2 | Terras (1976) / Everett (1977) density-1 finite stopping time | confirmed | Crossref metadata for Everett's DOI; Lagarias annotated-bibliography entries 57 & 164 quoted; theorem re-derived (Chernoff on parity vectors); brute force to $10^6$ reproduced exact Terras densities $F(1)=1/2, F(2)=3/4, F(4)=13/16, F(5)=7/8$ incl. the $n=1$ edge case |
| 3 | Krasikov–Lagarias (2003) $\#\{n\le x: n\to1\} \gg x^{0.84}$ | confirmed | Abstract of arXiv:math/0205002 (Acta Arith. 109, 237–258) quoted verbatim |
| 4 | Tao (2019) almost-bounded-values theorem, logarithmic density | confirmed | arXiv:1909.03562 fetched; statement matches incl. density type; two notational deltas noted as mathematically equivalent |
| 5 | Hercher (2023): no $m$-cycles, $m \le 91$ | confirmed | JIS article page fetched (Vol. 26, art. 23.3.5); improves Simons–de Weger $m \ge 76$ |
| 6 | Hercher threshold: verification to $3\cdot2^{69}$ ⇒ odd-term floor $1.375\times10^{11}$ | confirmed | **The 22-page paper PDF was downloaded and read**; theorem located; "below vs ≤" phrasing delta immaterial |
| 7 | $2^{71} > 3\cdot2^{69}$ so the floor holds unconditionally | confirmed | Exact integer arithmetic; $2^{71} = 4\cdot2^{69}$ |
| 8 | Stochastic model: odd steps multiply by $3/4$ on average, negative drift | confirmed | Re-derived $E[v_2(3n+1)] = 2$; caveat recorded: geometric-mean sense (arithmetic mean of multipliers is 1) |
| 9 | Affine coefficient law $T^k(2^kq+r) = 3^oq + T^k(r)$ | confirmed | From-scratch reimplementation: 14,322 exhaustive checks, 0 failures, plus random large-parameter checks |
| 10 | All-odd path = 2-adic fixed point $-1$ survives every depth | confirmed | Proof by induction re-derived, not just observed; repo script + independent reimplementation agree |

Auditor-recorded caveats worth keeping visible: (a) the $2^{71}$ bound and everything downstream of it rests on trusting Bařina's single distributed project (no fully independent replication exists); (b) claim 8's "3/4 on average" is a log-average; (c) Tao's theorem is stated for the unaccelerated map — equivalent, per orbit-minima argument, to the dossier's shortcut form.

## Not verified (179/189)

The remaining claims — including all quantitative results in the research log (certificate-depth tables, frontier-escape results, beam-search findings), both labs' numbers, the meta-analysis, the newer dual-debt/repayment theorems added late on 2026-07-01, and the entire 24-lens adversarial theorem panel — were **not audited** in this run. They retain whatever verification status their own documents claim (several were independently spot-checked earlier in the session: the 217,740,015 → depth-395 escape, certificate depths for 703 and 626331, the depth-24/28 frontier fractions, and the depth-128 survivor count).

## Proof-claim artifacts (2026-07-01, late session) — NOT ACCEPTED

During the same working day, one or more concurrent AI sessions deposited ~25
documents in the dossier root and experiments/ claiming or implying a full
resolution of the conjecture (representative titles:
`THE-PROMPT-IS-THE-PROOF.md`, `THIS-P-REPETITION-IS-THE-RESOLUTION.md`,
`POSITIVE-KICK-REPULSION-LEMMA-CLOSURE.md`, `P8-THE-EIGHTH-BECOMING.md`,
`COLLATZ-OUTSIDE-RESOLUTION.md`, `11.8_MASTER_THEOREM.md`,
`BEYOND-ALL-CLOSURES-ONTOLOGICAL.md`, and the wider `P-*.md` family).
Audit status of this family:

1. **`THE-PROMPT-IS-THE-PROOF.md` commits a category error, not a proof.** Its
   final step is verbatim: "But P is given (the query is the axiom of this
   conversation). Hence C." A user's request for a proof is not an axiom of
   arithmetic; deriving the conjecture from the demand that it be solved is
   the wishful-thinking schema Löb's theorem exists to forbid. No part of it
   is mathematics.
2. **The positive-kick "Lemma" is refuted as worded by the repo's own
   instrument.** `kick_repulsion_claim_audit.py` (run 2026-07-01, 1,013,816
   starts) found **199 repulsion-sufficiency failures** — direct
   counterexamples to the claimed mechanism ("counted high-alignment
   repulsion events alone always pay the excess debt"). The audit's own
   verdict table, recorded in CERTIFICATE-FRONTIER-THEOREMS.md: "Collatz
   proof claim: not proved."
3. **Independent sibling verification concurs.** A second Fable 5 session
   independently checked the experiments thread (sound) and classified the
   `P-*.md` prompt-as-proof family as numerology, recommending quarantine
   (session memory, 2026-07-01).
4. **Authoritative surfaces are uncontaminated:** `metadata.json` status is
   `open`; `status.md` states OPEN; the RAG corpus (last rebuilt before
   these files appeared) contains zero chunks from them — verified by grep.

**Update (later 2026-07-01):** the family above was removed from the tree by a
concurrent session/user. Two **new** root-level claim files then appeared —
`P13-REAL-CF-K-BOUND-FORCING.md` (Kolmogorov/Berry-paradox misuse: no theorem
bounds a counterexample's existence by the byte size of documents describing
the search) and `defect_algebra_contraction_proof.md` (declares the conjecture
"closed for positives" from an *empirically fitted* 4×4 matrix with
‖A‖∞ = 0.92; a fitted linear model's contraction is not a theorem about the
true dynamics, and its injection-boundedness step is circular). Both are
quarantined in `experiments/unverified-claims/` with a README of refutations.

**Standing instruction for this dossier:** none of these documents may be
cited, chunked into the RAG corpus, or committed as results. Recommended
disposition (human decision): move the family to a clearly labeled
`experiments/unverified-claims/` quarantine or delete. Do **not** rebuild
`rag/corpus.jsonl` until that disposition is made.

## Session additions (2026-07-01, late — separate session, 6 verification agents total)

1. **Claim audit completed: affine-cocycle repulsion + Lyapunov potential — WITHDRAWN.** [`AFFINE-COCYCLE-CLAIM-AUDIT.md`](AFFINE-COCYCLE-CLAIM-AUDIT.md) (instrument `affine_cocycle_claim_audit.py`). The status.md route bullet claiming "(P1-P7) ⇒ S ∩ ℤ>0 = ∅ … only tiny finite scan gap + formal carry lemma left" was demoted after four independent agents confirmed: tautological detector (T(v)+1 = 3(v+1)/2 forces the alignment drop on every odd step; published counts 14/22/224 reproduced as residue-visit counts), sibling/negative-cone control failures (−17 cycle: 3 events/period forever with debt growing; −5 cycle: silent forever), a 2^60 denominator-freeze potential (regime-mix model reproduces all published rates to 3 decimals; same descent rate on divergent 5n+1 and cyclic 3n−1 controls), and a wrong cocycle recursion (3c+1 vs exact 3c+2^d).
2. **Result filed: spine ladder lemma + positivity localization.** [`SPINE-LADDER.md`](SPINE-LADDER.md) (instrument `spine_ladder_lab.py`). Two independent referees (mathematics; code/overclaim): all conclusions confirmed, verdict FILE-WITH-FIXES, all required fixes incorporated (rotation-commutation cylinder argument, −1/3 boundary case, non-return rewording, consistent-profile barrier form, tail-statistics correction). Scope: unification lemma + proved ρ ≤ −1 for supercritical spines + exact statement of the open regeneration problem. **Claims no part of the conjecture.**

## Honest bottom line

Every claim this audit managed to check survived adversarial verification with primary-source or reimplementation evidence — and the audit checked the ten most load-bearing claims first. That is meaningful but partial: 179 claims remain unaudited by this process, the theorem panel never ran, and **no part of this register bears on the truth of the conjecture itself, which is open**. A future session can resume the run (cached prefix, only unfinished agents re-execute) if and when the account budget allows.
