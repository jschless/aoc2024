# fname = "./examples/day06.txt"
fname = "./inputs/day06.txt"
START_MOVE_DIR = (-1, 0)
START_LOC = None

with open(fname) as f:
    grid = []
    for i, row in enumerate(f.read().strip().split("\n")):
        grid.append([c for c in row])
        if "^" in row:
            START_LOC = (i, row.index("^"))

rotater = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
HT, WD = len(grid), len(grid[0])


def check_for_loop(new_block):
    # Checks if you end up back at the start point
    # if new block is None, return list of path
    # if new_block is something, return whether this creates a loop or not
    cur_loc = START_LOC
    move_dir = START_MOVE_DIR
    seen = set([(START_LOC, START_MOVE_DIR)])
    if new_block is None:
        print("Part 1 running")
    elif grid[new_block[0]][new_block[1]] == "#":
        return False
    else:
        grid[new_block[0]][new_block[1]] = "#"

    while True:
        next_move = (cur_loc[0] + move_dir[0], cur_loc[1] + move_dir[1])
        if (next_move, move_dir) in seen:
            grid[new_block[0]][new_block[1]] = "."
            break
        elif (
            next_move[0] < 0
            or next_move[0] >= HT
            or next_move[1] < 0
            or next_move[1] >= WD
        ):
            if new_block:
                grid[new_block[0]][new_block[1]] = "."
                return False
            else:
                return list(set([x for x, y in seen]))
        elif grid[next_move[0]][next_move[1]] == "#":
            move_dir = rotater[move_dir]
        else:
            seen.add((next_move, move_dir))
            cur_loc = next_move
    return True


path = check_for_loop(None)
p1 = len(path)
print("Part 1:", p1)

p2 = len([1 for block in list(path) if check_for_loop(block)])
print("Part 2:", p2)
