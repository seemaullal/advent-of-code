import sys
from collections import Counter

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/14.txt"
with open(input_file) as file:
    sequence = file.readline().strip()
    file.readline()
    rules = dict([line.strip().split(" -> ") for line in file.readlines()])


def part_1():
    current_sequence = sequence
    for _ in range(10):
        new_sequence = ""
        for first, second in zip(current_sequence, current_sequence[1:]):
            current = first + second
            if current in rules:
                new_sequence += f"{first}{rules[current]}"
            else:
                new_sequence += first
        current_sequence = new_sequence + second
    sorted_counts = Counter(current_sequence).most_common()
    return sorted_counts[0][1] - sorted_counts[-1][1]


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
