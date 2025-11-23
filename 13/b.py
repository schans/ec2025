#!/usr/bin/env pypy3

import fileinput
from collections import deque

# counters
T = 0
D = deque([1])
N = 20252025

right = True
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    (s, e) = (int(x) for x in ll.split("-"))

    print(s, e)
    for x in range(s, e + 1):
        if right:
            D.append(x)
        else:
            D.appendleft(x)

    right = not right

T = D[(N + D.index(1)) % len(D)]
print(f"{T}")
