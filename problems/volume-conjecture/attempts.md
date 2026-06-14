# Attempts — The Volume Conjecture

_Notable attempts, near-misses, retracted proofs._

## Confirmed cases (genuine, fully proved)

- **Torus knots (Kashaev–Tirkkonen, 2000/2004).** Since torus-knot complements are Seifert fibered and not hyperbolic, the simplicial volume is $0$. Kashaev and Tirkkonen proved the limit is indeed $0$, with the colored Jones at $e^{2\pi i/N}$ growing only polynomially (no exponential term). This is the first rigorous confirmation, and it is exactly why the conjecture is stated with *simplicial* volume.
- **Figure-eight knot $4_1$ (Andersen–Hansen 2006; Ohtsuki 2016).** The smallest hyperbolic knot is the touchstone. Andersen–Hansen gave an analytic treatment of the asymptotics; Ohtsuki later produced a complete, rigorous asymptotic expansion via the saddle-point method, recovering $\mathrm{Vol}(4_1)=2.029883\ldots$ together with the $1$-loop correction and a power-series tail. Widely regarded as the model proof.
- **$5_2$, $6_1$, and selected twist / double-twist knots (Ohtsuki; Ohtsuki–Yokota; later authors).** The figure-eight method, with substantial extra labor, has been extended to a handful of additional small hyperbolic knots, in several cases including the complexified ($\mathrm{Vol}+i\,\mathrm{CS}$) statement.
- **Whitehead-type links, fundamental shadow links (Belletti–Detcherry–Kalfagianni–Yang, 2018+).** In the Turaev–Viro/Chen–Yang formulation, the volume conjecture is proved for the rich family of fundamental shadow links and certain Dehn fillings — currently the largest class for which a volume-conjecture-type statement is a theorem.

## Near-misses and structural milestones

- **Murakami–Murakami (2001).** Not an attempt to prove the limit, but the identification $\langle K\rangle_N = J_N(K;e^{2\pi i/N})$ that made all subsequent attempts possible.
- **Garoufalidis–Lê (2005, *Ann. of Math.*).** Proved $q$-holonomicity of the colored Jones, the foundation of the AJ-conjecture route. It constrains the asymptotics structurally without delivering the volume limit.
- **Ohtsuki–Yokota potential functions.** Reduced the conjecture (for a given knot) to a saddle-point/contour problem whose geometric critical value is the complex volume; the remaining gap — proving the geometric saddle dominates — is the recurring difficulty.

## Disputed / over-claimed statements (stated neutrally)

There is no widely circulated "claimed proof of the full Volume Conjecture for all hyperbolic knots" that the community accepted and later retracted; the conjecture remains formally open, and most experts treat it as genuinely hard. The disputes that exist are about **scope and formulation** rather than about a single flawed manuscript:

- **Universality over all links / roots of unity.** Early optimistic phrasings suggested the plain limit holds for every link. Subsequent work showed the limit can fail to exist, can be dominated by a non-geometric flat connection, or can pick up oscillatory subexponential factors for certain links and torus knots. The objection — that the precise statement must use $\limsup$, simplicial volume, and sometimes the complexified version — is now standard and not contested.
- **Chen–Yang root-of-unity subtlety.** The Chen–Yang reformulation depends essentially on using $q=e^{2\pi i/r}$ rather than the "standard" $e^{\pi i/r}$; conflating the two leads to false growth-rate claims. This is a clarified convention, not an unresolved dispute.

In short: the field's caution is methodological. Numerical evidence is overwhelming and several clean special cases are fully proved, but no accepted argument covers all hyperbolic knots, and the literature has been careful to flag where naive generalizations break.
