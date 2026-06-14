# Originator(s) — Carmichael's Totient Conjecture

_Biography, background, and the ideas that led here._

**Robert Daniel Carmichael** (1879–1967) was an American mathematician whose name attaches to several enduring objects in number theory and beyond: the **Carmichael numbers** (composite $n$ satisfying Fermat's little theorem for all bases coprime to $n$, the "pseudoprimes" that complicate primality testing), the **Carmichael function** $\lambda(n)$ (the exponent of the multiplicative group $(\mathbb{Z}/n\mathbb{Z})^\times$), and the **totient conjecture** treated here.

## Life and background

Carmichael was born in Goodwater, Alabama. He received his undergraduate education at Lineville College and earned his Ph.D. in 1911 from **Princeton University** under **G. D. Birkhoff** — one of Birkhoff's earliest doctoral students. His thesis, on the theory of linear difference equations, reflected a breadth of interest that ranged from number theory and group theory to differential equations and the foundations and philosophy of relativity, on which he later wrote expository books.

He taught at Indiana University and then, for the bulk of his career, at the **University of Illinois at Urbana–Champaign**, where he served as a long-time and influential graduate dean and supervised a large number of doctoral students. He was a prolific author of textbooks and research papers, an editor, and a fixture of early-twentieth-century American mathematics during the period when the U.S. research community was maturing.

## The idea behind the conjecture

Carmichael's totient work grew directly out of his fascination with the multiplicative structure of $(\mathbb{Z}/n\mathbb{Z})^\times$ and the arithmetic functions $\varphi$ and $\lambda$ that describe it. In his 1907 paper "On Euler's $\varphi$-function" (_Bulletin of the AMS_), he examined the **fibers** of $\varphi$ — how many integers share a given totient — and observed empirically that totient values are never produced uniquely. The intuition is concrete: the standard formula $\varphi(n)=n\prod_{p\mid n}(1-1/p)$ makes $\varphi$ highly "collision-prone," because distinct factorizations frequently yield the same product. Carmichael conjectured that this collision behavior is **universal**: the value $1$ is never a fiber size.

He believed he had a proof and published it as such. By **1922** he recognized a gap in the argument and issued a correction in the same _Bulletin_, downgrading the claim to a conjecture and providing the first concrete lower bound ($>10^{37}$) below which no counterexample can lie. This honest retraction is itself part of the conjecture's character: the problem looks elementary and "obviously true," yet a complete, gap-free proof has resisted more than a century of effort.

## Legacy

Carmichael's name became attached to so many distinct results that "Carmichael" functions almost as a brand in elementary and computational number theory. The totient conjecture is the least resolved of these. Where Carmichael numbers were eventually shown to be infinite (Alford–Granville–Pomerance, 1994) and the Carmichael function is thoroughly understood, the totient multiplicity conjecture remains stubbornly open — a fitting memorial to a mathematician drawn to the deceptively simple structure of modular arithmetic. The modern formulation is unchanged from Carmichael's: only the surrounding analytic apparatus (Klee, Pomerance, Ford) has grown around the original, still-unproven assertion that $A(n)\neq 1$ for every $n$.
