# Written by Josh Yeaton on 1/15/24
# For Advent of Code 2024

def move_bot(dir, map, bot_loc):
    start_loc = bot_loc
    check_loc = bot_loc
    if (dir == '^'):
        check_loc = (check_loc[0] - 1, check_loc[1])
        new_bot_loc = check_loc
        while (map.get(check_loc) == 'O'):
            check_loc = (check_loc[0] - 1, check_loc[1])
        if (map.get(check_loc) == '#'):
            # unable to move
            new_loc = bot_loc
        else:
            # empty spot exists, move. 
            map.update({bot_loc:'.'})
            map.update({new_bot_loc:'@'})
            prev_loc = (check_loc[0] + 1, check_loc[1])
            if (prev_loc != start_loc):
                # there were intervening boxes, so move them down
                map.update({check_loc:'O'})
            new_loc = new_bot_loc
    elif (dir == '>'):
        check_loc = (check_loc[0], check_loc[1] + 1)
        new_bot_loc = check_loc
        while (map.get(check_loc) == 'O'):
            check_loc = (check_loc[0], check_loc[1] + 1)
        if (map.get(check_loc) == '#'):
            # unable to move
            new_loc = bot_loc
        else:
            # empty spot exists, move. 
            map.update({bot_loc:'.'})
            map.update({new_bot_loc:'@'})
            prev_loc = (check_loc[0], check_loc[1] - 1)
            if (prev_loc != start_loc):
                # there were intervening boxes, so move them down
                map.update({check_loc:'O'})
            new_loc = new_bot_loc
    elif (dir == 'v'):
        check_loc = (check_loc[0] + 1, check_loc[1])
        new_bot_loc = check_loc
        while (map.get(check_loc) == 'O'):
            check_loc = (check_loc[0] + 1, check_loc[1])
        if (map.get(check_loc) == '#'):
            # unable to move
            new_loc = bot_loc
        else:
            # empty spot exists, move. 
            map.update({bot_loc:'.'})
            map.update({new_bot_loc:'@'})
            prev_loc = (check_loc[0] - 1, check_loc[1])
            if (prev_loc != start_loc):
                # there were intervening boxes, so move them down
                map.update({check_loc:'O'})
            new_loc = new_bot_loc
    else: # dir == '<'
        check_loc = (check_loc[0], check_loc[1] - 1)
        new_bot_loc = check_loc
        while (map.get(check_loc) == 'O'):
            check_loc = (check_loc[0], check_loc[1] - 1)
        if (map.get(check_loc) == '#'):
            # unable to move
            new_loc = bot_loc
        else:
            # empty spot exists, move. 
            map.update({bot_loc:'.'})
            map.update({new_bot_loc:'@'})
            prev_loc = (check_loc[0], check_loc[1] + 1)
            if (prev_loc != start_loc):
                # there were intervening boxes, so move them down
                map.update({check_loc:'O'})
            new_loc = new_bot_loc
    return new_loc

def find_score_pt1(map, max_row, max_col):
    score = 0
    for r in range(max_row):
        for c in range(max_col):
            if (map.get((r,c)) == 'O'):
                score += ((100 * r) + c)
    return score

def check_pt2_move(loc, map, already_checked, dir):
    # already_checked: dic
    if (dir == '<' or dir == '>'):
        return check_pt2_lateral_move(loc, map, dir)
    if (already_checked.get(loc) != None):
        return already_checked.get(loc)
    # Find coordinate we are checking
    if (dir == '^'):
        check_coord = (loc[0] - 1, loc[1])
    else:
        check_coord = (loc[0] + 1, loc[1])
    # Check coord
    if (map.get(loc) == '@'):
        # we are the robot
        if (map.get(check_coord) == '#'):
            return False
        elif (map.get(check_coord) == '.'):
            already_checked.update({check_coord:True})
            already_checked.update({loc:True})
            return True
        else:
            # must be a box, see if the box can move
            res = check_pt2_move(check_coord, map, already_checked, dir)
            if (res):
                already_checked.update({loc:True})
                return True
            else:
                return False
    elif (map.get(loc) == '['):
        # left side of a box, check right side first
        right_loc = (loc[0], loc[1] + 1)
        if (not check_pt2_move(right_loc, map, already_checked, dir)):
            already_checked.update({loc:False})
            return False
        else:
            # The right side is able to move, see if we can
            if (map.get(check_coord) == '#'):
                already_checked.update({loc:False})
                already_checked.update({right_loc:False})
                return False
            elif (map.get(check_coord) == '.'):
                already_checked.update({check_coord:True})
                already_checked.update({loc:True})
                return True
            else:
                # Another box...
                if (check_pt2_move(check_coord, map, already_checked, dir)):
                    already_checked.update({loc:True})
                    return True
                else:
                    already_checked.update({loc:False})
                    return False
    else:
        # right side of a box
        left_loc = (loc[0], loc[1] - 1)
        if (map.get(check_coord) == '#'):
            already_checked.update({loc:False})
            already_checked.update({left_loc:False})
            return False
        elif (map.get(check_coord) == '.'):
            already_checked.update({check_coord:True})
            already_checked.update({loc:True})
            if (check_pt2_move(left_loc, map, already_checked, dir)):
                return True
            else:
                already_checked.update({loc:False})
                return False
        else:
            # another box...
            if (check_pt2_move(check_coord, map, already_checked, dir)):
                already_checked.update({loc:True})
                if (check_pt2_move(left_loc, map, already_checked, dir)):
                    return True
                else:
                    already_checked.update({loc:False})
                    return False
            else:
                already_checked.update({loc:False})
                return False


