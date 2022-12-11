with open("inputs/sample11.txt") as file:
    monkey_input = [line.strip() for line in file]
monkeys = []

for line in monkey_input:
    if line.startswith("Monkey"):
        monkeys.append({})
        test = {}
    if line.strip().startswith("Starting items"):
        items = [int(item) for item in line[line.find(":") + 2 :].split(",")]
        monkeys[-1]["starting_items"] = items
    if line.strip().startswith("Operation"):
        formula_parts = line[line.find("=") + 2 :].split(" ")
        monkeys[-1]["operation"] = [
            int(part) if part.isnumeric() else part for part in formula_parts
        ]
    if line.strip().startswith("Test"):
        test["divisible_by"] = int(line[line.find("by") + 2 :])
    if line.strip().startswith("If true"):
        test[True] = int(line[line.rfind(" ") + 1 :])
    if line.strip().startswith("If false"):
        test[False] = int(line[line.rfind(" ") + 1 :])
        monkeys[-1]["test"] = test


def part_1():
    pass


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
