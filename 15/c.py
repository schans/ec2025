#!/usr/bin/env pypy3

import fileinput
from heapq import heapify, heappop, heappush
from collections import deque

# counters
T = 0
G = set()
S = set()

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

    len = int(inst[1:])

    (rr, cc) = pos
    pos = (rr + dr * len, cc + dc * len)
    G.add(pos)
    S.add((rr, cc, *pos))

    minr = min(minr, pos[0])
    minc = min(minc, pos[1])
    maxr = max(maxr, pos[0])
    maxc = max(maxc, pos[1])
    end = pos


def on_seg(rr, cc):
    if (rr, cc) == end:
        return False
    for r1, c1, r2, c2 in S:
        if r1 == r2 == rr:
            if min(c1, c2) <= cc <= max(c1, c2):
                return True
        elif c1 == c2 == cc:
            if min(r1, r2) <= rr <= max(r1, r2):
                return True

    return False


def dir_opts(rr, cc, dr, dc):
    if not (minr <= rr + dr <= maxr and minc <= cc + dc <= maxc):
        return []

    if on_seg(rr + dr, cc + dc):
        return []

    if (rr + dr, cc + dc) == end:
        return [1]

    if dr > 0:
        ds = set()
        maxd = maxr - rr
        for r1, c1, r2, c2 in S:
            if r1 >= rr:
                ds.add(abs(r1 - rr) - 1)
                ds.add(abs(r1 - rr) + 1)
            if r2 >= rr:
                ds.add(abs(r2 - rr) - 1)
                ds.add(abs(r2 - rr) + 1)

            if r1 == r2 and min(c1, c2) <= cc <= max(c1, c2) and r1 > rr:
                maxd = min(maxd, abs(r1 - rr) - 1)
            if c1 == c2 == cc and rr < min(r1, r2):
                maxd = min(maxd, abs(min(r1, r2) - rr) - 1)

        ds.add(maxd)
        ds = sorted([x for x in ds if x <= maxd and x > 0], reverse=True)
        if ds:
            return ds
        else:
            assert False

    if dr < 0:
        ds = set()
        maxd = rr - minr
        for r1, c1, r2, c2 in S:
            if r1 <= rr:
                ds.add(abs(r1 - rr) - 1)
                ds.add(abs(r1 - rr) + 1)
            if r2 <= rr:
                ds.add(abs(r2 - rr) - 1)
                ds.add(abs(r2 - rr) + 1)

            if r1 == r2 and min(c1, c2) <= cc <= max(c1, c2) and r1 < rr:
                maxd = min(maxd, abs(r1 - rr) - 1)
            if c1 == c2 == cc and rr > max(r1, r2):
                maxd = min(maxd, abs(max(r1, r2) - rr) - 1)

        ds.add(maxd)
        ds = sorted([x for x in ds if x <= maxd and x > 0], reverse=True)
        if ds:
            return ds
        else:
            assert False

    if dc > 0:
        ds = set()
        maxd = maxc - cc
        for r1, c1, r2, c2 in S:
            if c1 >= cc:
                ds.add(abs(c1 - cc) - 1)
                ds.add(abs(c1 - cc) + 1)
            if c2 >= cc:
                ds.add(abs(c2 - cc) - 1)
                ds.add(abs(c2 - cc) + 1)

            if c1 == c2 and min(r1, r2) <= rr <= max(r1, r2) and c1 > cc:
                maxd = min(maxd, abs(c1 - cc) - 1)
            if r1 == r2 == rr and cc < min(c1, c2):
                maxd = min(maxd, abs(min(c1, c2) - cc) - 1)

        ds.add(maxd)
        ds = sorted([x for x in ds if x <= maxd and x > 0], reverse=True)
        if ds:
            return ds
        else:
            assert False

    if dc < 0:
        ds = set()
        maxd = cc - minc
        for r1, c1, r2, c2 in S:
            if c1 <= cc:
                ds.add(abs(c1 - cc) - 1)
                ds.add(abs(c1 - cc) + 1)
            if c2 <= cc:
                ds.add(abs(c2 - cc) - 1)
                ds.add(abs(c2 - cc) + 1)

            if c1 == c2 and min(r1, r2) <= rr <= max(r1, r2) and c1 < cc:
                maxd = min(maxd, abs(c1 - cc) - 1)
            if r1 == r2 == rr and cc > max(c1, c2):
                maxd = min(maxd, abs(max(c1, c2) - cc) - 1)

        ds.add(maxd)
        ds = sorted([x for x in ds if x <= maxd and x > 0], reverse=True)
        if ds:
            return ds
        else:
            assert False
    return [1]


# def pgrid():
#     print("-" * (maxr - minr))
#     for rr in range(minr, maxr + 1):
#         for cc in range(minc, maxc + 1):
#             if (rr, cc) == (0, 0):
#                 print("S", end="")
#             elif (rr, cc) == end:
#                 print("E", end="")
#             elif on_seg(rr, cc):
#                 print("#", end="")
#             else:
#                 print(" ", end="")
#         print()
#     print("-" * (maxr - minr))
#
#
# pgrid()


def dijkstra(start, end):
    pq = [(0, start, (0, 0))]
    heapify(pq)
    seen = set()

    while pq:
        (d, (r, c), pdir) = heappop(pq)

        if (r, c) == end:
            return d

        # don't hop across from corners
        for dr, dc in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
            if (r + dr, c + dc) == end:
                return d + 2

        if (r, c) in seen:
            continue
        seen.add((r, c))

        for dr, dc in DIRS:
            if (dr * -1, dc * -1) != pdir:
                dds = dir_opts(r, c, dr, dc)
                for dd in dds:
                    heappush(pq, (d + dd, (r + dd * dr, c + dd * dc), (dr, dc)))
    return -1


T = dijkstra((0, 0), end)

print(f"{T}")
