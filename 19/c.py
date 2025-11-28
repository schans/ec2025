#!/usr/bin/env pypy3

import fileinput
from heapq import heapify, heappop, heappush

# counters
T = 0
G = []
GS = set()
S = (0, 0)
ll = ""
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue
    G.append([int(x) for x in ll.split(",")])
    GS.add(G[-1][0])

# pre calc wall list
GL = list()
for i, c in enumerate(GS):
    GL.append(list())
    for j, g in enumerate(G):
        if g[0] == c:
            GL[i].append(j)


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
    pq = [(0, start, 0)]
    heapify(pq)
    seen = set()

    while pq:
        d, (r, c), i = heappop(pq)

        if c == end[0]:
            # pgrid(40, c, path)
            return d

        if (r, c) in seen:
            continue
        seen.add((r, c))

        ni = i + 1
        for gi in GL[i]:
            g = G[gi]
            dc = g[0] - c
            cc = g[0]
            maxdr = dc
            even = dc % 2 == 0
            for rr in range(g[1], g[1] + g[2]):
                if not (r - maxdr <= rr <= r + maxdr):
                    continue
                dr = rr - r
                if (dr % 2 == 0 and even) or (dr % 2 != 0 and not even):
                    dd = (dr + dc) // 2
                    nd = max(0, dd) + d
                    heappush(pq, (nd, (rr, cc), ni))
    return -1


T = dijkstra(S, G[-1])
print(f"{T}")
