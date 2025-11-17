#!/usr/bin/env pypy3

import fileinput

# counters
G = []

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    G.append(int(l))

m = 1
for i in range(0, len(G) - 1):
    m = m * (G[i] / G[i + 1])

r = int(m * 2025)
print(f"Total {r}")
