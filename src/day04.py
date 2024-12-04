from itertools import product

# fname = "./examples/day04.txt"
fname = "./inputs/day04.txt"

grid = []
with open(fname) as f:
    grid = [list(line.strip()) for line in f.readlines()]


def grid_get(x: int, y: int) -> str:
    return "?" if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) else grid[y][x]


def xmas_search(i: int, j: int) -> int:
    count = 0
    for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
        for step, char in enumerate("MAS"):
            x, y = i + dx * (step + 1), j + dy * (step + 1)
            if grid_get(x, y) != char:
                break
            elif char == "S":  # End of search, found XMAS
                count += 1
    return count


def mas2_search(i: int, j: int) -> int:
    # returns 1 if a is at the center of an xmas x

    d1 = grid_get(i - 1, j - 1) + grid_get(i + 1, j + 1)
    d2 = grid_get(i - 1, j + 1) + grid_get(i + 1, j - 1)
    if (d1 == "MS" or d1 == "SM") and (d2 == "MS" or d2 == "SM"):
        return 1
    return 0


p1, p2 = 0, 0
for col in range(len(grid)):
    for row in range(len(grid[0])):
        if grid[col][row] == "X":
            p1 += xmas_search(row, col)

        if grid[col][row] == "A":
            p2 += mas2_search(row, col)


print("Part 1:", p1)
print("Part 2:", p2)
