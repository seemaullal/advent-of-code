with open("inputs/input.txt", "r") as file:
    shapes = file.read().strip().split("\n\n")


def fits_into(key, lock):
    row_number = len(key)
    column_number = len(key[0])
    for row in range(row_number):
        for column in range(column_number):
            if key[row][column] == "#" and lock[row][column] == "#":
                return False
    return True


keys = []
locks = []
for shape in shapes:
    rows = shape.split("\n")
    row_number = len(rows)
    column_number = len(rows[0])
    grid = [
        [rows[row][column] for column in range(column_number)]
        for row in range(row_number)
    ]
    is_key = True
    for column in range(column_number):
        if grid[0][column] == "#":
            is_key = False
            break
    if is_key:
        keys.append(shape)
    else:
        locks.append(shape)


part_1 = sum(1 for key in keys for lock in locks if fits_into(key, lock))
print(f"Part 1: {part_1}")
