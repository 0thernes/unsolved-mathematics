# History — The Beal Conjecture

The Beal Conjecture asserts that the Diophantine equation
$$A^x + B^y = C^z,\qquad x,y,z>2,\ A,B,C\in\mathbb{Z}^{+},$$
has no solution in which $A$, $B$, and $C$ are pairwise coprime — equivalently, that any solution forces $A$, $B$, $C$ to share a common prime factor. It generalizes Fermat's Last Theorem (FLT): setting $x=y=z=n\ge 3$ recovers the FLT equation, and FLT (proved by Andrew Wiles, 1995) is exactly the equal-exponent, coprime case.

The conjecture grew out of computational number theory rather than from inside academia. Around 1993, **Andrew Beal**, a Dallas banker and self-taught number theorist, was experimenting with the FLT equation on computers. He observed that whenever $A^x+B^y=C^z$ held with all exponents exceeding 2, the bases shared a factor — the canonical example being $3^3 + 6^3 = 3^5$ (since $27+216=243$), where $3$ divides every base. He conjectured that the coprime case is impossible. Beal communicated the problem to several number theorists, including **R. Daniel Mauldin** of the University of North Texas, who published it for the wider community in a 1997 *Notices of the AMS* article, "A Generalization of Fermat's Last Theorem: The Beal Conjecture and Prize Problem," which also announced a cash prize Beal had endowed.

The conjecture is tied to the family of generalized Fermat equations $A^p+B^q=C^r$, organized by the inverse-exponent sum $\chi=\tfrac1p+\tfrac1q+\tfrac1r$. When $\chi>1$ (the "spherical" case) there are infinitely many coprime solutions; when $\chi=1$ (the "Euclidean" case, e.g. $(3,3,3),(2,3,6),(2,4,4)$) finitely many; and when $\chi<1$ (the "hyperbolic" case) the Darmon–Granville theorem (1995), via Faltings' theorem, gives finitely many coprime solutions for each fixed triple. Beal's condition $x,y,z>2$ forces $\chi\le 1$, with equality only at $(3,3,3)$, so the conjecture lives entirely in the hyperbolic regime plus that single Euclidean triple. A more general statement — the **Fermat–Catalan conjecture** of Darmon and Granville — predicts only finitely many coprime solutions across all triples with $\chi<1$; the ten known such solutions all involve an exponent equal to 2, and so all violate Beal's $x,y,z>2$ hypothesis, consistent with Beal.

The prize history made the problem unusually public. Beal initially offered \$5{,}000 (1997), raised it in stages, and in **2013** set it at **\$1{,}000{,}000**, administered by the American Mathematical Society, which holds the funds in trust and adjudicates submissions. The large prize drew amateur submissions in volume; none has survived refereeing.

## Timeline

- **1637** — Pierre de Fermat states FLT in the margin of his Diophantus, the historical root of the equal-exponent case.
- **1993** — Andrew Beal, experimenting computationally on FLT-type equations, formulates the coprimality conjecture and begins circulating it.
- **1994–95** — Wiles, with Taylor, completes the proof of FLT, settling the equal-exponent coprime case $x=y=z=n\ge 3$.
- **1995** — Darmon and Granville prove that $A^p+B^q=C^r$ with $\tfrac1p+\tfrac1q+\tfrac1r<1$ has finitely many coprime solutions for each fixed $(p,q,r)$, via Faltings.
- **1997** — Mauldin publishes the conjecture and Beal's prize in the *Notices of the AMS*, fixing the name "Beal Conjecture."
- **1997** — Darmon and Loïc Merel resolve $A^n+B^n=2C^n$ and related ternary equations, extending the modular method.
- **2000s** — Modular-method case studies (Bennett, Skinner, Kraus, Bruin, Poonen, Siksek, and others) resolve many individual signatures $(p,q,r)$, including infinite families such as $(n,n,2)$ and $(n,n,3)$.
- **2013** — Beal raises the prize to \$1{,}000{,}000, administered by the AMS; press coverage renews public attention.
- **2010s–2020s** — Frey-curve and level-lowering methods plus large-scale computation extend coverage of small exponent signatures; the general coprime case remains open.
- **present** — No general proof or counterexample; the conjecture stands as a flagship open problem in Diophantine number theory, with progress confined to specific exponent families.
