part_1 = 0
part_2 = 0

starting_row, starting_colummn = None, None
with open("inputs/input.txt", "r") as file:
    grid, instructions = file.read().split("\n\n")
    grid = [list(row) for row in grid.split("\n")]

DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
NUM_ROWS = len(grid)
NUM_COLS = len(grid[0])


for row in range(NUM_ROWS):
    for column in range(NUM_COLS):
        if grid[row][column] == "@":
            grid[row][column] = "."
            starting_row, starting_column = row, column

current_row, current_column = starting_row, starting_column
for instruction in instructions:
    if instruction == "\n":
        continue
    row_direction, col_direction = DIRECTIONS[instruction]
    new_row = current_row + row_direction
    new_column = current_column + col_direction
    if grid[new_row][new_column] == "#":
        continue
    elif grid[new_row][new_column] == ".":
        current_row = new_row
        current_column = new_column
    else:
        to_visit = [(current_row, current_column)]
        seen = set()
        ok = True
        while to_visit:
            row, column = to_visit.pop()
            if (row, column) in seen:
                continue
            seen.add((row, column))
            new_row, new_column = row + row_direction, column + col_direction
            if grid[new_row][new_column] == "#":
                ok = False
                break
            if grid[new_row][new_column] == "O":
                to_visit.append((new_row, new_column))
            if grid[new_row][new_column] == "[":
                to_visit.append((new_row, new_column))
                to_visit.append((new_row, new_column + 1))
            if grid[new_row][new_column] == "]":
                to_visit.append((new_row, new_column))
                to_visit.append((new_row, new_column - 1))
        if not ok:
            continue
        while len(seen) > 0:
            for row, column in sorted(seen):
                new_row, new_column = row + row_direction, column + col_direction
                if (new_row, new_column) not in seen:
                    grid[new_row][new_column] = grid[row][column]
                    grid[row][column] = "."
                    seen.remove((row, column))
        current_row = current_row + row_direction
        current_column = current_column + col_direction

for row in range(NUM_ROWS):
    for column in range(NUM_COLS):
        if grid[row][column] in {"[", "O"}:
            part_1 += 100 * row + column

print(f"Part 1: {part_1}")
# print(f"Part 2: {part_2}")
