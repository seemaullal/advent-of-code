from pathlib import Path


def solve():
    ranges, available_ingredient_ids = (
        item.split()
        for item in Path("inputs/input.txt").read_text().strip().split("\n\n")
    )

    fresh_ranges = [tuple(map(int, range_str.split('-'))) for range_str in ranges]

    part_1 = 0
    for ingredient_id in available_ingredient_ids:
        ingredient_id = int(ingredient_id)
        if any(start <= ingredient_id <= end for start, end in fresh_ranges):
            part_1 += 1
    print(f"Part 2: {part_1}")

    part_2 = 0
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    solve()
