# Written by Josh Yeaton on 1/18/24
# For Advent of Code 2024

import collections

def create_grid(grid, time, f):
    for r in range(0, rows):
        for c in range(0, cols):
            grid.update({(r,c):'.'})

    for r in range(-1, rows + 1):
        grid.update({(r,-1):'O'})
        grid.update({(r, cols):'O'})

    for c in range(-1, cols + 1):
        grid.update({(-1, c):'O'})
        grid.update({(rows, c):'O'})

    for i in range(time):
        l = f.readline().strip().split(',')
        r = int(l[1])
        c = int(l[0])
        grid.update({(r, c):'#'})

def update_grid(grid, f, point_arr):
    l = f.readline().strip().split(',')
    r = int(l[1])
    c = int(l[0])
    grid.update({(r, c):'#'})
    point_arr.append((str(c) + ',' + str(r)))


def find_goal(start, goal, grid):
    cur_dist = 0
    visited = {}
    cur_level = collections.deque([start])
    next_level = collections.deque()
    while (True):
        while (len(cur_level) > 0):
            cur_loc = cur_level.popleft()
            if (cur_loc == goal):
                return cur_dist
            up = (cur_loc[0] - 1, cur_loc[1])
            right = (cur_loc[0], cur_loc[1] + 1)
            down = (cur_loc[0] + 1, cur_loc[1])
            left = (cur_loc[0], cur_loc[1] - 1)
            to_check = [up, right, down, left]

            for check_loc in to_check:
                if (grid.get(check_loc) == '.' and visited.get(check_loc) == None):
                    next_level.append(check_loc)
                visited.update({check_loc:True})
        if (len(next_level) == 0):
            break
        cur_level = next_level
        next_level = collections.deque()
        cur_dist += 1
    return 0

def find_goal_pt2(start, goal, grid):
    cur_dist = 0
    visited = {}
    cur_level = collections.deque([start])
    next_level = collections.deque()
    while (True):
        while (len(cur_level) > 0):
            cur_loc = cur_level.popleft()
            if (cur_loc == goal):
                return True
            up = (cur_loc[0] - 1, cur_loc[1])
            right = (cur_loc[0], cur_loc[1] + 1)
            down = (cur_loc[0] + 1, cur_loc[1])
            left = (cur_loc[0], cur_loc[1] - 1)
            to_check = [up, right, down, left]

            for check_loc in to_check:
                if (grid.get(check_loc) == '.' and visited.get(check_loc) == None):
                    next_level.append(check_loc)
                visited.update({check_loc:True})
        if (len(next_level) == 0):
            return False
        cur_level = next_level
        next_level = collections.deque()
        cur_dist += 1        

if __name__ == "__main__":
    filename = 'data_test.txt'
    rows = 7
    cols = 7
    time = 12
    filename = 'data.txt'
    rows = 71
    cols = 71
    time = 1024

    f = open(filename)

    start = (0,0)
    goal = (rows - 1, cols -1)

    grid = {}
    create_grid(grid, time, f)

    print(find_goal(start, goal, grid))

    # for r in range(-1, rows + 1):
    #     for c in range(-1, cols + 1):
    #         print(grid.get((r,c)), end='')
    #     print()


    point_arr = []
    while (find_goal_pt2(start, goal, grid)):
        update_grid(grid, f, point_arr)
    print(point_arr[-1])


    f.close()

    
    