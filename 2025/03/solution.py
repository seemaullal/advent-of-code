from pathlib import Path


def part_1(instructions):
    result = 0
    for banks in instructions:
        max_bank_excluding_last = max(banks[:-1])
        max_index = banks.index(max_bank_excluding_last)
        ones_place = max(banks[max_index + 1 :])
        max_joltage = max_bank_excluding_last * 10 + ones_place
        result += max_joltage
    return result


def part_2(instructions):
    pass


def parse_instructions(filename):
    return [
        [int(bank) for bank in banks]
        for banks in Path(filename).read_text().strip().splitlines()
    ]


def solve():
    instructions = parse_instructions("inputs/input.txt")
    print(f"Part 1: {part_1(instructions)}")
    print(f"Part 2: {part_2(instructions)}")


if __name__ == "__main__":
    solve()
