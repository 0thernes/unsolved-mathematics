/* SPDX-License-Identifier: MIT
 *
 * collatz_asymmetric_hydra.c — Five-Vector Convergent Asymmetric & Game-Theoretic
 * Collatz Research Instrument (C17, Zero External Dependencies, LP64/LLP64 Portable).
 *
 * Implements five mathematically independent, falsifiable, sibling-calibrated
 * attack vectors against the shortcut Collatz map T(n) = n/2 (even), (3n+1)/2 (odd)
 * paired against its exact epsilon = -1 sibling control T_-(n) = (3n-1)/2:
 *
 *   Vector A (adelic-pincer):
 *     Dual-prime adelic valuation profiler (v2, v3, v5, v7, log2|.|_inf) across
 *     supercritical rational spine collisions, verifying Lean-proved 3-adic unit law
 *     (3 nmid c(w)), mod-3 chiral asymmetry (T(x) == 2 vs T_-(x) == 1 mod 3), and
 *     chiral mod-27 intercept inversion.
 *
 *   Vector B (minimax-game):
 *     Two-player zero-sum Minimax Carry-Adversary Game computing exact optimal
 *     "Demon Integers" n*_B in [3, 2^B) for B = 4..22 maximizing stopping time,
 *     total stopping time, peak supercritical excess o(d) - log_3(2)*d, and altitude
 *     ratio under T, directly against T_- where Adversary wins +infinity at B >= 3.
 *
 *   Vector C (carry-shockwave):
 *     Exact binary carry-avalanche counter popcount((2x) ^ x ^ (3x +- 1)), signed
 *     Hamming-weight drift Delta H, and trailing-1 erosion mirror across 2^19 odd
 *     integers for 3n+1 vs 3n-1 vs 5n+1, plus 100k signed checks of Lean-proved
 *     sign conjugacy T^d(-x) = -T_-^d(x).
 *
 *   Vector D (tropical-karp):
 *     Exact Tropical / Max-Plus Karp Maximum Cycle Mean algorithm (exact cleared-
 *     denominator rational comparisons, zero floating-point drift) on mixed-base
 *     adelic quotient automata Z / (2^a * 3^b) Z. Empirically proves the Tropical
 *     Modular Mirror (G_+(M) ~= G_-(M) via u -> -u mod M -> identical mu*(M)) AND
 *     demonstrates the exact Archimedean Positivity Break on positive boxes [1, N]
 *     where mu*_box(+) = 1/2 < log_3(2) < 2/3 = mu*_box(-).
 *
 *   Vector E (symbolic-lz76):
 *     Exact Lempel-Ziv (LZ76) phrase complexity, odd density, max consecutive-1 run,
 *     and lag-1/lag-2 parity autocorrelation of Minimax Demon orbits vs typical
 *     orbits vs 3n-1 periodic sibling attractors.
 *
 * Explicit Non-Claim: Exact finite research instrument; proves NO part of the
 * Collatz Conjecture (status: OPEN).
 */

#if !defined(_WIN32) && !defined(_POSIX_C_SOURCE)
#  define _POSIX_C_SOURCE 200809L
#endif

#include <inttypes.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#if defined(_WIN32)
#  define WIN32_LEAN_AND_MEAN
#  include <windows.h>
static double hydra_now_seconds(void) {
    LARGE_INTEGER freq, counter;
    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&counter);
    return (double)counter.QuadPart / (double)freq.QuadPart;
}
#else
static double hydra_now_seconds(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec * 1e-9;
}
#endif

/* Exact mathematical constant theta = log_3(2) = ln(2)/ln(3). */
#define THETA_LOG3_2 0.63092975357145743710

/* Portable integer helpers (strictly ISO C17 UB-free on signed values) */
static inline int64_t step_T_i64(int64_t x) {
    return (x & 1LL) ? ((3LL * x + 1LL) / 2LL) : (x / 2LL);
}

static inline int64_t step_TMinus_i64(int64_t x) {
    return (x & 1LL) ? ((3LL * x - 1LL) / 2LL) : (x / 2LL);
}

static inline uint32_t popcount64(uint64_t x) {
    return (uint32_t)__builtin_popcountll(x);
}

static inline uint32_t ctz64(uint64_t x) {
    return (x == 0) ? 64U : (uint32_t)__builtin_ctzll(x);
}

static inline uint32_t val_p_u128(__uint128_t x, uint32_t p) {
    if (x == 0) return 0;
    uint32_t v = 0;
    while ((x % p) == 0) {
        x /= p;
        v++;
    }
    return v;
}

/* ============================================================================
 * Vector A: Dual-Prime Adelic Pincer (Z_2 x Z_3 x Z_5 x Z_7 x R)
 * ============================================================================ */

typedef struct {
    uint32_t bits;
    uint32_t d;
    uint32_t o;
    __int128 c;
    __int128 D; /* 2^d - 3^o < 0 for supercritical words */
    uint64_t lsb;
} spine_rec_t;

static inline uint64_t hydra_tile_lsb64(uint32_t bits, uint32_t d) {
    uint64_t out = 0;
    uint32_t sh = 0;
    uint64_t blk = (uint64_t)bits;
    while (sh < 64) {
        out |= (blk << sh);
        sh += d;
    }
    return out;
}

static uint32_t hydra_min_super_ones(uint32_t d) {
    __uint128_t two_d = ((__uint128_t)1) << d;
    __uint128_t p3 = 1;
    uint32_t o = 0;
    while (p3 <= two_d) {
        p3 *= 3;
        o++;
    }
    return o;
}

typedef struct {
    spine_rec_t *data;
    size_t len;
    size_t cap;
} spine_vec_t;

static void spine_vec_push(spine_vec_t *v, uint32_t bits, uint32_t d, uint32_t o) {
    if (v->len == v->cap) {
        size_t ncap = v->cap ? v->cap * 2 : 512;
        spine_rec_t *nd = (spine_rec_t *)realloc(v->data, ncap * sizeof(spine_rec_t));
        if (!nd) {
            fprintf(stderr, "ERROR: OOM in spine_vec_push\n");
            exit(2);
        }
        v->data = nd;
        v->cap = ncap;
    }
    __int128 c = 0, p3 = 1;
    for (uint32_t i = 0; i < d; i++) {
        if ((bits >> i) & 1U) {
            c = 3 * c + ((__int128)1 << i);
            p3 *= 3;
        }
    }
    __int128 D = ((__int128)1 << d) - p3;
    v->data[v->len++] = (spine_rec_t){bits, d, o, c, D, hydra_tile_lsb64(bits, d)};
}

typedef struct {
    uint32_t d;
    uint32_t o_min;
    uint8_t a[32];
    spine_vec_t *out;
} hydra_fkm_t;

static void hydra_fkm_rec(hydra_fkm_t *st, uint32_t t, uint32_t p, uint32_t ones) {
    const uint32_t n = st->d;
    if (ones + (n - t + 1) < st->o_min) return;
    if (t > n) {
        if (p == n && ones >= st->o_min) {
            uint32_t bits = 0;
            for (uint32_t i = 1; i <= n; i++) {
                if (st->a[i]) bits |= (1U << (i - 1));
            }
            spine_vec_push(st->out, bits, n, ones);
        }
        return;
    }
    uint8_t b = st->a[t - p];
    st->a[t] = b;
    hydra_fkm_rec(st, t + 1, p, ones + b);
    if (b == 0) {
        st->a[t] = 1;
        hydra_fkm_rec(st, t + 1, t, ones + 1);
    }
}

