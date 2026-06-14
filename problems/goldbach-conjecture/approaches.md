# Approaches — Goldbach's Conjecture

_Major strategies, partial results, and barriers._

## The Circle Method (Hardy–Littlewood–Vinogradov)

The dominant analytic tool. Write the number of representations of $n$ as a sum of $k$ primes as a Fourier integral $r_k(n)=\int_0^1 S(\alpha)^k e(-n\alpha)\,d\alpha$, where $S(\alpha)=\sum_{p\le n} e(p\alpha)$ is an exponential sum over primes. One partitions $[0,1]$ into **major arcs** (near rationals with small denominator), where $S(\alpha)$ is estimated via the prime-counting machinery / Siegel–Walfisz and contributes the expected singular series, and **minor arcs**, where one needs strong cancellation. The method delivers the asymptotic for $r_3(n)$ and hence the **ternary** Goldbach problem.

- **Best result:** Vinogradov (1937) proved every sufficiently large odd $n$ is a sum of three primes unconditionally; Helfgott (2013) closed the remaining gap to *all* odd $n>5$, completing the weak conjecture, by sharpening minor-arc bounds and certifying the major arcs with verified computation (Platt).
- **Barrier for the binary problem:** for $k=2$ the integral is dominated by the minor arcs, where the available cancellation in $S(\alpha)^2$ is insufficient. There is no known way to control the binary minor-arc integral; the method gives the *average* (almost-all) result but not every even $n$. This is the central obstruction.

## Sieve Methods (Brun, Selberg, and the parity problem)

Sieves count integers (or prime pairs) by inclusion–exclusion with smoothed weights. Brun's sieve (1920) first produced finite upper bounds and "almost-prime" theorems; the Selberg sieve and the linear sieve of Rosser–Iwaniec gave the sharpest tools, culminating in Chen's theorem.

- **Best result:** **Chen's theorem (1973):** every sufficiently large even integer is $p + P_2$, where $P_2$ has at most two prime factors. This is the closest unconditional approximation to "$p+p$".
- **Barrier — the parity problem (Selberg).** Pure sieve methods cannot distinguish numbers with an even number of prime factors from those with an odd number. A sieve that could prove $n=p_1+p_2$ would have to break parity, and Selberg's parity obstruction shows classical sieves alone cannot reach exactly two prime factors on both summands. Chen's $1+2$ sits right at this wall; pushing to $1+1$ requires genuinely new input beyond sieve theory.

## Schnirelmann Density / Additive Bases

Schnirelmann (1930) showed the set of primes (plus 0,1) has positive Schnirelmann density after adding, so it forms an additive basis of finite order: every integer $>1$ is a sum of at most $C$ primes.

- **Best result:** Schnirelmann's constant has been driven down to **at most 6 primes** for all even integers (Ramaré, 1995), and follows from Helfgott's ternary theorem that every even number is a sum of at most 4 primes; every odd from 3. (The strong conjecture asserts the answer is 2 for evens.)
- **Barrier:** density arguments are inherently lossy — they bound the *number* of summands, not their structure, and cannot by themselves reach the sharp value 2.

## Exceptional-Set / Almost-All Estimates

Rather than every even number, bound the count $E(X)=\#\{n\le X:\ n\ \text{even},\ n\neq p+q\}$.

- **Best result:** Montgomery–Vaughan (1975) proved $E(X)=O(X^{1-\delta})$ for some explicit $\delta>0$; subsequent work (Pintz and others) has improved the savings, with $\delta$ now around $0.7$ in the literature. Thus the conjecture holds for **almost all** even integers, with a power-saving exceptional set.
- **Barrier:** improving $E(X)$ to $0$ (i.e. to finitely many exceptions, then none) appears to require the same minor-arc control the binary circle method lacks; an unconditional $E(X)=O(1)$ would essentially be the conjecture.

## Conditional Approaches (GRH and beyond)

Under the **Generalized Riemann Hypothesis** the major-arc estimates sharpen dramatically. GRH yields the ternary theorem for all $n$ cheaply (this was the original Hardy–Littlewood route) and improves exceptional-set bounds for the binary problem, but **does not** by itself prove binary Goldbach — the minor-arc obstruction persists even under GRH.

## Computational Verification

Direct verification certifies the conjecture up to a height, supplying the "small cases" that analytic theorems leave out (crucial to Helfgott's proof) and testing heuristics.

- **Best result:** Oliveira e Silva, Herzog, and Pardi verified the strong conjecture for all even $n\le 4\times10^{18}$.
- **Barrier:** computation can never settle an asymptotic statement; it complements, not replaces, proof.
