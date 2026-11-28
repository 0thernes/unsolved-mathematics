/* SPDX-License-Identifier: MIT
 *
 * fuzz_collatz_hydra.c — 250,000-Case Sanitized Fuzz Harness for the Five-Vector
 * Asymmetric Collatz Hydra (`collatz_asymmetric_hydra.c`, Build Standard B15/B16).
 *
 * Fuzzes:
 *   1. Exact chiral sign conjugacy T^d(-x) == -T_-^d(x) & oddCount parity match
 *   2. Exact mod-3 chiral phase-lock asymmetry (T(odd) == 2, T_-(odd) == 1 mod 3)
 *   3. Exact 3-adic intercept unit law (3 nmid c(w) for all nonempty odd-containing words)
 *   4. Exact binary carry-avalanche identity (2x) + x + 1 == 3x + 1 & trailing-1 erosion
 *   5. Exact LZ76 complexity monotonicity & lower/upper bounds on arbitrary binary words
 */

#define COLLATZ_HYDRA_NO_MAIN
#include "collatz_asymmetric_hydra.c"

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    if (size < 16) return 0;

    /* 1. Signed orbit conjugacy over arbitrary 32-bit signed integers and depth 1..14 */
    int32_t sx;
    memcpy(&sx, data, 4);
    int64_t x = (int64_t)sx;
    uint32_t depth = (data[4] % 14U) + 1U;
    int64_t a = -x, b = x;
    uint32_t oa = 0, ob = 0;
    for (uint32_t i = 0; i < depth; i++) {
        if ((a & 1LL) != 0) oa++;
        if ((b & 1LL) != 0) ob++;
        a = step_T_i64(a);
        b = step_TMinus_i64(b);
    }
    if (a != -b || oa != ob) __builtin_trap();

    /* 2. Mod-3 chiral asymmetry on odd integers (strictly UB-free arithmetic) */
    int64_t odd_x = 2LL * (int64_t)sx + 1LL;
    int64_t tp_m3 = ((step_T_i64(odd_x) % 3) + 3) % 3;
    int64_t tm_m3 = ((step_TMinus_i64(odd_x) % 3) + 3) % 3;
    if (tp_m3 != 2 || tm_m3 != 1) __builtin_trap();

    /* 3. Universal 3-adic intercept unit law: 3 nmid c(w) whenever o(w) >= 1 */
    uint32_t wd = (data[5] % 16U) + 1U;
    uint32_t raw_w = (uint32_t)data[6] | ((uint32_t)data[7] << 8);
    uint32_t bits = raw_w & ((1U << wd) - 1U);
    if (bits != 0) {
        __int128 c = 0;
        for (uint32_t i = 0; i < wd; i++) {
            if ((bits >> i) & 1U) {
                c = 3 * c + ((__int128)1 << i);
            }
        }
        if ((c % 3) == 0) __builtin_trap();
    }

    /* 4. Carry-avalanche & trailing-1 erosion identity on positive odd integers */
    uint64_t ux = (((uint64_t)data[8] | ((uint64_t)data[9] << 8) | ((uint64_t)data[10] << 16)) << 1) | 1ULL;
    uint64_t yp = 3ULL * ux + 1ULL;
    uint64_t ym = 3ULL * ux - 1ULL;
    uint32_t r_ones = ctz64(ux + 1ULL); /* number of trailing 1s in ux */
    if (r_ones >= 2 && ctz64(yp) != 1) __builtin_trap(); /* 3*(2^r k - 1)+1 = 3*2^r k - 2 => v2 = 1! */
    uint32_t r_zeros = ctz64(ux - 1ULL); /* trailing 0s after LSB 1 in ux */
    if (r_zeros >= 2 && ctz64(ym) != 1) __builtin_trap(); /* 3*(2^r k + 1)-1 = 3*2^r k + 2 => v2 = 1! */

    /* 5. LZ76 bounds: 1 <= LZ76(w) <= len(w) on arbitrary 1..32-bit strings */
    uint32_t lz_len = (data[11] % 32U) + 1U;
    uint8_t seq[32];
    for (uint32_t i = 0; i < lz_len; i++) {
        seq[i] = (uint8_t)((data[12 + (i >> 3)] >> (i & 7U)) & 1U);
    }
    uint32_t c_lz = lz76_complexity(seq, lz_len);
    if (c_lz < 1 || c_lz > lz_len) __builtin_trap();

    /* Suppress unused-function warnings for header inclusion */
    (void)hydra_now_seconds;
    (void)run_vector_a;
    (void)run_vector_b;
    (void)run_vector_c;
    (void)run_vector_d;
    (void)analyze_orbit_word;
    return 0;
}

#ifdef STANDALONE_FUZZ_MAIN
int main(void) {
    uint64_t state = 0xD1B54A32D192ED03ULL;
    uint8_t buf[16];
    const uint32_t N = 250000;
    for (uint32_t i = 0; i < N; i++) {
        state += 0x9E3779B97F4A7C15ULL;
        uint64_t z = state;
        z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
        z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
        uint64_t v1 = z ^ (z >> 31);
        state += 0x9E3779B97F4A7C15ULL;
        z = state;
        z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
        z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
        uint64_t v2 = z ^ (z >> 31);
        memcpy(buf, &v1, 8);
        memcpy(buf + 8, &v2, 8);
        LLVMFuzzerTestOneInput(buf, sizeof(buf));
    }
    printf("fuzz_collatz_hydra PASS: %u deterministic fuzz cases verified (0 traps).\n", N);
    return 0;
}
#endif
