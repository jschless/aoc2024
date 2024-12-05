from collections import defaultdict

# fname = "./examples/day05.txt"
fname = "./inputs/day05.txt"

with open(fname) as f:
    ordering, updates = tuple(f.read().split("\n\n"))

gt = defaultdict(list)
for rules in ordering.split():
    before, after = tuple(map(int, rules.split("|")))
    gt[before].append(after)


def find_insert_loc(cur_update, pg, reorder):
    for i, pg2 in enumerate(cur_update):
        if pg2 in reorder:
            return i
    return -1


def validate_update(update, p1):
    update = [int(x) for x in update.strip().split(",")]
    seen = set()
    corrected_update = []
    broken = False
    for length, pg in enumerate(update):
        for after in gt[pg]:
            if after in seen:  # this should have come before
                broken = True
                if p1:
                    return 0
                corrected_update.insert(
                    find_insert_loc(corrected_update, pg, gt[pg]), pg
                )
                break

        seen.add(pg)
        if len(corrected_update) == length:
            corrected_update.append(pg)

    if p1:
        return update[int(len(update) / 2)]
    elif broken:
        return corrected_update[int(len(update) / 2)]
    else:
        return 0


p1, p2 = 0, 0
for update in updates.split():
    p1 += validate_update(update, True)
    p2 += validate_update(update, False)


print("Part 1:", p1)
print("Part 2:", p2)
