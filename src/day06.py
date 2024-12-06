# fname = "./examples/day06.txt"
fname = "./inputs/day06.txt"
cur_loc = None
move_dir = (-1, 0)
START_MOVE_DIR = (-1, 0)
START_LOC = None
with open(fname) as f:
    grid = []
    for i, row in enumerate(f.read().strip().split("\n")):
        grid.append([c for c in row])
        if "^" in row:
            START_LOC = (i, row.index("^"))

cur_loc = START_LOC
rotater = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
HT, WD = len(grid), len(grid[0])

seen = set([cur_loc])
while True:
    next_move = (cur_loc[0] + move_dir[0], cur_loc[1] + move_dir[1])
    if next_move[0] < 0 or next_move[0] >= HT or next_move[1] < 0 or next_move[1] >= WD:
        break
    elif grid[next_move[0]][next_move[1]] == "#":
        move_dir = rotater[move_dir]
    else:
        seen.add(next_move)
        cur_loc = next_move

p1 = len(seen)

print("Part 1:", p1)


def check_for_loop(start_pt, start_dir, new_block):
    # Checks if you end up back at the start point
    cur_loc = start_pt
    move_dir = start_dir
    if grid[new_block[0]][new_block[1]] == "#":
        return False
    else:
        grid[new_block[0]][new_block[1]] = "#"
    seen = set()
    while True:
        next_move = (cur_loc[0] + move_dir[0], cur_loc[1] + move_dir[1])
        if (next_move, move_dir) in seen:
            grid[new_block[0]][new_block[1]] = "."
            return True
        elif (
            next_move[0] < 0
            or next_move[0] >= HT
            or next_move[1] < 0
            or next_move[1] >= WD
        ):
            grid[new_block[0]][new_block[1]] = "."
            return False
        elif grid[next_move[0]][next_move[1]] == "#":
            move_dir = rotater[move_dir]
        else:
            seen.add((next_move, move_dir))
            cur_loc = next_move


p2 = 0
from tqdm import tqdm

for block in tqdm(list(seen)):
    if check_for_loop(START_LOC, START_MOVE_DIR, block):
        p2 += 1

print("Part 2:", p2)
