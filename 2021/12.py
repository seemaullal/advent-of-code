import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/12.txt"
nums = []
with open(input_file) as file:
    for line in file:
        nums.append([int(num) for num in list(line.strip())])


def part_1():
    pass


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
