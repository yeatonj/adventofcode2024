# Written by Josh Yeaton on 1/13/24
# For Advent of Code 2024

import numpy as np

def score_pt1(a_moves, b_moves, goal):
    min_tokens = 0
    for a_presses in range(1, 101):
        for b_presses in range(1, 101):
            x_total = a_moves[0] * a_presses + b_moves[0] * b_presses
            y_total = a_moves[1] * a_presses + b_moves[1] * b_presses
            if (x_total == goal[0] and y_total == goal[1]):
                tokens_spent = 3 * a_presses + b_presses
                if (min_tokens == 0 or min_tokens > tokens_spent):
                    min_tokens = tokens_spent
    return min_tokens

def score_pt2(a_moves, b_moves, goal):
    ans = 0
    a = np.array([[a_moves[0], b_moves[0]], [a_moves[1], b_moves[1]]])
    b = np.array([goal[0], goal[1]])
    x = np.linalg.solve(a, b)
    # check vals with ints
    a_presses = int(np.round(x[0]))
    b_presses = int(np.round(x[1]))
    if ((a_presses * a_moves[0] + b_presses * b_moves[0] == goal[0]) and 
        (a_presses * a_moves[1] + b_presses * b_moves[1] == goal[1]) and
        (a_presses > 0) and
        (b_presses > 0)):
        ans = (3*a_presses + b_presses)
    return ans
                


if __name__ == "__main__":
    f = open('data.txt')

    a_buttons = []
    b_buttons = []
    prize_locs = []

    for l in f:
        if ('A' in l):
            l = l.strip().split(',')
            x = int(l[0].split('+')[1])
            y = int(l[1].split('+')[1])
            a_buttons.append((x,y))
        elif ('B' in l):
            l = l.strip().split(',')
            x = int(l[0].split('+')[1])
            y = int(l[1].split('+')[1])
            b_buttons.append((x,y))
        elif ('P' in l):
            l = l.strip().split(',')
            x = int(l[0].split('=')[1])
            y = int(l[1].split('=')[1])
            prize_locs.append((x,y))

    f.close()

    total_pt1 = 0
    pt2_prize_locs = []
    for i in range(len(a_buttons)):
        total_pt1 += score_pt1(a_buttons[i], b_buttons[i], prize_locs[i])
        pt2_prize_locs.append((prize_locs[i][0] + 10000000000000, prize_locs[i][1] + 10000000000000))
        
    print(total_pt1)


    total_pt2 = 0
    for i in range(len(a_buttons)):
        total_pt2 += score_pt2(a_buttons[i], b_buttons[i], pt2_prize_locs[i])

    print(total_pt2)