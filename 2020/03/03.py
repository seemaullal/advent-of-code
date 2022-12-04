with open("inputs/3.txt") as file:
    lines = file.readlines()
    grid = []
    slopes_list = [
        [
            1,
            1,
        ],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]
    for line in lines:
        line = list(line.strip())
        grid.append(line)

part_1 = float('-inf')
part_2 = 1
for colInc, rowInc in slopes_list:
    current_trees = 0
    row = 0
    col = 0
    while row < len(grid):
        if grid[row][col % len(grid[0])] == "#":
            current_trees += 1
        row += rowInc
        col += colInc
    part_1 = max(current_trees, part_1)
    part_2 *= current_trees

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
