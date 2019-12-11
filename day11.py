from utils.printing import printed
from intcode.intcode import IntcodeComputer

file = open("day11.txt")
data = [int(x) for x in file.read().split(',')]
file.close()

ROTATIONS = {
    'LEFT': {
        (1,0): (0,1),
        (0,1): (-1,0),
        (-1,0): (0,-1),
        (0,-1): (1,0)
    },
    'RIGHT': {
        (1,0): (0,-1),
        (0,-1): (-1,0),
        (-1,0): (0,1),
        (0,1): (1,0)
    }
}

def turn_left(direction):
    return ROTATIONS['LEFT'][direction]

def turn_right(direction):
    return ROTATIONS['RIGHT'][direction]

def move(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])

def run_program(inp):
    computer = IntcodeComputer(data)
    ret_code = None
    pos = (0,0)
    direction = (0, 1)
    steps = 0
    hull = {}
    current_color = inp
    while ret_code != (0, 0):
        ret_code = computer.step(current_color)
        if ret_code[0] == 1: # we have output
            if steps % 2 == 0:
                color = ret_code[1]
                hull[pos] = color
            else:
                turn = ret_code[1]
                if turn == 0:
                    direction = turn_left(direction)
                else:
                    direction = turn_right(direction)
                pos = move(pos, direction)
                current_color = hull[pos] if pos in hull else 0
                
            steps += 1
    return hull

@printed
def part1():
    hull = run_program(0)    
    return len(hull)

@printed
def part2():
    hull = run_program(1)
    grid = [['' for i in range(48)] for j in range(6)]
    for pos, color in hull.items():
        grid[pos[1]+5][pos[0]+5] = '#' if color is 1 else ''
    
    result = '\n'
    for row in grid:
        s = ''
        for col in row:
            if col != '':
                s += col + ' '
            else: 
                s += '  '
        result += s + '\n'

    return result

part1()
part2()