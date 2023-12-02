games = []
AVAILABLE = {"blue": 14, "red": 12, "green": 13}

part_1 = 0

# with open("../inputs/2.txt") as file:
#     for line_number, line in enumerate(file):
#         valid = True
#         cube_sets = [
#             set.split(", ") for set in line.strip()[line.find(":") + 2 :].split("; ")
#         ]
#         for set in cube_sets:
#             for cube in set:
#                 number, color = cube.split(" ")
#                 if AVAILABLE[color] < int(number):
#                     valid = False
#         if valid:
#             part_1 += line_number + 1
part_2 = 0

with open("../inputs/2.txt") as file:
    for line in file:
        max_num_per_color = {}
        cube_sets = [
            set.split(", ") for set in line.strip()[line.find(":") + 2 :].split("; ")
        ]
        for set in cube_sets:
            for cube in set:
                number, color = cube.split(" ")
                if color not in max_num_per_color:
                    max_num_per_color[color] = int(number)
                else:
                    max_num_per_color[color] = max(
                        max_num_per_color[color], int(number)
                    )
        power = 1
        for max_needed in max_num_per_color.values():
            power *= max_needed
        part_2 += power


# print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
