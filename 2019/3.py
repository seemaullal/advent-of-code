with open("inputs/3.txt") as file:
    wire_1, wire_2 = [line.strip().split(",") for line in file.readlines()]


def part_1():
    first_location = [0, 0]
    second_location = [0, 0]
    max_intersection_distance = 0
    for path_1, path_2 in zip(wire_1, wire_2):
        direction_1 = path_1[0]
        distance_1 = int(path_1[1:])
        direction_2 = path_2[0]
        distance_2 = int(path_2[1:])
        if direction_1 == "L":
            first_location[0] -= distance_1
        if direction_1 == "R":
            first_location[0] += distance_1
        if direction_1 == "U":
            first_location[1] += distance_1
        if direction_1 == "D":
            first_location[1] -= distance_1
        if direction_2 == "L":
            second_location[0] -= distance_2
        if direction_2 == "R":
            second_location[0] += distance_2
        if direction_2 == "U":
            second_location[1] += distance_2
        if direction_2 == "D":
            second_location[1] -= distance_2
        print(first_location)
        print(second_location, "\n")
        if first_location == second_location:
            if (
                abs(first_location[0]) + abs(first_location[1])
                > max_intersection_distance
            ):
                max_intersection_distance = abs(first_location[0]) + abs(
                    first_location[1]
                )
    return max_intersection_distance


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
