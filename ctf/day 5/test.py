import socket
HOST, PORT = "chatelaine.cylabacademy.net", 40748

s = socket.create_connection((HOST, PORT), timeout=10)
print("prompt:", s.recv(4096))
s.sendall(b"00" * 16 + b"\n")
print("answer:", s.recv(4096))
s.close()
