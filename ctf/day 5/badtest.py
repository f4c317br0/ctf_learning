import socket

HOST, PORT = "chatelaine.cylabacademy.net", 39951
s = socket.create_connection((HOST, PORT), timeout=10)
prompt = s.recv(4096)
print("PROMPT:", prompt)
s.sendall(b"00" * 16 + b"\n")
response = b""
s.settimeout(3)
try:
    while True:
        chunk = s.recv(65536)
        if not chunk:
            break
        response += chunk
except socket.timeout:
    pass

s.close()
print("RESPONSE LENGTH:", len(response))
print("RESPONSE:", response[:2000])
