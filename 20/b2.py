#!/usr/bin/env pypy3

import fileinput
from heapq import heapify, heappop, heappush

# counters
T = 0
X = set()
S, E = (-1, -1), (-1, -1)

r = 0
ll = ""
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    c = 0
    for ch in ll:
        if ch == ".":
            continue
        if ch == "T":
            X.add((r, c))
        elif ch == "S":
            S = (r, c)
        elif ch == "E":
            E = (r, c)

        c += 1
    r += 1


def dijkstra(start, end):
    pq = [(0, start)]
    heapify(pq)
    seen = set()

    while pq:
        d, (r, c) = heappop(pq)

        if (r, c) == end:
            return d

        if (r, c) in seen:
            continue
        seen.add((r, c))

        HDIRS = {(0, -1), (0, 1)}
        dirs = HDIRS
        if c % 2 == 0:
            dirs.add((-1, 1))
        else:
            dirs.add((1, -1))

        for dr, dc in dirs:
            rr, cc = r + dr, c + dc
            if (rr, cc) in X or (rr, cc) == end:
                heappush(pq, (d + 1, (rr, cc)))
    return -1


T = dijkstra(S, E)

print(f"{T}")
