#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
N = 32

nails = list()
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    nails = [int(x) for x in l.split(",")]

for i in range(0, len(nails) - 1):
    d = abs(nails[i] - nails[i + 1])
    if d == N / 2:
        T += 1

print(f"{T}")
