from Crypto.Util.number import *

p = getStrongPrime(1024)
q = p
e = 0x10001
N = p*q

phi = (p-1)*q
d = pow(e, -1, phi)

flag = b"HCS{this_math_thing_is_confusing__ayaya}"
flag = bytes_to_long(flag)
ct = pow(flag, e, N)

print(f"""
p = getStrongPrime(1024)
q = p # it doesnt really matter, just random number

e = 0x10001
{N = }

phi = (p-1)*q
{ct = }
""")
