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
        c = (c - int(m[1:])) % N
    if m.startswith("R"):
        c = (c + int(m[1:])) % N

print(f"{n[c]}")
