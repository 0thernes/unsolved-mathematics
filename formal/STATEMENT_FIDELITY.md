# Statement Fidelity Audit — `FormalAtlas` (Lean 4.35.0)

> **Purpose:** Machine-checked Lean proofs fail in the real world not because the kernel is wrong, but because a formal definition silently diverges from the mathematical literature (**representational mismatch**). This table maps every definition and headline theorem in [`FormalAtlas/Defs.lean`](FormalAtlas/Defs.lean) and [`Challenge.lean`](Challenge.lean) line-by-line to its primary mathematical source, non-vacuity witness, and exact epistemic boundary.

## 1. Trusted Definition Audit (`FormalAtlas/Defs.lean`)

| Lean Declaration | Informal Mathematical Object | Literature Anchor | Exactness / Fidelity Notes |
|---|---|---|---|
| `T : Int → Int` | Shortcut Collatz map $T(x) = x/2$ (even), $(3x+1)/2$ (odd) | Terras (1976), Lagarias (1985) | Defined over all $\mathbb{Z}$ using Euclidean `% 2` / `/ 2`; agrees on $\mathbb{Z}_{>0}$ and extends to negative cycles $\{-1, -5, -17\}$. |
| `TMinus : Int → Int` | Sibling $3n-1$ shortcut map $T_-(x) = x/2$ (even), $(3x-1)/2$ (odd) | Lagarias (1985); Atlas `SIBLING-CONTROL.md` | Exact $\varepsilon = -1$ control sharing identical parity-word combinatorics while admitting positive cycles $\{5,7,10\}$ and $\{17,\dots\}$. |
| `parityWord`, `oddCount` | Length-$d$ parity vector $w \in \{0,1\}^d$ and odd-step count $o(w)$ | Terras (1976) | `parityBit x := (x % 2 != 0)`; `wordOddCount` counts `true` bits identically. |
| `wordIntercept` | Exact affine intercept $c(w) \in \mathbb{Z}_{\ge 0}$ in $2^d T^d(x) = 3^o x + c(w)$ | Bernstein–Lagarias (1996); White Paper §3 | Proved exact in `thm_collatz_exact_intercept_law` for all $d \in \mathbb{N}, x \in \mathbb{Z}$. |
| `IsErdosStrausSol n x y z` | Positive integers $x,y,z > 0$ solving $\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$ | Erdős (1950); Mordell (1967) | Exact denominator-cleared integer equation $4xyz = n(yz + xz + xy)$ with $x,y,z > 0$; equivalent over $\mathbb{Q}$ since $n,x,y,z > 0$. |
| `FarEnough m p q v` / `WithinDist m p q v` | Circular distance $\|(p/q)\cdot v\| \ge 1/m$ (resp. $\le 1/m$) on $\mathbb{R}/\mathbb{Z}$ | Wills (1967), Cusick (1973) | Exact integer arithmetic via $r = (pv) \bmod q \in [0,q)$: $\min(r, q-r)/q \ge 1/m \iff q \le m r \land q \le m(q-r)$. Zero floating-point error. |
| `IsBrocardSol n m` | $n! + 1 = m^2$ over $\mathbb{N}$ | Brocard (1876), Ramanujan (1913) | Exact `Nat` equality `fact n + 1 = m * m`. |

## 2. Headline Theorem Fidelity & Non-Vacuity Audit (`Challenge.lean` ↔ `Solution.lean`)

