with open("inputs/10.txt") as file:
    commands = [command.split() for command in file.read().splitlines()]


def cycle_number_affects_strength(cycle_number):
    return cycle_number % 40 == 20


def part_1():
    cycle_number = 0
    x = 1
    strength = 0
    for command in commands:
        cycle_number += 1
        if cycle_number_affects_strength(cycle_number):
            strength += cycle_number * x
        if command[0] == "addx":
            cycle_number += 1
            if cycle_number_affects_strength(cycle_number):
                strength += cycle_number * x
            x += int(command[1])
    return strength


def update_pixels(pixels, cycle_number, x):
    row_number = cycle_number // 40
    col_number = cycle_number % 40
    pixels[row_number][col_number] = "█" if abs(x - col_number) <= 1 else " "


def part_2():
    cycle_number = 0
    x = 1
    pixels = [["" for _ in range(40)] for _ in range(6)]
    for command in commands:
        update_pixels(pixels, cycle_number, x)
        cycle_number += 1
        if command[0] == "addx":
            update_pixels(pixels, cycle_number, x)
            cycle_number += 1
            x += int(command[1])
    return pixels


print(f"Part 1: {part_1()}")
pixels = part_2()
for index in range(len(pixels)):
    print("".join(pixels[index]))
