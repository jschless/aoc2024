# fname = "./examples/day02.txt"
fname = "./inputs/day02.txt"

with open(fname) as f:
    lines = [[int(x) for x in line.split()] for line in f.read().strip().split("\n")]


def validate_line(line: list) -> bool:
    # Returns first location where there is an issue, or -1 if its valid
    diff_range = (1, 3) if line[1] > line[0] else (-3, -1)
    for i in range(len(line) - 1):
        if (
            line[i + 1] - line[i] < diff_range[0]
            or line[i + 1] - line[i] > diff_range[1]
        ):
            return i
    return -1


p1 = 0
for line in lines:
    if validate_line(line) == -1:
        p1 += 1

print("Part 1:", p1)

p2 = 0
for line in lines:
    ans = validate_line(line)
    if ans == -1:
        p2 += 1
    elif (  # Check neighborhood of the problem
        validate_line(line[:ans] + line[ans + 1 :]) == -1
        or validate_line(line[: ans + 1] + line[ans + 2 :]) == -1
        or validate_line(line[: ans - 1] + line[ans:]) == -1
    ):
        p2 += 1

print("Part 2:", p2)
