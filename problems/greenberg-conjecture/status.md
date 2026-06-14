# Status & Frontier — Greenberg's Conjecture

_Where the problem stands and what a resolution would require._

**Status: open.** For a totally real number field $k$ and a prime $p$, the conjecture asserts $\lambda_p(k) = \mu_p(k) = 0$ for the cyclotomic $\mathbb{Z}_p$-extension — equivalently, the $p$-part of the class number $h_n$ of $k_n$ is bounded, i.e. $X_\infty = \varprojlim A_n$ is finite. No proof and no counterexample are known.

## What is known (unconditional)

- **$\mu = 0$ in the abelian case.** Ferrero–Washington (1979): $\mu_p(k) = 0$ for every abelian number field. So for abelian totally real $k$ the conjecture is exactly the statement $\lambda_p(k) = 0$. For non-abelian totally real fields, even $\mu_p = 0$ is open in general.
- **Analytic interpretation.** Via the Iwasawa Main Conjecture (Mazur–Wiles, 1984, over $\mathbb{Q}$), $\lambda_p$ counts the zeros in the open unit disk of the relevant $p$-adic $L$-function; vanishing is thus equivalent to that $L$-function having no such zeros (being a $p$-adic unit power series, up to known factors).
- **Effective finite criteria.** Fukuda's stabilization theorem makes finiteness of $X_\infty$ checkable: equality of $p$-ranks of $A_n, A_{n+1}$ at a suitable level (under a splitting hypothesis on $p$) forces $\lambda = \mu = 0$.
- **Many families verified.** $\lambda_p = \mu_p = 0$ is proven for infinitely many real quadratic and cubic fields under hypotheses on the splitting of $p$ and on cyclotomic-unit indices (Greenberg, Fukuda–Komatsu, Ozaki–Taya, Ichimura–Sumida), and confirmed numerically for thousands of fields and small primes. No counterexample has ever appeared.

## What is known (conditional)

- Greenberg's Conjecture follows in various settings from the **Gross–Kuz'min conjecture** or from **non-vanishing of a $p$-adic regulator** of global units; Brumer's $p$-adic Baker theorem supplies Gross–Kuz'min (hence inputs) in many abelian cases.
- Sufficient unit/regulator and capitulation criteria (Greenberg, Fukuda) give vanishing whenever a specific $p$-adic index is a unit.

## What a full resolution requires

A general proof must control the zeros of $p$-adic $L$-functions (or, equivalently, non-vanishing of $p$-adic regulators) for **all** totally real $k$ and **all** $p$ — without circular appeal to the conjecture. Ozaki's constructions of totally real fields with arbitrarily complicated $\Lambda$-module structure show that no purely algebraic/structural argument can suffice: genuinely analytic or transcendence-theoretic input is needed. In the non-abelian case one additionally needs $\mu_p = 0$, itself unproven.

## Plausible routes

1. **Main-Conjecture + non-vanishing.** Combine the (now broadly available) Main Conjectures for totally real fields with a general non-vanishing theorem for $p$-adic $L$-values/regulators — the latter being the missing piece.
2. **Gross–Kuz'min first.** Settle Gross–Kuz'min unconditionally, then transfer to Greenberg via the known implications.
3. **Transcendence input.** Extend $p$-adic linear-forms-in-logarithms (Brumer-type) methods to force non-vanishing of the relevant regulators beyond the abelian case.
4. **Module-theoretic control** of $X_\infty$ via Fitting ideals and Selmer modules, conditional on the analytic non-vanishing.

The consensus is that the conjecture is true; what is lacking is a uniform handle on the analytic non-vanishing that the algebraic framework reduces it to.

## Related problems

- [Riemann Hypothesis](../riemann-hypothesis/) — non-vanishing of $L$-functions; classical analogue of the analytic input needed here.
- [Birch–Swinnerton-Dyer Conjecture](../birch-swinnerton-dyer/) — Iwasawa-theoretic and Selmer-group methods overlap heavily.
- [Grand Riemann Hypothesis](../grand-riemann-hypothesis/) — zeros of automorphic $L$-functions, the analytic backdrop to Iwasawa Main Conjectures.
- [Fontaine–Mazur Conjecture](../fontaine-mazur-conjecture/) — Galois-representation framework shared with modern Iwasawa theory.
- [Telescope Conjecture](../telescope-conjecture/) — a different "vanishing/finiteness" conjecture, included as a structural sibling in the Atlas.
