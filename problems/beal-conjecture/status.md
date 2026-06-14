# Status & Frontier — The Beal Conjecture

**Status: open.** There is no accepted proof and no known counterexample. The conjecture states that $A^x+B^y=C^z$ with $x,y,z>2$ and $A,B,C$ positive integers forces $\gcd(A,B,C)>1$.

## What is known (unconditional)

- **The diagonal case is closed.** For $x=y=z=n\ge 3$, coprime solutions are impossible by Fermat's Last Theorem (Wiles 1995). This is the deepest established sub-statement.
- **Finiteness per signature.** For every fixed exponent triple $(p,q,r)$ with $\tfrac1p+\tfrac1q+\tfrac1r<1$ — which includes all Beal signatures except $(3,3,3)$ — there are only finitely many coprime solutions (Darmon–Granville 1995, via Faltings). This bound is **ineffective**: it gives no way to enumerate or exclude the solutions.
- **Many individual signatures fully resolved.** A large catalogue of triples $(p,q,r)$ has been completely settled by the modular method and by descent/Chabauty: the families $(n,n,2)$, $(n,n,3)$, and numerous mixed and small-exponent cases (Darmon–Merel, Bennett–Skinner, Kraus, Bruin, Poonen–Schaefer–Stoll, Siksek, Chen, Dahmen, Freitas, and others). Within the strict Beal range these confirm the conjecture for infinitely many — but not all — exponent configurations.
- **Computation.** No coprime counterexample exists within the (large) ranges of bases and exponents that have been searched.

## What is known (conditional)

- **Under the $abc$ conjecture**, Beal holds for all but finitely many solutions; with a sufficiently effective form of $abc$ it would follow entirely. The $abc$ conjecture itself is open: Mochizuki's claimed proof (published 2021) is **disputed**, with the Scholze–Stix objection (2018) unresolved by community consensus.

## What a full resolution would require

The essential gap is **uniformity across infinitely many exponent triples**. Every effective method is tied to a single signature $(p,q,r)$; Faltings' finiteness is ineffective and non-uniform. A complete proof would need one of:

1. an **unconditional, effective $abc$** (or a Beal-tailored Diophantine inequality) strong enough to bound the smooth terms;
2. a **uniform Frey-curve / modularity construction** covering all hyperbolic signatures at once, rather than case by case; or
3. a genuinely new structural idea linking the coprimality hypothesis to a global obstruction.

A short, elementary proof is regarded as unlikely: it would imply an unexpectedly elementary route to FLT (a corollary of Beal), contrary to the depth FLT is known to require. The most plausible near-term routes are incremental — extending the modular method over number fields (asymptotic-Fermat techniques) to swallow ever-larger families of signatures — while a clean general theorem awaits progress on $abc$ or a new method.

## Related problems

- [The abc Conjecture](../abc-conjecture/README.md) — implies Beal up to finitely many exceptions; the natural conditional route.
- [Fermat's Last Theorem context: Goldbach Conjecture](../goldbach-conjecture/README.md) — companion additive/multiplicative number-theory problem of comparable fame.
- [The Erdős–Straus Conjecture](../erdos-straus-conjecture/README.md) — another elementary-to-state Diophantine equation resistant to general proof.
- [The Riemann Hypothesis](../riemann-hypothesis/README.md) — the central conditional-results hub of analytic number theory bordering this area.
- [Odd Perfect Numbers](../odd-perfect-numbers/README.md) — a sibling "elementary statement, deep obstruction" problem in multiplicative number theory.
