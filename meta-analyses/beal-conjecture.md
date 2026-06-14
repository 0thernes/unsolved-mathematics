---
title: "Meta-Analysis: The Beal Conjecture"
slug: beal-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "An accurate, appropriately hedged survey of the coprime generalized-Fermat problem whose references carry verification flags and require primary-source checking before citation."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Beal Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Beal Conjecture asserts that the Diophantine equation $A^x + B^y = C^z$ with exponents $x,y,z>2$ and positive integers $A,B,C$ admits no solution with $A,B,C$ pairwise coprime — equivalently, any solution forces a common prime factor. Posed around 1993 by the banker and amateur number theorist Andrew Beal and publicized by R. Daniel Mauldin in 1997, it generalizes Fermat's Last Theorem, which is recovered at the diagonal $x=y=z=n\ge3$. The problem sits in the hyperbolic regime of the generalized Fermat equation, where the inverse-exponent sum $\chi=\tfrac1p+\tfrac1q+\tfrac1r<1$. This meta-analysis surveys the state of the art: Fermat's Last Theorem (Wiles 1995) closes the diagonal; Darmon–Granville (1995) gives ineffective finiteness per signature via Faltings; and the modular method plus descent/Chabauty have resolved a large but finite catalogue of individual signatures. Conditionally, the $abc$ conjecture would settle Beal up to finitely many exceptions, but $abc$ is itself open and Mochizuki's claimed proof is disputed. The governing obstruction is uniformity across infinitely many exponent triples. The conjecture remains open, backed by a $1{,}000{,}000 AMS-administered prize.

## 1. Statement and significance

The conjecture concerns $A^x+B^y=C^z$ with $A,B,C\in\mathbb{Z}^{+}$ and $x,y,z>2$. It claims that any such solution has $\gcd(A,B,C)>1$. The canonical illustrative solution is $3^3+6^3=3^5$ (i.e. $27+216=243$), in which $3$ divides every base — consistent with, not a counterexample to, the conjecture. Setting $x=y=z=n\ge3$ recovers the Fermat equation; thus Beal implies Fermat's Last Theorem (FLT) for exponents $\ge3$ as the equal-exponent, coprime special case, while the converse fails because unequal exponents demand more than the modularity of a single elliptic curve.

The significance is twofold. First, Beal is a clean, falsifiable generalization of the most celebrated equation in number theory, embedding FLT in the broader family of generalized Fermat equations $A^p+B^q=C^r$ organized by $\chi=\tfrac1p+\tfrac1q+\tfrac1r$. The condition $x,y,z>2$ forces $\chi\le1$, with equality only at $(3,3,3)$, so the problem lives entirely in the hyperbolic regime plus that single Euclidean triple. Second, the seven-figure Beal Prize, held in trust and adjudicated by the American Mathematical Society, has given the problem unusual public visibility and a steady inflow of amateur submissions, none surviving refereeing.

## 2. State of the art

**Unconditional results.** The diagonal is closed: coprime solutions of $A^n+B^n=C^n$ for $n\ge3$ are impossible by FLT (Wiles, with Taylor, 1995). For every fixed signature $(p,q,r)$ with $\chi<1$ — all Beal signatures except $(3,3,3)$ — Darmon–Granville (1995) prove finitely many coprime solutions, via Faltings' theorem applied to an associated curve of genus $\ge2$. A large catalogue of individual signatures has been completely resolved: the families $(n,n,2)$ and $(n,n,3)$ (Darmon–Merel 1997), numerous mixed cases by Bennett, Skinner, Kraus and collaborators, and hard individual triples such as $(2,3,7)$, $(2,3,8)$, and $(2,3,9)$ by Poonen–Schaefer–Stoll, Bruin, Siksek, Chen, Dahmen, Freitas and others using descent and Chabauty–Coleman. Within the strict range $x,y,z>2$ these confirm Beal for infinitely many — but not all — exponent configurations.

