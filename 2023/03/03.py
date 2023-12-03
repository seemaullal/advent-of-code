schematic = []
with open("../inputs/3.txt") as file:
    for line in file:
        schematic.append(list(line.strip()))

NUM_ROWS = len(schematic)
NUM_COLS = len(schematic[0])

part_1 = 0
part_2 = 0
pos_to_part_num = {}
for row_index in range(NUM_ROWS):
    pos = 0
    while pos < NUM_COLS:
        current = ""
        valid = False
        if not schematic[row_index][pos].isdigit():
            pos += 1
        else:
            starting = pos
            while (
                pos < len(schematic[row_index]) and schematic[row_index][pos].isdigit()
            ):
                current += schematic[row_index][pos]
                delta = [-1, 0, 1]
                for row_delta in delta:
                    for col_delta in delta:
                        current_row = row_index + row_delta
                        current_col = pos + col_delta
                        if (
                            0 <= current_row < NUM_ROWS
                            and 0 <= current_col < NUM_COLS
                            and not schematic[current_row][current_col].isdigit()
                            and schematic[current_row][current_col] != "."
                        ):
                            valid = True
                pos += 1
            if valid:
                part_1 += int(current)
                for col in range(starting, pos + 1):
                    pos_to_part_num[(row_index, col)] = int(current)


# part_2 = 0
# for row_index in range(len(schematic)):
#     for col_index in range(len(schematic[row_index])):
#         if schematic[row_index][col_index] == "*":
#             num_gears = 0
#             gears = []
#             if (
#                 col_index != len(schematic[0]) - 1
#                 and schematic[row_index][col_index + 1].isdigit()
#             ):
#                 num_gears += 1
#                 gears.append((row_index, col_index + 1))
#             if col_index != 0 and schematic[row_index][col_index - 1].isdigit():
#                 num_gears += 1
#                 gears.append((row_index, col_index - 1))
#             left_top = False
#             right_top = False
#             left_bottom = False
#             right_bottom = False
#             top = False
#             bottom = False
#             if (
#                 row_index != len(schematic) - 1 and col_index != len(schematic[0]) - 1
#             ) and schematic[row_index + 1][col_index + 1].isdigit():
#                 num_gears += 1
#                 right_bottom = True
#                 # gears.append((row_index + 1, col_index + 1))
#             if (row_index != 0 and col_index != 0) and schematic[row_index - 1][
#                 col_index - 1
#             ].isdigit():
#                 num_gears += 1
#                 left_top = True
#                 # gears.append((row_index - 1, col_index - 1))
#             if (row_index != 0 and col_index != len(schematic[0]) - 1) and schematic[
#                 row_index - 1
#             ][col_index + 1].isdigit():
#                 num_gears += 1
#                 right_top = True
#                 # gears.append((row_index - 1, col_index + 1))
#             if (row_index != len(schematic) - 1 and col_index != 0) and schematic[
#                 row_index + 1
#             ][col_index - 1].isdigit():
#                 num_gears += 1
#                 left_bottom = True
#                 # gears.append((row_index + 1, col_index - 1))
#             if row_index != 0 and schematic[row_index - 1][col_index].isdigit():
#                 num_gears += 1
#                 top = True
#                 # if not left_top and not right_top:
#                 #     gears.append((row_index - 1, col_index))
#             if (
#                 row_index != len(schematic) - 1
#                 and schematic[row_index + 1][col_index].isdigit()
#             ):
#                 num_gears += 1
#                 bottom = True
#                 # if not left_bottom and not right_bottom:
#                 #     gears.append((row_index + 1, col_index))
#             if top:
#                 gears.append((row_index - 1, col_index))
#             else:
#                 if left_top:
#                     gears.append((row_index - 1, col_index - 1))
#                 if right_top:
#                     gears.append((row_index - 1, col_index + 1))
#             if bottom:
#                 gears.append((row_index + 1, col_index))
#             else:
#                 if left_bottom:
#                     gears.append((row_index + 1, col_index - 1))
#                 if right_bottom:
#                     gears.append((row_index + 1, col_index + 1))
#             if left_top and top:
#                 num_gears -= 1
#             if right_top and top:
#                 num_gears -= 1
#             if left_bottom and bottom:
#                 num_gears -= 1
#             if right_bottom and bottom:
#                 num_gears -= 1
#             if num_gears == 2:
#                 print(len(gears))
#                 part_2 += pos_to_part_num[gears[0]] * pos_to_part_num[gears[1]]

print(f"Part 1: {part_1}")
# print(f"Part 2: {part_2}")
