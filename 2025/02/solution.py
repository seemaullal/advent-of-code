from pathlib import Path


def is_invalid_part_1(num):
    num_as_string = str(num)
    return (
        len(num_as_string) % 2 == 0
        and num_as_string[: len(num_as_string) // 2]
        == num_as_string[len(num_as_string) // 2 :]
    )


def is_invalid_part_2(num):
    num_as_string = str(num)
    return (num_as_string + num_as_string).find(num_as_string, 1) != len(num_as_string)


def solve():
    part_1 = 0
    part_2 = 0
    ranges = [
        (int(start), int(end))
        for start, end in (
            r.split("-")
            for r in Path("inputs/input.txt").read_text().strip().split(",")
        )
    ]
    for start, end in ranges:
        for possible_id in range(start, end + 1):
            if is_invalid_part_1(possible_id):
                part_1 += possible_id
            if is_invalid_part_2(possible_id):
                part_2 += possible_id
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    solve()