**Conditional results.** Under the $abc$ conjecture of Masser and Oesterlé, Beal holds for all but finitely many solutions; a sufficiently effective form of $abc$ would settle it entirely, since a coprime solution with large exponents would carry implausibly smooth (high-power) terms violating the radical bound $c\ll_\varepsilon\operatorname{rad}(abc)^{1+\varepsilon}$. The $abc$ conjecture remains open by mainstream consensus.

**Computation.** Independent searches (Norvig and others) have found no coprime counterexample within wide ranges of bases and exponents.

## 3. Principal approaches and barriers

**The modular method** — Frey–Hellegouarch curves, Ribet level-lowering, and modularity — is the dominant tool, descended directly from the FLT proof. Its barrier is structural: it operates essentially one signature at a time, each new triple requiring its own Frey curve and modularity input (often over number fields, where modularity is harder), with no uniform construction covering all hyperbolic $(p,q,r)$.

**Faltings finiteness (Darmon–Granville)** gives unconditional finiteness for each fixed signature, but Faltings is ineffective — it bounds the number of solutions without a computable height bound — and is non-uniform across the infinitely many triples.

**The $abc$ route** is the most powerful conditional path, but $abc$ is open; Mochizuki's inter-universal Teichmüller proof (published in *PRIMS*, 2021) is not accepted, with the Scholze–Stix objection (2018) targeting a key inequality around "Corollary 3.12" unresolved by community consensus.

**Descent and Chabauty–Coleman** provably resolve individual small-genus signatures but require the Jacobian (or a quotient) to have rank below its dimension and substantial case-specific computation; they do not scale with growing exponent.

The recurring obstruction across all four is **uniformity**: every effective technique is anchored to a fixed signature while Beal ranges over infinitely many.

## 4. Critical assessment

The dossier's central claim — that Beal is confirmed on infinitely many but not all signatures, conditionally near-settled under $abc$, and possessed of no accepted general proof or counterexample — is the honest and defensible position. The framing through $\chi$ and the hyperbolic regime is mathematically correct and is the standard organizing principle in the generalized-Fermat literature. The relationship to FLT is stated precisely, including the non-trivial point that FLT does not imply Beal.

Two cautions are worth emphasizing. First, several signatures repeatedly cited as Beal "near-misses" — notably $(2,3,7)$, $(2,3,8)$, $(2,4,5)$ — involve an exponent equal to 2 and therefore lie *outside* the strict Beal hypothesis $x,y,z>2$; the dossier flags this, but a casual reader could over-credit them as direct Beal progress. They bound the surrounding Fermat–Catalan landscape rather than the Beal range proper. Second, the strongest genuinely-within-range families are the equal-exponent diagonal (FLT) and signatures of shape $(n,n,k)$; the conjecture's hard core — genuinely distinct large exponents — remains essentially untouched by current methods.

The skeptical conclusion that a short elementary proof is unlikely is well-grounded: such a proof would yield an unexpectedly elementary route to FLT, against strong prior evidence.

## 5. What a resolution would require / open directions

A full proof needs uniformity across infinitely many exponent triples. The dossier identifies three plausible routes: (1) an unconditional, effective $abc$ (or a Beal-tailored Diophantine inequality) strong enough to bound the smooth terms; (2) a uniform Frey-curve / modularity construction covering all hyperbolic signatures simultaneously rather than case by case; or (3) a genuinely new structural idea linking the coprimality hypothesis to a global obstruction. The most plausible near-term progress is incremental — extending the modular method over number fields (asymptotic-Fermat techniques of Freitas, Siksek and others) to absorb ever-larger families of signatures — while a clean general theorem awaits progress on $abc$ or a new method. A counterexample, though not excluded, is regarded as unlikely given the computational evidence and the $abc$-conditional argument.

## 6. Selected references

