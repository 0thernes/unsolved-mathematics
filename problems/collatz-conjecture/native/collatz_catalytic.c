/* SPDX-License-Identifier: MIT
 *
 * collatz_catalytic.c — Provably Exact Catalytic Native Accelerator for
 * Collatz Odd-Unit-Lock Target-Tail & Finite-Residue Descent Certificate Research.
 *
 * Mathematical Foundation (machine-checked in lean/FormalAtlas/Collatz.lean):
 *   1. Terras 2-Adic Isometry (`thm_collatz_odd_unit_lock_valuation_isometry`):
 *      For ANY two non-empty parity words w, v and ANY precision k >= 0:
 *          2^k | (c(w) D(v) - c(v) D(w))  <=>  periodicPrefix w k = periodicPrefix v k.
 *      Equivalently, v2(rho_w - rho_v) = lcp(w^inf, v^inf) EXACTLY.
 *   2. Fine-Wilf Spine Ceiling (`thm_collatz_fine_wilf_spine_ceiling`):
 *      For distinct rational spines (rho_w != rho_v):
 *          v2(rho_w - rho_v) <= |w| + |v| - gcd(|w|, |v|) - 1.
 *      Therefore, whenever |w| + |v| - gcd(|w|, |v|) <= 64 (all depths <= 32),
 *      a single 64-bit tiled word mask is 100% MATHEMATICALLY EXACT with zero
 *      truncation error, reducing arbitrary-precision rational subtraction to
 *      hardware bit-prefix slicing / tzcnt (`__builtin_ctzll`).
 *   3. Cylinder Affine Law (`thm_collatz_cylinder_affine_law`):
 *      T^d(2^d q + r) = 3^o q + T^d(r) enables O(1) incremental bit-lifting in
 *      an O(depth) catalytic fixed-stack DFS for descent-certificate mining
 *      (eliminating Python's O(frontier) BFS deque RAM explosion).
 *
 * Algorithmic & Resource Engineering:
 *   - FKM Lyndon-word generator (O(d) stack, zero wasted non-canonical words).
 *   - Catalytic in-place sort on bit-reversed 64-bit periodic keys:
 *     computes the EXACT full valuation histogram over ALL |P| x |T| pairs in
 *     O(|T| log |T| + |P| * 64 * log |T|) instead of O(|P| * |T| * bignum).
 *   - Zero heap allocation in inner loops; O(1) catalytic working memory per
 *     source phase and O(max_depth) fixed stack (< 4 KiB) for residue mining.
 *   - Deterministic output (Build Standard B03), sanitizer-clean (B16),
 *     differentially tested bit-for-bit against exact Python Fraction and
 *     safe Rust oracles (B11/B12).
 *
 * Explicit Non-Claim: Finite exact computation instrument; proves NO part of
 * the Collatz Conjecture (status: OPEN).
 */

#if !defined(_WIN32) && !defined(_POSIX_C_SOURCE)
#  define _POSIX_C_SOURCE 200809L
#endif

#include <inttypes.h>
#include <limits.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#if defined(_WIN32)
#  define WIN32_LEAN_AND_MEAN
#  include <windows.h>
static double now_seconds(void) {
    LARGE_INTEGER freq, counter;
    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&counter);
    return (double)counter.QuadPart / (double)freq.QuadPart;
}
#else
static double now_seconds(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec * 1e-9;
}
#endif

/* Portable 64-bit bit reversal (MSB <-> LSB) for prefix-ordered sorting. */
static inline uint64_t bitrev64(uint64_t x) {
    x = ((x & 0x5555555555555555ULL) << 1) | ((x >> 1) & 0x5555555555555555ULL);
    x = ((x & 0x3333333333333333ULL) << 2) | ((x >> 2) & 0x3333333333333333ULL);
    x = ((x & 0x0F0F0F0F0F0F0F0FULL) << 4) | ((x >> 4) & 0x0F0F0F0F0F0F0F0FULL);
    x = ((x & 0x00FF00FF00FF00FFULL) << 8) | ((x >> 8) & 0x00FF00FF00FF00FFULL);
    x = ((x & 0x0000FFFF0000FFFFULL) << 16) | ((x >> 16) & 0x0000FFFF0000FFFFULL);
    return (x << 32) | (x >> 32);
}

/* Pack w[0..d-1] (bit i at position i) tiled periodically across all 64 bits:
 * bit k (0 <= k < 64) of result equals w[k % d]. */
static inline uint64_t tile_lsb64(uint32_t word_bits, uint32_t d) {
    uint64_t out = 0;
    uint32_t shift = 0;
    uint64_t block = (uint64_t)word_bits;
    while (shift < 64) {
        out |= (block << shift);
        shift += d;
    }
    return out;
}

