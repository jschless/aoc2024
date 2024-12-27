from collections import deque

# fname = "./examples/day24.txt"
fname = "./inputs/day24.txt"
regs, gates = open(fname).read().strip().split("\n\n")
registers = {}
for line in regs.strip().split("\n"):
    k, v = line.split(": ")
    registers[k] = True if v == "1" else False

# would be nice to sort the gates before solving so it happens in one pass, but can just brute force it

ops = deque()
for line in gates.split("\n"):
    inst1, op, inst2, _, out = line.split()
    ops.append((op, inst1, inst2, out))


def do_op(op, inst1, inst2):
    if op == "AND":
        return registers[inst1] and registers[inst2]
    elif op == "OR":
        return registers[inst1] or registers[inst2]
    elif op == "XOR":
        return registers[inst1] ^ registers[inst2]


while ops:
    op, inst1, inst2, out = ops.popleft()
    if inst1 in registers and inst2 in registers:
        registers[out] = do_op(op, inst1, inst2)
    else:
        ops.append((op, inst1, inst2, out))


# Part 2. There are 222 gates, so can't brute force duh
def sum_bin(prefix, length):
    ans = 0
    for i in range(0, length + 1):
        if registers.get(f"{prefix}{i:02}", False) == True:
            ans += 2**i
    return ans


def find_diff(length):
    mistakes = []
    for i in range(0, length + 1):
        if registers.get(f"x{i:02}", False) ^ registers.get(
            f"y{i:02}", False
        ) != registers.get(f"z{i:02}", False):
            mistakes.append(f"z{i:02}")
    return mistakes


# Approach:
# 1. Find messed up output
# 2. Figure out outputs that lead to that messed up output
sus_gates = set(find_diff(44))
for line in gates.split("\n"):
    inst1, op, inst2, _, out = line.split()
    if out in sus_gates:
        if not inst1.startswith("x") and not inst1.startswith("y"):
            sus_gates.add(inst1)
        if not inst2.startswith("x") and not inst2.startswith("y"):
            sus_gates.add(inst2)

print(len(sus_gates))
for line in gates.split("\n"):
    inst1, op, inst2, _, out = line.split()
    if out in sus_gates:
        if not inst1.startswith("x") and not inst1.startswith("y"):
            sus_gates.add(inst1)
        if not inst2.startswith("x") and not inst2.startswith("y"):
            sus_gates.add(inst2)

print(len(sus_gates))
for line in gates.split("\n"):
    inst1, op, inst2, _, out = line.split()
    if out in sus_gates:
        if not inst1.startswith("x") and not inst1.startswith("y"):
            sus_gates.add(inst1)
        if not inst2.startswith("x") and not inst2.startswith("y"):
            sus_gates.add(inst2)

print(len(sus_gates))
# print(sus_gates)
print("Part 1:", sum_bin("z", 45))
print(sum_bin("x", 44))
print(sum_bin("y", 44))
print(sum_bin("x", 44) + sum_bin("y", 44), sum_bin("z", 45))
