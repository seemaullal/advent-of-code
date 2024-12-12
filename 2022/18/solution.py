with open("inputs/18.txt") as file:
    cubes = set()
    for line in file.read().splitlines():
        cubes.add(tuple(int(x) for x in line.split(",")))


def part_1():
    count = 0
    for x, y, z in cubes:
        for offset in (-1, 1):
            count += int(((x + offset, y, z)) not in cubes)
            count += int(((x, y + offset, z)) not in cubes)
            count += int(((x, y, z + offset)) not in cubes)
    return count


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
