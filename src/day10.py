# fname = "./examples/day10.txt"
fname = "./inputs/day10.txt"
grid = {}
poss = []
with open(fname) as f:
    txt = f.read().strip()
    for i, row in enumerate(txt.split("\n")):
        for j, col in enumerate(row):
            grid[(i, j)] = int(col)
            if int(col) == 0:
                poss.append((i, j))

nines = set()


def explore(loc, last):
    if grid[loc] == 9:
        nines.add(loc)
        return 1
    else:
        ans = 0
        for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_loc = (loc[0] + i, loc[1] + j)
            if grid.get(new_loc, -99) == last + 1:
                ans += explore(new_loc, grid[new_loc])
        return ans


p1, p2 = 0, 0
for p in poss:
    nines = set()
    p2 += explore(p, 0)
    p1 += len(nines)

print("Part 1:", p1)
print("Part 2:", p2)
