import sys
from copy import deepcopy

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/11.txt"
with open(input_file) as file:
    energy = [list(map(int, list(line.strip()))) for line in file.readlines()]

ROW_NUM = len(energy)
COL_NUM = len(energy[0])


def get_adjacent_coordinates(x, y):
    adjacent = []
    for x_dir in (-1, 0, 1):
        for y_dir in (-1, 0, 1):
            if 0 <= x + x_dir < ROW_NUM and 0 <= y + y_dir < COL_NUM:
                adjacent.append((x + x_dir, y + y_dir))
    return adjacent


def solve_both_parts():
    current_energy = deepcopy(energy)
    flashes_after_hundred_steps = None
    num_flashes = 0
    current_step = 0
    while current_step < 100 or not all_flashing(current_energy):
        if current_step == 100:
            flashes_after_hundred_steps = num_flashes
        for row_num in range(ROW_NUM):
            for col_num in range(COL_NUM):
                current_energy[row_num][col_num] += 1
        still_flashing = True
        while still_flashing:
            still_flashing = False
            for row_num in range(ROW_NUM):
                for col_num in range(COL_NUM):
                    if current_energy[row_num][col_num] > 9:
                        num_flashes += 1
                        current_energy[row_num][col_num] = 0
                        for x, y in get_adjacent_coordinates(row_num, col_num):
                            if current_energy[x][y] != 0:
                                current_energy[x][y] += 1
                            if current_energy[x][y] > 9:
                                still_flashing = True
        current_step += 1
    return flashes_after_hundred_steps, current_step


def all_flashing(energy):
    for row in energy:
        if any([cell for cell in row if cell != 0]):
            return False
    return True


def part_1():
    return solve_both_parts()[0]


def part_2():
    return solve_both_parts()[1]


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
