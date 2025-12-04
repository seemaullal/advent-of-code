from pathlib import Path
from collections import Counter


def solve():
    box_ids = Path("inputs/input.txt").read_text().strip().splitlines()

    twice_count = sum(1 for box_id in box_ids if 2 in Counter(box_id).values())
    thrice_count = sum(1 for box_id in box_ids if 3 in Counter(box_id).values())
    part_1 = twice_count * thrice_count

    for position in range(len(box_ids[0])):
        seen = set()
        for box_id in box_ids:
            id_without_char = box_id[:position] + box_id[position + 1 :]
            if id_without_char in seen:
                part_2 = id_without_char
                break
            seen.add(id_without_char)

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    solve()
