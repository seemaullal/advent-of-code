with open("inputs/7.txt") as file:
    rules = [line.strip() for line in file]

bag_dependencies = {}

for rule in rules:
    name, contents = rule[:-1].split(" contain ")
    name = name[: name.find("bag")].strip()
    if contents == "no other bags":
        items = {}
    else:
        bags = contents.split(",")
        items = {}
        for bag in bags:
            bag = bag.strip()
            number = int(bag[0])
            rest = bag[1 : bag.find("bag")].strip()
            items[rest] = number

    bag_dependencies[name] = items


def find_golden_bags(bag):
    if bag == "shiny gold":
        return True

    dependencies = bag_dependencies[bag]
    for bag_type in dependencies:
        if find_golden_bags(bag_type):
            return True
    return False


def count_bags(bag, index=1):
    count = 1
    for bag_type, bag_number in bag_dependencies[bag].items():
        count += bag_number * count_bags(bag_type, index + 1)

    return count


def part_1():
    return sum(find_golden_bags(bag) for bag in bag_dependencies) - 1


def part_2():
    return count_bags("shiny gold") - 1


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
