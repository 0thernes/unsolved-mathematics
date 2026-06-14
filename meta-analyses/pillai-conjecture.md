---
title: "Meta-Analysis: Pillai's Conjecture"
slug: pillai-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful and well-structured survey of an open problem whose unconditional core remains untouched; references carry verification flags and require primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: Pillai's Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

Pillai's conjecture asserts that for every fixed integer $k \ge 1$, the equation $x^p - y^q = k$ has only finitely many solutions in positive integers with $p, q \ge 2$; equivalently, the gaps between consecutive perfect powers tend to infinity. Posed by S. S. Pillai in the 1930s as a generalization of Catalan's 1844 conjecture (the $k = 1$ case), it sits at the intersection of transcendence theory, Diophantine geometry, and the $abc$ conjecture. This meta-analysis surveys what is and is not known. Unconditionally, finiteness is established whenever both exponents are fixed (Baker's method, refined by Tijdeman, Mignotte, Bennett, Bugeaud), and the $k = 1$ case is completely settled by Mihăilescu's 2002 cyclotomic proof. The $abc$ conjecture implies Pillai in full, but $abc$ itself is open. The genuinely unresolved content — bounding the variable exponents $p, q$ for any single $k \ge 2$ — remains untouched by every unconditional method. We assess the principal approaches, the structural barrier common to all of them, and what a resolution would require. The conjecture has stood open for over ninety years.

## 1. Statement and significance

Order the perfect powers $1 < 4 < 8 < 9 < 16 < 25 < 27 < \dots$ as $a_1 < a_2 < \dots$. Pillai's conjecture is the assertion that $a_{n+1} - a_n \to \infty$; equivalently, that for each fixed $k \ge 1$ the equation $x^p - y^q = k$ (with $x, y > 0$ and $p, q \ge 2$) has only finitely many solutions. The case $k = 1$ is exactly Catalan's conjecture, so Pillai is a strict generalization. The significance is twofold. First, it is a clean quantitative statement about the multiplicative thinness of perfect powers, a recurring theme in Diophantine number theory. Second, it is a canonical consequence of the $abc$ conjecture, placing it within the dense web of $abc$-adjacent problems (Hall's conjecture, Beal's conjecture, Schinzel's Hypothesis H). Its difficulty is rated high (80/100 in the dossier) with low tractability (20/100), reflecting that the unconditional core appears to require either $abc$ or a genuinely new idea.

## 2. State of the art

The status is **open**. The known results partition cleanly:

- **Fixed exponents (unconditional).** For any fixed pair $p, q \ge 2$, $|x^p - y^q| = k$ has finitely many solutions, effectively computable via Baker's theory of linear forms in logarithms. Bennett showed that for fixed $p, q$ the count is typically at most two, with the full solution set determinable.
- **The case $k = 1$ (Catalan, unconditional).** Completely solved: $3^2 - 2^3 = 1$ is the only nontrivial solution, for all exponents. Tijdeman (1976) gave effective finiteness; Mihăilescu (2004) achieved complete resolution via cyclotomic field theory.
- **Individual equations (unconditional).** Modular (Frey-curve) methods have resolved numerous specific $x^p \pm y^q = k$ and Lebesgue–Nagell equations $x^2 + D = y^n$ for fixed signatures.
- **Recurrence-sequence variants (unconditional).** "Pillai's problem" for Fibonacci, Tribonacci, and other linear recurrences is solved in many concrete families by the Luca school.
- **Under $abc$ (conditional).** The $abc$ conjecture implies Pillai in full, for all $k$ simultaneously, with an effective bound.

No unconditional proof exists that $x^p - y^q = k$ has finitely many solutions with variable exponents for any single $k \ge 2$.

## 3. Principal approaches and barriers

**Linear forms in logarithms (Baker's method).** A solution forces $x^p$ and $y^q$ to be multiplicatively close, so $|p \log x - q \log y|$ is tiny; Baker's lower bounds, combined with the equation's upper bound, give effective control of $x, y$ once $p, q$ are bounded. *Barrier:* the dependence on the exponents is too weak to cap them; the method does not bound $p, q$ for general $k$.

**Cyclotomic methods (Mihăilescu).** For $k = 1$, Mihăilescu replaced transcendence with the arithmetic of cyclotomic fields — Wieferich-type congruences, Stickelberger's theorem, group-ring annihilators — converting Catalan from "effectively bounded" to "completely solved." *Barrier:* the machinery is exquisitely adapted to the difference being exactly $1$, which forces the divisibility relations; for $k \ge 2$ the analogous congruences are far weaker, and no extension to even a single $k > 1$ exists.

**The $abc$ conjecture (conditional).** Applying $abc$ to $y^q + k = x^p$ bounds $\max(x^p, y^q)$ by the radical, which is tiny for perfect powers, forcing $p, q, x, y$ all bounded for each $k$. *Barrier:* $abc$ is itself open; Mochizuki's IUT claim is not accepted following the 2018 Scholze–Stix objections.

**Modular / Frey-curve methods.** Attach a Frey–Hellegouarch object and derive a contradiction via level-lowering, as in Fermat's Last Theorem. *Barrier:* works one signature at a time, depending on case-specific modularity inputs; no uniform statement across all exponents.

The common obstruction is stark: every unconditional method controls the problem once the exponents are bounded. The open content is precisely the bounding of $p, q$ for $k \ge 2$, and the only known route — $abc$ — is unproven.

## 4. Critical assessment

The dossier's framing is, in my assessment, accurate and refreshingly honest: Pillai's conjecture is not a graveyard of failed proofs but a steady accumulation of partial results that stop at one wall. The most important structural observation — that "fixed exponents" is tractable and "variable exponents" is the entire difficulty — is correct and is the right organizing principle. The reduction $abc \Rightarrow$ Pillai is genuine and well-attested in the literature (Waldschmidt's surveys, among others), though it should be emphasized that this is a *reduction*, not a proof, and that it inherits all of $abc$'s difficulty.

Two points merit caution. First, the claim that Mihăilescu's method "has resisted generalization to $k \ge 2$" is correct as of the dossier, but a human reviewer should confirm no recent partial extension has appeared. Second, the dossier's quantitative claims about Bennett's solution counts ("at most two") are stated at a level of generality that, while broadly faithful, depends on coprimality and signature hypotheses that the prose elides; a referee should check the precise statement against Bennett's papers before quoting it as unconditional.

## 5. What a resolution would require / open directions

A full proof requires an unconditional bound on the **exponents** $p, q$ in terms of $k$ for $k \ge 2$. Concretely, one of:

1. a proof of the $abc$ conjecture (or a weaker effective consequence sufficient to bound exponents) — structurally the most promising lever, with Stewart–Yu-type linear-forms bounds the most-watched partial progress;
2. an extension of Mihăilescu's cyclotomic framework to differences $k \ge 2$ — currently blocked by the special role of the difference being exactly $1$;
3. a uniform modular/Galois-representation argument across all exponent signatures for a fixed $k$ — beyond the current case-by-case reach.

The modular method and the recurrence-sequence program continue to extend the catalog of solved special cases, but neither currently threatens the variable-exponent core for any $k \ge 2$.

## 6. Selected references

1. A. Baker, *Linear forms in the logarithms of algebraic numbers I* (1966), *Mathematika*. [high-confidence]
2. R. Tijdeman, *On the equation of Catalan* (1976), *Acta Arithmetica*. [high-confidence]
3. T. N. Shorey, R. Tijdeman, *Exponential Diophantine Equations* (1986), Cambridge monograph. [high-confidence]
4. P. Mihăilescu, *Primary cyclotomic units and a proof of Catalan's conjecture* (2004), *J. reine angew. Math.* **572**, 167–195. [high-confidence]
5. P. Ribenboim, *Catalan's Conjecture: Are 8 and 9 the only consecutive powers?* (2004). [high-confidence]
6. R. Schoof, *Catalan's Conjecture* (2006), book. [high-confidence]
7. Y. Bugeaud, M. Mignotte, S. Siksek, *Classical and modular approaches to exponential Diophantine equations I: Fibonacci and Lucas perfect powers* (2006), *Annals of Mathematics*. [high-confidence]
8. S. S. Pillai, *On some Diophantine equations* (1931), foundational. [needs-verification]
9. S. S. Pillai, *On $a^x - b^y = c$* (1945), foundational. [needs-verification]
10. M. A. Bennett, *On some exponential equations of S. S. Pillai* (2001), modern. [needs-verification]
11. M. Mignotte, *The Catalan equation* (1990), survey. [needs-verification]
12. M. Waldschmidt, *Perfect powers: Pillai's works and their developments* (2008), survey. [needs-verification]
13. M. Waldschmidt, *Open Diophantine problems* (2008), survey. [needs-verification]
14. M. Ddamulira, F. Luca, M. Rakotomalala, *On a conjecture of Pillai (with linear recurrences)* (2017), modern. [needs-verification]
15. A. Bérczes, K. Győry et al. (lineage), *Solving Pillai's equation $X^n - Y^m = c$ via the modular/Baker method* (2018), computational. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is structurally sound and, importantly, honest about the boundary between what is proven and what is conjectured. Its central thesis — that the difficulty of Pillai is entirely concentrated in bounding the exponents for $k \ge 2$, while everything "downstream" of fixed exponents is tractable — is the correct and standard framing, and the document resists the common temptation to let the $abc \Rightarrow$ Pillai reduction masquerade as more than a reduction. The treatment of Mihăilescu's cyclotomic proof, and of why it does not generalize, is accurate to the literature I can recall.

Three skeptical flags. (i) The reference list is mixed-confidence: items 8–15 carry **needs-verification** flags, and the dossier itself notes that Pillai's original titles and years are "reconstructed from memory." These must be checked against primary sources — the *Collected Works of S. S. Pillai* (ed. Balasubramanian, Thangadurai) and the original journal runs — before any citation is quoted. Even the high-confidence items have had DOIs deliberately suppressed and should be matched to canonical bibliographic records. (ii) There is mild single-source reliance on Waldschmidt's surveys for the $abc \Rightarrow$ Pillai reduction and its framing; while this reduction is genuinely folklore-to-textbook, a reviewer should confirm the precise hypotheses (it is the radical bound, not merely $abc$ "in spirit," that does the work). (iii) The quantitative claim that fixed-exponent equations have "at most two" solutions is stated more cleanly than Bennett's actual theorems, which carry coprimality and signature conditions; this is the single most important thing a human reviewer should verify before the claim is repeated as unconditional.

None of these undermine the assessment's core, which makes no claim of a new result and correctly reports the problem as open for every $k \ge 2$ in the variable-exponent regime.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This document is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citations — especially those flagged needs-verification — require checking against primary sources before being relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
