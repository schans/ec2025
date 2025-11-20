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


T = score(lines[0], lines[2]) * score(lines[1], lines[2])
print(f"{T}")
