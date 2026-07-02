# ChatGPT Share Ingest - 2026-07-02

This ledger records how the four shared ChatGPT links were treated. The links
are useful research prompts, not evidence. Sandbox attachments from those
shares were not available in this repo, so only locally reproduced claims are
accepted.

## Links

1. https://chatgpt.com/share/6a46ab12-6df8-83ec-8c83-3ad580b9daae
2. https://chatgpt.com/share/6a46ab08-8f38-83ec-9b68-f37740f93826
3. https://chatgpt.com/share/6a46aafc-df94-83ec-9e39-0a4838f4bd58
4. https://chatgpt.com/share/6a46aae7-a2a8-83ec-836e-1db1cdfa6c3a

## Triage

### Link 1: Regeneration Sieve

Accepted as a theorem target and implemented locally in stronger phase form.
The block-boundary normal form is exact:

```text
F_w^k(x) - eta = 2^(s-kd) u 3^(ko) + (rho_w - eta).
```

Its key consequence is also exact: if the leftover alignment `s-kd` does not
match `v2(rho_w - eta)`, deep cancellation is impossible.

Local follow-up: [`SPINE-PHASE-COLLISION.md`](SPINE-PHASE-COLLISION.md) and
[`spine_phase_collision_lab.py`](spine_phase_collision_lab.py).

### Link 2: Phase-Collision Sprint

Accepted as the main actionable direction. The phase-to-target formula is
exact and was verified locally:

```text
T^t(x) - eta = 3^a(t) 2^(m-t) u + (rho_t - eta).
```

The shared negative result is important: phase matching alone is too weak.
The local script stores explicit denominator choices for the phase-gate
statistics because the shared aggregate count mixes primitive/nonprimitive
cycle conventions.

### Link 3: Round 20 Survival Extension

Not accepted as repo evidence in this run. The claim is a very large external
scan:

```text
M_+(606) > 3,231,751,768,559
```

with sandboxed C++ sources and manifests unavailable here. This remains an
unverified external computational claim until its source, manifest, and command
log are present locally and rerun or independently audited.

### Link 4: Round 21 Density / Boundary Package

Partially accepted. The density-zero theorem for coefficient-barrier survivors
is standard entropy-counting and is locally reproducible by dynamic programming.
The boundary-ray audit through `k <= 200000` is not accepted as evidence here
because the sandbox package was unavailable. The new local lab reproduces the
cheap exact pieces: density counts through `k=4096` and the critical
inverse-residue fingerprint through `L=512`.

## Current Verdict

No proof of Collatz was obtained. The useful distilled frontier is:

```text
Collatz as a positivity-sensitive phase-collision and odd-unit-lock problem.
```

The next honest theorem target is to show that repeated deep regeneration locks
have cumulative codimension larger than the entropy of admissible survivor
branches, while consuming value-positivity rather than only parity-word data.

