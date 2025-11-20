#!/usr/bin/env pypy3

import fileinput

# counters
T = 0

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    lines.append(l.split(":")[1])


def score(l1, l2):
    cnt = 0
    for c1, c2 in zip(l1, l2):
        if c1 == c2:
            cnt += 1
    return cnt


def parents(child, parent1, parent2):
    for c, p1, p2 in zip(child, parent1, parent2):
        if c != p1 and c != p2:
            return False
    return True


for c in lines:
    for p1 in lines:
        if c == p1:
            continue
        for p2 in lines:
            if c == p2 or p1 == p2:
                continue
            if parents(c, p1, p2):
                T += score(c, p1) * score(c, p2)

print(f"{T // 2}")
