# Attempts — The Lonely Runner Conjecture

_Notable attempts, near-misses, retracted proofs._

The Lonely Runner Conjecture has the unusual profile of being **proven for every small case anyone has checked** while remaining open in general — so the historical record is dominated by hard-won case-by-case theorems rather than failed grand proofs. The verified frontier has advanced roughly one runner per decade, each step requiring substantially more work than the last.

## The ladder of proven cases

- **$n \le 3$ (Wills, 1967–1968).** The originating cases, handled by direct Diophantine estimates.
- **$n = 4$ (Cusick–Pomerance, 1984; reproved by Bienia–Goddyn–Gvozdjak–Sebő–Tarsi, 1998).** Five runners. The 1984 proof is intricate; the 1998 treatment is cleaner and embeds the result in a broader combinatorial framework.
- **$n = 5$ (Barajas–Serra, 2008).** Six runners. A genuine tour de force of the view-obstruction method, widely regarded as the technical high-water mark of the elementary approaches. Renault (2011) later gave a more transparent argument.
- **$n = 6$ and beyond.** Progress here relies on Tao's finiteness reduction plus heavy computation for structured subfamilies; a complete clean proof for the next value has been the object of sustained effort but no single celebrated paper has closed it in full generality the way Barajas–Serra closed $n=5$.

## Near-misses and partial results

- **The trivial constant $\tfrac{1}{2n}$** is immediate from averaging; the entire difficulty is the factor-of-two gap up to $\tfrac{1}{n+1}$. Many incremental papers shave this gap for restricted speed sets.
- **Tao (2017)** proved the conjecture with a constant strictly better than $\tfrac{1}{2n}$ (an explicit improvement growing like $\tfrac{c \log n}{n^2}$) and, more importantly, reduced the general conjecture to a **finite computation** for each $n$ by bounding the speeds that need to be checked. This is the closest thing to a structural breakthrough, yet it deliberately stops short of the sharp constant.
- **Structured speed sets.** Numerous results confirm the conjecture when the speeds satisfy extra hypotheses: arithmetic progressions, geometric-like spacing, small $\max v_i / n$, coprimality patterns, or membership in generalized arithmetic progressions (gap-of-divisors results of Renault and others; polyhedral results of the Beck–Hoşten–Schymura circle).

## Variants, where claims are more contested

The hardness of the original drove attention to relaxations, and it is in these variants — not the main conjecture — that disputes and corrections have appeared:

- **Shifted / inhomogeneous Lonely Runner.** Asking for loneliness around a nonzero target gap, or with prescribed shifts, changes the extremal constant; several proposed sharp constants for shifted versions have been revised in the literature as counterexamples to over-optimistic formulations were found.
- **Rational / "shifted by 1/2" variants** and the **dynamic/"lonely vector" generalizations** have produced statements that were announced, then weakened, once boundary cases were examined. These are honest corrections of variant conjectures, not refutations of the classical statement.

## Status of any "claimed proof" of the full conjecture

As of the knowledge cutoff, **there is no widely accepted complete proof of the general Lonely Runner Conjecture**, and no famous retracted claim of one in the manner of (say) disputed proofs of major conjectures elsewhere. Preprints proposing general resolutions appear from time to time on arXiv and elsewhere; the community's consistent assessment is that none has survived scrutiny, typically because the argument either silently assumes a covering structure that fails for near-arithmetic-progression speed sets, or loses the sharp constant exactly where the extremal example $1,2,\dots,n$ lives. Readers should treat any such announced proof as **unverified** until it appears in a refereed venue with independent confirmation; the present dossier asserts no resolution.
