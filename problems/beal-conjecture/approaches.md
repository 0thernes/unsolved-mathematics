# Approaches — The Beal Conjecture

The Beal Conjecture is the coprime case of the generalized Fermat equation $A^x+B^y=C^z$ with $x,y,z>2$. No single technique reaches the full statement; progress is organized by exponent signature $(p,q,r)$ and by the inverse-sum $\chi=\tfrac1p+\tfrac1q+\tfrac1r$. The principal lines of attack follow.

## The modular method (Frey curves, level-lowering, modularity)

The dominant tool, descended directly from the proof of FLT. To a putative coprime solution of $A^p+B^q=C^r$ one attaches a **Frey–Hellegouarch elliptic curve** whose discriminant encodes the solution. Ribet's level-lowering and the modularity of elliptic curves over $\mathbb{Q}$ (Wiles; Breuil–Conrad–Diamond–Taylor) then force the associated mod-$\ell$ Galois representation to match a modular form of very small level, which one shows cannot exist — a contradiction. This program, developed by Darmon, Merel, Bennett, Skinner, Kraus, Siksek and others, has resolved many specific signatures.

*Best results.* Equal-exponent families and many mixed cases are settled: $(n,n,n)$ is FLT; $(n,n,2)$ and $(n,n,3)$ are handled by Darmon–Merel (1997) and Bennett–Skinner-type arguments; numerous individual triples such as $(2,3,n)$ (Catalan-type, partly via Poonen–Schaefer–Stoll and Chen, Siksek, Dahmen) and small fixed exponents are known. Within the strict Beal range $x,y,z>2$, every signature with two equal exponents in the resolved families is covered.

*Barrier.* The method is essentially **one signature at a time**. Each new triple typically demands its own Frey curve, its own modularity input (often over a real quadratic or other number field, where modularity is harder), and its own elimination of residual newforms. There is no uniform Frey curve covering all $(p,q,r)$ with $\chi<1$, so the method does not, as presently understood, reach the infinitely many exponent triples that Beal requires.

## Finiteness via Faltings (Darmon–Granville)

For each *fixed* signature $(p,q,r)$ with $\chi<1$, the equation $A^p+B^q=C^r$ defines (after passage to a suitable cover) a curve of genus $\ge 2$; **Faltings' theorem** then gives finitely many coprime solutions. This is the Darmon–Granville theorem (1995).

*Best result.* Unconditional finiteness for every fixed hyperbolic triple, hence for Beal restricted to any bounded exponent set.

*Barrier.* Faltings is **ineffective**: it bounds the *number* of solutions but yields no computable height bound, so one cannot in general enumerate or exclude them. Worse, finiteness per triple says nothing across the infinitely many triples; it does not even bound the bases uniformly.

## The $abc$ conjecture and Diophantine inequalities

The $abc$ conjecture of Masser and Oesterlé implies the Beal Conjecture **for all but finitely many** solutions, and with an explicit-enough form of $abc$ would settle it entirely. The mechanism: a coprime solution with large exponents has very smooth (high-power) terms, contradicting the radical bound $c \ll_\varepsilon \operatorname{rad}(abc)^{1+\varepsilon}$.

*Best result.* Conditional on $abc$, Beal holds up to finitely many exceptions; combined with the known finiteness per triple this is close to a conditional proof.

*Barrier.* The $abc$ conjecture is itself open. Shinichi Mochizuki's claimed proof via inter-universal Teichmüller theory remains **disputed**: it was published in *PRIMS* (2021) but is not accepted by the wider community, with a specific gap identified by Scholze and Stix (2018). No unconditional, effective $abc$ bound strong enough for Beal exists.

## Descent and explicit Chabauty–Coleman

For individual signatures where the relevant curve has small genus or special structure, **descent** and **Chabauty–Coleman** (and its quotient/elliptic-curve Chabauty refinements) can provably determine *all* rational points, hence all solutions. Bruin, Poonen, Schaefer, Stoll, Siksek and collaborators used these to finish signatures such as $(2,3,8)$, $(2,3,7)$ (the Klein quartic), $(2,4,5)$, and others.

*Best result.* Complete resolution of several otherwise-intractable individual cases, often where the modular method stalls on residual forms.

*Barrier.* These methods require the rank of the relevant Jacobian (or a quotient) to be strictly less than its dimension, and substantial case-specific computation. They do not scale to families with growing exponent.

## Computation and verification

Large-scale search has verified no coprime counterexample exists within wide bounds (historically, bases up to $1000$ and exponents up to large limits in independent searches by Norvig and others).

*Best result.* Strong empirical support and confirmation that no small counterexample exists; useful for ruling out specific residual signatures.

*Barrier.* Computation can only refute, never prove, the conjecture; the search space is infinite in both bases and exponents.

## Summary of obstructions

The recurring obstruction is **uniformity**: every effective method is anchored to a fixed exponent signature, while Beal ranges over infinitely many. Bridging that gap appears to require either an unconditional effective $abc$, a uniform Frey-type construction, or a genuinely new idea. The ineffectivity of Faltings and the unresolved status of $abc$ together explain why a problem so close to FLT has resisted a general proof.
