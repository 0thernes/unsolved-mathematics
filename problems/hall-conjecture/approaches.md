# Approaches — Hall's Conjecture

_Major strategies, partial results, and barriers._

## Deduction from the $abc$ conjecture

**Core idea.** Apply the $abc$ conjecture (Masser–Oesterlé) to the relation $x^3 = y^2 + k$ with $k = x^3 - y^2$. Treating $y^2 + k = x^3$ as an $abc$ triple and bounding the radical (product of distinct primes) by $|y|\cdot|k|\cdot \mathrm{rad}(\dots)$ yields, after standard manipulation, $x \ll_\varepsilon |k|^{2+\varepsilon}$, i.e. $|x^3 - y^2| \gg_\varepsilon x^{1/2-\varepsilon}$.

**Best result reached.** This gives the **weak Hall conjecture as a theorem conditional on $abc$**, with the essentially optimal exponent $1/2-\varepsilon$. It is the standard textbook illustration that $abc$ implies Hall.

**Barrier.** The $abc$ conjecture is itself wide open. Mochizuki's claimed proof via inter-universal Teichmüller theory remains unaccepted by most of the community (the Scholze–Stix obstruction). Moreover $abc$ is fundamentally ineffective in the usual formulation: even granting it, one does not extract the *strong* form's explicit constant. So this route delivers the qualitative shape but neither unconditional truth nor the sharp constant.

## Vojta's conjecture and height inequalities

**Core idea.** View integral points on the Mordell curve $y^2 = x^3 - k$ as $S$-integral points on an affine curve of genus $1$ minus a point. Vojta's height inequality for curves bounds the height of integral points in terms of the discriminant/conductor, and specializing recovers the weak Hall bound. Conceptually this places Hall inside the general Bombieri–Lang–Vojta picture of integral and rational points.

**Best result reached.** Weak Hall follows from Vojta's conjecture; this clarifies *why* the exponent $1/2$ is the natural one (it matches the ramification of the map $x \mapsto x^3$ at the relevant places).

**Barrier.** Vojta's conjecture is at least as hard as $abc$ and is unproven in this generality. The diophantine-approximation machinery (Schmidt subspace theorem, Roth-type bounds) that proves nearby statements gives ineffective constants and does not reach the genus-1 integral-point case with the needed uniformity.

## Linear forms in logarithms (Baker's method)

**Core idea.** For *fixed* $k$, the integral solutions of $y^2 = x^3 + k$ are effectively bounded by Baker's theory of linear forms in logarithms, giving explicit (if astronomical) bounds on $x$ in terms of $k$.

**Best result reached.** Effective resolution of $y^2 = x^3 + k$ for individual $k$ (and tables for $|k|$ up to large ranges, e.g. Gebel–Pethő–Zimmer). This *proves* a lower bound on $|x^3-y^2|$ but of the wrong, far weaker shape: Baker bounds give $x \ll \exp(c\,|k|^{\,\kappa})$-type or polynomial-in-$\log$ control per fixed $k$, not a uniform power law $x \ll k^2$.

**Barrier.** Baker's method is exponential and non-uniform in $k$. The gap between its effective exponential bounds and the conjectured polynomial bound $x \ll k^2$ is enormous and has never been bridged; the method seems structurally incapable of delivering a uniform power-saving lower bound for the gap.

## Function-field analogue (Davenport / Mason–Stothers)

**Core idea.** Replace integers by polynomials. Davenport (1965) proved $\deg(f^3 - g^2) \geq \tfrac12\deg f + 1$ for coprime polynomials with $f^3 \neq g^2$, the exact analogue of strong Hall, with the *best-possible constant*. The Mason–Stothers theorem (the polynomial $abc$) gives a clean derivation.

**Best result reached.** A complete, unconditional proof of the strong Hall inequality over function fields — including the sharp constant — via the Wronskian / Riemann–Hurwitz argument underlying Mason–Stothers.

**Barrier.** The proof uses differentiation (the Wronskian) and the absence of an archimedean "infinitesimal" obstruction — tools with no integer counterpart. This is exactly the wall that separates the (solved) function-field $abc$ from the (open) number-field $abc$: there is no known arithmetic derivative making the argument transfer.

## Computational search and the strong constant

**Core idea.** Directly hunt for pairs $(x,y)$ with small **Hall ratio** $r = |x^3-y^2|/\sqrt{x}$, both to test the strong form and to calibrate the conjectural constant. Methods: Elkies's lattice-basis-reduction search (using LLL to find $x$ with $x^3$ near a square), continued-fraction and Diophantine-approximation sieves, and exhaustive Mordell-curve tabulation.

**Best result reached.** Elkies's example near $x = 5853886516781223$ achieves $r \approx 0.0211$; later searches (Jiménez Calvo, Herzog, and others) catalogue dozens of "good" examples with small $r$. These confirm $|x^3-y^2|$ can be far below $\sqrt{x}$ for individual points, consistent with weak Hall and pressuring any naive strong constant.

**Barrier.** Search is intrinsically finite and cannot prove a lower bound; it can only refute over-optimistic constants or supply data. The persistent smallness of record ratios (no examples with $r$ bounded away from a clear positive floor *and* arbitrarily many of them with $r \to 0$) leaves the true infimum of $r$ unknown, which is precisely the crux of the strong conjecture.

## Modularity / elliptic-curve heights (heuristic)

**Core idea.** Relate $|x^3-y^2|$ to canonical heights and conductors of the Mordell curves $y^2 = x^3 - k$, using conjectures (Lang's height conjecture, Szpiro's conjecture) that are themselves equivalent to or implied by $abc$. Heuristic counting of integral points predicts the $x^{1/2-\varepsilon}$ law and the density of small-ratio examples.

**Best result.** A coherent heuristic web (Szpiro $\Leftrightarrow$ $abc$ up to constants; Lang's conjecture on lower bounds for canonical height) that all point to weak Hall.

**Barrier.** Every link in this web is conjectural and mutually entangled with $abc$; none is independently proven, so the approach explains and unifies rather than resolves.
