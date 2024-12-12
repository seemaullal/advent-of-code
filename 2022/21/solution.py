with open("inputs/21.txt") as file:
    monkeys = {}
    for line in file.read().splitlines():
        monkey, operation = line.split(": ")
        if operation.isnumeric():
            monkeys[monkey] = int(operation)
        else:
            monkeys[monkey] = operation.split(" ")


def is_integer(value):
    return isinstance(value, int)


def part_1():
    while True:
        for monkey, instruction in monkeys.items():
            if is_integer(instruction):
                continue
            part1, op, part2 = instruction
            if is_integer(monkeys[part1]) and is_integer(monkeys[part2]):
                monkeys[monkey] = int(eval(f"{monkeys[part1]}{op}{monkeys[part2]}"))
                if monkey == "root":
                    return monkeys[monkey]


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
