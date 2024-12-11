# fname = "./examples/day11.txt"
fname = "./inputs/day11.txt"

with open(fname) as f:
    stones = [int(x) for x in f.read().strip().split()]

memo = {}


def explore_number(x, i):
    s_x = str(x)
    len_s = len(s_x)
    ans = None
    if (x, i) in memo:
        return memo[(x, i)]

    if i == 0:
        return 1
    elif x == 0:
        ans = explore_number(1, i - 1)
    elif len_s % 2 == 0:
        ans = explore_number(int(s_x[: len_s // 2]), i - 1) + explore_number(
            int(s_x[len_s // 2 :]), i - 1
        )
    else:
        ans = explore_number(x * 2024, i - 1)

    memo[(x, i)] = ans
    return ans


p1 = 0
p2 = 0
for s in stones:
    p1 += explore_number(s, 25)
    p2 += explore_number(s, 75)

print("Part 1:", p1)
print("Part 2:", p2)
