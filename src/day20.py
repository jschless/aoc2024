import sys

sys.setrecursionlimit(10_000)
fname = "./examples/day20.txt"
fname = "./inputs/day20.txt"
grid = {}
start, end = None, None
open_squares = []
with open(fname) as f:
    for i, row in enumerate(f.read().strip().split()):
        for j, char in enumerate(row):
            grid[(i, j)] = char
            if char == "S":
                start = (i, j)
            if char == "E":
                end = (i, j)
            if char in [".", "S", "E"]:
                open_squares.append((i, j))

explored = set([start])
costs = {start: 0}
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def search(cur, cost):
    costs[cur] = cost
    if cur != end:
        for dy, dx in moves:
            nxt = (cur[0] + dy, cur[1] + dx)
            c = grid.get(nxt, -1)
            if c != "#" and c != "-1" and nxt not in explored:
                explored.add(nxt)
                return search(nxt, cost + 1)


def cost_savings(p1, p2, max_diff=2):
    y1, x1 = p1
    y2, x2 = p2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Ensure the move is valid (only movement of max_diff spaces)
    if dx + dy > 1 and dx + dy <= max_diff:
        y_min, y_max = sorted([y1, y2])
        x_min, x_max = sorted([x1, x2])
        wall_count = 0
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                if grid[(y, x)] == "#":
                    wall_count += 1

        if wall_count > 0:
            return abs(costs[p2] - costs[p1]) - (dx + dy)
    return -1


search(start, 0)
p1, p2 = 0, 0
for i in range(len(open_squares)):
    for j in range(i + 1, len(open_squares)):
        if cost_savings(open_squares[i], open_squares[j], 2) >= 100:
            p1 += 1
        if cost_savings(open_squares[i], open_squares[j], 20) >= 100:
            p2 += 1

print("Part 1:", p1)
print("Part 2:", p2)
