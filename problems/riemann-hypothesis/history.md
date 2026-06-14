# History — The Riemann Hypothesis

_Origin, formulation, and timeline._

## How the problem arose

The hypothesis emerged from a single eight-page memoir, Bernhard Riemann's 1859 paper *"Über die Anzahl der Primzahlen unter einer gegebenen Größe"* ("On the number of primes less than a given magnitude"), submitted on the occasion of his election to the Berlin Academy. Riemann's goal was an exact formula for the prime-counting function $\pi(x)$. Following Euler, who had connected the series $\sum n^{-s}$ to the primes via the product $\zeta(s)=\prod_p (1-p^{-s})^{-1}$, Riemann took the decisive step of treating $s$ as a *complex* variable. He showed that $\zeta(s)$, defined for $\Re(s)>1$, extends to a meromorphic function on the whole plane with a single pole at $s=1$, and satisfies a functional equation relating $s$ and $1-s$, symmetric about the line $\Re(s)=\tfrac12$.

Riemann's explicit formula expresses $\pi(x)$ in terms of a sum over the non-trivial zeros $\rho$ of $\zeta$. The error in the prime-number approximation is controlled precisely by the real parts of these zeros. The "trivial" zeros lie at the negative even integers $-2,-4,\dots$; all other ("non-trivial") zeros lie in the critical strip $0<\Re(s)<1$. Riemann remarked, almost in passing, that it is "very probable" (*sehr wahrscheinlich*) that all of them lie on the critical line $\Re(s)=\tfrac12$, adding that he had set aside the search for a proof. That remark is the Riemann Hypothesis (RH).

## Formulation and reformulations

**Standard form.** Every non-trivial zero $\rho$ of $\zeta(s)$ satisfies $\Re(\rho)=\tfrac12$.

**Equivalent statements.** RH is equivalent to the prime-counting bound $\pi(x)=\operatorname{li}(x)+O(\sqrt{x}\log x)$; to the Mertens-type bound $M(x)=\sum_{n\le x}\mu(n)=O(x^{1/2+\varepsilon})$; to the sum-of-divisors bound $\sigma(n)<e^{\gamma} n\log\log n$ for $n>5040$ (Robin's criterion); and to positivity of the Li/Keiper coefficients. The Generalized RH (GRH) extends the claim to Dirichlet $L$-functions, and the Grand RH to all automorphic $L$-functions.

## Timeline

- **1737** — Euler proves the product formula $\zeta(s)=\prod_p(1-p^{-s})^{-1}$, linking $\zeta$ to the primes.
- **1859** — Riemann's memoir introduces complex $\zeta(s)$, the functional equation, the explicit formula, and the conjecture.
- **1896** — Hadamard and de la Vallée Poussin independently prove the Prime Number Theorem by showing $\zeta(1+it)\ne 0$.
- **1901** — von Koch shows RH is equivalent to the sharp error term $\pi(x)=\operatorname{li}(x)+O(\sqrt{x}\log x)$.
- **1914** — Hardy proves infinitely many zeros lie exactly on the critical line; Bohr–Landau give density results.
- **1914** — Littlewood proves $\pi(x)-\operatorname{li}(x)$ changes sign infinitely often, refuting numerical expectations.
- **1942** — Selberg proves a positive proportion of zeros lie on the line.
- **1948–49** — Selberg and Erdős give "elementary" proofs of the PNT.
- **1972** — Montgomery formulates the pair-correlation conjecture; Dyson notes the link to random-matrix (GUE) statistics.
- **1974** — Levinson shows at least one third of zeros lie on the line; later improved by Conrey (1989) to over two fifths.
- **1986** — van de Lune, te Riele, Winter verify the first $1.5\times10^9$ zeros on the line.
- **2000** — RH named a Clay Millennium Prize Problem ($1,000,000).
- **2004** — Conrey, Farmer, Keating, Rubinstein, Snaith give random-matrix predictions for moments of $\zeta$.
- **2004** — Gourdon and Demichel verify the first $10^{13}$ zeros computationally.
- **2018** — Bombieri and Sarnak frame the Hilbert–Pólya program in modern terms; Platt and Trudgian extend rigorous zero-free verifications.
- **Present** — RH remains open; the strongest unconditional zero-free regions and the Bombieri–Lagarias/Newman de Bruijn constant program ($\Lambda\ge 0$, proven by Rodgers–Tao 2020) mark the frontier.
