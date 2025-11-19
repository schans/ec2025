#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
L = ""
D = 1000
R = 1000

for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    L = l

p = 0
diff = 0
orig = L
for r in range(1, 3):
    L = orig * r
    T = 0
    for i in range(len(L)):
        if L[i] in "ABC":
            continue

        s = max(0, i - D)
        e = min(i + D + 1, len(L))
        for j in range(s, e):
            if L[i] == "a" and L[j] == "A":
                T += 1
            elif L[i] == "b" and L[j] == "B":
                T += 1
            elif L[i] == "c" and L[j] == "C":
                T += 1
    diff = T - p
    p = T

T += (R - 2) * diff
print(f"Total {int(T)}")
