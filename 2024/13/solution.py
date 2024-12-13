from re import findall

part_1 = 0
part_2 = 0

with open("inputs/input.txt", "r") as file:
    groups = file.read().strip().split("\n\n")

groups = [group.split("\n") for group in groups]
nums = []
for button_a, button_b, prize in groups:
    button_a_x, button_a_y = findall(r"\d+", button_a)
    button_b_x, button_b_y = findall(r"\d+", button_b)
    prize_x, prize_y = findall(r"\d+", prize)
    nums.append(
        [
            int(button_a_x),
            int(button_a_y),
            int(button_b_x),
            int(button_b_y),
            int(prize_x),
            int(prize_y),
        ]
    )


def solve(x1, y1, x2, y2, a, b):
    button_a = (x2 * b - y2 * a) / (y1 * x2 - x1 * y2)
    button_b = (a - button_a * x1) / x2
    if button_a.is_integer() and button_b.is_integer():
        return int(3 * button_a + button_b)
    return 0


for [button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y] in nums:
    part_1 += solve(button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y)
    part_2 += solve(
        button_a_x,
        button_a_y,
        button_b_x,
        button_b_y,
        prize_x + 10000000000000,
        prize_y + 10000000000000,
    )


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
