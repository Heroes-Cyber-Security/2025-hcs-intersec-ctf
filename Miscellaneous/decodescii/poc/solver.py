#!/usr/bin/env python3
from pwn import *
import re
import base64
import subprocess

HOST = "localhost"
PORT = 7003
CHALL_FILE = "chall.dots"

# answers we already know
STEP1_ANSWER = "1312"
STEP2_ANSWER = "https://files.catbox.moe/fmg01x.webp"


def fetch_payload_and_write(challenge_text):
    # extract b'...' literal
    m = re.search(r"b'(.*)'", challenge_text, re.DOTALL)
    if not m:
        print("[!] Failed to extract payload")
        return False
    payload = m.group(1)

    # handle escaped bytes
    payload = payload.encode()

    # base64 decode
    code = base64.b64decode(payload).decode().split("code=")[-1]
    dots_bytes = base64.b64decode(code + "=" * (4 - len(code) % 4), altchars="-_")
    with open(CHALL_FILE, "wb") as f:
        f.write(dots_bytes)
    print(f"[+] Wrote AsciiDots program to {CHALL_FILE}")
    return True


def run_asciidots(val: int) -> str:
    proc = subprocess.run(
        ["asciidots", CHALL_FILE],
        input=f"{val}\n",
        capture_output=True,
        text=True,
    )
    return proc.stdout + proc.stderr


def is_success(output: str) -> bool:
    out = output.lower()
    return "berhasil" in out or "success" in out or "correct" in out


def find_minimum(low: int, high: int) -> int:
    ans = None
    while low < high:
        mid = (low + high) // 2
        out = run_asciidots(mid)
        if is_success(out):
            ans = mid
            high = mid
        else:
            low = mid + 1
        print(f"[+] Tried {ans}")
    return ans


def main():
    conn = remote(HOST, PORT)

    # receive initial text until step 1 prompt
    data = conn.recvuntil(b"1. THE WEIRD STRING...")
    print(data.decode())

    # send step 1 answer
    conn.sendline(STEP1_ANSWER)
    print(f"[+] Sent step 1 answer: {STEP1_ANSWER}")
    conn.recvuntil(b"2. Asset?")

    # send step 2 answer
    conn.recvuntil(b"Answer:")
    conn.sendline(STEP2_ANSWER)
    print(f"[+] Sent step 2 answer: {STEP2_ANSWER}")
    step3_text = conn.recvuntil(b"Answer:").decode()
    print("[+] Received step 3 payload")

    # decode & write .dots
    fetch_payload_and_write(step3_text)

    # find smallest working input
    upper_bound = 10**18
    smallest = find_minimum(0, upper_bound)
    print(f"[+] Smallest input found: {smallest}")

    # send final answer
    conn.sendline(str(smallest))
    final_output = conn.recvall(timeout=5).decode()
    print("[+] Final response / flag:\n", final_output)


if __name__ == "__main__":
    main()
