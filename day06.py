from utils.printing import printed

file = open("day06.txt")
puzzle_input = [x for x in file.read().split('\n')]
file.close()

def build_map(puzzle_input):
    orbiter_map = {}
    for s in puzzle_input:
        base, orbiter = s.split(')')
        if orbiter in orbiter_map:
            orbiter_map[orbiter].append(base)
        else:
            orbiter_map[orbiter] = [base]    
    return orbiter_map

def count_orbits(orbiter_map, key, num = 0):
    for k in orbiter_map[key]:
        if k in orbiter_map:
            num = count_orbits(orbiter_map, k, num + 1)
    return num

@printed
def part1(puzzle_input):
    orbiter_map = build_map(puzzle_input)
    count = 0
    for key in orbiter_map.keys():
        count += count_orbits(orbiter_map, key) + 1
    return count

def find_path(orbiter_map, src, dst, visited = {}, steps = 0):
    if src == dst:
        return steps - 2 # don't count start and end nodes as steps
    orbiters = orbiter_map[src]
    curr = 0
    for orbiter in orbiters:
        if orbiter in orbiter_map and not orbiter in visited:
            visited[orbiter] = True
            curr = curr + find_path(orbiter_map, orbiter, dst, visited, steps + 1)
    return curr

def build_map_2(puzzle_input):
    planet_map = {}
    for s in puzzle_input:
        base, orbiter = s.split(')')
        if base in planet_map:
            planet_map[base].append(orbiter)
        else:
            planet_map[base] = [orbiter]
        if orbiter in planet_map:
            planet_map[orbiter].append(base)
        else:
            planet_map[orbiter] = [base]
    return planet_map

@printed
def part2(puzzle_input):
    planet_map = build_map_2(puzzle_input)
    return find_path(planet_map, 'YOU', 'SAN')

part1(puzzle_input)
part2(puzzle_input)