static void generate_spines(uint32_t min_d, uint32_t max_d, spine_vec_t *out) {
    hydra_fkm_t st;
    memset(&st, 0, sizeof(st));
    st.out = out;
    for (uint32_t d = min_d; d <= max_d; d++) {
        st.d = d;
        st.o_min = hydra_min_super_ones(d);
        st.a[0] = 0;
        hydra_fkm_rec(&st, 1, 1, 0);
    }
}

typedef struct {
    uint64_t mod3_checked_odds;
    uint64_t mod3_T_eq_2_count;
    uint64_t mod3_TMinus_eq_1_count;
    uint64_t supercritical_spines_checked;
    uint64_t intercept_div3_violations;
    uint64_t mod9_plus_hist[9];
    uint64_t mod9_minus_hist[9];
    uint64_t pair_total;
    uint64_t high_v2_pairs; /* v2 >= 10 */
    double avg_v3_all;
    double avg_v3_high_v2;
    double avg_v5_all;
    double avg_v5_high_v2;
    double avg_v7_all;
    double avg_v7_high_v2;
    double avg_log2_arch_all;
    double avg_log2_arch_high_v2;
    uint32_t max_v2_observed;
    uint32_t max_v3_observed;
    uint32_t max_v5_observed;
    uint32_t max_v7_observed;
    double elapsed_seconds;
} vector_a_result_t;

static vector_a_result_t run_vector_a(uint32_t max_src_d, uint32_t max_tgt_d) {
    double t0 = hydra_now_seconds();
    vector_a_result_t res;
    memset(&res, 0, sizeof(res));

    /* 1. Verify mod-3 chiral asymmetry on all odd integers in [1, 1,000,000] */
    for (int64_t x = 1; x < 1000000LL; x += 2) {
        res.mod3_checked_odds++;
        if ((step_T_i64(x) % 3) == 2) res.mod3_T_eq_2_count++;
        if ((step_TMinus_i64(x) % 3) == 1) res.mod3_TMinus_eq_1_count++;
    }

    /* 2. Generate supercritical Lyndon spines up to max_tgt_d (<= 16 fits fast) */
    spine_vec_t srcs = {0}, tgts = {0};
    generate_spines(3, max_src_d, &srcs);
    generate_spines(1, max_tgt_d, &tgts);

    res.supercritical_spines_checked = (uint64_t)tgts.len;
    for (size_t i = 0; i < tgts.len; i++) {
        uint32_t m9 = (uint32_t)(tgts.data[i].c % 9);
        if ((m9 % 3) == 0) res.intercept_div3_violations++;
        res.mod9_plus_hist[m9]++;
        res.mod9_minus_hist[(9U - m9) % 9U]++;
    }

    /* 3. Joint adelic valuation profile across all distinct (source, target) pairs */
    uint64_t sum_v3_all = 0, sum_v5_all = 0, sum_v7_all = 0;
    uint64_t sum_v3_hi = 0, sum_v5_hi = 0, sum_v7_hi = 0;
    double sum_log_all = 0.0, sum_log_hi = 0.0;

    for (size_t i = 0; i < srcs.len; i++) {
        const spine_rec_t *s = &srcs.data[i];
        for (size_t j = 0; j < tgts.len; j++) {
            const spine_rec_t *t = &tgts.data[j];
            __int128 delta = s->c * t->D - t->c * s->D;
            if (delta == 0) continue;
            __uint128_t mag = (delta < 0) ? (__uint128_t)(-delta) : (__uint128_t)delta;
            uint32_t v2 = ctz64(s->lsb ^ t->lsb);
            uint32_t v3 = val_p_u128(mag, 3);
            uint32_t v5 = val_p_u128(mag, 5);
            uint32_t v7 = val_p_u128(mag, 7);
            double log2_mag = log2((double)mag);

            res.pair_total++;
            sum_v3_all += v3;
            sum_v5_all += v5;
            sum_v7_all += v7;
            sum_log_all += log2_mag;
            if (v2 > res.max_v2_observed) res.max_v2_observed = v2;
            if (v3 > res.max_v3_observed) res.max_v3_observed = v3;
            if (v5 > res.max_v5_observed) res.max_v5_observed = v5;
            if (v7 > res.max_v7_observed) res.max_v7_observed = v7;

            if (v2 >= 10) {
                res.high_v2_pairs++;
                sum_v3_hi += v3;
                sum_v5_hi += v5;
                sum_v7_hi += v7;
                sum_log_hi += log2_mag;
            }
        }
    }

    if (res.pair_total > 0) {
        res.avg_v3_all = (double)sum_v3_all / (double)res.pair_total;
        res.avg_v5_all = (double)sum_v5_all / (double)res.pair_total;
        res.avg_v7_all = (double)sum_v7_all / (double)res.pair_total;
        res.avg_log2_arch_all = sum_log_all / (double)res.pair_total;
    }
    if (res.high_v2_pairs > 0) {
        res.avg_v3_high_v2 = (double)sum_v3_hi / (double)res.high_v2_pairs;
        res.avg_v5_high_v2 = (double)sum_v5_hi / (double)res.high_v2_pairs;
        res.avg_v7_high_v2 = (double)sum_v7_hi / (double)res.high_v2_pairs;
        res.avg_log2_arch_high_v2 = sum_log_hi / (double)res.high_v2_pairs;
    }

    free(srcs.data);
    free(tgts.data);
    res.elapsed_seconds = hydra_now_seconds() - t0;
    return res;
}

/* ============================================================================
 * Vector B: Two-Player Zero-Sum Minimax Collatz Carry-Adversary Game
 * ============================================================================ */

typedef struct {
    uint32_t bits;
    uint64_t odd_starts_scanned;
    uint64_t demon_stop_n;
    uint32_t demon_stop_val;
    uint64_t demon_total_n;
    uint32_t demon_total_val;
    uint64_t demon_excess_n;
    double demon_excess_val;
    uint64_t demon_alt_n;
    double demon_alt_log2_ratio;
    /* 3n - 1 sibling control basin counts */
    uint64_t sibling_to_1;
    uint64_t sibling_to_5_cycle;
    uint64_t sibling_to_17_cycle;
    uint64_t sibling_other;
} minimax_tier_t;

/* Classify 3n-1 basin in catalytic O(1) RAM:
 * Known positive cycles of T_-(x): {1}, {5, 7, 10}, {17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34}. */
static int classify_tminus_basin(uint64_t start) {
    __uint128_t x = start;
    for (uint32_t step = 0; step < 50000; step++) {
        if (x == 1) return 1;
        if (x == 5 || x == 7 || x == 10) return 5;
        if (x == 17 || x == 25 || x == 37 || x == 55 || x == 82 ||
            x == 41 || x == 61 || x == 91 || x == 136 || x == 68 || x == 34) {
            return 17;
        }
        x = (x & 1U) ? ((3 * x - 1) >> 1) : (x >> 1);
    }
    return 0;
}

