# Originator(s) — Lehmer's Conjecture on the Ramanujan Tau Function

_Biography, background, and the ideas that led here._

## Derrick Henry Lehmer (1905–1991)

**Derrick Henry Lehmer** — universally "D. H. Lehmer" — was an American number theorist whose career bridged classical analytic and computational number theory at exactly the moment mechanical and electronic computation became feasible. He was born on 23 February 1905 in Berkeley, California, the son of Derrick Norman Lehmer, himself a number theorist at Berkeley known for factor-table and prime-sieve work. The younger Lehmer absorbed this milieu directly: as a child he helped operate his father's mechanical factoring devices, and a lifelong instinct for treating number-theoretic questions as concrete computational experiments runs through all of his work.

Lehmer took his undergraduate degree at Berkeley and his Ph.D. at Brown University in 1930, under Jacob Tamarkin. He held positions at Lehigh and elsewhere before settling at the University of California, Berkeley, where he spent the bulk of his career and trained numerous students. During the Second World War he worked at the Aberdeen Proving Ground and was among the early users of the ENIAC, running number-theoretic computations on one of the first electronic computers. He married **Emma Lehmer** (née Trotskaia), herself a distinguished number theorist and frequent collaborator. (Lehmer's Berkeley tenure was briefly interrupted in the early 1950s by the University of California loyalty-oath controversy, which he, like several colleagues, resisted; he was later reinstated.)

### The ideas behind the conjecture

Lehmer's signature was the marriage of deep classical number theory with serious computation. He is responsible for the **Lucas–Lehmer primality test** for Mersenne numbers, foundational work on sieve methods (including physical sieve machines), studies of cyclotomy and the distribution of primitive roots, and the separate, famous **Lehmer Mahler-measure problem** (the smallest Mahler measure $>1$ of an integer polynomial) — a different "Lehmer's conjecture" not to be confused with the tau problem.

His engagement with the Ramanujan tau function fits this pattern. By the 1940s $\tau(n)$ was understood to be multiplicative (Mordell) and the subject of striking congruences (Ramanujan, Wilton), but its qualitative behavior — in particular whether it could ever vanish — was unexamined. Lehmer's instinct was to compute. Tabulating $\tau(n)$ and finding no zeros, he distilled the multiplicative structure into the key reduction: $\tau$ never vanishes if and only if $\tau(p)\ne 0$ for every prime $p$. He framed the persistent non-vanishing not as an idle numerical curiosity but as a precise conjecture demanding explanation, writing in his 1947 paper that the absence of zeros "seems very remarkable." That combination — a clean reduction plus a computationally grounded conjecture — is the lasting form of the problem.

### Why the problem is hard, in Lehmer's framing

Lehmer recognized that the obstruction is structural. The Hecke recursion expresses $\tau(p^r)$ through $\tau(p)$ alone, so a single prime zero would propagate, yet nothing in the available analytic apparatus pins $\tau(p)$ away from zero at an individual prime. The conjecture thus isolates a hard local question — the exact value (not merely the size) of a Frobenius trace — inside a theory that otherwise controls $\tau$ only in aggregate.

### Legacy

Lehmer's name attaches to several of the most durable open problems in number theory; the tau non-vanishing conjecture is among the most quoted. Beyond specific problems, his career helped legitimize experimental and computational number theory as a serious discipline: he founded and long edited *Mathematics of Computation*, championed machine computation in pure mathematics, and produced extensive tables that seeded later theoretical work. The modern framing of his tau conjecture in terms of $\ell$-adic Galois representations — Frobenius traces of $\rho_{\Delta,\ell}$ — is a translation of his elementary 1947 observation into the language of Deligne, Serre, and Swinnerton-Dyer, but the question he asked is unchanged. D. H. Lehmer died on 22 May 1991 in Berkeley.
