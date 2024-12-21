# Written by Josh Yeaton on 1/20/24
# For Advent of Code 2024

# general idea - represent keypads as graphs
import collections

def pad_bfs(layout, start_loc, goal_key):
    DIRS = ['^', '>', 'v', '<']
    path_queue = collections.deque([(start_loc, '')])
    poss_paths = []
    found_len = -1
    while(len(path_queue) > 0):
        cur_path = path_queue.popleft()
        cur_loc = cur_path[0]
        cur_seq = cur_path[1]
        if ((found_len != -1) and (len(cur_seq) > found_len)):
            return poss_paths
        if (layout.get(cur_loc) == goal_key):
            poss_paths.append((cur_loc, cur_seq))
            found_len = len(cur_seq)

        # find all adjacent possibilities
        up_loc = (cur_loc[0] - 1, cur_loc[1])
        right_loc = (cur_loc[0], cur_loc[1] + 1)
        down_loc = (cur_loc[0] + 1, cur_loc[1])
        left_loc = (cur_loc[0], cur_loc[1] - 1)

        adj_locs = [up_loc, right_loc, down_loc, left_loc]

        for i in range(len(adj_locs)):
            if (layout.get(adj_locs[i]) != None):
                path_queue.append((adj_locs[i], cur_seq + DIRS[i]))

    return [((-1, -1), '')]

def compare_dirs(d1, d2):
    if (d1 == '<'):
        if (d2 == '<'):
            return 0
        else:
            return -1
    elif (d1 == 'v'):
        if (d2 == '<'):
            return 1
        elif (d2 == 'v'):
            return 0
        else:
            return -1
    elif (d1 == '^' or d1 == '>'):
        if (d2 == '<' or d2 == 'v'):
            return 1
        else:
            return 0

def find_min_turns(poss_res):
    if (len(poss_res) == 1):
        return poss_res[0]
    # At this point we need to look thru them
    best_ind = 0
    cur_res = poss_res[0]
    cur_turn_ct = 0
    cur_cmd_seq = cur_res[1]
    if (len(cur_cmd_seq) == 1):
        print('should not be possible')
        exit()
    cur_cmd = cur_cmd_seq[0]
    for i in range(1,len(cur_cmd_seq)):
        next_cmd = cur_cmd_seq[i]
        if (cur_cmd != next_cmd):
            cur_turn_ct += 1
        cur_cmd = next_cmd
    best_turn_ct = cur_turn_ct
    # At this point, we are set on the first command
    for j in range(1,len(poss_res)):
        cur_res = poss_res[j]
        cur_turn_ct = 0
        cur_cmd_seq = cur_res[1]
        if (len(cur_cmd_seq) == 1):
            print('should not be possible')
            exit()
        cur_cmd = cur_cmd_seq[0]
        for i in range(1,len(cur_cmd_seq)):
            next_cmd = cur_cmd_seq[i]
            if (cur_cmd != next_cmd):
                cur_turn_ct += 1
            cur_cmd = next_cmd
        if (cur_turn_ct < best_turn_ct):
            best_turn_ct = cur_turn_ct
            best_ind = j
        elif (cur_turn_ct == best_turn_ct):
            # from here, prefer left -> down -> (up == right)
            best_str = poss_res[best_ind][1]
            new_str = cur_cmd_seq
            for k in range(len(best_str)):
                comp_res = compare_dirs(best_str[k], new_str[k])
                if (comp_res > 0):
                    best_turn_ct = cur_turn_ct
                    best_ind = j
                    break
                elif (comp_res > 0):
                    break
    return poss_res[best_ind]

def find_len_at_depth(char, depth, mem_dic):
    
    return 0

if __name__ == "__main__":
    filename = 'data_test.txt'
    filename = 'data.txt'

    f = open(filename)
    codes = []

    for l in f:
        l = l.strip()
        codes.append(l) 
    f.close()

    NUMPAD = {(0,0):'7', (0,1):'8', (0,2):'9', (1,0):'4', (1,1):'5', (1,2):'6', (2,0):'1', (2,1):'2', (2,2):'3', (3,1):'0', (3,2):'A'}
    KEYPAD = {(0,1):'^', (0,2):'A', (1,0):'<', (1,1):'v', (1,2):'>'}

    NUMPAD_START = (3,2)
    KEYPAD_START = (0,2)

    score = 0
    reps = 2 # part 1
    # reps = 25 # part 2

    # Layer 1, robot 1 to numpad robot
    for code in codes:
        print(code)
        # Commands for Numpad
        cur_loc = NUMPAD_START
        seq_np = ''
        for input in code:
            poss_res = pad_bfs(NUMPAD, cur_loc, input)
            (cur_loc, sub_seq) = find_min_turns(poss_res)
            seq_np += (sub_seq + 'A')
        # print(seq_np)

        cur_seq = seq_np
        seq_dic = {}
        for i in range(reps):
            print(cur_seq)
            cur_loc = KEYPAD_START
            next_seq_kp = ''
            for input in cur_seq:
                poss_res = pad_bfs(KEYPAD, cur_loc, input)
                (cur_loc, sub_seq) = find_min_turns(poss_res)
                next_seq_kp += (sub_seq + 'A')
            cur_seq = next_seq_kp
            print(cur_seq)

        score += (len(cur_seq) * int(code[:-1]))
        print()

    print(score)