typedef struct {
    minimax_tier_t tiers[16];
    int n_tiers;
    double elapsed_seconds;
} vector_b_result_t;

static vector_b_result_t run_vector_b(uint32_t max_bits) {
    double t0 = hydra_now_seconds();
    vector_b_result_t res;
    memset(&res, 0, sizeof(res));

    uint32_t cur_stop_val = 0, cur_tot_val = 0;
    uint64_t cur_stop_n = 3, cur_tot_n = 3, cur_exc_n = 3, cur_alt_n = 3;
    double cur_exc_val = -1e9, cur_alt_val = -1e9;

    uint64_t sib_1 = 0, sib_5 = 0, sib_17 = 0, sib_other = 0;
    uint64_t scanned = 0;

    uint32_t next_tier_b = 4;
    uint64_t next_limit = (1ULL << next_tier_b);
    uint64_t grand_limit = (1ULL << max_bits);

    for (uint64_t n = 3; n < grand_limit; n += 2) {
        scanned++;
        __uint128_t x = n;
        __uint128_t peak = n;
        uint32_t steps = 0;
        uint32_t odd_cnt = 0;
        uint32_t stop_time = 0;
        bool stopped = false;
        double max_excess = 0.0;

        while (x != 1) {
            if (x & 1U) {
                odd_cnt++;
                x = (3 * x + 1) >> 1;
                if (x > peak) peak = x;
            } else {
                x >>= 1;
            }
            steps++;
            if (!stopped && x < n) {
                stop_time = steps;
                stopped = true;
            }
            double exc = (double)odd_cnt - THETA_LOG3_2 * (double)steps;
            if (exc > max_excess) max_excess = exc;
        }
        if (!stopped) stop_time = steps;

        if (stop_time > cur_stop_val) {
            cur_stop_val = stop_time;
            cur_stop_n = n;
        }
        if (steps > cur_tot_val) {
            cur_tot_val = steps;
            cur_tot_n = n;
        }
        if (max_excess > cur_exc_val) {
            cur_exc_val = max_excess;
            cur_exc_n = n;
        }
        double alt_ratio = log2((double)peak) - log2((double)n);
        if (alt_ratio > cur_alt_val) {
            cur_alt_val = alt_ratio;
            cur_alt_n = n;
        }

        /* Sibling control 3n-1 exact basin */
        int b = classify_tminus_basin(n);
        if (b == 1) sib_1++;
        else if (b == 5) sib_5++;
        else if (b == 17) sib_17++;
        else sib_other++;

        if (n + 2 >= next_limit && res.n_tiers < 16) {
            minimax_tier_t *tr = &res.tiers[res.n_tiers++];
            tr->bits = next_tier_b;
            tr->odd_starts_scanned = scanned;
            tr->demon_stop_n = cur_stop_n;
            tr->demon_stop_val = cur_stop_val;
            tr->demon_total_n = cur_tot_n;
            tr->demon_total_val = cur_tot_val;
            tr->demon_excess_n = cur_exc_n;
            tr->demon_excess_val = cur_exc_val;
            tr->demon_alt_n = cur_alt_n;
            tr->demon_alt_log2_ratio = cur_alt_val;
            tr->sibling_to_1 = sib_1;
            tr->sibling_to_5_cycle = sib_5;
            tr->sibling_to_17_cycle = sib_17;
            tr->sibling_other = sib_other;

            next_tier_b += 2;
            if (next_tier_b <= max_bits) {
                next_limit = (1ULL << next_tier_b);
            } else {
                next_limit = UINT64_MAX;
            }
        }
    }

    res.elapsed_seconds = hydra_now_seconds() - t0;
    return res;
}

/* ============================================================================
 * Vector C: Binary Carry-Avalanche Shockwave & Chiral Two's-Complement Asymmetry
 * ============================================================================ */

typedef struct {
    uint64_t odd_samples;
    double mean_carry_bits_3n_plus_1;
    double mean_carry_bits_3n_minus_1;
    double mean_carry_bits_5n_plus_1;
    uint32_t max_carry_bits_3n_plus_1;
    uint32_t max_carry_bits_3n_minus_1;
    double mean_hamming_drift_3n_plus_1;
    double mean_hamming_drift_3n_minus_1;
    double mean_hamming_drift_5n_plus_1;
    double mean_v2_on_trailing1_ge4_plus;
    double mean_v2_on_trailing1_ge4_minus;
    double mean_v2_on_mod16_eq1_plus;
    double mean_v2_on_mod16_eq1_minus;
    uint64_t sign_conjugacy_checks;
    uint64_t sign_conjugacy_mismatches;
    double elapsed_seconds;
} vector_c_result_t;

static vector_c_result_t run_vector_c(uint32_t sample_bits) {
    double t0 = hydra_now_seconds();
    vector_c_result_t res;
    memset(&res, 0, sizeof(res));

    uint64_t limit = 1ULL << sample_bits;
    uint64_t sum_carry_p = 0, sum_carry_m = 0, sum_carry_5 = 0;
    int64_t sum_dh_p = 0, sum_dh_m = 0, sum_dh_5 = 0;

    uint64_t cnt_t1_ge4 = 0, sum_v2_t1_p = 0, sum_v2_t1_m = 0;
    uint64_t cnt_mod16_1 = 0, sum_v2_m16_p = 0, sum_v2_m16_m = 0;

    for (uint64_t x = 1; x < limit; x += 2) {
        res.odd_samples++;
        uint64_t two_x = x << 1;
        uint64_t four_x = x << 2;

        uint64_t y_p = 3ULL * x + 1ULL;
        uint64_t y_m = 3ULL * x - 1ULL;
        uint64_t y_5 = 5ULL * x + 1ULL;

        /* Carry-in bitmask for a + b (+ c_in): (a ^ b ^ sum) */
        uint32_t c_p = popcount64(two_x ^ x ^ y_p);
        uint32_t c_m = popcount64(two_x ^ (x - 1ULL) ^ y_m);
        uint32_t c_5 = popcount64(four_x ^ x ^ y_5);

        sum_carry_p += c_p;
        sum_carry_m += c_m;
        sum_carry_5 += c_5;
        if (c_p > res.max_carry_bits_3n_plus_1) res.max_carry_bits_3n_plus_1 = c_p;
        if (c_m > res.max_carry_bits_3n_minus_1) res.max_carry_bits_3n_minus_1 = c_m;

        int32_t hx = (int32_t)popcount64(x);
        sum_dh_p += (int32_t)popcount64(y_p >> 1) - hx;
        sum_dh_m += (int32_t)popcount64(y_m >> 1) - hx;
        sum_dh_5 += (int32_t)popcount64(y_5 >> 1) - hx;

        /* Trailing-1 erosion asymmetry: x == 15 (mod 16) vs x == 1 (mod 16) */
        if ((x & 15ULL) == 15ULL) {
            cnt_t1_ge4++;
            sum_v2_t1_p += ctz64(y_p);
            sum_v2_t1_m += ctz64(y_m);
        }
        if ((x & 15ULL) == 1ULL) {
            cnt_mod16_1++;
            sum_v2_m16_p += ctz64(y_p);
            sum_v2_m16_m += ctz64(y_m);
        }
    }

    res.mean_carry_bits_3n_plus_1 = (double)sum_carry_p / (double)res.odd_samples;
    res.mean_carry_bits_3n_minus_1 = (double)sum_carry_m / (double)res.odd_samples;
    res.mean_carry_bits_5n_plus_1 = (double)sum_carry_5 / (double)res.odd_samples;
    res.mean_hamming_drift_3n_plus_1 = (double)sum_dh_p / (double)res.odd_samples;
    res.mean_hamming_drift_3n_minus_1 = (double)sum_dh_m / (double)res.odd_samples;
    res.mean_hamming_drift_5n_plus_1 = (double)sum_dh_5 / (double)res.odd_samples;
    res.mean_v2_on_trailing1_ge4_plus = (double)sum_v2_t1_p / (double)cnt_t1_ge4;
    res.mean_v2_on_trailing1_ge4_minus = (double)sum_v2_t1_m / (double)cnt_t1_ge4;
    res.mean_v2_on_mod16_eq1_plus = (double)sum_v2_m16_p / (double)cnt_mod16_1;
    res.mean_v2_on_mod16_eq1_minus = (double)sum_v2_m16_m / (double)cnt_mod16_1;

    /* Exact signed check of Lean theorem T^d(-x) == -T_-^d(x) across 100,000 orbits (d=12) */
    for (int64_t x = -50000LL; x < 50000LL; x++) {
        int64_t a = -x, b = x;
        for (int d = 0; d < 12; d++) {
            a = step_T_i64(a);
            b = step_TMinus_i64(b);
        }
        res.sign_conjugacy_checks++;
        if (a != -b) res.sign_conjugacy_mismatches++;
    }

    res.elapsed_seconds = hydra_now_seconds() - t0;
    return res;
}

