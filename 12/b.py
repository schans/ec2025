#!/usr/bin/env pypy3

import fileinput
from collections import deque

# counters
T = 0
G = []
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
S = (0, 0)

for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue
    G.append([int(x) for x in ll])

R = len(G)
C = len(G[0])

moved = True
seen = set()
q = deque([(0, 0), (R - 1, C - 1)])
while q:
    (rr, cc) = q.popleft()
    if (rr, cc) in seen:
        continue
    seen.add((rr, cc))
    T += 1

    for dr, dc in DIRS:
        nr, nc = rr + dr, cc + dc
        if not (0 <= nr < R and 0 <= nc < C and G[rr][cc] >= G[nr][nc]):
            continue
        q.append((nr, nc))


print(f"{T}")
