# Operation Asymmetric Hydra: Five-Vector Convergent Asymmetric, Game-Theoretic, Adelic & Tropical Audit of the Collatz Map (`v0.10.0`, 2026-11-27)

> **Epistemic Status & Explicit Non-Claim:** Every theorem cited from `lean/FormalAtlas/Collatz.lean` is machine-checked across six independent Lean 4.35.0 kernels (zero `sorry`, zero custom axioms). Every finite measurement below comes verbatim from `problems/collatz-conjecture/experiments/results/collatz_asymmetric_hydra_20261127.json`, compiled cleanly under `-std=c17 -Wall -Wextra -Werror` (Windows GCC 16.1 + Linux LP64 `zig cc`), audited with 250,000 UBSan fuzz cases (`0` traps), and differentially cross-verified bit-for-bit against an independent 100%-safe Rust oracle (`problems/collatz-conjecture/native/collatz_hydra_oracle.rs`, zero `unsafe`). **The Collatz Conjecture remains OPEN.** Nothing in this document proves global convergence, excludes unbounded divergent trajectories, or rules out nontrivial positive cycles with $o \ge 5$ odd steps.

---

## 1. Executive Purpose & Sibling-Control Discipline

Earlier work in this repository established an empirical **$\varepsilon$-invariance filter** (see `SIBLING-CONTROL.md` and Lean theorem `thm_collatz_epsilon_invariance_barrier`): any attack relying purely on 2-adic parity-word bijections, cylinder measures, or $3^o / 2^d$ slope heuristics applies equally to the $\varepsilon = -1$ sibling map $T_-(x) = (3x-1)/2$, which admits nontrivial positive cycles at $5$ (period $3$, $o=2$) and $17$ (period $11$, $o=7$).

In `v0.10.0`, we pair **five new machine-checked Lean 4.35.0 theorems** (Collatz formal core expanded from 31 to **36 theorems**) with **five independent, unconventional, sibling-calibrated computational vectors** implemented in a catalytic native C17/Safe-Rust instrument (`collatz_asymmetric_hydra.c`, total wall-clock runtime **1.12 s** on a consumer laptop with zero heap explosion):

1. **Vector A — Dual-Prime Adelic Pincer ($\mathbb{Z}_2 \times \mathbb{Z}_3 \times \mathbb{Z}_5 \times \mathbb{Z}_7 \times \mathbb{R}$)**
2. **Vector B — Two-Player Zero-Sum Minimax Carry-Adversary Game ("Demon Integer" Frontier, $B = 4 \dots 22$)**
3. **Vector C — Binary Carry-Avalanche Shockwave & Chiral Two's-Complement Asymmetry**
4. **Vector D — Tropical / Max-Plus Karp Cycle-Mean Attack on Mixed-Base Adelic Quotients $\mathbb{Z}/(2^a 3^b)\mathbb{Z}$ + Archimedean Box Break**
5. **Vector E — Symbolic LZ76 Phrase Complexity, Run-Length & Autocorrelation Spectrum**

---

## 2. Five New Machine-Checked Lean 4.35.0 Theorems (`FormalAtlas.Collatz` §VIII)

All five theorems are verified with zero `sorry`, zero `native_decide`, and strictly standard axioms `{propext, Classical.choice, Quot.sound}` across all six independent kernels (`lean`, `leanchecker-paranoid`, `lean4lean`, `nanoda_bin`, `con-leche`, `con-ron`):

