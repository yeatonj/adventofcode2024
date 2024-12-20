# Written by Josh Yeaton on 1/20/24
# For Advent of Code 2024

# idea - 
# 1. shortest path from start to every point
# 2. shortest path from end to every point
# 3. remove walls and recalculate shortest path from start to the surrounding points and end to surrounding points
# 5. add them together and compare to the current path length, record savings

def find_paths(grid, start, goal, distance_dic):
    # Only one path according to problem statement...
    distance_dic.update({start:0})
    cur = start
    path_dist = 1
    while (cur != goal):
        up = (cur[0] - 1, cur[1])
        right = (cur[0], cur[1] + 1)
        down = (cur[0] + 1, cur[1])
        left = (cur[0], cur[1] - 1)
        poss = [up, right, down, left]
        for to_visit in poss:
            if ((distance_dic.get(to_visit) == None) and (grid.get(to_visit) != '#')):
                distance_dic.update({to_visit:path_dist})
                path_dist += 1
                cur = to_visit
                break
    return distance_dic.get(goal)

def get_cheat_points_pt1(grid, cur_loc):
    cheat_pts_temp = []
    # go straigh
    cheat_pts_temp.append((cur_loc[0] + 2, cur_loc[1]))
    cheat_pts_temp.append((cur_loc[0] - 2, cur_loc[1]))
    cheat_pts_temp.append((cur_loc[0], cur_loc[1] + 2))
    cheat_pts_temp.append((cur_loc[0], cur_loc[1] - 2))
    # go diagonal
    cheat_pts_temp.append((cur_loc[0] + 1, cur_loc[1] + 1))
    cheat_pts_temp.append((cur_loc[0] - 1, cur_loc[1] + 1))
    cheat_pts_temp.append((cur_loc[0] + 1, cur_loc[1] - 1))
    cheat_pts_temp.append((cur_loc[0] - 1, cur_loc[1] - 1))
    cheat_pts_final = []
    for loc in cheat_pts_temp:
        val = grid.get(loc)
        if ((val == None) or (val == '#')):
            continue
        cheat_pts_final.append(loc)
    return cheat_pts_final

def get_cheat_pts(grid, cur_loc, dist):
    # manhattan distance
    cheat_pts_temp = []
    start_row = cur_loc[0] - dist
    start_col = cur_loc[1] - dist
    end_row = cur_loc[0] + dist
    end_col = cur_loc[1] + dist
    for r in range(start_row, end_row + 1):
        for c in range(start_col, end_col + 1):
            # check manhattan dist
            man_dist = abs(cur_loc[0] - r) + abs(cur_loc[1] - c)
            if (man_dist > dist):
                continue
            cheat_pts_temp.append(((r,c), man_dist))
    cheat_pts_final = []
    for loc in cheat_pts_temp:
        val = grid.get(loc[0])
        if ((val == None) or (val == '#')):
            continue
        cheat_pts_final.append(loc)
    return cheat_pts_final


def find_cheats_pt1(grid, from_start, from_goal, rows, cols, orig_dist):
    cheats = {}
    for r in range(rows):
        for c in range(cols):
            cur_loc = (r,c)
            if (grid.get(cur_loc) == '#'):
                # we couldn't be here
                continue
            cur_dist = from_start.get(cur_loc)
            # find cheat points
            check_locs = get_cheat_points_pt1(grid, cur_loc)
            for loc in check_locs:
                cheat_dist = cur_dist + 2 + from_goal.get(loc)
                cheat_saved = orig_dist - cheat_dist
                if (cheat_saved > 0):
                    cheats.update({(cur_loc, loc):cheat_saved})
    return cheats

def find_cheats(grid, from_start, from_goal, rows, cols, orig_dist, manhattan_dist):
    cheats = {}
    for r in range(rows):
        for c in range(cols):
            cur_loc = (r,c)
            if (grid.get(cur_loc) == '#'):
                # we couldn't be here
                continue
            cur_dist = from_start.get(cur_loc)
            # find cheat points
            check_locs = get_cheat_pts(grid, cur_loc, manhattan_dist)
            for check_loc in check_locs:
                loc = check_loc[0]
                cheat_dist = cur_dist + check_loc[1] + from_goal.get(loc)
                cheat_saved = orig_dist - cheat_dist
                if (cheat_saved > 0):
                    cheats.update({(cur_loc, loc):cheat_saved})
    return cheats





if __name__ == "__main__":
    filename = 'data_test.txt'
    filename = 'data.txt'

    f = open(filename)

    grid = {}

    row = 0
    for l in f:
        col = 0
        l = l.strip()
        for c in l:
            if (c == 'S'):
                start = (row, col)
            elif (c == 'E'):
                goal = (row, col)
            grid.update({(row, col):c})
            col += 1
        row += 1

    f.close()

    max_row = row
    max_col = col

    dists_from_start = {}
    dists_from_goal = {}

    orig_dist = find_paths(grid, start, goal, dists_from_start)
    find_paths(grid, goal, start, dists_from_goal)

    # Part 1

    cheats = find_cheats_pt1(grid, dists_from_start, dists_from_goal, max_row, max_col, orig_dist)
    totals = {}
    for cheat in cheats:
        cheat_val = cheats.get(cheat)
        if (totals.get(cheat_val) == None):
            totals.update({cheat_val:0})
        totals.update({cheat_val:(totals.get(cheat_val) + 1)})

    pt1_ans = 0
    for savings in totals:
        if (savings >= 100):
            pt1_ans += totals.get(savings)

    print(pt1_ans)

    # Part 2

    cheats = find_cheats(grid, dists_from_start, dists_from_goal, max_row, max_col, orig_dist, 20)
    totals = {}
    for cheat in cheats:
        cheat_val = cheats.get(cheat)
        if (totals.get(cheat_val) == None):
            totals.update({cheat_val:0})
        totals.update({cheat_val:(totals.get(cheat_val) + 1)})

    pt1_ans = 0
    for savings in totals:
        if (savings >= 100):
            pt1_ans += totals.get(savings)

    print(pt1_ans)