# History — Existence of Odd Perfect Numbers

A positive integer $n$ is **perfect** if it equals the sum of its proper divisors, equivalently if $\sigma(n) = 2n$ where $\sigma$ is the sum-of-divisors function. The four perfect numbers known to antiquity — $6, 28, 496, 8128$ — are all even, and the question of whether any **odd** perfect number (OPN) exists is among the oldest unresolved problems in mathematics.

## Origin and formulation

The notion of a perfect number is set down in Book IX, Proposition 36 of Euclid's *Elements* (c. 300 BCE), which proves that if $2^p - 1$ is prime then $2^{p-1}(2^p - 1)$ is perfect. This furnishes only even perfect numbers. Nicomachus of Gerasa, in his *Introduction to Arithmetic* (c. 100 CE), classified numbers as deficient, perfect, or abundant and asserted (without proof) several properties of perfect numbers that implicitly suggested all were even and ended alternately in 6 and 8. The OPN question is the natural complement to Euclid's construction: does the even family exhaust all perfect numbers?

The modern formulation is sharp. By Euler's theorem an odd perfect number must have the form
$$ n = p^{\alpha} m^2, \qquad p \equiv \alpha \equiv 1 \pmod 4, $$
where $p$ is a prime (the **special** or **Euler prime**) not dividing $m$. The problem is to prove no such $n$ exists, or to exhibit one.

## Timeline

- **c. 300 BCE** — Euclid (*Elements* IX.36) proves $2^{p-1}(2^p-1)$ is perfect when $2^p-1$ is prime; only even examples produced.
- **c. 100 CE** — Nicomachus states (unproven) structural claims about perfect numbers, implicitly framing the even-only expectation.
- **1638** — Descartes, in correspondence with Mersenne, gives the first serious analysis of OPNs and proposes the near-miss "Descartes number" $D = 3^2 \cdot 7^2 \cdot 11^2 \cdot 13^2 \cdot 22021$, perfect if $22021$ were prime (it is $19^2 \cdot 61$). He suspects no OPN exists.
- **1747** — Euler proves the converse of Euclid (every even perfect number has Euclid's form) and establishes the **Euler form** $p^\alpha m^2$ with $p \equiv \alpha \equiv 1 \pmod 4$ for any OPN.
- **1888** — Sylvester intensifies study, showing an OPN must have at least 4 (later 5) distinct prime factors and popularizes the "web of conditions" strategy: "a prolonged meditation... will not be altogether lost."
- **1913** — Carmichael and others extend the distinct-prime-factor and congruence constraints.
- **1937** — Steuerwald proves an OPN cannot have all non-special exponents equal to 1 (it cannot be of the form $p^\alpha q_1^2 q_2^2 \cdots q_k^2$ with every $q_i$ to the second power and the special prime to the first), an early "the exponents cannot all be small" result.
- **1973** — Hagis and McDaniel; and independently work raising the lower bound on the largest prime factor; Hagis–McDaniel show the largest prime factor exceeds $10^5$.
- **1973** — Hagis proves an OPN has at least 8 distinct prime factors.
- **1980** — Hagis and Cohen / subsequent computations push the lower bound on the magnitude of any OPN past $10^{50}$.
- **1991** — Brent, Cohen, and te Riele establish $n > 10^{300}$ by a large factor-chain computation.
- **2003** — Iannucci, and later Hagis–Cohen, pin down lower bounds on the three largest prime factors.
- **2006–2008** — Nielsen proves an OPN has at least 9 distinct prime factors; Goto and Ohno show the largest prime factor exceeds $10^8$.
- **2012** — Ochem and Rao prove $n > 10^{1500}$ and that the largest component (prime power) exceeds $10^{62}$.
- **2015** — Nielsen proves an OPN must have at least **10 distinct prime factors** (the current unconditional record).
- **2018–present** — Continued refinement: bounds on the second/third largest prime factors (Zelinsky, Konyagin–Pomerance directions), and "spoof" perfect number studies (Nielsen et al.) probing why no genuine OPN appears.

The cumulative effect is a vast, mutually reinforcing system of constraints — yet no contradiction, and no example. The problem remains open.

(Word count ≈ 640.)
