import string

LOWERCASE_OFFSET = ord("a")  # 97
ALPHABET = string.ascii_lowercase[:16]  # abcdefghijklmnop
plain = 'redacted'  # hcgfgegbgdhegfge
b16 = 'hcgfgegbgdhegfge'
enc = ''
key = 'redacted'
# for c in plain:
#     binary = "{0:08b}".format(ord(c))
#     print(f'1   {binary}')
#     enc += ALPHABET[int(binary[:4], 2)]
#     print(f'2   {enc}')
#     enc += ALPHABET[int(binary[4:], 2)]
#     print(f'3   {enc}')


# def shift(c, k):
#     t1 = ord(c) - LOWERCASE_OFFSET
#     print(f'       t1 - {t1}, ord(c) - {ord(c)}')
#     t2 = ord(k) - LOWERCASE_OFFSET
#     print(f'       t2 - {t2}, ord(k) - {ord(k)}')
#     print(f'       result - {ALPHABET[(t1 + t2) % len(ALPHABET)]}')
#     return ALPHABET[(t1 + t2) % len(ALPHABET)]
#
#
# key = 'redacted'
# for i, c in enumerate(b16):
#     print(f'{i}:    from b16: {c}, from key - {key[i % len(key)]}')
#     enc += shift(c, key[i % len(key)])
# print(enc)

# print([k in ALPHABET for k in key])
# print(all([k in ALPHABET for k in key]))