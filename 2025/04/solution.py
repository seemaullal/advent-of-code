from pathlib import Path

DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))


def count_adjacent_rolls(grid, row, col):
    num_rolls = 0
    for dr, dc in DIRECTIONS:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            if grid[new_row][new_col] == "@":
                num_rolls += 1
    return num_rolls


def is_accessible(grid, row, col):
    return grid[row][col] == "@" and count_adjacent_rolls(grid, row, col) < 4


def part_1(grid):
    return sum(
        is_accessible(grid, row, col)
        for row in range(len(grid))
        for col in range(len(grid[0]))
    )


def part_2(grid):
    grid_copy = [row[:] for row in grid]
    removed_count = 0
    while True:
        accessible_positions = [
            (row, col)
            for row in range(len(grid))
            for col in range(len(grid[0]))
            if is_accessible(grid_copy, row, col)
        ]
        if not accessible_positions:
            break
        for row, col in accessible_positions:
            grid_copy[row][col] = "."
        removed_count += len(accessible_positions)
    return removed_count


def solve():
    grid = [
        list(row) for row in Path("inputs/input.txt").read_text().strip().splitlines()
    ]
    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")


if __name__ == "__main__":
    solve()
