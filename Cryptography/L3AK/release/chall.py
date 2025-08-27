from Crypto.Util.number import *
with open('flag.txt') as f:
    flag = f.read().strip()

p = getPrime(512)
q = getPrime(512)
n = p * q
phi = (p - 1) * (q - 1)

e = 65537
d = inverse(e, phi)
what = d % (p - 1)

ct = pow(bytes_to_long(flag.encode()), e, n)
with open('output.txt', 'w') as f:
    f.write(f'n = {n}\n')
    f.write(f'ct = {ct}\n')
    f.write(f'what = {what}\n')