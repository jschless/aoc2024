from tqdm import tqdm

# fname = "./examples/day14.txt"
fname = "./inputs/day14.txt"


with open(fname) as f:
    robots = []
    for rob in f.read().strip().split("\n"):
        p, v = rob.split(" ")

        x, y = map(int, p[p.find("=") + 1 :].split(","))
        dx, dy = map(int, v[v.find("=") + 1 :].split(","))

        robots.append(((y, x), (dy, dx)))

# HT, WD = 7, 11
HT, WD = 103, 101


def make_move(pos, vel):
    return ((pos[0] + vel[0]) % HT, (pos[1] + vel[1]) % WD)


def print_robots(r):
    s = {x[0] for x in r}
    st = ""
    for i in range(HT):
        for j in range(WD):
            if (i, j) in s:
                st += "#"
            else:
                st += " "
        st += "\n"
    st += "#" * WD
    st += "#" * WD
    st += "#" * WD

    print(st)


def check_line(robots):
    # looks for line of length N in robot list
    locs = {l for l, _ in robots}
    N = 8
    for r, _ in robots:
        for i in range(N):
            if (r[0], r[1] + i) not in locs:
                break
            if i == N - 1:
                return True
    return False


def make_score(robots):
    q_counts = [0, 0, 0, 0]
    H1 = (HT - 1) / 2
    W1 = (WD - 1) / 2
    for p, _ in robots:
        if p[0] < H1 and p[1] < W1:
            q_counts[0] += 1
        elif p[0] < H1 and p[1] > W1:
            q_counts[1] += 1
        elif p[0] > H1 and p[1] > W1:
            q_counts[2] += 1
        elif p[0] > H1 and p[1] < W1:
            q_counts[3] += 1

    return q_counts[0] * q_counts[1] * q_counts[2] * q_counts[3]


p1, p2 = 0, 0
for x in tqdm(range(100_000)):
    for i in range(len(robots)):
        p, v = robots[i]
        p = make_move(p, v)
        robots[i] = (p, v)
    if x == 99:
        p1 = make_score(robots)
    if check_line(robots):
        print_robots(robots)
        p2 = x + 1
        break

print("Part 1:", p1)
print("Part 2:", p2)
