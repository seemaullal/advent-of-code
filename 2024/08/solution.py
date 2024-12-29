from collections import defaultdict

with open("inputs/08.txt", "r") as file:
    grid = [list(line) for line in file.read().splitlines()]

ROW_COUNT = len(grid)
COLUMN_COUNT = len(grid[0])


def is_valid_position(row, col):
    return 0 <= row < ROW_COUNT and 0 <= col < COLUMN_COUNT


antennas = defaultdict(list)
for r in range(ROW_COUNT):
    for c in range(COLUMN_COUNT):
        if grid[r][c] != ".":
            antennas[grid[r][c]].append((r, c))

part_1 = set()
part_2 = set()
for row_number in range(ROW_COUNT):
    for column_number in range(COLUMN_COUNT):
        for antenna, vertices in antennas.items():
            for row_1, column_1 in vertices:
                for row_2, column_2 in vertices:
                    if is_valid_position(row_number, column_number) and (
                        row_1,
                        column_1,
                    ) != (
                        row_2,
                        column_2,
                    ):
                        distance_1 = abs(row_number - row_1) + abs(
                            column_number - column_1
                        )
                        distance_2 = abs(row_number - row_2) + abs(
                            column_number - column_2
                        )

                        row_distance_1 = row_number - row_1
                        row_distance_2 = row_number - row_2
                        column_distance_1 = column_number - column_1
                        column_distance_2 = column_number - column_2

                        if (
                            distance_1 == 2 * distance_2 or distance_1 * 2 == distance_2
                        ) and (
                            row_distance_1 * column_distance_2
                            == column_distance_1 * row_distance_2
                        ):
                            part_1.add((row_number, column_number))
                        if (
                            row_distance_1 * column_distance_2
                            == column_distance_1 * row_distance_2
                        ):
                            part_2.add((row_number, column_number))


print(f"Part 1: {len(part_1)}")
print(f"Part 2: {len(part_2)}")