| # | Challenge Theorem | Mathematical Claim | Literature Anchor | Non-Vacuity Witness (`NonVacuity.lean`) | Status |
|---|---|---|---|---|---|
| 1 | `thm_collatz_cylinder_affine_law` | $T^d(2^d q + r) = 3^{o(r,d)} q + T^d(r)$ | Terras (1976); White Paper Thm 3.1 | Unconditional ($\forall d, q, r$) | **Exact match** |
| 2 | `thm_collatz_exact_intercept_law` | $2^d T^d(x) = 3^o x + c(w)$ | Bernstein–Lagarias (1996) | Unconditional ($\forall d, x$) | **Exact match** |
| 3 | `thm_terras_parity_word_bijection` | $r \mapsto w_d(r)$ is a bijection $\{0,\dots,2^d-1\} \leftrightarrow \{0,1\}^d$ | Terras (1976), Thm 1.1 | Unconditional ($\forall d$) | **Exact match** |
| 4 | `thm_collatz_descent_certificate_sound` | $3^o < 2^d \land (2^d-3^o)q > T^d(r)-r \implies T^d(2^dq+r) < 2^dq+r$ | Terras (1976); White Paper Thm 3.3 | `witness_descent_certificate` ($d=2, r=1, q=1 \Rightarrow T^2(5)=4<5$) | **Exact match** |
| 5 | `thm_collatz_no_finite_subcritical_cover` | $T^d(-1) = -1$, $o(-1,d)=d$, $2^d \le 3^d$ (no finite subcritical cover of $\mathbb{Z}$) | Elementary 2-adic fixed point; White Paper Thm 3.4 | Unconditional ($\forall d$) | **Exact match** |
| 6 | `thm_collatz_spine_ladder_identity` | $2^d((2^d-3^o)T^d(x)-c) = 3^o((2^d-3^o)x-c)$ | White Paper Lemma 4.1 (cleared denominators) | Unconditional ($\forall d, x$) | **Exact match** |
| 7 | `thm_collatz_positivity_localization` | Every supercritical word ($3^o > 2^d$) has $c(w) \ge 3^o - 2^d$, i.e. $\rho_w \le -1$ | White Paper Cor. 4.2 (unconditional for all $d \ge 1$) | `witness_positivity_localization` (`[T,T,F]`, $c=5 \ge 1$, $\rho=-5$) + negative check `witness_subcritical_positive_cycle` | **Exact match** |
| 8 | `thm_collatz_epsilon_invariance_barrier` | $T_-$ shares exact Terras bijection yet has positive supercritical cycles at $5$ (len 3) and $17$ (len 11) | Atlas `SIBLING-CONTROL.md` & `EPSILON-BARRIER.md` | Explicit concrete cycles $T_-^3(5)=5$, $T_-^{11}(17)=17$ | **Exact match** |
| 9 | `thm_erdos_straus_mordell_840` | $\forall n \ge 2$ with $n \bmod 840 \notin \{1,121,169,289,361,529\}$, $\exists x,y,z > 0,\ \frac{4}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}$ | Mordell (1967), *Diophantine Equations* ch. 30 | `witness_erdos_straus_hypotheses` ($n=97$ non-exceptional; $n=121$ exceptional witness $(44,121,484)$) | **Exact match (834/840 classes = 99.29%)** |
| 10 | `thm_lonely_runner_sharpness_all_n` | For every $n \ge 1$ and rational $t = p/q$, speeds $\{1,\dots,n\}$ have $\exists i,\ \|t \cdot i\| \le \frac{1}{n+1}$ | Wills (1967) sharpness optimality | `witness_lonely_runner_concrete` ($n=2, t=1/3$) | **Exact match (over $\mathbb{Q}$; density extends to $\mathbb{R}$)** |
| 11 | `thm_lonely_runner_n1` | Lonely Runner Conjecture holds for $n=1$ (2 runners) | Wills (1967) | Explicit time $t = 1/(2v)$ | **Exact match** |
| 12 | `thm_lonely_runner_n2` | Lonely Runner Conjecture holds for $n=2$ (3 runners) | Wills (1967) | `witness_lonely_runner_concrete` ($v_1=3, v_2=10, t=1/6$) | **Exact match** |
| 13 | `thm_brocard_brown_solutions` | $(4,5), (5,11), (7,71)$ solve $n!+1 = m^2$ | Brocard (1876), Ramanujan (1913) | Concrete values | **Exact match** |
| 14 | `thm_brocard_exhaustive_le_12` | No other $n \le 12$ admits $m \in \mathbb{N}$ with $n!+1 = m^2$ | Elementary finite exhaustion | Negative check `witness_brocard_non_solution` ($6!+1=721$) | **Exact match** |

## 3. Explicitly NOT Proved (Hard Epistemic Boundary)

- **Collatz Conjecture (`OPEN`):** Proved NO convergence, NO divergence exclusion, and NO cycle exclusion for $3n+1$.
- **Erdős–Straus Conjecture (`OPEN` / `active-progress`):** The six quadratic-residue classes $\{1, 121, 169, 289, 361, 529\} \pmod{840}$ remain uncovered by polynomial identities; the general conjecture is NOT proved.
- **Lonely Runner Conjecture (`active-progress`):** Only global sharpness (all $n$) and base cases $n \in \{1, 2\}$ are formalized here; general uniform proof for all $n$ remains OPEN.
- **Brocard's Problem (`OPEN`):** Only $n \le 12$ is classified here; finiteness for all $n$ remains OPEN.

## 4. Exact `#print axioms` Audit Output (`VerifyAxioms.lean`, Lean 4.35.0)

Reproduced identically on local Windows (`lean 4.35.0`) and ephemeral Ubuntu CI ([Run `45263348677`](https://github.com/0thernes/unsolved-mathematics/actions/runs/45263348677)). Every exported theorem and non-vacuity witness depends strictly on subsets of `{propext, Classical.choice, Quot.sound}` (five require **zero axioms**):

```text
'FormalAtlas.Challenge.thm_collatz_cylinder_affine_law' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_exact_intercept_law' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_terras_parity_word_bijection' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_descent_certificate_sound' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_no_finite_subcritical_cover' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_spine_ladder_identity' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_positivity_localization' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_collatz_epsilon_invariance_barrier' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_erdos_straus_mordell_840' depends on axioms: [propext, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_sharpness_all_n' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_n1' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_lonely_runner_n2' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.Challenge.thm_brocard_brown_solutions' does not depend on any axioms
'FormalAtlas.Challenge.thm_brocard_exhaustive_le_12' depends on axioms: [propext, Quot.sound]
'FormalAtlas.NonVacuity.witness_descent_certificate' depends on axioms: [propext, Classical.choice, Quot.sound]
'FormalAtlas.NonVacuity.witness_positivity_localization' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_erdos_straus_hypotheses' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_lonely_runner_concrete' does not depend on any axioms
'FormalAtlas.NonVacuity.witness_brocard_non_solution' does not depend on any axioms
```

## 5. Multi-Kernel Replay Verdict (6/6 Independent Kernels)

All 14 challenge/solution theorem signatures passed `lake check --paranoid` and `lake comparator --config comparator.json --paranoid` inside a Linux `bubblewrap` sandbox on GitHub Actions (`ubuntu-latest`) as well as direct local replay across all six bundled Lean 4.35.0 kernels:
1. `lean` (C++ reference kernel) — **ACCEPT**
2. `leanchecker-paranoid --fresh` — **ACCEPT**
3. `lean4lean` (Lean-in-Lean verified kernel, 58,275 decls) — **ACCEPT**
4. `nanoda_bin` (Rust independent kernel, strict `{propext, Classical.choice, Quot.sound}` whitelist) — **ACCEPT**
5. `con-leche --verified` (58,278 decls) — **ACCEPT**
6. `con-ron --verified` (Rust arena checker, 58,278 decls) — **ACCEPT**
