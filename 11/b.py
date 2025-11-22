#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
N = 0
M = 10
C = list()

for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue
    C.append(int(ll))

# round 1
moved = True
while moved:
    moved = False
    for i in range(len(C) - 1):
        if C[i] > C[i + 1]:
            C[i] -= 1
            C[i + 1] += 1
            moved = True
    if moved:
        N += 1

# round 2
moved = True
while moved:
    moved = False
    for i in range(len(C) - 1):
        if C[i] < C[i + 1]:
            C[i] += 1
            C[i + 1] -= 1
            moved = True
    if moved:
        N += 1

print(f"{N}")