| Theorem (`FormalAtlas.Challenge`) | Statement | Structural Role |
|---|---|---|
| `thm_collatz_sign_conjugacy` | $\forall d, x,\ T^d(-x) = -T_-^d(x) \land o(T,d,-x) = o(T_-,d,x)$ | Exact chiral involution mapping $3n+1$ on $\mathbb{Z}_{<0}$ to $3n-1$ on $\mathbb{Z}_{>0}$; explains why every purely modular attack inherits $G_+(M) \cong G_-(M)$. |
| `thm_collatz_mod3_chiral_asymmetry` | $\forall x,\ 2 \nmid x \implies T(x) \equiv 2 \pmod 3 \land T_-(x) \equiv 1 \pmod 3$ | Exact $\varepsilon$-sensitive mod-3 phase-lock asymmetry breaking the 2-adic mirror. |
| `thm_collatz_intercept_not_div3` | $\forall w,\ o(w) \ge 1 \implies 3 \nmid c(w)$ | Universal 3-adic unit law for every non-trivial affine intercept and rational periodic spine $\rho_w$. |
| `thm_collatz_cycle_no_div3` | $\forall d \ge 1, x \ne 0,\ T^d(x) = x \implies 3 \nmid x$ | Global 3-adic exclusion: NO nonzero multiple of $3$ can EVER lie on any positive or negative Collatz cycle of any period $d \ge 1$. |
| `thm_collatz_positive_cycle_four_odd` | $\forall d \ge 1, x > 0,\ T^d(x) = x \land o = 4 \implies d = 8 \land x \in \{1, 2\}$ | Unconditional 4-odd-step positive-cycle exclusion for ALL periods $d \ge 1$ (odd-quotient parity elimination, 3-adic obstruction killing $q=3$ at $d=8$, and exact 2-adic valuation cascade mod $128$). |

---

## 3. Exact Empirical Results Across All Five Vectors

### Vector A — Dual-Prime Adelic Pincer ($\mathbb{Z}_2 \times \mathbb{Z}_3 \times \mathbb{Z}_5 \times \mathbb{Z}_7 \times \mathbb{R}$)

- **Mod-3 Chiral Asymmetry Check:** `500,000 / 500,000` odd integers in $[1, 10^6)$ satisfy $T(x) \equiv 2 \pmod 3$ and $T_-(x) \equiv 1 \pmod 3$ (`100%`, matching `thm_collatz_mod3_chiral_asymmetry`).
- **3-Adic Intercept Unit Law:** `491 / 491` primitive supercritical Lyndon spines ($d \le 14$) satisfy $3 \nmid c(w)$ (`0` violations, matching `thm_collatz_intercept_not_div3`).
- **Mod-9 Chiral Pile-Up Inversion:** Across all 491 supercritical spines, the mod-9 intercept distribution exhibits a dramatic chiral concentration that **inverts under $\varepsilon \mapsto -\varepsilon$**:
  - $3n+1$ (`mod 9` histogram `[0..8]`): `[0, 22, 25, 0, 54, 208, 0, 80, 102]` — **42.4%** (`208/491`) pile up on $c(w) \equiv 5 \pmod 9$.
  - $3n-1$ (`mod 9` histogram `[0..8]`): `[0, 102, 80, 0, 208, 54, 0, 25, 22]` — **42.4%** (`208/491`) invert to $c_-(w) \equiv 4 \pmod 9$.
  - Classes `{0, 3, 6} mod 9` carry identically `0` mass.
- **Joint Adelic Product-Formula Profile (`6,860` distinct spine pairs $s \le 8, t \le 14$; `27` deep $v_2 \ge 10$ collisions):**
  - All pairs: mean $(v_3, v_5, v_7, \log_2 |\Delta|_\infty) = (3.441, 0.253, 0.167, 22.449)$, with peaks $(v_2, v_3, v_5, v_7) = (13, 17, 4, 5)$.
  - High-$v_2$ collision tail ($v_2 \ge 10$): mean $(v_3, v_5, v_7, \log_2 |\Delta|_\infty) = (3.593, 0.370, 0.222, 20.653)$ — high 2-adic collision pairs exhibit **smaller** Archimedean separation ($\Delta\log_2|\Delta|_\infty = -1.796$ bits) accompanied by elevated $p$-adic valuations across $p \in \{3, 5, 7\}$.
- **Sibling-Control Verdict:** **PASS** (mod-3 and mod-9 intercept distributions cleanly separate $3n+1$ from $3n-1$; however, without positivity bounds, spine separations alone do not exclude cycles of arbitrary period).

