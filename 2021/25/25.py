import sys
import time

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/25.txt"
with open(input_file) as file:
    directions = [list(line.strip()) for line in file.readlines()]

ROW_NUM = len(directions)
COL_NUM = len(directions[0])


def part_1():
    step = 0
    still_moving = True
    global directions
    while still_moving:
        dir_2 = [[directions[r][c] for c in range(COL_NUM)] for r in range(ROW_NUM)]
        still_moving = False
        for row_num in range(ROW_NUM):
            for col_num in range(COL_NUM):
                new_col_num = 0 if col_num == COL_NUM - 1 else col_num + 1
                if directions[row_num][col_num] == ">" and directions[row_num][new_col_num] == ".":
                    dir_2[row_num][col_num] = "."
                    dir_2[row_num][new_col_num] = ">"
                    still_moving = True
        dir_3 = [[dir_2[r][c] for c in range(COL_NUM)] for r in range(ROW_NUM)]
        for row_num in range(ROW_NUM):
            for col_num in range(COL_NUM):
                new_row_num = 0 if row_num == ROW_NUM - 1 else row_num + 1
                if dir_2[row_num][col_num] == "v" and dir_2[new_row_num][col_num] == ".":
                    dir_3[row_num][col_num] = "."
                    dir_3[new_row_num][col_num] = "v"
                    still_moving = True
        step += 1
        directions = dir_3
    return step


# no part 2 for last day
def part_2():
    pass


start = time.perf_counter()
print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
stop = time.perf_counter()
print(f"Finished in {stop - start:0.4f} seconds")
