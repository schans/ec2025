#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
G = []
DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
N = 2025

for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    G.append(ll)

R = len(G)
C = len(G[0])

for _ in range(N):
    NG = []
    cnt = 0
    for rr in range(R):
        nextr = []
        for cc in range(C):
            odd = False
            for dr, dc in DIRS:
                nr, nc = rr + dr, cc + dc
                if 0 <= nr < R and 0 <= nc < C and G[nr][nc] == "#":
                    odd = not odd

            if G[rr][cc] == "#":
                if odd:
                    cnt += 1
                    nextr.append("#")
                else:
                    nextr.append(".")
            elif G[rr][cc] == ".":
                if odd:
                    nextr.append(".")
                else:
                    cnt += 1
                    nextr.append("#")
        NG.append(nextr)
    T += cnt
    G = NG

print(f"{T}")
