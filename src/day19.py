from collections import deque

fname = "./examples/day19.txt"

fname = "./inputs/day19.txt"
patterns = set()
with open(fname) as f:
    p, d = f.read().strip().split("\n\n")
    patterns = set(p.split(", "))
    designs = list(d.split("\n"))

MAX_LEN = max(len(s) for s in patterns)

memo = {}


def legit_design(d, builder):
    # Go through string and store pottential patterns in builder
    # If builder is a pattern, reset builder
    # print("Call to", d, builder)
    if (d, builder) in memo:
        return memo[(d, builder)]

    if len(d) == 0:
        return builder == "" or builder in patterns
    elif builder in patterns:
        ans = legit_design(d[1:], d[0]) or legit_design(d[1:], builder + d[0])
        memo[(d, builder)] = ans
        return ans
    elif builder == "" or len(builder) < MAX_LEN:
        ans = legit_design(d[1:], builder + d[0])
        memo[(d, builder)] = ans
        return ans
    else:
        return False


p1 = 0
for d in designs:
    # print(d, possible_designs(d, ""))
    # p1 += possible_designs(d, ""
    print(d, legit_design(d, ""))
    if legit_design(d, ""):
        p1 += 1
    # break
print("Part 1:", p1)
