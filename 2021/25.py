import sys
from copy import deepcopy

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/25.txt"
with open(input_file) as file:
    directions = [list(line.strip()) for line in file.readlines()]

ROW_NUM = len(directions)
COL_NUM = len(directions[0])


def part_1():
    step = 0
    current_directions = deepcopy(directions)
    still_moving = True
    while still_moving:
        new_directions = [
            [current_directions[row_num][col_num] for col_num in range(COL_NUM)] for row_num in range(ROW_NUM)
        ]
        still_moving = False
        for row_num in range(ROW_NUM):
            for col_num in range(COL_NUM):
                new_col_num = 0 if col_num == COL_NUM - 1 else col_num + 1
                if (
                    current_directions[row_num][col_num] == ">"
                    and current_directions[row_num][new_col_num] == "."
                ):
                    new_directions[row_num][col_num] = "."
                    new_directions[row_num][new_col_num] = ">"
                    still_moving = True
        tmp = deepcopy(new_directions)
        for row_num in range(ROW_NUM):
            for col_num in range(COL_NUM):
                new_row_num = 0 if row_num == ROW_NUM - 1 else row_num + 1
                if (
                    current_directions[row_num][col_num] == "v"
                    and new_directions[new_row_num][col_num] == "."
                ):
                    tmp[row_num][col_num] = "."
                    tmp[new_row_num][col_num] = "v"
                    still_moving = True
        new_directions = tmp
        step += 1
        if not still_moving:
            break
        current_directions = deepcopy(new_directions)
    return step

# no part 2 for last day
def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
