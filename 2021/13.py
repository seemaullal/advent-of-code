import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/13.txt"
with open(input_file) as file:
    coordinate_string, fold_string = file.read().split("\n\n")
    coordinates = []
    folds = []
    for line in coordinate_string.split("\n"):
        x, y = line.strip().split(",")
        coordinates.append((int(x), int(y)))
    for line in fold_string.strip().split("\n"):
        directions, location = line.split("=")
        folds.append((directions[-1], int(location)))


def get_grid():
    max_x = max([coordinate[0] for coordinate in coordinates])
    max_y = max([coordinate[1] for coordinate in coordinates])
    grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in coordinates:
        grid[y][x] = "#"
    return grid


def fold_grid(direction, location, current_grid):
    if direction == "x":
        new_grid = []
        for row in current_grid:
            new_row = row[:location]
            for col_num in range(location):
                if row[len(row) - col_num - 1] == "#":
                    new_row[col_num] = "#"
            new_grid.append(new_row)
    else:
        for row_num in range(location, len(current_grid)):
            for col_num in range(len(current_grid[0])):
                if current_grid[row_num][col_num] == "#":
                    current_grid[location - (row_num - location)][col_num] = "#"
        new_grid = current_grid[:location]
    return new_grid


def part_1():
    grid = get_grid()
    for direction, location in folds[:1]:
        grid = fold_grid(direction, location, grid)
    ans = 0
    for row in grid:
        for col in row:
            if col == "#":
                ans += 1
    return ans


def part_2():
    grid = get_grid()
    for direction, location in folds:
        grid = fold_grid(direction, location, grid)
    for row in grid:
        print("".join(map(lambda cell: cell if cell == "#" else " ", row)))


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
