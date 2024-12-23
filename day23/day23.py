# Written by Josh Yeaton on 1/23/24
# For Advent of Code 2024

def gen_subgraphs(node_list, order):
    ret_arr = []
    if (order == 1):
        for node in node_list:
            ret_arr.append([node])
        return ret_arr
    for i in range(len(node_list) - order + 1):
        cur_prefix = node_list[i]
        suffixes = gen_subgraphs(node_list[i + 1:], order - 1)
        for suffix in suffixes:
            sub_arr = []
            sub_arr.append(cur_prefix)
            for entry in suffix:
                sub_arr.append(entry)
            ret_arr.append(sub_arr)
    return ret_arr

def verify_connectivity(graph, perm):
    if len(perm) == 1:
        return True
    start_node_conns = graph.get(perm[0])
    for i in range(1, len(perm)):
        if perm[i] not in start_node_conns:
            return False
    return verify_connectivity(graph, perm[1:])



if __name__ == "__main__":
    filename = 'data_test.txt'
    filename = 'data.txt'

    f = open(filename)

    graph = {}
    
    for l in f:
        l = l.strip()
        l = l.split('-')
        source = l[0]
        dest = l[1]
        if source not in graph:
            graph.update({source:{}})
        if dest not in graph:
            graph.update({dest:{}})
        source_dic = graph.get(source)
        dest_dic = graph.get(dest)
        source_dic.update({dest:1})
        dest_dic.update({source:1})
    f.close()


    found_combos = {}
    node_list = []

    for node_1 in graph:
        node_list.append(node_1)
        if (node_1[0] != 't'):
            continue
        poss_node_2 = graph.get(node_1)
        for node_2 in poss_node_2:
            poss_node_3 = graph.get(node_2)
            for node_3 in poss_node_3:
                if (node_1 in graph.get(node_3)):
                    # This is a possible solution
                    poss_sol = [node_1, node_2, node_3]
                    poss_sol.sort()
                    sol = (poss_sol[0], poss_sol[1], poss_sol[2])
                    found_combos.update({sol:1})
    print(len(found_combos))

    # Part 2

    # Get initial solutions
    subgraphs = gen_subgraphs(node_list, 2)
    solutions = []
    for perm in subgraphs:
            is_connected = verify_connectivity(graph, perm)
            if (is_connected):
                solutions.append(perm)
    
    checked = {}
    while (len(solutions) > 1):
        print(len(solutions))
        # Go to next level
        checked = {}
        next_solutions = []
        for soln in solutions:
            for node in node_list:
                temp_soln = []
                if node not in soln:
                    for temp_node in soln:
                        temp_soln.append(temp_node)
                    temp_soln.append(node)
                    temp_soln.sort()
                    if (tuple(temp_soln) not in checked):
                        if (verify_connectivity(graph, temp_soln)):
                            next_solutions.append(temp_soln)
                        checked.update({tuple(temp_soln):1})
        solutions = next_solutions
        

    soln = solutions[0]
    soln.sort()
    ans = ''
    for n in soln:
        ans += n +','
    
    print(ans[:-1])




            