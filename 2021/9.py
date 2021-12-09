import sys
from copy import deepcopy

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/9.txt"
with open(input_file) as file:
    heights = []
    for line in file.readlines():
        heights.append([int(height) for height in list(line.strip())])

ROW_NUM = len(heights)
COL_NUM = len(heights[0])


def get_low_point_coordinates():
    low_points = []
    for row_num in range(ROW_NUM):
        for col_num in range(COL_NUM):
            eligible = True
            curr = heights[row_num][col_num]
            if row_num != 0 and heights[row_num - 1][col_num] <= curr:
                eligible = False
            if row_num < ROW_NUM - 1 and heights[row_num + 1][col_num] <= curr:
                eligible = False
            if col_num != 0 and heights[row_num][col_num - 1] <= curr:
                eligible = False
            if col_num != COL_NUM - 1 and heights[row_num][col_num + 1] <= curr:
                eligible = False
            if eligible:
                low_points.append(((row_num, col_num)))
    return low_points


def traverse_graph(row, col, basin_size, visited):
    if row < 0 or col < 0 or row == ROW_NUM or col == COL_NUM:
        return 0
    if visited[row][col] == "X" or visited[row][col] == 9:
        return 0
    visited[row][col] = "X"
    return (
        1
        + traverse_graph(row - 1, col, basin_size, visited)
        + traverse_graph(row + 1, col, basin_size, visited)
        + traverse_graph(row, col - 1, basin_size, visited)
        + traverse_graph(row, col + 1, basin_size, visited)
    )


def part_1():
    return sum([heights[row][col] + 1 for row, col in get_low_point_coordinates()])


def part_2():
    visited = deepcopy(heights)
    basin_sizes = []
    low_points = get_low_point_coordinates()
    for row, col in low_points:
        basin_sizes.append(traverse_graph(row, col, 0, visited))
    basin_sizes.sort()
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
