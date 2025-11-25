#!/usr/bin/env pypy3

import fileinput

# counters
T = 1
N = []

ll = ""
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue
    N = [int(x) for x in ll.split(",")]

L = len(N)
while sum(N) > 0:
    for n in range(L):
        if N[n] == 1:
            T *= n + 1
            for i in range(n, L):
                if (i + 1) % (n + 1) == 0:
                    N[i] -= 1
            break

print(f"{T}")
