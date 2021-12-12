import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/11.txt"
with open(input_file) as file:
    energy = [list(map(int, list(line.strip()))) for line in file.readlines()]

ROW_NUM = len(energy)
COL_NUM = len(energy[0])


def get_adjacent_coordinates(x_coordinate, y_coordinate):
    adjacent = []
    for x_dir, y_dir in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
        current_x = x_coordinate + x_dir
        current_y = y_coordinate + y_dir
        if 0 <= current_x < ROW_NUM and 0 <= current_y < COL_NUM:
            adjacent.append((current_x, current_y))
    return adjacent


def part_1():
    num_flashes = 0
    for _ in range(100):
        for row_num in range(len(energy)):
            for col_num in range(len(energy[row_num])):
                energy[row_num][col_num] += 1
        still_flashing = True
        while still_flashing:
            still_flashing = False
            for row_num in range(len(energy)):
                for col_num in range(len(energy[row_num])):
                    if energy[row_num][col_num] > 9:
                        num_flashes += 1
                        energy[row_num][col_num] = 0
                        for x_coord, y_coord in get_adjacent_coordinates(row_num, col_num):
                            if energy[x_coord][y_coord] != 0:
                                energy[x_coord][y_coord] += 1
                            if energy[x_coord][y_coord] > 9:
                                still_flashing = True
    return num_flashes


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
