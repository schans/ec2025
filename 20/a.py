#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
X = set()
H = set()

r = 0
ll = ""
even_row = True
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    c = 0

    for ch in ll:
        rr = r
        if even_row:
            if c % 2 == 1:
                rr += 1
            if ch == "T":
                X.add((rr, c))
            if ch == "#":
                H.add((rr, c))
        else:
            if c % 2 == 0:
                rr += 1
            if ch == "T":
                X.add((rr, c))
            if ch == "#":
                H.add((rr, c))

        c += 1
    r += 2
    even_row = not even_row

for r, c in X:
    for dr, dc in [(-1, 0), (1, -1), (1, 1), (-1, -1), (-1, 1), (1, 0)]:
        if (r + dr, c + dc) in X:
            T += 1

print(f"{T // 2}")
