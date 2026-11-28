/* SPDX-License-Identifier: MIT
 *
 * fuzz_collatz_catalytic.c — libFuzzer + Deterministic Corpus Fuzz Harness
 * (Build Standard v1.2.0 item B15 + B16).
 *
 * Fuzzes the core exact 2-adic valuation isometry, Fine-Wilf ceiling, bit-reversal,
 * periodic tiling, and cylinder affine lifting against independent 128-bit exact
 * integer arithmetic across arbitrary fuzzer-supplied bit patterns.
 *
 * Build with Clang libFuzzer + ASan/UBSan:
 *   clang -O1 -g -fsanitize=fuzzer,address,undefined fuzz_collatz_catalytic.c -o fuzz_collatz
 *
 * Or standalone deterministic corpus mode (GCC / Zig CC with UBSan):
 *   gcc -O2 -DSTANDALONE_FUZZ_MAIN -Wall -Wextra -Werror fuzz_collatz_catalytic.c -o fuzz_collatz
 */

#define COLLATZ_CATALYTIC_NO_MAIN
#include "collatz_catalytic.c"

static uint32_t gcd_u32(uint32_t a, uint32_t b) {
    while (b != 0) {
        uint32_t t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    if (size < 10) return 0;

    /* Extract two arbitrary words of lengths d1, d2 in [1, 18] (fits exact 128-bit c, D). */
    uint32_t d1 = (data[0] % 18U) + 1U;
    uint32_t d2 = (data[1] % 18U) + 1U;
    uint32_t raw1 = (uint32_t)data[2] | ((uint32_t)data[3] << 8) | ((uint32_t)data[4] << 16);
    uint32_t raw2 = (uint32_t)data[5] | ((uint32_t)data[6] << 8) | ((uint32_t)data[7] << 16);
    uint32_t b1 = raw1 & ((1U << d1) - 1U);
    uint32_t b2 = raw2 & ((1U << d2) - 1U);

    /* Independent 128-bit exact spine numerator/denominator calculation. */
    __int128 c1 = 0, p3_1 = 1;
    for (uint32_t i = 0; i < d1; i++) {
        if ((b1 >> i) & 1U) {
            c1 = 3 * c1 + ((__int128)1 << i);
            p3_1 *= 3;
        }
    }
    __int128 D1 = ((__int128)1 << d1) - p3_1;

    __int128 c2 = 0, p3_2 = 1;
    for (uint32_t i = 0; i < d2; i++) {
        if ((b2 >> i) & 1U) {
            c2 = 3 * c2 + ((__int128)1 << i);
            p3_2 *= 3;
        }
    }
    __int128 D2 = ((__int128)1 << d2) - p3_2;

    uint64_t lsb1 = tile_lsb64(b1, d1);
    uint64_t lsb2 = tile_lsb64(b2, d2);
    uint64_t msb1 = tile_msb64(b1, d1);
    uint64_t msb2 = tile_msb64(b2, d2);

    /* Invariant 1: bitrev64 is an exact involution, periodic_prefix_len_u64 matches exact bit scan,
     * and min_supercritical_ones satisfies 3^(o-1) <= 2^d < 3^o. */
    if (bitrev64(msb1) != lsb1 || bitrev64(msb2) != lsb2) __builtin_trap();
    uint32_t o_min = min_supercritical_ones(d1);
    __uint128_t p3_lo = 1;
    for (uint32_t s = 0; s + 1 < o_min; s++) p3_lo *= 3;
    if (o_min == 0 || p3_lo > ((__uint128_t)1 << d1) || p3_lo * 3 <= ((__uint128_t)1 << d1)) {
        __builtin_trap();
    }
    uint32_t pfx_fast = periodic_prefix_len_u64(lsb1, lsb2, d2);
    uint32_t pfx_ref = d2;
    for (uint32_t k = 0; k < d2; k++) {
        if (((b1 >> (k % d1)) & 1U) != ((b2 >> k) & 1U)) {
            pfx_ref = k;
            break;
        }
    }
    if (pfx_fast != pfx_ref) __builtin_trap();
    char wbuf[40];
    format_word(b1, d1, wbuf);
    if (strlen(wbuf) != d1) __builtin_trap();
    (void)generate_supercritical_lyndon;
    (void)now_seconds;

    /* Invariant 2: Lean-proved Odd-Unit-Lock valuation isometry & Fine-Wilf ceiling. */
    __int128 sep = c1 * D2 - c2 * D1;
    uint64_t diff_lsb = lsb1 ^ lsb2;
    uint64_t diff_msb = msb1 ^ msb2;
    if (sep == 0) {
        if (diff_lsb != 0 || diff_msb != 0) __builtin_trap();
    } else {
        if (diff_lsb == 0 || diff_msb == 0) __builtin_trap();
        __uint128_t mag = (sep < 0) ? (__uint128_t)(-sep) : (__uint128_t)sep;
        uint32_t v2 = 0;
        while ((mag & 1U) == 0) { mag >>= 1; v2++; }
        uint32_t lcp = (uint32_t)__builtin_ctzll(diff_lsb);
        uint32_t clz = (uint32_t)__builtin_clzll(diff_msb);
        uint32_t fw_max = d1 + d2 - gcd_u32(d1, d2) - 1U;
        if (v2 != lcp || clz != lcp || v2 > fw_max) __builtin_trap();
    }

    /* Invariant 3: Cylinder affine lift matches direct shortcut Collatz iteration. */
    uint32_t depth = (data[8] % 16U) + 1U;
    uint64_t r = (uint64_t)(raw1 & ((1U << depth) - 1U));
    uint64_t q = (uint64_t)data[9];
    uint64_t x_r = r;
    uint32_t o = 0;
    for (uint32_t s = 0; s < depth; s++) {
        if (x_r & 1ULL) { o++; x_r = (3ULL * x_r + 1ULL) >> 1; }
        else { x_r >>= 1; }
    }
    __uint128_t p3 = 1;
    for (uint32_t s = 0; s < o; s++) p3 *= 3;
    __uint128_t x_n = ((__uint128_t)q << depth) + r;
    for (uint32_t s = 0; s < depth; s++) {
        x_n = (x_n & 1U) ? ((3 * x_n + 1) >> 1) : (x_n >> 1);
    }
    if (x_n != p3 * q + x_r) __builtin_trap();

    return 0;
}

#ifdef STANDALONE_FUZZ_MAIN
int main(void) {
    /* Deterministic SplitMix64 corpus: 250,000 adversarial random cases. */
    uint64_t state = 0x9E3779B97F4A7C15ULL;
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
    printf("fuzz_collatz_catalytic PASS: %u deterministic fuzz cases verified (0 traps).\n", N);
    return 0;
}
#endif
