#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
L = ""
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    L = l

for i in range(len(L)):
    if L[i] in "ABC":
        continue
    for j in range(0, i):
        if L[i] == "a" and L[j] == "A":
            T += 1
        elif L[i] == "b" and L[j] == "B":
            T += 1
        elif L[i] == "c" and L[j] == "C":
            T += 1

print(f"Total {int(T)}")
