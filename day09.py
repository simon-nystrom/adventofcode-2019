from utils.printing import printed
from intcode.intcode import IntcodeComputer

file = open("day09.txt")
puzzle_input = [int(x) for x in file.read().split(',')]
file.close()

@printed
def part1(data):
    computer = IntcodeComputer(data)
    ret_code = None
    output = None
    while ret_code != (0, 0):
        ret_code = computer.step(1)
        if ret_code[0] == 1:
            output = ret_code[1]
    return output

@printed
def part2(data):
    computer = IntcodeComputer(data)
    ret_code = None
    output = None
    while ret_code != (0, 0):
        ret_code = computer.step(2)
        if ret_code[0] == 1:
            output = ret_code[1]
    return output


part1(puzzle_input)
part2(puzzle_input)
