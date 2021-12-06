from collections import Counter
import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/day6.txt"
with open(input_file) as file:
    nums = [int(num) for num in file.read().split(",")]

def calculate_lanternfish(days):
    counts = Counter(nums)
    for _ in range(days):
        original_zero = counts[0]
        for i in range(1, 9):
            counts[i - 1] = counts[i]
        counts[8] = original_zero
        counts[6] += original_zero
    return sum(counts.values())

def part_1():
    return calculate_lanternfish(80)

def part_2():
    return calculate_lanternfish(256)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
