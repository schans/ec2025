#!/usr/bin/env pypy3

import fileinput

# counters
D = set()
S = set()
H = set()

N = 20
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
        elif x == "#":
            H.add((r, c))
    r += 1

R = r - 1
C = len(l)

eaten = 0
for _ in range(N):
    safe = 0
    DN = set()
    SN = set()

    # dragon move
    for rr, cc in D:
        for dr, dc in DIRS:
            nd = (rr + dr, cc + dc)
            DN.add(nd)

    # eat
    cur = len(S)
    DA = DN - H
    S = S - DA

    # sheep move
    for rr, cc in S:
        if rr > R - 1:
            safe += 1
        else:
            SN.add((rr + 1, cc))

    # eat
    S = SN - DA
    D = DN
    eaten += cur - len(S) - safe


print(f"{eaten}")
