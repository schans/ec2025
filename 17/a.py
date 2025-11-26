#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
G = []
L = 10
S = (0, 0)

ll = ""
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue
    if "@" in ll:
        S = (len(G), ll.index("@"))
        ll = ll.replace("@", "0")
    G.append([int(x) for x in ll])

R = len(G)
C = len(G[0])
R2 = pow(L, 2)

for r in range(R):
    for c in range(C):
        x2 = pow(S[0] - r, 2)
        y2 = pow(S[1] - c, 2)
        if x2 + y2 <= R2:
            T += G[r][c]


print(f"{T}")
