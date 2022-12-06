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
                current_position[0] += x_move
                current_position[1] += y_move
                wire_points[wire_index].add(tuple(current_position))
    min_intersection = float("inf")
    for point_x, point_y in wire_points[0].intersection(wire_points[1]):
        min_intersection = min(min_intersection, abs(point_x) + abs(point_y))
    return min_intersection


def part_2():
    wire_points = [set(), set()]
    steps_to_points = [{}, {}]
    for wire_index, wire in enumerate([wire_1, wire_2]):
        current_position = [0, 0]
        steps = 0
        for path in wire:
            direction = path[0]
            distance = int(path[1:])
            x_move, y_move = MOVES[direction]
            for _ in range(distance):
                steps += 1
                current_position[0] += x_move
                current_position[1] += y_move
                current_position_tuple = tuple(current_position)
                wire_points[wire_index].add(current_position_tuple)
                if current_position_tuple not in steps_to_points[wire_index]:
                    steps_to_points[wire_index][current_position_tuple] = steps
    min_intersection_steps = float("inf")
    for point in wire_points[0].intersection(wire_points[1]):
        min_intersection_steps = min(
            min_intersection_steps,
            steps_to_points[0][point] + steps_to_points[1][point],
        )
    return min_intersection_steps


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
