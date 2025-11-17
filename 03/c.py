#!/usr/bin/env pypy3

import fileinput
from collections import Counter

# counters
T = 0


for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    _, T = Counter([int(x) for x in l.split(",")]).most_common(1).pop()


print(f"Total {T}")
