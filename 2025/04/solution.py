from pathlib import Path

DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))


def is_accessible(grid, row, col):
    if grid[row][col] != "@":
        return False
    num_rolls = 0
    for row_d, col_d in DIRECTIONS:
        to_check_row = row + row_d
        to_check_col = col + col_d
        if 0 <= to_check_row < len(grid) and 0 <= to_check_col < len(grid[0]):
            if grid[to_check_row][to_check_col] == "@":
                num_rolls += 1
    return num_rolls < 4


def part_1(grid):
    result = 0
    for row_num in range(len(grid)):
        for col_num in range(len(grid[0])):
            if is_accessible(grid, row_num, col_num):
                result += 1
    return result


def part_2(grid):
    grid_copy = [row[:] for row in grid]
    result = 0
    changed = True
    while changed:
        changed = False
        for row_num in range(len(grid_copy)):
            for col_num in range(len(grid_copy[0])):
                if is_accessible(grid_copy, row_num, col_num):
                    changed = True
                    result += 1
                    grid_copy[row_num][col_num] = "."
    return result


def solve():
    grid = [
        list(row) for row in Path("inputs/input.txt").read_text().strip().splitlines()
    ]
    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")


if __name__ == "__main__":
    solve()
