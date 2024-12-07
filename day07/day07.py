# Written by Josh Yeaton on 1/7/24
# For Advent of Code 2024


def check_pt1(target, val_arr):
    if (len(val_arr) == 1):
        if (val_arr[0] == target):
            return True
        else:
            return False
    orig_first_val = val_arr[0]
    orig_second_val = val_arr[1]
    val_arr[1] += val_arr[0]
    if (check_pt1(target, val_arr[1:])):
        return True
    val_arr[1] = orig_first_val * orig_second_val
    if (check_pt1(target, val_arr[1:])):
        return True
    val_arr[0] = orig_first_val
    val_arr[1] = orig_second_val
    return False

def check_pt2(target, val_arr):
    if (len(val_arr) == 1):
        if (val_arr[0] == target):
            return True
        else:
            return False
    orig_second_val = val_arr[1]
    val_arr[1] += val_arr[0]
    if (check_pt2(target, val_arr[1:])):
        return True
    val_arr[1] = val_arr[0] * orig_second_val
    if (check_pt2(target, val_arr[1:])):
        return True
    val_arr[1] = int(str(val_arr[0]) + str(orig_second_val))
    if (check_pt2(target, val_arr[1:])):
        return True
    val_arr[1] = orig_second_val
    return False

if __name__ == "__main__":
    f = open('data.txt')

    targets = []
    vals = []

    for l in f:
        l = l.strip().split(': ')
        targets.append(int(l[0]))
        nums = l[1].split()
        vals.append([int(i) for i in nums])
    f.close()

    pt1_total = 0
    pt2_subtotal = 0
    for i in range(len(targets)):
        if (check_pt1(targets[i], vals[i])):
            pt1_total += targets[i]
        elif (check_pt2(targets[i], vals[i])):
            pt2_subtotal += targets[i]

    print(pt1_total)
    print(pt1_total + pt2_subtotal)
