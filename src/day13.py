import numpy as np

# fname = "./examples/day13.txt"
fname = "./inputs/day13.txt"


def get_ints(s):
    _, _, a1, a2 = s.split(" ")
    return (int(a1[2:-1]), int(a2[2:]))


def solve(pset):
    (ax, ay), (bx, by), (zx, zy) = pset
    solution = np.linalg.solve(np.array([[ax, bx], [ay, by]]), np.array([zx, zy]))

    # check solution, make sure clean integers work
    a, b = round(solution[0]), round(solution[1])
    if ax * a + bx * b == zx and ay * a + by * b == zy:
        return 3 * a + b
    return 0


p1 = 0
p2 = 0
P2_CONST = 10_000_000_000_000
with open(fname) as f:
    for pset in f.read().strip().split("\n\n"):
        a, b, prize = pset.split("\n")
        a = get_ints(a)
        b = get_ints(b)
        _, x, y = prize.split(" ")
        prize = (int(x[2:-1]), int(y[2:]))
        p2_prize = (prize[0] + P2_CONST, prize[1] + P2_CONST)
        p1 += solve((a, b, prize))
        p2 += solve((a, b, p2_prize))

print("Part 1:", p1)
print("Part 2:", p2)
