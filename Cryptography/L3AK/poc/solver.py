# eter
from Crypto.Util.number import *
from sympy import gcd
import random

def solve(n, e, dp):
    r = random.randint(2, n-1)
    u = pow(r, e*dp, n)
    g = gcd(n, (u-r) % n)
    if 1 < g < n:
        p = g
        q = n // p
        if p * q == n:
            return p, q

def main():
    with open('output.txt', 'r') as f:
        n = int(f.readline().strip().split(' = ')[1])
        ct = int(f.readline().strip().split(' = ')[1])
        leak = int(f.readline().strip().split(' = ')[1])

    p, q = solve(n, 65537, leak)
    # print(p, q)
    phi = (p-1) * (q-1)
    d = inverse(65537, int(phi))
    pt = long_to_bytes(pow(ct, d, n))
    print(pt)

if __name__ == '__main__':
    main()