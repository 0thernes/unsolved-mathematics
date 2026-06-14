# Attempts — Pillai's Conjecture

_Notable attempts, near-misses, retracted proofs._

The status of Pillai's conjecture is unusual: rather than a graveyard of failed "proofs," its history is a steady accumulation of partial results, each pushing the boundary of what is known but stopping at the same structural wall — the inability to bound the exponents for $k \ge 2$.

## The Catalan special case ($k = 1$)

The most consequential near-completion is the $k = 1$ slice. **Tijdeman (1976)** proved that Catalan's equation $x^p - y^q = 1$ has only finitely many solutions, effectively bounded, via Baker's method. This fell short of solving Pillai because it (a) addressed only $k = 1$ and (b) gave bounds far too large to verify by computation at the time. The gap was closed not by extending Tijdeman but by a new idea: **Mihăilescu (2002–2004)** proved Catalan's conjecture outright using cyclotomic field theory. This is a genuine resolution of one infinite family ($k = 1$, all exponents), but the techniques have resisted generalization to $k \ge 2$.

## Fixed-exponent finiteness

Pillai himself proved finiteness when the exponents are fixed, and this has been refined to fully explicit form. **Bennett (2001, 2004)** showed that for fixed $p, q \ge 2$, the equation $|x^p - y^q| = k$ has at most a bounded (often $\le 2$) number of positive solutions, and gave methods to find them all. **Bennett–Bugeaud–Mignotte–Siksek** and related collaborations resolved long lists of Lebesgue–Nagell equations $x^2 + D = y^n$. These are decisive successes — but each is a fixed-signature statement, not the variable-exponent conjecture.

## Conditional resolution under $abc$

It is a folklore-to-textbook observation (made precise by many authors, including in surveys by Waldschmidt and in the work surrounding the $abc$ conjecture) that the **$abc$ conjecture implies Pillai's conjecture in full**. This is not a proof of Pillai's conjecture; it is a reduction. Any claimed proof of $abc$ would, if accepted, settle Pillai. Mochizuki's inter-universal Teichmüller (IUT) program, claiming $abc$, is **not accepted by the broader mathematical community** (notably following the Scholze–Stix objections of 2018), so it cannot currently be regarded as resolving Pillai's conjecture even conditionally-as-fact.

## Quantitative refinements and near-misses

- **Pillai's asymptotic counts (1930s).** Pillai obtained asymptotics for the number of solutions of $a x^p - b y^q = k$ in fixed-exponent cases — genuine theorems, but not the finiteness-over-all-exponents claim.
- **Lower bounds on power gaps.** Effective lower bounds of the shape $x^p - y^q \gg (\log x)^{c}$ or polynomial-in-height bounds for restricted exponents follow from Baker's method but are conjectured (under $abc$) to be far weaker than the truth $x^p - y^q \gg x^{p(1-\varepsilon)}$.
- **Pillai's equation $|x^p - y^q| = k$ for specific small $k$.** Computer-assisted modular and Baker-based work has determined all solutions for many individual small values of $k$ (e.g. small differences between perfect powers), but no method covers all $k \ge 2$ uniformly.

## Disputed or retracted claims

There is no widely circulated, peer-reviewed claimed proof of the **full** Pillai conjecture that was later retracted; the problem has largely been approached honestly as open. The only claim that would settle it — Mochizuki's $abc$ proof — is disputed on the $abc$ side, not on a direct Pillai-specific argument. Caution is warranted with occasional arXiv preprints announcing elementary proofs of Pillai or Catalan-type statements; none has survived expert scrutiny, and the conjecture remains open for every $k \ge 2$ in the variable-exponent regime.
