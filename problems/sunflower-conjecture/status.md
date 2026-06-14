# Status & Frontier — The Sunflower Conjecture

_Where the problem stands and what a resolution would require._

**Status: active progress — open, but dramatically narrowed.** As of mid-2020s the conjecture itself, $f(w,k) \le C(k)^w$, is **unproved**, but the gap between the best known upper bound and the conjecture has shrunk to a single logarithmic factor — the closest the problem has been to resolution in its sixty-year history.

## What is known (unconditional)

Write $f(w,k)$ for the threshold above which any family of $w$-sets must contain a $k$-petal sunflower.

- **Classical (1960):** Erdős–Rado, $f(w,k) \le w!\,(k-1)^w$.
- **Classical record (1997):** Kostochka, $f(w,3) \le c\,w!\,(\log\log\log w/\log\log w)^w$ — still super-exponential.
- **Breakthrough (2019):** Alweiss–Lovett–Wu–Zhang (arXiv:1908.08483), $f(w,k) \le (C k^3 \log w \log\log w)^w$ — base polylogarithmic in $w$.
- **Cleaned form (2020–2021):** Rao (arXiv:1909.04774, "Coding for sunflowers") and Tao's exposition, then Bell–Chueluecha–Warnke (arXiv:2105.06561, "Note on sunflowers"), give the sharpest current bound
$$ f(w,k) \le (C k \log w)^w $$
for an absolute constant $C$.
- **Lower bound:** $f(w,k) \ge (k-1)^w$, essentially unimproved at the super-exponential scale.

So the truth lies between $(k-1)^w$ and $(C k \log w)^w$. The conjecture asserts the lower end is correct up to the constant base $C(k)$.

## Conditional / structural results

The breakthrough rests on the **spread lemma**: an $r$-spread family of $w$-sets with $r = \Omega(k \log w)$ contains a sunflower. The full conjecture is equivalent (up to the usual reductions) to proving the spread lemma with threshold $r = O(k)$, **independent of $w$**. No conditional assumption is known to deliver this; it is a genuine gap, not a barrier waiting on a hypothesis.

## What a full resolution would require

Eliminating the residual $\log w$ from the spread threshold. Every current proof — probabilistic coupling (ALWZ), entropy encoding (Rao/Tao), or constant-optimized refinement (BCW) — produces the logarithm intrinsically: the sampling/compression certificate that "spread forces disjoint petals" loses a factor per coordinate scale. A resolution plausibly needs either (i) a new way to certify sunflower structure in spread families that avoids per-scale loss, (ii) an amplification or bootstrapping that recycles the existing bound to remove its own logarithm, or (iii) an entirely different, possibly algebraic or structural, characterization of sunflower-free families. A *disproof* would require a super-exponential lower-bound construction beating $(k-1)^w$, of which there is currently no hint; the weight of evidence favors the conjecture being true.

## Plausible routes

- Sharpening the spread/encoding machinery — most actively pursued, but believed to be at or near its limit at $\log w$.
- Importing ideas from the **Kahn–Kalai / threshold program** (Park–Pham, Frankston–Kahn–Narayanan–Park), which shares the spread technology and resolved adjacent expectation-threshold questions.
- A robust **polynomial-method** or randomness-extractor approach (continuing the Li–Lovett–Zhang line).

## Related problems

- [Kakeya Conjecture](../kakeya-conjecture/README.md) — another problem where spread/incidence and the polynomial method are central tools.
- [Hadwiger–Nelson Problem](../hadwiger-nelson-problem/README.md) — extremal/combinatorial geometry with a similar "unavoidable structure" flavor.
- [Union-Closed Sets Conjecture](../union-closed-sets-conjecture/README.md) — a sibling open problem in extremal set theory recently moved by new ideas.
- [Hadwiger Conjecture](../hadwiger-conjecture/README.md) — extremal combinatorics where greedy bounds long resisted improvement.
- [Caccetta–Häggkvist Conjecture](../caccetta-haggkvist-conjecture/README.md) — a stubborn extremal conjecture awaiting a structural breakthrough.
