# History — Schanuel's Conjecture

Schanuel's Conjecture is the single statement that, if true, would systematize essentially all of classical transcendence theory for the exponential function. It asserts a uniform lower bound on transcendence degree:

> **Schanuel's Conjecture.** If $z_1,\dots,z_n \in \mathbb{C}$ are linearly independent over $\mathbb{Q}$, then the field $\mathbb{Q}(z_1,\dots,z_n,e^{z_1},\dots,e^{z_n})$ has transcendence degree at least $n$ over $\mathbb{Q}$.

The conjecture arose not from an isolated puzzle but from the recognition that the major transcendence results of the early twentieth century — Hermite's transcendence of $e$ (1873), Lindemann's of $\pi$ (1882), the Lindemann–Weierstrass theorem, and the Gelfond–Schneider theorem (1934) settling Hilbert's seventh problem — were all special cases or shadows of one organizing principle. Schanuel's insight, recorded and disseminated by Serge Lang, was to ask for the *maximal* algebraic independence one could plausibly hope for among numbers $z_i$ and their exponentials, given only the obvious obstruction: linear $\mathbb{Q}$-relations among the $z_i$ force multiplicative relations among the $e^{z_i}$.

The strength of the formulation is immediate. Taking $n=1$, $z_1 = 1$ recovers transcendence of $e$. Taking $z_1 = 2\pi i$, where $e^{z_1}=1$ is algebraic, forces $2\pi i$ — hence $\pi$ — transcendental. More generally the conjecture implies the Lindemann–Weierstrass theorem and the Gelfond–Schneider theorem as corollaries. Famously, applying it to a $\mathbb{Q}$-independent pair would give the algebraic independence of $e$ and $\pi$ over $\mathbb{Q}$ — a result still completely open, illustrating how far beyond current technique the conjecture reaches.

A pivotal reformulation came through model theory and exponential algebra. Boris Zilber, in work culminating in his 2005 paper on *pseudo-exponentiation*, constructed an exponential field (now called Zilber's field $\mathbb{B}$) that is the unique model in cardinality $2^{\aleph_0}$ of a natural set of axioms, and in which a *strong* form of Schanuel's Conjecture holds by construction. Zilber conjectured that $\mathbb{B} \cong (\mathbb{C}, \exp)$. This recasts Schanuel's Conjecture as part of a categoricity statement about the complex exponential field, fusing transcendence theory with the model theory of Hrushovski constructions.

## Timeline

- **1873** — Hermite proves $e$ is transcendental.
- **1882** — Lindemann proves $\pi$ transcendental; with Weierstrass's extension this becomes the Lindemann–Weierstrass theorem ($e^{\alpha_1},\dots,e^{\alpha_n}$ algebraically independent for $\mathbb{Q}$-independent algebraic $\alpha_i$).
- **1934** — Gelfond and Schneider independently settle Hilbert's seventh problem: $a^b$ is transcendental for algebraic $a\neq 0,1$ and algebraic irrational $b$.
- **c. 1960** — Stephen Schanuel formulates the conjecture; it circulates through Serge Lang's lectures and correspondence.
- **1966** — Lang's *Introduction to Transcendental Numbers* publishes the conjecture, naming it and noting that it implies the Lindemann–Weierstrass and Gelfond–Schneider theorems.
- **1971** — James Ax proves the **formal/differential analogue** (Ax–Schanuel): the conjecture holds with $\mathbb{C}$ replaced by formal power series / differential fields, giving the first decisive structural evidence.
- **1980s** — Waldschmidt, Wüstholz and others advance transcendence on algebraic groups; Wüstholz's analytic subgroup theorem (1989) yields the strongest unconditional *linear* results.
- **2004–2005** — Boris Zilber constructs pseudo-exponential fields, proving categoricity and embedding a strong Schanuel statement as an axiom; conjectures $\mathbb{B}\cong(\mathbb{C},\exp)$.
- **2006–2010** — Kirby, Macintyre, Marker, and others develop the model theory of the exponential closure and "exponential-algebraic closedness".
- **2010s** — Pila–Zannier o-minimality methods and Ax–Schanuel-type theorems proliferate (Pila–Tsimerman for the $j$-function; Mok–Pila–Tsimerman in the Shimura-variety setting).
- **2021–2023** — Bays–Kirby and Aslanyan–Kirby establish strong **Exponential-Algebraic Closedness** results, reducing Zilber's conjecture to a strong form of Schanuel plus closedness; the arithmetic core remains untouched.

As of 2026 the conjecture is open for every $n\ge 1$ in the genuinely complex-analytic setting beyond the cases already covered by Lindemann–Weierstrass and Gelfond–Schneider.
