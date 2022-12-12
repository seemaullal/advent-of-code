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

ROW_NUM = len(grid)
COL_NUM = len(grid[0])

seen = set()


def breadth_first_search(starting_position, is_at_endpoint, comparitor):
    to_visit = deque([(*starting_position, 0)])
    seen = set([starting_position])
    while to_visit:
        current_row, current_col, current_steps = to_visit.popleft()
        print(current_row, current_col)
        if is_at_endpoint(current_row, current_col):
            return current_steps
        for x_dir, y_dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            possible_position_x = current_row + x_dir
            possible_position_y = current_col + y_dir
            if (
                0 <= possible_position_x < ROW_NUM
                and 0 <= possible_position_y < COL_NUM
                and comparitor(
                    current_row, current_col, possible_position_x, possible_position_y
                )
                and (possible_position_x, possible_position_y) not in seen
            ):
                to_visit.append(
                    (possible_position_x, possible_position_y, current_steps + 1)
                )
                seen.add((possible_position_x, possible_position_y))


def part_1():
    def comparitor(current_x, current_y, possible_x, possible_y):
        if  0<=possible_x<ROW_NUM and 0<= possible_y <= COL_NUM:
        boolean = ord(grid[possible_x][possible_y]) <= ord(grid[current_x][current_y]) + 1
        print(grid[current_x][current_y], grid[possible_x][possible_y], boolean)
        return (
            0 <= possible_x < ROW_NUM
            and 0 <= possible_y < COL_NUM
            and ord(grid[possible_x][possible_y]) <= ord(grid[current_x][current_y]) + 1
        )

    def is_at_endpoint(current_row, current_col):
        current_row == END_X and current_col == END_Y

    return breadth_first_search((START_X, START_Y), is_at_endpoint, comparitor)


def part_2():
    def comparitor(current_x, current_y, possible_x, possible_y):
        return ord(grid[current_x][current_y]) - 1 <= ord(grid[possible_x][possible_y])

    def is_at_endpoint(current_row, current_col):
        return grid[current_row][current_col] == "a"

    return breadth_first_search((END_X, END_Y), is_at_endpoint, comparitor)


print(f"Part 1: {part_1()}")
# print(f"Part 2: {part_2()}")
