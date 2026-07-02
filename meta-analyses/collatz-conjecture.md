---
title: "Meta-Analysis: The Collatz Conjecture"
slug: collatz-conjecture
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: open
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-organized survey of an open problem whose every reference flag and single-source claim must be checked against primary literature before publication."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Collatz Conjecture

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Collatz conjecture asserts that iterating the map $T(n)=n/2$ for even $n$ and $T(n)=3n+1$ for odd $n$ eventually reaches $1$ for every positive integer. Recorded by Lothar Collatz around 1937 and spread orally under many names (Syracuse, Ulam, Kakutani, Hasse, Thwaites), it remains **open**: verified computationally to $n < 2^{71} \approx 2.36\times10^{21}$ but proven for no infinite family. The conjecture splits into two logically independent claims — no nontrivial cycle and no divergent orbit — and most progress is probabilistic. The unconditional high-water mark is Tao's 2019 theorem that almost all orbits (in logarithmic density) attain almost bounded values; cycle-exclusion combines transcendence theory with computation but only bounds cycle complexity. This meta-analysis synthesizes the problem's history, the state of the art, the principal approaches and their structural barriers, and what a resolution would require. It is a survey, not a proof, and its references carry verification flags requiring human confirmation against primary sources. (~155 words)

## 1. Statement and significance

Define $T:\mathbb{Z}^{+}\to\mathbb{Z}^{+}$ by $T(n)=n/2$ for even $n$ and $T(n)=3n+1$ for odd $n$. Collatz's conjecture is that the orbit of every positive integer eventually reaches $1$ (entering the cycle $1\to4\to2\to1$). Because $3n+1$ is always even, many authors use the accelerated **Syracuse map** $(3n+1)/2$ on odds, which simplifies the dynamics without altering the conjecture. The problem is significant less for its consequences than for what its intractability reveals: a map of utterly elementary definition whose long-term behavior resists ergodic theory, $p$-adic analysis, transcendence theory, and additive combinatorics alike. It has become a benchmark for the limits of our understanding of deterministic iteration, and a cautionary case for the gap between heuristic plausibility and rigorous proof. Erdős's verdict — "mathematics is not yet ready for such problems" — remains the field's honest summary.

## 2. State of the art

