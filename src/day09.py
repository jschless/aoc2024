# fname = "./examples/day09.txt"
fname = "./inputs/day09.txt"


with open(fname) as f:
    files, files_2, free, to_add = [], [], [], []
    flag = True
    f_id = 0
    for x in f.read().strip():
        if flag:
            to_add.append((f_id, int(x)))
            files_2 += [len(files)] * int(x)
            files.append(int(x))
            f_id += 1
        else:
            to_add.append((-1, int(x)))
            free.append(int(x))
        flag = not flag

n_files = len(files_2)
new_ans = []

for file_id, size in enumerate(files):
    new_ans += [file_id] * size
    if file_id < len(free):
        for _ in range(free[file_id]):
            new_ans.append(files_2.pop())


to_add_2 = [x for x in to_add]
# ans = []
# while len(to_add) > 0:
#     f_id, size = to_add.pop(0)
#     if f_id == -1:
#         # fill gap with items from the end
#         gap_size = size
#         while gap_size > 0:
#             f_id_end, size_end = to_add.pop()
#             if f_id_end == -1:
#                 # skip gaps
#                 continue
#             if size_end > size:
#                 ans += [f_id_end] * gap_size
#                 to_add.append((f_id_end, (size_end - gap_size)))
#                 # add remainder back to end
#                 gap_size = 0
#             else:
#                 ans += [f_id_end] * size_end
#                 gap_size -= size_end
#     else:
#         ans += [f_id] * size


p1, p2 = 0, 0
# print(new_ans)
for i, x in enumerate(new_ans[:n_files]):
    p1 += i * x


def find_and_replace(files, space_avail):
    # Returns the item to insert + a new list with the item replaced by a gap
    i_to_replace = -1
    to_insert = None
    for i, (file_id, size) in list(enumerate(files))[::-1]:
        if size <= space_avail and file_id != -1:
            i_to_replace = i
            to_insert = (file_id, size)
            break

    if i_to_replace != -1:
        files[i] = (-1, to_insert[1])
    return to_insert


ans_2 = []
while len(to_add_2) > 0:
    f_id, size = to_add_2.pop(0)
    if f_id == -1:
        # fill gap with items from the end
        gap_size = size
        while gap_size > 0:
            to_insert = find_and_replace(to_add_2, gap_size)
            if to_insert:
                f_id_end, size_end = to_insert
                ans_2 += [f_id_end] * size_end
                gap_size -= size_end
            else:  # no candidates, fill remainder with -1
                ans_2 += [-1] * gap_size
                gap_size = 0

    else:
        ans_2 += [f_id] * size


for i, x in enumerate(ans_2):
    if x != -1:
        p2 += i * x

print("Part 1:", p1)

print("Part 2:", p2)