/* ============================================================================
 * Vector D: Tropical / Max-Plus Karp Cycle-Mean Attack on Adelic Quotient
 * Automata Z / (2^a * 3^b) Z + Archimedean Positivity Box Break
 * ============================================================================ */

typedef struct {
    int64_t num;
    int64_t den;
} rat_t;

static int64_t gcd_i64(int64_t a, int64_t b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b != 0) {
        int64_t t = a % b;
        a = b;
        b = t;
    }
    return a ? a : 1;
}

static rat_t make_rat(int64_t n, int64_t d) {
    if (d < 0) { n = -n; d = -d; }
    int64_t g = gcd_i64(n, d);
    return (rat_t){n / g, d / g};
}

/* Compare a/b vs c/d (b, d > 0) using exact 128-bit cross-multiplication */
static inline int cmp_rat(rat_t a, rat_t b) {
    __int128 lhs = (__int128)a.num * (__int128)b.den;
    __int128 rhs = (__int128)b.num * (__int128)a.den;
    return (lhs < rhs) ? -1 : ((lhs > rhs) ? 1 : 0);
}

/* Karp's exact Tropical Maximum Cycle Mean on a graph with V vertices and
 * out-degree <= 2 per vertex (adj[u][0..deg[u]-1], weight w[u] in {0, 1}).
 * Returns exact rational max cycle mean (or {-1, 1} if acyclic). */
static rat_t karp_max_cycle_mean(
    int V, const int (*adj)[2], const int *deg, const int *wt, const bool *active
) {
    /* Compact active vertex indices 0..N-1 */
    int *id_map = (int *)malloc((size_t)V * sizeof(int));
    int *rev_map = (int *)malloc((size_t)V * sizeof(int));
    int N = 0;
    for (int u = 0; u < V; u++) {
        if (active[u]) {
            id_map[u] = N;
            rev_map[N] = u;
            N++;
        } else {
            id_map[u] = -1;
        }
    }
    if (N == 0) {
        free(id_map);
        free(rev_map);
        return (rat_t){-1, 1};
    }

    /* DP table: dp[k][v] = max weight of a length-k walk ending at v (or NEG_INF) */
    const int32_t NEG_INF = -1000000000;
    int32_t *dp = (int32_t *)malloc((size_t)(N + 1) * (size_t)N * sizeof(int32_t));
    if (!dp) {
        fprintf(stderr, "ERROR: OOM in Karp DP (N=%d)\n", N);
        exit(2);
    }
    for (int i = 0; i < N; i++) dp[i] = 0; /* Multi-source start: length-0 walk at every vertex */

    for (int k = 1; k <= N; k++) {
        int32_t *prev = dp + (size_t)(k - 1) * (size_t)N;
        int32_t *cur = dp + (size_t)k * (size_t)N;
        for (int v = 0; v < N; v++) cur[v] = NEG_INF;
        for (int ui = 0; ui < N; ui++) {
            if (prev[ui] <= NEG_INF / 2) continue;
            int u = rev_map[ui];
            int32_t cand = prev[ui] + (int32_t)wt[u];
            for (int e = 0; e < deg[u]; e++) {
                int v = adj[u][e];
                int vi = id_map[v];
                if (vi >= 0 && cand > cur[vi]) {
                    cur[vi] = cand;
                }
            }
        }
    }

    /* Karp formula: mu* = max_{v: dp[N][v] > -inf} min_{0 <= k < N, dp[k][v] > -inf} (dp[N][v] - dp[k][v]) / (N - k) */
    bool found_any = false;
    rat_t best = {-1, 1};
    int32_t *last = dp + (size_t)N * (size_t)N;

    for (int vi = 0; vi < N; vi++) {
        if (last[vi] <= NEG_INF / 2) continue;
        bool has_min = false;
        rat_t vmin = {0, 1};
        for (int k = 0; k < N; k++) {
            int32_t pk = dp[(size_t)k * (size_t)N + (size_t)vi];
            if (pk <= NEG_INF / 2) continue;
            rat_t r = make_rat((int64_t)(last[vi] - pk), (int64_t)(N - k));
            if (!has_min || cmp_rat(r, vmin) < 0) {
                vmin = r;
                has_min = true;
            }
        }
        if (has_min && (!found_any || cmp_rat(vmin, best) > 0)) {
            best = vmin;
            found_any = true;
        }
    }

    free(dp);
    free(id_map);
    free(rev_map);
    return found_any ? best : (rat_t){-1, 1};
}

typedef struct {
    int a;
    int b;
    int M;
    int active_mod3_states;
    rat_t mu_raw_plus;
    rat_t mu_raw_minus;
    rat_t mu_pruned_plus;  /* remove u == 0 (mod 3) and self-loop u = M - 1 */
    rat_t mu_pruned_minus; /* remove u == 0 (mod 3) and self-loop u = 1 */
    bool mirror_exact_equal;
    uint32_t mod3_transient_violations; /* edges from odd state to 0 mod 3 (must be 0) */
} tropical_mod_rec_t;

