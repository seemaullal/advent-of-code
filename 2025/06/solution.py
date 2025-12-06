from pathlib import Path
from math import prod

def apply_operation(numbers, operation):
    return sum(numbers) if operation == '+' else prod(numbers)


def solve():
    lines = Path("inputs/input.txt").read_text().strip().splitlines()
    rows = [[int(num) for num in line.split()] for line in lines[:-1]]
    operations = lines[-1].split()

    part_1 = 0
    for i in range(len(rows[0])):
        part_1 += apply_operation([row[i] for row in rows], operations[i])
    print(f"Part 1: {part_1}")

    part_2 = 0
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    solve()
