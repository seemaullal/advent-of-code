from pathlib import Path


def solve():
    part_1 = 0
    ranges = [
        (int(start), int(end))
        for start, end in (
            r.split("-")
            for r in Path("inputs/input.txt").read_text().strip().split(",")
        )
    ]
    for start, end in ranges:
        for possible_id in range(start, end + 1):
            possible_id_string = str(possible_id)
            if (
                len(possible_id_string) % 2 == 0
                and possible_id_string[: len(possible_id_string) // 2]
                == possible_id_string[len(possible_id_string) // 2 :]
            ):
                part_1 += possible_id
    print(f"Part 1: {part_1}")


if __name__ == "__main__":
    solve()
