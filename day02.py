from utils.timing import timing

file = open("day02.txt")
puzzle_input = [int(x) for x in file.read().split(',')]
file.close()

def solve(puzzle_input, arg1, arg2):
    data = puzzle_input.copy()
    data[1] = arg1
    data[2] = arg2
    for i in range(0, len(data), 4):
        slice = data[i:]
        if len(slice) >= 4:
            op_code, pos1, pos2, result_pos, *rest = slice
            if op_code == 1:
                data[result_pos] = data[pos1] + data[pos2]
            elif op_code == 2:
                data[result_pos] = data[pos1] * data[pos2]
            else:
                return data[0]

@timing
def part1(puzzle_input, arg1, arg2):
    return solve(puzzle_input, arg1, arg2)

@timing
def part2(puzzle_input):
    for i in range(99):
        for j in range(99):
            if solve(puzzle_input, i, j) == 19690720:
                return 100 * i + j
            



part1(puzzle_input, 12, 2)
part2(puzzle_input)

