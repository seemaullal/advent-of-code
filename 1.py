with open("inputs/day1.txt") as file:
    depths = [int(depth) for depth in file.readlines()]


def part_1():
    previous = depths[0]
    increasing = 0
    for num in depths[1:]:
        if num > previous:
            increasing += 1
        previous = num
    return increasing


def part_2():
    previous = depths[0] + depths[1] + depths[2]
    increasing = 0
    for index in range(len(depths) - 2):
        current = depths[index] + depths[index + 1] + depths[index + 2]
        if current > previous:
            increasing += 1
        previous = current
    return increasing


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
