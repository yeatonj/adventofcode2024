# Written by Josh Yeaton on 1/2/24
# For Advent of Code 2024

def check_line_pt1(line_arr):
    if (line_arr[0] > line_arr[-1]):
        for i in range(len(line_arr) - 1):
            diff = line_arr[i] - line_arr[i + 1]
            if ((diff > 3) or (diff < 1)):
                return False
    else:
        for i in range(len(line_arr) - 1):
            diff = line_arr[i] - line_arr[i + 1]
            if ((diff < -3) or (diff > -1)):
                return False
    return True

def check_line_pt2(line_arr):
    if (check_line_pt1(line_arr[1:]) or check_line_pt1(line_arr[:-1])):
        return True
    return helper_pt2(line_arr, False)
            
def helper_pt2(line_arr, skipped):
    if (line_arr[0] > line_arr[-1]):
        for i in range(len(line_arr) - 1):
            diff = line_arr[i] - line_arr[i + 1]
            if ((diff > 3) or (diff < 1)):
                if (skipped):
                    return False
                else:
                    # remove and check with left index
                    if (i == 0):
                        left_arr = line_arr[1:]
                    else:
                        left_arr = line_arr[0:i] + line_arr[i+1:]
                    # remove and check with right index
                    if (i + 2 == len(line_arr)):
                        right_arr = line_arr[:-1]
                    else:
                        right_arr = line_arr[0:i+1] + line_arr[i+2:]
                return (helper_pt2(left_arr, True) or helper_pt2(right_arr, True))
    else:
        for i in range(len(line_arr) - 1):
            diff = line_arr[i] - line_arr[i + 1]
            if ((diff < -3) or (diff > -1)):
                if (skipped):
                    return False
                else:
                    # remove and check with left index
                    if (i == 0):
                        left_arr = line_arr[1:]
                    else:
                        left_arr = line_arr[0:i] + line_arr[i+1:]
                    # remove and check with right index
                    if (i + 2 == len(line_arr)):
                        right_arr = line_arr[:-1]
                    else:
                        right_arr = line_arr[0:i+1] + line_arr[i+2:]
                return (helper_pt2(left_arr, True) or helper_pt2(right_arr, True))
    return True


if __name__ == "__main__":
    data = open("data.txt")

    total = 0
    total_pt2 = 0

    for line in data:
        int_arr = []
        line_array = line.strip().split()
        for num in line_array:
            int_arr.append(int(num))
        if (check_line_pt1(int_arr)):
            total += 1
        if (check_line_pt2(int_arr)):
            total_pt2 += 1

    print(total)
    print(total_pt2)
    
    data.close()

