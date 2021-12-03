with open("inputs/day3.txt") as file:
    binary_nums = [num.strip() for num in file.readlines()]


def binary_to_decimal(binary_num):
    result = 0
    for i in range(len(binary_num)):
        if binary_num[len(binary_num) - i - 1] == "1":
            result += 2 ** i
    return result


def part_1():
    bits = [0] * 12
    for binary_num in binary_nums:
        for i in range(12):
            bits[i] += 1 if binary_num[i] == "1" else -1
    gamma = ""
    epsilon = ""
    for bit in bits:
        if bit > 0:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return binary_to_decimal(gamma) * binary_to_decimal(epsilon)


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
