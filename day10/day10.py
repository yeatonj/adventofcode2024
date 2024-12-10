# Written by Josh Yeaton on 1/10/24
# For Advent of Code 2024

def count_trails_pt1(topo_map, start, found):
    if (topo_map.get(start) == 9):
        found.update({start:1})
    target_height = topo_map.get(start) + 1
    up_coord = (start[0] - 1, start[1])
    down_coord = (start[0] + 1, start[1])
    right_coord = (start[0], start[1] + 1)
    left_coord = (start[0], start[1] - 1)

    if (topo_map.get(up_coord) == target_height):
        count_trails_pt1(topo_map, up_coord, found)
    if (topo_map.get(down_coord) == target_height):
        count_trails_pt1(topo_map, down_coord, found)
    if (topo_map.get(right_coord) == target_height):
        count_trails_pt1(topo_map, right_coord, found)
    if (topo_map.get(left_coord) == target_height):
        count_trails_pt1(topo_map, left_coord, found)

    if (target_height == 1):
        return len(found)
    else:
        return 0

def count_trails_pt2(topo_map, start):
    if (topo_map.get(start) == 9):
        return 1
    total = 0
    target_height = topo_map.get(start) + 1
    up_coord = (start[0] - 1, start[1])
    down_coord = (start[0] + 1, start[1])
    right_coord = (start[0], start[1] + 1)
    left_coord = (start[0], start[1] - 1)

    if (topo_map.get(up_coord) == target_height):
        total += count_trails_pt2(topo_map, up_coord)
    if (topo_map.get(down_coord) == target_height):
        total += count_trails_pt2(topo_map, down_coord)
    if (topo_map.get(right_coord) == target_height):
        total += count_trails_pt2(topo_map, right_coord)
    if (topo_map.get(left_coord) == target_height):
        total += count_trails_pt2(topo_map, left_coord)

    return total


if __name__ == "__main__":
    f = open('data.txt')

    topo_map = {}

    row = 0
    for r in f:
        r = r.strip()
        col = 0
        for c in r:
            topo_map.update({(row, col):int(c)})
            col += 1
        row += 1
    for i in range(-1, row + 1):
        topo_map.update({(i, -1):'#'})
        topo_map.update({(i, col):'#'})
    for i in range(-1, col + 1):
        topo_map.update({(-1, i):'#'})
        topo_map.update({(row, i):'#'})

    total_pt1 = 0
    total_pt2 = 0

    for r in range(0, row):
        for c in range(0, col):
            if (topo_map.get((r,c)) == 0):
                found = {}
                total_pt1 += count_trails_pt1(topo_map, (r,c), found)
                total_pt2 += count_trails_pt2(topo_map, (r,c))

    print(total_pt1)
    print(total_pt2)
    
    f.close()