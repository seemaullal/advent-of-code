calories = []

with open("inputs/01.txt", "r") as file:
    elves  = [[int(item) for item in elf.split()] for elf in file.read().split("\n\n")]

for elf in elves:
    calories.append(sum(elf))

sorted_calories = sorted(calories, reverse=True)

print(f"Part 1: {sorted_calories[0]}")
print(f"Part 2: {sum(sorted_calories[:3])}")
