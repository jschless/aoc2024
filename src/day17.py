# fname = "./examples/day17.txt"
fname = "./inputs/day17.txt"

with open(fname) as f:
    registers, instrs = f.read().strip().split("\n\n")
    registers = {
        r.split(":")[0][-1]: int(r.split(": ")[1]) for r in registers.split("\n")
    }
    instrs = instrs.split(": ")[1]
    instrs = [int(x) for x in instrs.split(",")]


def combo(oper):
    if oper == 4:
        return registers["A"]
    if oper == 5:
        return registers["B"]
    if oper == 6:
        return registers["C"]
    return oper


def do_op(inst, lit_op):
    global ip
    combo_op = combo(lit_op)
    if inst == 0:
        num = registers["A"]
        den = 2**combo_op
        registers["A"] = int(num / den)
    elif inst == 1:
        registers["B"] = registers["B"] ^ lit_op
    elif inst == 2:
        registers["B"] = combo_op % 8
    elif inst == 3:
        if registers["A"] != 0:
            # print(f"Setting {ip} to {lit_op-2}")
            ip = lit_op - 2
    elif inst == 4:
        registers["B"] = registers["B"] ^ registers["C"]
    elif inst == 5:
        return combo_op % 8
    elif inst == 6:
        num = registers["A"]
        den = 2**combo_op
        registers["B"] = int(num / den)
    elif inst == 7:
        num = registers["A"]
        den = 2**combo_op
        registers["C"] = int(num / den)
    return None


# Examples
# 1.
# registers = {"A": 0, "B": 0, "C": 9}
# instrs = [2, 6]
# 2
# registers = {"A": 10, "B": 0, "C": 0}
# instrs = [5, 0, 5, 1, 5, 4]
# 3.
# registers = {"A": 2024, "B": 0, "C": 0}
# instrs = [0, 1, 5, 4, 3, 0]
# P2:R
# registers = {"A": 2024, "B": 0, "C": 0}
# instrs = [0, 3, 5, 4, 3, 0]

ip = 0


memo = {}


def run_instructions(instrs, p2=False):
    global ip
    ip = 0
    outs = []
    while ip < len(instrs):
        # if (registers["A"], registers["B"], registers["C"], ip) in memo:
        # return memo[(registers["A"], registers["B"], registers["C"], ip)]
        inst, op = instrs[ip], instrs[ip + 1]
        ans = do_op(inst, op)
        if ans is not None:
            outs.append(ans)
            if p2 and outs[len(outs) - 1] != instrs[len(outs) - 1]:
                # memo[(registers["A"], registers["B"], registers["C"], ip)] = []
                # end early
                return []
        ip += 2
    return outs


og_registers = {k: v for k, v in registers.items()}

print("Part 1:", ",".join([str(x) for x in run_instructions(instrs)]))

from tqdm import tqdm

# brute force checkpitn: 158760830
# 44_895_377_610
start = 158760830
for guess in tqdm(range(start, 100_000_000_000)):
    registers = {k: v for k, v in og_registers.items()}
    registers["A"] = guess
    out = run_instructions(instrs, p2=True)
    if instrs == out:
        print("Part 2:", guess)
        break
print(registers, instrs)

# Part 2 reasoning:
# Could do a memoization thing, bc the output is determined based on (A, B, C, ip)
# Which instructions involve A?
