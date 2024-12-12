import sys
import time

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/20.txt"
with open(input_file) as file:
    algorithm, image = file.read().split("\n\n")
    image_pixels = [list(line.strip()) for line in image.strip().split("\n")]
    lit_points = set()
    for row_number in range(len(image_pixels[0])):
        for col_number in range(len(image_pixels)):
            if image_pixels[row_number][col_number] == "#":
                lit_points.add((row_number, col_number))


def step(previous_lit, min_row, max_row, min_col, max_col):
    new_lit = set()
    for row_num in range(min_row, max_row + 1):
        for col_num in range(min_col, max_col + 1):
            binary_string = ""
            for y in range(-1, 2):
                for x in range(-1, 2):
                    row = row_num + y
                    col = col_num + x
                    binary_string += "1" if (row, col) in previous_lit else "0"
            if algorithm[int(binary_string, 2)] == "#":
                new_lit.add((row_num, col_num))
    return new_lit


def part_1():
    currently_lit = set(lit_points)
    min_row = min({x for x, y in lit_points}) - 200
    max_row = max({x for x, y in lit_points}) + 200
    min_col = min({y for x, y in lit_points}) - 200
    max_col = max({y for x, y in lit_points}) + 200
    for _ in range(2):
        currently_lit = step(currently_lit, min_row, max_row, min_col, max_col)
        min_row += 3
        max_row -= 3
        min_col += 3
        max_col -= 3
    return len(currently_lit)


def part_2():
    currently_lit = set(lit_points)
    min_row = min({x for x, y in lit_points}) - 200
    max_row = max({x for x, y in lit_points}) + 200
    min_col = min({y for x, y in lit_points}) - 200
    max_col = max({y for x, y in lit_points}) + 200
    for _ in range(50):
        currently_lit = step(currently_lit, min_row, max_row, min_col, max_col)
        min_row += 3
        max_row -= 3
        min_col += 3
        max_col -= 3
    return len(currently_lit)


start = time.perf_counter()
print(f"Part 1: {part_1()}")
stop = time.perf_counter()
print(f"Finished Part 1 in {stop - start:0.4f} seconds")
start = time.perf_counter()
print(f"Part 2: {part_2()}")
stop = time.perf_counter()
print(f"Finished Part 2 in {stop - start:0.4f} seconds")
