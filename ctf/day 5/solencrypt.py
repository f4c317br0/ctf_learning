#!/usr/bin/env python3
import socket, random
from concurrent.futures import ThreadPoolExecutor
import time

def query(pt: bytes) -> int:
    last = None
    for _ in range(8):
        try:
            s = socket.create_connection((HOST, PORT), timeout=10)
            s.recv(4096)
            s.sendall(pt.hex().encode() + b"\n")
            data = b""
            while b"leakage result:" not in data or not data.endswith(b"\n"):
                chunk = s.recv(4096)
                if not chunk:
                    break
                data += chunk
            s.close()
            return int(data.split(b"leakage result:")[1].strip())
        except Exception as e:
            last = e
            time.sleep(0.5)
    raise RuntimeError(f"server unreachable: {last!r}")
HOST, PORT = "chatelaine.cylabacademy.net", 40748   # проверьте порт в вашем инстансе

# --- генерация стандартного AES S-box ---
def gen_sbox():
    rotl = lambda x, s: ((x << s) | (x >> (8 - s))) & 0xFF
    sbox = [0] * 256
    p = q = 1
    while True:
        p = p ^ ((p << 1) & 0xFF) ^ (0x1B if p & 0x80 else 0)
        q ^= q << 1; q ^= q << 2; q ^= q << 4; q &= 0xFF
        if q & 0x80:
            q ^= 0x09
        sbox[p] = q ^ rotl(q, 1) ^ rotl(q, 2) ^ rotl(q, 3) ^ rotl(q, 4) ^ 0x63
        if p == 1:
            break
    sbox[0] = 0x63
    return sbox

Sbox = gen_sbox()
assert Sbox[0] == 0x63 and Sbox[1] == 0x7C and Sbox[0x53] == 0xED

# --- один запрос = одно соединение ---
def query(pt: bytes) -> int:
    for _ in range(5):                      # повтор при сбое
        try:
            s = socket.create_connection((HOST, PORT), timeout=10)
            f = s.makefile("rwb")
            f.readline() if False else None
            s.recv(4096)                    # приглашение "Please provide..."
            s.sendall(pt.hex().encode() + b"\n")
            data = b""
            while b"leakage result:" not in data or not data.endswith(b"\n"):
                chunk = s.recv(4096)
                if not chunk:
                    break
                data += chunk
            s.close()
            return int(data.split(b"leakage result:")[1].strip())
        except Exception:
            continue
    raise RuntimeError("server unreachable")

N = 24
xs = random.sample(range(256), N)

def probe(args):
    i, x = args
    pt = bytearray(16)
    pt[i] = x
    return i, x, query(bytes(pt))

jobs = [(i, x) for i in range(16) for x in xs]
results = []
with ThreadPoolExecutor(max_workers=8) as ex:
    for n, r in enumerate(ex.map(probe, jobs), 1):
        results.append(r)
        if n % 50 == 0:
            print(f"{n}/{len(jobs)}", flush=True)

leaks = [{} for _ in range(16)]
for i, x, l in results:
    leaks[i][x] = l

key = []
for i in range(16):
    cands = [k for k in range(256)
             if len({leaks[i][x] - (Sbox[x ^ k] & 1) for x in xs}) == 1]
    print(f"byte {i}: {cands}")
    key.append(cands[0])

print("academy{" + bytes(key).hex() + "}")