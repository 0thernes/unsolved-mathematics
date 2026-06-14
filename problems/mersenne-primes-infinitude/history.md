# History — Infinitude of Mersenne Primes

A *Mersenne number* is an integer of the form $M_n = 2^n - 1$; a *Mersenne prime* is one that is prime. An elementary lemma forces the exponent to be prime: if $n = ab$ with $a,b > 1$, then $2^a - 1$ divides $2^n - 1$, so $M_n$ can be prime only when $n = p$ is prime. The central open problem asks:

> **Are there infinitely many primes of the form $2^p - 1$?**

The converse — that $2^p - 1$ is prime whenever $p$ is prime — is false ($2^{11} - 1 = 23 \cdot 89$), so the question concerns a sparse, irregular subsequence. The problem is widely believed to have an affirmative answer; the *Lenstra–Pomerance–Wagstaff heuristic* predicts roughly $e^{\gamma}\log_2 x$ Mersenne primes with exponent $p \le x$ — hence infinitely many, with about $e^{\gamma}/\log 2 \approx 2.57$ new Mersenne-prime exponents per doubling of $p$. No proof of infinitude (or of finitude) exists.

The subject predates Mersenne. Euclid (c. 300 BCE, *Elements* IX.36) proved that if $2^p - 1$ is prime then $2^{p-1}(2^p-1)$ is perfect, tying Mersenne primes to perfect numbers — a link that motivated the search for centuries. In 1644, in the preface to his *Cogitata Physico-Mathematica*, Marin Mersenne asserted that $2^p - 1$ is prime exactly for $p \in \{2,3,5,7,13,17,19,31,67,127,257\}$ and composite for all other $p \le 257$. His list was both incomplete and erroneous, but it framed the modern problem and attached his name to it.

The decisive theoretical tool arrived with Édouard Lucas (1876–1878), who developed a primality criterion from Lucas sequences and verified by hand that $M_{127} = 2^{127} - 1$ is prime — a 39-digit number that remained the largest known prime until 1952. Derrick H. Lehmer (1930) refined Lucas's criterion into the modern **Lucas–Lehmer test**: for odd prime $p$, $M_p$ is prime iff $s_{p-2} \equiv 0 \pmod{M_p}$, where $s_0 = 4$ and $s_{k+1} = s_k^2 - 2$. This deterministic, near-quadratic-time test is what makes Mersenne primes the perennial record-holders: testing $M_p$ is far cheaper than testing a generic number of the same size.

## Timeline

- **c. 300 BCE** — Euclid (*Elements* IX.36) links Mersenne primes to even perfect numbers.
- **1644** — Marin Mersenne publishes his list of prime exponents $p \le 257$ in *Cogitata Physico-Mathematica*.
- **1750** — Leonhard Euler proves $M_{31}$ prime; it remains the largest known prime for over a century.
- **1849** — Euler's converse to Euclid (posthumous): every *even* perfect number has Euclid's form, completing the equivalence.
- **1876** — Édouard Lucas proves $M_{127}$ prime via Lucas sequences; the record stands until 1952.
- **1883** — Ivan Pervushin shows $M_{61}$ prime, an exponent Mersenne had omitted (first confirmed gap in the list).
- **1903** — Frank Nelson Cole factors $M_{67} = 193{,}707{,}721 \cdot 761{,}838{,}257{,}287$, refuting Mersenne's claim that it is prime.
- **1911–1914** — $M_{89}$ and $M_{107}$ found prime (Powers, Fauquembergue), further correcting Mersenne.
- **1930** — D. H. Lehmer formalizes the **Lucas–Lehmer test**.
- **1947** — The range $p \le 257$ is fully checked; Mersenne's list is found to have five errors and three omissions.
- **1952** — Raphael Robinson uses the SWAC computer to find five new Mersenne primes ($M_{521}, M_{607}, M_{1279}, M_{2203}, M_{2281}$), opening the computer era.
- **1963** — Donald Gillies finds $M_{11213}$; Illinois franks departmental mail "$2^{11213}-1$ is prime."
- **1980** — Wagstaff articulates the **Lenstra–Pomerance–Wagstaff heuristic**, predicting infinitude and density.
- **1996** — George Woltman founds **GIMPS** (Great Internet Mersenne Prime Search), a distributed-computing effort.
- **1999–2008** — GIMPS finds the first million-digit ($M_{6972593}$) and ten-million-digit ($M_{43112609}$) primes; the latter wins a \$100{,}000 EFF Cooperative Computing Award.
- **2016–2018** — $M_{74207281}$, then $M_{77232917}$, then $M_{82589933}$ are discovered.
- **2024 (October)** — $M_{136279841}$, a 41{,}024{,}320-digit number, becomes the 52nd known Mersenne prime and the largest known prime, found by Luke Durant via GIMPS on GPU hardware.

Despite 380 years of computation, the infinitude question remains entirely open: every result to date is an existence statement about a *specific* prime, not a proof that the sequence never terminates.
