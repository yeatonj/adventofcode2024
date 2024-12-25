# Written by Josh Yeaton on 1/24/24
# For Advent of Code 2024

def test_adder(x_val, y_val, insts, z_list):
    # set up initial values
    x_bin = format(x_val, 'b')
    while (len(x_bin) < 45):
        x_bin = '0' + x_bin
    y_bin = format(y_val, 'b')
    while (len(y_bin) < 45):
        y_bin = '0' + y_bin
    cur_vals = {}
    for i in range(len(x_bin)):
        bit_pos = str(44 - i)
        if (len(bit_pos) == 1):
            bit_pos = '0' + bit_pos
        cur_vals.update({('x' + bit_pos):int(x_bin[i])})
        cur_vals.update({('y' + bit_pos):int(y_bin[i])})
    new_vals = {}
    z_vals = 0
    # Reset instructions
    for inst in insts:
        inst[4] = False
    while (z_vals < len(z_list)):
        for inst in insts:
            # If we've already done this operation, skip it
            if (inst[4] == True):
                continue
            # Get current operator values, if they exist
            # operator 1
            if (new_vals.get(inst[0]) != None):
                op1 = new_vals.get(inst[0])
            elif (cur_vals.get(inst[0]) != None):
                op1 = cur_vals.get(inst[0])
            else:
                continue
            # operator 2
            if (new_vals.get(inst[1]) != None):
                op2 = new_vals.get(inst[1])
            elif (cur_vals.get(inst[1]) != None):
                op2 = cur_vals.get(inst[1])
            else:
                continue
            # At this point, we have both operators and can perform the instruction
            if (inst[2] == 'A'):
                res = op1 & op2
            elif (inst[2] == 'X'):
                res = op1 ^ op2
            else:
                # OR
                res = op1 | op2
            # We have now finished this operator
            if (inst[3][0] == 'z'):
                print(inst[3])
                z_vals += 1
            inst[4] = True
            new_vals.update({inst[3]:res})

    p1_str = ''

    for z in z_list:
        p1_str += str(new_vals.get(z[0]))

    return int(p1_str, 2)

if __name__ == "__main__":
    filename = 'data_test.txt'
    filename = 'data.txt'

    f = open(filename)

    cur_vals = {}
    insts = []

    x_str = ''
    y_str = ''

    for l in f:
        l = l.strip()
        if (':' in l):
            l = l.split(': ')
            cur_vals.update({l[0]:int(l[1])})
            if 'x' in l[0]:
                x_str = l[1] + x_str
            else:
                y_str = l[1] + y_str
        elif ('->' in l):
            l = l.split(' -> ')
            output = l[1]
            (op1, operator, op2) = l[0].split(' ')
            operator = operator[0]

            insts.append([op1, op2, operator, output, False])
    f.close()

    # insts -> [operand1, operand2, operator, output_wire, complete_in_round]

    # Find z's
    z_list = []
    ind = 0
    for inst in insts:
        if (inst[3][0] == 'z'):
            z_list.append((inst[3], ind))
        ind += 1

    z_list.sort(reverse=True)

    # Part 1
    new_vals = {}
    z_vals = 0
    while (z_vals < len(z_list)):
        for inst in insts:
            # If we've already done this operation, skip it
            if (inst[4] == True):
                continue
            # Get current operator values, if they exist
            # operator 1
            if (new_vals.get(inst[0]) != None):
                op1 = new_vals.get(inst[0])
            elif (cur_vals.get(inst[0]) != None):
                op1 = cur_vals.get(inst[0])
            else:
                continue
            # operator 2
            if (new_vals.get(inst[1]) != None):
                op2 = new_vals.get(inst[1])
            elif (cur_vals.get(inst[1]) != None):
                op2 = cur_vals.get(inst[1])
            else:
                continue
            # At this point, we have both operators and can perform the instruction
            if (inst[2] == 'A'):
                res = op1 & op2
            elif (inst[2] == 'X'):
                res = op1 ^ op2
            else:
                # OR
                res = op1 | op2
            # We have now finished this operator
            if (inst[3][0] == 'z'):
                z_vals += 1
            inst[4] = True
            new_vals.update({inst[3]:res})

    p1_str = ''

    for z in z_list:
        p1_str += str(new_vals.get(z[0]))

    print(int(p1_str, 2))


    ## PART 2
    # print(int(x_str,2))     # 26526748548813, original x val
    # print(int(y_str, 2))    # 27228562090009, original y val

    # print(test_adder(26526748548813, 27228562090009, insts, z_list))
    # for x in range(1000):
    #     for y in range(1000):
    #         adder_res = test_adder(x, y, insts, z_list)
    #         diff = (x + y) - adder_res
    #         if (diff != 0):
    #             print((x, y, diff, (x + y), adder_res))
    #             exit()


    test_power = 45
    # issue in here somewhere...
    a = test_adder(2**test_power - 1, 1, insts, z_list)
    b = 2**test_power - 1 + 1
    print(a)
    print(b)
    print(a-b)
    # inspection shows that z05 is happening too early (happens before z00)
    # inspection shows that z10 is happening too early (happens before z09)
    # inspection shows that z21 is hpanneing too early (happens before z20)

    a = ['ggk','rhv','z20','hhh','dkr','z05','z15','htp']
    a.sort()
    pt2 = ''
    for entry in a:
        pt2 += entry + ','
    print(pt2[:-1])