fname = "./examples/day15.txt"
# fname = "./examples/day15b.txt"
fname = "./inputs/day15.txt"
DEBUG = False
grid = {}
cur_loc = None
with open(fname) as f:
    grid_str, inst = f.read().strip().split("\n\n")
    for i, row in enumerate(grid_str.split("\n")):
        for j, char in enumerate(row):
            if char == "@":
                cur_loc = (i, j)
            grid[(i, j)] = char
            WD = j
            HT = i

move_dir = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def push_rock(l, d):
    new_loc = (l[0] + d[0], l[1] + d[1])
    if DEBUG:
        print(f"Call to push rock at {l} in dir {d}, new_loc is {new_loc}")
    if grid[new_loc] == ".":
        grid[new_loc] = "O"
    elif grid[new_loc] == "O":
        # propogate the push
        grid[new_loc] = "O"
        grid[l] = "O"
        push_rock(new_loc, d)


def has_space(l, d):
    new_loc = (l[0] + d[0], l[1] + d[1])
    if grid[new_loc] == "O":
        return has_space(new_loc, d)
    else:
        return grid[new_loc] == "."


def make_move(cur_loc, d):
    new_loc = (cur_loc[0] + d[0], cur_loc[1] + d[1])
    if grid[new_loc] == ".":
        grid[cur_loc] = "."
        grid[new_loc] == "@"
        return new_loc
    elif grid[new_loc] == "O" and has_space(cur_loc, d):
        push_rock(new_loc, d)
        grid[cur_loc] = "."
        grid[new_loc] = "@"
        return new_loc

    return cur_loc


def print_grid():
    print(cur_loc)
    s = ""
    for i in range(HT + 1):
        for j in range(WD + 1):
            s += grid[(i, j)]
        s += "\n"
    print(s)


for x, i in enumerate(inst.strip().replace("\n", "")):
    if DEBUG:
        print(f"{x+1}:  current move is {i}")
    cur_loc = make_move(cur_loc, move_dir[i])
    if DEBUG:
        print_grid()

p1, p2 = 0, 0
for coord, char in grid.items():
    if char == "O":
        p1 += 100 * coord[0] + coord[1]

print("Part 1:", p1)
print("Part 2:", p2)
