import sys
import re

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/17.txt"
with open(input_file) as file:
    x_start, x_end, y_start, y_end = map(int, re.findall(r"-?\d+", file.read()))


def has_path_to_target(x_velocity, y_velocity):
    x, y = 0, 0
    while x <= x_end and y >= y_start:
        x, y = x + x_velocity, y + y_velocity
        # in the target area
        if x_start <= x <= x_end and y_start <= y <= y_end:
            return True
        x_velocity = x_velocity - 1 if x_velocity > 0 else 0
        y_velocity -= 1
    # never reached the target area
    return False


def part_1():
    y_velocity = -y_start - 1
    y = 0
    while y_velocity > 0:
        y += y_velocity
        y_velocity -= 1
    return y


def part_2():
    count = 0
    for x_velocity in range(x_end + 1):
        for y_velocity in range(y_start, -y_start):
            if has_path_to_target(x_velocity, y_velocity):
                count += 1
    return count


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
