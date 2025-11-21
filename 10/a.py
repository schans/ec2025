#!/usr/bin/env pypy3

import fileinput

# counters
D = set()
S = set()
N = 4
DIRS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
r = 0
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    for c, x in enumerate(l):
        if x == "D":
            D.add((r, c))
        elif x == "S":
            S.add((r, c))
    r += 1


for _ in range(N):
    DN = set()
    for rr, cc in D:
        DN.add((rr, cc))
        for dr, dc in DIRS:
            nd = (rr + dr, cc + dc)
            DN.add(nd)
    D = DN


print(f"{len(D & S)}")
