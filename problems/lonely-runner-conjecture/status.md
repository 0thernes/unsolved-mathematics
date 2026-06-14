# Status & Frontier — The Lonely Runner Conjecture

_Where the problem stands and what a resolution would require._

**Status: open (active progress).** The conjecture is proven for small numbers of runners and reduced to a finite computation per case, but no general proof exists.

## What is known (unconditional)

After the standard reduction — fix one runner at speed $0$, take the others' speeds to be distinct positive integers $v_1,\dots,v_n$ — the conjecture states there is a time $t$ with $\|t v_i\| \ge \tfrac{1}{n+1}$ for all $i$. The sharp constant $\tfrac{1}{n+1}$ is realized by $v_i = i$, so no improvement is possible.

Confirmed cases (by number of moving runners $n$):
- $n \le 3$: Wills (1967–1968).
- $n = 4$: Cusick–Pomerance (1984); reproved by Bienia–Goddyn–Gvozdjak–Sebő–Tarsi (1998).
- $n = 5$: Barajas–Serra (2008); elementary reproof by Renault (2011).

In total-runner language (the moving count plus the stationary reference runner), these settle the conjecture up through six or seven runners depending on convention. Each new case has demanded markedly more work than the last, and the $n=5$ proof is the technical ceiling of the purely elementary methods.

## Strongest current results

- **Finiteness reduction (Tao, 2017, arXiv:1701.02048).** It suffices to check speed sets whose entries are bounded by an explicit (super-polynomial) function of $n$. Thus for each fixed $n$ the conjecture is *decidable by finite computation* — though the search space is astronomically large for $n \ge 7$.
- **Improved constant (Tao, 2017).** The conjecture holds with $\tfrac{1}{n+1}$ replaced by $\tfrac{1}{2n} + \tfrac{c\log n}{n^2}$-type bounds — an explicit improvement over the trivial averaging constant $\tfrac{1}{2n}$, but still short of the sharp value.
- **Structured families.** Gap-of-divisors arguments (Renault and others) and polyhedral/Ehrhart methods (Beck–Hoşten–Schymura circle) verify large classes of speed sets, e.g. when $\max v_i$ is not too large relative to $n$, or for generalized arithmetic progressions.

There are no significant *conditional* results of the "follows from RH/GRH" type; the conjecture's difficulty is combinatorial-geometric rather than dependent on deep arithmetic hypotheses.

## What a full resolution would require

A proof must be **uniform in $n$ and attain the exact constant $\tfrac{1}{n+1}$.** The two structural obstacles are precise: (1) any averaging or second-moment argument provably sees only the order $\tfrac{1}{2n}$, never the sharp threshold, because the loneliness region of the extremizer $1,2,\dots,n$ has measure meeting the bound exactly; and (2) the hard instances are the **near-arithmetic-progression** speed sets, on which divisibility/covering shortcuts fail. A successful proof would likely need a new invariant that is simultaneously tight at the extremizer and stable across all speed sets — something neither Fourier moments nor view-obstruction case analysis currently provide.

## Plausible routes

- **Mechanizing Tao's finite check** for $n = 6, 7$ via the lonely-runner polytope and modern integer-feasibility / Ehrhart computation — the most likely source of the next confirmed cases.
- **A sharp harmonic-analytic identity** that recovers $\tfrac{1}{n+1}$ exactly, perhaps via extremal trigonometric polynomials tuned to the arithmetic-progression extremizer.
- **A colouring-theoretic breakthrough** on circular chromatic numbers of distance graphs (Zhu's dictionary) that bypasses explicit case analysis.

The consensus is that incremental case-by-case progress will continue while a uniform proof remains out of reach; the dossier asserts no resolution.

## Related problems

- [Littlewood Conjecture](../littlewood-conjecture/README.md) — sibling sharp problem in simultaneous Diophantine approximation.
- [Schanuel Conjecture](../schanuel-conjecture/README.md) — another deep Diophantine-flavored open problem on transcendence and independence.
- [Hadwiger–Nelson Problem](../hadwiger-nelson-problem/README.md) — a combinatorial-geometric colouring problem linked via distance graphs.
- [Kakeya Conjecture](../kakeya-conjecture/README.md) — geometry-of-numbers / covering flavor, obstructions to coverings of space.
- [Twin Prime Conjecture](../twin-prime-conjecture/README.md) — a benchmark open problem where finite-reduction and sieve barriers play analogous roles.
