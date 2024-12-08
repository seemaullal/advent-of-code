from re import match

part_1 = 0
part_2 = 0

with open("inputs/03.txt", "r") as file:
    sequence = file.read().strip()

is_on = True
for index in range(len(sequence)):
    if sequence[index:].startswith("don't()"):
        is_on = False
    elif sequence[index:].startswith("do()"):
        is_on = True
    current = match(r"mul\((\d+),(\d+)\)", sequence[index:])
    if current:
        product = int(current.group(1)) * int(current.group(2))
        part_1 += product
        part_2 += product * is_on


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
