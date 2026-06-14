# Attempts — The Caccetta–Häggkvist Conjecture

_Notable attempts, near-misses, retracted proofs._

The Caccetta–Häggkvist conjecture has a long record of partial results and approximations, but — unlike some celebrated problems — it has not been the subject of a single famous, widely publicized false "proof." Its difficulty is honest and incremental: progress has come as a slow tightening of constants rather than dramatic claimed breakthroughs. What follows are the most significant near-misses and partial results, together with the relaxations that have been settled.

## The additive-constant approximation (Chvátal–Szemerédi, 1985)

The first decisive general result was the theorem of **Václav Chvátal and Endre Szemerédi**: every digraph with minimum out-degree $d \ge 1$ on $n$ vertices contains a directed cycle of length at most $n/d + 2500$. This is exactly the conjecture ($k = n/d$) up to an *additive constant*. The constant $2500$ was an artifact of the method, not believed to be best possible, and has been improved by later authors. The result remains the canonical "almost-proof" of the general statement: it shows the right linear scaling but cannot remove the additive slack — which is precisely the hard part, since the conjecture predicts a clean threshold with no slack at all.

## The triangle case: a chain of constants

For $k=3$ the recorded near-misses are a sequence of improving constants $\beta$ such that minimum out-degree $\ge \beta n$ forces a directed triangle:

- Early counting arguments gave $\beta$ noticeably above $1/3$.
- **Shen Jian (2003)** reached $\beta \le 0.3532$.
- **Hladký, Král', and Norin** (mid-2000s, via flag algebras) reached $\beta \approx 0.3465$, the current best.

Each is a genuine partial theorem, valid and uncontested, but each falls short of the conjectured $1/3 \approx 0.3333$. The persistent gap of roughly $0.013\,n$ is the headline open quantity.

## Settled relaxations

Several weaker or modified versions are **known to be true**, which is why confidence in the conjecture is high:

- **Fractional version.** The fractional relaxation of the triangle case was established (work associated with **D. C. Fisher** and others), giving exactly the $1/3$ constant in the relaxed setting.
- **Vertex-transitive and Cayley digraphs.** The conjecture holds for these algebraically structured cases via additive-combinatorial arguments.
- **Eulerian and regular special cases.** Various degree-regular and Eulerian sub-families have been confirmed.

These successes sharpen the contrast: the obstruction lies entirely in the lack of structure of *general* digraphs, not in the threshold itself.

## On disputed or retracted claims

There is **no prominent retracted or disputed full proof** of the Caccetta–Häggkvist conjecture in the mainstream literature, and this dossier makes no claim of one. From time to time elementary "proofs" of the triangle case circulate informally (e.g. on preprint servers or discussion forums); the standard objection to such attempts is that they implicitly use only *local* density information and therefore cannot beat the flag-algebra ceiling near $0.3465$ — any argument purporting to reach exactly $1/3$ by local averaging is, on those grounds, viewed with strong skepticism until it explains how it captures the global cyclic structure that the extremal example $\vec{C}_n$ exploits. As of the present frontier, the conjecture stands open in every case $k \ge 3$, with all accepted results being strictly partial.