---

### Vector B — Two-Player Zero-Sum Minimax Collatz Carry-Adversary Game

We formulate Collatz as an asymmetric zero-sum game on bit-width $B$: **Adversary** picks an odd starting integer $n \in [3, 2^B)$ to maximize stopping delay $\sigma(n)$, total flight $\tau(n)$, peak supercritical excess $E_{\max}(n) = \max_d (o(d) - \theta d)$ ($\theta = \log_3 2 \approx 0.630930$), or altitude amplification $\log_2(\max_d T^d(n)/n)$; **Gravity** applies deterministic $T$. Exhaustive catalytic scan of all **2,097,151 odd integers** $< 2^{22}$ (`1.10 s`, zero heap):

| Bit Width $B$ | Odd Starts | Stop Demon $n^*_{\text{stop}}$ ($\sigma$) | Total Demon $n^*_{\text{tot}}$ ($\tau$) | Excess Demon $n^*_{\text{exc}}$ ($E_{\max}$) | Peak Altitude ($\log_2$) | $3n-1$ Sibling Escape to $\{5, 17\}$ Cycles |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 7 | `7` (7) | `9` (13) | `15` (+1.476) | 2.42 | **57.14%** (`4/7` → 5-cycle) |
| 6 | 31 | `27` (59) | `55` (71) | `27` (+4.608) | 7.42 | **70.97%** (`10`→5, `12`→17) |
| 8 | 127 | `27` (59) | `231` (81) | `27` (+4.608) | 7.42 | **61.42%** (`37`→5, `41`→17) |
| 10 | 511 | `703` (81) | `871` (113) | `703` (+4.715) | 7.48 | **67.32%** (`162`→5, `182`→17) |
| 12 | 2,047 | `703` (81) | `3,711` (150) | `1,819` (+5.334) | 8.46 | **67.61%** (`664`→5, `720`→17) |
| 14 | 8,191 | `10,087` (105) | `13,255` (174) | `9,663` (+6.596) | 10.45 | **67.38%** (`2,667`→5, `2,852`→17) |
| 16 | 32,767 | `35,655` (135) | `52,527` (214) | `60,975` (+7.728) | 12.25 | **66.70%** (`10,536`→5, `11,320`→17) |
| 18 | 131,071 | `35,655` (135) | `230,631` (278) | `159,487` (+9.917) | 15.72 | **67.06%** (`42,190`→5, `45,702`→17) |
| 20 | 524,287 | `1,027,431` (183) | `837,799` (329) | `159,487` (+9.917) | 15.72 | **67.22%** (`169,868`→5, `182,577`→17) |
| **22** | **2,097,151** | **`1,126,015` (224)** | **`3,732,423` (374)** | **`3,873,535` (+10.573)** | **16.76** | **67.23%** (`680,067`→5, `729,892`→17, `0` other) |

- **Key Game-Theoretic Finding:** Under $3n-1$, the Adversary wins **$V_-(B) = +\infty$** for every $B \ge 3$ and captures **67.23%** of the odd integer line into the $\{5\}$-cycle (`32.43%`) and $\{17\}$-cycle (`34.80%`) basins. Under $3n+1$, the Adversary captures **0 / 2,097,151 (0.000%)**, and the optimal Excess Demons (`15`, `9663`, `60975`, `159487`, `3873535`) all purchase their temporary supercritical ascent by burning trailing `1`-bit runs ($n \equiv -1 \pmod{2^r}$, e.g., $3{,}873{,}535 \equiv 127 \pmod{128}$), yielding a linear-in-$B$ entropy budget ceiling ($\approx 0.48 B$ odd steps above $\theta d$).
- **Sibling-Control Verdict:** **PASS** (sharp macroscopic separation between finite $V_+(B)$ and infinite $V_-(B) = +\infty$ capturing 67.23% of starts).

---

### Vector C — Binary Carry-Avalanche Shockwave & Chiral Two's-Complement Asymmetry

