import string

LOWERCASE_OFFSET = ord("a") # 97
ALPHABET = string.ascii_lowercase[:] # abcdefghijklmnop

def b16_encode(plain): # буква каждая в бинарную хрень, потом левая половина в десятичную и из алфавита по индексу, потом тоже самое, но справа
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc # новый текст для redacted - hcgfgegbgdhegfge

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "cbdabldadbplblcnpfpnpapapecpcn"
key = "redacted"
assert all([k in ALPHABET for k in key]), 'не все буквы из ключа не в алфавите' # если не все буквы из ключа не в алфавите, то капут
assert len(key) == 1, 'длина ключа равна 1' # если длина ключа равна 1, то капут

b16 = b16_encode(flag) # новый текст для redacted - hcgfgegbgdhegfge
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)