/* Compute exact MSB-first tiled periodic key directly (bit 63-k = w[k % d]). */
static inline uint64_t tile_msb64(uint32_t word_bits, uint32_t d) {
    return bitrev64(tile_lsb64(word_bits, d));
}

/* Minimum odd count o_min(d) such that 3^o > 2^d (exact integer arithmetic). */
static uint32_t min_supercritical_ones(uint32_t d) {
    __uint128_t two_d = ((__uint128_t)1) << d;
    __uint128_t p3 = 1;
    uint32_t o = 0;
    while (p3 <= two_d) {
        p3 *= 3;
        o++;
    }
    return o;
}

/* Format LSB-first bit-packed word (bit 0 = char 0) into buf[d+1]. */
static void format_word(uint32_t word_bits, uint32_t d, char *buf) {
    for (uint32_t i = 0; i < d; i++) {
        buf[i] = ((word_bits >> i) & 1U) ? '1' : '0';
    }
    buf[d] = '\0';
}

/* Exact periodic_prefix_len matching Python:
 * first index i in [0, target_len) where target[i] != phase_word[i % phase_len]. */
static inline uint32_t periodic_prefix_len_u64(
    uint64_t phase_lsb, uint64_t target_lsb, uint32_t target_len
) {
    uint64_t diff = phase_lsb ^ target_lsb;
    if (diff == 0) {
        return target_len;
    }
    uint32_t first_diff = (uint32_t)__builtin_ctzll(diff);
    return (first_diff < target_len) ? first_diff : target_len;
}

/* ============================================================================
 * FKM Binary Lyndon-Word Generator (Supercritical Pruned, O(d) Catalytic Stack)
 * ============================================================================ */

typedef void (*lyndon_cb_t)(uint32_t word_bits, uint32_t d, void *ctx);

typedef struct {
    uint32_t d;
    uint32_t o_min;
    uint8_t a[36]; /* 1-indexed FKM buffer: a[1..d], a[0] = 0 */
    lyndon_cb_t cb;
    void *ctx;
} fkm_state_t;

static void fkm_gen(fkm_state_t *st, uint32_t t, uint32_t p, uint32_t ones_so_far) {
    const uint32_t n = st->d;
    if (ones_so_far + (n - t + 1) < st->o_min) {
        return; /* Exact supercritical pruning: impossible to reach o_min ones */
    }
    if (t > n) {
        if (p == n && ones_so_far >= st->o_min) {
            uint32_t bits = 0;
            for (uint32_t i = 1; i <= n; i++) {
                if (st->a[i]) {
                    bits |= (1U << (i - 1));
                }
            }
            st->cb(bits, n, st->ctx);
        }
        return;
    }
    uint8_t bit = st->a[t - p];
    st->a[t] = bit;
    fkm_gen(st, t + 1, p, ones_so_far + bit);

    if (bit == 0) {
        st->a[t] = 1;
        fkm_gen(st, t + 1, t, ones_so_far + 1);
    }
}

static void generate_supercritical_lyndon(
    uint32_t min_d, uint32_t max_d, lyndon_cb_t cb, void *ctx
) {
    fkm_state_t st;
    memset(&st, 0, sizeof(st));
    st.cb = cb;
    st.ctx = ctx;
    for (uint32_t d = min_d; d <= max_d; d++) {
        st.d = d;
        st.o_min = min_supercritical_ones(d);
        st.a[0] = 0;
        fkm_gen(&st, 1, 1, 0);
    }
}

/* ============================================================================
 * Mode 1: Exact Odd-Unit-Lock Target-Tail Accelerator
 * ============================================================================ */

#ifndef COLLATZ_CATALYTIC_NO_MAIN

typedef struct {
    uint64_t rev_key;   /* MSB-first 64-bit tiled periodic word */
    uint32_t word_bits; /* LSB-first primitive word bits */
    uint8_t depth;
} target_rec_t;

typedef struct {
    target_rec_t *data;
    size_t len;
    size_t cap;
} target_vec_t;

static void target_vec_push(uint32_t word_bits, uint32_t d, void *ctx) {
    target_vec_t *vec = (target_vec_t *)ctx;
    if (vec->len == vec->cap) {
        size_t new_cap = vec->cap ? vec->cap * 2 : 1024;
        target_rec_t *next = (target_rec_t *)realloc(vec->data, new_cap * sizeof(target_rec_t));
        if (!next) {
            fprintf(stderr, "ERROR: out of memory allocating target vector\n");
            exit(2);
        }
        vec->data = next;
        vec->cap = new_cap;
    }
    vec->data[vec->len].rev_key = tile_msb64(word_bits, d);
    vec->data[vec->len].word_bits = word_bits;
    vec->data[vec->len].depth = (uint8_t)d;
    vec->len++;
}

