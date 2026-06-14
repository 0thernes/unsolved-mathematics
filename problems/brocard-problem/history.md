# History — Brocard's Problem

_Origin, formulation, and timeline._

Brocard's problem asks whether the Diophantine equation
$$n! + 1 = m^2$$
has only finitely many solutions in positive integers $n$. The integers $n$ for which a solution exists are called **Brown numbers** (the pairs $(n,m)$ are *Brown pairs*), after Kevin S. Brown, who popularized the question. The only known solutions are
$$4! + 1 = 25 = 5^2,\quad 5! + 1 = 121 = 11^2,\quad 7! + 1 = 5041 = 71^2,$$
giving $n \in \{4,5,7\}$. No fourth Brown number is known despite extensive computation, and it is conjectured — but not proved — that these three are the complete list.

The problem was first raised by the French mathematician and meteorologist **Henri Brocard** in a short note to the *Nouvelle correspondance mathématique* in **1876**, and restated by him in *Mathesis* in **1885**. Strikingly, **Srinivasa Ramanujan** posed the identical question independently in **1913** as Question 469 in the *Journal of the Indian Mathematical Society*, asking for which $n$ the quantity $n! + 1$ is a perfect square. Because of this dual origin the equation is sometimes called the **Brocard–Ramanujan equation**, and the broader study of $n! + A = m^2$ is named after both men.

The equation sits at the intersection of two notoriously hard themes: the multiplicative irregularity of factorials and the additive rigidity of perfect squares. Heuristically, $n!$ is "almost never" one less than a square: modeling $n!+1$ as a "random" integer near $m^2$, the probability that it is a perfect square is on the order of $m^{-1} \approx (n!)^{-1/2}$, and $\sum_n (n!)^{-1/2}$ converges very rapidly. The expected number of solutions beyond a modest bound is therefore tiny — consistent with there being no fourth Brown number. But this heuristic is not a proof, and no unconditional argument forces finiteness.

A natural **generalization**, studied by Erdős, Obláth, Dąbrowski and others, replaces $1$ by an integer parameter: for which $A$ does $n! + A = m^2$ (or $n!+1 = m^k$) have finitely many solutions? Dąbrowski's work shows that for fixed $A$ that is *not* a perfect square, $n! + A = m^2$ has only finitely many solutions — a theorem that conspicuously fails to settle the case $A = 1$ (where $1$ *is* a square). This asymmetry is the technical heart of why Brocard's original problem remains open while close relatives are solved.

## Timeline

- **1876** — Henri Brocard poses the question whether $n!+1$ is a square for only finitely many $n$, in *Nouvelle correspondance mathématique*.
- **1885** — Brocard restates the problem in *Mathesis*, fixing its attribution.
- **1906** — Brocard returns to the question in *L'Intermédiaire des mathématiciens*, listing the known solutions $n=4,5,7$.
- **1913** — Srinivasa Ramanujan independently asks the same question (Question 469, *Journal of the Indian Mathematical Society*).
- **1935** — Richard Obláth treats related factorial–power equations $n! + 1 = m^k$ and surrounding problems.
- **1996** — Andrzej Dąbrowski proves that for any fixed non-square integer $A$, $n! + A = m^2$ has only finitely many solutions, sharpening the contrast with the unsolved $A=1$ case.
- **2000** — Bruce C. Berndt and William F. Galway publish a computational search confirming no further Brown numbers for $n \le 10^9$.
- **2000s** — Marius Overholt observes that a (weak form of the) abc conjecture implies Brocard's problem has only finitely many solutions.
- **2010s** — Numerical verification is extended; searches push the bound on $n$ well beyond $10^9$ with no new solution. Generalizations to $n! + A$ and to other gamma-like sequences are explored.
- **2020s** — The problem remains open. It is cited as a benchmark "easy to state, hard to solve" Diophantine equation; conditional results under abc and effective Diophantine methods constitute the current frontier.

In qualitative terms the status today is exactly what it was in Brocard's lifetime — three known solutions, no others found — but the surrounding theory (abc-conditional finiteness, generalized-equation theorems, vast computation) gives strong, though non-rigorous, support to the conjecture that $\{4,5,7\}$ is complete.