**Status: open.** No proof or disproof exists; no counterexample (divergent orbit or nontrivial cycle) has ever been found. Computational verification reaches $n < 2^{71}$ (Bařina, *J. Supercomput.* **81**, 810 (2025), extending his 2020 verification to $2^{68}$ and Oliveira e Silva's earlier distributed project).

The conjecture decomposes into two independent statements: **(a)** no orbit diverges to infinity, and **(b)** no nontrivial cycle exists. The unconditional results address these unevenly.

On the divergence side, the foundational results are **density** theorems: Terras (1976) and Everett (1977) independently showed that natural density $1$ of integers have a finite stopping time (the first time the orbit drops below its start). Krasikov–Lagarias (2003) gave the unconditional counting bound $\#\{n\le x : n\to 1\}\gg x^{0.84}$. The landmark is **Tao (2019)**: for any $f(n)\to\infty$, almost all $n$ in logarithmic density satisfy $\min_k T^k(n)<f(n)$ — "almost all orbits attain almost bounded values." This remains the strongest unconditional result.

On the cycle side, results are **conditional on bounded complexity**: Steiner (1977) excluded $1$-cycles, Simons–de Weger (2005) excluded $m$-cycles for small $m$, and Hercher (2023) extended the exclusion to all $m \le 91$, each via Baker-type bounds on linear forms in logarithms controlling $|2^\ell-3^k|$. Combined with verification to $2^{71}$ — which exceeds Hercher's stated threshold of $3\cdot 2^{69}$ — any nontrivial cycle must contain at least $1.375\times 10^{11}$ odd terms, superseding the older Eliahou-style hundreds-of-millions floor.

The **heuristic** (conditional) picture is uniform and compelling: each odd step multiplies by roughly $3/4$ on average, giving negative multiplicative drift and hence almost-sure descent. This predicts the conjecture is true — but it is a model of typical, not specific, integers, and it is not a proof.

## 3. Principal approaches and barriers

**Density / "almost all" methods.** Study the stopping time and show the failing set has density zero; induction would then finish *if* "almost all" could be promoted to "all." *Barrier:* density-$1$ control says nothing about the thin exceptional set, where a divergent orbit could hide. Tao himself notes his method does not reach every orbit.

**Cycle exclusion (the periodicity problem).** A nontrivial cycle forces a tight Diophantine relation making $2^\ell-3^k$ small; continued-fraction approximation to $\log_2 3$ and transcendence theory constrain this. *Barrier:* bounds grow only with the verified range and transcendence constants — a finite computation plus a finite bound never excludes cycles of *all* lengths.

**Ergodic theory and the 2-adic model.** Extend $T$ to $\mathbb{Z}_2$; the parity sequence yields a measure-preserving conjugacy to the shift (Hedlund; Lagarias; Matthews–Watts), explaining why descent should hold on average. *Barrier:* the integers are a measure-zero, dynamically distinguished subset, so $\mathbb{Z}_2$-ergodicity cannot certify any single integer's fate.

**Undecidability of generalized maps.** Conway showed generalized $3n+1$ functions can simulate computation; Kurtz–Simon (2007) made the undecidability precise. *Barrier (and warning):* this is a negative result about the *family* — it implies any technique general enough to handle all such maps must fail, so a proof of the specific case must exploit the particular arithmetic of $3$ and $2$. It does **not** make the original conjecture itself undecidable.

**Tree-based and additive-combinatorics methods.** Count preimages of $1$ (the Collatz tree) and analyze the "Syracuse random variable" Tao exploits. *Barrier:* a "parity"-type obstruction — mixing the primes $2$ and $3$ so no single sieve or character sum sees both, leaving methods blind to structured exceptional orbits.

## 4. Critical assessment

What is **solid**: the pillars are genuine theorems — Terras/Everett density-$1$ descent, Krasikov–Lagarias's $x^{0.84}$ bound, Tao's 2019 almost-bounded-values theorem, Hercher's 2023 exclusion of $m$-cycles with $m \le 91$, and Bařina's verification to $2^{71}$ (2025). These are correctly characterized in the dossier as *unconditional but partial*: each controls typical or bounded-complexity behavior, none reaches every integer or every cycle length.

What is **speculative or merely heuristic**: the probabilistic $3/4$-drift model. It is intellectually persuasive and predicts both halves of the conjecture, but it is a statement about measure-typical orbits, and the dossier is appropriately careful to label it a model rather than evidence of imminent resolution.

How far is the frontier? **Very far.** The honest reading is that the gap between Tao's theorem and the conjecture is not incremental: upgrading logarithmic density to full density, and "almost bounded" to "bounded," appears to require qualitatively new input, and the cycle problem is essentially untouched in its full generality. The undecidability backdrop sharpens the pessimism: it actively warns against expecting a general-purpose proof. The pattern of failed attempts (silently treating "almost all" as "all," bounding only finite cycle lengths, hidden circularity, heuristics dressed as rigor) is consistent and well-diagnosed. Nothing in the dossier suggests the problem is close to falling.

## 5. What a resolution would require / open directions

A complete proof must close **both** independent gaps at once:

1. **No divergent orbit** — upgrade Tao's logarithmic-density, almost-bounded statement to an every-integer, genuinely-bounded one, controlling the thin exceptional set that density methods discard.
2. **No nontrivial cycle** — exclude cycles of *all* lengths, not merely bounded complexity, plausibly via a new Diophantine input controlling $2^\ell-3^k$ uniformly.

A disproof would require exhibiting a cycle or a provably divergent orbit; both are ruled out below $2^{71}$, so any counterexample is astronomically large or structurally subtle.

Plausible routes flagged in the dossier: strengthening the entropy/additive-combinatorics machinery behind Tao's theorem to full density and true boundedness; finding a conserved or monotone invariant distinguishing integer orbits from measure-typical ones (the missing structural object); sharper transcendence theory on $\log_2 3$; or ergodic/$2$-adic rigidity transferring measure-theoretic typicality to the measure-zero integers. All four are open; none is near.

## 6. Selected references

1. Riho Terras, *The $3x+1$ problem and its generalizations* (stopping-time density), 1976. [high-confidence]
2. C. J. Everett, *The coefficients in the $3x+1$ problem* (almost-all stopping time), 1977. [high-confidence]
3. Ray P. Steiner, *On the "$3x+1$" problem* (exclusion of 1-cycles), 1977. [needs-verification]
4. Jeffrey C. Lagarias, *The $3x+1$ problem and its generalizations*, 1985, DOI:10.2307/2322189. [high-confidence]
5. Ilia Krasikov, *Bounds on the $3x+1$ counting function*, 1989. [needs-verification]
6. Tomás Oliveira e Silva, *Verification of the $3x+1$ conjecture* (large-scale computation), 1998. [needs-verification]
7. Ilia Krasikov & Jeffrey C. Lagarias, *Bounds for the $3x+1$ problem using difference inequalities* ($x^{0.84}$), 2003. [high-confidence]
8. Jeffrey C. Lagarias, *The $3x+1$ problem: an annotated bibliography (1963–1999)*, arXiv:math/0309224. [high-confidence]
9. Simons & de Weger, *m-cycle exclusion for the $3x+1$ problem*, 2005. [needs-verification]
10. Stuart Kurtz & Janos Simon, *The undecidability of the generalized Collatz problem*, 2007. [needs-verification]
11. Jeffrey C. Lagarias (ed.), *The Ultimate Challenge: The $3x+1$ Problem* (edited volume), 2010. [high-confidence]
12. Shalom Eliahou (and successors), *Lower bounds for cycle lengths in the $3x+1$ problem*, 2011. [needs-verification]
13. Gerhard Opfer, *An analytic approach to the Collatz $3n+1$ problem* (disputed; circular argument), 2011. [needs-verification]
14. Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, arXiv:1909.03562, 2019. [high-confidence]
15. David Bařina, *Convergence verification of the Collatz problem* (to $2^{68}$), 2020, DOI:10.1007/s11227-020-03368-x. [high-confidence]
16. Christian Hercher, *There are no Collatz $m$-cycles with $m \le 91$*, J. Integer Seq. 26 (2023), art. 23.3.5, arXiv:2201.00406. [verified]
17. David Bařina, *Improved verification limit for the convergence of the Collatz conjecture* (to $2^{71}$), J. Supercomput. 81, 810 (2025), DOI:10.1007/s11227-025-07337-0. [verified]

**Source-verification update (2026-07-01).** Addressing review concern (ii): references 14–17 and the headline bounds were checked against live sources on this date — Tao's paper at arXiv:1909.03562; Bařina's 2025 paper at Springer (DOI above) with the project page (pcbarina.fit.vutbr.cz) reporting all $n < 2^{71}$ verified as of 2025-01-15; Hercher's paper at the *Journal of Integer Sequences* and arXiv:2201.00406, including its statement that verification below $3\cdot 2^{69}$ raises the minimum odd-term count of any nontrivial cycle to $\ge 1.375\times 10^{11}$ (a threshold Bařina's bound now meets). The body text above has been updated from the superseded $2^{68}$ / hundreds-of-millions figures accordingly. Entries flagged [needs-verification] remain unchecked.

