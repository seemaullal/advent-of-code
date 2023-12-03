schematic = []
with open("../inputs/3.txt") as file:
    for line in file:
        schematic.append(list(line.strip()))

part_1 = 0
for row_index in range(len(schematic)):
    pos = 0
    while pos < len(schematic[row_index]):
        current = ""
        valid = False
        if not schematic[row_index][pos].isdigit():
            pos += 1
        else:
            while (
                pos < len(schematic[row_index]) and schematic[row_index][pos].isdigit()
            ):
                current += schematic[row_index][pos]
                if (
                    row_index != 0
                    and not schematic[row_index - 1][pos].isdigit()
                    and schematic[row_index - 1][pos] != "."
                ):
                    valid = True
                elif (
                    pos != 0
                    and not schematic[row_index][pos - 1].isdigit()
                    and schematic[row_index][pos - 1] != "."
                ):
                    valid = True
                elif (
                    row_index != len(schematic) - 1
                    and not schematic[row_index + 1][pos].isdigit()
                    and schematic[row_index + 1][pos] != "."
                ):
                    valid = True
                elif (
                    (row_index != len(schematic) - 1 and pos != len(schematic[0]) - 1)
                    and not schematic[row_index + 1][pos + 1].isdigit()
                    and schematic[row_index + 1][pos + 1] != "."
                ):
                    valid = True
                elif (
                    (row_index != 0 and pos != 0)
                    and not schematic[row_index - 1][pos - 1].isdigit()
                    and schematic[row_index - 1][pos - 1] != "."
                ):
                    valid = True
                elif (
                    (row_index != 0 and pos != len(schematic[0]) - 1)
                    and not schematic[row_index - 1][pos + 1].isdigit()
                    and schematic[row_index - 1][pos + 1] != "."
                ):
                    valid = True
                elif (
                    pos != len(schematic[0]) - 1
                    and not schematic[row_index][pos + 1].isdigit()
                    and schematic[row_index][pos + 1] != "."
                ):
                    valid = True
                elif (
                    (row_index != len(schematic) - 1 and pos != 0)
                    and not schematic[row_index + 1][pos - 1].isdigit()
                    and schematic[row_index + 1][pos - 1] != "."
                ):
                    valid = True
                pos += 1
            print(current, valid)
            if valid:
                part_1 += int(current)
print(f"Part 1: {part_1}")
# print(f"Part 2: {part_2}"
