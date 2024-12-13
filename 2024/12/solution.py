with open("inputs/input.txt") as f:
    garden = [[plant for plant in list(line.strip())] for line in f]

ROW_COUNT = len(garden)
COL_COUNT = len(garden)
POSSIBLE_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

part_1 = 0
part_2 = 0


seen = set()
for row_number in range(ROW_COUNT):
    for col_number in range(COL_COUNT):
        if (row_number, col_number) in seen:
            continue
        to_visit = [(row_number, col_number)]
        area = 0
        perimeter = 0
        grouped_coordinates = [set(), set(), set(), set()]
        dd = []
        while to_visit:
            current_row, current_col = to_visit.pop()
            if (current_row, current_col) in seen:
                continue
            seen.add((current_row, current_col))
            area += 1
            for index, (row_direction, column_direction) in enumerate(
                POSSIBLE_DIRECTIONS
            ):
                new_row = current_row + row_direction
                new_col = current_col + column_direction
                if (
                    0 <= new_row < ROW_COUNT
                    and 0 <= new_col < COL_COUNT
                    and garden[new_row][new_col] == garden[current_row][current_col]
                ):
                    to_visit.append((new_row, new_col))
                else:
                    perimeter += 1
                    grouped_coordinates[index].add((current_row, current_col))
        sides = 0
        for group in grouped_coordinates:
            seen_perimeter = set()
            for row, col in group:
                if (row, col) not in seen_perimeter:
                    sides += 1
                    to_visit_sides = [(row, col)]
                    while to_visit_sides:
                        current_row, current_col = to_visit_sides.pop()
                        if (current_row, current_col) in seen_perimeter:
                            continue
                        seen_perimeter.add((current_row, current_col))
                        for row_direction, column_direction in POSSIBLE_DIRECTIONS:
                            new_row = current_row + row_direction
                            new_col = current_col + column_direction
                            if (new_row, new_col) in group:
                                to_visit_sides.append((new_row, new_col))

        part_1 += area * perimeter
        part_2 += area * sides


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
