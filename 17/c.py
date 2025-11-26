#!/usr/bin/env pypy3

import fileinput
from heapq import heapify, heappop, heappush

# counters
T = 0
G = []
L = 10
V = (0, 0)
S = (0, 0)
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # u, r, d, l

ll = ""
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue
    if "@" in ll:
        V = (len(G), ll.index("@"))
        ll = ll.replace("@", "0")
    if "S" in ll:
        S = (len(G), ll.index("S"))
        ll = ll.replace("S", "0")
    G.append([int(x) for x in ll])

R = len(G)
C = len(G[0])


def dijkstra(start, end, rad, wall):
    r2 = rad * rad
    pq = [(0, start)]
    heapify(pq)
    seen = set()

    while pq:
        d, (r, c) = heappop(pq)

        if (r, c) == end:
            return d, (r, c)

        if (r, c) in seen:
            continue
        seen.add((r, c))

        for dr, dc in DIRS:
            rr, cc = r + dr, c + dc
            if not (0 <= rr < R and 0 <= cc < C):
                continue

            # block left or right side
            if wall and rr == V[0] and cc > V[1]:
                continue
            if not wall and rr == V[0] and cc < V[1]:
                continue

            dd = d + G[rr][cc]
            x2 = pow(V[0] - rr, 2)
            y2 = pow(V[1] - cc, 2)
            if x2 + y2 > r2:
                heappush(pq, (dd, (rr, cc)))
    assert False


def get_half_ends(rad):
    return [(r, V[1]) for r in range(V[0] + rad, R)]


found = False
for rad in range(R // 5, R // 2):
    ends = get_half_ends(rad)
    for end in ends[:3]:
        left, hwp = dijkstra(S, end, rad - 1, True)
        right, _ = dijkstra(hwp, S, rad - 1, False)
        tot = left + right
        if tot < rad * 30:
            found = True
            T = tot * (rad - 1)
            break

    if found:
        break

print(f"{T}")
