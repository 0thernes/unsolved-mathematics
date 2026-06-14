# History — Singmaster's Conjecture

_Origin, formulation, and timeline._

## How the problem arose

Pascal's triangle records the binomial coefficients $\binom{n}{k}$. A natural counting question is: how often does a fixed value $a > 1$ occur in the triangle? Defining the **multiplicity** $N(a) = \#\{(n,k) : \binom{n}{k} = a\}$, how large can $N(a)$ be? Every $a$ trivially appears at least twice via the symmetry $\binom{n}{k} = \binom{n}{n-k}$, and via $a = \binom{a}{1} = \binom{a}{a-1}$. Beyond these forced appearances, repeated values become scarce.

David Singmaster posed the question crisply around 1971: is there an absolute constant $C$ with $N(a) \le C$ for every $a > 1$? This is **Singmaster's conjecture**. Singmaster observed $N(a) \ge 6$ infinitely often, driven by a Fibonacci coincidence: the identity
$$\binom{F_{2i+2}F_{2i+3}}{F_{2i}F_{2i+3}} = \binom{F_{2i+2}F_{2i+3}-1}{F_{2i}F_{2i+3}+1},$$
where $F_j$ are Fibonacci numbers, produces infinitely many integers appearing at least six times. The smallest number known to appear six times is $3003 = \binom{3003}{1} = \binom{78}{2} = \binom{15}{5} = \binom{14}{6}$ (with mirror images). No integer is known to appear seven or more times, and whether $\sup_a N(a)$ is finite remains open.

## Formulation and reformulations

The bare conjecture asserts $\sup_{a>1} N(a) < \infty$. A decisive structural observation, due to Abbott, Erdős, and Hanson (1974), is that almost all multiplicity must come from small $k$: for $k \ge 2$ the values $\binom{n}{k}$ grow polynomially in $n$, so a number near magnitude $a$ can be a value $\binom{n}{k}$ for only a controlled range of $n$. The problem thus reduces to bounding solutions of low-degree Diophantine equations such as $\binom{n}{2} = \binom{m}{3}$, $\binom{n}{2} = \binom{m}{4}$, and $\binom{n}{3} = \binom{m}{4}$ — connecting Singmaster's conjecture to integral points on curves and to Faltings/Siegel finiteness. A statistical reformulation asks for the bound to hold on average, or outside a sparse exceptional set, which is the form in which the strongest modern results are stated.

## Timeline

- **1971** — David Singmaster poses the conjecture that the multiplicity $N(a)$ of any integer $a>1$ in Pascal's triangle is bounded by an absolute constant; he records $3003$ as the least number occurring six times.
- **1971** — Singmaster notes the Fibonacci-driven family giving $N(a) \ge 6$ infinitely often.
- **1974** — Harvey Abbott, Paul Erdős, and Denis Hanson prove the first nontrivial upper bound, commonly cited as $N(a) = O\!\left(\log a / \log\log a\right)$ — the benchmark unconditional bound, still essentially unimproved.
- **1976** — Erdős popularizes the problem in his problem lists, conjecturing the true answer is that $N(a) \le 8$ for all large $a$ and that $8$ is attained only finitely often, if at all.
- **1980s** — Effective Diophantine methods (Baker's theory of linear forms in logarithms, Thue/Thue–Mahler equations) settle finiteness of solutions for individual equations $\binom{n}{2}=\binom{m}{\ell}$.
- **1988** — Work of de Weger and others gives explicit, complete solution sets for equations like $\binom{n}{2}=\binom{m}{4}$.
- **1990s–2000s** — Siegel's theorem and Faltings's theorem yield finiteness of solutions for each fixed pair $(k,\ell)$ with the associated curve of genus $\ge 1$; computational searches confirm no $a \le 10^{60}$ appears more than six times.
- **2017** — Hugo Spiess / contributors to the Polymath-style discussion sharpen heuristics suggesting that $N(a) = 8$ should happen at most finitely often.
- **2021** — Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, and Joni Teräväinen (arXiv:2106.03335) prove that the number of solutions of $\binom{n}{k}=a$ in the nontrivial range $k \ge 3$, $a \le N$ is $O(N^{2/3})$ (improving the trivial $O(N \log N)$), giving strong control on the average multiplicity — the current analytic frontier.
- **Present** — A uniform bound $N(a) \le C$ for *all* $a$ remains unproven; no number is known to appear $> 6$ times, and even $N(a) \le 8$ for every $a$ is open unconditionally.
