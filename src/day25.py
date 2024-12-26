# fname = "./examples/day25.txt"
fname = "./inputs/day25.txt"
things = open(fname).read().strip().split("\n\n")
HEIGHT = 6


def parse_grid(grid):
    values = {}
    search_val = "." if grid[0] == "#" else "#"
    for i, row in enumerate(grid.split("\n")):
        for j, val in enumerate(row):
            if val == search_val and j not in values:
                if search_val == ".":
                    values[j] = i - 1
                else:
                    values[j] = HEIGHT - i

    return [j for i, j in sorted(values.items())]


keys, locks = [], []

for t in things:
    if t[0] == "#":
        locks.append(parse_grid(t))
    else:
        keys.append(parse_grid(t))

p1 = 0
for k in keys:
    for l in locks:
        if all(a + b < HEIGHT for a, b in zip(k, l)):
            p1 += 1

print("Part 1:", p1)