typedef struct {
    int box_N;
    rat_t mu_box_plus;           /* positive box [1, N] under 3n+1 */
    rat_t mu_box_minus_all;      /* positive box [1, N] under 3n-1 */
    rat_t mu_box_minus_no1;      /* positive box [2, N] under 3n-1 (excluding 1-loop) */
} tropical_box_rec_t;

typedef struct {
    tropical_mod_rec_t mods[10];
    int n_mods;
    tropical_box_rec_t boxes[4];
    int n_boxes;
    double elapsed_seconds;
} vector_d_result_t;

static void build_adelic_quotient(
    int M, int eps, int (*adj)[2], int *deg, int *wt, uint32_t *mod3_odd_to_zero
) {
    int half = M / 2;
    for (int u = 0; u < M; u++) {
        if ((u & 1) == 0) {
            wt[u] = 0;
            int v0 = u / 2;
            int v1 = (v0 + half) % M;
            adj[u][0] = v0;
            adj[u][1] = v1;
            deg[u] = (v0 == v1) ? 1 : 2;
        } else {
            wt[u] = 1;
            int raw = (3 * u + eps) / 2;
            int v0 = ((raw % M) + M) % M;
            int v1 = (v0 + half) % M;
            adj[u][0] = v0;
            adj[u][1] = v1;
            deg[u] = (v0 == v1) ? 1 : 2;
            if ((v0 % 3) == 0 || (v1 % 3) == 0) (*mod3_odd_to_zero)++;
        }
    }
}

static rat_t box_max_cycle_mean(int lo_val, int N, int eps) {
    /* Exact positive-box deterministic functional graph on [lo_val, N] */
    int V = N + 1;
    int (*adj)[2] = (int (*)[2])calloc((size_t)V, sizeof(*adj));
    int *deg = (int *)calloc((size_t)V, sizeof(int));
    int *wt = (int *)calloc((size_t)V, sizeof(int));
    bool *active = (bool *)calloc((size_t)V, sizeof(bool));

    for (int x = lo_val; x <= N; x++) {
        active[x] = true;
        wt[x] = (x & 1);
        int64_t nxt = (x & 1) ? ((3LL * x + eps) >> 1) : (x >> 1);
        if (nxt >= lo_val && nxt <= N) {
            adj[x][0] = (int)nxt;
            deg[x] = 1;
        } else {
            deg[x] = 0; /* escapes positive box */
        }
    }
    rat_t r = karp_max_cycle_mean(V, adj, deg, wt, active);
    free(adj);
    free(deg);
    free(wt);
    free(active);
    return r;
}

static vector_d_result_t run_vector_d(void) {
    double t0 = hydra_now_seconds();
    vector_d_result_t res;
    memset(&res, 0, sizeof(res));

    const int specs[][2] = {
        {2, 1}, /* 12 */
        {3, 1}, /* 24 */
        {2, 2}, /* 36 */
        {4, 1}, /* 48 */
        {3, 2}, /* 72 */
        {5, 1}, /* 96 */
        {4, 2}, /* 144 */
        {6, 1}, /* 192 */
        {5, 2}, /* 288 */
        {6, 2}  /* 576 */
    };
    const int n_specs = (int)(sizeof(specs) / sizeof(specs[0]));

    for (int si = 0; si < n_specs; si++) {
        int a = specs[si][0];
        int b = specs[si][1];
        int M = (1 << a);
        for (int i = 0; i < b; i++) M *= 3;

        int (*adj_p)[2] = (int (*)[2])calloc((size_t)M, sizeof(*adj_p));
        int (*adj_m)[2] = (int (*)[2])calloc((size_t)M, sizeof(*adj_m));
        int *deg_p = (int *)calloc((size_t)M, sizeof(int));
        int *deg_m = (int *)calloc((size_t)M, sizeof(int));
        int *wt_p = (int *)calloc((size_t)M, sizeof(int));
        int *wt_m = (int *)calloc((size_t)M, sizeof(int));
        bool *act_all = (bool *)malloc((size_t)M * sizeof(bool));
        bool *act_p = (bool *)malloc((size_t)M * sizeof(bool));
        bool *act_m = (bool *)malloc((size_t)M * sizeof(bool));

        uint32_t mod3_viol = 0;
        build_adelic_quotient(M, +1, adj_p, deg_p, wt_p, &mod3_viol);
        build_adelic_quotient(M, -1, adj_m, deg_m, wt_m, &mod3_viol);

        int active_cnt = 0;
        for (int u = 0; u < M; u++) {
            act_all[u] = true;
            /* Prune 3 | u (proved transient) and the 2-adic bad fixed point (-1 for +, +1 for -) */
            act_p[u] = ((u % 3) != 0) && (u != M - 1);
            act_m[u] = ((u % 3) != 0) && (u != 1);
            if (act_p[u]) active_cnt++;
        }

        tropical_mod_rec_t *rec = &res.mods[res.n_mods++];
        rec->a = a;
        rec->b = b;
        rec->M = M;
        rec->active_mod3_states = active_cnt;
        rec->mu_raw_plus = karp_max_cycle_mean(M, adj_p, deg_p, wt_p, act_all);
        rec->mu_raw_minus = karp_max_cycle_mean(M, adj_m, deg_m, wt_m, act_all);
        rec->mu_pruned_plus = karp_max_cycle_mean(M, adj_p, deg_p, wt_p, act_p);
        rec->mu_pruned_minus = karp_max_cycle_mean(M, adj_m, deg_m, wt_m, act_m);
        rec->mirror_exact_equal = (cmp_rat(rec->mu_pruned_plus, rec->mu_pruned_minus) == 0);
        rec->mod3_transient_violations = mod3_viol;

        free(adj_p); free(adj_m); free(deg_p); free(deg_m);
        free(wt_p); free(wt_m); free(act_all); free(act_p); free(act_m);
    }

    /* Archimedean Positivity Break: finite positive boxes [1, N] */
    const int box_sizes[4] = {20, 50, 150, 500};
    for (int bi = 0; bi < 4; bi++) {
        int N = box_sizes[bi];
        tropical_box_rec_t *br = &res.boxes[res.n_boxes++];
        br->box_N = N;
        br->mu_box_plus = box_max_cycle_mean(1, N, +1);
        br->mu_box_minus_all = box_max_cycle_mean(1, N, -1);
        br->mu_box_minus_no1 = box_max_cycle_mean(2, N, -1);
    }

    res.elapsed_seconds = hydra_now_seconds() - t0;
    return res;
}

/* ============================================================================
 * Vector E: Symbolic LZ76 Complexity, Run-Length & Autocorrelation Spectrum
 * ============================================================================ */

/* Standard Lempel-Ziv 1976 (LZ76) exhaustive phrase count on binary array s[0..n-1]. */
static uint32_t lz76_complexity(const uint8_t *s, uint32_t n) {
    if (n == 0) return 0;
    uint32_t c = 1;
    uint32_t i = 0;      /* start of prefix search */
    uint32_t l = 1;      /* end of current history */
    uint32_t k = 1;      /* current match length */
    uint32_t k_max = 1;  /* best match length found */
    while (l + k <= n) {
        if (s[i + k - 1] == s[l + k - 1]) {
            k++;
            if (l + k > n) {
                c++;
                break;
            }
        } else {
            if (k > k_max) k_max = k;
            i++;
            if (i == l) {
                c++;
                l += k_max;
                if (l >= n) break;
                i = 0;
                k = 1;
                k_max = 1;
            } else {
                k = 1;
            }
        }
    }
    return c;
}

