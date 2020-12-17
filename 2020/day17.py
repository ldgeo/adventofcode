"""
result dim3 : 348
result dim4 : 2236

times:

dim=3 (python3.9): 0.4s
dim=4 (python3.9): 19s
dim=4 (pypy3): 10s

"""

from itertools import product

dimensions = 4
cycles = 6
root_coords = (0,) * dimensions

with open('day17.input') as f:
    actives = {
        (x, y, *([0] * (dimensions - 2)))
        for y, line in enumerate(f)
        for x, state in enumerate(line.strip())
        if state == '#'
    }


def neighbors(*coords):
    """
    for shift in product((1, 0, -1), repeat=dimensions):
        if shift == (0,) * dimensions:
            continue
        yield tuple([c + s for c, s in zip(coords, shift)])
    """
    return {
        tuple([c + s for c, s in zip(coords, shift)])
        for shift in product((1, 0, -1), repeat=dimensions)
        if shift != root_coords
    }


newactives = actives.copy()

for _ in range(cycles):
    for active in actives:
        potes = neighbors(*active)
        if len(potes & actives) not in (2, 3):
            newactives.remove(active)
        for pote in potes:
            if len(neighbors(*pote) & actives) == 3:
                newactives.add(pote)

    actives = newactives.copy()

print(len(actives))
