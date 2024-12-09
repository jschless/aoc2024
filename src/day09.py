# fname = "./examples/day09.txt"
fname = "./inputs/day09.txt"

with open(fname) as f:
    to_add = []
    flag = True
    f_id = 0
    for x in f.read().strip():
        to_add.append((f_id if flag else -1, int(x)))
        f_id += 1 if flag else 0
        flag = not flag


to_add_2 = [x for x in to_add]
p1, p2 = 0, 0
index = 0
while len(to_add) > 0:
    f_id, size = to_add.pop(0)
    if f_id == -1:
        # fill gap with items from the end
        gap_size = size
        while gap_size > 0:
            f_id_end, size_end = to_add.pop()
            if f_id_end == -1:
                # skip gaps
                continue
            elif size_end > gap_size:
                for i in range(gap_size):
                    p1 += f_id_end * index
                    index += 1
                to_add.append((f_id_end, (size_end - gap_size)))
                # add remainder back to end
                gap_size = 0
            else:
                for i in range(size_end):
                    p1 += f_id_end * index
                    index += 1
                gap_size -= size_end
    else:
        for i in range(size):
            p1 += f_id * index
            index += 1

print("Part 1:", p1)


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


index = 0
while len(to_add_2) > 0:
    f_id, size = to_add_2.pop(0)
    if f_id == -1:
        # fill gap with items from the end
        gap_size = size
        while gap_size > 0:
            to_insert = find_and_replace(to_add_2, gap_size)
            if to_insert:
                f_id_end, size_end = to_insert
                for i in range(size_end):
                    p2 += index * f_id_end
                    index += 1
                gap_size -= size_end
            else:
                index += gap_size  # don't need to add to total
                gap_size = 0

    else:
        for i in range(size):
            p2 += index * f_id
            index += 1

print("Part 1:", p1)

print("Part 2:", p2)
