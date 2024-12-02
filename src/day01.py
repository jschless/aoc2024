from collections import Counter

fname = "./inputs/day01.txt"

with open(fname) as f:
    l1, l2 = map(list, zip(*(map(int, line.split()) for line in f)))

print("Part 1:", sum(abs(x - y) for x, y in zip(sorted(l1), sorted(l2))))


c = Counter(l2)
print("Part 2:", sum((x * c.get(x, 0) for x in l1)))
