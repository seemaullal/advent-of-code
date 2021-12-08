import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/day8.txt"
patterns = []
with open(input_file) as file:
    for line in file.readlines():
        first, second = line.strip().split(" | ")
        patterns.append([first.split(), second.split()])

def part_1():
    total = 0
    for _signals, output in patterns:
        for combination in output:
            if len(combination) in (2,4,3,7):
                total += 1
    return total

def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
