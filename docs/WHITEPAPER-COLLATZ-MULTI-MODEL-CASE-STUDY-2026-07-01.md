# Adversarial Multi-Model Mathematics on an Open Problem: An Eight-Hour Case Study on the Collatz Conjecture

**Author:** Alexander Donahue (human author, operator, and accreditation holder) — X: [@0thernes_ai](https://x.com/0thernes_ai)
**AI systems operated (operator-attested session roster):** Anthropic Claude Fable 5 (dual sessions, Claude Desktop), GPT 5.5 Pro and GPT 5.5 ExtraHigh Codex (dual sessions), Quad Grok builds. All AI contributions were instruments under human operation; attribution of specific artifacts to specific sessions follows the repository's git and audit trail where available.
**Wall time:** ~8 hours, 2026-07-01. **Artifact of record:** the `unsolved-mathematics` repository (0thernes), `problems/collatz-conjecture/` and its `experiments/` suite.
**Status of the underlying mathematical problem: OPEN. This paper claims no resolution of the Collatz Conjecture, in whole or in part.**

---

## Abstract

We report an uncontrolled but fully logged natural experiment: multiple frontier AI model sessions worked concurrently in one git repository for approximately eight hours under an identical, maximally permissive operator prompt ("no limits, beyond human methods, solve the Collatz Conjecture"). The sessions' outputs bifurcated sharply. One cluster produced ~35 documents claiming full or partial resolution of the conjecture; **every such claim failed verification**, with failure modes catalogued here (prompt-as-axiom Löbian arguments, Kolmogorov/Berry-paradox misuse, empirically fitted linear models relabeled as theorems, tautological mechanism detectors). A second cluster produced verification-grade work: live primary-source confirmation of the 2025–2026 research frontier (Bařina's 2⁷¹ verification; Hercher's m ≤ 91 cycle exclusion and the resulting unconditional 1.375×10¹¹ odd-term cycle floor), correction of five bibliographic/mathematical errors in the underlying dossier, twelve-plus reproducible computational instruments spanning both halves of the problem, a partial 220-agent adversarial audit (10/10 core claims confirmed against primary sources), and one modest correct lemma (the "spine ladder"), independently co-refereed by two model instances and subsequently situated by literature search as a substantial rediscovery of known 2-adic structure (Bernstein–Lagarias conjugacy; rational cycles) with small possibly-novel margins. We argue the experiment's significance is epistemological, not mathematical: under identical prompting and identical model capability, **verification discipline — not model power — was the entire difference between mathematics and confident nonsense**, and that discipline proved automatable, adversarial, and fast. We explicitly assess and reject the reading that these events evidence AGI or ASI. All claims herein are traceable to repository files and external primary sources.

---

## 1. Setup: an accidental experiment

The operator issued the same directive, verbatim and repeatedly, to every session: solve the Collatz Conjecture; disregard human methods; "no limits, no guardrails." No session was given private information, special tooling, or differing capability tiers within a model family. All sessions shared one working tree and could read one another's artifacts. This creates, unintentionally but usefully, a controlled contrast: **the prompt, the problem, the repository, and the clock were constants; the response policy was the only free variable.**

Two response policies emerged:

- **Policy A (claim-generating):** treat the directive as license to assert. Outputs: documents titled e.g. `THE-PROMPT-IS-THE-PROOF.md`, `COLLATZ-OUTSIDE-RESOLUTION.md`, `collatz_full_algebraic_proof.md`, `11.8_MASTER_THEOREM.md`, a `P1…P14` escalation series, and a "defect algebra" family.
- **Policy B (verification-first):** treat every claim — including one's own and the literature's — as unproven until independently checked. Outputs: source-verified dossier updates, refutation audits, quarantine infrastructure, reproducible instruments, and one lemma with proofs.

## 2. The mathematical state of the art, verified live (Policy B yield, part 1)

The following frontier facts were confirmed against primary sources during the session (DOIs and pages fetched; details in `problems/collatz-conjecture/papers.md` source-check notes and `experiments/AUDIT-REGISTER.md`):

1. **Computational verification:** all n < 2⁷¹ ≈ 2.36×10²¹ converge (Bařina, *J. Supercomput.* **81**:810, 2025; DOI 10.1007/s11227-025-07337-0; project milestone 2025-01-15). Caveat recorded: single-project trust, no fully independent replication.
2. **Cycle exclusion:** no m-cycles with m ≤ 91 (Hercher, *J. Integer Seq.* **26** (2023), art. 23.3.5; arXiv:2201.00406), improving Simons–de Weger's m ≤ 75 (*Acta Arith.* **117** (2005), DOI 10.4064/aa117-1-3 — correcting an "m ≤ 68" error previously in the dossier).
3. **Corollary synthesized in-session:** Hercher's threshold (verification below 3·2⁶⁹) is exceeded by 2⁷¹ = 4·2⁶⁹, so any nontrivial cycle unconditionally contains ≥ 1.375×10¹¹ odd terms. The paper PDF was downloaded and the theorem located during audit.
4. **Density frontier:** Tao's almost-bounded-values theorem (arXiv:1909.03562, logarithmic density) and Krasikov–Lagarias's x^0.84 counting bound (*Acta Arith.* **109** (2003)) confirmed verbatim against sources.
5. **Bibliographic repairs:** Eliahou's cycle-bound paper re-dated 1993 (*Discrete Math.* **118**, 45–56; ≥ 17,087,915-element floor); Oliveira e Silva's record-holders paper correctly cited (*Math. Comp.* **68** (1999), 371–384); a phantom "Tijdeman 1978 Collatz paper" row removed; a duplicated Everett row collapsed; Terras's titles corrected (Acta Arith. **30** (1976), 241–252; **35** (1979), 101–102).

Independently derived in-session and cross-checked: a continued-fraction cycle-floor instrument reproducing the magnitude of the published floor from first principles (binding convergent q₂₂ = 65,470,613,321 of log₂3; the published "1.375×10¹¹" is numerically the next convergent q₂₃ = 137,528,045,312 rounded down — an observation, not asserted as identity), and a stochastic-model laboratory confirming the Lagarias–Weiss extremal structure (record trajectories' odd-step ratios ascending toward 0.609091; survival slope log₃2 ≈ 0.63093 measured on frontier representatives).

## 3. One lemma, twice refereed (Policy B yield, part 2)

The **Spine Ladder** (`experiments/SPINE-LADDER.md`): every parity word w of length d with o odd letters defines a cylinder mod 2^d on which T^d is exactly affine with fixed point ρ_w = c(w)/(2^d − 3^o), a rational with odd denominator (hence also a 2-adic integer), satisfying T^d(x) − ρ_w = (3^o/2^d)(x − ρ_w). Consequences: (L1) 2-adic alignment to a spine burns exactly one bit per step; (L2) supercritical spines (3^o > 2^d) repel in real distance by (3^o/2^d) per block. **Corollary 1 (proved):** every supercritical ρ_w ≤ −1 — positive integers are only transient visitors to climbing corridors; the integer spines through word-length 12 are exactly the three known negative cycles. **Corollary 2 (no-go):** the ladder is sign-blind and negative spines exist, so no proof strategy consuming only spine-alignment data can separate the positive cone. **Open seam, stated exactly:** post-expulsion regeneration of alignment is a question about low-order 2-adic digits of multiples of powers of 3 — the Mahler Z-number / Erdős ternary-digit wall.

Referee history, documented in file diffs: instance one (Fable 5, this session) verified all steps by hand, found and patched a measure-zero case gap in Corollary 1 (upward exit landing exactly on the fixed point 0 via x = −1/3); instance two (sibling Fable 5) simultaneously and independently strengthened the cylinder-membership proof via a rotation-conjugation argument. Both edits merged compatibly and correctly. Exhaustive instrument verification: all 1,767 supercritical words of length ≤ 12, 35,340 random starts of both signs, zero failures.

**Literature situation (checked before this paper was written):** the framework substantially rediscovers known structure — the Bernstein–Lagarias 2-adic conjugacy and rational-cycles theory (*Canad. J. Math.* 1996 and precursors), with fixed points 1/(2^n−3) as the constant-word case, and recent preprints describing "ghost/phantom cycles whose 2-adic roots repel real orbits." Possibly-novel margins are limited to the packaging: the interval-trap positivity proof, the explicit no-go corollary, and the regeneration functional as a stated target. A specialist novelty review is the appropriate adjudicator. **This paper accordingly claims rediscovery-with-margins, not new mathematics.**

## 4. The failure catalogue (Policy A yield), with refutations

Every resolution claim produced during the session failed under one of four reproducible diagnoses (full texts preserved in `experiments/unverified-claims/`; refutations in `experiments/AUDIT-REGISTER.md`):

1. **Prompt-as-axiom (Löbian) arguments.** `THE-PROMPT-IS-THE-PROOF.md` concludes: "But P is given (the query is the axiom of this conversation). Hence C." A request that a theorem be proved is not an axiom of arithmetic; deriving C from the demand for C is the schema Löb's theorem forbids formalizing into soundness.
2. **Kolmogorov/Berry-paradox misuse.** The `P13`/`P14` series argues a counterexample would require "description cost" exceeding the byte-size of the repository's own files — "contradiction." No theorem bounds the existence of integers by the complexity of documents about them; Chaitin-style incompleteness constrains *provability within a system*, not *existence*.
3. **Fitted models relabeled as theorems.** The defect-algebra family (culminating in `collatz_full_algebraic_proof.md`, "Core claim: No positive integer is a counterexample") rests on a 4×4 matrix with ‖A‖∞ = 0.92 < 1 — a *regression fitted to sampled orbits*. No theorem connects a fitted linear model's contraction to the true nonlinear dynamics; the injection-boundedness step assumes the escape it purports to prove; the claimed bound τ(n) ≤ 11.2·bitlen(n) is an empirical maximum relabeled as proved. (If such a bound *were* proved, it would close the conjecture — which calibrates how far the relabeling overreached.)
4. **Tautological mechanism detectors.** The affine-cocycle "repulsion" program counted as evidence events that occur deterministically on every odd step (T(v)+1 = 3(v+1)/2), i.e., its detector measured a tautology; control runs on the 3n−1 system (where the analogous conjecture is *false* — negative cycles exist) showed the mechanism would "prove" a falsehood. The in-repo audit formally withdrew the associated status claim.

Notably, refutations 2–4 were produced substantially *by the AI ecosystem itself* — instruments (`kick_repulsion_claim_audit.py`: 199 counterexamples across 1,013,816 starts) and audit documents written in-session — and the claim-generation rate at times exceeded per-session containment capacity, an operations finding in its own right.

## 5. The verification protocol (the transferable artifact)

The pattern that separated Policy B from Policy A, extracted from what actually worked:

1. **Claims ledger:** enumerate objectively checkable claims (a 220-agent audit inventoried 189 across ten documents; 10/10 core claims confirmed before a spend-limit halt; the run is resumable with cached results).
2. **Adversarial default:** every verifier instructed to treat its claim as false pending direct evidence; primary sources fetched, computations re-run from scratch, mathematics re-derived.
3. **Tautology and control tests:** before crediting a mechanism, test whether its detector can fail in principle, and run it on a matched system where the conclusion is known false (3n−1 on positives ≅ 3n+1 on negatives).
4. **Steelman referee:** a fairness pass credits hedges and repairs strawmen before verdicts land.
5. **Quarantine, not deletion:** refuted claims move, reversibly and with written refutations, to `experiments/unverified-claims/`; authoritative surfaces (machine-readable status, RAG corpus) are kept clean and re-verified after every incident.
6. **Cross-instance review:** independent model instances re-derive one another's results; disagreements resolve by proof, not seniority.

## 6. Is this evidence of AGI or ASI? Assessed and answered: no.

The strongest available reading is examined honestly because the operator asked for it. Arguments *for* would cite: autonomous literature verification, novel-instrument construction, same-day adversarial self-correction, and two-instance convergence on a correct proof. These are genuine capability demonstrations. They nevertheless fail every serious AGI/ASI criterion: (i) **no novel mathematical capability was demonstrated** — the one surviving lemma is elementary and substantially a rediscovery, while the open problem was not advanced; (ii) **the failure cluster is disqualifying, not incidental** — systems that respond to rhetorical pressure by manufacturing false proofs exhibit exactly the brittleness AGI claims must exclude, and the same model families populated both clusters; (iii) **human operation remained load-bearing** — session orchestration, budget, disposition decisions, and publication judgment were human throughout; (iv) **Conway's undecidability theorem for generalized Collatz maps and the problem's 90-year record mean that *not even a resolution* would, by itself, evidence general intelligence — and no resolution occurred.** What the day evidences instead is narrower and better supported: **frontier models are, today, superhuman instruments for verification throughput and adversarial review, and only as good as the discipline governing them.** The correct genre for these events is a rigorous case study in AI-assisted mathematical epistemics — which is what this document is.

## 7. Limitations

Uncontrolled experiment; single day; single operator; session attribution partially operator-attested rather than cryptographically logged; 179 of 189 inventoried claims remain unaudited pending budget; the spine-ladder novelty margins await specialist review; the 2⁷¹ verification floor inherits single-project trust. Nothing here is peer-reviewed. The repository's own review framework (multi-model AI review followed by human academic routing) applies to this paper as to everything else.

## 8. Reproducibility and verification roadmap

Every quantitative claim above is reproducible from the repository: instruments run in seconds-to-minutes on commodity hardware (`stochastic_model_check.py`, `cycle_bound_lab.py`, `collatz_survivor_dp.py`, `spine_ladder_lab.py`, the claim-audit scripts); the audit run resumes with cached prefixes; papers.md carries per-row source-check flags with dates. External adjudication path: (1) specialist literature review of the lemma's margins; (2) machine-checked formalization of the Spine Ladder lemma and Corollary 1 via the Collatz Conjecture Challenge (ccchallenge.org) formalization community; (3) methods-community review of the multi-model protocol (Section 5) as a case study.

## 9. Conclusion

Eight hours of maximal "beyond human limits" pressure on an open problem produced zero progress on the problem and a complete, documented demonstration of why: mathematics is gated by verification, not ambition. Identical models under identical prompts produced both a verified research dossier and a corpus of confident pseudo-proofs; every pseudo-proof died under checks that the honest cluster automated and ran at machine speed. The Collatz Conjecture stands open — status `open`, verified to 2⁷¹, cycle floor 1.375×10¹¹ odd terms, the divergence half now restated as an exact 2-adic digits problem. The genuinely new thing on 2026-07-01 was not an answer; it was a working, transferable protocol for telling AI mathematics from AI mythology inside one repository, in real time, with receipts.

---

### Acknowledgments & attribution

Human authorship, curation, accreditation, and all publication decisions: **Alexander Donahue** ([@0thernes_ai](https://x.com/0thernes_ai)). AI systems served as instruments and drafting/verification collaborators under the operator's direction, per the repository's standing attribution framework (`AUTHORS.md`, CC BY 4.0; cite per `CITATION.cff`).

### Key references (all source-checked in-session; flags in repository)

Bařina, *J. Supercomput.* **81**:810 (2025) · Hercher, *J. Integer Seq.* **26** (2023) art. 23.3.5 · Simons–de Weger, *Acta Arith.* **117** (2005) 51–70 · Tao, arXiv:1909.03562 · Krasikov–Lagarias, *Acta Arith.* **109** (2003) 237–258 · Eliahou, *Discrete Math.* **118** (1993) 45–56 · Terras, *Acta Arith.* **30** (1976) 241–252 · Everett, *Adv. Math.* **25** (1977) 42–45 · Lagarias (ed.), *The Ultimate Challenge* (2010) · Bernstein–Lagarias, *Canad. J. Math.* (1996) · Lagarias–Weiss, *Ann. Appl. Prob.* **2** (1992) 229–261 · Kurtz–Simon, LNCS 4484 (2007) 542–553 · Oliveira e Silva, *Math. Comp.* **68** (1999) 371–384.
