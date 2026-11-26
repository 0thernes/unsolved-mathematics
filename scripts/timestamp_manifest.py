#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Dual Cryptographic Timestamping (DigiCert RFC 3161 .tsr + Bitcoin OpenTimestamps .ots).

Cryptographically binds `data/MANIFEST.sha256` to two independent public third-party
timestamp authorities (zero credentials required):
  1. DigiCert RFC 3161 TSA (`http://timestamp.digicert.com`) -> `data/MANIFEST.sha256.tsr`
  2. Bitcoin OpenTimestamps 3-calendar pool -> `data/MANIFEST.sha256.ots`

Usage:
    python scripts/timestamp_manifest.py          # mint fresh .tsr and .ots proofs
    python scripts/timestamp_manifest.py --check  # offline cryptographic imprint verification
"""

from __future__ import annotations

import argparse
import hashlib
import secrets
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data" / "MANIFEST.sha256"
TSR_PATH = ROOT / "data" / "MANIFEST.sha256.tsr"
OTS_PATH = ROOT / "data" / "MANIFEST.sha256.ots"

TSA_URL = "http://timestamp.digicert.com"
OTS_CALENDARS = [
    "https://a.pool.opentimestamps.org/digest",
    "https://b.pool.opentimestamps.org/digest",
    "https://a.pool.eternitywall.com/digest",
]
OTS_HEADER = b"\x00OpenTimestamps\x00\x00Proof\x00\xbf\x89\xe2\xe8\x84\xe8\x92\x94\x01"
USER_AGENT = "unsolved-mathematics/0.6.0 (https://github.com/0thernes/unsolved-mathematics)"


def der_len(n: int) -> bytes:
    if n < 0x80:
        return bytes([n])
    raw = n.to_bytes((n.bit_length() + 7) // 8, "big")
    return bytes([0x80 | len(raw)]) + raw


def der_tlv(tag: int, body: bytes) -> bytes:
    return bytes([tag]) + der_len(len(body)) + body


def build_rfc3161_request(sha256_digest: bytes) -> bytes:
    """Build ASN.1 DER RFC 3161 TimeStampReq for a 32-byte SHA-256 digest."""
    # OID 2.16.840.1.101.3.4.2.1 (id-sha256)
    oid_sha256 = der_tlv(0x06, bytes([0x60, 0x86, 0x48, 0x01, 0x65, 0x03, 0x04, 0x02, 0x01]))
    alg_id = der_tlv(0x30, oid_sha256 + der_tlv(0x05, b""))
    msg_imprint = der_tlv(0x30, alg_id + der_tlv(0x04, sha256_digest))
    version = der_tlv(0x02, b"\x01")
    nonce_bytes = secrets.token_bytes(8)
    if nonce_bytes[0] & 0x80:
        nonce_bytes = b"\x00" + nonce_bytes
    nonce = der_tlv(0x02, nonce_bytes)
    cert_req = der_tlv(0x01, b"\xff")
    return der_tlv(0x30, version + msg_imprint + nonce + cert_req)


def mint_rfc3161(digest: bytes) -> bytes:
    tsq = build_rfc3161_request(digest)
    req = urllib.request.Request(
        TSA_URL,
        data=tsq,
        headers={
            "Content-Type": "application/timestamp-query",
            "User-Agent": USER_AGENT,
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        tsr = resp.read()
    verify_tsr_bytes(tsr, digest)
    return tsr


def mint_ots(digest: bytes) -> bytes:
    branches: list[bytes] = []
    for url in OTS_CALENDARS:
        try:
            req = urllib.request.Request(
                url,
                data=digest,
                headers={
                    "Accept": "application/vnd.opentimestamps.v1",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": USER_AGENT,
                },
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=20) as resp:
                chunk = resp.read()
                if chunk:
                    branches.append(chunk)
        except Exception as exc:
            print(f"WARN: OTS calendar {url} skipped: {exc}", file=sys.stderr)
    if not branches:
        raise RuntimeError("No OpenTimestamps calendar server responded.")
    # OTS v1 format: HEADER + 0x08 (SHA256) + 32-byte digest + forks (\xff before all but last)
    out = bytearray(OTS_HEADER)
    out.append(0x08)
    out.extend(digest)
    for idx, br in enumerate(branches):
        if idx < len(branches) - 1:
            out.append(0xFF)
        out.extend(br)
    return bytes(out)


def verify_tsr_bytes(tsr: bytes, digest: bytes) -> None:
    if len(tsr) < 100 or tsr[0] != 0x30:
        raise ValueError("Invalid RFC 3161 TSR: missing outer ASN.1 SEQUENCE.")
    # PKIStatusInfo: SEQUENCE { INTEGER 0 } = 30 03 02 01 00
    if b"\x30\x03\x02\x01\x00" not in tsr[:32]:
        raise ValueError("Invalid RFC 3161 TSR: PKIStatus is not granted (0).")
    # Exact SHA-256 OCTET STRING (04 20 <32-byte digest>) embedded in TSTInfo messageImprint
    if (b"\x04\x20" + digest) not in tsr:
        raise ValueError("RFC 3161 TSR messageImprint does NOT match current data/MANIFEST.sha256 SHA-256!")


def verify_ots_bytes(ots: bytes, digest: bytes) -> None:
    prefix = OTS_HEADER + b"\x08" + digest
    if not ots.startswith(prefix):
        raise ValueError("OpenTimestamps .ots header or SHA-256 digest does NOT match current data/MANIFEST.sha256!")
    if len(ots) <= len(prefix) + 20:
        raise ValueError("OpenTimestamps .ots proof appears truncated (missing calendar attestation).")


def find_openssl() -> str | None:
    found = shutil.which("openssl")
    if found:
        return found
    for cand in (
        Path(r"C:\Program Files\Git\usr\bin\openssl.exe"),
        Path(r"C:\Program Files\Git\mingw64\bin\openssl.exe"),
    ):
        if cand.exists():
            return str(cand)
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Mint or verify RFC 3161 .tsr + Bitcoin OTS .ots timestamps.")
    parser.add_argument("--check", action="store_true", help="Verify offline that .tsr and .ots match data/MANIFEST.sha256.")
    args = parser.parse_args()

    if not MANIFEST.exists():
        print("ERROR: data/MANIFEST.sha256 missing.", file=sys.stderr)
        return 1
    digest = hashlib.sha256(MANIFEST.read_bytes()).digest()

    if args.check:
        if not TSR_PATH.exists() or not OTS_PATH.exists():
            print("ERROR: Missing data/MANIFEST.sha256.tsr or .ots — run python scripts/timestamp_manifest.py", file=sys.stderr)
            return 1
        try:
            verify_tsr_bytes(TSR_PATH.read_bytes(), digest)
            verify_ots_bytes(OTS_PATH.read_bytes(), digest)
        except ValueError as exc:
            print(f"TIMESTAMP CHECK FAILED: {exc}", file=sys.stderr)
            return 1
        print(
            f"OK: Dual cryptographic timestamps verified offline against data/MANIFEST.sha256 "
            f"(sha256={digest.hex()[:16]}...; .tsr={TSR_PATH.stat().st_size}B, .ots={OTS_PATH.stat().st_size}B)."
        )
        return 0

    tsr = mint_rfc3161(digest)
    TSR_PATH.write_bytes(tsr)
    ots = mint_ots(digest)
    OTS_PATH.write_bytes(ots)
    print(f"Minted DigiCert RFC 3161 TSA token -> {TSR_PATH.relative_to(ROOT)} ({len(tsr)} bytes)")
    print(f"Minted Bitcoin OpenTimestamps proof -> {OTS_PATH.relative_to(ROOT)} ({len(ots)} bytes)")
    print(f"Bound SHA-256(data/MANIFEST.sha256) = {digest.hex()}")

    openssl = find_openssl()
    if openssl:
        proc = subprocess.run(
            [openssl, "ts", "-reply", "-in", str(TSR_PATH), "-text"],
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0:
            for ln in proc.stdout.splitlines():
                if any(k in ln for k in ("Status:", "Time stamp:", "Hash Algorithm:", "Message data:", "TSA:")):
                    print("  [openssl]", ln.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
