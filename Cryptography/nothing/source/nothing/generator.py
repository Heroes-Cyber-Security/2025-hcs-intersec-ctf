SBox = dict()

for ch in range(1, 256):
	SBox[ch] = ' ' * (ch-1) + '\t'

def subtitute(p):
	return ''.join(SBox[ord(ch)] for ch in p)

flag = "HCS{sbox_is_very_cool__ayaya}"
flag = subtitute(flag)

print(f"{SBox = }")
print(f"""
{flag = }

def decrypt():
	...
	print(flag)

decrypt()
""")
