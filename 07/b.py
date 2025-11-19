#!/usr/bin/env pypy3

import fileinput
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
for i in range(1, len(lines)):
    l, r = lines[i].split(" > ")
    TR[l] = r.split(",")


@cache
def check(w):
    if len(w) == 1:
        return True
    if not check(w[:-1]):
        return False
    if w[-2] not in TR or w[-1] not in TR[w[-2]]:
        return False
    return True


for i in range(0, len(words)):
    if check(words[i]):
        T += i + 1

print(f"{T}")
