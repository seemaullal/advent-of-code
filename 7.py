import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/7.txt"
with open(input_file) as file:
    nums = [int(num) for num in file.readline().strip().split(",")]


def part_1():
    sorted_positions = sorted(nums)
    midpoint = sorted_positions[len(sorted_positions) // 2]
    return sum([abs(num - midpoint) for num in nums])


def part_2():
    minimum_cost = None
    for position1 in range(max(nums) + 1):
        current_cost = 0
        for position2 in nums:
            distance = abs(position1 - position2)
            # sum of numbers from 1 to N is N * (N+1) / 2
            # the one math formula I remember and is sometimes useful!
            current_cost += (distance) * (distance + 1) // 2
        if minimum_cost is None or current_cost < minimum_cost:
            minimum_cost = current_cost
    return minimum_cost


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
