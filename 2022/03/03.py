with open("inputs/3.txt") as file:
    rucksack_items = [list(rucksack.strip()) for rucksack in file]

def part_1():
    priority_sum = 0
    for items in rucksack_items:
        item_number = len(items)
        compartment1 = set(items[:(item_number//2)])
        compartment2 = set(items[(item_number//2):])
        in_common = compartment1.intersection(compartment2).pop()
        if in_common.lower() == in_common:
            priority_sum += ord(in_common) - 96
        else:
            priority_sum += ord(in_common)-38
    return priority_sum

def part_2():
    priority_sum = 0
    for group_start_index in range(0, len(rucksack_items)-2, 3):
        group = [set(items) for items in rucksack_items[group_start_index:group_start_index + 3]]
        in_common = group[0].intersection(group[1]).intersection(group[2]).pop()
        if in_common.lower() == in_common:
            priority_sum += ord(in_common) - 96
        else:
            priority_sum += ord(in_common)-38
    return priority_sum

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
