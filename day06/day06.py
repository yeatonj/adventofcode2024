# Written by Josh Yeaton on 1/6/24
# For Advent of Code 2024

def part_1(start_loc, map, width, height):
    cur_dir = 0 # 0: up, 1: right, 2: down, 3: right
    cur_loc = start_loc
    map.update({cur_loc:'X'})
    while(True):
        if (cur_dir == 0):
            next_loc = (cur_loc[0] - 1, cur_loc[1])
        elif (cur_dir == 1):
            next_loc = (cur_loc[0], cur_loc[1] + 1)
        elif (cur_dir == 2):
            next_loc = (cur_loc[0] + 1, cur_loc[1])
        else:
            next_loc = (cur_loc[0], cur_loc[1] - 1)
        if (map.get(next_loc) == '@'):
            break
        elif (map.get(next_loc) == '#'):
            cur_dir = (cur_dir + 1) % 4
        else:
            map.update({next_loc:'X'})
            cur_loc = next_loc

    total = 0
    for r in range(height):
        for c in range(width):
            if (map.get((r,c)) == 'X'):
                total += 1
                map.update({(r, c):'.'})
            
    return total

def part_2(start_loc, map, width, height):
    total_loops = 0
    for r in range(height):
        for c in range(width):
            if (map.get((r,c)) != '.'):
                continue
            # This is a valid possible location
            map.update({(r,c):'#'})
            
            visited = {}

            cur_dir = 0 # 0: up, 1: right, 2: down, 3: right
            cur_loc = start_loc
            visited.update({start_loc:[cur_dir]})
            while(True):
                if (cur_dir == 0):
                    next_loc = (cur_loc[0] - 1, cur_loc[1])
                elif (cur_dir == 1):
                    next_loc = (cur_loc[0], cur_loc[1] + 1)
                elif (cur_dir == 2):
                    next_loc = (cur_loc[0] + 1, cur_loc[1])
                else:
                    next_loc = (cur_loc[0], cur_loc[1] - 1)
                if (map.get(next_loc) == '@'):
                    break
                elif (map.get(next_loc) == '#'):
                    cur_dir = (cur_dir + 1) % 4
                else:
                    if (next_loc not in visited):
                        visited.update({next_loc:[cur_dir]})
                    else:
                        if (cur_dir in visited.get(next_loc)):
                            total_loops += 1
                            break
                        else:
                            visited.get(next_loc).append(cur_dir)
                    cur_loc = next_loc
            # reset the map
            map.update({(r,c):'.'})
    return total_loops

if __name__ == "__main__":
    f = open('data.txt')

    map = {}

    height = 0
    starting_loc = (0, 0)

    for l in f:
        l = l.strip()
        width = 0
        for c in l:
            if (c == '^'):
                starting_loc = (height, width)
                map.update({(height, width):'.'})
            else:
                map.update({(height, width):c})
            width += 1
        height += 1

for r in range(-1, height + 1):
    map.update({(r, -1): '@'})
    map.update({(r, width): '@'})

for c in range(-1, width + 1):
    map.update({(-1, c): '@'})
    map.update({(height, c): '@'})




# 5211 is too low
print(part_1(starting_loc, map, width, height))
print(part_2(starting_loc, map, width, height))




            
# for r in range(-1, height + 1):
#     for c in range(-1, width + 1):
#         print(map.get((r, c)), end='')
    
#     print()


f.close()