from collections import Counter

coordinates = []
with open("inputs/day5.txt") as file:
    for line in file.readlines():
        start, end = line.strip().split(" -> ")
        coordinates.append([list(map(int, start.split(","))), list(map(int, end.split(",")))])


def update_seen(start: int, end: int, update_x: bool, other_coordinate: int, seen: Counter) -> int:
    """Returns number coordinates that were passed more than once after this run"""
    passed_more_than_once = 0
    for i in range(start, end + 1):
        if update_x:
            current_point = (i, other_coordinate)
        else:
            current_point = (other_coordinate, i)
        seen[current_point] += 1
        if seen[current_point] == 2:
            passed_more_than_once += 1
    return passed_more_than_once


def part_1():
    seen = Counter()
    passed_more_than_once = 0
    for start, end in coordinates:
        if end[0] == start[0]:
            starting_y = min(end[1], start[1])
            ending_y = max(end[1], start[1])
            passed_more_than_once += update_seen(starting_y, ending_y, False, start[0], seen)
        elif end[1] == start[1]:
            starting_x = min(end[0], start[0])
            ending_x = max(end[0], start[0])
            passed_more_than_once += update_seen(starting_x, ending_x, True, start[1], seen)
    return passed_more_than_once


def part_2():
    seen = Counter()
    passed_more_than_once = 0
    for start, end in coordinates:
        if end[0] == start[0]:
            starting_y = min(end[1], start[1])
            ending_y = max(end[1], start[1])
            passed_more_than_once += update_seen(starting_y, ending_y, False, start[0], seen)
        elif end[1] == start[1]:
            starting_x = min(end[0], start[0])
            ending_x = max(end[0], start[0])
            passed_more_than_once += update_seen(starting_x, ending_x, True, start[1], seen)
        else:
            current_x = start[0]
            current_y = start[1]
            increase_by_x = 1 if end[0] > start[0] else -1
            increase_by_y = 1 if end[1] > start[1] else -1
            while current_x != end[0] + increase_by_x and current_y != end[1] + increase_by_y:
                current_point = (current_x, current_y)
                seen[current_point] += 1
                if seen[current_point] == 2:
                    passed_more_than_once += 1
                current_x += increase_by_x
                current_y += increase_by_y
    return passed_more_than_once


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
