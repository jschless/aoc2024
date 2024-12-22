from math import floor
from collections import defaultdict, deque

# fname = "./examples/day22.txt"
fname = "./inputs/day22.txt"
nums = list(map(int, open(fname).read().strip().split()))


def next_num(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(floor(secret / 32), secret))
    return prune(mix(secret * 2048, secret))


def mix(n, secret):
    return n ^ secret


def prune(secret):
    return secret % 16777216


p1 = 0
counts = defaultdict(int)
for secret in nums:
    seq = deque()
    seen = set()
    last_first = int(str(secret)[-1])
    for i in range(2000):
        secret = next_num(secret)
        first_dig = int(str(secret)[-1])
        seq.append(first_dig - last_first)
        if len(seq) == 5:
            seq.popleft()

        if len(seq) == 4 and tuple(seq) not in seen:
            seen.add(tuple(seq))
            counts[tuple(seq)] += first_dig

        last_first = first_dig

    p1 += secret

print("Part 1:", p1)
print("Part 2:", max([x for _, x in counts.items()]))
