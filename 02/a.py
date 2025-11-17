#!/usr/bin/env pypy3

import fileinput

# counters
a = 0 + 0j
r = 0 + 0j
N = 3

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    p = [int(x) for x in l.split("=")[1][1:-1].split(",")]
    a = complex(*p)

for _ in range(N):
    r = r * r
    # [X1,Y1] / [X2,Y2] = [X1 / X2, Y1 / Y2]
    r = complex(int(r.real / 10), int(r.imag / 10))
    r = r + a

print(f"{[int(r.real), int(r.imag)]}")
