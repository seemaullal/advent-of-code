import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/1.txt"
with open(input_file) as file:
    masses = [int(num.strip()) for num in file.readlines()]


def part_1():
    return sum([mass // 3 - 2 for mass in masses])


def calculate_fuel(mass):
    fuel_required = 0
    while mass:
        mass = max(mass // 3 - 2, 0)
        fuel_required += mass
    return fuel_required


def part_2():
    return sum([calculate_fuel(mass) for mass in masses])


print(f"Part 1 answer: {part_1()}")
print(f"Part 2 answer: {part_2()}")
