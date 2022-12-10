with open("inputs/10.txt") as file:
    commands = file.read().splitlines()


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
        if command.startswith("addx"):
            cycle_number += 1
            if cycle_number_affects_strength(cycle_number):
                strength += cycle_number * x
            x += int(command[command.find(" ") + 1 :])
    return strength


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
