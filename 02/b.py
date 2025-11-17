#!/usr/bin/env pypy3

import fileinput

# counters
a = 0 + 0j
e = 0 + 0j
r = 0 + 0j
N = 100
P = 0

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    p = [int(x) for x in l.split("=")[1][1:-1].split(",")]
    a = complex(*p)
    e = a + 1000 + 1000j

for x in range(int(a.real), int(e.real) + 1, 10):
    for y in range(int(a.imag), int(e.imag) + 1, 10):
        ok = True
        r = 0 + 0j
        c = complex(x, y)
        for _ in range(N):
            r = r * r
            # [X1,Y1] / [X2,Y2] = [X1 / X2, Y1 / Y2]
            r = complex(int(r.real / 100000), int(r.imag / 100000))
            r = r + c
            if abs(r.real) > 1_000_000 or abs(r.imag) > 1_000_000:
                ok = False
                break
        if ok:
            P += 1

print(f"{P}")
