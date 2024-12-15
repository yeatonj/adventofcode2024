# Written by Josh Yeaton on 1/14/24
# For Advent of Code 2024

# For test cases
N_ROWS = 7
N_COLS = 11
F_NAME = 'data_test.txt'
# For actual
N_ROWS = 103
N_COLS = 101
F_NAME = 'data.txt'

def move_bots(bot_arr, interval):
    for bot in bot_arr:
        bot[0] = (bot[0] + (bot[2] * interval)) % N_ROWS
        bot[1] = (bot[1] + (bot[3] * interval)) % N_COLS
    return

def calc_score(bot_arr):
    # quadrant 1: (0, N_COLS // 2 + 1) to (N_ROWS // 2 - 1, N_COLS // 2 + 1)
    # quadrant 2: (0, 0) to (N_ROWS // 2 - 1, N_COLS // 2 - 1)
    # quadrant 3: (N_ROWS // 2 + 1, 0) to (N_ROWS - 1, N_COLS // 2 - 1)
    # quadrant 4: (N_ROWS // 2 + 1, N_COLS // 2 + 1) to (N_ROWS - 1, N_COLS - 1)
    quad_totals = [0,0,0,0]
    for bot in bot_arr:
        if (bot[0] <= N_ROWS // 2 - 1):
            # Quadrant 1 or 2
            if (bot[1] <= N_COLS // 2 - 1):
                # Quadrant 2
                quad_totals[1] += 1
            elif (bot[1] >= N_COLS // 2 + 1):
                # Quadrant 1
                quad_totals[0] += 1
            # else, bot is between quadrants
        elif (bot[0] >= N_ROWS // 2 + 1):
            # Quadrant 3 or 4
            if (bot[1] <= N_COLS // 2 - 1):
                # Quadrant 3
                quad_totals[2] += 1
            elif (bot[1] >= N_COLS // 2 + 1):
                # Quadrant 4
                quad_totals[3] += 1
        # else, bot is between quadrants
    score = 1
    for q in quad_totals:
        score *= q
    return score

def check_mirror(cur_bots, mirror_col):
    # check to see if we are mirrored over the y-axis
    mirror_count_y = 0
    bot_locs = {}
    for bot in cur_bots:
        bot_locs.update({(bot[0], bot[1]):'1'})
    for bot in bot_locs:
        mirror_line_y = mirror_col
        if (bot[1] < mirror_line_y):
            # check to make sure there is a mirrored one
            diff = mirror_line_y - bot[1]
            mirror_coord = (bot[0], mirror_line_y + diff)
            if (bot_locs.get(mirror_coord) != None):
                mirror_count_y += 1
    return (mirror_count_y > 100)
    

def is_equal(cur_bots, new_bots, iteration):
    for i in range(len(cur_bots)):
        if (cur_bots[i] != new_bots[i]):
            return
    print('Found repeat at cycle ' + str(iteration))

if __name__ == "__main__":
    f = open(F_NAME)

    robots = []

    for l in f:
        l = l.strip().split()
        pos_coord = l[0].split('=')[1].split(',')
        vels = l[1].split('=')[1].split(',')
        pos_row = int(pos_coord[1])
        pos_col = int(pos_coord[0])
        vel_row = int(vels[1])
        vel_col = int(vels[0])
        robot_status = [pos_row, pos_col, vel_row, vel_col]

        # robots saved as (pos_row, pos_col, vel_row, vel_col)
        robots.append(robot_status)

    # Part 1 (uncomment)
    # move_bots(robots, 100)

    # print(calc_score(robots))
    
    # Part 2

    # Deep copy the original robot array to allow us to compare
    orig_bots = []
    for i in range(len(robots)):
        orig_bot = []
        for val in robots[i]:
            orig_bot.append(val)
        orig_bots.append(orig_bot)

    for i in range(10500):
        move_bots(robots, 1)
        # is_equal(orig_bots, robots, i + 1)
        # Cycle repeats every 10403 iterations, so the tree must be somewhere in there

        for j in range(N_COLS):
            if (check_mirror(robots, j)):
                print(i+1)
                to_display = {}
                for bot in robots:
                    to_display.update({(bot[0], bot[1]):'O'})
                for r in range(N_ROWS):
                    for c in range(N_COLS):
                        if (to_display.get((r,c)) == None):
                            print('.',end='')
                        else:
                            print('O', end='')
                    print()
                exit()
    


    f.close()