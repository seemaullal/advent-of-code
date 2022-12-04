import re

with open("inputs/4.txt") as file:
    assignments = []
    for elf_assignments in file:
        values = [int(value) for value in  re.split(",|-", elf_assignments.strip())]
        assignments.append(
           [
                values[0],
                values[1],
                values[2],
                values[3]
           ]
        )

def part_1():
    count = 0
    for (elf1_start, elf1_end, elf2_start, elf2_end) in assignments:
        if elf2_start >= elf1_start and elf2_end <= elf1_end:
            count += 1
        elif elf1_start >= elf2_start and elf1_end <= elf2_end:
            count += 1
    return count

def part_2():
    count = 0
    for (elf1_start, elf1_end, elf2_start, elf2_end) in assignments:
        if elf1_end < elf2_start or elf2_end < elf1_start:
            continue
        count += 1
    return count

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
