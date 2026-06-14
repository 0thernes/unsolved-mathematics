# Attempts — The Hadamard Matrix Conjecture

_Notable attempts, near-misses, retracted proofs._

The Hadamard conjecture has the unusual character of being attacked almost entirely by **construction**: progress is measured by the shrinking list of unsettled orders rather than by failed grand proofs. There is no widely circulated *claimed proof of the full conjecture* in the refereed literature; the honest history is one of celebrated individual orders falling and asymptotic theorems narrowing the gap.

## The march of smallest open orders

For most of the twentieth century the frontier was the **smallest order not yet known to exist**, and clearing it was a notable event each time.

- **Order $92$.** Listed by Paley (1933) as open, it resisted for decades and became the canonical hard case. In **1962, Baumert, Golomb, and Hall** found a Williamson-type solution by computer at JPL, a landmark early use of machine search in pure mathematics.
- **Order $116, 156, 172, \dots$** Subsequent orders fell to Williamson sequences, Goethals–Seidel arrays, and base-sequence methods through the 1960s–1980s, largely via the Australian school around **Jennifer Seberry** and collaborators.
- **Order $428$.** This stood as the smallest open order for years until **Hadi Kharaghani and Behruz Tayfeh-Rezaie** announced a construction in 2004 (published 2005) using a Turyn-type sequence approach, a widely noted result.
- **Order $668$.** With $428$ resolved, $668 = 4 \cdot 167$ became — and remains — the smallest order for which existence is **undecided**. It lies outside Paley reach (since $167$ is prime but $q+1=168$ and $2(q+1)$ patterns do not deliver it directly) and has resisted Williamson, base-sequence, and SAT-based searches.

## Near-misses and provable local failures

Several methods have been shown to **provably fail at specific orders**, which is itself substantive knowledge:

- **Williamson matrices of order $4 \cdot 35 = 140$** were shown by exhaustive search not to exist in symmetric circulant form, demonstrating that Williamson's elegant method is not a universal route and that other constructions must cover such orders. Similar non-existence of Williamson-type solutions has been established computationally at additional orders.
- **Circulant Hadamard matrices.** A separate, sharper conjecture (often attributed to **Ryser**) asserts there is *no* circulant Hadamard matrix of order $> 4$. This is widely believed and verified for enormous ranges (e.g. all orders below very large bounds), but is itself **unproven**; it is a cautionary sibling showing how delicate $\pm1$ orthogonality questions can be. It does **not** contradict the Hadamard conjecture, which permits non-circulant constructions.

## Asymptotic "almost-proofs"

The closest the field has come to a general theorem are the **asymptotic existence results**. Turyn's 1970s arguments and **Seberry's 1985** theorem (order $2^t m$ exists for $t \ge 2\log_2(m-3)$) effectively prove "a Hadamard matrix of order $4m$ exists for *almost all* $m$ once a sufficient power of two is allowed." Later refinements by **Craigen, de Launey, and Gordon** reduced the exponent, and conditional results assuming number-theoretic hypotheses bring it closer to constant. These are genuine theorems, not disputed claims — but none reaches the required exponent $t = 2$ for *all* $m$, so the conjecture stands.

## Status of "proof" claims

No retracted or seriously disputed *complete* proof of the conjecture is recorded in the mainstream literature, which distinguishes this problem from, say, the abc conjecture. Occasional informal or preprint-level claims to settle particular open orders appear and are checked against the existence tables maintained by the community (notably the long-running survey table due to **Seberry** and to **Craigen–Kharaghani**); when a construction is correct it is absorbed into those tables, and when it is not it quietly fails verification. The neutral summary is: the conjecture is **open**, the smallest unsettled order is **$668$**, and the strongest unconditional general results remain asymptotic.
