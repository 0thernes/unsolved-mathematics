---
title: "Meta-Analysis: The Hadwiger–Nelson Problem"
slug: hadwiger-nelson-problem
author: Alexander Donahue
type: ai-assisted-meta-analysis
peer_reviewed: false
problem_status: active-progress
ai_review:
  claude:
    verdict: accept-with-revisions
    date: "2026-06-14"
    version: "claude-opus-4-8"
    summary: "A faithful, well-scoped survey of the chromatic number of the plane that correctly reports the 5 ≤ χ ≤ 7 bracket and the 2018 de Grey breakthrough, but leans on several unverified or AI-suggested citations that require primary-source checking."
  gpt:
    verdict: pending
  gemini:
    verdict: pending
  grok:
    verdict: pending
human_review: pending
---

# Meta-Analysis: The Hadwiger–Nelson Problem

> **AI-generated meta-analysis — not peer-reviewed.** Curated and accredited by **Alexander Donahue** (human-in-the-loop). A survey/assessment of an open problem; it makes no claim of a new result. Citations carry verification flags and require human source-checking.

## Abstract

The Hadwiger–Nelson problem asks for the **chromatic number of the plane** $\chi(\mathbb{R}^2)$: the fewest colors needed so that no two points at Euclidean distance exactly $1$ share a color. Equivalently it is the chromatic number of the infinite unit-distance graph $G(\mathbb{R}^2)$. Posed by Edward Nelson in 1950 — with John Isbell supplying the hexagonal $7$-coloring that gives the still-standing upper bound — the problem sat at $4 \le \chi \le 7$ for sixty-eight years. In April 2018 Aubrey de Grey exhibited an explicit $1581$-vertex unit-distance graph with no proper $4$-coloring, raising the lower bound to $\chi \ge 5$; the bracket is now $5 \le \chi \le 7$. This survey records the statement and its significance, the De Bruijn–Erdős reduction to finite graphs, the SAT-driven Polymath16 minimizations, the measurable/density and spectral relaxations, and the unresolved question of whether $\chi$ is even fully determined by ZFC. It assesses which routes are live, flags reliance on several unverified citations, and states what a full resolution would demand. No new mathematical result is claimed.

## 1. Statement and significance

Color every point of the Euclidean plane so that any two points exactly one unit apart receive different colors. The minimum number of colors is $\chi(\mathbb{R}^2)$, the chromatic number of the infinite graph whose vertices are all points of $\mathbb{R}^2$ and whose edges join unit-distance pairs. The problem is celebrated for the extreme gap between the simplicity of its statement and the difficulty of its resolution: anyone can understand the question, yet the exact value has been open for more than seventy years. It sits at the junction of combinatorial geometry, graph coloring, and Euclidean Ramsey theory, and it seeded the modern study of unit-distance graphs. Its appeal is amplified by a genuine foundational subtlety — the possibility, raised by Erdős, that the answer might depend on set-theoretic axioms.

## 2. State of the art

The current unconditional bracket is
$$5 \le \chi(\mathbb{R}^2) \le 7.$$
The upper bound $\chi \le 7$ is Isbell's $7$-coloring of a tiling by regular hexagons of diameter slightly under $1$ (1950), never improved. The lower bound $\chi \ge 5$ is the 2018 result of **Aubrey de Grey**, who constructed an explicit $1581$-vertex unit-distance graph with no proper $4$-coloring (arXiv:1804.02385). Because the claim reduces to a finite, fully specified graph, it was independently verified within days by SAT solvers and reproduced by other researchers; it is accepted without serious dispute. The earlier record, $\chi \ge 4$, came from the **Moser spindle** (1961), a rigid $7$-vertex $4$-chromatic graph. Following de Grey, the **Polymath16** collaboration and **Marijn Heule** drove the smallest known $5$-chromatic unit-distance graphs down to roughly $500$ vertices (examples near $510$ and $509$ are reported), with machine-checkable UNSAT certificates. On the restricted side, **Falconer (1981)** established that the *measurable* chromatic number is at least $5$, and later density and Lovász-theta / LP arguments have been reported to push measurable lower bounds higher.

## 3. Principal approaches and barriers

