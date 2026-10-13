import string

ALPHABET = string.ascii_lowercase[:16]
ciphertext = "cbdabldadbplblcnpfpnpapapecpcn"


def b16_decode(text):
    result = ""

    for i in range(0, len(text), 2):
        high = ALPHABET.index(text[i])
        low = ALPHABET.index(text[i + 1])

        char_code = high * 16 + low
        result += chr(char_code)

    return result


for key in ALPHABET:
    shifted = ""

    for c in ciphertext:
        position = ALPHABET.index(c)
        key_position = ALPHABET.index(key)

        new_position = (position - key_position) % 16
        shifted += ALPHABET[new_position]

    result = b16_decode(shifted)
    print(f"Ключ {key}: {result}")
