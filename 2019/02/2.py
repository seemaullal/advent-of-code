import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/2.txt"
with open(input_file) as file:
    nums = [int(num) for num in file.read().strip().split(",")]


def part_1():
    current_position = 0
    current_nums = nums[:]
    current_nums[1] = 12
    current_nums[2] = 2
    while current_nums[current_position] != 99:
        first_number_position = current_nums[current_position + 1]
        second_number_position = current_nums[current_position + 2]
        destination_position = current_nums[current_position + 3]
        if current_nums[current_position] == 1:
            current_nums[destination_position] = (
                current_nums[first_number_position]
                + current_nums[second_number_position]
            )
        elif current_nums[current_position] == 2:
            current_nums[destination_position] = (
                current_nums[first_number_position]
                * current_nums[second_number_position]
            )
        current_position += 4
    return current_nums[0]


def part_2():
    for i in range(100):
        for j in range(100):
            current_position = 0
            current_nums = nums[:]
            current_nums[1] = i
            current_nums[2] = j
            while current_nums[current_position] != 99:
                first_number_position = current_nums[current_position + 1]
                second_number_position = current_nums[current_position + 2]
                destination_position = current_nums[current_position + 3]
                if current_nums[current_position] == 1:
                    current_nums[destination_position] = (
                        current_nums[first_number_position]
                        + current_nums[second_number_position]
                    )
                elif current_nums[current_position] == 2:
                    current_nums[destination_position] = (
                        current_nums[first_number_position]
                        * current_nums[second_number_position]
                    )
                current_position += 4
            if current_nums[0] == 19690720:
                return 100 * i + j


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