def check_pt2_lateral_move(loc, map, dir):
    if (map.get(loc) == '.'):
        return True
    elif (map.get(loc) == '#'):
        return False
    if (dir == '<'):
        return check_pt2_lateral_move((loc[0], loc[1] - 1), map, dir)
    else:
        return check_pt2_lateral_move((loc[0], loc[1] + 1), map, dir)
    
def execute_pt2_move(start_loc, map, prev_checked, dir):
    if (dir == '<' or dir == '>'):
        return execute_pt2_lateral_move(start_loc, map, 0, dir)
    if (dir == '^'):
        next_loc = (start_loc[0] - 1, start_loc[1])
    else:
        next_loc = (start_loc[0] + 1, start_loc[1])
    # copy the map
    map_copy = {}
    for loc in map:
        map_copy.update({loc:map.get(loc)})
    for loc in prev_checked:
        if (dir == '^'):
            prev_loc = (loc[0] + 1, loc[1])
        else:
            prev_loc = (loc[0] - 1, loc[1])

        if (prev_checked.get(prev_loc) == None):
            map.update({loc:'.'})
        else:
            map.update({loc:map_copy.get(prev_loc)})
    return next_loc



def execute_pt2_lateral_move(loc, map, prev_loc, dir):
    # first, origin
    if (dir == '<'):
        next_loc = (loc[0], loc[1] - 1)
    else:
        next_loc = (loc[0], loc[1] + 1)
    if (map.get(loc) == '.'):
        map.update({loc:map.get(prev_loc)})
        return next_loc
    execute_pt2_lateral_move(next_loc, map, loc, dir)
    if (prev_loc == 0):
        map.update({loc:'.'})
    else:
        map.update({loc:map.get(prev_loc)})
    return next_loc

def pt2_round(loc, map, dir):
    already_checked = {}
    if (check_pt2_move(loc, map, already_checked, dir)):
        # find direction and move
        return execute_pt2_move(loc, map, already_checked, dir)
    else:
        return loc
    
def find_score_pt2(map, max_row, max_col):
    score = 0
    for r in range(max_row):
        for c in range(max_col):
            if (map.get((r,c)) == '['):
                score += ((100 * r) + c)
    return score
        
if __name__ == "__main__":
    filename = 'data_test.txt'
    filename = 'data.txt'
    f = open(filename)

    map = {}
    dirs = ''

    start_loc = (0,0)

    row = 0
    for l in f:
        l = l.strip()
        
        if ('#' in l):
            col = 0
            for c in l:
                if c == '@':
                    start_loc = (row, col)
                map.update({(row, col):c})
                col += 1
            row += 1
        else:
            dirs += l
    f.close()

    cur_loc = start_loc
    for i in range(len(dirs)):
        cur_loc = move_bot(dirs[i], map, cur_loc)


    print(find_score_pt1(map, row, col))

    # Part 2

    f = open(filename)

    map = {}
    dirs = ''

    start_loc = (0,0)

    row = 0
    for l in f:
        l = l.strip()
        
        if ('#' in l):
            col = 0
            for c in l:
                if c == 'O':
                    map.update({(row, col):'['})
                    map.update({(row, col + 1):']'})
                elif c == '@':
                    map.update({(row, col):'@'})
                    map.update({(row, col + 1):'.'})
                    start_loc = (row, col)
                else:
                    map.update({(row, col):c})
                    map.update({(row, col + 1):c})
                col += 2
            row += 1
        else:
            dirs += l
    f.close()

    cur_loc = start_loc
    for i in range(len(dirs)):
        already_checked = {}
        cur_loc = pt2_round(cur_loc, map, dirs[i])



    # for r in range(row):
    #         for c in range(col):
    #             print(map.get((r, c)), end='')
    #         print()

    print(find_score_pt2(map, row, col))