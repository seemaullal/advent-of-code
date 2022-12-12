from collections import deque

with open("inputs/12.txt") as file:
    grid = []
    for row_number, line in enumerate(file):
        grid.append([])
        for col_number, elevation in enumerate(line.strip()):
            if elevation == "S":
                START_X, START_Y = row_number, col_number
                elevation = "s"
            elif elevation == "E":
                END_X, END_Y = row_number, col_number
                elevation = "z"
            grid[-1].append(ord(elevation) - ord("a"))


def is_within_grid(row_number, column_number):
    return 0 <= row_number < len(grid) and 0 <= column_number < len(grid[0])


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


def part_1():
    comparitor = lambda cx, cy, px, py: grid[px][py] <= grid[cx][cy] + 1
    stop = lambda row, col: row == END_X and col == END_Y

    return breadth_first_search((START_X, START_Y), stop, comparitor)


def part_2():
    comparitor = lambda cx, cy, px, py: grid[px][py] + 1 >= grid[cx][cy]
    stop = lambda row, col: grid[row][col] == 0

    return breadth_first_search((END_X, END_Y), stop, comparitor)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
