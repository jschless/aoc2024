fname = "./examples/day19.txt"
fname = "./inputs/day19.txt"

with open(fname) as f:
    p, d = f.read().strip().split("\n\n")
    patterns = set(p.split(", "))
    designs = list(d.split("\n"))

MAX_LEN = max(len(s) for s in patterns)

memo = {}


def count_designs(d, builder):
    if (d, builder) in memo:
        return memo[(d, builder)]

    if len(d) == 0:
        return 1 if builder == "" or builder in patterns else 0
    elif builder in patterns:
        ans = count_designs(d[1:], d[0]) + count_designs(d[1:], builder + d[0])
        memo[(d, builder)] = ans
        return ans
    elif builder == "" or len(builder) < MAX_LEN:
        ans = count_designs(d[1:], builder + d[0])
        memo[(d, builder)] = ans
        return ans
    else:
        return 0


p1, p2 = 0, 0
for d in designs:
    ans = count_designs(d, "")
    if ans > 0:
        p1 += 1
        p2 += ans

print("Part 1:", p1)
print("Part 2:", p2)
