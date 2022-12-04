with open("inputs/4.txt") as file:
    start_range, end_range = [int(num) for num in file.read().strip().split("-")]


def part_1():
    valid = 0
    for num in range(start_range, end_range + 1):
        digits = list(str(num))
        if sorted(digits) == digits:
            consecutive_digits = False
            for i in range(len(digits) - 1):
                if digits[i] == digits[i + 1]:
                    consecutive_digits = True
            if consecutive_digits:
                valid += 1
    return valid


def part_2():
    valid = 0
    for num in range(start_range, end_range + 1):
        digits = list(str(num))
        if sorted(digits) == digits:
            consecutive_digits = False
            for i in range(len(digits) - 1):
                if (
                    digits[i] == digits[i + 1]
                    and (i == 0 or digits[i - 1] != digits[i])
                    and (i == len(digits) - 2 or digits[i + 1] != digits[i + 2])
                ):
                    consecutive_digits = True
            if consecutive_digits:
                valid += 1
    return valid


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
