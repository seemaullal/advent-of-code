from pathlib import Path
from collections import Counter


def find_start_column(grid):
    return grid[0].index("S")


def count_splits(grid):
    height, width = len(grid), len(grid[0])
    start_row = 0
    start_col = find_start_column(grid)

    splits = 0
    beams = {start_col}

    for row_number in range(start_row + 1, height):
        next_beams = set()
        for column_number in beams:
            if grid[row_number][column_number] == "^":
                splits += 1
                next_beams.add(column_number - 1)
                next_beams.add(column_number + 1)
            else:
                next_beams.add(column_number)

        beams = next_beams

    return splits


def count_timelines(grid):
    height, width = len(grid), len(grid[0])
    start_row = 0
    start_col = find_start_column(grid)


    timelines = {start_col: 1}

    for row_number in range(start_row + 1, height):
        next_timelines = Counter()
        for column_number, count in timelines.items():
            if grid[row_number][column_number] == "^":
                next_timelines[column_number - 1] = next_timelines[column_number - 1] + count
                next_timelines[column_number + 1] = next_timelines[column_number + 1] + count
            else:
                next_timelines[column_number] = next_timelines[column_number] + count

        timelines = next_timelines

    return timelines.total()


def solve():
    grid = [list(row) for row in Path("inputs/input.txt").read_text().strip().splitlines()]

    part1 = count_splits(grid)
    print(f"Part 1: {part1}")

    part2 = count_timelines(grid)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    solve()