Across all **524,288 odd integers** in $[1, 2^{20})$ (`0.004 s`):

| Metric | $3n+1$ | $3n-1$ (Sibling Control) | $5n+1$ (Divergent Control) | Interpretation |
|---|---:|---:|---:|---|
| Mean carry bits (`popcount(carry_mask)`) | **12.833332** | **9.833334** | 12.500000 | **$3n+1$ fires exactly `+3.000` more binary carry bits/step than $3n-1$** via mandatory bit-0 carry avalanche. |
| Max carry bits ($x < 2^{20}$) | **22** | **20** | — | Extra overflow carry into MSB under $+1$. |
| Mean Hamming-weight drift $\Delta H$ | **-0.333332** | **-0.333334** | **0.000000** | Exact $-1/3$ bit/step compression shared by $3n\pm 1$ (fails $\varepsilon$-separation; separates $3n\pm 1$ from $5n+1$). |
| Mean $v_2(3x \pm 1)$ on $x \equiv 15 \pmod{16}$ | **1.000000** | **2.000000** | — | Chiral trailing-1 mirror: $+1$ traps $v_2 = 1$ on trailing `1`s while $-1$ releases $v_2 \ge 2$. |
| Mean $v_2(3x \pm 1)$ on $x \equiv 1 \pmod{16}$ | **2.000000** | **1.000000** | — | Exact dual mirror: $-1$ traps $v_2 = 1$ on trailing `0001` while $+1$ releases $v_2 \ge 2$. |
| Signed conjugacy $T^{12}(-x) = -T_-^{12}(x)$ | `100,000 / 100,000` (`0` mismatches) | — | — | Exact empirical confirmation of Lean `thm_collatz_sign_conjugacy`. |

- **Sibling-Control Verdict:** **MIXED (HONEST DIAGNOSTIC)** — carry-avalanche bit count (`12.833` vs `9.833`) and trailing-1/trailing-0001 $v_2$-chiral swap cleanly separate $+1$ from $-1$; mean Hamming drift $\Delta H = -1/3$ is **$\varepsilon$-blind** (identical for $3n+1$ and $3n-1$) and is therefore explicitly flagged as non-discriminating between $+1$ and $-1$.

---

### Vector D — Tropical / Max-Plus Karp Cycle-Mean Attack on Mixed-Base Adelic Quotients $\mathbb{Z}/(2^a 3^b)\mathbb{Z}$ + Archimedean Box Break

For every mixed-base adelic modulus $M = 2^a \cdot 3^b$ ($a \ge 2, b \ge 1$), the shortcut map $T_\varepsilon$ projects onto an exact $M$-state, out-degree-2 weighted transition automaton $G_\varepsilon(M)$ with edge weights $w(u \to v) = u \bmod 2 \in \{0, 1\}$. Using Karp's exact cleared-denominator rational Tropical Maximum Cycle Mean algorithm (`0.017 s`):

