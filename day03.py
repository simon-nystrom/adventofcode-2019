from utils.printing import printed

file = open("day03.txt")
wire_a, wire_b = [x.split(',') for x in file.read().split('\n')]
file.close()

def get_delta(dir):
    if dir == 'R':
        return (1, 0)
    elif dir == 'L':
        return (-1, 0)
    elif dir == 'U':
        return (0, 1)
    else:
        return (0, -1)

def place_wire(wire):
    visited = { (0, 0): 0 }
    pos = (0, 0)
    num_steps = 0
    for instruction in wire:
        direction, length = instruction[0], int(instruction[1:])
        delta_x, delta_y = get_delta(direction)
        for i in range(1, length + 1):
            pos = (pos[0] + delta_x, pos[1] + delta_y)
            num_steps += 1
            if not pos in visited:
                visited[pos] = num_steps
    return visited


def find_intersections(existing_wire, wire):
    visited = { (0, 0): 0 }
    intersections = {}
    min_intersection_dist = -1
    num_steps = 0
    pos = (0, 0)
    for instruction in wire:
        direction, length = instruction[0], int(instruction[1:])
        delta_x, delta_y = get_delta(direction)
        for i in range(1, length + 1):
            pos = (pos[0] + delta_x, pos[1] + delta_y)
            num_steps += 1
            if not pos in visited:
                visited[pos] = num_steps
            if pos in existing_wire:
                min_intersection_dist = abs(pos[0]) + abs(pos[1]) if min_intersection_dist == -1 else min(min_intersection_dist, abs(pos[0]) + abs(pos[1]))
                intersections[pos] = True
    return intersections, visited, min_intersection_dist


@printed
def part1(wire_a, wire_b):
    visited_wire_a = place_wire(wire_a)
    _, _, min_dist_intersect = find_intersections(visited_wire_a, wire_b)
    return min_dist_intersect

@printed
def part2(wire_a, wire_b):
    visited_wire_a = place_wire(wire_a)
    intersections, visited_wire_b, _ = find_intersections(visited_wire_a, wire_b)
    return min(map(lambda x: visited_wire_a[x] + visited_wire_b[x], intersections.keys()))
        

    

part1(wire_a, wire_b)
part2(wire_a, wire_b)
