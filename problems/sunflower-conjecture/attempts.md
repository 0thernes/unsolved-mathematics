# Attempts — The Sunflower Conjecture

_Notable attempts, near-misses, retracted proofs._

## The classical ceiling: Kostochka's bound

For nearly four decades after 1960, the only substantive movement on the $k=3$ case was a sequence of incremental sharpenings of the Erdős–Rado induction, culminating in **Kostochka's 1997 result**, $f(w,3) \le c\, w!\,(\log\log\log w / \log\log w)^w$. This was widely regarded as the limit of the inductive approach and stood as the best known bound until 2019. It is a genuine improvement but only a $(1-o(1))^w$ factor below $w!$ — it never escapes the super-exponential regime the conjecture predicts is wrong. Its long reign is the clearest evidence that the problem required a new idea rather than a better calculation.

## The near-miss that reframed the problem: ALWZ 2019

The single most important near-miss is **Alweiss, Lovett, Wu, and Zhang (2019)**, *"Improved bounds for the sunflower lemma."* By introducing the spread/sampling machinery they proved $f(w,k) \le (C k^3 \log w \log\log w)^w$ — collapsing the bound from $\sim w!$ all the way down to base **polylogarithmic** in $w$. This is the closest anyone has come: it leaves only a $\log w$ factor between the known bound and the conjecture's $C(k)^w$. It is not a proof of the conjecture, and the authors were explicit that the residual logarithm appeared intrinsic to their method. The work won the **2022 Hollis Cooley / FOCS-era recognition** in the community and is the basis of all subsequent progress.

## Simplifications that did not close the gap

Two influential follow-ups deserve mention as "famous partial results" rather than near-misses, because each reproduced the ALWZ bound by a cleaner route without improving the exponent's dependence on $w$:

- **Rao (2020)** and **Tao (2020, expository blog/notes)** independently reformulated the spread lemma via Shannon-entropy encoding, giving the clean $f(w,k) \le (C k \log w)^w$ with markedly simpler proofs. Tao's exposition in particular made the argument accessible and is frequently cited as the canonical write-up.
- **Bell, Chueluecha, and Warnke (2021)**, *"Note on sunflowers,"* optimized constants and removed extraneous factors, giving the sharpest current form of the bound. Again the $\log w$ remained.

These are correct, accepted results; they sharpen the constant and the proof but not the regime.

## On disputed or retracted claimed proofs

The sunflower conjecture has a comparatively clean record. **No widely-circulated, peer-reviewed claim of a full proof of $f(w,k) \le C(k)^w$ has been accepted, and the author is not aware of a prominent retracted preprint claiming the complete conjecture.** As with any famous prize problem, informal or unrefereed claims of removing the final $\log w$ have appeared from time to time on preprint servers and discussion forums; none has gained acceptance, and they should be treated as unverified absent independent confirmation. This dossier deliberately does not name or endorse any such claim, because the author cannot verify a specific, citable dispute with confidence — and the house rule is honesty over completeness. The reliable statement is: the residual $\log w$ has not been removed in any accepted work, and the full conjecture remains open.

## Lower-bound side

On the construction side, the relevant "attempt" is to push the lower bound $f(w,k) \ge (k-1)^w$ upward and so prove the conjecture *false*. No such super-exponential lower bound is known; the best constructions remain at the $(k-1)^w$ scale (with lower-order improvements), consistent with — and widely believed to confirm — the conjecture being true. The gap between the proven upper bound $(C k \log w)^w$ and the lower bound $(k-1)^w$ is therefore the live arena.
