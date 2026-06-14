# Status & Frontier — The abc Conjecture

_Where the problem stands and what a resolution would require._

**Current status: open, with a prominent disputed claim.** The mainstream arithmetic-geometry community regards the abc conjecture as unproven. A claimed proof exists — Shinichi Mochizuki's Inter-universal Teichmüller theory (IUT), *Inter-universal Teichmüller Theory I–IV*, released 2012, published in *Publications of the RIMS* in 2020/2021 — but it has not achieved independent verification, and a specific, documented objection to its central step stands unanswered to the community's satisfaction. The institute classifies the problem as a **disputed-claim** for exactly this reason.

## What is known unconditionally

The strongest unconditional result is **Stewart–Yu** (1991; sharpened 2001): for coprime $a+b=c$,
$$ \log c \;\ll_\varepsilon\; \mathrm{rad}(abc)^{\,1/3+\varepsilon}. $$
This is *exponentially* weaker than the conjecture, which demands $\log c \ll (1+\varepsilon)\log\mathrm{rad}(abc) + O(1)$. The gap is structural: the only engine producing unconditional bounds, Baker's theory of linear forms in logarithms, cannot in principle deliver a polynomial-in-$\log$ bound. Computationally, abc is verified for all triples below very large bounds, and the record extremal triple has quality only $q\approx 1.6299$ ($2 + 3^{10}\cdot 109 = 23^5$), consistent with — but not proving — the conjecture.

## What is known conditionally / by analogy

- The **function-field** analogue (Mason–Stothers, 1981/84) and the **holomorphic/Nevanlinna** analogue are full theorems. They establish the conjecture's "moral truth" and pinpoint the missing ingredient: an integer analogue of the derivative/Wronskian.
- abc is **equivalent** to a uniform Szpiro inequality and is a special case of **Vojta's** height conjectures.
- abc would *imply*, often immediately: asymptotic Fermat, effective Mordell (Elkies), Roth's theorem with effective constants, infinitude of non-Wieferich primes, Erdős–Woods, the Granville–Langevin conjecture, and bounds on Brocard–Ramanujan-type equations.

## What a full resolution requires

A genuine proof must produce a bound of the form $\log c \le (1+\varepsilon)\log\mathrm{rad}(abc) + C_\varepsilon$ holding for all but finitely many triples — a *polynomial-in-log* control with explicit $\varepsilon$-dependence. The two live routes are: (i) **rehabilitate or refute IUT**, by making Corollary 3.12 of IUT III either rigorous and quantitatively non-trivial (against the Scholze–Stix reading) or definitively wrong; and (ii) **find a new arithmetic mechanism** supplying the "derivative" that the function-field proof uses — whether through Joshi's arithmetic-Teichmüller spaces, $p$-adic Hodge-theoretic comparison, or an as-yet-unknown idea. No incremental sharpening of Baker's method can reach the conjecture; a qualitatively new input is mandatory.

The neutral assessment of record: abc remains one of the central unsolved problems of number theory. The Mochizuki proof is cited as a claim, not as established fact, and its key inequality is the subject of an unresolved technical dispute (Scholze–Stix, 2018).

## Related problems

- [Beal Conjecture](../beal-conjecture/README.md) — a Diophantine cousin on common-factor constraints in $A^x+B^y=C^z$, in the same radical/power circle of ideas.
- [Fermat-type / Birch–Swinnerton-Dyer](../birch-swinnerton-dyer/README.md) — elliptic-curve arithmetic adjacent to the Frey-curve/Szpiro reformulation.
- [Schanuel Conjecture](../schanuel-conjecture/README.md) — a transcendence-theory grand conjecture, sibling in the "deep input from algebraic independence" sense.
- [Brocard Problem](../brocard-problem/README.md) — $n!+1=m^2$, a finiteness question that abc would constrain.
- [Erdős–Straus Conjecture](../erdos-straus-conjecture/README.md) — another elementary-to-state, hard Diophantine problem in the same neighborhood.