## AI Review Panel

### Claude (Anthropic) — in-house review

This survey is faithful to the dossier and correctly characterizes the central state of affairs: an open problem with a clear two-way decomposition (no cycle / no divergence), a genuine unconditional frontier in Tao's 2019 theorem, and a probabilistic heuristic that explains but does not prove. The altitude is right — it neither overstates the density results nor dismisses them, and it foregrounds the structural barriers (the measure-zero integers, the parity-type obstruction, the undecidability warning) that explain *why* the problem is hard rather than merely asserting that it is. The decomposition into conditional versus unconditional results in Section 2 is the document's strongest feature.

Three concerns a human reviewer must address. (i) **The references carry verification flags and must be checked against primary sources.** Of the fifteen selected, the dossier flags several as *needs-verification* — notably Steiner's 1-cycle paper, Simons–de Weger's m-cycle exclusion, Kurtz–Simon undecidability, Oliveira e Silva's verification, Eliahou's cycle bounds, and the Opfer dispute. Exact titles, years, venues, and identifiers for these are *not* independently confirmed here; the two DOIs and two arXiv ids should also be re-checked. Do not cite any flagged entry as established without source confirmation. (ii) **Several quantitative claims lean on a single source.** The "$2^{68}$" bound, the $x^{0.84}$ exponent, the "hundreds of millions of terms" cycle floor, and the attribution of the $\Pi^0_2$/undecidability result all trace to one dossier line each; a reviewer should confirm the verified bound (date and exact value), the Krasikov–Lagarias exponent, and especially the precise statement and authorship of the undecidability result, which is easy to overstate.

(iii) **The single most important thing to verify** is the exact wording and scope of Tao's 2019 theorem — specifically that it is *logarithmic* density (not natural density) and *almost bounded* (not bounded) — because the entire "how far is the frontier" assessment depends on that distinction, and conflating it would silently convert a partial result into a near-proof. The dossier states this correctly; the reviewer should confirm it survived into the survey intact (it has) and against arXiv:1909.03562 itself.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending

_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending

_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. The panel above is an automated, in-house assessment intended to surface concerns and verification targets, not to certify correctness. This meta-analysis is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and every reference flag and quantitative claim should be confirmed against primary sources before any citation or reliance. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
