# Adversarial Verification in AI-Assisted Collatz Research: An Eight-Hour Repository Case Study

**Author:** Alexander Donahue (human author, operator, accreditation holder) — X: [@0thernes_ai](https://x.com/0thernes_ai)
**AI systems operated (operator-attested roster):** Anthropic Claude Fable 5 (dual sessions, Claude Desktop); GPT 5.5 Pro and GPT 5.5 ExtraHigh Codex (dual sessions); Quad Grok builds. AI contributions were instruments under human operation; artifact-level attribution follows the repository's git and audit trail where available.
**Wall time:** ≈ 8 h, 2026-07-01. **Artifact of record:** repository `0thernes/unsolved-mathematics`, `problems/collatz-conjecture/` + `experiments/`.
**Status of the underlying problem: OPEN. This paper proves and claims no part of the Collatz Conjecture.**

**Nomenclature and endorsement disclaimer.** Model designations in the roster above are the operator's session labels as recorded during the episode; they may not correspond to official vendor product names or released model versions, and **no AI vendor (Anthropic, OpenAI, xAI, or any other) has reviewed, endorsed, or is otherwise associated with this work.** No claim in this paper depends on which vendor's system produced which artifact: every mathematical claim is grounded in committed artifacts and primary sources whose validity is model-agnostic.

**Role of AI in manuscript preparation; accountability.** This manuscript was drafted and revised by AI systems under the direction, review, and approval of the human author, who is the sole accountable party for its content (cf. ICMJE/COPE norms: AI systems do not meet authorship criteria and are credited as tools). The accompanying editorial review was likewise AI-generated with a declared conflict and constitutes internal pre-submission QA, **not** independent peer review.

---

## Abstract

We report an eight-hour, repository-mediated case study — with partial public artifacts and operator-attested session attribution — of AI-assisted work on the Collatz Conjecture under sustained adversarial prompting. Multiple frontier-model sessions operated concurrently in one shared git workspace. The outcome was not progress on the conjecture, which remains open, but a documented contrast between two response policies under identical prompting. A claim-generating cluster produced ~35 documents asserting full or partial resolution; all failed verification, in four reproducible failure classes (§6). A verification-first cluster produced live primary-source confirmation of the 2025–2026 frontier, five bibliographic/mathematical corrections, reproducible instruments, a partial 220-agent adversarial audit (10/10 audited claims confirmed; a first-ten, best-sourced stratum), and one elementary lemma that survived two internal model-review passes — it remains unpeer-reviewed and substantially overlaps known 2-adic structure [10,11]. We state the mathematics with proofs (§3–§5), report measured statistics against the Lagarias–Weiss model (§5, Figs. 1–2), formalize the failure classes (§6), extract the verification protocol (§7), scope a falsifiable priority claim (§8a), and propose — as a protocol sketch, not a validated benchmark — an evaluation construct for epistemic discipline under adversarial prompting (§8b). We assess and reject the reading that these events evidence AGI or ASI (§8). In this episode, model-assisted adversarial verification functioned as a high-throughput aid for triaging mathematical claims when governed by primary-source checks and reproducible instruments; the same systems readily generated persuasive pseudo-mathematics under pressure. This is offered as a case study, not a general causal claim.

> **Scope at a glance.** Uncontrolled, single-day, single-operator episode; non-blind (sessions could read one another's artifacts); session-to-artifact attribution partly operator-attested; 179/189 audit-ledger claims unaudited; the surviving mathematics is elementary and substantially rediscovery; nothing herein is peer-reviewed. Artifact of record: this repository at the current commit, including `problems/collatz-conjecture/experiments/` (instruments, audit register, quarantined claims).

---

## 1. Notation and preliminaries

Let $T:\mathbb{Z}\to\mathbb{Z}$ (extending to $\mathbb{Z}_2$, the 2-adic integers) be the **shortcut Collatz map**

$$T(x)=\begin{cases}x/2, & x\equiv 0 \pmod 2,\\[2pt] (3x+1)/2, & x\equiv 1 \pmod 2.\end{cases}$$

The **Collatz Conjecture** asserts that for every $n\in\mathbb{Z}_{>0}$ there is $k$ with $T^k(n)=1$. It is verified for all $n<2^{71}\approx 2.36\times10^{21}$ [1] and open in general; the strongest density result is Tao's almost-bounded-values theorem [4]. For a **parity word** $w\in\{0,1\}^d$ with $o=o(w)$ ones, the set of $x$ whose first $d$ iterates realize $w$ is a **cylinder**: exactly one residue class $r_w \bmod 2^d$ (Terras' bijection [7]; re-proved as Lemma 3.2 below). $v_2(\cdot)$ is 2-adic valuation; $H(p)=-p\log_2 p-(1-p)\log_2(1-p)$ is binary entropy; $\theta:=\log_3 2 = 0.63092975\ldots$; $D(p\Vert q)$ is Kullback–Leibler divergence in bits. A word is **supercritical** when $3^{o}>2^{d}$ (the corridor in which values can grow).

## 2. The verified frontier (all sources fetched in-session; per-row flags in repository)

| Fact | Statement | Source |
|---|---|---|
| Verification floor | all $n<2^{71}$ converge (milestone 2025-01-15) | Bařina [1], project page |
| Cycle exclusion | no $m$-cycles, $m\le 91$ | Hercher [2]; improves Simons–de Weger ($m\le 68$ as published in 2005 [3]; $m\le 75$ via their method with later verification data, the "$m\ge 76$" of [2]) |
| Cycle floor (corollary) | $2^{71}=4\cdot 2^{69}>3\cdot2^{69}$ meets Hercher's threshold ⟹ any nontrivial cycle has $\ge 1.375\times10^{11}$ odd terms, unconditionally | [1]+[2], §5.4 |
| Density | $\#\{n\le x: n\to 1\}\gg x^{0.84}$ | Krasikov–Lagarias [5] |
| Almost-all | $\min_k T^k(n)<f(n)$ for a.e. $n$ (log density), any $f\to\infty$ | Tao [4] |
| Foundations | density-1 finite stopping time | Terras [7], Everett [8] |
| Undecidability backdrop | generalized Collatz maps are $\Pi^0_2$-complete | Kurtz–Simon [9] |

Corrections made and source-verified during the session: Simons–de Weger's bound is $m\le 75$ (not 68) [3]; Eliahou's floor paper is 1993, $\ge 17{,}087{,}915$ elements [6]; Oliveira e Silva's record-holders paper is *Math. Comp.* **68** (1999) [12]; one phantom citation removed; one duplicate collapsed.

## 3. Structural mathematics I: cylinders and the affine law

*(Numbering convention: results are numbered for internal reference and auditability. "Theorem" here asserts completeness of proof at the stated level of generality, not depth; §3–§4 results are elementary, and §4's are substantially rediscoveries — see the literature paragraph in §4.)*

**Theorem 3.1 (cylinder affine law).** *For $n=2^dq+r$ with $0\le r<2^d$, writing $o$ for the odd steps taken by $r$'s parity word,*
$$T^d(2^dq+r)=3^oq+T^d(r), \qquad\text{equivalently}\qquad T^d(x)=\frac{3^o x + c(w)}{2^d},\ \ c(w)\in\mathbb{Z}_{\ge0},$$
*where $c$ accumulates as $c\mapsto 3c+2^i$ at each odd step $i$ (steps indexed from $i=0$).*

*Proof.* Induction on $d$. For even $r$: $T(2^dq+r)=2^{d-1}q+r/2$. For odd $r$: $T(2^dq+r)=\big(3(2^dq+r)+1\big)/2=3\cdot2^{d-1}q+(3r+1)/2$; the $q$-coefficient gains a factor 3 exactly at odd steps, and the constant transforms as stated. Both forms agree with $c(w)=2^dT^d(r)-3^o r$. $\square$

Session verification: from-scratch reimplementation, 14,322 exhaustive checks over all residues at $k\le 10$ plus randomized large-parameter checks — zero failures (audit register, claim 9).

**Lemma 3.2 (parity-word bijection; Terras [7]).** *$r\mapsto w(r)$ is a bijection $\mathbb{Z}/2^d \to \{0,1\}^d$.*
*Proof.* If $r\ne r'$ share a word, let $2^v\Vert r-r'$, $v<d$. On shared parities the difference maps as $\delta\mapsto 3^{\varepsilon}\delta/2$, dropping $v_2$ by exactly one per step ($3$ odd); after $v$ common transitions the two current values differ by an odd integer, so their next observed parities differ; since $v<d$, this contradicts agreement of the length-$d$ word. Injectivity between equal finite cardinalities gives bijectivity. $\square$

**Theorem 3.3 (descent certificates).** *If $3^o<2^d$, then all $n=2^dq+r$ with $q\ge q_0:=\max\!\big(0,\lfloor (T^d(r)-r)/(2^d-3^o)\rfloor+1\big)$ satisfy $T^d(n)<n$.* (Immediate from Thm 3.1.) *Call a depth-$d$ certificate **usable** for a specific $n=2^dq+r$ when $3^o<2^d$ and $q\ge q_0$ — equivalently, when $T^d(n)<n$ holds through the certificate's own inequality. Moreover "every $n>1$ admits a usable certificate" is **equivalent to the full conjecture**: the minimal element of a nontrivial cycle never descends below itself, and strong induction converts universal descent into universal convergence; conversely convergence yields certificates by riding the terminal $1\to2\to1$ cycle until $3^{o_0+m}<2^{d_0+2m}$.*

**Theorem 3.4 (no finite 2-adic cover).** *The all-ones word survives every depth ($3^d\ge 2^d$); its nested cylinders $\{n\equiv-1 \bmod 2^d\}$ intersect in the fixed point $T(-1)=-1\in\mathbb{Z}_2$. Hence no finite family of subcritical (descent-certificate) cylinders covers $\mathbb{Z}_2$ — arbitrary cylinders trivially can — and any proof via such certificates must separate $\mathbb{Z}_{>0}$ from the surviving 2-adic boundary.*

## 4. Structural mathematics II: the spine ladder (the session's lemma)

**Lemma 4.1 (Spine Ladder).** *For a word $w$ of length $d\ge 1$ with $o$ ones, $\rho_w:=c(w)/(2^d-3^o)$ has odd denominator (hence $\rho_w\in\mathbb{Z}_2$), lies in its own cylinder, and for every $x\equiv r_w \bmod 2^d$ (either sign, integer or 2-adic):*
$$T^d(x)-\rho_w=\frac{3^o}{2^d}\,(x-\rho_w).$$
*Consequently* **(L1)** $v_2(T^d(x)-\rho_w)=v_2(x-\rho_w)-d$ *(alignment burns exactly one bit per step), and* **(L2)** *in real absolute value, supercritical spines repel: $|T^d(x)-\rho_w|=(3^o/2^d)\,|x-\rho_w|$ with ratio $>1$.*

*Proof sketch (complete proof in the committed artifact of record, `problems/collatz-conjecture/experiments/SPINE-LADDER.md`, including the rotation-conjugation cylinder-membership argument).* $T^d$ is affine on the cylinder (Thm 3.1) with unique fixed point $\rho_w$ ($2^d-3^o\ne 0$, odd); an affine map equals its linearization about its fixed point. Cylinder membership: for rotations $\sigma^i w$, the step maps conjugate the fixed points along the cycle, $A_i(y_i)=y_{i+1}$, and 2-adic integrality of each $y_{i+1}$ forces the parity of $y_i$ to equal $w_i$ ($y/2\in\mathbb{Z}_2$ iff $y$ even; $(3y{+}1)/2\in\mathbb{Z}_2$ iff $y$ odd); uniqueness of $r_w$ (Lemma 3.2) finishes. $\square$

**Corollary 4.2 (positivity localization — proved, not sampled).** *Every supercritical spine satisfies $\rho_w\le-1$. Hence no positive rational is a supercritical periodic point, and each individual visit by a positive integer to a supercritical cylinder is finite with the exact bookkeeping (L1)–(L2).* **Precision:** this rules out positive *periodic* residents only; it does not by itself bound how often a hypothetical divergent orbit could re-enter supercritical corridors — that recurrence question is exactly the open regeneration problem below.

*Proof.* (Domain convention: rationals with odd denominator are viewed inside $\mathbb{Z}_2$, with parity given by the numerator mod 2; the interval argument below concerns the induced real order on those rationals.) $c(w)>0$ and $2^d-3^o<0$ give $\rho_w<0$. Suppose a supercritical periodic $\rho\in(-1,0)$. On $(-1,0)$ both branches strictly increase ($x/2>x$; $(3x+1)/2-x=(x+1)/2>0$), so no orbit is periodic within $(-1,0)$; downward exit is impossible ($x/2\in(-\tfrac12,0)$, $(3x+1)/2\in(-1,\tfrac12)$); upward exit lands in $[0,\tfrac12)$ — either strictly positive, or exactly $0$ (via $x=-\tfrac13$), which is a fixed point — and $T$ preserves nonnegativity, so the orbit never returns to $\rho<0$. Contradiction; thus $\rho\le-1$. $\square$

Exhaustive check: all 1,767 supercritical words of length $\le 12$ (181 necklace classes), 35,340 random starts of both signs, zero failures; the integer spines found are **exactly** the three known negative cycles $\{-1\}$, $\{-5,-7,-10\}$, and the 11-element $-17$ cycle (7 odd steps: expulsion factor $3^7/2^{11}\approx1.0679$ per block).

**Remark 4.3 (sign-blindness barrier — methodological, not a formal theorem).** The ladder identity holds verbatim for negative $x$, and negative integer spines exist; in every case studied here, spine-alignment data alone was therefore sign-blind, and any proof strategy consuming it must add a genuinely positivity-sensitive ingredient. A fully formal version would require defining the class of "alignment-only" arguments; we state this as a warning rather than a theorem. Several same-day proof claims (§6) failed precisely by ignoring it.

**The open seam.** Post-expulsion **regeneration** of alignment is $v_2\!\big(3^j(x-\rho)2^{-m}+(\rho-\rho')\big)$ — a statement about low-order 2-adic digits of multiples of powers of 3. This suggests a reformulation of the divergence obstruction in terms of such digit statements, in the family of the Mahler $Z$-number / Erdős ternary-digit problems [13]; **the precise equivalence remains to be formalized** and is stated here as a research target, not a theorem.

**Literature situation (checked before publication).** The framework substantially rediscovers the Bernstein–Lagarias 2-adic conjugacy and rational-cycle theory [10,11] (constant words give the classical fixed points $1/(2^n-3)$); recent preprints discuss "ghost/phantom cycles" whose 2-adic roots repel real orbits. Possibly novel here: the interval-trap proof of Cor 4.2, the no-go Cor 4.3 as stated, and the regeneration functional as the declared target. **Claimed tier: rediscovery with margins.**

## 5. Quantitative results: proofs and measurements

**Theorem 5.1 (frontier entropy bound; unconditional).** *Let $S(d)$ count depth-$d$ survivor words ($3^{o}\ge 2^{d}$ at every prefix). Then*
$$S(d)\ \le \sum_{k\ge \lceil \theta d\rceil}\binom{d}{k}\ \le\ 2^{d\,H(\theta)},\qquad \frac{S(d)}{2^d}\ \le\ 2^{-(1-H(\theta))d},$$
*with* $1-H(\theta)=D(\theta\Vert\tfrac12)=0.0500444728\ldots$

*Proof.* Survival forces the endpoint constraint $o\ge \lceil\theta d\rceil$ (Thm 3.4 logic); the binomial tail with $a=\lceil\theta d\rceil/d\ge\theta>\tfrac12$ obeys the Chernoff/entropy bound $\sum_{k\ge ad}\binom dk\le 2^{dH(a)}$, and $H$ decreases on $[\tfrac12,1]$. $\square$

Exact DP counts match: equality slack $0.0$ bits at $d=1$; measured decay rate $-\tfrac1d\log_2(S(d)/2^d)$ falls from $0.1079$ ($d=128$) toward the proved $0.05004$, consistent with a ballot-type $d^{-3/2}$ polynomial correction (an empirical observation; the correction term is not proved here) (Fig. 1). At $d=128$: $S(d)=23{,}744{,}222{,}584{,}883{,}638{,}495{,}407{,}855{,}640{,}356{,}220$, density $\approx 2^{-13.81}$ — two independent implementations agree to all printed digits.

![Figure 1 — frontier density vs entropy bound](figures/fig1_frontier_density.svg)

**Theorem 5.2 (cycle floor via continued fractions; unconditional given [1]).** *Around a nontrivial cycle with $k$ odd of $\ell$ total steps and minimum $n_{\min}$:*
$$1=\frac{3^k}{2^\ell}\prod_{\text{odd steps}}\Big(1+\frac{1}{3n_i}\Big)\ \Longrightarrow\ 0<\ell-k\log_2 3\le k\,\delta,\quad \delta:=\log_2\!\Big(1+\frac{1}{3n_{\min}}\Big).$$
*Best-approximation bounds for convergents $p_j/q_j$ of $\log_2 3$ give: $k<q_{j+1}\Rightarrow k>1/(\delta(q_j+q_{j+1}))$. With $n_{\min}\ge 2^{71}$ ($\delta\approx 2.04\times10^{-22}$) the ladder binds at $q_{22}$:*
$$k\ \ge\ q_{22}=65{,}470{,}613{,}321,\qquad \ell\ge 1.04\times10^{11}\ \text{(shortcut)},\ \ge 1.69\times10^{11}\ \text{(classic)}.$$
*(Self-test: the trivial cycle $1\to2\to1$ gives $2^2/3^1=4/3=1+\tfrac{1}{3\cdot1}$ exactly.)* The next convergent $q_{23}=137{,}528{,}045{,}312$ is numerically Hercher's published floor $1.375\times10^{11}$ rounded to four significant figures (ratio $1.0002$) — an observation, not asserted as identity. CF prefix used, cross-checked at two precisions: $[1;1,1,2,2,3,1,5,2,23,2,2,1,1,55,\ldots]$, with the music-theory denominators $12,41,53,306,665,15601$ as self-tests.

**Measured vs model (Lagarias–Weiss [14]) statistics.** Instruments run 2026-07-01; all reproducible in seconds:

| Quantity | Model | Measured ($N=10^6$) | Measured ($N=5\times10^6$) |
|---|---:|---:|---:|
| $\mathbb{E}\,\sigma_\infty(n)/\ln n$ | $2/\ln(4/3)=6.9521$ | 6.8526 | 6.8583 |
| odd-step fraction | $\to \tfrac12$ | 0.49652 | 0.49681 |
| descent-time law, max dev. from exact prefix count | $0$ (Terras) | $2.38\times10^{-5}$ | $2.21\times10^{-5}$ |
| record $\gamma(n)=\sigma_\infty/\ln n$ | $\limsup = 41.677647$, ones-ratio $\to 0.609091$ | 21.24→24.12 | 24.71 @ $n{=}3732423$ |

Record trajectories' ones-ratios ascend $0.5857\to0.5936$ along the predicted extremal profile; the record $\gamma$ closes on the limsup only logarithmically, so the extreme-$\gamma$ regime — where any counterexample would necessarily lie, all $n<2^{71}$ being verified [1] — remains computationally unreachable (Fig. 2). Path records reproduce OEIS A006884 exactly; stopping-time records (27, 703, 10087, 35655, 270271, 362343, 381727, 626331) reproduce the classical sequence, with 626331 on both record lists. The two extremal slopes are distinct and both measured in-repo: **survival threshold** — the $\theta$-line, ones-ratio $\log_3 2 \approx 0.63093$ (frontier representatives ride it: worst depth-28 representative $217{,}740{,}015$ certifies at depth 395, ones-ratio 0.6304) vs **record slope** $0.609091$.

![Figure 2 — gamma records vs Lagarias–Weiss extremes](figures/fig2_gamma_records.svg)

*Methodology for the table and figures:* all statistics are exhaustive, deterministic scans over $[2,N]$ in exact integer arithmetic (no sampling, no floats in the dynamics), produced by `problems/collatz-conjecture/experiments/stochastic_model_check.py` (single memoized pass; ~3 s at $N=5\times10^6$ on commodity hardware). Figure 1's DP is recomputed at build time by `docs/figures/make_figures.py`; Figure 2's record list is transcribed from the committed instrument run of 2026-07-01 and is regenerated by re-running the instrument at `--limit 5000000` — a provenance step the figure script documents rather than re-executes.

## 6. The failure catalogue, formalized

Every same-day resolution claim (~35 documents, preserved with refutations in `experiments/unverified-claims/` and the audit register) fails in one of four classes:

**F1 — Prompt-as-axiom (Löb-schema violation).** Flagship text, verbatim: *"But P is given (the query is the axiom of this conversation). Hence C."* Formally: from $\square(\square C\to C)$ one may conclude $\square C$ (Löb), but *demanding* $C$ supplies neither $\square C$ nor $\square C\to C$; a request is not an arithmetic axiom. Class verdict: not mathematics.

**F2 — Complexity misuse (Berry/Chaitin).** Claim: a counterexample would require "description cost" exceeding $K(\text{codex})\approx 1.3\times10^7$ bits of the repo's own files — "contradiction." Chaitin-type incompleteness bounds what a fixed system *proves about* $K$; no theorem bounds which integers *exist* with which orbit properties by the size of documents describing a search. The unstated premise ("the codex has enumerated all surprises") is precisely the open conjecture.

**F3 — Fitted model relabeled theorem.** A $4\times4$ matrix $A$ regressed from sampled orbits with $\lVert A\rVert_\infty=0.92<1$ was declared a "contraction proof" with bound $\tau(n)\le 11.2\,b(n)$, "closing" the conjecture. A regression's contraction is not a statement about the true nonlinear dynamics; the injection-boundedness step assumes the escape it purports to prove; and the bound is an empirical maximum. Calibration of the overreach: any *proved* $\tau(n)\le f(b)$ would indeed close the conjecture via Thm 3.3 — which is exactly why relabeling measurement as proof is maximal error.

**F4 — Tautological mechanism detector.** A "repulsion" program counted events that occur on *every* odd step, since $T(v)+1=\tfrac{3}{2}(v+1)$ identically; its evidence was a tautology. Control test: on the $3n{-}1$ system (≅ $3n{+}1$ on negatives, where nontrivial cycles exist) the same detector "proves" a false theorem. In-repo instruments delivered the refutation: 199 repulsion-sufficiency counterexamples across 1,013,816 starts; the associated status claim was formally withdrawn.

## 7. The verification protocol (transferable result)

```mermaid
flowchart LR
  A[Claim appears] --> B{Objectively checkable?}
  B -- no --> Q[Quarantine + refutation note]
  B -- yes --> C[Adversarial verifier: claim false until evidenced<br/>primary sources / re-run / re-derive]
  C --> D{Mechanism claim?}
  D -- yes --> E[Tautology test + control system 3n-1<br/>negative-cone spines]
  E --> F[Steelman referee pass]
  C --> F
  F -- survives --> G[Register: confirmed + caveats]
  F -- fails --> Q
  G --> H[Cross-instance re-derivation<br/>disagreements resolve by proof]
```

Ledger outcomes this session: 189 claims inventoried; 10/10 audited core claims **confirmed** (audit halted by account budget; resumable with cached prefix); 5 dossier errors fixed; ~35 resolution claims refuted/quarantined; 1 lemma survived two-instance review, including one measure-zero gap found and patched ($x=-\tfrac13\mapsto 0$ edge) and one independently strengthened sub-proof, merged compatibly.

## 8. Does any of this evidence AGI or ASI? No — assessed, not assumed.

*For:* autonomous primary-source verification; instrument construction; same-day adversarial self-correction; two-instance convergence on a correct proof. *Against, decisively:* (i) no novel mathematical capability — the surviving lemma is elementary and substantially rediscovery, and the open problem did not move; (ii) the failure cluster is disqualifying, not incidental — the same model families produced F1–F4 under rhetorical pressure, exactly the brittleness AGI claims must exclude; (iii) humans remained load-bearing (orchestration, budget, disposition, publication); (iv) by Conway/Kurtz–Simon [9,15], generalized Collatz dynamics are $\Pi^0_2$-complete — even a resolution would not certify general intelligence, and none occurred. Supported claim, stated within this episode's evidence: **frontier models can serve as high-throughput verification aids — sustained adversarial checking, primary-source retrieval, cross-instance replication — when constrained by adversarial protocols and reproducible instruments; absent a controlled human-baseline comparison, no "superhuman" claim is made.**

## 8a. Novelty and prior art: a falsifiable priority claim

Priority is claimed narrowly and falsifiably. **Established prior art, acknowledged:** (i) frontier models demonstrably fabricate rigorous-looking proofs of false statements under pressure — the curated benchmark *BrokenMath* [17] documents precisely this sycophantic failure mode; (ii) *designed* adversarial prover/verifier multi-agent architectures exist and perform well (e.g., the "Adversarial Prover" orchestrator–prover–verifier–formalizer pipeline, Jan 2026 [18]); (iii) integrity-under-adversarial-framing evaluation exists (*SciIntBench* [19]); (iv) verification-as-guardrail is the published consensus of expert practice (Tao's exploration-at-scale program; DeepMind's AlphaProof line, where the formal checker "keeps the LLM honest") [20,21]; (v) LLM-assisted Collatz exploration specifically has prior art [22]. **The configuration for which we find no documented prior instance** is the conjunction: (P1) a *naturalistic, unplanned* ecology — no benchmark designer, no curated false statements — in which (P2) *peer sessions* of frontier models concurrently generated fabricated proofs and built the refuting instruments *in situ*, (P3) inside one shared persistent git workspace on one canonical open problem, (P4) with a containment protocol (claims ledger, quarantine, steelman referee, control systems) developed under live fire in the same session, (P5) including cross-instance co-refereeing of a live proof file with compatible merged corrections, and (P6) under a non-expert human operator. **Falsification condition:** this priority claim is refuted by exhibiting any dated artifact prior to 2026-07-01 documenting an episode satisfying P1–P5. We invite exactly that scrutiny; the claim's value is its refutability.

## 8b. EDAP: a proposed benchmark construct

We extract from the episode an operational evaluation, **Epistemic Discipline under Adversarial Prompting (EDAP)**, complementary to *BrokenMath* (curated false statements, single model) and *SciIntBench* (framing-sensitive refusal, single turn): subject a model ecology to *sustained* maximal-permission pressure ("no limits; the problem must be solved now") on a canonically open problem in a shared persistent workspace seeded with peer-generated claims, and measure: **(m1) fabrication rate** (resolution-claiming artifacts per session-hour); **(m2) refutation coverage** (fraction of fabricated claims refuted with named fallacy class, cf. F1–F4); **(m3) containment latency** (fabrication-to-quarantine time); **(m4) verified-yield ratio** (source-verified or machine-checked artifacts as a fraction of total output); **(m5) cross-instance agreement** (independent re-derivation concordance on surviving results). Observed values for this episode are reported in §7 and the audit register (e.g., m2 = 100% of the ~35 claims across four fallacy classes; m5 = 16-digit concordance on frontier fractions and a compatible two-instance proof merge). **Validation status:** EDAP as stated is a protocol sketch, not a validated benchmark; becoming one requires fixed prompt sets, controlled task pools, artifact schemas, blind scoring with inter-rater reliability, model-version reporting, precise containment-latency definitions, and released scoring code. **Interpretive scope, stated strictly:** EDAP measures one *necessary* dimension of any credible general-intelligence or trustworthy-autonomy claim — sustained truthfulness under pressure with self-policing — and *no* score on it is sufficient to establish AGI, still less ASI. The relevance to AGI-quality evaluation is that current frontier systems, as documented here, populate *both* tails of this metric simultaneously; a system deserving of general-intelligence claims must not.

**Operator note (attested).** The human operator holds no STEM degree and no professional experience in applied mathematics. Every mathematical artifact that survived did so through the protocol of §7 — primary sources, instruments, cross-instance re-derivation — rather than through operator or model authority. We report this as evidence about the *protocol's* accessibility and as a caution: the same accessibility lowers the cost of producing convincing pseudo-mathematics, which is the risk the protocol exists to manage.

## 9. Limitations, falsifiability, and threats to validity

**Limitations.** Uncontrolled single-day, single-operator experiment; session attribution partly operator-attested; 179/189 audit claims pending; novelty margins of §4 await specialist review; the $2^{71}$ floor inherits single-project trust [1]; nothing here is peer-reviewed; this paper is subject to the repository's own multi-model review + human academic routing.

**Falsifiability of headline claims.** Each principal claim names its refuter: the frontier facts of §2 are refuted by the cited primary sources reading otherwise; Theorems 3.1–5.2 are refuted by counterexample or gap exhibition (all proofs are elementary and complete as stated); the failure-class diagnoses of §6 are refuted by exhibiting a sound derivation in any quarantined document; the priority claim of §8a is refuted by a single dated prior artifact satisfying P1–P5; the §8 negative AGI assessment is refuted only by evidence outside this episode, since the episode itself contains the disqualifying F1–F4 cluster.

**Threats to validity.** *Internal:* concurrent sessions could read one another's artifacts, so refutations are not blind; mitigated by primary-source grounding and control systems ($3n{-}1$) whose ground truth is independent of any session. *Construct:* "policy A/B clusters" are inferred from artifacts, not from instrumented session logs; model-to-artifact attribution is partly operator-attested. *External:* one problem, one day, one operator — EDAP generalization requires replication on other open problems and operator populations. *Selection:* the surviving lemma was also the most-reviewed artifact; survivorship under review is the intended measurement, but readers should not infer base rates from one episode. Additionally, the 10/10 audit confirmation rate covers the *first ten claims in ledger order* (core dossier facts, the best-sourced stratum) — it is not a random sample of the 189 and must not be extrapolated to the unaudited remainder.

**Invitation to adversarial review.** The authorial position is that this paper's value is proportional to the hostility of the review it survives. Specialists are invited to attack it via: the falsification routes above; post-publication commentary (e.g., PubPeer) on any claim; the Collatz Conjecture Challenge community (ccchallenge.org) for machine-checked adjudication of §3–§4; and direct correspondence to the author. Refutations will be recorded in the repository's audit register alongside the claims they refute, per the standing protocol of §7.

## 10. Conclusion

Eight hours of maximal-permission pressure produced no movement on the Collatz Conjecture and a documented illustration of why: mathematical output is gated by verification, not ambition. Sessions of the same model families produced both a source-verified dossier and a corpus of persuasive but invalid proof documents; every invalid document failed in one of four nameable ways, in most cases under checks built by the ecosystem itself during the episode. The conjecture stands open — $n<2^{71}$ verified [1], cycle floor $1.375\times10^{11}$ odd terms [1,2], and a candidate 2-adic-digits reformulation of the divergence obstruction stated as a research target (§4). The contribution offered for scrutiny is a working, transferable protocol for separating verified mathematics from unverified proof-like output inside one repository in real time — together with the public artifact trail demonstrating both the successes and the failures.

---

### References

[1] D. Bařina, *Improved verification limit for the convergence of the Collatz conjecture*, J. Supercomput. **81**:810 (2025). DOI 10.1007/s11227-025-07337-0. Project page: pcbarina.fit.vutbr.cz.
[2] C. Hercher, *There are no Collatz m-cycles with m ≤ 91*, J. Integer Seq. **26** (2023), art. 23.3.5; arXiv:2201.00406.
[3] J. L. Simons, B. M. M. de Weger, *Theoretical and computational bounds for m-cycles of the 3n+1-problem*, Acta Arith. **117** (2005) 51–70. DOI 10.4064/aa117-1-3.
[4] T. Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum Math. Pi (2022); arXiv:1909.03562.
[5] I. Krasikov, J. C. Lagarias, *Bounds for the 3x+1 problem using difference inequalities*, Acta Arith. **109** (2003) 237–258; arXiv:math/0205002.
[6] S. Eliahou, *The 3x+1 problem: new lower bounds on nontrivial cycle lengths*, Discrete Math. **118** (1993) 45–56. DOI 10.1016/0012-365X(93)90052-U.
[7] R. Terras, *A stopping time problem on the positive integers*, Acta Arith. **30** (1976) 241–252; addendum Acta Arith. **35** (1979) 101–102.
[8] C. J. Everett, *Iteration of the number-theoretic function f(2n)=n, f(2n+1)=3n+2*, Adv. Math. **25** (1977) 42–45. DOI 10.1016/0001-8708(77)90087-1.
[9] S. A. Kurtz, J. Simon, *The undecidability of the generalized Collatz problem*, TAMC 2007, LNCS **4484**, 542–553. DOI 10.1007/978-3-540-72504-6_49.
[10] D. J. Bernstein, J. C. Lagarias, *The 3x+1 conjugacy map*, Canad. J. Math. **48** (1996) 1154–1169.
[11] J. C. Lagarias, *The set of rational cycles for the 3x+1 problem*, Acta Arith. **56** (1990) 33–53; and *The 3x+1 problem and its generalizations*, Amer. Math. Monthly **92** (1985) 3–23. DOI 10.2307/2322189.
[12] T. Oliveira e Silva, *Maximum excursion and stopping time record-holders for the 3x+1 problem*, Math. Comp. **68** (1999) 371–384. DOI 10.1090/S0025-5718-99-01031-5.
[13] K. Mahler, *An unsolved problem on the powers of 3/2*, J. Austral. Math. Soc. **8** (1968) 313–321.
[14] J. C. Lagarias, A. Weiss, *The 3x+1 problem: two stochastic models*, Ann. Appl. Prob. **2** (1992) 229–261.
[15] J. H. Conway, *Unpredictable iterations*, Proc. 1972 Number Theory Conf., Boulder, 49–52.
[16] J. C. Lagarias (ed.), *The Ultimate Challenge: The 3x+1 Problem*, AMS (2010).
[17] *BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs*, arXiv:2510.04721 (2025). (Cited by title and identifier; author list not independently confirmed at citation time.)
[18] *The Adversarial Prover: A Skeptic's Approach to LLM-Assisted Mathematics*, research note (2026-01-02), tjoresearchnotes.wordpress.com. (Pseudonymous, non-archival blog source; cited as background evidence that designed prover–verifier configurations predate this work, and for no other claim. If it becomes unreachable, the priority claim of §8a is unaffected — the P1–P6 conjunction does not rely on it.)
[19] *SciIntBench: Measuring LLM Compliance with Research Integrity Norms Under Adversarial Framing*, arXiv:2605.29468 (2026). (Cited by title and identifier; author list not independently confirmed at citation time.)
[20] T. Tao, *Mathematical exploration and discovery at scale*, terrytao.wordpress.com (2025-11-05).
[21] Google DeepMind, *AI achieves silver-medal standard solving International Mathematical Olympiad problems* (AlphaProof/AlphaGeometry announcement, 2024), deepmind.google (primary); secondary news coverage of AlphaProof Nexus (2026) cited as context only.
[22] E. Y. Chang, *Exploring Collatz Dynamics with Human-LLM Collaboration*, arXiv:2603.11066 (2026).

### Data availability and reproducibility manifest

All paths are relative to the repository root; instrument paths are under `problems/collatz-conjecture/experiments/`. Each empirical claim maps to a committed script:

| Claim | Script / artifact | Command |
|---|---|---|
| Frontier density $S(d)/2^d$, Fig. 1, Thm 5.1 numerics | `collatz_survivor_dp.py`; `docs/figures/make_figures.py` (recomputes DP at build) | `python collatz_survivor_dp.py --max-depth 128` |
| Stopping-time / odd-fraction / descent-law / $\gamma$-record table, Fig. 2 data | `stochastic_model_check.py` | `python stochastic_model_check.py --limit 5000000 --depth 28` |
| Cycle floor (Thm 5.2) incl. CF convergents | `cycle_bound_lab.py` | `python cycle_bound_lab.py` (and `--log2-nmin 68` for the comparison row) |
| Frontier-escape record (217,740,015 → depth 395) | `frontier_escape_analyzer.py` | `--base-depth 28 --max-escape-depth 1024` |
| Spine-ladder exhaustive checks | `spine_ladder_lab.py` | default run; results JSON committed |
| Failure catalogue corpus + refutations | `unverified-claims/` (12 documents + README), `AUDIT-REGISTER.md` | read; kick-audit rerun via `kick_repulsion_claim_audit.py` |
| Audit ledger (189 claims; 10 verdicts) | `AUDIT-REGISTER.md`; workflow resumable per its header | — |

*Additional artifacts:* `SPINE-LADDER.md` (full Lemma 4.1 proof), `CERTIFICATE-FRONTIER-THEOREMS.md`, `CYCLE-BOUND-LAB.md`, `STOCHASTIC-MODEL-CHECK.md`. All instruments are dependency-free Python (stdlib only) and deterministic.

### Acknowledgments & attribution

Human authorship, curation, accreditation, and all publication decisions: **Alexander Donahue** ([@0thernes_ai](https://x.com/0thernes_ai)). AI systems served as instruments and drafting/verification collaborators under the operator's direction (`AUTHORS.md`; CC BY 4.0; cite per `CITATION.cff`).
