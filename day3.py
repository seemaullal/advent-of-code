from typing import List

with open("inputs/day3.txt") as file:
    binary_nums = [num.strip() for num in file.readlines()]

def calculate_target_num(binary_nums: List[str], index_to_check: int, use_higher_num: bool):
    number_zeroes = len([num for num in binary_nums if num[index_to_check] == "0"])
    number_ones = len(binary_nums) - number_zeroes
    if number_zeroes <= number_ones:
        return "1" if use_higher_num else "0"
    else:
        return "0" if use_higher_num else "1"


def part_1():
    gamma, epsilon = "", ""
    for i in range(len(binary_nums[0])):
        gamma += calculate_target_num(binary_nums, i, True)
        epsilon += "1" if gamma[-1] == "0" else "0"
    return int(gamma, 2) * int(epsilon, 2)


def part_2():
    oxygen_nums, co2_nums = binary_nums[:], binary_nums[:]
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
    return int(oxygen_nums[0], 2) * int(co2_nums[0], 2)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
