#!/usr/bin/env python3

import argparse

def xor_bytes(plaintext: bytes, key: bytes) -> bytes:
  out = bytearray(len(plaintext))
  for i, b in enumerate(plaintext):
    out[i] = b ^ key[i % len(key)]
  return bytes(out)

def format_chr_inline(b: bytes) -> str:
  return " + ".join(f"chr(0x{byte:02x})" for byte in b)

def format_chr_multiline(b: bytes, width=8) -> str:
  parts = [" + ".join(f"chr(0x{byte:02x})" for byte in b[i:i+width]) for i in range(0, len(b), width)]
  joined = " +\n  ".join(parts)
  return f"(\n  {joined}\n)"

def format_bytes_literal(b: bytes) -> str:
  return "b'" + "".join(f"\\x{byte:02x}" for byte in b) + "'"

def main():
  p = argparse.ArgumentParser()
  p.add_argument("-f", "--flag", required=True)
  p.add_argument("-k", "--key", required=True)
  p.add_argument("--multiline", action="store_true")
  p.add_argument("--bytes-literal", action="store_true")
  p.add_argument("--width", type=int, default=8)
  args = p.parse_args()

  flag_bytes = args.flag.encode("utf-8")
  key_bytes = args.key.encode("utf-8")
  encrypted = xor_bytes(flag_bytes, key_bytes)

  if args.multiline:
    encoded = format_chr_multiline(encrypted, width=args.width)
  else:
    encoded = format_chr_inline(encrypted)

  print("flag_enc = " + encoded + "\n")

  if args.bytes_literal:
    print("flag_enc_bytes = " + format_bytes_literal(encrypted) + "\n")

  print(f"# original flag: {args.flag!r}")
  print(f"# decode with same key '{args.key}':")
  print("".join(["# ", args.flag]))
  print()

if __name__ == "__main__":
  main()
