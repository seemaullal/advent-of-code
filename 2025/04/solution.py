from pathlib import Path

DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))


def number_adjacent_rolls(grid, row, col):
    num_rolls = 0
    for row_d, col_d in DIRECTIONS:
        if 0 <= row + row_d < len(grid) and 0 <= col + col_d < len(grid[0]):
            if grid[row + row_d][col + col_d] == "@":
                num_rolls += 1
    return num_rolls


def is_accessible(grid, row, col):
    return grid[row][col] == "@" and number_adjacent_rolls(grid, row, col) < 4


def part_1(grid):
    return sum(
        is_accessible(grid, row_num, col_num)
        for row_num in range(len(grid))
        for col_num in range(len(grid[0]))
    )


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
