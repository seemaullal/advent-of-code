from collections import defaultdict

cards = []
with open("../inputs/4.txt") as file:
    for line in file:
        cards.append(
            [group.split() for group in line.strip().split(": ")[1].split(" | ")]
        )
# part_1 = 0
card_counts = defaultdict(int)
for index, card in enumerate(cards):
    card_counts[index] += 1
    winning, actual = card
    matches = len(set(winning) & set(actual))
    for card_index_to_add in range(1, matches + 1):
        card_counts[index + card_index_to_add] += card_counts[index]
part_2 = sum(card_counts.values())

# print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
