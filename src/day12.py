fname = "./examples/day12c.txt"
# fname = "./inputs/day12.txt"
grid = {}
WD, HT = 0, 0
with open(fname) as f:
    txt = f.read().strip()
    for i, row in enumerate(txt.split("\n")):
        for j, col in enumerate(row):
            grid[(i, j)] = col
            HT = i
            WD = j

seen = set()

neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def explore(loc):
    ans = []
    for i, j in neighbors:
        new_loc = (loc[0] + i, loc[1] + j)
        if grid.get(new_loc, -1) == grid[loc] and new_loc not in seen:
            seen.add(new_loc)
            ans.append(new_loc)
            ans.extend(explore(new_loc))
    return ans


def compute_perimeter(locs):
    # given a region in the form of a list, compute the perimeter
    per = 0
    for loc in locs:
        for i, j in neighbors:
            new_loc = (loc[0] + i, loc[1] + j)
            if grid.get(new_loc, -1) != grid[loc]:
                per += 1
    return per


debug = False


def compute_sides(locs, start_i=0):
    per = 0
    for loc in locs:
        if any(
            [grid.get((loc[0] + i, loc[1] + j), -1) != grid[loc] for i, j in neighbors]
        ):
            per += 1

    if len(locs) == 1:
        return 4

    s_loc = set(locs)
    sides = 1
    cur = locs[start_i]
    explored = set([cur])
    start = cur
    cur_dir = (0, 1)
    turn_left = {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1)}
    turn_right = {k: (-v[0], -v[1]) for k, v in turn_left.items()}
    if debug:
        print(grid[cur], cur)
    while True:
        if (cur[0] + turn_left[cur_dir][0], cur[1] + turn_left[cur_dir][1]) in s_loc:
            # Turn left
            cur_dir = turn_left[cur_dir]
            sides += 1
        elif (cur[0] + cur_dir[0], cur[1] + cur_dir[1]) in s_loc:
            # go straight
            cur_dir = cur_dir
        elif (
            cur[0] + turn_right[cur_dir][0],
            cur[1] + turn_right[cur_dir][1],
        ) in s_loc:
            # turn right
            cur_dir = turn_right[cur_dir]
            sides += 1
        elif (
            cur[0] + turn_right[turn_right[cur_dir]][0],
            cur[1] + turn_right[turn_right[cur_dir]][1],
        ) in s_loc:
            # need to do a 180
            cur_dir = turn_right[turn_right[cur_dir]]
            sides += 2

        cur = (cur[0] + cur_dir[0], cur[1] + cur_dir[1])
        explored.add(cur)
        if debug:
            print(
                f"After move, location is  {cur} and dir is {cur_dir}, sides is {sides}"
            )
            print(f"Explored {len(explored)} but per is {per}")
        if cur == start and len(explored) >= per:
            # started facing east, so if i return facing west, I will miss one side (bc i won't do the turn)
            if cur_dir == (0, -1):
                sides += 1
            return sides


p1, p2 = 0, 0
for i in range(HT + 1):
    for j in range(WD + 1):
        if (i, j) not in seen:
            region = [(i, j)]
            seen.add((i, j))
            region.extend(explore((i, j)))
            area = len(region)
            per = compute_perimeter(region)
            # print(region)
            for z in range(len(region)):
                sides = compute_sides(region, start_i=z)
                print(sides)
            p1 += area * per
            print(area, sides)
            p2 += area * sides

print("Part 1:", p1)
print("Part 2:", p2)

# P2 should be 908042
