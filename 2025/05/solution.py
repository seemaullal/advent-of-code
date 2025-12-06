from pathlib import Path


def solve():
    ranges, available_ingredient_ids = (
        item.split()
        for item in Path("inputs/input.txt").read_text().strip().split("\n\n")
    )

    fresh_ranges = [tuple(map(int, range_str.split("-"))) for range_str in ranges]

    part_1 = sum(
        any(start <= int(ingredient_id) <= end for start, end in fresh_ranges)
        for ingredient_id in available_ingredient_ids
    )
    print(f"Part 1: {part_1}")

    merged_ranges = []
    # 1, 6  2, 8 --> 1, 8
    # 1, 11 2, 8 --> 1, 11
    # 1, 6  9, 11 --> 1,6 and 9,11
    for start, end in sorted(fresh_ranges):
        if not merged_ranges or start > merged_ranges[-1][1]:
            merged_ranges.append((start, end))
        else:
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], end))

    part_2 = sum(end - start + 1 for start, end in merged_ranges)

    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    solve()
