# Reverse Day 1 - Proof of Concept

## Challenge Description

Participants need to analyze a C binary to extract the hidden flag.

## Solution Steps

### 1. Initial Analysis

First, try using `strings` on the binary:
```bash
strings chall
```

This will show a fake flag: `HCS{faaakeeeflaaaaaaag}` which is intentionally misleading.

### 2. Static Analysis

Analyze the binary using a disassembler or decompiler (like Ghidra, IDA, or radare2) to understand the program flow:

- Function `a()` returns the length of the fake flag (23 characters)
- Function `check()` contains the real flag validation logic
- The real flag is stored as XOR-encrypted bytes

### 3. Key Findings

In the `check()` function:
- Array `enc[]` contains encrypted bytes of the real flag
- XOR key is `0x5E` (ASCII '^')
- The flag is decrypted by XORing each byte with the key

### 4. Decryption

The encrypted bytes are:
```
0x16, 0x1D, 0x0D, 0x25, 0x2C, 0x3B, 0x28, 0x3B, 
0x2C, 0x2D, 0x3B, 0x01, 0x37, 0x2D, 0x01, 0x3B,
0x3F, 0x24, 0x27, 0x27, 0x27, 0x27, 0x23
```

XOR each byte with `0x5E` to get the flag:
```python
enc = [0x16, 0x1D, 0x0D, 0x25, 0x2C, 0x3B, 0x28, 0x3B, 0x2C, 0x2D, 0x3B, 0x01, 0x37, 0x2D, 0x01, 0x3B, 0x3F, 0x24, 0x27, 0x27, 0x27, 0x27, 0x23]
key = 0x5E
flag = ''.join(chr(byte ^ key) for byte in enc)
print(flag)
```

### 5. Verification

Run the binary with the discovered flag:
```bash
./chall "HCS{reverse_is_eazyyyy}"
```

Output should be: `GG!, dont forget to submit your flag!`

## Flag

`HCS{reverse_is_eazyyyy}`
