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
ss = []
ss.append(0)

for mx in range(1, R // 2):
    t = 0
    for r in range(R // 2 - mx - 1, R // 2 + mx + 1):
        for c in range(C // 2 - mx - 1, C // 2 + mx + 1):
            x2 = pow(S[0] - r, 2)
            y2 = pow(S[1] - c, 2)
            if x2 + y2 <= mx * mx:
                t += G[r][c]
                G[r][c] = 0
    ss.append(t)

T = max(ss) * (ss.index(max(ss)))

print(f"{T}")
