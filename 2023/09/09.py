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
            if part_2:
                value_to_add = current[i - 1][0] - current[i][0]
            else:
                value_to_add = current[i - 1][-1] + current[i][-1]
            position_to_add = 0 if part_2 else len(current[i - 1])
            current[i - 1].insert(position_to_add, value_to_add)
        result += value_to_add
    return result


print(f"Part 1: {calculate_sum()}")
print(f"Part 2: {calculate_sum(part_2 = True)}")
