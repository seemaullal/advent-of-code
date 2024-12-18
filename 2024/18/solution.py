from collections import deque
from re import findall

part_1 = 0
part_2 = 0

DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))
GRID_SIZE = 70


def get_digits(string):
    return [int(digit) for digit in findall(r"\d+", string)]


rows = open("inputs/input.txt").read().strip().splitlines()

current_grid = [["." for _ in range(GRID_SIZE + 1)] for _ in range(GRID_SIZE + 1)]
for index, row in enumerate(rows):
    x, y = get_digits(row)
    if 0 <= y <= GRID_SIZE and 0 <= x <= GRID_SIZE:
        current_grid[y][x] = "#"

    to_visit = deque([(0, 0, 0)])
    seen = set()
    unreachable = True
    while to_visit:
        current_steps, current_row, current_column = to_visit.popleft()
        if current_row == GRID_SIZE and current_column == GRID_SIZE:
            if index == 1023:
                part_1 = current_steps
            unreachable = False
            break
        if (current_row, current_column) in seen:
            continue
        seen.add((current_row, current_column))
        for row_direction, column_direction in DIRECTIONS:
            next_row = current_row + row_direction
            next_column = current_column + column_direction
            if (
                0 <= next_row <= GRID_SIZE
                and 0 <= next_column <= GRID_SIZE
                and current_grid[next_row][next_column] != "#"
            ):
                to_visit.append((current_steps + 1, next_row, next_column))
    if unreachable:
        part_2 = f"{x},{y}"
        break

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
