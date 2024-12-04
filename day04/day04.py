# Written by Josh Yeaton on 1/4/24
# For Advent of Code 2024

WORD_LEN = 4
TARGET = 'XMAS'

def check_loc(dic, row, col, max_r, max_c):
    found = 0
    up_ok = False
    down_ok = False
    if (row >= (WORD_LEN - 1)):
        found += check_up(dic, row, col)
        up_ok = True
    if ((row + WORD_LEN) <= max_r):
        found += check_down(dic, row, col)
        down_ok = True
    if (col >= (WORD_LEN - 1)):
        found += check_left(dic, row, col)
        if (up_ok):
            found += check_up_left(dic, row, col)
        if (down_ok):
            found += check_down_left(dic, row, col)
    if ((col + WORD_LEN) <= max_c):
        found += check_right(dic, row, col)
        if (up_ok):
            found += check_up_right(dic, row, col)
        if (down_ok):
            found += check_down_right(dic, row, col)
    
    return found

def check_up(dic, row, col):
    actual = ''
    for i in range(WORD_LEN):
        actual += dic.get((row - i, col))
    return actual == TARGET

def check_right(dic, row, col):
    actual = ''
    for i in range(WORD_LEN):
        actual += dic.get((row, col + i))
    return actual == TARGET

def check_down(dic, row, col):
    actual = ''
    for i in range(WORD_LEN):
        actual += dic.get((row + i, col))
    return actual == TARGET

def check_left(dic, row, col):
    actual = ''
    for i in range(WORD_LEN):
        actual += dic.get((row, col - i))
    return actual == TARGET

def check_up_right(dic, row, col):
    actual = ''
    for i in range(WORD_LEN):
        actual += dic.get((row - i, col + i))
    return actual == TARGET

def check_up_left(dic, row, col):
    actual = ''
    for i in range(WORD_LEN):
        actual += dic.get((row - i, col - i))
    return actual == TARGET

def check_down_right(dic, row, col):
    actual = ''
    for i in range(WORD_LEN):
        actual += dic.get((row + i, col + i))
    return actual == TARGET

def check_down_left(dic, row, col):
    actual = ''
    for i in range(WORD_LEN):
        actual += dic.get((row + i, col - i))
    return actual == TARGET

def check_loc_pt2(dic, row, col, max_r, max_c):
    if ((row < 1) or (col < 1) or (row > (max_r - 2) or (col > max_c - 2))):
        return 0
    diag_1 = ''
    diag_2 = ''
    for i in [-1, 0, 1]:
        diag_1 += dic.get((row + i, col + i))
        diag_2 += dic.get((row + i, col - i))
    if (((diag_1 == 'MAS') or (diag_1 == 'SAM')) and ((diag_2 == 'MAS') or (diag_2 == 'SAM'))):
        return 1
    return 0


f = open('data.txt')

letter_dic = {}

r = 0

for l in f:
    l = l.strip()
    c = 0
    for char in l:
        letter_dic.update({(r,c):char})
        c += 1
    r += 1

max_r = r
max_c = c

total_pt1 = 0
total_pt2 = 0

for i in range(max_r):
    for j in range(max_c):
        letter = letter_dic.get((i, j))
        if (letter == 'X'):
            total_pt1 += check_loc(letter_dic, i, j, max_r, max_c)
        elif (letter == 'A'):
            total_pt2 += check_loc_pt2(letter_dic, i, j, max_r, max_c)



print(total_pt1)
# 2462 is the right answer

print(total_pt2)




f.close()