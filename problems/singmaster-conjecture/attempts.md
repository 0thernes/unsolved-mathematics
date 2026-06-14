# Attempts — Singmaster's Conjecture

_Notable attempts, near-misses, retracted proofs._

## The benchmark partial result

The earliest and still-canonical partial result is the **Abbott–Erdős–Hanson bound** of 1974, $N(a) = O(\log a / \log\log a)$. It is not a near-miss in the sense of almost proving the conjecture — it is exponentially far from a constant — but it remains the best *unconditional uniform* statement and frames every subsequent attempt. Half a century of effort has not improved its order of magnitude for general $a$, which is itself a striking measure of the problem's difficulty.

## Per-equation finiteness and explicit enumerations

A long sequence of authors settled individual equations $\binom{n}{2}=\binom{m}{\ell}$ completely. The most celebrated coincidences are:

- $\binom{n}{2}=\binom{m}{3}$, whose solutions correspond to numbers that are simultaneously of the form $\binom{n}{2}$ and $\binom{m}{3}$ — finitely many, fully enumerated.
- $\binom{n}{2}=\binom{m}{4}$, solved explicitly by **de Weger** (1980s) using Baker's method, with the largest solution famously involving the value $3003$ and its relatives.
- The single known equality giving the "eight-fold" near-record is bound up with $3003$, the unique number known to occur six times below astronomically large bounds.

These are genuine, verified results — each shows finiteness for one curve — but they are partial precisely because the constants do not assemble uniformly across all $(k,\ell)$.

## The conditional / averaged frontier

The 2021 work of **Matomäki, Radziwiłł, Shao, Tao, and Teräväinen** is the most substantial modern advance. It proves a power-saving bound on the *total* number of nontrivial solutions up to $N$, hence that the conjecture holds on average and that exceptional $a$ are very sparse. It is correct and refereed, but it is honestly a partial result: it does not bound $N(a)$ for an individual $a$, which is what the conjecture requires. The authors themselves frame it as evidence for, not a proof of, Singmaster's conjecture.

## Computational searches

Extensive computer searches (continuing the tradition of Singmaster's own hand computations) have verified that **no integer below very large bounds appears more than six times**, and that no integer at all is known to appear seven or more times. These searches strongly suggest the true maximum multiplicity is $6$ (or possibly $8$ at finitely many points, per Erdős's guess), but a search can never establish a conjecture of this form — it only fails to find counterexamples.

## Claimed proofs and disputes

Singmaster's conjecture has not attracted a famous **retracted or widely disputed claimed proof** of the kind that surrounds, say, the abc conjecture or the Riemann hypothesis. There is no established, peer-reviewed claim of a full resolution, and the problem is universally regarded as open. From time to time elementary "proofs" have circulated informally (e.g., on preprint repositories and discussion forums) asserting a constant bound; these have not been accepted because they invariably either (i) bound only the average or a single equation, conflating it with the uniform statement, or (ii) rely on an unproven uniformity across the family of curves that is exactly the crux of the difficulty. In keeping with house policy, no such claim is reported here as established; the neutral statement is that the conjecture remains open and the strongest accepted results are the averaged/exceptional-set bounds above. Anyone evaluating a purported proof should check specifically whether it controls a *single* rare $a$ uniformly, since that is the precise gap every partial method leaves open.
