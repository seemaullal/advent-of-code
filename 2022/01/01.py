
with open("../inputs/1.txt") as file:
    calories_per_elf = [[int(calories) for calories in elf.split("\n")] for elf in file.read().split("\n\n")]

def part_1():
    return max([sum(calories) for calories in calories_per_elf])

def part_2():
    sorted_calories = sorted([sum(calories) for calories in calories_per_elf], reverse= True)
    return sum(sorted_calories[:3])

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
