#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
N = 8

nails = list()
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    nails = [int(x) for x in l.split(",")]


def cross(l1, l2):
    a, b = min(l1), max(l1)
    x, y = min(l2), max(l2)
    if a < x < b and y > b:
        return True
    if a < y < b and x < a:
        return True
    return False


placed = set()
for i in range(0, len(nails) - 1):
    cur = (nails[i], nails[i + 1])
    for p in placed:
        if cross(cur, p):
            T += 1
    placed.add(cur)

print(f"{T}")
