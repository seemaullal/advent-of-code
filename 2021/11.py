import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/11.txt"
with open(input_file) as file:
    energy = [list(map(int, list(line.strip()))) for line in file.readlines()]


def part_1():
    num_flashes = 0
    for _ in range(100):
        for row_num in range(len(energy)):
            for col_num in range(len(energy[row_num])):
                energy[row_num][col_num] += 1
        still_flashing = True
        while still_flashing:
            still_flashing = False
            for row_num in range(len(energy)):
                for col_num in range(len(energy[row_num])):
                    if energy[row_num][col_num] > 9:
                        num_flashes += 1
                        energy[row_num][col_num] = 0
                        if row_num != 0:
                            # top
                            if energy[row_num - 1][col_num] != 0:
                                energy[row_num - 1][col_num] += 1
                            if energy[row_num - 1][col_num] > 9:
                                still_flashing = True
                            if col_num != 0:
                                # diagonal up left
                                if energy[row_num - 1][col_num - 1] != 0:
                                    energy[row_num - 1][col_num - 1] += 1
                                if energy[row_num - 1][col_num - 1] > 9:
                                    still_flashing = True
                            if col_num != len(energy[row_num]) - 1:
                                # diagonal up right
                                if energy[row_num - 1][col_num + 1] != 0:
                                    energy[row_num - 1][col_num + 1] += 1
                                if energy[row_num - 1][col_num + 1] > 9:
                                    still_flashing = True
                        if row_num != len(energy[row_num]) - 1:
                            # down
                            if energy[row_num + 1][col_num] != 0:
                                energy[row_num + 1][col_num] += 1
                            if energy[row_num + 1][col_num] > 9:
                                still_flashing = True
                            if col_num != 0:
                                # diagonal down left
                                if energy[row_num + 1][col_num - 1] != 0:
                                    energy[row_num + 1][col_num - 1] += 1
                                if energy[row_num + 1][col_num - 1] > 9:
                                    still_flashing = True
                            if col_num != len(energy[row_num]) - 1:
                                # diagonal down right
                                if energy[row_num + 1][col_num + 1] != 0:
                                    energy[row_num + 1][col_num + 1] += 1
                                if energy[row_num + 1][col_num + 1] > 9:
                                    still_flashing = True
                        if col_num != 0:
                            if energy[row_num][col_num - 1] != 0:
                                energy[row_num][col_num - 1] += 1
                            if energy[row_num][col_num - 1] > 9:
                                still_flashing = True
                        if col_num != len(energy[row_num]) - 1:
                            if energy[row_num][col_num + 1] != 0:
                                energy[row_num][col_num + 1] += 1
                            if energy[row_num][col_num + 1] > 9:
                                still_flashing = True

    return num_flashes


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