**Finite unit-distance graphs (De Bruijn–Erdős).** The De Bruijn–Erdős theorem (1951, via compactness/choice) reduces the infinite problem to finite subgraphs: to prove $\chi \ge k$ it suffices to find one finite unit-distance graph that is not $(k-1)$-colorable. This converts an infinitary question into a finite search and underwrites every lower-bound advance. *Barrier:* no finite $6$-chromatic unit-distance graph is known, and there is no proof one exists. If $\chi = 5$, this entire route to $\chi \ge 6$ is closed.

**SAT solvers and computer search.** De Grey's graph and all Polymath16 refinements depend on encoding "$G$ is $k$-colorable" as Boolean satisfiability, with vertex-criticality search used to shrink known examples. *Barrier:* certifying $\chi \ge 6$ needs an UNSAT instance for $5$-coloring of some graph one must *first find*; candidate graphs are far larger, and exact unit-distance realizability (often irrational coordinates) complicates encoding.

**Measurable and density colorings.** Restricting to measurable color classes admits harmonic-analysis and LP/SDP tools; Falconer's $\chi_m \ge 5$ is the anchor, with reported pushes toward $\chi_m \ge 6$. *Barrier:* the true optimal coloring may be non-measurable (built using choice), so these bounds need not transfer to $\chi$.

**Upper-bound constructions and spectral/LP relaxations.** No $6$-coloring of the full plane is known; every attempt to beat Isbell's $7$ has failed. Fractional and independence-density bounds (the $m_1(\mathbb{R}^2)$ problem) give nontrivial constraints but, being relaxations, cannot force the integer $\chi$ upward.

## 4. Critical assessment

The dossier is internally consistent and faithful to the established landscape. Its central claims — the $5 \le \chi \le 7$ bracket, the De Bruijn–Erdős reduction, the 2018 de Grey breakthrough at $1581$ vertices, the Polymath16 minimizations toward ~$500$ vertices, and Falconer's measurable bound — are the standard account and are correctly stated. The treatment is appropriately honest that this is an *open* problem: there is no claimed resolution to contest, and the one breakthrough is finite and machine-verified.

Two cautions are warranted. First, the most reliably anchored citation is de Grey's arXiv:1804.02385; many other rows in the bibliography carry `needs-verification` or `ai-suggested` flags, and several quantitative claims about minimal vertex counts and about measurable bounds reaching $\chi_m \ge 6$ are reported rather than pinned to confidently identified sources. Second, the founding contributions of Nelson and Isbell were never formally published, so their record is necessarily indirect (Gardner's column; Soifer's *The Mathematical Coloring Book*). These are limitations of sourcing, not of the mathematics, but they matter for a survey that aims to be citable.

## 5. What a resolution would require / open directions

- **To prove $\chi \ge 6$:** exhibit a finite unit-distance graph that is not $5$-colorable (one suffices, by De Bruijn–Erdős). None is known; this is the most active target.
- **To prove $\chi = 5$:** beyond $\chi \ge 5$, construct an explicit $5$-coloring of the whole plane with no monochromatic unit pair — none is known.
- **To prove $\chi \le 6$:** find an explicit $6$-coloring beating Isbell's $7$ — every attempt has failed.
- **To prove $\chi = 7$:** show no $6$-coloring exists — currently inaccessible.
- **Foundational direction:** determine whether $\chi(\mathbb{R}^2)$ is fully fixed by ZFC, given Shelah–Soifer results that related distance-graph chromatic numbers can be axiom-sensitive.

The most plausible near-term route is continued computer-assisted finite search; the measurable/LP route could at best force $\chi \ge 6$ under regularity; closing the upper bound likely requires a genuinely new coloring idea. Most experts regard $\chi \in \{5,6,7\}$ as genuinely undecided.

## 6. Selected references

