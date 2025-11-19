#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
N = 256

nails = list()
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    nails = [int(x) for x in l.split(",")]


def cross(l1, l2):
    a, b = min(l1), max(l1)
    x, y = min(l2), max(l2)
    if a < x < b and y > b:
        return True
    if a < y < b and x < a:
        return True
    if a == x and b == y:
        return True
    return False


placed = set()
for i in range(0, len(nails) - 1):
    cur = (nails[i], nails[i + 1])
    placed.add(cur)

for i in range(1, N):
    for j in range(i + 1, N + 1):
        c = 0
        for p in placed:
            if cross((i, j), p):
                c += 1
        T = max(c, T)

print(f"{T}")
