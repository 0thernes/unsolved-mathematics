# History — Carmichael's Totient Conjecture

_Origin, formulation, and timeline._

The conjecture concerns the **multiplicity** (or **fiber size**) of Euler's totient function $\varphi$. For a positive integer $n$, define
$$A(n) = \#\{\, m : \varphi(m) = n \,\}.$$
The values $A(n)$ are the cardinalities of the level sets of $\varphi$. Numbers in the image of $\varphi$ are called **totient values** (or **nontotients** when $A(n)=0$); a value with $A(n)=1$ would be **sporadic** — taken exactly once. Carmichael's Totient Conjecture asserts that **no such sporadic value exists**: for every $m$ there is some $m'\neq m$ with $\varphi(m')=\varphi(m)$, equivalently $A(n)\neq 1$ for all $n$.

The statement is easy to verify in small cases and is reinforced by an elementary observation: multiplicity is typically large. If $\varphi(m)=n$ and $m$ is, say, divisible by an odd prime $p$ with $p\nmid (m/p)$, one can often produce a sibling. The difficulty is uniformity — ruling out a single exceptional $m$ of enormous size.

The problem sits beside Sierpiński's question on which multiplicities occur (every $k\geq 2$ is a value of $A$, proven via Erdős and finalized by Ford) and Ford's deep analysis of the distribution of totient values. A key reformulation, due to **Klee (1947)**, gives a finite computable criterion that a counterexample must satisfy, which underlies all modern lower-bound computations on the smallest possible counterexample.

## Timeline

**1907** — Robert D. Carmichael, in _Bulletin of the AMS_ ("On Euler's $\varphi$-function"), states the conjecture and offers an argument intended as a proof.

**1922** — Carmichael publishes a note in the _Bulletin of the AMS_ acknowledging that his 1907 argument is **flawed**; the assertion is thereafter treated as a conjecture, and he establishes that any counterexample must exceed $10^{37}$.

**1947** — Victor Klee gives a reformulation and criterion (an "irreducible" structure a counterexample must have), substantially raising the computational lower bound and providing the template later authors refine.

**1955** — Patrick A. Masai and others, and subsequently several computational notes, push the bound on the least counterexample upward as machine computation matures.

**1980s** — Carl Pomerance proves a striking conditional result: if a counterexample $m$ exists, then for every prime $p$ with $(p-1)\mid \varphi(m)$ one must have $p^2 \mid m$, forcing such $m$ to be highly structured and divisible by squares of many primes. This both constrains counterexamples and connects the problem to questions about primes $p$ with $p-1$ smooth.

**1994** — Aaron Schlafly and Stan Wagon compute that any counterexample exceeds $10^{10^{7}}$.

**1998** — Kevin Ford, in landmark work on the image of $\varphi$ (_Annals of Mathematics_, "The distribution of totients"), proves that **every multiplicity $k\geq 2$ is attained** (Sierpiński's conjecture) and develops the analytic machinery that frames Carmichael's conjecture; he raises the lower bound on a counterexample to roughly $10^{10^{10}}$.

**1998–1999** — Ford and Sungjin Konyagin study related multiplicity phenomena; the "Carmichael" question is highlighted as the conspicuous gap: the value $1$ is the only multiplicity not known to occur or be excluded.

**2014** — In follow-up computational and theoretical work, the lower bound for the least counterexample is reported beyond $10^{10^{10}}$, with the structural constraints (Pomerance-type conditions, Klee's criterion) doing the heavy lifting.

**Present** — The conjecture remains **open**. It is widely believed true, supported by enormous lower bounds and heuristic arguments that sporadic totient values, if they existed, would have to evade an essentially infinite family of sibling-producing constructions simultaneously. No counterexample is known, and no proof technique has closed the uniformity gap.
