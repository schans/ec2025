#!/usr/bin/env pypy3

import fileinput
from heapq import heapify, heappop, heappush

# counters
T = 0
G = set()

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # u, r, d, l
cur = 0
pos = (0, 0)

G.add(pos)

ll = ""
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

minr, maxr, minc, maxc = 0, 0, 0, 0
end = (0, 0)
for inst in ll.split(","):
    # turning
    if inst.startswith("R"):
        cur = (cur + 1) % 4
    else:
        cur = (cur - 1) % 4
    (dr, dc) = DIRS[cur]

    for _ in range(int(inst[1:])):
        (rr, cc) = pos
        pos = (rr + dr, cc + dc)
        G.add(pos)
        minr = min(minr, pos[0])
        minc = min(minc, pos[1])
        maxr = max(maxr, pos[0])
        maxc = max(maxc, pos[1])
        end = pos

G.remove(end)

# def pgrid():
#     print("-" * (maxr - minr))
#     for rr in range(minr, maxr + 1):
#         for cc in range(minc, maxc + 1):
#             if (rr, cc) == (0, 0):
#                 print("S", end="")
#             elif (rr, cc) == end:
#                 print("E", end="")
#             elif (rr, cc) in G:
#                 print("#", end="")
#             else:
#                 print(" ", end="")
#         print()
#     print("-" * (maxr - minr))
#
#
# pgrid()


def dijkstra(start, end):
    pq = [(0, start)]
    heapify(pq)
    seen = set()

    while pq:
        (d, p) = heappop(pq)

        if p == end:
            return d
        if p in seen:
            continue
        seen.add(p)

        (r, c) = p
        for dr, dc in DIRS:
            rr, cc = r + dr, c + dc
            if minr <= rr <= maxr and minc <= cc <= maxc and (rr, cc) not in G:
                heappush(pq, (d + 1, (rr, cc)))

    return -1


T = dijkstra((0, 0), end)

print(f"{T}")
