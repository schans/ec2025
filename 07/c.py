#!/usr/bin/env pypy3

import fileinput
from collections import deque
from functools import cache

# counters
T = 0

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    lines.append(l)

words = lines[0].split(",")
TR = dict()
C = set()

for i in range(1, len(lines)):
    l, r = lines[i].split(" > ")
    TR[l] = r.split(",")
    C |= set(r.split(","))


@cache
def check(w):
    if len(w) == 1:
        return True
    if not check(w[:-1]):
        return False
    if w[-2] not in TR or w[-1] not in TR[w[-2]]:
        return False
    return True


found = set()
for i in range(0, len(words)):
    cand = deque([words[i]])
    while cand:
        w = cand.popleft()
        for c in C:
            nw = w + c
            if check(nw):
                if len(nw) < 11 and nw not in found:
                    cand.append(nw)
                if len(nw) >= 7:
                    found.add(nw)


print(f"{len(found)}")
