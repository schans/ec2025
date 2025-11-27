#!/usr/bin/env pypy3

import fileinput

# counters
T = 0
activates = list()
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
    if ll[0] in "01":
        activates.append([x == "1" for x in ll.split()])

last = cur


def get_output_for(tree, run):
    if trees[tree]["free"]:
        if activates[run][tree - 1]:
            return 1
        return 0

    t = 0
    for ct, th in trees[tree]["conn"].items():
        t += get_output_for(ct, run) * th

    if t >= trees[tree]["th"]:
        return t

    return 0


def get_min_for(tree):
    if trees[tree]["free"]:
        return 0

    t = 0
    for ct, th in trees[tree]["conn"].items():
        if th < 0:
            t += get_max_for(ct) * th
        else:
            t += get_min_for(ct) * th

    if t >= trees[tree]["th"]:
        return t

    return 0


def get_max_for(tree):
    if trees[tree]["free"]:
        return 1

    t = 0
    for ct, th in trees[tree]["conn"].items():
        if th < 0:
            t += get_min_for(ct) * th
        else:
            t += get_max_for(ct) * th

    if t >= trees[tree]["th"]:
        return t

    return 0


energies = []
for i in range(len(activates)):
    energies.append(get_output_for(last, i))

# this strategy works because of structure of the tree and is not a general solution
max_out = get_max_for(last)
for enery in energies:
    if enery > 0:
        T += max_out - enery

print(f"{T}")
