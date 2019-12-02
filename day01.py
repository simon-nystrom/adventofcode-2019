from utils.timing import timing
from functools import reduce

file = open("day01.txt")
puzzle_input = [int(x) for x in file.read().split('\n')]
file.close()

def calculate_fuel(mass):
    return mass // 3 - 2;

def calculate_fuel2(mass, current_fuel = 0):
    req_fuel = calculate_fuel(mass)
    if (req_fuel <= 0):
        return current_fuel
    return calculate_fuel2(req_fuel, current_fuel + req_fuel)

@timing
def part1(puzzle_input):
    return reduce(lambda prev, mass: prev + calculate_fuel(mass), puzzle_input, 0)

@timing
def part2(puzzle_input):
    return reduce(lambda prev, mass: prev + calculate_fuel2(mass), puzzle_input, 0)

part1(puzzle_input)
part2(puzzle_input)