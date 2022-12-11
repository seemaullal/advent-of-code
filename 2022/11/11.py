from copy import deepcopy

with open("inputs/11.txt") as file:
    monkey_input = [line.strip() for line in file]
monkeys = []
product_of_divisible_by = 1

for line in monkey_input:
    if line.startswith("Monkey"):
        monkeys.append({})
        test = {}
    if line.strip().startswith("Starting items"):
        items = [int(item) for item in line[line.find(":") + 2 :].split(",")]
        monkeys[-1]["starting_items"] = items
    if line.strip().startswith("Operation"):
        monkeys[-1]["operation"] = line[line.find("=") + 2 :].split(" ")
    if line.strip().startswith("Test"):
        value = int(line[line.find("by") + 2 :])
        product_of_divisible_by *= value
        test["divisible_by"] = value
    if line.strip().startswith("If true"):
        test[True] = int(line[line.rfind(" ") + 1 :])
    if line.strip().startswith("If false"):
        test[False] = int(line[line.rfind(" ") + 1 :])
        monkeys[-1]["test"] = test


def part_1():
    current_monkeys = deepcopy(monkeys)
    inspected_items = [0 for _ in current_monkeys]
    for _ in range(20):
        for monkey_number, monkey in enumerate(current_monkeys):
            for worry_level in monkey["starting_items"]:
                inspected_items[monkey_number] += 1
                expression = ""
                for part in monkey["operation"]:
                    expression += "worry_level" if part == "old" else part
                worry_level = eval(expression) // 3
                key = worry_level % monkey["test"]["divisible_by"] == 0
                current_monkeys[monkey["test"][key]]["starting_items"].append(
                    worry_level
                )
            monkey["starting_items"] = []
    inspected_items.sort()
    return inspected_items[-2] * inspected_items[-1]


def part_2():
    current_monkeys = deepcopy(monkeys)
    inspected_items = [0 for _ in current_monkeys]
    for _ in range(10_000):
        for monkey_number, monkey in enumerate(current_monkeys):
            for worry_level in monkey["starting_items"]:
                inspected_items[monkey_number] += 1
                expression = ""
                for part in monkey["operation"]:
                    expression += "worry_level" if part == "old" else part
                worry_level = eval(expression) % product_of_divisible_by
                key = worry_level % monkey["test"]["divisible_by"] == 0
                current_monkeys[monkey["test"][key]]["starting_items"].append(
                    worry_level
                )
            monkey["starting_items"] = []
    inspected_items.sort()
    return inspected_items[-2] * inspected_items[-1]


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
