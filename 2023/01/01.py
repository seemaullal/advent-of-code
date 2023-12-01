NUMS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

with open("../inputs/1.txt") as file:
    document_lines = file.read().strip().split("\n")


part_1 = 0
part_2 = 0
for line in document_lines:
    part_1_values = []
    part_2_values = []
    for char_index, character in enumerate(line):
        if character.isdigit():
            part_1_values.append(character)
            part_2_values.append(character)
        for num_index, word in enumerate(NUMS):
            if line[char_index : char_index + len(word)] == word:
                part_2_values.append(num_index + 1)
    part_1 += int(f"{part_1_values[0]}{part_1_values[-1]}")
    part_2 += int(f"{part_2_values[0]}{part_2_values[-1]}")


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
