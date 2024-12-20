from collections import Counter
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
            HT, WD = i, j
            if char == "S":
                start = (i, j)
            if char == "E":
                end = (i, j)
            if char in [".", "S", "E"]:
                open_squares.append((i, j))
# Approach:
# There is only one path around
# 1. Find this path, make a dict that maps each location on path to its time
# 2. Search through all pairs of "." squares that are <= 2 movements away),
#    if you can join them by going through two "#"s, then return the cost savings

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


search(start, 0)
savings = []


def cost_savings(p1, p2):
    # If a cheat can save some time here, return time saved
    # If you run into a ".", return (some other pairing will catch this cheat)
    # Orientations: a##b, a#.b, a.#b,
    # a a a a
    # # . # ##
    # # # . #b
    # b b b
    # generate all possible move sequences (16)
    # if the move gets you to one of p2's neighbors and it included only "#s", then print something
    y1, x1 = p1
    y2, x2 = p2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Ensure the move is valid (only vertical or horizontal movement of 1 or 2 spaces)
    if (
        (dx == 0 and dy in [1, 2])
        or (dy == 0 and dx in [1, 2])
        or (dy == 1 and dx == 1)
    ):
        path = []
        if dx == 0:  # vertical movement
            y_min, y_max = sorted([y1, y2])
            path = [grid[(y, x1)] for y in range(y_min, y_max + 1)]
        elif dy == 0:  # Horizontal movement
            x_min, x_max = sorted([x1, x2])
            path = [grid[(y1, x)] for x in range(x_min, x_max + 1)]
        if path.count("#") in [1, 2]:
            # print(f"Savings from {p1} to {p2}: {abs(costs[p2] - costs[p1]) - 2}")
            savings.append(abs(costs[p2] - costs[p1]) - 2)
    else:
        return


for i in range(len(open_squares)):
    for j in range(i + 1, len(open_squares)):
        cost_savings(open_squares[i], open_squares[j])

THRESH = 100
p1 = len([x for x in savings if x >= THRESH])

print("Part 1:", p1)
# print(sorted(Counter(savings).items()))