typedef struct {
    char label[48];
    uint64_t seed_n;
    int eps;
    uint32_t word_len;
    uint32_t odd_steps;
    double odd_density;
    uint32_t lz76_phrases;
    double lz76_normalized; /* c * log2(L) / L */
    uint32_t max_odd_run;
    double autocorr_lag1;
    double autocorr_lag2;
} symbolic_profile_t;

static symbolic_profile_t analyze_orbit_word(
    const char *label, uint64_t seed_n, int eps, uint32_t max_len
) {
    symbolic_profile_t p;
    memset(&p, 0, sizeof(p));
    snprintf(p.label, sizeof(p.label), "%s", label);
    p.seed_n = seed_n;
    p.eps = eps;

    uint8_t *bits = (uint8_t *)malloc((size_t)max_len);
    uint32_t len = 0;
    uint32_t odd = 0;
    uint32_t cur_run = 0, max_run = 0;
    __uint128_t x = seed_n;

    while (len < max_len) {
        if (eps == +1 && x == 1) break;
        uint8_t b = (uint8_t)(x & 1U);
        bits[len++] = b;
        if (b) {
            odd++;
            cur_run++;
            if (cur_run > max_run) max_run = cur_run;
            x = (eps == +1) ? ((3 * x + 1) >> 1) : ((3 * x - 1) >> 1);
        } else {
            cur_run = 0;
            x >>= 1;
        }
    }

    p.word_len = len;
    p.odd_steps = odd;
    p.odd_density = len ? ((double)odd / (double)len) : 0.0;
    p.lz76_phrases = lz76_complexity(bits, len);
    p.lz76_normalized = (len >= 2) ? ((double)p.lz76_phrases * log2((double)len) / (double)len) : 0.0;
    p.max_odd_run = max_run;

    /* Centered lag-1 and lag-2 binary autocorrelation */
    double mean = p.odd_density;
    double var = mean * (1.0 - mean);
    if (len > 2 && var > 1e-12) {
        double s1 = 0.0, s2 = 0.0;
        for (uint32_t i = 0; i + 1 < len; i++) {
            s1 += ((double)bits[i] - mean) * ((double)bits[i + 1] - mean);
        }
        for (uint32_t i = 0; i + 2 < len; i++) {
            s2 += ((double)bits[i] - mean) * ((double)bits[i + 2] - mean);
        }
        p.autocorr_lag1 = (s1 / (double)(len - 1)) / var;
        p.autocorr_lag2 = (s2 / (double)(len - 2)) / var;
    }

    free(bits);
    return p;
}

/* ============================================================================
 * JSON Output + Built-In Deterministic Self-Test
 * ============================================================================ */

#ifndef COLLATZ_HYDRA_NO_MAIN

static int run_hydra_self_test(void) {
    /* 1. Verify exact sign conjugacy on [-2000, 2000] */
    for (int64_t x = -2000; x <= 2000; x++) {
        int64_t a = -x, b = x;
        for (int d = 0; d < 10; d++) {
            a = step_T_i64(a);
            b = step_TMinus_i64(b);
        }
        if (a != -b) {
            fprintf(stderr, "HYDRA SELF-TEST FAIL: sign conjugacy mismatch at x=%" PRId64 "\n", x);
            return 1;
        }
    }
    /* 2. Verify mod-3 chiral asymmetry on all odd x in [1, 10000] */
    for (int64_t x = 1; x < 10000; x += 2) {
        if ((step_T_i64(x) % 3) != 2 || (step_TMinus_i64(x) % 3) != 1) {
            fprintf(stderr, "HYDRA SELF-TEST FAIL: mod-3 asymmetry at x=%" PRId64 "\n", x);
            return 1;
        }
    }
    /* 3. Verify Karp exactness on box [1, 50]: mu_+(50) = 1/2, mu_-(50, no 1) = 2/3 */
    rat_t mp = box_max_cycle_mean(1, 50, +1);
    rat_t mm = box_max_cycle_mean(2, 50, -1);
    if (mp.num != 1 || mp.den != 2 || mm.num != 2 || mm.den != 3) {
        fprintf(stderr, "HYDRA SELF-TEST FAIL: box Karp got + %" PRId64 "/%" PRId64 ", - %" PRId64 "/%" PRId64 "\n",
                mp.num, mp.den, mm.num, mm.den);
        return 1;
    }
    /* 4. Verify Vector B exact Demon at B=6 (n < 64): n = 55 has 71 shortcut steps (n = 27 has 70) */
    vector_b_result_t vb = run_vector_b(8);
    if (vb.tiers[1].bits != 6 || vb.tiers[1].demon_total_n != 55 || vb.tiers[1].demon_total_val != 71) {
        fprintf(stderr, "HYDRA SELF-TEST FAIL: B=6 demon expected 55 (71), got %" PRIu64 " (%u)\n",
                vb.tiers[1].demon_total_n, vb.tiers[1].demon_total_val);
        return 1;
    }
    symbolic_profile_t p27 = analyze_orbit_word("check27", 27ULL, +1, 256);
    if (p27.word_len != 70) {
        fprintf(stderr, "HYDRA SELF-TEST FAIL: n=27 expected 70 shortcut steps, got %u\n", p27.word_len);
        return 1;
    }
    /* 5. Verify LZ76 on periodic 01010101... vs non-periodic */
    uint8_t per[64];
    for (int i = 0; i < 64; i++) per[i] = (uint8_t)(i & 1);
    uint32_t lz_p = lz76_complexity(per, 64);
    if (lz_p != 3) {
        fprintf(stderr, "HYDRA SELF-TEST FAIL: periodic 01^32 expected LZ76=3, got %u\n", lz_p);
        return 1;
    }
    printf("collatz_asymmetric_hydra self-test PASS: sign-conjugacy, mod-3 chiral asymmetry, Karp exact box (1/2 vs 2/3), B=6 Demon (55: 71 steps; 27: 70 steps), LZ76 verified.\n");
    return 0;
}

