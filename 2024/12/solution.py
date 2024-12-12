# from collections import deque

part_1 = 0
part_2 = 0

with open("inputs/input.txt") as f:
    garden = [[plant for plant in list(line.strip())] for line in f]

ROW_COUNT = len(garden)
COL_COUNT = len(garden)
POSSIBLE_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

seen = set()
for row_number in range(ROW_COUNT):
    for col_number in range(COL_COUNT):
        if (row_number,col_number) in seen:
            continue
        to_visit = [(row_number,col_number)]
        area = 0
        perimeter = 0
        while to_visit:
            current_row,current_col = to_visit.pop()
            if (current_row,current_col) in seen:
                continue
            seen.add((current_row,current_col))
            area += 1
            for row_direction,column_direction in POSSIBLE_DIRECTIONS:
                new_row = current_row+row_direction
                new_col = current_col+column_direction
                if 0<=new_row<ROW_COUNT and 0<=new_col<COL_COUNT and garden[new_row][new_col]==garden[current_row][current_col]:
                    to_visit.append((new_row,new_col))
                else:
                    perimeter += 1


        part_1 += area*perimeter


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
