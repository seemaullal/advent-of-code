import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/20.txt"
with open(input_file) as file:
    algorithm, image = file.read().split("\n\n")
    image_pixels = [list(line.strip()) for line in image.strip().split("\n")]


def part_1():
    pass


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
