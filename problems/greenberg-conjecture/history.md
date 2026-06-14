# History — Greenberg's Conjecture

_Origin, formulation, and timeline._

## Origin

Greenberg's Conjecture grew directly out of the foundational period of Iwasawa theory. In the late 1950s Kenkichi Iwasawa initiated the study of how class numbers vary in towers of number fields. For a number field $k$ and a prime $p$, the cyclotomic $\mathbb{Z}_p$-extension $k_\infty/k$ is the unique tower $k = k_0 \subset k_1 \subset \cdots$ with $\mathrm{Gal}(k_\infty/k) \cong \mathbb{Z}_p$, obtained from the $p$-power cyclotomic fields. Iwasawa proved that if $p^{e_n}$ is the exact power of $p$ dividing the class number $h_n$ of $k_n$, then for $n \gg 0$,
$$ e_n = \lambda n + \mu p^n + \nu, $$
with integers $\lambda = \lambda_p(k) \ge 0$, $\mu = \mu_p(k) \ge 0$, and $\nu$ independent of $n$. The invariants $\lambda$ and $\mu$ encode the structure of the inverse limit $X_\infty$ of $p$-class groups as a module over the Iwasawa algebra $\Lambda \cong \mathbb{Z}_p[[T]]$.

## Formulation

Ralph Greenberg, in his 1976 paper "On the Iwasawa invariants of totally real number fields" (American Journal of Mathematics), asked whether these invariants must vanish in the simplest natural case. The conjecture states: **for a totally real number field $k$ and any prime $p$, the cyclotomic invariants satisfy $\lambda_p(k) = \mu_p(k) = 0$.** Equivalently, the $p$-part of the class number $h_n$ is bounded as $n \to \infty$, so $X_\infty$ is finite.

The $\mu = 0$ half is itself believed but generally open; it is known only in special families. The Ferrero–Washington theorem (1979) proves $\mu_p = 0$ for all abelian $k$, so for abelian totally real fields Greenberg's Conjecture reduces to the assertion $\lambda_p = 0$. This $\lambda = 0$ statement is the heart of the problem and what is usually meant by "Greenberg's Conjecture." It admits a sharp reformulation via Iwasawa's Main Conjecture (proved by Mazur–Wiles, 1984): $\lambda_p = 0$ is tied to the non-vanishing of $p$-adic $L$-functions and to the triviality of certain $p$-adic regulators of units (Gross-type conditions).

## Timeline

**1959** — Iwasawa introduces $\mathbb{Z}_p$-extensions and proves the growth formula for $e_n$.

**1973** — Iwasawa develops the $\Lambda$-module framework and the main-conjecture philosophy linking $\lambda$ to $p$-adic $L$-functions.

**1976** — Greenberg poses the conjecture for totally real fields in the American Journal of Mathematics; he also gives criteria (involving units and $p$-adic $L$-values) for $\lambda = \mu = 0$.

**1979** — Ferrero and Washington prove $\mu_p(k) = 0$ for all abelian number fields, settling the $\mu$ half in the abelian case.

**1984** — Mazur and Wiles prove the Iwasawa Main Conjecture over $\mathbb{Q}$, sharpening the analytic interpretation of $\lambda$.

**1982** — Greenberg (with the criterion of his thesis advisor Iwasawa's circle) and others link $\lambda_p = 0$ for real quadratic fields to the index of cyclotomic units and capitulation of ideals.

**1980s–1990s** — Extensive computational verification: Kraft, Schoof, Ozaki, Taya, Fukuda, and Komatsu verify the conjecture for many real quadratic and cubic fields and small primes; effective criteria via cyclotomic units and capitulation are refined.

**1990s–2000s** — Ozaki–Taya, Itoh, and Fukuda–Komatsu obtain results for $\mathbb{Q}(\sqrt{d})$ under conditions on how $p$ splits and on unit indices; Greenberg's generalized conjecture (vanishing of higher invariants in multiple $\mathbb{Z}_p$-extensions) is studied.

**2000s–2010s** — Connections deepen to the Gross–Kuz'min conjecture, to non-vanishing of $p$-adic regulators, and to Galois deformation theory; large-scale numerics confirm the conjecture for $p = 3, 5, 7$ across many real quadratic and biquadratic fields.

**2020s** — The conjecture remains open in general, established only conditionally or in restricted families. No counterexample is known; the consensus is strongly in its favor. It is regarded as one of the central open problems of Iwasawa theory.
