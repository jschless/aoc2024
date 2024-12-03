import re

# fname = "./examples/day03b.txt"
fname = "./inputs/day03.txt"

with open(fname) as f:
    s = f.read().strip()

match_str = r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
p1, p2 = 0, 0
flag = True
for x in re.findall(match_str, s):
    if x == "do()":
        flag = True
    elif x == "don't()":
        flag = False
    else:
        nums = [int(a) for a in x[4:-1].split(",")]
        p1 += nums[0] * nums[1]
        if flag:
            p2 += nums[0] * nums[1]

print("Part 1:", p1)
print("Part 2:", p2)
