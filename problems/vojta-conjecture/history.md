# History — Vojta's Conjecture

_Origin, formulation, and timeline._

## Origin

Vojta's conjecture crystallized a dictionary, long sensed but never made precise, between two seemingly unrelated theories: **Nevanlinna theory** (the value-distribution theory of holomorphic maps from $\mathbb{C}$, governed by Nevanlinna's Second Main Theorem of 1925) and **Diophantine approximation** (how well algebraic points can be approximated by rationals, governed by the theorems of Thue–Siegel–Roth and Schmidt's Subspace Theorem). Charles Osgood had noticed in the early 1980s that the exponent $2$ in Roth's theorem and the Euler characteristic appearing in Nevanlinna's defect relation were "the same" number. Paul Vojta, in his 1987 Harvard Ph.D. thesis (supervised by Barry Mazur) and the Springer Lecture Notes *Diophantine Approximations and Value Distribution Theory*, turned the analogy into a precise systematic correspondence and distilled from it a single sweeping inequality.

## Statement (height form)

Let $X$ be a smooth projective variety over a number field $k$, $D$ a normal-crossings divisor on $X$, $K_X$ the canonical divisor, $A$ a big (ample) divisor, and $S$ a finite set of places. For every $\varepsilon>0$ there is a proper Zariski-closed $Z\subsetneq X$ such that for all $k$-rational points $P\in X(k)\setminus Z$,
$$ m_S(P,D) + h_{K_X}(P) \le \varepsilon\, h_A(P) + O(1), $$
where $m_S$ is the proximity (counting) function to $D$ and $h$ denotes Weil heights. The arithmetic discriminant refines this with a term $d_k(P)$ for points of bounded degree (the "general $1+\varepsilon$" form): $m_S(P,D)+h_{K_X}(P)\le (1+\varepsilon)\,d_k(P)+\varepsilon\,h_A(P)+O(1)$.

The conjecture is the exact arithmetic mirror of the Griffiths–Nevanlinna second main theorem: $S$-integral / rational points play the role of a holomorphic curve, the proximity term mirrors the defect, and $K_X$ mirrors the ramification/Euler-characteristic term.

## Why it matters

Specializing the geometry recovers a startling list: the **abc conjecture** (blow up $\mathbb{P}^2$ at coordinate points, or work on $\mathbb{P}^1$ with $D=\{0,1,\infty\}$), the **Mordell conjecture / Faltings' theorem** (curves of genus $\ge 2$ have finitely many rational points), the **Bombieri–Lang conjecture** (general-type varieties are not potentially dense), Schmidt's Subspace Theorem in qualitative form, and Siegel's theorem on integral points. A single inequality thus unifies much of Diophantine geometry.

## Timeline

- **1925** — Rolf Nevanlinna proves the Second Main Theorem, the analytic template.
- **1955** — Klaus Roth proves the sharp approximation exponent $2$ (Fields Medal 1958).
- **1972** — Wolfgang Schmidt establishes the Subspace Theorem.
- **early 1980s** — Charles Osgood observes the numerical coincidence between Roth's exponent and Nevanlinna's defect relation.
- **1983** — Faltings proves the Mordell conjecture by other means, sharpening the demand for a structural explanation.
- **1987** — Vojta states the conjecture in his thesis and in LNM 1239, fixing the full dictionary.
- **1991** — Vojta gives a new proof of the Mordell conjecture using Diophantine approximation (Arakelov/Gillet–Soulé arithmetic intersection), confirming the program's power.
- **1992** — Faltings proves the Mordell–Lang conjecture for subvarieties of abelian varieties ("Diophantine approximation on abelian varieties"), a major case in the conjecture's orbit.
- **1994** — Vojta extends Faltings' results to semiabelian varieties.
- **1996** — Vojta proves a general result on integral points on semiabelian varieties, the strongest unconditional evidence toward the conjecture.
- **2000s** — Ru, Wong, Evertse, Corvaja–Zannier develop the Subspace-Theorem method, proving cases of the conjecture for divisors on $\mathbb{P}^n$ and on surfaces.
- **2008** — Corvaja–Zannier and Levin obtain new degeneracy results for integral points via the conjecture's $\mathbb{G}_m^n$ cases.
- **2009–2021** — Autissier, Levin, Ru–Vojta (general "Ru–Vojta theorem" 2020) prove the conjecture for divisors in general position under Seshadri-type conditions; the function-field and "$abc$-for-function-fields" analogues are established.
- **present** — The conjecture remains open in full. The general-type / $K_X$ case, and uniform $abc$, are the frontier; no path is known that does not effectively prove $abc$.
