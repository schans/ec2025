#!/usr/bin/env pypy3

import fileinput

# counters
c = 0

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    lines.append(l)

n = lines[0].split(",")
N = len(n)

for m in lines[1].split(","):
    if m.startswith("L"):
        c = (-int(m[1:])) % N
    if m.startswith("R"):
        c = int(m[1:]) % N
    n[0], n[c] = n[c], n[0]

print(f"{n[0]}")
