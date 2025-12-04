from pathlib import Path
from collections import defaultdict
import re


def solve():
    claims = Path("inputs/input.txt").read_text().strip().splitlines()
    part_1 = 0
    coordinate_counts = defaultdict(int)
    for claim in claims:
        _, left, top, width, height = map(int, re.findall(r"\d+", claim))
        for x in range(left, left + width):
            for y in range(top, top + height):
                coordinate_counts[(x, y)] += 1
                if coordinate_counts[(x, y)] == 2:
                    part_1 += 1

    print(f"Part 1: {part_1}")
    # print(f"Part 2: {part_2}")


if __name__ == "__main__":
    solve()
