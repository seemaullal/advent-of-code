import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/day7.txt"
with open(input_file) as file:
    nums = [int(num) for num in file.readline().strip().split(",")]


def part_1():
    sorted_positions = sorted(nums)
    midpoint = sorted_positions[len(sorted_positions) // 2]
    cost = 0
    for num in nums:
        cost += abs(num - midpoint)
    return cost


def part_2():
    minimum_cost = None
    for horizontal_position in range(max(nums) + 1):
        current_cost = 0
        for second_num in nums:
            distance = abs(second_num - horizontal_position)
            # sum of numbers from 1 to N is N * (N+1) / 2
            # the one math formula I remember and is sometimes useful!
            current_cost += (distance) * (distance + 1) // 2
        if minimum_cost is None or current_cost < minimum_cost:
            minimum_cost = current_cost
    return minimum_cost


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
