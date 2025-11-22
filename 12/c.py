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


def solve(starts, seen):
    t = 0
    q = deque(starts)
    while q:
        (rr, cc) = q.popleft()
        if (rr, cc) in seen:
            continue
        seen.add((rr, cc))
        t += 1

        for dr, dc in DIRS:
            nr, nc = rr + dr, cc + dc
            if not (0 <= nr < R and 0 <= nc < C and G[rr][cc] >= G[nr][nc]):
                continue
            q.append((nr, nc))
    return t, seen


best = 0
best_seen = set()
best_point = (-1, -1)
all_seen = set()
all_bests = set()
for _ in range(3):
    best = 0
    for r in range(R):
        for c in range(C):
            if (r, c) in all_seen:
                continue
            t, seen = solve([(r, c)], all_seen.copy())

            if t > best:
                best = t
                best_seen = seen.copy()
                best_point = (r, c)

    all_seen |= best_seen
    all_bests.add(best_point)

print(f"{len(all_seen)}")
