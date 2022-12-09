with open("inputs/8.txt") as file:
    heights = [[int(num) for num in list(line.strip())] for line in file]

ROW_NUM = len(heights)
COL_NUM = len(heights[0])


def is_on_edge(row, col):
    return row == 0 or row == ROW_NUM - 1 or col == 0 or col == COL_NUM - 1


def max_in_column(starting_row, ending_row, column):
    max_in_col = float("-inf")
    for row_num in range(starting_row, ending_row):
        max_in_col = max(max_in_col, heights[row_num][column])
    return max_in_col


def part_1():
    num_visible = 0
    for row_number in range(ROW_NUM):
        for col_number in range(COL_NUM):
            current_height = heights[row_number][col_number]
            if (
                is_on_edge(row_number, col_number)
                or max(heights[row_number][:col_number]) < current_height
                or max(heights[row_number][col_number + 1 :]) < current_height
                or max_in_column(0, row_number, col_number) < current_height
                or max_in_column(row_number + 1, ROW_NUM, col_number) < current_height
            ):
                num_visible += 1
    return num_visible


def count_visible_trees(
    current_row, current_col, horizontal_move, vertical_move, starting_height
):
    if (
        current_row < 0
        or current_row >= ROW_NUM
        or current_col < 0
        or current_col >= COL_NUM
    ):
        return 0
    elif heights[current_row][current_col] >= starting_height:
        return 1
    return 1 + count_visible_trees(
        current_row + horizontal_move,
        current_col + vertical_move,
        horizontal_move,
        vertical_move,
        starting_height,
    )


def part_2():
    highest_scenic_score = 0
    for row_number in range(ROW_NUM):
        for col_number in range(COL_NUM):
            if is_on_edge(row_number, col_number):
                continue
            current_score = 1
            for x_move, y_move in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                current_score *= count_visible_trees(
                    row_number + x_move,
                    col_number + y_move,
                    x_move,
                    y_move,
                    heights[row_number][col_number],
                )
            highest_scenic_score = max(highest_scenic_score, current_score)
    return highest_scenic_score


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
