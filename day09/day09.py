# Written by Josh Yeaton on 1/9/24
# For Advent of Code 2024

def compact(orig_data):
    data = []
    for element in orig_data:
        data.append(element)

    head = 0
    while(data[head] != '.'):
        head += 1
    tail = len(data) - 1
    while(data[tail] == '.'):
        tail -= 1

    while (head < tail):
        data[head] = data[tail]
        data[tail] = '.'
        head += 1
        tail -= 1

        while(data[head] != '.' and head < tail):
            head += 1

        while(data[tail] == '.' and head < tail):
            tail -= 1
    return data

def find_checksum(data):
    i = 0
    total = 0
    for i in range(len(data)):
        if (data[i] != '.'):
            total += i * data[i]
    return total

def compact_pt2(data):
    # Find free space, starting from front
    # [(start index, blocks free), ... ()]
    free_space_list = []
    i = 0
    while (i < len(data)):
        if (data[i] != '.'):
            i += 1
            continue
        start_ind = i
        space_len = 0
        while (i < len(data) and data[i] == '.'):
            space_len += 1
            i += 1
        free_space_list.append([start_ind, space_len])


    # Find blocks, starting from back
    # [(start index, blocks used), ... ()]
    block_list = []
    i = len(data) - 1
    while (i >= 0):
        if (data[i] == '.'):
            i -= 1
            continue
        data_len = 0
        data_id = data[i]
        while (i >=0 and data[i] != '.' and data[i] == data_id):
            data_len += 1
            i -= 1
        block_list.append([i + 1, data_len])

    for block in block_list:
        for i in range(len(free_space_list)):
            if (free_space_list[i][0] > block[0]):
                break
            if (block[1] <= free_space_list[i][1]):
                # move this block into this free space
                for j in range(block[1]):
                    from_ind = j + block[0]
                    to_ind = j + free_space_list[i][0]
                    data[to_ind] = data[from_ind]
                    data[from_ind] = '.'
                # adjust free space list
                free_space_list[i][0] += block[1]
                free_space_list[i][1] -= block[1]
                break
    return data


if __name__ == "__main__":
    f = open('data.txt')

    data = f.readline()
    data = data.strip()

    actual_data = []

    block_id = 0

    for i in range(len(data)):
        size = int(data[i])
        if (i % 2 == 0):
            for j in range(size):
                actual_data.append(block_id)
            block_id += 1
        else:
            for j in range(size):
                actual_data.append('.')

    pt1_compacted = compact(actual_data)
    pt1 = find_checksum(pt1_compacted)
    print(pt1)

    pt2_compacted = compact_pt2(actual_data)
    pt2 = find_checksum(pt2_compacted)
    print(pt2)


    f.close()