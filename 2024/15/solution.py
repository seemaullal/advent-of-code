part_1 = 0
part_2 = 0

starting_row, starting_colummn = None, None
with open("inputs/input.txt", "r") as file:
    part_1_grid, instructions = file.read().split("\n\n")
    part_1_grid = [list(row) for row in part_1_grid.split("\n")]

DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

mapping = {"#": ["#", "#"], "O": ["[", "]"], ".": [".", "."], "@": ["@", "."]}

part_2_grid = [[char for cell in row for char in mapping[cell]] for row in part_1_grid]


def solve(grid):
    grid_height = len(grid)
    grid_width = len(grid[0])
    for row in range(grid_height):
        for column in range(grid_width):
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
            cannot_move = False
            while to_visit:
                row, column = to_visit.pop()
                if (row, column) in seen:
                    continue
                seen.add((row, column))
                new_row, new_column = row + row_direction, column + col_direction
                if grid[new_row][new_column] == "#":
                    cannot_move = True
                if grid[new_row][new_column] == "O":
                    to_visit.append((new_row, new_column))
                if grid[new_row][new_column] == "[":
                    to_visit.extend([(new_row, new_column), (new_row, new_column + 1)])
                if grid[new_row][new_column] == "]":
                    to_visit.extend([(new_row, new_column), (new_row, new_column - 1)])
            if cannot_move:
                continue
            while len(seen) > 0:
                for row, column in seen.copy():
                    new_row, new_column = row + row_direction, column + col_direction
                    if (new_row, new_column) not in seen:
                        grid[new_row][new_column] = grid[row][column]
                        grid[row][column] = "."
                        seen.remove((row, column))
            current_row = current_row + row_direction
            current_column = current_column + col_direction
    result = 0
    for row in range(grid_height):
        for column in range(grid_width):
            if grid[row][column] in {"[", "O"}:
                result += 100 * row + column
    return result


print(f"Part 1: {solve(part_1_grid)}")
print(f"Part 2: {solve(part_2_grid)}")
