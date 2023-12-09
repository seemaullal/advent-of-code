sequences = []
with open("../inputs/9.txt") as file:
    for line in file:
        sequences.append([int(value) for value in line.split(" ")])


def calculate_sum(part_2=False):
    result = 0
    for sequence in sequences:
        current = [sequence]
        while True:
            current.append(
                [
                    value2 - value1
                    for value1, value2 in zip(current[-1], current[-1][1:])
                ]
            )
            if all(num == 0 for num in current[-1]):
                break
        current[-1].append(0)
        for i in range(len(current) - 2, 0, -1):
            index = 0 if part_2 else -1
            if part_2:
                current[i - 1].insert(0, current[i - 1][index] - current[i][index])
            else:
                current[i - 1].append(current[i][index] + current[i - 1][index])
        result += current[i - 1][index]
    return result


print(f"Part 1: {calculate_sum()}")
print(f"Part 2: {calculate_sum(part_2 = True)}")
