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


L = L * R
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

print(f"Total {int(T)}")
