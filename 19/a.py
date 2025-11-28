#!/usr/bin/env pypy3

import fileinput
from heapq import heapify, heappop, heappush

# counters
T = 0
G = []
S = (0, 0)
ll = ""
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue
    G.append([int(x) for x in ll.split(",")])


# def pgrid(maxr, maxc, path):
#     for r in range(maxr + 1):
#         for cc in range(maxc + 1):
#             rr = maxr - r
#             if (rr, cc) == (0, 0):
#                 print("S", end="")
#                 continue
#             if (rr, cc) in path:
#                 print("*", end="")
#                 continue
#
#             opening = False
#             wall = False
#             for g in G:
#                 if cc == g[0]:
#                     wall = True
#
#                     if g[1] <= rr <= g[1] + g[2]:
#                         opening = True
#             if wall and not opening:
#                 print("#", end="")
#             else:
#                 print(".", end="")
#         print()


def dijkstra(start, end):
    pq = [(0, start, list())]
    heapify(pq)
    seen = set()

    while pq:
        d, (r, c), path = heappop(pq)

        if c == end[0] and end[1] <= r <= end[1] + end[2]:
            # pgrid(40, c, path)
            return d

        if (r, c) in seen:
            continue
        seen.add((r, c))

        # don't hop across from corners
        for dr, dc in [(1, 1), (-1, 1)]:
            rr, cc = r + dr, c + dc

            if rr < 1:
                continue
            if cc > end[0]:
                continue

            opening = False
            wall = False
            for g in G:
                if cc == g[0]:
                    wall = True

                    if g[1] <= rr <= g[1] + g[2]:
                        opening = True
            if wall and not opening:
                continue

            dd = d
            if dr == 1:
                dd += 1

            dpath = path.copy()
            dpath.append((rr, cc))
            heappush(pq, (dd, (rr, cc), dpath))
    return -1


T = dijkstra(S, G[-1])
print(f"{T}")
