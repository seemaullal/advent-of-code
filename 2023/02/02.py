from collections import defaultdict

PART_1_AVAILABLE_VALUES = {"blue": 14, "red": 12, "green": 13}

part_1 = 0
part_2 = 0
with open("../inputs/2.txt") as file:
    for line_number, line in enumerate(file):
        valid_for_part_1 = True
        max_required_part_2 = defaultdict(int)
        for set in line.strip()[line.find(":") + 2 :].split("; "):
            for cube in set.split(", "):
                number, color = cube.split(" ")
                if PART_1_AVAILABLE_VALUES[color] < int(number):
                    valid_for_part_1 = False
                max_required_part_2[color] = max(
                    max_required_part_2[color], int(number)
                )
        if valid_for_part_1:
            part_1 += line_number + 1
        power = 1
        for max_needed in max_required_part_2.values():
            power *= max_needed
        part_2 += power


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
