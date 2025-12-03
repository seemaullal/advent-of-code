from pathlib import Path


def max_joltage_part_1(digits):
    max_tens = max(digits[:-1])
    max_tens_index = digits.index(max_tens)
    ones_place = max(digits[max_tens_index + 1 :])
    return max_tens * 10 + ones_place


def max_joltage_part_2(digits, sequence_length):
    to_skip = len(digits) - sequence_length
    result = []
    skipped_count = 0
    for digit in digits:
        while result and skipped_count < to_skip and result[-1] < digit:
            result.pop()
            skipped_count += 1
        if len(result) < sequence_length:
            result.append(digit)
        else:
            skipped_count += 1
    return int("".join(map(str, result)))


def parse_input(filename):
    return [
        [int(digit) for digit in line]
        for line in Path(filename).read_text().strip().splitlines()
    ]


def solve():
    banks = parse_input("inputs/input.txt")

    part_1 = sum(max_joltage_part_1(bank) for bank in banks)
    print(f"Part 1: {part_1}")

    part_2 = sum(max_joltage_part_2(bank, 12) for bank in banks)
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    solve()
