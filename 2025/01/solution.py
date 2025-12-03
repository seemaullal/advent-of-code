from pathlib import Path


def part_1(instructions):
    position = 50
    result = 0
    for rotation, distance in instructions:
        if rotation == "L":
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
        if position == 0:
            result += 1
    return result


def part_2(instructions):
    position = 50
    result = 0
    for rotation, distance in instructions:
        if rotation == "L":
            if position == 0:
                result += distance // 100
            else:
                result += (distance + 100 - position) // 100
            position = (position - distance) % 100
        else:
            result += (position + distance) // 100
            position = (position + distance) % 100
    return result


def parse_instructions(filename):
    return [
        (instruction[0], int(instruction[1:]))
        for instruction in Path(filename).read_text().strip().splitlines()
    ]


def solve():
    instructions = parse_instructions("inputs/input.txt")
    print(f"Part 1: {part_1(instructions)}")
    print(f"Part 2: {part_2(instructions)}")


if __name__ == "__main__":
    solve()
