import sys
from collections import defaultdict

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/13.txt"
graph = defaultdict(set)
with open(input_file) as file:
    for line in file:
        first, second = line.strip().split("-")
        graph[first].add(second)
        graph[second].add(first)


def part_1():
    pass


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
