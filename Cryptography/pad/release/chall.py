from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from os import urandom
from random import SystemRandom

with open("flag.txt", "r") as f:
    FLAG = f.read().strip()

rng = SystemRandom()

class Challenge:
    def __init__(self):
        self.msg = urandom(16).hex()
        self.key = urandom(16)
        self.q = 0
        self.L = 15000

    def inc(self):
        self.q += 1
        return self.q >= self.L

    def encrypt(self):
        iv = urandom(16)
        c  = AES.new(self.key, AES.MODE_CBC, iv=iv).encrypt(self.msg.encode("ascii"))
        return (iv + c).hex()

    def unpad_oracle(self, xhex: str):
        try:
            if len(xhex) % 2 != 0:
                return 0
            b = bytes.fromhex(xhex)
            if len(b) < 32 or len(b) % 16 != 0:
                return 0
            iv, ct = b[:16], b[16:]
            pt = AES.new(self.key, AES.MODE_CBC, iv=iv).decrypt(ct)
            try:
                unpad(pt, 16)
                good = True
            except ValueError:
                good = False
            noisy = good ^ (rng.random() > 0.2)
            return 1 if noisy else 0
        except Exception:
            return 0

    def check(self, s: str):
        return s == self.msg

def main():
    ch = Challenge()
    while True:
        if ch.q >= ch.L:
            print("bye :(")
            break
        print("\n:3\n")
        print("1 - Encrypt fresh IV-CT for the secret message")
        print("2 - Padding check for supplied (IV-CT) hex")
        print("3 - Submit recovered message")
        print("4 - Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            ct = ch.encrypt()
            quit_now = ch.inc()
            print(f"ct = {ct}")
            if quit_now:
                print("bye :(")
                break

        elif choice == "2":
            x = input("ct = ").strip()
            r = ch.unpad_oracle(x)
            quit_now = ch.inc()
            print(f"pad = {r}")
            if quit_now:
                print("bye :(")
                break

        elif choice == "3":
            m = input("msg = ").strip()
            quit_now = ch.inc()
            if ch.check(m):
                print(f"flag = {FLAG}")
            else:
                print("whuh")
            if quit_now:
                print("bye :(")
                break

        elif choice == "4":
            print("bye :(")
            break

        else:
            print("what")

if __name__ == "__main__":
    main()
