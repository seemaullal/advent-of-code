cards = []
with open("../inputs/4.txt") as file:
    for line in file:
        cards.append(
            [group.split() for group in line.strip().split(": ")[1].split(" | ")]
        )
part_1 = 0
for card in cards:
    winning, actual = card
    intersection = set(winning) & set(actual)
    if len(intersection):
        current = 1
        for i in range(len(intersection) - 1):
            current *= 2
        part_1 += current

print(f"Part 1: {part_1}")
# print(f"Part 2: {part_2}")
