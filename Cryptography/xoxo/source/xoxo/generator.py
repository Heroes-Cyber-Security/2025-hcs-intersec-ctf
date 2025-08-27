import os
from Crypto.Util.number import long_to_bytes
from Crypto.Util.strxor import strxor

FLAG = "HCS{r3p34t1ng_x0r_1s_t00_w34k_xoxo}"

key = bytes.fromhex("9e592362") * 9

flag_bytes = FLAG.encode()

c = strxor(flag_bytes, key[:len(flag_bytes)])
print(c.hex())


