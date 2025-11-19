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
    if L[i] in "A":
        continue
    for j in range(0, i):
        if L[i] == "a" and L[j] == "A":
            T += 1

print(f"Total {int(T)}")
