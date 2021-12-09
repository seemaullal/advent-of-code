import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/9.txt"
with open(input_file) as file:
    heights = []
    for line in file.readlines():
        heights.append([int(height) for height in list(line.strip())])


def part_1():
    low_points = []
    for row_num in range(len(heights)):
        for col_num in range(len(heights[0])):
            eligible = True
            current = heights[row_num][col_num]
            if row_num != 0:
                if heights[row_num - 1][col_num] <= current:
                    eligible = False
            if row_num != len(heights) - 1:
                if heights[row_num + 1][col_num] <= current:
                    eligible = False
            if col_num != 0:
                if heights[row_num][col_num - 1] <= current:
                    eligible = False
            if col_num != len(heights[0]) - 1:
                if heights[row_num][col_num + 1] <= current:
                    eligible = False
            if eligible:
                low_points.append(current)
    return sum([height + 1 for height in low_points])


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
