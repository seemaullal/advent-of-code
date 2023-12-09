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
            if set(current[-1]) == {0}:
                break
        if part_2:
            current[-1].insert(0, 0)
            for i in range(len(current) - 2, 0, -1):
                current[i - 1].insert(0, current[i - 1][0] - current[i][0])
            result += current[i - 1][0]
        else:
            current[-1].append(0)
            for i in range(len(current) - 2, 0, -1):
                current[i - 1].append(current[i][-1] + current[i - 1][-1])
            result += current[i - 1][-1]
    return result


print(f"Part 1: {calculate_sum()}")
print(f"Part 2: {calculate_sum(part_2 = True)}")
