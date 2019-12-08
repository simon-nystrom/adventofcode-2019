from utils.printing import printed
from itertools import permutations

file = open("day07.txt")
puzzle_input = [int(x) for x in file.read().split(',')]
file.close()


def unroll_params(data, param_mode, param1, param2):
    one, two = param1, param2
    if param_mode != '00':
        if param_mode[1] != '1':
            one = data[param1]
        if param_mode[0] != '1':
            two = data[param2]
    else:
        one = data[param1]
        two = data[param2]
    return one, two


def execute(data, inp, phase_setting, ptr=0, prev_out=0):
    i = ptr
    output = ''
    while i < len(data):
        instr = str(data[i]).zfill(4)

        op_code = instr[2:4]
        param_mode = instr[0:2]

        if op_code == '01':
            one, two, addr, *_ = data[i + 1:]
            one, two = unroll_params(data, param_mode, one, two)
            data[addr] = one + two
            i += 4
        elif op_code == '02':
            one, two, addr, *_ = data[i + 1:]
            one, two = unroll_params(data, param_mode, one, two)
            data[addr] = one * two
            i += 4
        elif op_code == '03':
            addr, *_ = data[i+1:]
            if phase_setting != -1:
                data[addr] = phase_setting
                phase_setting = -1
            else:
                data[addr] = inp
            i += 2
        elif op_code == '04':
            addr, *_ = data[i+1:]
            output = data[addr]
            i += 2
            return output, i, False
        elif op_code == '05':  # jump-if-true
            one, two, *_ = data[i + 1:]
            one, two = unroll_params(data, param_mode, one, two)
            if one != 0:
                i = two
            else:
                i += 3
        elif op_code == '06':  # jump-if-false
            one, two, *_ = data[i + 1:]
            one, two = unroll_params(data, param_mode, one, two)
            if one == 0:
                i = two
            else:
                i += 3
        elif op_code == '07':  # less than
            one, two, addr, *_ = data[i + 1:]
            one, two = unroll_params(data, param_mode, one, two)
            if one < two:
                data[addr] = 1
            else:
                data[addr] = 0
            i += 4
        elif op_code == '08':  # equals
            one, two, addr, *_ = data[i + 1:]
            one, two = unroll_params(data, param_mode, one, two)
            if one == two:
                data[addr] = 1
            else:
                data[addr] = 0
            i += 4
        elif op_code == '99':
            return prev_out, i, True
        else:
            raise 'Unknown op_code!'


@printed
def part1(data):
    max_thruster_signal = 0
    perms = list(permutations([0, 1, 2, 3, 4]))
    for perm in perms:
        p1, p2, p3, p4, p5 = perm
        out, _, _ = execute(data.copy(), 0, p1)
        out, _, _ = execute(data.copy(), out, p2)
        out, _, _ = execute(data.copy(), out, p3)
        out, _, _ = execute(data.copy(), out, p4)
        out, _, _ = execute(data.copy(), out, p5)
        max_thruster_signal = max(max_thruster_signal, out)
    return max_thruster_signal


@printed
def part2(data):
    max_thruster_signal = 0
    perms = list(permutations([5, 6, 7, 8, 9]))
    for perm in perms:
        out1, out2, out3, out4, out5 = [0] * 5
        ptr1, ptr2, ptr3, ptr4, ptr5 = [0] * 5
        data1, data2, data3, data4, data5 = puzzle_input.copy(), puzzle_input.copy(
        ), puzzle_input.copy(), puzzle_input.copy(), puzzle_input.copy()
        halt = False
        p1, p2, p3, p4, p5 = perm
        while not halt:
            out1, ptr1, _ = execute(data1, out5, p1, ptr1, out1)
            out2, ptr2, _ = execute(data2, out1, p2, ptr2, out2)
            out3, ptr3, _ = execute(data3, out2, p3, ptr3, out3)
            out4, ptr4, _ = execute(data4, out3, p4, ptr4, out4)
            out5, ptr5, halt = execute(data5, out4, p5, ptr5, out5)
            p1, p2, p3, p4, p5 = -1, -1, -1, -1, -1
        max_thruster_signal = max(max_thruster_signal, out5)
    return max_thruster_signal


part1(puzzle_input)
part2(puzzle_input)
