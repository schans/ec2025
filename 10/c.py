#!/usr/bin/env pypy3

import fileinput
from collections import deque

# counters
T = 0
D = set()
S = set()
H = set()

N = 20
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

queue = deque([(D, tuple(S), True)])
seen = dict()
seen[(D, tuple(S), True)] = 1

while queue:
    (dd, ss, smove) = queue.popleft()
    cnt = seen.pop((dd, ss, smove))
    if smove:
        if len(ss) == 0:
            T += cnt
            continue

        # sheep move
        moved = False
        for i, (rr, cc) in enumerate(ss):
            nr = rr + 1
            if nr == R:
                moved = True
            elif (nr, cc) in H or (nr, cc) != dd:
                # safe step
                moved = True
                ns = (*ss[:i], (nr, cc), *ss[i + 1 :])
                if (dd, ns, False) in seen:
                    seen[(dd, ns, False)] += cnt
                else:
                    seen[(dd, ns, False)] = cnt
                    queue.append((dd, ns, False))
            else:
                # blocked
                assert (nr, cc) == dd

        # no sheep moved
        if not moved:
            if (dd, ss, False) in seen:
                seen[(dd, ss, False)] += cnt
            else:
                seen[(dd, ss, False)] = cnt
                queue.append((dd, ss, False))

    else:
        # dragon move
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

            if (nd, ns, True) in seen:
                seen[(nd, ns, True)] += cnt
            else:
                seen[(nd, ns, True)] = cnt
                queue.append((nd, ns, True))

print(f"{T}")
