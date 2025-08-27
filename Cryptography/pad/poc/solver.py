# eter
from pwn import *
from binascii import hexlify, unhexlify

hostport = 'nc localhost 50005'
HOST = hostport.split()[1]
PORT = int(hostport.split()[2])

BLOCK_SIZE = 16
MIN_SAMPLES = 7
MAX_SAMPLES = 35
PRIORITY_BYTES = list(b'0123456789abcdef') + [b for b in range(256) if b not in b'0123456789abcdef']

def menu_encrypt(r):
    r.sendlineafter(b"Choice: ", b"1")
    line = r.recvline_regex(br'^ct = [0-9a-fA-F]+\s*$', timeout=5)
    ct_hex = line.strip().split(b"=", 1)[1].strip()
    return ct_hex.decode()

def menu_unpad(r, ct_hex: str) -> int:
    r.sendlineafter(b"Choice: ", b"2")
    r.sendlineafter(b"ct = ", ct_hex.encode())
    line = r.recvline_regex(br'^pad = [01]\s*$', timeout=5)
    return int(line.strip().split(b"=", 1)[1].strip())

def menu_check(r, msg_ascii: str):
    r.sendlineafter(b"Choice: ", b"3")
    r.sendlineafter(b"msg = ", msg_ascii.encode())
    line = r.recvline(timeout=5)
    return line.decode(errors="ignore").strip()

def candidate_valid_majority(r, ct_hex):
    """
    Query the padding oracle up to MAX_SAMPLES times for the given ciphertext.
    The challenge returns pad = 1 when (noisy result) is True, and 0 otherwise.
    In the server, valid padding is flipped to False ~75% of the time, so we detect
    validity by counting how many times we see pad == 0.
    """
    false_count = 0
    total = 0
    needed = (MAX_SAMPLES // 2) + 1  # majority threshold

    while total < MAX_SAMPLES:
        res = menu_unpad(r, ct_hex)
        if res == 0:
            false_count += 1
        total += 1

        # early accept/reject once majority decision is certain and we met MIN_SAMPLES
        if total >= MIN_SAMPLES:
            if false_count >= needed:
                return True
            if (false_count + (MAX_SAMPLES - total)) < needed:
                return False

    return false_count > (total // 2)

def noisy_oracle(r, candidate_ct_bytes):
    return candidate_valid_majority(r, hexlify(candidate_ct_bytes).decode())

def decrypt_block(r, prev_block, current_block):
    I = bytearray(BLOCK_SIZE)
    P = bytearray(BLOCK_SIZE)

    log.info(f"Decrypting block: {hexlify(current_block).decode()}")

    for i in range(BLOCK_SIZE - 1, -1, -1):
        pad = BLOCK_SIZE - i
        suffix = bytearray()
        for j in range(i + 1, BLOCK_SIZE):
            suffix.append(pad ^ I[j])

        found = False
        for cand in PRIORITY_BYTES:
            g = cand if isinstance(cand, int) else (cand[0] if isinstance(cand, (bytes, bytearray)) else int(cand))
            crafted_i = pad ^ (g ^ prev_block[i])
            test_prev = bytearray(b'\x00' * i) + bytes([crafted_i]) + suffix
            candidate_ct = bytes(test_prev) + current_block

            if noisy_oracle(r, candidate_ct):
                I[i] = g ^ prev_block[i]
                P[i] = I[i] ^ prev_block[i]
                log.info(f"i={i:02d} found byte 0x{P[i]:02x}  tail(hex)={(P[i:]).hex()}")
                found = True
                break

        if not found:
            log.warning(f"Byte i={i} not in priority set, brute-forcing 0..255")
            for test_val in range(256):
                crafted_i = test_val
                test_prev = bytearray(b'\x00' * i) + bytes([crafted_i]) + suffix
                candidate_ct = bytes(test_prev) + current_block

                if noisy_oracle(r, candidate_ct):
                    interm = pad ^ crafted_i
                    I[i] = interm
                    P[i] = I[i] ^ prev_block[i]
                    log.info(f"i={i:02d} brute found 0x{P[i]:02x}")
                    found = True
                    break

        if not found:
            log.error(f"Failed to recover byte at index {i}. Aborting.")
            raise SystemExit(1)

    log.success(f"Block decrypted (hex): {P.hex()}")
    return bytes(P)

def main():
    r = remote(HOST, PORT)

    ct_hex = menu_encrypt(r)
    ct = unhexlify(ct_hex)

    iv = ct[:BLOCK_SIZE]
    c1 = ct[BLOCK_SIZE:2*BLOCK_SIZE]
    c2 = ct[2*BLOCK_SIZE:3*BLOCK_SIZE]

    log.info(f"IV: {hexlify(iv).decode()}")
    log.info(f"C1: {hexlify(c1).decode()}")
    log.info(f"C2: {hexlify(c2).decode()}")

    p2 = decrypt_block(r, prev_block=c1, current_block=c2)
    p1 = decrypt_block(r, prev_block=iv, current_block=c1)

    recovered = p1 + p2
    try:
        recovered_str = recovered.decode('ascii')
        log.success(f"ascii: {recovered_str}")
    except UnicodeDecodeError:
        recovered_str = recovered.decode('ascii', errors='ignore')
        log.success(f"hex: {recovered.hex()}  (ascii best-effort: {recovered_str})")

    res = menu_check(r, recovered_str)
    log.success(res)
    r.interactive()

if __name__ == '__main__':
    main()
