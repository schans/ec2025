#!/usr/bin/env pypy3

import fileinput
from heapq import heapify, heappop, heappush

# counters
T = 0
X = set()
H = set()
E = (0, 0)
S = (0, 0)

r = 0
ll = ""
even_row = True
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    c = 0

    for ch in ll:
        rr = r
        if even_row:
            if c % 2 == 1:
                rr += 1
            if ch == "T":
                X.add((rr, c))
            if ch == "#":
                H.add((rr, c))
            if ch == "E":
                E = (rr, c)
            if ch == "S":
                S = (rr, c)
        else:
            if c % 2 == 0:
                rr += 1
            if ch == "T":
                X.add((rr, c))
            if ch == "#":
                H.add((rr, c))
            if ch == "E":
                E = (rr, c)
            if ch == "S":
                S = (rr, c)

        c += 1
    r += 2
    even_row = not even_row


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

        for dr, dc in [(-1, 0), (1, -1), (1, 1), (-1, -1), (-1, 1), (1, 0)]:
            rr, cc = r + dr, c + dc
            if (rr, cc) in X or (rr, cc) == end:
                heappush(pq, (d + 1, (rr, cc)))
    return -1


T = dijkstra(S, E)


print(f"{T}")
