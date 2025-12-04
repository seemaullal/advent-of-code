from pathlib import Path


def solve():
    seen_frequencies = {0}
    changes = [
        int(num) for num in Path("inputs/input.txt").read_text().strip().splitlines()
    ]
    current = 0
    part_1 = sum(changes)
    part_2 = None
    while part_2 is None:
        for change in changes:
            current += change
            if current in seen_frequencies:
                part_2 = current
            seen_frequencies.add(current)
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    solve()
