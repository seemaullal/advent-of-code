part_1 = 0
part_2 = 0

with open("inputs/10.txt") as file:
    heights = [[int(num) for num in list(line.strip())] for line in file]

ROW_NUM = len(heights)
COL_NUM = len(heights[0])

def calculate_ways_part_1(row_number, col_number):
    peaks_seen_for_current_height = set()
    to_visit = [(row_number, col_number, 0)]
    number_ways = 0
    while to_visit:
        current_row, current_col, next_to_visit = to_visit.pop()
        if (
            0 <= current_row < ROW_NUM
            and 0 <= current_col < COL_NUM
            and heights[current_row][current_col] == next_to_visit
        ):
            if (
                next_to_visit == 9
                and (current_row, current_col) not in peaks_seen_for_current_height
            ):
                peaks_seen_for_current_height.add((current_row, current_col))
                number_ways += 1
            else:
                to_visit.append((current_row + 1, current_col, next_to_visit + 1))
                to_visit.append((current_row - 1, current_col, next_to_visit + 1))
                to_visit.append((current_row, current_col + 1, next_to_visit + 1))
                to_visit.append((current_row, current_col - 1, next_to_visit + 1))
    return number_ways


def calculate_ways_part_2(row_num, column_num, previously_calculated):
    if heights[row_num][column_num] == 9:
        return 1
    if (row_num, column_num) in previously_calculated:
        return previously_calculated[(row_num, column_num)]
    number_ways = 0
    for row_direction, column_direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        current_row = row_num + row_direction
        current_col = column_num + column_direction
        if (
            0 <= current_row < ROW_NUM
            and 0 <= current_col < COL_NUM
            and heights[current_row][current_col] == heights[row_num][column_num] + 1
        ):
            number_ways += calculate_ways_part_2(
                current_row, current_col, previously_calculated
            )
    previously_calculated[(row_num, column_num)] = number_ways
    return number_ways


for row_num in range(ROW_NUM):
    for col_num in range(COL_NUM):
        if heights[row_num][col_num] == 0:
            part_1 += calculate_ways_part_1(row_num, col_num)
            part_2 += calculate_ways_part_2(row_num, col_num, {})


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
