def split_into_parts(command):
    direction, distance = command.split()
    return (direction, int(distance))


with open("inputs/day2.txt") as file:
    commands = map(split_into_parts, file.readlines())


def part_1_and_2():
    horizontal = 0
    depth_part1_aim_part_2 = 0  # same as aim for part 2
    depth_part2 = 0
    for command, distance in commands:
        if command == "forward":
            horizontal += distance
            depth_part2 += depth_part1_aim_part_2 * distance
        elif command == "up":
            depth_part1_aim_part_2 -= distance
        else:
            depth_part1_aim_part_2 += distance
    print(f"Part 1: {horizontal * depth_part1_aim_part_2}")
    print(f"Part 2: {horizontal * depth_part2}")


part_1_and_2()
