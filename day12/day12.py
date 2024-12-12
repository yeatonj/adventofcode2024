# Written by Josh Yeaton on 1/12/24
# For Advent of Code 2024

from collections import deque

def find_perim(coords):
    perim = 0
    for loc in coords:
        if (coords.get((loc[0] + 1, loc[1])) == None):
            perim += 1
        if (coords.get((loc[0] - 1, loc[1])) == None):
            perim += 1
        if (coords.get((loc[0], loc[1] + 1)) == None):
            perim += 1
        if (coords.get((loc[0], loc[1] - 1)) == None):
            perim += 1
    return perim

def get_next_edge(coords, cur_edge):
    # returns (next_edge, wasTurn)
    # edge: (r, c, e), where e=0 bottom (travel l->r), 1 left (travel u->d), 2 top (travel r->l), 3 right (travel d->u)
    r = cur_edge[0]
    c = cur_edge[1]
    dir = cur_edge[2]
    if (dir == 0):
        # bottom edge, travel l->r
        # check right cube
        if (coords.get((r, c + 1)) != None):
            # can only keep going or travel down
            if (coords.get((r + 1, c + 1)) != None):
                # now moving down
                result = ((r + 1, c + 1, 1), True)
            else:
                # keep going straight
                result = ((r, c + 1, 0), False)
        else:
            # must go up
            result = ((r, c, 3), True)
    elif (dir == 1):
        # left edge, travel u->d
        # check below cube
        if (coords.get((r + 1, c)) != None):
            # can either continue going down or go left
            if (coords.get((r + 1, c - 1)) != None):
                # now moving left
                result = ((r + 1, c - 1, 2), True)
            else:
                # keep going down
                result = ((r + 1, c, 1), False)
        else:
            # must go right
            result = ((r, c, 0), True)
        pass
    elif  (dir == 2):
        # top edge, travel r->l
        if (coords.get((r, c - 1)) != None):
            # can either continue going left or go up
            if (coords.get((r - 1, c - 1)) != None):
                # now going up
                result = ((r - 1, c - 1, 3), True)
            else:
                # keep moving along the top
                result = ((r, c - 1, 2), False)
        else:
            # must go down
            result = ((r, c, 1), True)
        pass
    else: # dir == 3
        # right edge, travel d->u
        if (coords.get((r - 1, c)) != None):
            # can eiher continue going up or turn right
            if (coords.get((r - 1, c + 1)) != None):
                # turn right
                result = ((r - 1, c + 1, 0), True)
            else:
                # keep going up
                result = ((r - 1, c, 3), False)
        else:
            # must turn left
            result = ((r, c, 2), True)
    return result

def find_sides(coords):
    # edge: (r, c, e), where e=0 bottom (travel l->r), 1 left (travel u->d), 2 top (travel r->l), 3 right (travel d->u)
    side_count = 0
    edges_to_visit = deque()
    edges_visited = {}
    for loc in coords:
        if (coords.get((loc[0] + 1, loc[1])) == None):
            edges_to_visit.append((loc[0], loc[1], 0))
        if (coords.get((loc[0] - 1, loc[1])) == None):
            edges_to_visit.append((loc[0], loc[1], 2))
        if (coords.get((loc[0], loc[1] + 1)) == None):
            edges_to_visit.append((loc[0], loc[1], 3))
        if (coords.get((loc[0], loc[1] - 1)) == None):
            edges_to_visit.append((loc[0], loc[1], 1))
        # now, visit all edges for this location
        while (len(edges_to_visit) > 0):
            start_edge = edges_to_visit.popleft()
            # skip edges we have already traveled
            if (edges_visited.get(start_edge) != None):
                continue
            # This is a new edge, follow it around
            next_edge = (-1, -1, -1) # dummy value
            cur_edge = start_edge
            while (next_edge != start_edge):
                # infinite loop here...
                (next_edge, wasTurn) = get_next_edge(coords, cur_edge)
                if (wasTurn):
                    side_count += 1
                edges_visited.update({next_edge:1})
                cur_edge = next_edge
    return side_count


def pt1_bfs(map, rows, cols):
    explored = {}
    total_price = 0
    for r in range(rows):
        for c in range(cols):
            # skip already visited start points
            if (explored.get((r,c)) != None):
                continue
            cur_region = {}
            region_val = map.get((r,c))
            to_check = deque([(r,c)])
            while (len(to_check) > 0):
                cur_loc = to_check.popleft()
                cur_val = map.get(cur_loc)
                if ((explored.get(cur_loc) != None) or (cur_val == None) or (cur_val != region_val)):
                    # already explored, not on map, or not in our current region
                    continue
                explored.update({cur_loc:region_val})
                cur_region.update({cur_loc:region_val})
                # add surrounding
                to_check.append((cur_loc[0] + 1, cur_loc[1]))
                to_check.append((cur_loc[0] - 1, cur_loc[1]))
                to_check.append((cur_loc[0], cur_loc[1] + 1))
                to_check.append((cur_loc[0], cur_loc[1] - 1))
            if (len(cur_region) > 0):
                cur_perim = find_perim(cur_region)
                total_price += (cur_perim * len(cur_region))
    return total_price

def pt2_bfs(map, rows, cols):
    explored = {}
    total_price = 0
    for r in range(rows):
        for c in range(cols):
            # skip already visited start points
            if (explored.get((r,c)) != None):
                continue
            cur_region = {}
            region_val = map.get((r,c))
            to_check = deque([(r,c)])
            while (len(to_check) > 0):
                cur_loc = to_check.popleft()
                cur_val = map.get(cur_loc)
                if ((explored.get(cur_loc) != None) or (cur_val == None) or (cur_val != region_val)):
                    # already explored, not on map, or not in our current region
                    continue
                explored.update({cur_loc:region_val})
                cur_region.update({cur_loc:region_val})
                # add surrounding
                to_check.append((cur_loc[0] + 1, cur_loc[1]))
                to_check.append((cur_loc[0] - 1, cur_loc[1]))
                to_check.append((cur_loc[0], cur_loc[1] + 1))
                to_check.append((cur_loc[0], cur_loc[1] - 1))
            if (len(cur_region) > 0):
                num_sides = find_sides(cur_region)
                total_price += (num_sides * len(cur_region))
    return total_price


if __name__ == "__main__":
    f = open('data.txt')

    map = {}

    row = 0
    for l in f:
        l = l.strip()
        col = 0
        for c in l:
            map.update({(row, col):c})
            col += 1
        row += 1

    print(pt1_bfs(map, row, col))

    print(pt2_bfs(map, row, col))


    

    f.close()