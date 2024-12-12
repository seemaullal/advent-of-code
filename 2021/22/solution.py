import sys
import re
from dataclasses import dataclass


@dataclass
class Step:
    instruction: str
    x_start: int
    x_end: int
    y_start: int
    y_end: int
    z_start: int
    z_end: int


input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/22.txt"
with open(input_file) as file:
    steps = []
    for line in file:
        instruction, rest = line.strip().split()
        x_start, x_end, y_start, y_end, z_start, z_end = map(int, re.findall(r"-?\d+", rest))
        steps.append(Step(instruction, x_start, x_end, y_start, y_end, z_start, z_end))


def part_1():
    on = set()
    for step in steps:
        x_start = max(step.x_start, -50)
        x_end = min(step.x_end, 50)
        y_start = max(step.y_start, -50)
        y_end = min(step.y_end, 50)
        z_start = max(step.z_start, -50)
        z_end = min(step.z_end, 50)
        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                for z in range(z_start, z_end + 1):
                    if step.instruction == "on":
                        on.add((x, y, z))
                    else:
                        on.discard((x, y, z))
    return len(on)


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
