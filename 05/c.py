#!/usr/bin/env pypy3

import fileinput
from functools import cmp_to_key

# counters
FL = []

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    N = [int(x) for x in l.split(":")[1].split(",")]
    ID = int(l.split(":")[0])
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

        # new segment
        if not placed:
            S.append([0, n, 0])
            T += str(n)

    FL.append((int(T), ID, S.copy()))


def sword_cmp(a, b):
    # quality compare
    if a[0] > b[0]:
        return -1
    elif a[0] < b[0]:
        return 1

    # sub compare
    for z in range(len(a[2])):
        # strip right zeros: '590' -> '59'
        k1 = int("".join([str(x) for x in a[2][z] if x > 0]))
        k2 = int("".join([str(x) for x in b[2][z] if x > 0]))
        if k1 < k2:
            return 1
        elif k1 > k2:
            return -1

    # id compare, ids are unique
    if a[1] < b[1]:
        return 1
    else:
        return -1


sword_cmp_key = cmp_to_key(sword_cmp)
FL.sort(key=sword_cmp_key)

tot = 0
for i in range(len(FL)):
    tot += (i + 1) * FL[i][1]

# print(f"b: {FL[0][0] - FL[-1][0]}")
print(f"Total {tot}")
