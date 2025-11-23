#!/usr/bin/env pypy3

import fileinput
from collections import deque

# counters
T = 0
D = deque([1])
N = 2025

for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    if len(D) % 2:
        D.append(int(ll))
    else:
        D.appendleft(int(ll))

T = D[(N + D.index(1)) % len(D)]
print(f"{T}")
