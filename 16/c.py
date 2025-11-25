#!/usr/bin/env pypy3

import fileinput

# counters
N = []
M = []
B = 202520252025000

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
            M.append(n + 1)
            for i in range(n, L):
                if (i + 1) % (n + 1) == 0:
                    N[i] -= 1
            break


def blocks_for_len(bl):
    tot = 0
    for n in M:
        tot += bl // n
    return tot


def bsearch(max_len, target):
    left = 1
    right = max_len

    mid, mid_bl = 0, 0
    while left <= right:
        mid = (left + right) // 2
        mid_bl = blocks_for_len(mid)

        if mid_bl == target:
            return mid, mid_bl

        if mid_bl < target:
            left = mid + 1
        else:
            right = mid - 1

    return mid, mid_bl


b_len, b_tot = bsearch(1e15, B)
if b_tot <= B:
    T = int(b_len)
else:
    T = int(b_len - 1)

print(f"{T}")
