# Approaches — The abc Conjecture

_Major strategies, partial results, and barriers._

The abc conjecture has resisted every classical tool. The unconditional bounds remain *exponentially* far from the truth, while the strategies that would close the gap are either conjectural themselves or, in the most ambitious case, disputed. Below are the principal lines of attack.

## Baker's method (linear forms in logarithms)

The only approach to have produced *unconditional* progress. By bounding linear forms $\Lambda = b_1\log\alpha_1+\cdots+b_n\log\alpha_n$ from below (Baker, Wüstholz; $p$-adic forms via Yu Kunrui), one controls how closely a smooth number can approximate another, hence how large $c$ can be relative to $\mathrm{rad}(abc)$.

- **Best result:** Stewart–Yu (1991, 2001) proved $\log c \ll_\varepsilon \mathrm{rad}(abc)^{1/3+\varepsilon}$, with later refinements of the constants.
- **Barrier:** The method is intrinsically *exponential* — it bounds $\log c$ by a power of $\mathrm{rad}(abc)$, whereas the conjecture demands $\log c \ll \log \mathrm{rad}(abc)$. The gap is not a matter of constants; linear forms in logarithms cannot, even in principle, reach a polynomial-in-$\log$ bound. This is a fundamental ceiling on the technique.

## The Frey curve / Szpiro reduction

abc is essentially equivalent to a uniform **Szpiro inequality** $|\Delta_E| \ll N_E^{6+\varepsilon}$ for elliptic curves, via the Frey curve attached to a triple. This recasts the problem in arithmetic geometry, where one may deploy modularity, Galois representations, and the theory of conductors and discriminants.

- **Best result:** The equivalence is exact, and modularity (Wiles, Taylor–Wiles, BCDT) makes the elliptic-curve side fully systematic — but proving the *uniform* Szpiro bound is exactly as hard as abc.
- **Barrier:** No mechanism in the modularity toolkit produces the required uniformity over all curves; one only re-encodes the difficulty.

## Vojta's conjectures and the Nevanlinna dictionary

Vojta embedded abc into a vast height-inequality program mirroring the Second Main Theorem of value-distribution theory: the radical plays the role of a truncated counting function, and abc becomes a special case of a conjectural arithmetic SMT for curves and higher-dimensional varieties.

- **Best result:** The *function-field* and *holomorphic* analogues are theorems (Mason–Stothers; the holomorphic abc / SMT of Nevanlinna–Cartan). These give complete proofs in the geometric setting.
- **Barrier:** The arithmetic case lacks a derivative. Function-field and Nevanlinna proofs use a Wronskian/logarithmic-derivative that has no integer counterpart; transplanting the proof founders precisely there. Vojta's full conjecture is strictly harder than abc.

## Inter-universal Teichmüller theory (IUT) — Mochizuki

Shinichi Mochizuki's program (2012) attacks a Szpiro-type inequality by deforming the multiplicative and additive structures of a number field across "distinct universes," tracking the distortion via the theory of Hodge theaters, theta-links, and the multiradial algorithm. The claimed payoff (Corollary 3.12) is an inequality yielding abc.

- **Claimed result:** A full proof of abc (and Szpiro, Vojta-for-curves) with effective constants.
- **Barrier / dispute:** **Scholze and Stix (2018)** argue that the central inequality of Corollary 3.12 either is unjustified or collapses to a triviality once certain identifications are made explicit; they contend a crucial "log-volume" comparison loses the needed quantitative content. Mochizuki rejects this reading. The proof has **not** achieved independent community validation and is treated as unverified. This is a genuine, open dispute, not a settled refutation.

## Elementary / probabilistic and computational heuristics

Conjectural sharpenings (Robert–Stewart–Tenenbaum) predict the precise extremal shape, $\log c < \log\mathrm{rad}(abc) + O\!\big(\sqrt{\log\mathrm{rad}}/\log\log\mathrm{rad}\big)$, refining how the $\varepsilon$ should behave.

- **Best result:** Massive computation (ABC@home, Reken mee met ABC) verifies abc for all triples up to large bounds and supplies the highest-quality known triples — e.g. $q \approx 1.6299$ for $2 + 3^{10}\cdot109 = 23^5$.
- **Barrier:** Heuristics and data are consistent with abc but prove nothing; the parity-of-evidence problem is that no finite verification constrains the infinitely many large triples that matter.
