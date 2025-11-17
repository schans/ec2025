#!/usr/bin/env pypy3

import fileinput

# counters
G = []

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    G.append(tuple(int(x) for x in l.split("|")))

G[0] = (0, G[0][0])
m = 1
for i in range(0, len(G) - 1):
    m = m * (G[i][1] / G[i + 1][0])

r = int(100 * m)
print(f"Total {r}")
