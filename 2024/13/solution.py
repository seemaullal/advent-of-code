from re import findall

PRIZE_ERROR = 10_000_000_000_000

with open("inputs/input.txt", "r") as file:
    groups = file.read().strip().split("\n\n")


def get_digits(string):
    return [int(digit) for digit in findall(r"\d+", string)]


groups = [group.split("\n") for group in groups]

nums = [
    get_digits(button_a) + get_digits(button_b) + get_digits(prize)
    for button_a, button_b, prize in groups
]


def solve(x1, y1, x2, y2, a, b):
    button_a = (x2 * b - y2 * a) / (y1 * x2 - x1 * y2)
    button_b = (a - button_a * x1) / x2
    if button_a.is_integer() and button_b.is_integer():
        return int(3 * button_a + button_b)
    return 0


part_1 = sum(
    solve(a_x, a_y, b_x, b_y, prize_x, prize_y)
    for a_x, a_y, b_x, b_y, prize_x, prize_y in nums
)
part_2 = sum(
    solve(a_x, a_y, b_x, b_y, prize_x + PRIZE_ERROR, prize_y + PRIZE_ERROR)
    for a_x, a_y, b_x, b_y, prize_x, prize_y in nums
)

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
