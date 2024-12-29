part_1 = set()
part_2 = 0

CURRENT_DIRECTION_TO_NEXT_DIRECTION = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N",
}

DIRECTION_TO_MOVE = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}

with open("inputs/input.txt", "r") as file:
    guard_map = [list(line) for line in file.read().splitlines()]


ROW_COUNT = len(guard_map)
COLUMN_COUNT = len(guard_map[0])

for row_num in range(ROW_COUNT):
    for column_num in range(COLUMN_COUNT):
        if guard_map[row_num][column_num] == "^":
            starting_row = row_num
            starting_column = column_num
            break

for current_row in range(ROW_COUNT):
    for current_column in range(COLUMN_COUNT):
        current_row,current_column = starting_row, starting_column
        current_direction = "N"
        seen_positions_and_directions = set()
        seen_positions= set()
        while True:
            if (current_row,current_column,current_direction) in seen_positions_and_directions:
                part_2 += 1
                break
            seen_positions_and_directions.add((current_row,current_column,current_direction))
            seen_positions.add((current_row,current_column))
            row_delta, column_delta = DIRECTION_TO_MOVE[current_direction]
            next_row, next_column = current_row + row_delta, current_column + column_delta
            if not (0<=next_row<ROW_COUNT and 0<=next_column<COLUMN_COUNT):
                if guard_map[current_row][current_column]=='#':
                    part_1 = len(seen_positions)
                break
            if guard_map[next_row][next_column] == "#" or next_row == current_row and next_column == current_column:
                current_direction = CURRENT_DIRECTION_TO_NEXT_DIRECTION[current_direction]
            else:
                current_row = next_row
                current_column = next_column


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
