#!/usr/bin/env pypy3

import fileinput
from functools import cache

# counters
D = set()
S = set()
H = set()

DIRS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
r = 0
for line in fileinput.input():
    l = line.strip()
    if not l:
        continue

    for c, x in enumerate(l):
        if x == "D":
            D = (r, c)
        elif x == "S":
            S.add((r, c))
        elif x == "#":
            H.add((r, c))
    r += 1

R = r
C = len(l)


@cache
def count(dd, ss, smove):
    if smove:
        # sheep move
        if len(ss) == 0:
            return 1

        moved = False
        cnt = 0
        for i, (rr, cc) in enumerate(ss):
            nr = rr + 1
            if nr == R:
                # survived, discard
                moved = True
            elif (nr, cc) in H or (nr, cc) != dd:
                # safe step
                moved = True
                ns = (*ss[:i], (nr, cc), *ss[i + 1 :])
                cnt += count(dd, ns, False)
            else:
                # blocked
                assert (nr, cc) == dd

        if moved:
            return cnt
        else:
            # no sheep moved
            return count(dd, ss, False)

    else:
        # dragon move
        cnt = 0
        (rr, cc) = dd
        for dr, dc in DIRS:
            nr = rr + dr
            nc = cc + dc
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            nd = (nr, nc)
            ns = ss
            # eat
            if nd in ss and nd not in H:
                ns = tuple(sh for sh in ss if sh != nd)
            cnt += count(nd, ns, True)
        return cnt


print(f"{count(D, tuple(S), True)}")
