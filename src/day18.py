from collections import deque

fname = "./examples/day18.txt"
end = (6, 6)
HT, WD = 6, 6
N_STEPS = 12


fname = "./inputs/day18.txt"
HT, WD = 70, 70
N_STEPS = 1024
end = (70, 70)

corrupted = set()
start = (0, 0)
to_add = []
with open(fname) as f:
    for i, coord in enumerate(f.read().strip().split()):
        x, y = coord.split(",")
        if i < N_STEPS:
            corrupted.add((int(y), int(x)))
        to_add.append((int(y), int(x)))


def neighbors(y, x):
    return [
        (y + dy, x + dx)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if (
            y + dy <= HT
            and y + dy >= 0
            and x + dx <= WD
            and x + dx >= 0
            and (y + dy, x + dx) not in corrupted
        )
    ]


def bfs(start, end):
    visited = set([start])
    q = deque([(0, start)])
    while q:
        cost, loc = q.popleft()
        if loc == end:
            return cost
        for n in neighbors(*loc):
            if n not in visited:
                visited.add(n)
                q.append((cost + 1, n))
    return -1


print("Part 1:", bfs(start, end))
corrupted = set()
for i, corr in enumerate(to_add):
    corrupted.add(corr)
    if bfs(start, end) == -1:
        print("Part 2:", (corr[1], corr[0]))
        break