1. Andrew Wiles, *Modular elliptic curves and Fermat's Last Theorem* (1995), DOI 10.2307/2118559. [high-confidence]
2. Richard Taylor, Andrew Wiles, *Ring-theoretic properties of certain Hecke algebras* (1995), DOI 10.2307/2118560. [high-confidence]
3. Henri Darmon, Andrew Granville, *On the equations $z^m=F(x,y)$ and $Ax^p+By^q=Cz^r$* (1995), DOI 10.1112/blms/27.6.513. [high-confidence]
4. R. Daniel Mauldin, *A generalization of Fermat's Last Theorem: the Beal conjecture and prize problem*, *Notices of the AMS* (1997). [high-confidence]
5. Henri Darmon, Loïc Merel, *Winding quotients and some variants of Fermat's Last Theorem* (1997), DOI 10.1515/crll.1997.490.81. [high-confidence]
6. C. Breuil, B. Conrad, F. Diamond, R. Taylor, *On the modularity of elliptic curves over $\mathbb{Q}$* (2001), DOI 10.1090/S0894-0347-01-00370-8. [high-confidence]
7. Michael A. Bennett, Chris M. Skinner, *Ternary Diophantine equations via Galois representations and modular forms* (2004), DOI 10.4153/CJM-2004-002-2. [needs-verification]
8. Frits Beukers, *Equations of the form $x^p+y^q=z^r$* (survey of the generalized Fermat equation) (2004). [needs-verification]
9. Bjorn Poonen, Edward Schaefer, Michael Stoll, *The equation $x^2+y^3=z^7$* (2006), DOI 10.1215/S0012-7094-07-13714-1. [needs-verification]
10. Preda Mihăilescu, *Catalan's Conjecture: proof of $x^p-y^q=1$* (2004). [high-confidence]
11. Nuno Freitas, Bartosz Naskręcki, Michael Stoll, *The generalized Fermat equation with exponents 2, 3, n* (2015). [needs-verification]
12. Nuno Freitas, Samir Siksek, *The asymptotic Fermat conjecture and the modular method over number fields* (2016). [needs-verification]
13. Michael A. Bennett, Imin Chen, Sander Dahmen, Soroosh Yazdani, *Generalized Fermat equations: a miscellany* (2019). [needs-verification]
14. Peter Norvig, *Beal's conjecture: a search for counterexamples* (computational note) (2013). [needs-verification]
15. Shinichi Mochizuki, *Inter-universal Teichmüller theory IV* (claimed proof of $abc$; disputed) (2021), DOI 10.4171/PRIMS/57-1-2. [needs-verification]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is technically sound and commendably honest. It correctly situates Beal as the coprime, $x,y,z>2$ slice of the generalized Fermat equation, organizes the landscape through the inverse-exponent sum $\chi$, and distinguishes unconditional results (FLT for the diagonal, ineffective per-signature finiteness via Darmon–Granville/Faltings, resolved individual signatures) from the $abc$-conditional path. The identification of uniformity across infinitely many exponent triples as the governing obstruction is the right diagnosis and matches the mainstream view. The handling of the Mochizuki dispute is appropriately neutral.

I flag three concerns for a human reviewer. (i) Every reference here carries a verification flag inherited from the dossier; rows 7–9 and 11–15 are marked "needs-verification," and exact titles, years, and DOIs for the modular-method and generalized-Fermat case studies vary between arXiv and journal versions. These must be checked against primary sources (MathSciNet/zbMATH/DOI resolution) before citation — do not treat them as established. (ii) There is potential for overstatement around the resolved signatures: several of the most-cited ones (e.g. $(2,3,7)$, $(2,3,8)$, $(2,4,5)$) contain an exponent equal to 2 and so lie strictly outside the Beal hypothesis; I have foregrounded this, but a reader could still over-credit them as direct Beal progress. (iii) The claim that "within the strict Beal range these confirm the conjecture for infinitely many exponent configurations" leans on the $(n,n,2)$/$(n,n,3)$ and diagonal families — note $(n,n,2)$ itself sits at the boundary; the precise inventory of fully-resolved within-range families is the single most important thing a human should verify against the survey literature (Bennett–Chen–Dahmen–Yazdani and Beukers).

No claim in this document asserts a proof, counterexample, or resolution of Beal; it remains open. Subject to the source-checking above, the analysis is fit to publish as a survey.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This assessment is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and all flagged references require primary-source checking before they are relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
