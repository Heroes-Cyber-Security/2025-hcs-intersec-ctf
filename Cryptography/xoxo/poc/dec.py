from Crypto.Util.strxor import strxor
from binascii import unhexlify

cipher_hex = "d61a7019ec6a5351aa2d120cf9065b52ec061211c12d1352c12e1056f5065b0de6365e"
cipher = unhexlify(cipher_hex)

known_prefix = b"HCS{"

key = strxor(cipher[:4], known_prefix)

expanded_key = (key * ((len(cipher) // len(key)) + 1))[:len(cipher)]

plaintext = strxor(cipher, expanded_key)
print("Recovered flag:", plaintext.decode())
