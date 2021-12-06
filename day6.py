import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/day6.txt"
with open(input_file) as file:
    nums = [int(num) for num in file.read().split(",")]

def part_1():
    counts = [0 for i in range(9)]
    for num in nums:
        counts[num] += 1
    for _ in range(80):
        updated = [0 for _ in range(9)]
        for i in range(1, 9):
            updated[i - 1] += counts[i]
        updated[8] += counts[0]
        updated[6] += counts[0]
        counts = updated
    return sum(counts)


def part_2():
    counts = [0 for _ in range(9)]
    for num in nums:
        counts[num] += 1
    for _ in range(256):
        updated = [0 for i in range(9)]
        for i in range(1, 9):
            updated[i - 1] += counts[i]
        updated[8] += counts[0]
        updated[6] += counts[0]
        counts = updated
    return sum(counts)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
