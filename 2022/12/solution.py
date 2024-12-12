from collections import deque

with open("inputs/12.txt") as file:
    grid = []
    for row_number, line in enumerate(file):
        grid.append([])
        for col_number, elevation in enumerate(line.strip()):
            if elevation == "S":
                START_ROW, START_COL, elevation = row_number, col_number, "a"
            elif elevation == "E":
                END_ROW, END_COL, elevation = row_number, col_number, "z"
            grid[-1].append(ord(elevation) - ord("a"))


def is_within_grid(row_number, column_number):
    return 0 <= row_number < len(grid) and 0 <= column_number < len(grid[0])


def breadth_first_search(stop_searching):
    to_visit = deque([(END_ROW, END_COL, 0)])
    seen = set([(END_ROW, END_COL)])
    while to_visit:
        row, col, steps = to_visit.popleft()
        if stop_searching(row, col):
            return steps
        for row_dir, col_dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if (
                is_within_grid(row + row_dir, col + col_dir)
                and grid[row + row_dir][col + col_dir] + 1 >= grid[row][col]
                and (row + row_dir, col + col_dir) not in seen
            ):
                to_visit.append((row + row_dir, col + col_dir, steps + 1))
                seen.add((row + row_dir, col + col_dir))


print("Part 1:", breadth_first_search(lambda r, c: r == START_ROW and c == START_COL))
print("Part 2:", breadth_first_search(lambda r, c: grid[r][c] == 0))
