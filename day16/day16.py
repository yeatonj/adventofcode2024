# Written by Josh Yeaton on 1/16/24
# For Advent of Code 2024


def dfs(start, goal, map, best_seats):
    # N E S W == 0 1 2 3, always explore in that order
    # Stack holds [loc, dir, score, to_explore]
    stack = [[start, 1, 0, 0]]
    visited = {}
    min_to_reach = {}
    min_score = -1
    while (stack != []):
        cur_loc = stack[-1][0]
        dir = stack[-1][1]
        score = stack[-1][2]
        to_explore = stack[-1][3]
        level_done = False
        # If we are over min score, skip this iteration, no point continuing
        if ((min_score != -1) and (score > min_score)):
            level_done = True
        # If we are at the goal, update min score
        if (cur_loc == goal):
            if ((min_score == -1) or (score < min_score)):
                min_score = score
                best_seats.clear()
                for entry in stack:
                    best_seats.update({entry[0]:True})
            elif (score == min_score):
                for entry in stack:
                    best_seats.update({entry[0]:True})
            level_done = True
        # If we are currently on a wall, skip this iteration
        if (map.get(cur_loc) == '#'):
            level_done = True
        # If we are done exploring from this point, drop it from the stack
        if (to_explore == 4):
            level_done = True
        # If we have already checked this point, ignore
        if (visited.get(cur_loc) != None):
            level_done = True
        # Finally, if we have already reached this point with a lower possible score, ignore
        cur_min_to_reach = min_to_reach.get((cur_loc, dir))
        if ((cur_min_to_reach == None) or (score <= cur_min_to_reach)):
            min_to_reach.update({(cur_loc,dir):score})
        else:
            level_done = True


        # Check if we should move back at least one level in the DFS, possibly more depending on minimum score
        if (level_done):
            stack = stack[:-1]
            # remove prev stack top from visited if necessary
            if (stack != []):
                visited.pop(stack[-1][0])
            continue


        # At this point, we know we have more exploring to do
        # We have now visited this point
        visited.update({cur_loc:True})

        if (dir == 0):
            grid_scores = [1, 1001, 1002, 1001]
        elif (dir == 1):
            grid_scores = [1001, 1, 1001, 1002]
        elif (dir == 2):
            grid_scores = [1002, 1001, 1, 1001]
        else: # dir == 3
            grid_scores = [1001, 1002, 1001, 1]

        if (to_explore == 0):
            next_pt = (cur_loc[0] - 1, cur_loc[1])
            next_score = score + grid_scores[0]
        elif (to_explore == 1):
            next_pt = (cur_loc[0], cur_loc[1] + 1)
            next_score = score + grid_scores[1]
        elif (to_explore == 2):
            next_pt = (cur_loc[0] + 1, cur_loc[1])
            next_score = score + grid_scores[2]
        else: 
            next_pt = (cur_loc[0], cur_loc[1] - 1)
            next_score = score + grid_scores[3]

        # Update to_explore for this value on the stack
        stack[-1][3] += 1

        # Stack holds [loc, dir, score, to_explore], append next value to stack
        stack.append([next_pt, to_explore, next_score, 0])
    return min_score

if __name__ == "__main__":
    filename = 'data_test.txt'
    filename = 'data.txt'
    f = open(filename)

    map = {}

    row = 0
    for l in f:
        l = l.strip()
        col = 0
        for c in l:
            if (c == 'S'):
                start = (row, col)
                map.update({(row,col):'.'})
            elif (c == 'E'):
                goal = (row, col)
                map.update({(row,col):'.'})
            else:
                map.update({(row,col):c})
            
            col += 1
        row +=1

    max_row = row
    max_col = col
    f.close()

    min_score = []
    best_seats = {}

    print(dfs(start, goal, map, best_seats))
    print(len(best_seats))

