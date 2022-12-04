import sys
from copy import deepcopy

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/11.txt"

with open(input_file) as file:
    seats = []
    for line in file.readlines():
        seats.append([])
        for seat in line.strip():
            seats[-1].append(seat)


def number_adjacent_occupied(row_num, col_num, layout):
    num_adjacent = 0
    if row_num != 0:
        if layout[row_num - 1][col_num] == "#":
            num_adjacent += 1
        if col_num != 0:
            if layout[row_num - 1][col_num - 1] == "#":
                num_adjacent += 1
        if col_num != len(layout[0]) - 1:
            if layout[row_num - 1][col_num + 1] == "#":
                num_adjacent += 1
    if col_num != 0:
        if layout[row_num][col_num - 1] == "#":
            num_adjacent += 1
    if row_num != len(layout) - 1:
        if layout[row_num + 1][col_num] == "#":
            num_adjacent += 1
        if col_num != 0:
            if layout[row_num + 1][col_num - 1] == "#":
                num_adjacent += 1
        if col_num != len(layout[0]) - 1:
            if layout[row_num + 1][col_num + 1] == "#":
                num_adjacent += 1
    if col_num != len(layout[0]) - 1:
        if layout[row_num][col_num + 1] == "#":
            num_adjacent += 1
    return num_adjacent


def number_adjacent_occupied_part_2(row_num, col_num, layout):
    num_adjacent = 0
    # left right down up right-up-diag left-up-diag left-down-diag right-down-diag
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
    for x_direction, y_direction in directions:
        current_row = row_num + x_direction
        current_col = col_num + y_direction
        keep_going = True
        while (
            keep_going
            and current_row >= 0
            and current_col >= 0
            and current_row < len(layout)
            and current_col < len(layout[0])
        ):
            if layout[current_row][current_col] == "#":
                num_adjacent += 1
                keep_going = False
            elif layout[current_row][current_col] == 'L':
                keep_going = False
            current_row += x_direction
            current_col += y_direction
    return num_adjacent


def part_1():
    seats_changed = True
    current_seats = deepcopy(seats)
    while seats_changed:
        seats_changed = False
        updated_seats = deepcopy(current_seats)
        for row_num in range(len(current_seats)):
            for col_num in range(len(current_seats[row_num])):
                adjacent_occupied = number_adjacent_occupied(
                    row_num, col_num, current_seats
                )
                if current_seats[row_num][col_num] == "L" and adjacent_occupied == 0:
                    updated_seats[row_num][col_num] = "#"
                    seats_changed = True
                if current_seats[row_num][col_num] == "#" and adjacent_occupied >= 4:
                    updated_seats[row_num][col_num] = "L"
                    seats_changed = True
        current_seats = updated_seats
    occupied = 0
    for row_num in range(len(current_seats)):
        for col_num in range(len(current_seats[row_num])):
            if current_seats[row_num][col_num] == "#":
                occupied += 1
    return occupied


def part_2():
    seats_changed = True
    current_seats = deepcopy(seats)
    while seats_changed:
        seats_changed = False
        updated_seats = deepcopy(current_seats)
        for row_num in range(len(current_seats)):
            for col_num in range(len(current_seats[row_num])):
                adjacent_occupied = number_adjacent_occupied_part_2(
                    row_num, col_num, current_seats
                )
                if current_seats[row_num][col_num] == "L" and adjacent_occupied == 0:
                    updated_seats[row_num][col_num] = "#"
                    seats_changed = True
                if current_seats[row_num][col_num] == "#" and adjacent_occupied >= 5:
                    updated_seats[row_num][col_num] = "L"
                    seats_changed = True
        current_seats = updated_seats
    occupied = 0
    for row_num in range(len(current_seats)):
        for col_num in range(len(current_seats[row_num])):
            if current_seats[row_num][col_num] == "#":
                occupied += 1
    return occupied


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
