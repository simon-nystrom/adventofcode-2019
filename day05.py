from utils.printing import printed

file = open("day05.txt")
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


def execute(data, inp):
    ram = {}
    i = 0
    output = ''
    while i < len(data):
        instr = str(data[i]).zfill(4)

        op_code = instr[2:4]
        param_mode =  instr[0:2]

        if op_code == '01':
            one, two, addr, *rest = data[i + 1:]
            one, two = unroll_params(data, param_mode, one, two)
            data[addr] = one + two
            i += 4
        elif op_code == '02':
            one, two, addr, *rest = data[i + 1:]
            one, two = unroll_params(data, param_mode, one, two)
            data[addr] = one * two
            i += 4
        elif op_code == '03':
            addr, *rest = data[i+1:]
            data[addr] = inp
            i += 2
        elif op_code == '04':
            addr, *rest = data[i+1:]
            output = data[addr]
            i += 2
        elif op_code == '05': #jump-if-true
            one, two, *rest = data[i + 1:]
            one, two = unroll_params(data, param_mode, one, two)
            if one != 0:
                i = two
            else:
                i += 3
        elif op_code == '06': #jump-if-false
            one, two, *rest = data[i + 1:]
            one, two = unroll_params(data, param_mode, one, two)
            if one == 0:
                i = two
            else:
                i += 3
        elif op_code == '07': #less than
            one, two, addr, *rest = data[i + 1:]
            one, two = unroll_params(data, param_mode, one, two)
            if one < two:
                data[addr] = 1
            else:
                data[addr] = 0
            i += 4
        elif op_code == '08': #equals
            one, two, addr, *rest = data[i + 1:]
            one, two = unroll_params(data, param_mode, one, two)
            if one == two:
                data[addr] = 1
            else:
                data[addr] = 0
            i += 4
        elif op_code == '99':
            return output
        else:
            raise 'Unknown op_code!'
        

@printed
def part1(data):
    return execute(data.copy(), 1)

@printed
def part2(data):
    return execute(data.copy(), 5)

part1(puzzle_input)
part2(puzzle_input)