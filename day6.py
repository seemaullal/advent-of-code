import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/day6.txt"
with open(input_file) as file:
    nums = [int(num) for num in file.readlines()]

def part_1():
    pass


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
