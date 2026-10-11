import hashlib


def str_xor(secret, key):
    new_key = key
    i = 0

    while len(new_key) < len(secret):
        new_key += key[i]
        i = (i + 1) % len(key)

    return "".join(
        chr(ord(a) ^ ord(b))
        for a, b in zip(secret, new_key)
    )


flag_enc = open("level5.flag.txt.enc", "rb").read()
correct_pw_hash = open("level5.hash.bin", "rb").read()


def hash_pw(pw_str):
    return hashlib.md5(pw_str.encode()).digest()


def level_5_pw_check(password):
    if hash_pw(password) == correct_pw_hash:
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), password)
        print(decryption)
        return True

    return False


def brutforce():
    with open("dictionary.txt", "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            password = line.strip()

            if not password:
                continue

            if level_5_pw_check(password):
                print("\n" + "=" * 40)
                print(f"[+] ПАРОЛЬ НАЙДЕН: {password}")
                print("=" * 40)
                return

    print("Пароль не найден в словаре.")


brutforce()
