with open("inputs/8.txt") as file:
    heights = [[int(num) for num in list(line.strip())] for line in file]


def max_in_column(starting_row, ending_row, column):
    max_in_col = float("-inf")
    for row_num in range(starting_row, ending_row):
        max_in_col = max(max_in_col, heights[row_num][column])
    return max_in_col


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
                if max_in_column(0, row, col) < heights[row][col]:
                    num_visible += 1
                elif max_in_column(row + 1, len(heights), col) < heights[row][col]:
                    num_visible += 1
    return num_visible


def part_2():
    highest_scenic_score = 0
    for row in range(len(heights)):
        for col in range(len(heights[0])):
            if (
                row == 0
                or row == len(heights) - 1
                or col == 0
                or col == len(heights[0]) - 1
            ):
                continue

            current_row = row - 1
            top_viewing_distance = 0

            while current_row >= 0:
                top_viewing_distance += 1
                if heights[current_row][col] >= heights[row][col]:
                    break
                current_row -= 1

            current_row = row + 1
            down_viewing_distance = 0

            while current_row < len(heights):
                down_viewing_distance += 1
                if heights[current_row][col] >= heights[row][col]:
                    break
                current_row += 1

            left_viewing_distance = 0
            current_col = col - 1

            while current_col >= 0:
                left_viewing_distance += 1
                if heights[row][current_col] >= heights[row][col]:
                    break
                current_col -= 1

            right_viewing_distance = 0
            current_col = col + 1

            while current_col < len(heights[row]):
                right_viewing_distance += 1
                if heights[row][current_col] >= heights[row][col]:
                    break
                current_col += 1

            highest_scenic_score = max(
                highest_scenic_score,
                top_viewing_distance
                * down_viewing_distance
                * left_viewing_distance
                * right_viewing_distance,
            )
    return highest_scenic_score


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