| Modulus $M = 2^a \cdot 3^b$ | Active States ($3 \nmid u$, no self-loop) | Odd $\to 0 \pmod 3$ Edges | $\mu^*_{\text{raw}}(+)$ / $\mu^*_{\text{raw}}(-)$ | $\mu^*_{\text{pruned}}(+)$ | $\mu^*_{\text{pruned}}(-)$ | Mirror Exact Equal? |
|---:|---:|---:|---:|---:|---:|:---:|
| $12 = 2^2 \cdot 3^1$ | 7 | `0` | `1/1` / `1/1` | **`2/3`** (`0.6667`) | **`2/3`** | **YES** |
| $24 = 2^3 \cdot 3^1$ | 15 | `0` | `1/1` / `1/1` | **`3/4`** (`0.7500`) | **`3/4`** | **YES** |
| $36 = 2^2 \cdot 3^2$ | 23 | `0` | `1/1` / `1/1` | **`3/4`** (`0.7500`) | **`3/4`** | **YES** |
| $48 = 2^4 \cdot 3^1$ | 31 | `0` | `1/1` / `1/1` | **`4/5`** (`0.8000`) | **`4/5`** | **YES** |
| $72 = 2^3 \cdot 3^2$ | 47 | `0` | `1/1` / `1/1` | **`4/5`** (`0.8000`) | **`4/5`** | **YES** |
| $96 = 2^5 \cdot 3^1$ | 63 | `0` | `1/1` / `1/1` | **`5/6`** (`0.8333`) | **`5/6`** | **YES** |
| $144 = 2^4 \cdot 3^2$ | 95 | `0` | `1/1` / `1/1` | **`5/6`** (`0.8333`) | **`5/6`** | **YES** |
| $192 = 2^6 \cdot 3^1$ | 127 | `0` | `1/1` / `1/1` | **`6/7`** (`0.8571`) | **`6/7`** | **YES** |
| $288 = 2^5 \cdot 3^2$ | 191 | `0` | `1/1` / `1/1` | **`6/7`** (`0.8571`) | **`6/7`** | **YES** |
| $576 = 2^6 \cdot 3^2$ | 383 | `0` | `1/1` / `1/1` | **`7/8`** (`0.8750`) | **`7/8`** | **YES** |

**Exact Empirical Discovery — The Tropical Modular Mirror Law:**
1. Every single modulus satisfies `mod3_odd_to_zero_edges = 0` (exact automaton reflection of Lean `thm_collatz_cycle_no_div3`).
2. Across ALL 10 mixed-base moduli, $\mu^*(G_+^{\text{pruned}}(2^a 3^b)) = \mu^*(G_-^{\text{pruned}}(2^a 3^b)) = \dfrac{a+b-1}{a+b} \to 1 > \theta$!
3. **Why purely modular tropical attacks CANNOT prove Collatz:** By Lean `thm_collatz_sign_conjugacy`, $\phi(u) = (-u) \bmod M$ is an **exact weight-preserving digraph isomorphism** $G_+(M) \cong G_-(M)$. Even after removing $3 \mid u$ and the $-1$ fixed point, modular ghost walks orbit arbitrarily close to $-1$ for $a+b-1$ consecutive odd steps, pushing the tropical spectral radius monotonically to $1$.
4. **The Archimedean Positivity Break:** The moment positivity is enforced on finite integer boxes $[1, N]$ ($N \in \{20, 50, 150, 500\}$), the mirror shatters completely:
   $$\mu^*_{\text{box}, +}([1, N]) = \frac{1}{2} = 0.500000 < \theta \approx 0.630930 < \frac{2}{3} = 0.666667 = \mu^*_{\text{box}, -}([2, N]).$$
- **Sibling-Control Verdict:** **NO-GO DIAGNOSED ON MODULAR QUOTIENTS (`FAIL`, proved via sign-conjugacy mirror); PASS ON ARCHIMEDEAN POSITIVE BOXES.**

---

### Vector E — Symbolic LZ76 Phrase Complexity & Autocorrelation Spectrum

| Orbit Label | Seed $n$ | Map | Word Len $L$ | Odd Density $o/L$ | LZ76 Phrases $c$ | Normalized LZ76 $c\log_2 L / L$ | Max Odd Run | Lag-1 Autocorr $r_1$ | Lag-2 Autocorr $r_2$ |
|---|---:|:---:|---:|---:|---:|---:|---:|---:|---:|
| `demon_B6_27` | `27` | $3n+1$ | 70 | 0.5857 | 14 | **1.2259** | 6 | +0.0136 | +0.0285 |
| `demon_top_total_Bmax` | `3,732,423` | $3n+1$ | 374 | 0.5936 | 47 | **1.0741** | 11 | +0.0163 | +0.0413 |
| `demon_top_excess_Bmax` | `3,873,535` | $3n+1$ | 206 | 0.5631 | 28 | **1.0448** | 9 | +0.0184 | +0.0034 |
| `typical_odd_1000003` | `1,000,003` | $3n+1$ | 77 | 0.4675 | 15 | **1.2208** | 7 | +0.2335 | -0.0179 |
| `sibling_3n_minus_1_cycle5` | `5` | $3n-1$ | 256 | **0.6680** | **3** | **0.0938** | 2 | **-0.5010** | **-0.4990** |
| `sibling_3n_minus_1_cycle17` | `17` | $3n-1$ | 256 | **0.6406** | **5** | **0.1563** | 4 | +0.2182 | -0.1765 |

