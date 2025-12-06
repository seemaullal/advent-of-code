from pathlib import Path
from math import prod


def apply_operation(numbers, op):
    return sum(numbers) if op == "+" else prod(numbers)


def get_numbers_p1(rows, cols):
    nums = []
    for row in rows:
        current = 0
        for i in cols:
            if i < len(row) and row[i].isdigit():
                current = current * 10 + int(row[i])
        nums.append(current)
    return nums


def get_numbers_p2(rows, cols):
    nums = []
    for i in cols:
        current = 0
        for row in rows:
            if i < len(row) and row[i].isdigit():
                current = current * 10 + int(row[i])
        nums.append(current)
    return nums


def solve():
    lines = Path("inputs/input.txt").read_text().strip().splitlines()
    rows = lines[:-1]
    operations = lines[-1].split()
    max_len = max(len(row) for row in rows)

    part1 = part2 = 0
    current_columns = []
    operation_index = 0

    for col in range(max_len + 1):
        should_process = col == max_len or all(
            col >= len(row) or row[col] == " " for row in rows
        )
        if should_process:
            part1 += apply_operation(
                get_numbers_p1(rows, current_columns), operations[operation_index]
            )
            part2 += apply_operation(
                get_numbers_p2(rows, current_columns), operations[operation_index]
            )
            current_columns = []
            operation_index += 1
        else:
            current_columns.append(col)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    solve()
