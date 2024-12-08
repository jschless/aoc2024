from collections import defaultdict
from itertools import combinations

# fname = "./examples/day08.txt"
fname = "./inputs/day08.txt"
ants = defaultdict(list)
with open(fname) as f:
    txt = f.read().strip()
    for i, row in enumerate(txt.split("\n")):
        for j, col in enumerate(row):
            HT, WD = i, j
            if col != ".":
                ants[col].append((i, j))


def bounds_check(a):
    return a[0] >= 0 and a[0] <= HT and a[1] >= 0 and a[1] <= WD


def find_antinodes(a1, a2, beg, end):
    ret = []
    for i in range(beg, end):
        antinode = (a1[0] + i * (a1[0] - a2[0]), a1[1] + i * (a1[1] - a2[1]))
        if bounds_check(antinode):
            ret.append(antinode)
        else:
            return ret
    return ret


antinodes = set()
for a, locs in ants.items():
    for a1, a2 in combinations(locs, 2):
        antinodes.update(find_antinodes(a1, a2, 1, 2))
        antinodes.update(find_antinodes(a2, a1, 1, 2))

p1 = len(antinodes)
print("Part 1:", p1)

for a, locs in ants.items():
    for a1, a2 in combinations(locs, 2):
        antinodes.update(find_antinodes(a1, a2, 0, 50))
        antinodes.update(find_antinodes(a2, a1, 0, 50))

p2 = len(antinodes)
print("Part 2:", p2)
