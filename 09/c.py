#!/usr/bin/env pypy3

import fileinput
from collections import defaultdict

# counters
T = 0

lines = []
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue
    lines.append(l.split(":")[1])


def score(l1, l2):
    cnt = 0
    for c1, c2 in zip(l1, l2):
        if c1 == c2:
            cnt += 1
    return cnt


def parents(child, parent1, parent2):
    for c, p1, p2 in zip(child, parent1, parent2):
        if c != p1 and c != p2:
            return False
    return True


nodes = defaultdict(lambda: {"p": set(), "c": set()})
for ci, c in enumerate(lines):
    for pi1, p1 in enumerate(lines):
        if c == p1:
            continue
        for pi2, p2 in enumerate(lines):
            if c == p2 or p1 == p2:
                continue
            if parents(c, p1, p2):
                nodes[ci + 1]["p"] = {pi1 + 1, pi2 + 1}
                nodes[pi1 + 1]["c"].add(ci + 1)
                nodes[pi2 + 1]["c"].add(ci + 1)


ml = 0
used = set()
for n in nodes:
    if n in used:
        continue
    cand = [n]
    fam = set()
    while cand:
        n = cand.pop()
        fam.add(n)
        if n in nodes:
            for p in nodes[n]["p"]:
                if p not in fam:
                    cand.append(p)
            for c in nodes[n]["c"]:
                if c not in fam:
                    cand.append(c)

    if len(fam) > ml:
        ml = len(fam)
        T = sum(fam)
    used |= fam


print(f"{T}")
