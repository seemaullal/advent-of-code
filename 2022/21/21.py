with open("inputs/21.txt") as file:
    monkeys = {}
    for line in file.read().splitlines():
        monkey, operation = line.split(": ")
        if operation.isnumeric():
            monkeys[monkey] = int(operation)
        else:
            monkeys[monkey] = operation.split(" ")


def part_1():
    while True:
        for monkey, operation in monkeys.items():
            if isinstance(operation, int):
                continue
            if isinstance(monkeys[operation[0]], int) and isinstance(
                monkeys[operation[2]], int
            ):
                monkeys[monkey] = int(
                    eval(
                        f"{monkeys[operation[0]]}{operation[1]}{monkeys[operation[2]]}"
                    )
                )
                if monkey == "root":
                    return monkeys[monkey]


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
