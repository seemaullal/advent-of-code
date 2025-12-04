from pathlib import Path

DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))


def part_1(grid):
    result = 0
    for row_num in range(len(grid)):
        for col_num in range(len(grid[0])):
            if grid[row_num][col_num] != "@":
                continue
            num_towels = 0
            for row_d, col_d in DIRECTIONS:
                to_check_row = row_num + row_d
                to_check_col = col_num + col_d
                if 0 <= to_check_row < len(grid) and 0 <= to_check_col < len(grid[0]):
                    if grid[to_check_row][to_check_col] == "@":
                        num_towels += 1
            if num_towels < 4:
                result += 1
    return result


def part_2(grid):
    result = 0
    while True:
        changed = False
        for row_num in range(len(grid)):
            for col_num in range(len(grid[0])):
                if grid[row_num][col_num] != "@":
                    continue
                num_towels = 0
                for row_d, col_d in DIRECTIONS:
                    to_check_row = row_num + row_d
                    to_check_col = col_num + col_d
                    if 0 <= to_check_row < len(grid) and 0 <= to_check_col < len(grid[0]):
                        if grid[to_check_row][to_check_col] == "@":
                            num_towels += 1
                if num_towels < 4:
                    changed = True
                    result += 1
                    grid[row_num][col_num] = '.'
        if not changed:
            break
    return result


def solve():
    grid = [
        list(row) for row in Path("inputs/input.txt").read_text().strip().splitlines()
    ]
    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")


if __name__ == "__main__":
    solve()
