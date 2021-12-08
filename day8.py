import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/day8.txt"
patterns = []
with open(input_file) as file:
    for line in file.readlines():
        first, second = line.strip().split(" | ")
        patterns.append([first.split(), second.split()])

def part_1():
    total = 0
    for signals, output in patterns:
        unique_lengths = set()
        seen = set()
        for signal in signals:
            if len(signal) not in seen:
                unique_lengths.add(len(signal))
                seen.add(len(signal))
            else:
                if len(signal) in unique_lengths:
                    unique_lengths.remove(len(signal))
        for combination in output:
            if len(combination) in unique_lengths:
                total += 1
    return total

def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
