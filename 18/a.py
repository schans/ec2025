#!/usr/bin/env pypy3

import fileinput

# counters
T = 0

trees = dict()

ll = ""
cur = 0
for line in fileinput.input():
    ll = line.strip()
    if not ll:
        continue

    if ll.startswith("Plant"):
        ps = ll[:-1].split()
        cur = int(ps[1])
        th = int(ps[-1])
        trees[cur] = {"th": th, "conn": dict(), "free": False}
    elif ll.startswith("-"):
        ps = ll.split()
        if ps[1] == "free":
            trees[cur]["free"] = True
        elif ps[1] == "branch":
            conn = int(ps[4])
            th = int(ps[-1])
            trees[cur]["conn"][conn] = th
        else:
            assert False

last = cur


def get_output_for(tree):
    if trees[tree]["free"]:
        return 1

    t = 0
    for ct, th in trees[tree]["conn"].items():
        t += get_output_for(ct) * th

    if t >= trees[tree]["th"]:
        return t

    return 0


T = get_output_for(last)
print(f"{T}")
