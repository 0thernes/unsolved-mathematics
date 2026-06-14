# History — Goldbach's Conjecture

_Origin, formulation, and timeline._

## Origin

The conjecture was born in correspondence. On 7 June 1742, the Prussian-born mathematician and diplomat Christian Goldbach wrote from Moscow to Leonhard Euler, then in Berlin, proposing — in a marginal afterthought to a letter chiefly about other matters — that **every integer greater than 2 can be written as a sum of three primes**. Goldbach worked with the convention then current that $1$ is prime, which is essential to reading his original statements correctly. In his reply of 30 June 1742, Euler reformulated and sharpened the idea, stating what we now call the **strong (binary) Goldbach conjecture**: every even integer greater than 2 is a sum of two primes. Euler remarked that he regarded this as "a wholly certain theorem" ("ein ganz gewisses Theorema") despite being unable to prove it.

## Formulations

Three statements circulate, and the relations among them matter:

- **Strong (binary) Goldbach:** every even $n > 2$ equals $p + q$ with $p,q$ prime. This is the modern headline statement and the one in this dossier's metadata.
- **Weak (ternary, odd) Goldbach:** every odd $n > 5$ is a sum of three primes.
- **Goldbach's original "every integer $> 2$ is a sum of three primes":** under the old convention $1\in\mathbb{P}$, this is equivalent to the modern strong form for evens (write $2k = (2k-1)+1$ etc.) and is what historically motivated both.

The strong form **implies** the weak form: if every even number is $p+q$, then any odd $n>5$ is $3+(n-3)$ with $n-3$ even $>2$. The weak form does not imply the strong. Heuristically, the Hardy–Littlewood circle-method asymptotic predicts the number $r(n)$ of representations of even $n$ grows like $r(n)\sim 2\,\Pi_2 \prod_{p\mid n,\,p>2}\frac{p-1}{p-2}\cdot\frac{n}{(\log n)^2}$, so representations become abundant — the conjecture is "true with enormous room to spare," yet no proof exists.

## Timeline

- **1742** — Goldbach's letter to Euler (7 June); Euler's reply (30 June) sharpens it to the binary even statement.
- **1855** — Desboves verifies the conjecture numerically up to $10^4$; later hand computations push the bound further.
- **1900** — Hilbert lists Goldbach (with twin primes and others) under his **8th problem** at the ICM, anchoring it in the modern research program.
- **1912** — Landau, at the ICM in Cambridge, calls Goldbach one of the problems "unattackable in the present state of science."
- **1920** — Viggo Brun introduces his **sieve**, the first method to give nontrivial upper bounds on Goldbach-type representations and "almost prime" results.
- **1923** — Hardy and Littlewood, using the **circle method** under GRH, prove a conditional asymptotic for the ternary problem and conjecture the quantitative form of the binary problem.
- **1930** — Lev Schnirelmann proves every integer $>1$ is a sum of a bounded number of primes (the **Schnirelmann constant**), the first unconditional density attack.
- **1937** — **Vinogradov** removes the GRH hypothesis: every sufficiently large odd integer is a sum of three primes. Borozdkin (1956) and later work make the threshold explicit.
- **1938** — Estermann, and independently others, show **almost all** even integers satisfy Goldbach (exceptional set of density zero).
- **1947** — Rényi proves a "$1+K$" theorem: every large even number is $p + (\text{almost prime})$.
- **1966** — **Chen Jingrun** announces the celebrated **"$1+2$"** result; full proof published 1973: every sufficiently large even integer is $p + P_2$, with $P_2$ having at most two prime factors. This remains the strongest approximation to the binary conjecture.
- **1975** — Montgomery and Vaughan give explicit bounds on the exceptional set: the count of even $n\le X$ failing Goldbach is $O(X^{1-\delta})$.
- **1995** — Ramaré proves every even integer is a sum of at most **6 primes**, sharpening Schnirelmann's constant.
- **2002** — Liu and Wang, and others, lower the explicit threshold for the ternary problem.
- **2012–2013** — **Harald Helfgott** proves the **ternary (weak) Goldbach conjecture unconditionally and completely**, for all odd $n>5$, combining refined circle-method bounds with massive verified computation (with David Platt).
- **2013–present** — **Tomás Oliveira e Silva** et al. verify the strong conjecture computationally up to $4\times10^{18}$; the binary conjecture remains **open**.
