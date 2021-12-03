with open("inputs/day3.txt") as file:
    binary_nums = [num.strip() for num in file.readlines()]


def binary_to_decimal(binary_num):
    result = 0
    for i in range(len(binary_num)):
        if binary_num[len(binary_num) - i - 1] == "1":
            result += 2 ** i
    return result


def part_1():
    gamma = ""
    epsilon = ""
    for i in range(len(binary_nums[0])):
        number_zeroes = 0
        number_ones = 0
        for binary_num in binary_nums:
            if binary_num[i] == '0':
                number_zeroes += 1
            else:
                number_ones += 1
        if number_zeroes > number_ones:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    return binary_to_decimal(gamma) * binary_to_decimal(epsilon)


def part_2():
    oxygen_nums = binary_nums[:]
    co2_nums = binary_nums[:]
    current_index = 0
    while len(oxygen_nums) != 1 or len(co2_nums) != 1:
        if len(oxygen_nums) != 1:
            number_ones = 0
            number_zeroes = 0
            for num in oxygen_nums:
                if num[current_index] == "0":
                    number_zeroes += 1
                elif num[current_index] == "1":
                    number_ones += 1
            if number_ones > number_zeroes or number_ones == number_zeroes:
                target = "1"
            else:
                target = "0"
            oxygen_nums = [binary_num for binary_num in oxygen_nums if binary_num[current_index] == target]
        if len(co2_nums) != 1:
            number_ones = 0
            number_zeroes = 0
            for num in co2_nums:
                if num[current_index] == "0":
                    number_zeroes += 1
                elif num[current_index] == "1":
                    number_ones += 1
            if number_zeroes <= number_ones:
                target = "0"
            else:
                target = "1"
            co2_nums = [binary_num for binary_num in co2_nums if binary_num[current_index] == target]
        current_index += 1
    return binary_to_decimal(oxygen_nums[0]) * binary_to_decimal(co2_nums[0])


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
