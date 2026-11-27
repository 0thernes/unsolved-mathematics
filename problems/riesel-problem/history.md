# History — The Riesel Problem

_Origin, formulation, and timeline._

In 1956, Swedish mathematician Hans Riesel proved that there are infinitely many odd integers $k$ such that $k \cdot 2^n - 1$ is composite for *every* positive integer $n \ge 1$, exhibiting the explicit witness $k = 509{,}203$ via the finite **covering system** of congruences $\{0 \pmod 2, 0 \pmod 3, 1 \pmod 4, 3 \pmod 8, 7 \pmod{12}, 23 \pmod{24}\}$ corresponding to the prime divisors $\{3, 5, 7, 13, 17, 241\}$. (Four years later, Wacław Sierpiński proved the sibling $+1$ theorem for $k \cdot 2^n + 1$, where John Selfridge found the conjectured smallest Sierpiński number $k = 78{,}557$ in 1962.)

The **Riesel problem** (tracked as OEIS `A108129` and formalized in Lean 4 in `google-deepmind/formal-conjectures` as `OeisA108129.conjecture`) asks whether **$509{,}203$ is the smallest Riesel number**. To confirm this, one must exhibit at least one prime of the form $k \cdot 2^n - 1$ for every odd $k < 509{,}203$. Over 70 years of distributed computing (most notably Wilfrid Keller's tracking and the **PrimeGrid** Riesel Problem subproject), the initial pool of $254{,}601$ odd candidates below $509{,}203$ has been whittled down to **41 remaining stubborn $k$ values** (starting with $k = 23669, 31859, 38473, \dots$), each tested past $n > 10^7$ without yet yielding a prime.

## Timeline

- **1950** — Paul Erdős introduces covering systems of congruences, the algebraic engine behind Riesel and Sierpiński numbers.
- **1956** — Hans Riesel discovers $k = 509{,}203$ and proves there are infinitely many Riesel numbers (all $k \equiv 509{,}203 \pmod{11{,}184{,}810}$).
- **1960–1962** — Wacław Sierpiński proves infinitely many $k \cdot 2^n + 1$ are always composite; John Selfridge exhibits $k = 78{,}557$ (the sibling Sierpiński problem).
- **1997–2003** — Keller, Gallot, and distributed volunteers launch systematic sieving and Lucas–Lehmer–Riesel (LLR) primality testing (`Riesel Sieve`, later merged into `PrimeGrid`).
- **2015** — Bob Hough solves Erdős's minimum-modulus covering-system problem (`10.4007/annals.2015.181.1.6`, `arXiv:1307.0874`), proving every covering system has minimum modulus $\le 10^{16}$ and showing why constructing *new* covering-system Riesel witnesses is far rarer than once imagined.
- **2015–2026** — PrimeGrid eliminates candidates one by one via multi-million-digit mega-primes (reaching exponents $n > 15{,}000{,}000$), leaving **41** uneliminated odd $k < 509{,}203$ (beginning with $k = 23669, 31859, 38473$; unchanged since late 2017 per Wilfrid Keller's tracking).
