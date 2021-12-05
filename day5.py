from collections import Counter
coordinates = []
with open("inputs/day5.txt") as file:
    for line in file.readlines():
        start, end = line.strip().split(" -> ")
        coordinates.append([list(map(int, start.split(","))), list(map(int, end.split(",")))])


def part_1():
    seen = Counter()
    passed_more_than_once = 0
    for start, end in coordinates:
        if end[0] == start[0]:
            for i in range(min(end[1],start[1]), max(end[1],start[1]) + 1):
                current_point = (end[0], i)
                seen[current_point] += 1
                if seen[current_point] == 2:
                    passed_more_than_once += 1
        elif end[1] == start[1]:
            for i in range(min(end[0],start[0]), max(end[0],start[0]) + 1):
                current_point = (i, end[1])
                seen[current_point] += 1
                if seen[current_point] == 2:
                    passed_more_than_once += 1
    return passed_more_than_once


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
