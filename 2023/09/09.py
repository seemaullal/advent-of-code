sequences = []
with open("../inputs/9.txt") as file:
    for line in file:
        sequences.append([int(value) for value in line.split(" ")])
part_1 = 0
for sequence in sequences:
    current = [sequence]
    while True:
        current.append(
            [value2 - value1 for value1, value2 in zip(current[-1], current[-1][1:])]
        )
        if set(current[-1]) == {0}:
            break
    current[-1].append(0)
    for i in range(len(current) - 2, 0, -1):
        current[i - 1].append(current[i][-1] + current[i - 1][-1])
    part_1 += current[i - 1][-1]

print(f"Part 1: {part_1}")
# print(f"Part 2: {part_2}")
