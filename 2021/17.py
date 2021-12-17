import sys
import re

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/17.txt"
with open(input_file) as file:
    x_start, x_end, y_start, y_end = map(int, re.findall(r"-?\d+", file.read()))


def calculate_max_y(x_velocity, y_velocity):
    x, y = 0, 0
    max_y = float("-inf")
    while x < x_end and y > y_start:
        x, y = x + x_velocity, y + y_velocity
        if y > max_y:
            max_y = y
        # in the target area
        if x_start <= x <= x_end and y_start <= y <= y_end:
            return max_y
        x_velocity = x_velocity - 1 if x_velocity > 0 else 0
        y_velocity -= 1
    # never reached the target area
    return float("-inf")


def part_1():
    possible_y_values = set()
    for x_velocity in range(x_end + 1):
        for y_velocity in range(y_start, 1000):
            possible_y_values.add(calculate_max_y(x_velocity, y_velocity))
    return max(possible_y_values)


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
