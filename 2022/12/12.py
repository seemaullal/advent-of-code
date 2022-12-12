from collections import deque

with open("inputs/12.txt") as file:
    grid = []
    for row_number, line in enumerate(file):
        grid.append([])
        for col_number, elevation in enumerate(line.strip()):
            if elevation == "S":
                START_X = row_number
                START_Y = col_number
                elevation = "s"
            elif elevation == "E":
                END_X, END_Y = (row_number, col_number)
                elevation = "z"
            grid[-1].append(elevation)

ROW_NUM = row_number
COL_NUM = col_number

seen = set()


def breadth_first_search(starting_position, stop_searching, comparitor):
    to_visit = deque([(*starting_position, 0)])
    seen = set([starting_position])
    while to_visit:
        current_row, current_col, current_steps = to_visit.popleft()
        if stop_searching(current_row, current_col):
            return current_steps
        for row_dir, col_dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            possible_row = current_row + row_dir
            possible_col = current_col + col_dir
            if (
                is_within_grid(possible_row, possible_col)
                and comparitor(current_row, current_col, possible_row, possible_col)
                and (possible_row, possible_col) not in seen
            ):
                to_visit.append((possible_row, possible_col, current_steps + 1))
                seen.add((possible_row, possible_col))


def is_within_grid(row_number, column_number):
    return 0 <= row_number < ROW_NUM and 0 <= column_number < COL_NUM


def part_1():
    def comparitor(current_x, current_y, possible_x, possible_y):
        return ord(grid[possible_x][possible_y]) <= ord(grid[current_x][current_y]) + 1

    def stop_searching(current_x, current_y):
        return current_x == END_X and current_y == END_Y

    return breadth_first_search((START_X, START_Y), stop_searching, comparitor)


def part_2():
    def comparitor(current_x, current_y, possible_x, possible_y):
        return ord(grid[current_x][current_y]) <= ord(grid[possible_x][possible_y]) + 1

    def stop_searching(current_x, current_y):
        return grid[current_x][current_y] == "a"

    return breadth_first_search((END_X, END_Y), stop_searching, comparitor)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
