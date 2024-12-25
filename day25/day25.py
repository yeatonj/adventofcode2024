# Written by Josh Yeaton on 1/25/24
# For Advent of Code 2024


if __name__ == "__main__":
    filename = 'data_test.txt'
    filename = 'data.txt'

    f = open(filename)

    keys = []
    locks = []
    
    new_iter = True
    cur_key = False
    cur_lock = False
    for l in f:
        l = l.strip()
        if (l == ''):
            if (cur_key):
                keys.append(temp)
            else:
                locks.append(temp)
            new_iter = True
            cur_key = False
            cur_lock = False
        else:
            if (new_iter == True):
                if ('#' in l):
                    cur_lock = True
                    temp = [-1,-1,-1,-1,-1]
                else:
                    cur_key = True
                    temp = [-1,-1,-1,-1,-1]
                new_iter = False
            for i in range(len(l)):
                if (l[i] == '#'):
                    temp[i] += 1
    if (cur_key):
        keys.append(temp)
    else:
        locks.append(temp)

    f.close()


    pt1_soln = 0
    for key in keys:
        for lock in locks:
            found_error = False
            for i in range(len(key)):
                if (key[i] + lock[i] > 5):
                    found_error = True
                    continue
            if not found_error:
                pt1_soln += 1

    print(pt1_soln)




    