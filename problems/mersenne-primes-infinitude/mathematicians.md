# Top Mathematicians — Infinitude of Mersenne Primes

The figures below shaped either the problem itself, the tools used to attack it, or the heuristics that frame current belief. All are well-documented historical or contemporary mathematicians.

| # | Name | Era | Role | Key contribution |
|---|------|-----|------|------------------|
| 1 | Euclid | c. 300 BCE | originator | Proved (*Elements* IX.36) that $2^p-1$ prime implies $2^{p-1}(2^p-1)$ perfect, founding the perfect-number link. |
| 2 | Marin Mersenne | 1588–1648 | originator | Stated the 1644 list of prime exponents $p\le257$; gave the sequence its name and the problem its initial data. |
| 3 | Leonhard Euler | 1707–1783 | breakthrough | Proved $M_{31}$ prime; proved every even perfect number has Euclid's form (converse to Euclid). |
| 4 | Édouard Lucas | 1842–1891 | breakthrough | Devised the Lucas-sequence primality criterion; proved $M_{127}$ prime by hand. |
| 5 | Frank Nelson Cole | 1861–1926 | breakthrough | Factored $M_{67}$ (1903), the famous "lecture without words," refuting Mersenne's list. |
| 6 | Derrick H. Lehmer | 1905–1991 | breakthrough | Formalized the Lucas–Lehmer test, the deterministic engine of all modern searches. |
| 7 | Raphael M. Robinson | 1911–1995 | breakthrough | Programmed the SWAC to find five new Mersenne primes (1952), opening the computer era. |
| 8 | Samuel S. Wagstaff Jr. | b. 1945 | frontier | Co-author of the density heuristic and the New Mersenne Conjecture; theory of divisors of $M_p$. |
| 9 | Carl Pomerance | b. 1944 | frontier | Co-developed the Lenstra–Pomerance–Wagstaff heuristic predicting infinitude and density. |
| 10 | George Woltman | b. 1957 | expositor | Founded GIMPS (1996) and wrote Prime95, the software behind 18+ record Mersenne primes. |

## Notes

The problem today has two largely disjoint active communities. On the **theoretical** side there is essentially no specialized "Mersenne infinitude" research program, because the question is recognized as beyond current methods; relevant progress is indirect and lives in analytic number theory (sieve theory, primes in thin and structured sequences, Artin's conjecture and the order of $2$ modulo $q$), where figures such as Pomerance, Wagstaff, and researchers in the Maynard–Tao tradition advance the surrounding terrain without targeting Mersenne primes directly. On the **computational** side the activity is intense and well-organized through GIMPS, coordinated by George Woltman (Prime95), Scott Kurowski and Aaron Blosser (PrimeNet server infrastructure), with major recent advances from contributors who ported testing to GPUs — Luke Durant's 2024 discovery of $M_{136279841}$ being the first GPU-found Mersenne prime. Algorithmic refinements (Gerbicz/Pietrzak error checking, probable-prime tests, fast FFT and NTT multiplication) come from a small expert pool around the GIMPS forums and the Lucas–Lehmer–Riesel/PRP testing literature. The two communities meet only at the heuristics, which the computational record continues to corroborate without bringing a proof any closer.
