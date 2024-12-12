with open("inputs/3.txt") as file:
    grid = [list(line.strip()) for line in file]

SLOPES = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]
part_1 = None
part_2 = 1
for index, (colInc, rowInc) in enumerate(SLOPES):
    current_trees = 0
    row = 0
    col = 0
    while row < len(grid):
        if grid[row][col % len(grid[0])] == "#":
            current_trees += 1
        row += rowInc
        col += colInc
    if index == 1:
        part_1 = current_trees
    part_2 *= current_trees

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
