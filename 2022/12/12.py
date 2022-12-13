from collections import deque

with open("inputs/12.txt") as file:
    grid = []
    for row_number, line in enumerate(file):
        grid.append([])
        for col_number, elevation in enumerate(line.strip()):
            if elevation == "S":
                START_X, START_Y, elevation = row_number, col_number, "a"
            elif elevation == "E":
                END_X, END_Y, elevation = row_number, col_number, "z"
            grid[-1].append(ord(elevation) - ord("a"))


def is_within_grid(row_number, column_number):
    return 0 <= row_number < len(grid) and 0 <= column_number < len(grid[0])


def breadth_first_search(stop_searching):
    to_visit = deque([(END_X, END_Y, 0)])
    seen = set([(END_X, END_Y)])
    while to_visit:
        curr_row, curr_col, curr_steps = to_visit.popleft()
        if stop_searching(curr_row, curr_col):
            return curr_steps
        for row_dir, col_dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            possible_row = curr_row + row_dir
            possible_col = curr_col + col_dir
            if (
                is_within_grid(possible_row, possible_col)
                and grid[possible_row][possible_col] + 1 >= grid[curr_row][curr_col]
                and (possible_row, possible_col) not in seen
            ):
                to_visit.append((possible_row, possible_col, curr_steps + 1))
                seen.add((possible_row, possible_col))


def part_1():
    return breadth_first_search(lambda row, col: row == START_X and col == START_Y)


def part_2():
    return breadth_first_search(lambda row, col: grid[row][col] == 0)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
