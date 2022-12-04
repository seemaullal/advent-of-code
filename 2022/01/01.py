with open("inputs/1.txt") as file:
    elves = file.read().strip().split("\n\n")
elves = [[int(n) for n in num_string.split("\n")] for num_string in elves]
calories = [sum(amounts) for amounts in elves]
part_1 = max(calories)
part_2 = sum(sorted(calories)[-3:])

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