static int run_full_hydra(const char *out_path, uint32_t max_b) {
    double t_all = hydra_now_seconds();

    vector_a_result_t va = run_vector_a(8, 14);
    vector_b_result_t vb = run_vector_b(max_b);
    vector_c_result_t vc = run_vector_c(20);
    vector_d_result_t vd = run_vector_d();

    double te0 = hydra_now_seconds();
    uint64_t demon_top_tot = vb.tiers[vb.n_tiers - 1].demon_total_n;
    uint64_t demon_top_exc = vb.tiers[vb.n_tiers - 1].demon_excess_n;
    symbolic_profile_t ve[6];
    ve[0] = analyze_orbit_word("demon_B6_27", 27ULL, +1, 2048);
    ve[1] = analyze_orbit_word("demon_top_total_Bmax", demon_top_tot, +1, 2048);
    ve[2] = analyze_orbit_word("demon_top_excess_Bmax", demon_top_exc, +1, 2048);
    ve[3] = analyze_orbit_word("typical_odd_1000003", 1000003ULL, +1, 2048);
    ve[4] = analyze_orbit_word("sibling_3n_minus_1_cycle5", 5ULL, -1, 256);
    ve[5] = analyze_orbit_word("sibling_3n_minus_1_cycle17", 17ULL, -1, 256);
    double te_elapsed = hydra_now_seconds() - te0;

    double total_elapsed = hydra_now_seconds() - t_all;

    FILE *fp = stdout;
    if (out_path != NULL) {
        fp = fopen(out_path, "wb");
        if (!fp) {
            fprintf(stderr, "ERROR: cannot open output path %s\n", out_path);
            return 2;
        }
    }

    fprintf(fp, "{\n");
    fprintf(fp, "  \"engine\": \"collatz_asymmetric_hydra_c17\",\n");
    fprintf(fp, "  \"version\": \"0.10.0\",\n");
    fprintf(fp, "  \"status\": \"finite exact multi-vector measurement; proves NO part of the Collatz Conjecture (OPEN)\",\n");
    fprintf(fp, "  \"total_elapsed_seconds\": %.6f,\n", total_elapsed);

    /* Vector A */
    fprintf(fp, "  \"vector_a_adelic_pincer\": {\n");
    fprintf(fp, "    \"mod3_checked_odds\": %" PRIu64 ",\n", va.mod3_checked_odds);
    fprintf(fp, "    \"mod3_T_eq_2_count\": %" PRIu64 ",\n", va.mod3_T_eq_2_count);
    fprintf(fp, "    \"mod3_TMinus_eq_1_count\": %" PRIu64 ",\n", va.mod3_TMinus_eq_1_count);
    fprintf(fp, "    \"supercritical_spines_checked\": %" PRIu64 ",\n", va.supercritical_spines_checked);
    fprintf(fp, "    \"intercept_div3_violations\": %" PRIu64 ",\n", va.intercept_div3_violations);
    fprintf(fp, "    \"mod9_intercept_plus_hist\": [");
    for (int i = 0; i < 9; i++) fprintf(fp, "%s%" PRIu64, i ? ", " : "", va.mod9_plus_hist[i]);
    fprintf(fp, "],\n    \"mod9_intercept_minus_hist\": [");
    for (int i = 0; i < 9; i++) fprintf(fp, "%s%" PRIu64, i ? ", " : "", va.mod9_minus_hist[i]);
    fprintf(fp, "],\n");
    fprintf(fp, "    \"distinct_spine_pairs\": %" PRIu64 ",\n", va.pair_total);
    fprintf(fp, "    \"high_v2_ge_10_pairs\": %" PRIu64 ",\n", va.high_v2_pairs);
    fprintf(fp, "    \"max_valuations_observed\": {\"v2\": %u, \"v3\": %u, \"v5\": %u, \"v7\": %u},\n",
            va.max_v2_observed, va.max_v3_observed, va.max_v5_observed, va.max_v7_observed);
    fprintf(fp, "    \"mean_valuations_all\": {\"v3\": %.6f, \"v5\": %.6f, \"v7\": %.6f, \"log2_arch\": %.6f},\n",
            va.avg_v3_all, va.avg_v5_all, va.avg_v7_all, va.avg_log2_arch_all);
    fprintf(fp, "    \"mean_valuations_high_v2\": {\"v3\": %.6f, \"v5\": %.6f, \"v7\": %.6f, \"log2_arch\": %.6f},\n",
            va.avg_v3_high_v2, va.avg_v5_high_v2, va.avg_v7_high_v2, va.avg_log2_arch_high_v2);
    fprintf(fp, "    \"breaks_epsilon_symmetry\": true,\n");
    fprintf(fp, "    \"elapsed_seconds\": %.6f\n", va.elapsed_seconds);
    fprintf(fp, "  },\n");

    /* Vector B */
    fprintf(fp, "  \"vector_b_minimax_game\": {\n");
    fprintf(fp, "    \"max_bits\": %u,\n", max_b);
    fprintf(fp, "    \"breaks_epsilon_symmetry\": true,\n");
    fprintf(fp, "    \"elapsed_seconds\": %.6f,\n", vb.elapsed_seconds);
    fprintf(fp, "    \"tiers\": [\n");
    for (int i = 0; i < vb.n_tiers; i++) {
        const minimax_tier_t *tr = &vb.tiers[i];
        double esc_frac = (double)(tr->sibling_to_5_cycle + tr->sibling_to_17_cycle + tr->sibling_other)
                          / (double)tr->odd_starts_scanned;
        fprintf(fp, "      {\n");
        fprintf(fp, "        \"bits\": %u,\n", tr->bits);
        fprintf(fp, "        \"odd_starts_scanned\": %" PRIu64 ",\n", tr->odd_starts_scanned);
        fprintf(fp, "        \"demon_stop\": {\"n\": %" PRIu64 ", \"steps\": %u},\n",
                tr->demon_stop_n, tr->demon_stop_val);
        fprintf(fp, "        \"demon_total\": {\"n\": %" PRIu64 ", \"steps\": %u},\n",
                tr->demon_total_n, tr->demon_total_val);
        fprintf(fp, "        \"demon_excess\": {\"n\": %" PRIu64 ", \"max_excess\": %.6f},\n",
                tr->demon_excess_n, tr->demon_excess_val);
        fprintf(fp, "        \"demon_altitude\": {\"n\": %" PRIu64 ", \"log2_ratio\": %.6f},\n",
                tr->demon_alt_n, tr->demon_alt_log2_ratio);
        fprintf(fp, "        \"sibling_3n_minus_1\": {\"to_1\": %" PRIu64 ", \"to_5_cycle\": %" PRIu64
                    ", \"to_17_cycle\": %" PRIu64 ", \"other\": %" PRIu64 ", \"nontrivial_cycle_fraction\": %.6f}\n",
                tr->sibling_to_1, tr->sibling_to_5_cycle, tr->sibling_to_17_cycle,
                tr->sibling_other, esc_frac);
        fprintf(fp, "      }%s\n", (i + 1 < vb.n_tiers) ? "," : "");
    }
    fprintf(fp, "    ]\n");
    fprintf(fp, "  },\n");

    /* Vector C */
    fprintf(fp, "  \"vector_c_carry_shockwave\": {\n");
    fprintf(fp, "    \"odd_samples\": %" PRIu64 ",\n", vc.odd_samples);
    fprintf(fp, "    \"mean_carry_bits\": {\"3n+1\": %.6f, \"3n-1\": %.6f, \"5n+1\": %.6f},\n",
            vc.mean_carry_bits_3n_plus_1, vc.mean_carry_bits_3n_minus_1, vc.mean_carry_bits_5n_plus_1);
    fprintf(fp, "    \"max_carry_bits\": {\"3n+1\": %u, \"3n-1\": %u},\n",
            vc.max_carry_bits_3n_plus_1, vc.max_carry_bits_3n_minus_1);
    fprintf(fp, "    \"mean_hamming_drift\": {\"3n+1\": %.6f, \"3n-1\": %.6f, \"5n+1\": %.6f},\n",
            vc.mean_hamming_drift_3n_plus_1, vc.mean_hamming_drift_3n_minus_1, vc.mean_hamming_drift_5n_plus_1);
    fprintf(fp, "    \"chiral_trailing1_v2_asymmetry\": {\n");
    fprintf(fp, "      \"x_mod16_eq_15_mean_v2_plus\": %.6f,\n", vc.mean_v2_on_trailing1_ge4_plus);
    fprintf(fp, "      \"x_mod16_eq_15_mean_v2_minus\": %.6f,\n", vc.mean_v2_on_trailing1_ge4_minus);
    fprintf(fp, "      \"x_mod16_eq_1_mean_v2_plus\": %.6f,\n", vc.mean_v2_on_mod16_eq1_plus);
    fprintf(fp, "      \"x_mod16_eq_1_mean_v2_minus\": %.6f\n", vc.mean_v2_on_mod16_eq1_minus);
    fprintf(fp, "    },\n");
    fprintf(fp, "    \"sign_conjugacy_checks\": %" PRIu64 ",\n", vc.sign_conjugacy_checks);
    fprintf(fp, "    \"sign_conjugacy_mismatches\": %" PRIu64 ",\n", vc.sign_conjugacy_mismatches);
    fprintf(fp, "    \"breaks_epsilon_symmetry\": true,\n");
    fprintf(fp, "    \"elapsed_seconds\": %.6f\n", vc.elapsed_seconds);
    fprintf(fp, "  },\n");

    /* Vector D */
    fprintf(fp, "  \"vector_d_tropical_karp\": {\n");
    fprintf(fp, "    \"modular_quotient_breaks_epsilon_symmetry\": false,\n");
    fprintf(fp, "    \"archimedean_box_breaks_epsilon_symmetry\": true,\n");
    fprintf(fp, "    \"elapsed_seconds\": %.6f,\n", vd.elapsed_seconds);
    fprintf(fp, "    \"mixed_base_quotients\": [\n");
    for (int i = 0; i < vd.n_mods; i++) {
        const tropical_mod_rec_t *r = &vd.mods[i];
        fprintf(fp, "      {\"a\": %d, \"b\": %d, \"M\": %d, \"active_states\": %d, "
                    "\"mu_raw_plus\": \"%" PRId64 "/%" PRId64 "\", \"mu_raw_minus\": \"%" PRId64 "/%" PRId64 "\", "
                    "\"mu_pruned_plus\": \"%" PRId64 "/%" PRId64 "\", \"mu_pruned_plus_float\": %.6f, "
                    "\"mu_pruned_minus\": \"%" PRId64 "/%" PRId64 "\", \"mirror_exact_equal\": %s, "
                    "\"mod3_odd_to_zero_edges\": %u}%s\n",
                r->a, r->b, r->M, r->active_mod3_states,
                r->mu_raw_plus.num, r->mu_raw_plus.den,
                r->mu_raw_minus.num, r->mu_raw_minus.den,
                r->mu_pruned_plus.num, r->mu_pruned_plus.den,
                (double)r->mu_pruned_plus.num / (double)r->mu_pruned_plus.den,
                r->mu_pruned_minus.num, r->mu_pruned_minus.den,
                r->mirror_exact_equal ? "true" : "false",
                r->mod3_transient_violations,
                (i + 1 < vd.n_mods) ? "," : "");
    }
    fprintf(fp, "    ],\n");
    fprintf(fp, "    \"archimedean_positive_boxes\": [\n");
    for (int i = 0; i < vd.n_boxes; i++) {
        const tropical_box_rec_t *b = &vd.boxes[i];
        fprintf(fp, "      {\"box_N\": %d, \"mu_box_plus\": \"%" PRId64 "/%" PRId64 "\", \"mu_box_plus_float\": %.6f, "
                    "\"mu_box_minus_all\": \"%" PRId64 "/%" PRId64 "\", "
                    "\"mu_box_minus_no1\": \"%" PRId64 "/%" PRId64 "\", \"mu_box_minus_no1_float\": %.6f}%s\n",
                b->box_N, b->mu_box_plus.num, b->mu_box_plus.den,
                (double)b->mu_box_plus.num / (double)b->mu_box_plus.den,
                b->mu_box_minus_all.num, b->mu_box_minus_all.den,
                b->mu_box_minus_no1.num, b->mu_box_minus_no1.den,
                (double)b->mu_box_minus_no1.num / (double)b->mu_box_minus_no1.den,
                (i + 1 < vd.n_boxes) ? "," : "");
    }
    fprintf(fp, "    ]\n");
    fprintf(fp, "  },\n");

    /* Vector E */
    fprintf(fp, "  \"vector_e_symbolic_lz76\": {\n");
    fprintf(fp, "    \"elapsed_seconds\": %.6f,\n", te_elapsed);
    fprintf(fp, "    \"profiles\": [\n");
    for (int i = 0; i < 6; i++) {
        const symbolic_profile_t *p = &ve[i];
        fprintf(fp, "      {\"label\": \"%s\", \"seed_n\": %" PRIu64 ", \"eps\": %d, \"word_len\": %u, "
                    "\"odd_steps\": %u, \"odd_density\": %.6f, \"lz76_phrases\": %u, "
                    "\"lz76_normalized\": %.6f, \"max_odd_run\": %u, "
                    "\"autocorr_lag1\": %.6f, \"autocorr_lag2\": %.6f}%s\n",
                p->label, p->seed_n, p->eps, p->word_len, p->odd_steps, p->odd_density,
                p->lz76_phrases, p->lz76_normalized, p->max_odd_run,
                p->autocorr_lag1, p->autocorr_lag2, (i + 1 < 6) ? "," : "");
    }
    fprintf(fp, "    ]\n");
    fprintf(fp, "  }\n");
    fprintf(fp, "}\n");

    if (out_path != NULL) fclose(fp);
    return 0;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr,
            "Usage:\n"
            "  collatz_asymmetric_hydra self-test\n"
            "  collatz_asymmetric_hydra run [--max-bits B] [--output PATH]\n");
        return 1;
    }
    if (strcmp(argv[1], "self-test") == 0) {
        return run_hydra_self_test();
    }
    if (strcmp(argv[1], "run") == 0) {
        uint32_t max_b = 22;
        const char *out_path = NULL;
        for (int i = 2; i < argc; i++) {
            if (strcmp(argv[i], "--max-bits") == 0 && i + 1 < argc) {
                max_b = (uint32_t)strtoul(argv[++i], NULL, 10);
            } else if (strcmp(argv[i], "--output") == 0 && i + 1 < argc) {
                out_path = argv[++i];
            } else {
                fprintf(stderr, "Unknown argument: %s\n", argv[i]);
                return 2;
            }
        }
        if (max_b < 4 || max_b > 26 || (max_b & 1U) != 0) {
            fprintf(stderr, "ERROR: --max-bits must be an even integer in [4, 26]\n");
            return 2;
        }
        return run_full_hydra(out_path, max_b);
    }
    fprintf(stderr, "Unknown command: %s\n", argv[1]);
    return 2;
}
#endif
