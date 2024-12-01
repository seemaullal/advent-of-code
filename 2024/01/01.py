from collections import Counter

left_nums = []
right_nums = []
right_counts = Counter()
part_1 = 0
part_2 = 0

with open("inputs/01.txt", "r") as file:
    for line in file.read().splitlines():
        left, right = line.split()
        left, right = int(left), int(right)
        left_nums.append(left)
        right_nums.append(right)
        right_counts[right] += 1

for left, right in zip(sorted(left_nums), sorted(right_nums)):
    part_1 += abs(left - right)
    part_2 += left * right_counts[left]

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
