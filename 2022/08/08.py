with open("inputs/8.txt") as file:
    heights = [[int(num) for num in list(line.strip())] for line in file]


def part_1():
    num_visible = 0
    for row in range(len(heights)):
        for col in range(len(heights[0])):
            if (
                row == 0
                or row == len(heights) - 1
                or col == 0
                or col == len(heights[0]) - 1
            ):
                num_visible += 1
            elif max(heights[row][:col]) < heights[row][col]:
                num_visible += 1
            elif max(heights[row][col + 1 :]) < heights[row][col]:
                num_visible += 1
            else:
                max_in_col = float("-inf")
                for row_num in range(row):
                    max_in_col = max(max_in_col, heights[row_num][col])
                if max_in_col < heights[row][col]:
                    num_visible += 1
                    continue
                max_in_col = float("-inf")
                for row_num in range(row + 1, len(heights)):
                    max_in_col = max(max_in_col, heights[row_num][col])
                if max_in_col < heights[row][col]:
                    num_visible += 1
                    continue
    return num_visible


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
