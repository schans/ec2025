#!/usr/bin/env pypy3

import fileinput
from collections import deque

# counters
T = 0
N = 202520252025
L = 1
R = deque([(1, 1, 1, False)])

right = True
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    (s, e) = (int(x) for x in ll.split("-"))

    assert e > s
    L += 1 + e - s
    if right:
        R.append((s, e, e - s + 1, right))
    else:
        R.appendleft((s, e, e - s + 1, right))

    right = not right

t = N % L
ii = R.index((1, 1, 1, False))

for x in range(len(R)):
    xi = (x + ii) % len(R)
    (s, e, n, right) = R[xi]
    if t - n >= 0:
        t -= n
    else:
        if right:
            T = s + t
        else:
            T = e - t
        break

print(f"{T}")
