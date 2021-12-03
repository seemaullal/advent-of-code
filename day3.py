from typing import List

with open("inputs/day3.txt") as file:
    binary_nums = [num.strip() for num in file.readlines()]


def binary_to_decimal(binary_num: str):
    return sum(
        [2 ** i for i in range(len(binary_num)) if binary_num[len(binary_num) - i - 1] == "1"]
    )


def calculate_target_num(binary_nums: List[str], index_to_check: int, use_higher_num: bool):
    number_ones = 0
    number_zeroes = 0
    for num in binary_nums:
        if num[index_to_check] == "0":
            number_zeroes += 1
        elif num[index_to_check] == "1":
            number_ones += 1
    if number_ones > number_zeroes:
        return "1" if use_higher_num else "0"
    elif number_ones < number_zeroes:
        return "0" if use_higher_num else "1"
    # this will only happen when there is an equal number of 0s and 1s at the index
    return "1" if use_higher_num else "0"


def part_1():
    gamma = ""
    epsilon = ""
    for i in range(len(binary_nums[0])):
        gamma += calculate_target_num(binary_nums, i, True)
        epsilon += "1" if gamma[-1] == "0" else "0"
    return binary_to_decimal(gamma) * binary_to_decimal(epsilon)


def part_2():
    oxygen_nums = binary_nums[:]
    co2_nums = binary_nums[:]
    current_index = 0
    while len(oxygen_nums) != 1 or len(co2_nums) != 1:
        if len(oxygen_nums) != 1:
            target = calculate_target_num(oxygen_nums, current_index, True)
            oxygen_nums = [
                binary_num for binary_num in oxygen_nums if binary_num[current_index] == target
            ]
        if len(co2_nums) != 1:
            target = calculate_target_num(co2_nums, current_index, False)
            co2_nums = [
                binary_num for binary_num in co2_nums if binary_num[current_index] == target
            ]
        current_index += 1
    return binary_to_decimal(oxygen_nums[0]) * binary_to_decimal(co2_nums[0])


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
