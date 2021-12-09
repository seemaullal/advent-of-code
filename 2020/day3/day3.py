file = open('advent-input.txt')
lines = file.readlines()
grid = []
slopes_list = [[1,1,], [3,1], [5,1], [7,1], [1,2]]
for line in lines: 
    line = list(line.strip())
    grid.append(line)
product = 1
for colInc, rowInc in slopes_list:
    trees = 0
    row = 0
    col = 0
    while row < len(grid):
        if grid[row][col % len(grid[0])] == '#':
            trees += 1
        row += rowInc
        col += colInc
    print('colInc', colInc)
    print('rowInc', rowInc)
    print('trees', trees)
    product *= trees
print(product)