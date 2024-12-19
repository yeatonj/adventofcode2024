# Written by Josh Yeaton on 1/19/24
# For Advent of Code 2024

def recursive_find_match(t, patterns):
    if (t == ''):
        return True
    for p in patterns:
        if (len(p) > len(t)):
            continue
        elif (t[:len(p)] == p):
            if (recursive_find_match(t[len(p):], patterns)):
                return True
    return False

def rec_pt2(t, patterns, memo_dic):
    if (memo_dic.get(t) != None):
        return memo_dic.get(t)
    if (t == ''):
        return 1
    subtotal = 0
    for p in patterns:
        if (len(p) > len(t)):
            continue
        elif (t[:len(p)] == p):
            subtotal += rec_pt2(t[len(p):], patterns, memo_dic)
    memo_dic.update({t:subtotal})
    return subtotal
    

def pt1(patterns, towels):
    total = 0
    for t in towels:
        if (recursive_find_match(t, patterns)):
            total += 1
    return total

def pt2(patterns, towels):
    total = 0
    memo_dic = {}
    for t in towels:
        total += rec_pt2(t, patterns, memo_dic)
    return total

if __name__ == "__main__":
    filename = 'data_test.txt'
    filename = 'data.txt'

    f = open(filename)
    patterns = f.readline().strip().split(', ')
    f.readline()
    towels = []
    for l in f:
        towels.append(l.strip())
    f = f.close()

    print(pt1(patterns, towels))

    # 781 too low
    print(pt2(patterns, towels))