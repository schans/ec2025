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
assert all(x < y for x, y in zip(C, C[1:]))
avg = sum(C) // len(C)

# round 2
for i in range(len(C)):
    if C[i] < avg:
        N += avg - C[i]

print(f"{N}")
