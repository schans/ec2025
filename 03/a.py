#!/usr/bin/env pypy3

import fileinput

# counters
T = 0


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    T = sum({int(x) for x in l.split(",")})


print(f"Total {T}")
