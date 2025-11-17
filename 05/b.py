#!/usr/bin/env pypy3

import fileinput

# counters
N = []
MA = 0
MI = 1e20

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    N = [int(x) for x in l.split(":")[1].split(",")]

    S = []
    T = ""
    for n in N:
        placed = False
        for i in range(len(S)):
            l, m, r = S[i]
            if l == 0 and n < m:
                S[i][0] = n
                placed = True
                break
            if r == 0 and n > m:
                S[i][2] = n
                placed = True
                break

        # new seg
        if not placed:
            S.append([0, n, 0])
            T += str(n)

    T = int(T)
    MA = max(MA, T)
    MI = min(MI, T)

print(f"Total {MA - MI}")
