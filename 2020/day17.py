"""
result dim3 : 348
result dim4 : 2236

times:

dim=3 (python3.9): 1s
dim=4 (python3.9): 22s
dim=4 (pypy3): 16s

"""

from itertools import product

dimensions = 4
cycles = 6

with open('day17.input') as f:
    actives = {
        (x, y, *([0] * (dimensions - 2)))
        for y, line in enumerate(f)
        for x, state in enumerate(line.strip())
        if state == '#'
    }


def neighbors(*coords):
    for shift in product((1, 0, -1), repeat=dimensions):
        if shift == (0,) * dimensions:
            continue
        yield tuple([c + s for c, s in zip(coords, shift)])


newactives = actives.copy()

for dz in range(1, cycles + 1):
    for active in actives:
        potes = set(neighbors(*active))
        if len(potes & actives) not in (2, 3):
            newactives.remove(active)
        for pote in potes:
            if len(set(neighbors(*pote)) & actives) == 3:
                newactives.add(pote)

    actives = newactives.copy()

print(len(actives))