typedef struct {
    uint64_t rev_key;
    uint64_t lsb_key;
    uint32_t source_bits;
    uint32_t phase_bits;
    uint8_t source_depth;
    uint8_t phase_t;
} phase_rec_t;

typedef struct {
    phase_rec_t *data;
    size_t len;
    size_t cap;
    size_t source_count;
} phase_vec_t;

static void phase_vec_push_source(uint32_t word_bits, uint32_t d, void *ctx) {
    phase_vec_t *vec = (phase_vec_t *)ctx;
    vec->source_count++;
    const uint32_t mask = (d == 32) ? 0xFFFFFFFFU : ((1U << d) - 1U);
    for (uint32_t t = 0; t < d; t++) {
        if (vec->len == vec->cap) {
            size_t new_cap = vec->cap ? vec->cap * 2 : 512;
            phase_rec_t *next = (phase_rec_t *)realloc(vec->data, new_cap * sizeof(phase_rec_t));
            if (!next) {
                fprintf(stderr, "ERROR: out of memory allocating phase vector\n");
                exit(2);
            }
            vec->data = next;
            vec->cap = new_cap;
        }
        uint32_t rot = (t == 0) ? word_bits
                                : (((word_bits >> t) | (word_bits << (d - t))) & mask);
        uint64_t lsb = tile_lsb64(rot, d);
        vec->data[vec->len].rev_key = bitrev64(lsb);
        vec->data[vec->len].lsb_key = lsb;
        vec->data[vec->len].source_bits = word_bits;
        vec->data[vec->len].phase_bits = rot;
        vec->data[vec->len].source_depth = (uint8_t)d;
        vec->data[vec->len].phase_t = (uint8_t)t;
        vec->len++;
    }
}

static int cmp_target_rev(const void *a, const void *b) {
    const target_rec_t *ta = (const target_rec_t *)a;
    const target_rec_t *tb = (const target_rec_t *)b;
    if (ta->rev_key < tb->rev_key) return -1;
    if (ta->rev_key > tb->rev_key) return 1;
    if (ta->depth != tb->depth) return (ta->depth < tb->depth) ? -1 : 1;
    return (ta->word_bits < tb->word_bits) ? -1 : (ta->word_bits > tb->word_bits);
}

