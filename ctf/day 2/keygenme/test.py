import hashlib

username = b"MILLER"

digest = hashlib.sha256(username).hexdigest()

print("Хеш:", digest)
print("Символы с индексами:")

for i, char in enumerate(digest[:9]):
    print(i, char)