1. N. G. de Bruijn, P. Erdős, *A colour problem for infinite graphs and a problem in the theory of relations* (1951) — foundational [high-confidence]
2. Martin Gardner, *Mathematical Games* column introducing the problem, *Scientific American* (1960) — expository [high-confidence]
3. Leo Moser, William Moser, *Solution to Problem 10* (the Moser spindle) (1961) — foundational [high-confidence]
4. Hugo Hadwiger, *Ungelöste Probleme* (Nr. 40) (1961) — expository [needs-verification]
5. P. Erdős, R. L. Graham, P. Montgomery, B. Rothschild, J. Spencer, E. Straus, *Euclidean Ramsey theorems I* (1973) — foundational [high-confidence]
6. Kenneth J. Falconer, *A unit-distance graph and the chromatic number of the plane* (measurable bound) (1981) — breakthrough [needs-verification]
7. Saharon Shelah, Alexander Soifer, *Axiom of choice and chromatic number of the plane* (2004) — negative-result [needs-verification]
8. Alexander Soifer, *The Mathematical Coloring Book* (2008) — survey [high-confidence]
9. Aubrey D. N. J. de Grey, *The chromatic number of the plane is at least 5*, arXiv:1804.02385 (2018) — breakthrough [high-confidence]
10. Marijn J. H. Heule, *The chromatic number of the plane is at least 5: a new proof (smaller graphs)*, arXiv:1805.12181 (2018) — computational [needs-verification]
11. Geoffrey Exoo, Dan Ismailescu, *A smaller 5-chromatic unit-distance graph in the plane*, arXiv:1805.06055 (2018) — modern [needs-verification]
12. D.H.J. Polymath, *The chromatic number of the plane is at least 5* (Polymath16 progress) (2019) — modern [needs-verification]
13. New lower bounds for the independence ratio / measurable density of the plane (LP/SDP methods) (2016) — computational [ai-suggested]
14. Measurable chromatic number lower bounds (≥6 under measurability) (2021) — breakthrough [ai-suggested]
15. *Recent developments on the chromatic number of the plane* (survey) (2023) — survey [ai-suggested]

## AI Review Panel

### Claude (Anthropic) — in-house review

The survey is a solid, honestly framed treatment. Its strengths are accuracy and discipline: it reports the $5 \le \chi \le 7$ bracket correctly, distinguishes the *measurable* chromatic number from the ordinary one (a distinction frequently muddled in popular accounts), and resists the common error of implying the 2018 breakthrough settled the value — it raised only the lower bound. The decomposition into independent upper-bound (coloring) and lower-bound (forbidden-configuration) tasks, and the central observation that we possess no theorem *characterizing* when a unit-distance graph forces many colors, are exactly the right framing.

My principal reservations concern sourcing. (i) The bibliography's verification flags are doing real work: only de Grey's arXiv:1804.02385 is high-confidence and identifier-anchored on the modern side, while several rows are `ai-suggested` placeholders for genuine *lines* of work rather than confirmed titled papers — a human must confirm these exist before citing them. (ii) Two specific claims rest on single or unverified sources and risk overstatement: the precise minimal vertex counts (e.g. "509/510") and the assertion that measurable lower bounds have reached $\chi_m \ge 6$; both should be checked against primary literature, as numbers in this fast-moving area drift and are easy to misattribute. (iii) The single most important thing a human reviewer should verify is the **arXiv identifiers in rows 10 and 11** (Heule 1805.12181; Exoo–Ismailescu 1805.06055) and the existence/title of the Falconer (1981) measurable-bound paper — these are load-bearing for the modern narrative yet flagged `needs-verification`.

None of this undermines the mathematics, which is standard and correctly reported; the gaps are bibliographic and resolvable by source-checking. I therefore recommend acceptance contingent on that verification pass.

**Verdict:** accept-with-revisions.

### GPT (OpenAI) — pending
_Not yet run. To complete the panel, run the prompt in docs/review/REVIEW-TEMPLATE.md through GPT and record the verdict here and in the front matter._

### Gemini (Google) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

### Grok (xAI) — pending
_Not yet run. See docs/review/REVIEW-TEMPLATE.md._

## Human verification

AI review is not human peer review. This document is offered for academic verification per ../docs/review/ACADEMIC-REVIEW.md, and its citations — especially those flagged `needs-verification` or `ai-suggested` — require checking against primary sources before being relied upon. Status: human_review pending.

---
*Accredited to **Alexander Donahue** · The Unsolved Mathematics Atlas · CC BY 4.0. Cite per CITATION.cff.*
