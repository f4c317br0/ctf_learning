import hashlib

username_trial = b"MILLER"

prefix = "academy{1n_7h3_kk3y_of_"
suffix = "}"

digest = hashlib.sha256(username_trial).hexdigest()
indexes = [4, 5, 3, 6, 2, 7, 1, 8]

dynamic_part = "".join(digest[i] for i in indexes)
key = prefix + dynamic_part + suffix

print("SHA-256:", digest)
print("Динамическая часть:", dynamic_part)
print("Ключ:", key)