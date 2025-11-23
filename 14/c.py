#!/usr/bin/env pypy3

import fileinput
from os import pathconf_names

# counters
T = 0
SG = []
DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
N = 1_000_000_000
R, C = 34, 34

for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    SG.append(ll)

SR = len(SG)
SC = len(SG[0])
G = R * [list("." * C)]


def match(G, SG):
    offset = len(G) // 2 - len(SG) // 2
    for rr in range(len(SG)):
        for cc in range(len(SG[0])):
            if G[rr + offset][cc + +offset] != SG[rr][cc]:
                return False
    return True


seen = list()
pat_s, pat_e, pat_c = 0, 0, 0
pat_l = list()

for i in range(N):
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
    G = NG
    if match(G, SG):
        if seen and cnt == seen[0]:
            # repeated
            pat_e = i
            break

        if not seen:
            pat_s = i
        pat_c += cnt
        seen.append(cnt)
        pat_l.append((i - pat_s, cnt))

full_reps = (N - pat_s) // (pat_e - pat_s)
left = (N - pat_s) % full_reps
T = pat_c * full_reps
for offset, cnt in pat_l:
    left -= offset
    if left < 0:
        break
    T += cnt

print(f"{T}")
