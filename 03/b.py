#!/usr/bin/env pypy3

import fileinput

# counters
T = 0


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    T = sum(sorted(list({int(x) for x in l.split(",")}))[:20])


print(f"Total {T}")
