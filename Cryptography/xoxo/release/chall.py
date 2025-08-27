import os
from Crypto.Util.number import long_to_bytes
from Crypto.Util.strxor import strxor

FLAG = "HCS{placeholder}"

key = os.urandom(4) * 9

flag_bytes = FLAG.encode()

c = strxor(flag_bytes, key[:len(flag_bytes)])
print(c.hex())
# d61a7019ec6a5351aa2d120cf9065b52ec061211c12d1352c12e1056f5065b0de6365e


