with open("inputs/3.txt") as file:
    wire_1, wire_2 = [line.strip().split(",") for line in file.readlines()]

MOVES = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}


def part_1():
    wire_points = [set(), set()]
    for wire_index, wire in enumerate([wire_1, wire_2]):
        current_position = [0, 0]
        for path in wire:
            direction = path[0]
            distance = int(path[1:])
            x_move, y_move = MOVES[direction]
            for _ in range(distance):
                current_position = [
                    current_position[0] + x_move,
                    current_position[1] + y_move,
                ]
                wire_points[wire_index].add(tuple(current_position))
    min_intersection = float("inf")
    for point_x, point_y in wire_points[0].intersection(wire_points[1]):
        manhattan_distance = abs(point_x) + abs(point_y)
        if manhattan_distance < min_intersection:
            min_intersection = manhattan_distance

    return min_intersection


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
