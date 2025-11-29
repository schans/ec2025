#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
X = set()

r = 0
ll = ""
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    c = 0
    for ch in ll:
        if ch == ".":
            continue
        if ch == "T":
            X.add((r, c))
        c += 1
    r += 1

for r, c in X:
    HDIRS = {(0, -1), (0, 1)}
    dirs = HDIRS

    if c % 2 == 0:
        dirs.add((-1, 1))
    else:
        dirs.add((1, -1))

    for dr, dc in dirs:
        if (r + dr, c + dc) in X:
            T += 1


print(f"{T // 2}")
