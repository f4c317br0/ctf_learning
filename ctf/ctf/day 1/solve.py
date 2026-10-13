import base64
from cryptography.fernet import Fernet

with open("pass.txt", "r") as f:
    password = f.read().strip()

key = base64.urlsafe_b64encode(password.encode())
cipher = Fernet(key)

with open("flag.txt.en", "rb") as f:
    encrypted = f.read().strip()

print(cipher.decrypt(encrypted).decode())
