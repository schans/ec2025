#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
N = []
L = 90

ll = ""
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue
    N = [int(x) for x in ll.split(",")]

for n in N:
    T += L // n

print(f"{T}")
