with open("inputs/10.txt") as file:
    commands = [command.split() for command in file.read().splitlines()]


def strength_increase(current_strength, cycle_number, x):
    return cycle_number * x if cycle_number % 40 == 20 else 0


def update_pixels(pixels, cycle_number, x):
    row_number = cycle_number // 40
    col_number = cycle_number % 40
    pixels[row_number][col_number] = "█" if abs(x - col_number) <= 1 else " "


part_1 = cycle_number = 0
x = 1
pixels = [["" for _ in range(40)] for _ in range(6)]
for command in commands:
    update_pixels(pixels, cycle_number, x)
    cycle_number += 1
    part_1 += strength_increase(part_1, cycle_number, x)
    if command[0] == "addx":
        update_pixels(pixels, cycle_number, x)
        cycle_number += 1
        part_1 += strength_increase(part_1, cycle_number, x)
        x += int(command[1])

print(f"Part 1: {part_1}")
print(f"Part 2:")
print("\n".join(["".join(row) for row in pixels]))
