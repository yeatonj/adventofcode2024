# Written by Josh Yeaton on 1/11/24
# For Advent of Code 2024

def blink(arr_in):
    arr_out = []
    for num in arr_in:
        if (num == 0):
            arr_out.append(1)
        elif (len(str(num)) % 2 == 0):
            num_str = str(num)
            half_len = len(num_str) // 2
            arr_out.append(int(num_str[0:half_len]))
            arr_out.append(int(num_str[half_len:]))
        else:
            arr_out.append(num * 2024)
    return arr_out

def blink2(num_in, target_depth, cur_depth, seen):
    poss_ans = seen.get((num_in, cur_depth))
    # memoization
    if (poss_ans != None):
        return poss_ans
    # base case
    if (target_depth == cur_depth):
        seen.update({(num_in, cur_depth):1})
        return 1
        
    if (num_in == 0):
        ans = blink2(1, target_depth, cur_depth + 1, seen)
    elif (len(str(num_in)) % 2 == 0):
        num_str = str(num_in)
        half_len = len(num_str) // 2
        temp1 = int(num_str[0:half_len])
        temp2 = int(num_str[half_len:])

        ans = blink2(temp1, target_depth, cur_depth + 1, seen) + blink2(temp2, target_depth, cur_depth + 1, seen)
    else:
        ans = blink2(num_in * 2024, target_depth, cur_depth + 1, seen)
    seen.update({(num_in, cur_depth):ans})
    return ans



if __name__ == "__main__":
    f = open('data.txt')

    input = f.readline().strip()

    pt1_arr = [int(i) for i in input.split()]
    pt2_arr = [int(i) for i in input.split()]


    num_blinks = 25
    for i in range(num_blinks):
        pt1_arr = blink(pt1_arr)
    
    print(len(pt1_arr))

    num_blinks = 75
    seen = {}
    total = 0
    for num in pt2_arr:
        total  += blink2(num, num_blinks, 0, seen)

    print(total)

    f.close()