- **Key Symbolic Finding:** Even the worst-case adversarial Minimax Demons under $3n+1$ (`3,732,423` and `3,873,535`) exhibit **pseudorandom, maximally incompressible parity words** (`LZ76_norm = 1.045–1.074`, $|r_1|, |r_2| < 0.042$), in stark contrast to the collapsed low-entropy periodic attractors of $3n-1$ (`LZ76_norm = 0.094–0.156`, odd density $> \theta$).

---

## 4. Honest Five-Vector Convergence & Sibling-Control Matrix

| Vector | Breaks $\varepsilon$-Symmetry? | Lean Kernel Anchor | Independent Rust Cross-Check | What It Actually Proves / Diagnoses |
|---|:---:|---|:---:|---|
| **A. Adelic Pincer** | **YES** (mod 3 & mod 9 inversion) | `thm_collatz_mod3_chiral_asymmetry`, `thm_collatz_intercept_not_div3`, `thm_collatz_cycle_no_div3` | **Bit-exact PASS** | Unconditionally excludes $3 \mid x$ from ALL nonzero cycles; quantifies mod-9 chiral pile-up & $(v_2,v_3,v_5,v_7)$ trade-off. |
| **B. Minimax Carry-Adversary Game** | **YES** ($V_+$ finite vs $V_- = \infty$, 67.23% escape) | `thm_collatz_cycle_amplitude_ceiling`, `thm_collatz_positive_cycle_four_odd` | **Bit-exact PASS** | Maps exact Demon frontier to $2^{22}$; shows supercritical excess requires trailing-1 entropy purchase. |
| **C. Carry-Avalanche Shockwave** | **PARTIAL** (`+3.000` carry bits & trailing-1 swap YES; $\Delta H = -1/3$ NO) | `thm_collatz_sign_conjugacy` | **Bit-exact PASS** | Isolates exact binary hardware asymmetry (`12.833` vs `9.833` carries) while honestly rejecting $\varepsilon$-blind $\Delta H$. |
| **D. Tropical Karp Quotient** | **NO on $\mathbb{Z}/M\mathbb{Z}$** ($\frac{a+b-1}{a+b}$ mirror); **YES on $[1, N]$** ($\frac{1}{2} < \theta < \frac{2}{3}$) | `thm_collatz_sign_conjugacy`, `thm_collatz_cycle_no_div3` | **Bit-exact PASS** | Diagnoses exact Tropical Modular Mirror no-go ($G_+(M)\cong G_-(M)$) and exact Archimedean positivity threshold break. |
| **E. Symbolic LZ76 Complexity** | **YES** (`1.04–1.23` vs `0.09–0.16`) | — (empirical diagnostic) | **Bit-exact PASS** | Quantifies pseudorandomness of $3n+1$ Demon orbits vs collapsed periodicity of $3n-1$ attractors. |

**Bottom-Line Convergent Synthesis:** All five vectors independently converge on ONE stark structural conclusion: **every obstruction that separates $3n+1$ from $3n-1$ MUST couple the finite-precision $2$-adic / $3$-adic chiral asymmetry (`thm_collatz_mod3_chiral_asymmetry`, `+3.000` carry avalanche, `3 ∤ x`) directly with Archimedean positivity ($x > 0$)**; any purely modular or purely 2-adic/tropical quotient argument is provably blind to the sign conjugacy $T^d(-x) = -T_-^d(x)$ and therefore cannot rule out positive cycles.
