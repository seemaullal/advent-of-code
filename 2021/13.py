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


def get_points():
    return {(x, y) for x, y in coordinates}

def fold_grid(direction, location, current_points):
    new_points = set()
    if direction == "x":
        for x, y in current_points:
            if x > location:
                new_points.add((2 * location - x, y))
            elif x < location:
                new_points.add((x, y))
    else:
        assert direction == "y"
        for x, y in current_points:
            if y > location:
                new_points.add((x, 2 * location - y))
            elif y < location:
                new_points.add((x, y))
    return new_points

def part_1():
    points = get_points()
    for direction, location in folds[:1]:
        points = fold_grid(direction, location, points)
    return len(points)


def part_2():
    points = get_points()
    for direction, location in folds:
        points = fold_grid(direction, location, points)
    for row in range(max([y for (x,y) in points]) + 1):
        line = ""
        for col in range(max([x for (x,y) in points]) + 1):
            line += "#" if (col, row) in points else " "
        print(line)

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
