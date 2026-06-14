# Originator(s) — Giuga's Conjecture

_Biography, background, and the ideas that led here._

## Giuseppe Giuga (1911–1981)

Giuseppe Giuga was an Italian mathematician active chiefly in number theory and analysis during the middle of the twentieth century. He worked in the Italian academic system around Rome, in the milieu of classical number theory that flourished in Italy in the decades following the work of figures such as Giovanni Vacca and the broader Peano school. Giuga's published output is modest in volume but unusually durable in impact: his name is attached to a single, sharply posed problem that has resisted resolution for more than seventy years and that sits at the intersection of primality testing, Carmichael-type congruences, and Bernoulli-number arithmetic.

## Background and motivation

Giuga's conjecture grew directly out of **Fermat's little theorem** and the search for a clean *converse* — a congruence that detects primality rather than merely being a property of primes. In 1950 he noticed that the power sum
$$
S_n=\sum_{k=1}^{n-1}k^{\,n-1}
$$
satisfies $S_p\equiv -1\pmod p$ for every prime $p$, and asked whether this single congruence *characterizes* the primes. The appeal is its economy: a great many primality criteria are one-directional (true for primes, but with composite "pseudoprime" exceptions), and Giuga was probing whether this particular symmetric power-sum was strong enough to exclude all pseudoprimes at once.

What makes Giuga's contribution more than a curiosity is the **reduction** he supplied. Rather than leave the converse as an opaque assertion, he proved that a composite counterexample would have to be squarefree and satisfy, for each prime factor $p$, the divisibility $p\mid(n/p-1)$ — equivalently $p^2\mid n-p$. This converts an analytic-looking congruence into a transparent multiplicative condition, and it is this reduction that every subsequent attack has used. It also revealed the conjecture's two-sided nature: a counterexample must be simultaneously a *Carmichael-like* number (so that the Fermat congruences hold for every base) and satisfy a much rarer *Giuga* relation $\sum_{p\mid n}1/p-\prod_{p\mid n}1/p\in\mathbb{Z}$. The interplay of these two conditions is precisely why no small counterexample can exist, and why the problem is hard.

## The modern formulation versus the historical root

Giuga's original 1950 statement is the *power-sum / primality* form. The **modern** working form, due to the later Bernoulli-number reinterpretation, is the **Agoh–Giuga conjecture**: $p$ is prime iff $pB_{p-1}\equiv -1\pmod p$, where $B_{p-1}$ is a Bernoulli number. Takashi Agoh arrived at this around 1990 independently; the equivalence of Agoh's and Giuga's forms was established rigorously by the Borwein–Borwein–Borwein–Girgensohn group in 1996. Thus the historical root is Giuga's elementary congruence on power sums, while the contemporary literature most often phrases the problem through Bernoulli numbers and through the combinatorial *Giuga numbers* that isolate the multiplicative half of the condition.

## Legacy

Giuga's name now denotes a small ecosystem of objects: **Giuga numbers**, **Giuga sequences**, the **Agoh–Giuga conjecture**, and the broader study of $\sum 1/p-\prod 1/p\in\mathbb Z$. The conjecture is a textbook example of a statement that is *easy to state, trivially true in one direction, computationally unfalsified to astronomical bounds, and yet apparently far beyond current technique* in the converse. Its enduring openness — and the clean reduction Giuga left behind — secure its place as a model "hard elementary" problem in number theory.
