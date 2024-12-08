# Written by Josh Yeaton on 1/8/24
# For Advent of Code 2024

def check_boundaries(node, max_r, max_c):
    return (node[0] >= 0 and node[0] < max_r and node[1] >=0 and node[1] < max_c)


if __name__ == "__main__":
    f = open('data.txt')

    node_coords = {}

    r = 0
    for l in f:
        l = l.strip()
        col = 0
        for c in l:
            if c == '.':
                col += 1
                continue
            if c not in node_coords:
                node_coords.update({c:[]})
            node_coords.get(c).append((r, col))
            col += 1
        r += 1

    rows = r
    cols = col

    f.close()

    ## Part 1
    antinode_list = {}
    for node_type in node_coords:
        cur_antinodes = []
        cur_coords = node_coords.get(node_type)
        for i in range(len(cur_coords) - 1):
            for j in range(i + 1, len(cur_coords)):
                node_1 = cur_coords[i]
                node_2 = cur_coords[j]

                r_dist = node_2[0] - node_1[0]
                c_dist = node_2[1] - node_1[1]

                antinode_1 = (node_1[0] - r_dist, node_1[1] - c_dist)
                antinode_2 = (node_2[0] + r_dist, node_2[1] + c_dist)

                if (check_boundaries(antinode_1, rows, cols)):
                    cur_antinodes.append(antinode_1)
                if (check_boundaries(antinode_2, rows, cols)):
                    cur_antinodes.append(antinode_2)
                
        antinode_list.update({node_type:cur_antinodes})

    unique_antinode_locs = {}
    for node_type in antinode_list:
        for antinode in antinode_list.get(node_type):
            unique_antinode_locs.update({antinode:1})

    print(len(unique_antinode_locs))


    ## Part 2
    antinode_list = {}
    for node_type in node_coords:
        cur_antinodes = []
        cur_coords = node_coords.get(node_type)
        for i in range(len(cur_coords) - 1):
            for j in range(i + 1, len(cur_coords)):
                node_1 = cur_coords[i]
                node_2 = cur_coords[j]

                r_dist = node_2[0] - node_1[0]
                c_dist = node_2[1] - node_1[1]

                # find all antinodes subtracting from node_1
                cur_node = node_1
                while(check_boundaries(cur_node, rows, cols)):
                    cur_antinodes.append(cur_node)
                    cur_node = (cur_node[0] - r_dist, cur_node[1] - c_dist)

                # find all antinodes adding to node_1
                cur_node = (node_1[0] + r_dist, node_1[1] + c_dist)
                while(check_boundaries(cur_node, rows, cols)):
                    cur_antinodes.append(cur_node)
                    cur_node = (cur_node[0] + r_dist, cur_node[1] + c_dist)
                
        antinode_list.update({node_type:cur_antinodes})

    unique_antinode_locs = {}
    for node_type in antinode_list:
        for antinode in antinode_list.get(node_type):
            unique_antinode_locs.update({antinode:1})

    print(len(unique_antinode_locs))