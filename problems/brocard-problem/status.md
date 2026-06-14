# Status & Frontier — Brocard's Problem

_Where the problem stands and what a resolution would require._

**Status: open.** Brocard's problem — whether $n! + 1 = m^2$ has only finitely many solutions in positive integers — is unresolved. Exactly three solutions are known, $n \in \{4, 5, 7\}$ (the **Brown numbers**), and it is conjectured that no others exist. Neither finiteness nor the stronger "only these three" is proved unconditionally.

## What is known (unconditional)

- **The three solutions** $4!+1=5^2$, $5!+1=11^2$, $7!+1=71^2$ are the complete list up to very large bounds. The canonical computational result, **Berndt and Galway (2000)**, verified no further solution for $n \le 10^9$; later searches push the verified range substantially higher (into the $10^9$–$10^{12}$ region by various sieve methods) with no new solution found.
- **The generalized theorem of Dąbrowski (1996):** for every fixed integer $A$ that is **not** a perfect square, $n! + A = m^2$ has only finitely many solutions. This is the strongest unconditional structural result in the area — but it explicitly excludes $A = 1$, since $1$ is a square and the factorization $m^2 - A = (m-\sqrt A)(m+\sqrt A)$ over $\mathbb{Z}$ destroys the obstruction the proof uses.
- Elementary congruence and quadratic-residue conditions sharply constrain any hypothetical fourth solution and power the computational sieves, but provide no upper bound on $n$.

## What is known (conditional)

- Under a **weak form of the abc conjecture**, Brocard's problem has only finitely many solutions (observed by **Overholt**). The mechanism: $\mathrm{rad}(n!) = \prod_{p\le n}p = e^{(1+o(1))n}$ is exponentially smaller than $n! = e^{(1+o(1))n\log n}$, so abc applied to $1 + n! = m^2$ forces $n!$ — hence $n$ — to be bounded. The same implication covers $n!+1=m^k$ and $n!+A=m^2$.
- This conditional resolution **cannot currently be promoted to unconditional**: the abc conjecture is open. Mochizuki's claimed proof (PRIMS, 2021) is not accepted following the **Scholze–Stix (2018)** objection, so abc cannot be invoked as a theorem.

## What a full resolution would require

A complete answer must do one of the following:
1. **Prove abc** (or just the weak quantitative form sufficient here), which would yield finiteness immediately and ineffectively; or
2. Supply a **new effective handle on $n!$** — some way to apply Baker-type linear-forms-in-logarithms bounds or a descent to an object with fixed algebraic structure — to bound $n$ directly. The central difficulty is that $n!$ is neither a fixed exponential $a^n$ nor a value of a fixed polynomial/binary form, so existing effective Diophantine machinery does not engage.

Proving the stronger statement that $\{4,5,7\}$ is the *exact* solution set would additionally require an explicit, computable bound on $n$ small enough to be closed by the existing verified search range.

## Plausible routes

The most likely path to finiteness is a proof (or accepted partial form) of abc. Absent that, progress is expected to come incrementally from the generalization program (extending Dąbrowski-type theorems toward the square-$A$ boundary), from sharper effective methods, and from continued computation that, while it cannot prove finiteness, keeps the conjecture empirically airtight. No credible route currently promises an unconditional proof in the near term; Brocard's problem is widely regarded as genuinely hard rather than merely unattacked.

## Related problems

- [abc Conjecture](../abc-conjecture/README.md) — its weak form implies Brocard's finiteness; the key conditional link.
- [Erdős–Straus Conjecture](../erdos-straus-conjecture/README.md) — a sibling elementary-to-state, computationally-probed Diophantine question.
- [Beal Conjecture](../beal-conjecture/README.md) — another perfect-power Diophantine problem in the abc orbit.
- [Bunyakovsky Conjecture](../bunyakovsky-conjecture/README.md) — prime/square values of polynomial-like sequences, sharing the "structure vs. density" tension.
- [Goldbach Conjecture](../goldbach-conjecture/README.md) — a comparably famous, elementary additive-multiplicative problem resistant to current methods.
