# fname = "./examples/day07.txt"
fname = "./inputs/day07.txt"

totals, ops = [], []
with open(fname) as f:
    for line in f.read().strip().split("\n"):
        total, op = line.split(":")
        totals.append(int(total))
        ops.append([int(x) for x in op.strip().split(" ")])


def test_ops(li, tot, acc, p2):
    if len(li) == 0:
        return tot == acc
    else:
        return (
            test_ops(li[1:], tot, li[0] * acc, p2)
            or test_ops(li[1:], tot, li[0] + acc, p2)
            or (p2 and test_ops(li[1:], tot, int(str(acc) + str(li[0])), p2))
        )


p1, p2 = 0, 0
for tot, op in zip(totals, ops):
    if test_ops(op[1:], tot, op[0], False):
        p1 += tot
    if test_ops(op[1:], tot, op[0], True):
        p2 += tot

print("Part 1:", p1)
print("Part 2:", p2)
