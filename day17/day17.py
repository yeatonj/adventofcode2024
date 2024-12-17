# Written by Josh Yeaton on 1/17/24
# For Advent of Code 2024

def get_combo_op_val(combo_op_num, reg_vals):
    if (combo_op_num <=3):
        return combo_op_num
    elif (combo_op_num == 4):
        return reg_vals[0]
    elif (combo_op_num == 5):
        return reg_vals[1]
    elif (combo_op_num == 6):
        return reg_vals[2]
    else:
        print('Error, attempting combo op out of bounds')
        exit()

def adv(reg_vals, operand):
    reg_vals[0] = reg_vals[0] // (2**get_combo_op_val(operand, reg_vals))

def bxl(reg_vals, operand):
    reg_vals[1] = operand ^ reg_vals[1]

def bst(reg_vals, operand):
    reg_vals[1] = get_combo_op_val(operand, reg_vals) % 8

def jnz(reg_vals, operand, ip):
    if (reg_vals[0] == 0):
        return ip
    else:
        return operand
    
def bxc(reg_vals):
    reg_vals[1] = reg_vals[1] ^ reg_vals[2]

def out(reg_vals, operand):
    res = get_combo_op_val(operand, reg_vals) % 8
    return str(res)

def bdv(reg_vals, operand):
    reg_vals[1] = reg_vals[0] // (2**get_combo_op_val(operand, reg_vals))

def cdv(reg_vals, operand):
    reg_vals[2] = reg_vals[0] // (2**get_combo_op_val(operand, reg_vals))

def run_program(program, reg_vals):
    output = ''
    ip = 0
    while (ip < len(program)):
        instr = program[ip]
        op = program[ip + 1]
        if (instr == 0):
            adv(reg_vals, op)
            ip += 2
        elif (instr == 1):
            bxl(reg_vals, op)
            ip += 2
        elif (instr == 2):
            bst(reg_vals, op)
            ip += 2
        elif (instr == 3):
            res = jnz(reg_vals, op, ip)
            if (res == ip):
                ip += 2
            else:
                ip = res
        elif (instr == 4):
            bxc(reg_vals)
            ip += 2
        elif (instr == 5):
            output += (out(reg_vals, op) + ',')
            ip += 2
        elif (instr == 6):
            bdv(reg_vals, op)
            ip += 2
        elif (instr == 7):
            cdv(reg_vals, op)
            ip += 2
    return output


if __name__ == "__main__":
    filename = 'data_test.txt'
    filename = 'data.txt'
    f = open(filename)

    reg_a = int(f.readline().strip().split(': ')[1])
    reg_b = int(f.readline().strip().split(': ')[1])
    reg_c = int(f.readline().strip().split(': ')[1])
    reg_vals = [reg_a, reg_b, reg_c]

    f.readline()
    program_str = f.readline().strip().split(': ')[1]
    program = program_str.split(',')
    program = [int(i) for i in program]
    f.close()

    ip = 0

    ## Part A
    output = run_program(program, reg_vals)
    print(output[:-1])
    print()
    print()

    ## Part B
    a_val = 0
    increase_factor = 8 # found by checking assembly
    # First 16
    add_val_ind = 0
    cur_match_ind = len(program_str) - 1
    while (cur_match_ind >= 0):
        cur_str = program_str[cur_match_ind:]
        while(True):
            reg_vals = [a_val, 0, 0]
            output = run_program(program, reg_vals)
            output = output[:-1]
            if (output == cur_str):
                break
            a_val += 1
        if (output == program_str):
            break
        a_val *= increase_factor
        cur_match_ind -= 2
    # print(output[:-1])
    print(a_val)