static inline size_t lower_bound_targets(
    const target_rec_t *targets, size_t lo, size_t hi, uint64_t key
) {
    while (lo < hi) {
        size_t mid = lo + ((hi - lo) >> 1);
        if (targets[mid].rev_key < key) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return lo;
}

typedef struct {
    uint32_t valuation_e;
    uint32_t source_bits;
    uint32_t phase_bits;
    uint32_t target_bits;
    uint8_t source_depth;
    uint8_t phase_t;
    uint8_t target_depth;
    uint8_t periodic_prefix;
} witness_rec_t;

typedef struct {
    uint32_t threshold;
    uint64_t count;
    uint64_t by_source_depth[33];
    uint64_t by_target_depth[33];
    uint64_t by_phase_t[33];
    uint64_t periodic_ge_75;
    uint64_t periodic_ge_90;
    uint64_t echo_exact_eq_e;
} threshold_stat_t;

static int cmp_witness_desc(const void *a, const void *b) {
    const witness_rec_t *wa = (const witness_rec_t *)a;
    const witness_rec_t *wb = (const witness_rec_t *)b;
    if (wa->valuation_e != wb->valuation_e) {
        return (wa->valuation_e > wb->valuation_e) ? -1 : 1;
    }
    if (wa->source_depth != wb->source_depth) {
        return (wa->source_depth < wb->source_depth) ? -1 : 1;
    }
    if (wa->source_bits != wb->source_bits) {
        return (wa->source_bits < wb->source_bits) ? -1 : 1;
    }
    if (wa->phase_t != wb->phase_t) {
        return (wa->phase_t < wb->phase_t) ? -1 : 1;
    }
    if (wa->target_depth != wb->target_depth) {
        return (wa->target_depth < wb->target_depth) ? -1 : 1;
    }
    return (wa->target_bits < wb->target_bits) ? -1 : (wa->target_bits > wb->target_bits);
}

static int parse_u32_csv(const char *raw, uint32_t *out, int max_n) {
    int count = 0;
    const char *p = raw;
    while (*p && count < max_n) {
        char *end = NULL;
        unsigned long v = strtoul(p, &end, 10);
        if (end == p) break;
        out[count++] = (uint32_t)v;
        p = end;
        while (*p == ',' || *p == ' ') p++;
    }
    return count;
}

static int run_target_tail(int argc, char **argv) {
    uint32_t source_min = 3, source_max = 10;
    uint32_t target_min = 1, target_max = 20;
    uint32_t cutoffs[32];
    int n_cutoffs = 0;
    uint32_t thresholds[32];
    int n_thresholds = 0;
    uint32_t top_n = 16;
    const char *out_path = NULL;

    for (int i = 2; i < argc; i++) {
        if (strcmp(argv[i], "--source-min-depth") == 0 && i + 1 < argc) {
            source_min = (uint32_t)strtoul(argv[++i], NULL, 10);
        } else if (strcmp(argv[i], "--source-max-depth") == 0 && i + 1 < argc) {
            source_max = (uint32_t)strtoul(argv[++i], NULL, 10);
        } else if (strcmp(argv[i], "--target-min-depth") == 0 && i + 1 < argc) {
            target_min = (uint32_t)strtoul(argv[++i], NULL, 10);
        } else if (strcmp(argv[i], "--target-max-depth") == 0 && i + 1 < argc) {
            target_max = (uint32_t)strtoul(argv[++i], NULL, 10);
        } else if (strcmp(argv[i], "--target-cutoffs") == 0 && i + 1 < argc) {
            n_cutoffs = parse_u32_csv(argv[++i], cutoffs, 32);
        } else if (strcmp(argv[i], "--thresholds") == 0 && i + 1 < argc) {
            n_thresholds = parse_u32_csv(argv[++i], thresholds, 32);
        } else if (strcmp(argv[i], "--top-witnesses") == 0 && i + 1 < argc) {
            top_n = (uint32_t)strtoul(argv[++i], NULL, 10);
        } else if (strcmp(argv[i], "--output") == 0 && i + 1 < argc) {
            out_path = argv[++i];
        } else {
            fprintf(stderr, "Unknown argument: %s\n", argv[i]);
            return 2;
        }
    }

    if (source_min < 1 || target_min < 1 || source_min > source_max || target_min > target_max) {
        fprintf(stderr, "ERROR: invalid depth bounds\n");
        return 2;
    }
    if (source_max > 32 || target_max > 32) {
        fprintf(stderr, "ERROR: 64-bit Fine-Wilf exactness requires source_max, target_max <= 32\n");
        return 2;
    }
    if (n_cutoffs == 0) {
        cutoffs[0] = target_max;
        n_cutoffs = 1;
    }
    for (int i = 0; i < n_cutoffs; i++) {
        if (cutoffs[i] > target_max) {
            fprintf(stderr, "ERROR: cutoff %u exceeds target_max %u\n", cutoffs[i], target_max);
            return 2;
        }
    }
    if (n_thresholds == 0) {
        uint32_t def_t[] = {8, 10, 12, 14, 16, 18, 20, 22, 24};
        n_thresholds = 9;
        memcpy(thresholds, def_t, sizeof(def_t));
    }

    double t_start = now_seconds();

    phase_vec_t phases = {0};
    generate_supercritical_lyndon(source_min, source_max, phase_vec_push_source, &phases);

    target_vec_t targets_all = {0};
    generate_supercritical_lyndon(target_min, target_max, target_vec_push, &targets_all);

    double t_gen = now_seconds();

    FILE *fp = stdout;
    if (out_path != NULL) {
        fp = fopen(out_path, "wb");
        if (!fp) {
            fprintf(stderr, "ERROR: cannot open output path %s\n", out_path);
            free(phases.data);
            free(targets_all.data);
            return 2;
        }
    }

    fprintf(fp, "{\n");
    fprintf(fp, "  \"engine\": \"collatz_catalytic_c17_bmi2\",\n");
    fprintf(fp, "  \"status\": \"finite exact measurement only; not a proof of Collatz\",\n");
    fprintf(fp, "  \"exactness_guarantee\": \"Lean 4.35.0 FormalAtlas.Collatz odd-unit-lock isometry + Fine-Wilf ceiling (<= 63 bits for depths <= 32)\",\n");
    fprintf(fp, "  \"parameters\": {\n");
    fprintf(fp, "    \"source_min_depth\": %u,\n", source_min);
    fprintf(fp, "    \"source_max_depth\": %u,\n", source_max);
    fprintf(fp, "    \"target_min_depth\": %u,\n", target_min);
    fprintf(fp, "    \"target_max_depth\": %u,\n", target_max);
    fprintf(fp, "    \"target_cutoffs\": [");
    for (int i = 0; i < n_cutoffs; i++) fprintf(fp, "%s%u", i ? ", " : "", cutoffs[i]);
    fprintf(fp, "],\n    \"thresholds\": [");
    for (int i = 0; i < n_thresholds; i++) fprintf(fp, "%s%u", i ? ", " : "", thresholds[i]);
    fprintf(fp, "]\n  },\n");
    fprintf(fp, "  \"cycle_counts\": {\n");
    fprintf(fp, "    \"primitive_source_cycles\": %zu,\n", phases.source_count);
    fprintf(fp, "    \"source_phases\": %zu,\n", phases.len);
    fprintf(fp, "    \"unique_target_spines_total\": %zu\n", targets_all.len);
    fprintf(fp, "  },\n");
    fprintf(fp, "  \"by_target_cutoff\": {\n");

    target_rec_t *work = (target_rec_t *)malloc((targets_all.len ? targets_all.len : 1) * sizeof(target_rec_t));
    if (!work) {
        fprintf(stderr, "ERROR: out of memory allocating target work buffer\n");
        exit(2);
    }

    uint32_t min_thresh = thresholds[0];
    for (int i = 1; i < n_thresholds; i++) {
        if (thresholds[i] < min_thresh) min_thresh = thresholds[i];
    }

    size_t top_cap = (top_n > 0) ? (size_t)top_n * 4 + 64 : 1;
    witness_rec_t *top_buf = (witness_rec_t *)malloc(top_cap * sizeof(witness_rec_t));

    for (int ci = 0; ci < n_cutoffs; ci++) {
        uint32_t cutoff = cutoffs[ci];
        size_t n_t = 0;
        for (size_t j = 0; j < targets_all.len; j++) {
            if (targets_all.data[j].depth <= cutoff) {
                work[n_t++] = targets_all.data[j];
            }
        }
        qsort(work, n_t, sizeof(target_rec_t), cmp_target_rev);

        uint64_t hist[64];
        memset(hist, 0, sizeof(hist));
        uint64_t pair_count = 0;
        uint64_t zero_skips = 0;
        uint64_t e_sum = 0;
        int max_e = -1;

        threshold_stat_t tstats[32];
        memset(tstats, 0, sizeof(tstats));
        for (int ti = 0; ti < n_thresholds; ti++) {
            tstats[ti].threshold = thresholds[ti];
        }

        size_t top_len = 0;
        uint32_t top_min_e = 0;

        for (size_t pi = 0; pi < phases.len; pi++) {
            const phase_rec_t *ph = &phases.data[pi];
            const uint64_t pkey = ph->rev_key;
            size_t lo = 0, hi = n_t;
            uint64_t prefix = 0;

            for (uint32_t k = 0; k < 64 && lo < hi; k++) {
                const uint64_t bit_mask = 1ULL << (63U - k);
                const uint64_t split_key = prefix | bit_mask;
                size_t mid = lower_bound_targets(work, lo, hi, split_key);

                const bool pbit = (pkey & bit_mask) != 0;
                size_t m_lo, m_hi;
                if (!pbit) {
                    m_lo = mid;
                    m_hi = hi;
                    hi = mid;
                } else {
                    m_lo = lo;
                    m_hi = mid;
                    lo = mid;
                    prefix |= bit_mask;
                }

                const uint64_t cnt = (uint64_t)(m_hi - m_lo);
                if (cnt == 0) continue;

                hist[k] += cnt;
                pair_count += cnt;
                e_sum += cnt * (uint64_t)k;
                if ((int)k > max_e) max_e = (int)k;

                bool need_detail = (k >= min_thresh) || (top_n > 0 && (top_len < top_n || k >= top_min_e));
                if (need_detail) {
                    for (size_t idx = m_lo; idx < m_hi; idx++) {
                        const target_rec_t *tg = &work[idx];
                        uint64_t tg_lsb = bitrev64(tg->rev_key);
                        uint32_t pfx = periodic_prefix_len_u64(ph->lsb_key, tg_lsb, tg->depth);

                        for (int ti = 0; ti < n_thresholds; ti++) {
                            if (k >= tstats[ti].threshold) {
                                tstats[ti].count++;
                                tstats[ti].by_source_depth[ph->source_depth]++;
                                tstats[ti].by_target_depth[tg->depth]++;
                                tstats[ti].by_phase_t[ph->phase_t]++;
                                if (pfx * 4U >= tg->depth * 3U) {
                                    tstats[ti].periodic_ge_75++;
                                }
                                if (pfx * 10U >= tg->depth * 9U) {
                                    tstats[ti].periodic_ge_90++;
                                }
                                if (pfx == k) {
                                    tstats[ti].echo_exact_eq_e++;
                                }
                            }
                        }

                        if (top_n > 0 && (top_len < top_n || k >= top_min_e)) {
                            if (top_len == top_cap) {
                                qsort(top_buf, top_len, sizeof(witness_rec_t), cmp_witness_desc);
                                top_len = top_n;
                                top_min_e = top_buf[top_len - 1].valuation_e;
                            }
                            if (top_len < top_n || k >= top_min_e) {
                                witness_rec_t *w = &top_buf[top_len++];
                                w->valuation_e = k;
                                w->source_bits = ph->source_bits;
                                w->phase_bits = ph->phase_bits;
                                w->target_bits = tg->word_bits;
                                w->source_depth = ph->source_depth;
                                w->phase_t = ph->phase_t;
                                w->target_depth = tg->depth;
                                w->periodic_prefix = (uint8_t)pfx;
                            }
                        }
                    }
                }
            }

            if (lo < hi) {
                zero_skips += (uint64_t)(hi - lo);
            }
        }

        if (top_len > 0) {
            qsort(top_buf, top_len, sizeof(witness_rec_t), cmp_witness_desc);
            if (top_len > top_n) top_len = top_n;
        }

        double avg_e = pair_count ? ((double)e_sum / (double)pair_count) : 0.0;
        fprintf(fp, "    \"%u\": {\n", cutoff);
        fprintf(fp, "      \"target_spines\": %zu,\n", n_t);
        fprintf(fp, "      \"source_phase_target_pairs\": %" PRIu64 ",\n", pair_count);
        fprintf(fp, "      \"zero_separation_skips\": %" PRIu64 ",\n", zero_skips);
        if (max_e >= 0) {
            fprintf(fp, "      \"max_valuation_e\": %d,\n", max_e);
        } else {
            fprintf(fp, "      \"max_valuation_e\": null,\n");
        }
        fprintf(fp, "      \"avg_valuation_e\": %.9f,\n", avg_e);

        fprintf(fp, "      \"valuation_histogram\": {");
        bool first_h = true;
        for (uint32_t k = 0; k < 64; k++) {
            if (hist[k] > 0) {
                fprintf(fp, "%s\"%u\": %" PRIu64, first_h ? "" : ", ", k, hist[k]);
                first_h = false;
            }
        }
        fprintf(fp, "},\n");

        fprintf(fp, "      \"tail_comparison\": [\n");
        for (int ti = 0; ti < n_thresholds; ti++) {
            const threshold_stat_t *ts = &tstats[ti];
            double frac = pair_count ? ((double)ts->count / (double)pair_count) : 0.0;
            double geom = (double)pair_count / (double)(1ULL << ts->threshold);
            double ratio = (geom > 0.0) ? ((double)ts->count / geom) : 0.0;
            fprintf(fp, "        {\n");
            fprintf(fp, "          \"threshold_e_ge\": %u,\n", ts->threshold);
            fprintf(fp, "          \"count\": %" PRIu64 ",\n", ts->count);
            fprintf(fp, "          \"fraction\": %.15f,\n", frac);
            fprintf(fp, "          \"geometric_expected_count\": %.6f,\n", geom);
            fprintf(fp, "          \"observed_over_geometric\": %.6f,\n", ratio);
            fprintf(fp, "          \"phase_0_count\": %" PRIu64 ",\n", ts->by_phase_t[0]);
            fprintf(fp, "          \"periodic_prefix_ge_75pct\": %" PRIu64 ",\n", ts->periodic_ge_75);
            fprintf(fp, "          \"periodic_prefix_ge_90pct\": %" PRIu64 ",\n", ts->periodic_ge_90);
            fprintf(fp, "          \"exact_echo_e_eq_prefix\": %" PRIu64 "\n", ts->echo_exact_eq_e);
            fprintf(fp, "        }%s\n", (ti + 1 < n_thresholds) ? "," : "");
        }
        fprintf(fp, "      ],\n");

        fprintf(fp, "      \"top_witnesses\": [\n");
        for (size_t wi = 0; wi < top_len; wi++) {
            const witness_rec_t *w = &top_buf[wi];
            char sbuf[40], pbuf[40], tbuf[40];
            format_word(w->source_bits, w->source_depth, sbuf);
            format_word(w->phase_bits, w->source_depth, pbuf);
            format_word(w->target_bits, w->target_depth, tbuf);
            double pfrac = (double)w->periodic_prefix / (double)w->target_depth;
            fprintf(fp,
                "        {\"valuation_e\": %u, \"source\": \"%s\", \"source_depth\": %u, "
                "\"phase_t\": %u, \"phase_word\": \"%s\", \"target\": \"%s\", "
                "\"target_depth\": %u, \"periodic_prefix_len\": %u, "
                "\"periodic_prefix_fraction\": %.6f}%s\n",
                w->valuation_e, sbuf, w->source_depth, w->phase_t, pbuf,
                tbuf, w->target_depth, w->periodic_prefix, pfrac,
                (wi + 1 < top_len) ? "," : "");
        }
        fprintf(fp, "      ]\n");
        fprintf(fp, "    }%s\n", (ci + 1 < n_cutoffs) ? "," : "");
    }

    double t_end = now_seconds();
    fprintf(fp, "  },\n");
    fprintf(fp, "  \"timings_seconds\": {\n");
    fprintf(fp, "    \"lyndon_generation\": %.6f,\n", t_gen - t_start);
    fprintf(fp, "    \"prefix_slice_analysis\": %.6f,\n", t_end - t_gen);
    fprintf(fp, "    \"total\": %.6f\n", t_end - t_start);
    fprintf(fp, "  }\n");
    fprintf(fp, "}\n");

    if (out_path != NULL) fclose(fp);
    free(top_buf);
    free(work);
    free(phases.data);
    free(targets_all.data);
    return 0;
}

/* ============================================================================
 * Mode 2: Catalytic Zero-Allocation DFS Finite-Residue Descent Certificate Miner
 * ============================================================================ */

typedef struct {
    uint32_t depth;
    uint32_t odd_count;
    uint64_t residue;
    __uint128_t image; /* exact T^depth(residue) */
} dfs_frame_t;

static void print_u128(FILE *fp, __uint128_t v) {
    if (v == 0) {
        fputc('0', fp);
        return;
    }
    char buf[48];
    int pos = 0;
    while (v > 0) {
        buf[pos++] = (char)('0' + (int)(v % 10));
        v /= 10;
    }
    for (int i = pos - 1; i >= 0; i--) fputc(buf[i], fp);
}

static int run_residue_mine(int argc, char **argv) {
    uint32_t max_depth = 20;
    for (int i = 2; i < argc; i++) {
        if (strcmp(argv[i], "--max-depth") == 0 && i + 1 < argc) {
            max_depth = (uint32_t)strtoul(argv[++i], NULL, 10);
        } else {
            fprintf(stderr, "Unknown argument: %s\n", argv[i]);
            return 2;
        }
    }
    if (max_depth < 1 || max_depth > 48) {
        fprintf(stderr, "ERROR: --max-depth must be in [1, 48] for exact 128-bit arithmetic\n");
        return 2;
    }

    __uint128_t pow3[64];
    pow3[0] = 1;
    for (uint32_t i = 1; i <= max_depth; i++) pow3[i] = pow3[i - 1] * 3;

    double t_start = now_seconds();

    dfs_frame_t stack[128];
    int sp = 0;
    stack[sp++] = (dfs_frame_t){1, 1, 1ULL, 2};
    stack[sp++] = (dfs_frame_t){1, 0, 0ULL, 0};

    uint64_t certified_leaves = 0;
    uint64_t frontier_leaves = 0;
    __uint128_t certified_units = 0;
    __uint128_t frontier_units = 0;
    __uint128_t scale = ((__uint128_t)1) << max_depth;
    uint32_t deepest_cert = 0;
    __uint128_t max_q_thresh = 0;
    __uint128_t finite_q_exceptions = 0;
    uint64_t odd_hist[64];
    memset(odd_hist, 0, sizeof(odd_hist));

    while (sp > 0) {
        dfs_frame_t cur = stack[--sp];
        __uint128_t two_d = ((__uint128_t)1) << cur.depth;
        __uint128_t p3 = pow3[cur.odd_count];

        if (p3 < two_d) {
            certified_leaves++;
            certified_units += (scale >> cur.depth);
            if (cur.depth > deepest_cert) deepest_cert = cur.depth;
            __uint128_t denom = two_d - p3;
            __uint128_t q_thresh = 0;
            if (cur.image >= (__uint128_t)cur.residue) {
                q_thresh = ((cur.image - (__uint128_t)cur.residue) / denom) + 1;
            }
            finite_q_exceptions += q_thresh;
            if (q_thresh > max_q_thresh) max_q_thresh = q_thresh;
            continue;
        }

        if (cur.depth >= max_depth) {
            frontier_leaves++;
            frontier_units++;
            odd_hist[cur.odd_count]++;
            continue;
        }

        uint32_t nd = cur.depth + 1;
        uint64_t r0 = cur.residue;
        uint64_t r1 = cur.residue | (1ULL << cur.depth);

        __uint128_t img0 = cur.image;
        uint32_t o0 = cur.odd_count + (uint32_t)(img0 & 1U);
        img0 = (img0 & 1U) ? ((3 * img0 + 1) >> 1) : (img0 >> 1);

        __uint128_t img1 = cur.image + p3;
        uint32_t o1 = cur.odd_count + (uint32_t)(img1 & 1U);
        img1 = (img1 & 1U) ? ((3 * img1 + 1) >> 1) : (img1 >> 1);

        stack[sp++] = (dfs_frame_t){nd, o1, r1, img1};
        stack[sp++] = (dfs_frame_t){nd, o0, r0, img0};
    }

    double elapsed = now_seconds() - t_start;
    double cert_frac = (double)certified_units / (double)scale;
    double front_frac = (double)frontier_units / (double)scale;

    printf("{\n");
    printf("  \"engine\": \"collatz_catalytic_dfs_c17\",\n");
    printf("  \"status\": \"%s\",\n", frontier_leaves == 0 ? "finite-cover" : "open-frontier");
    printf("  \"max_depth\": %u,\n", max_depth);
    printf("  \"elapsed_seconds\": %.6f,\n", elapsed);
    printf("  \"stack_memory_bytes\": %zu,\n", sizeof(stack));
    printf("  \"certified_leaves\": %" PRIu64 ",\n", certified_leaves);
    printf("  \"frontier_leaves\": %" PRIu64 ",\n", frontier_leaves);
    printf("  \"certified_fraction\": %.16f,\n", cert_frac);
    printf("  \"frontier_fraction\": %.16f,\n", front_frac);
    printf("  \"certified_units_mod_2^max_depth\": ");
    print_u128(stdout, certified_units);
    printf(",\n  \"frontier_units_mod_2^max_depth\": ");
    print_u128(stdout, frontier_units);
    printf(",\n  \"deepest_certificate\": %u,\n", deepest_cert);
    printf("  \"max_q_threshold\": ");
    print_u128(stdout, max_q_thresh);
    printf(",\n  \"finite_q_exceptions_upper_bound\": ");
    print_u128(stdout, finite_q_exceptions);
    printf(",\n  \"frontier_odd_count_histogram\": {");
    bool first = true;
    for (uint32_t o = 0; o <= max_depth; o++) {
        if (odd_hist[o] > 0) {
            printf("%s\"%u\": %" PRIu64, first ? "" : ", ", o, odd_hist[o]);
            first = false;
        }
    }
    printf("}\n}\n");
    return 0;
}

/* ============================================================================
 * Mode 3: Built-In Exact Self-Test (15,876-Pair Direct Big-Int Differential)
 * ============================================================================ */

static int run_self_test(void) {
    typedef struct { uint32_t bits; uint32_t d; __int128 c; __int128 D; uint64_t lsb; } w_t;
    w_t words[128];
    int nw = 0;
    for (uint32_t d = 1; d <= 6; d++) {
        for (uint32_t b = 0; b < (1U << d); b++) {
            __int128 c = 0, p3 = 1;
            for (uint32_t i = 0; i < d; i++) {
                if ((b >> i) & 1U) {
                    c = 3 * c + ((__int128)1 << i);
                    p3 *= 3;
                }
            }
            __int128 D = ((__int128)1 << d) - p3;
            words[nw++] = (w_t){b, d, c, D, tile_lsb64(b, d)};
        }
    }

    uint64_t checked = 0;
    for (int i = 0; i < nw; i++) {
        for (int j = 0; j < nw; j++) {
            __int128 num = words[i].c * words[j].D - words[j].c * words[i].D;
            uint64_t x = words[i].lsb ^ words[j].lsb;
            if (num == 0) {
                if (x != 0) {
                    fprintf(stderr, "SELF-TEST FAIL: equal spine had nonzero XOR\n");
                    return 1;
                }
            } else {
                __uint128_t mag = (num < 0) ? (__uint128_t)(-num) : (__uint128_t)num;
                uint32_t v2 = 0;
                while ((mag & 1U) == 0) { mag >>= 1; v2++; }
                if (x == 0) {
                    fprintf(stderr, "SELF-TEST FAIL: distinct spine had zero XOR\n");
                    return 1;
                }
                uint32_t lcp = (uint32_t)__builtin_ctzll(x);
                if (v2 != lcp) {
                    fprintf(stderr, "SELF-TEST FAIL: v2=%u != lcp=%u\n", v2, lcp);
                    return 1;
                }
                uint64_t rx = bitrev64(words[i].lsb) ^ bitrev64(words[j].lsb);
                uint32_t clz = (uint32_t)__builtin_clzll(rx);
                if (clz != lcp) {
                    fprintf(stderr, "SELF-TEST FAIL: clz(bitrev)=%u != lcp=%u\n", clz, lcp);
                    return 1;
                }
            }
            checked++;
        }
    }
    printf("collatz_catalytic self-test PASS: %" PRIu64 " exact spine pairs verified (0 mismatches).\n", checked);
    return 0;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr,
            "Usage:\n"
            "  collatz_catalytic self-test\n"
            "  collatz_catalytic target-tail [--source-min-depth N] [--source-max-depth N]\n"
            "                                [--target-min-depth N] [--target-max-depth N]\n"
            "                                [--target-cutoffs a,b,...] [--thresholds a,b,...]\n"
            "                                [--top-witnesses N] [--output PATH]\n"
            "  collatz_catalytic residue-mine [--max-depth N]\n");
        return 1;
    }
    if (strcmp(argv[1], "self-test") == 0) return run_self_test();
    if (strcmp(argv[1], "target-tail") == 0) return run_target_tail(argc, argv);
    if (strcmp(argv[1], "residue-mine") == 0) return run_residue_mine(argc, argv);
    fprintf(stderr, "Unknown command: %s\n", argv[1]);
    return 2;
}
#endif
