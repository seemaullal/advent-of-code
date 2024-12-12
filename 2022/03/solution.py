with open("inputs/3.txt") as file:
    rucksack_items = [list(rucksack.strip()) for rucksack in file]

def get_priority(character):
    if character.lower() == character:
        return ord(character) - 96
    else:
        return ord(character)-38

def part_1():
    priority_sum = 0
    for items in rucksack_items:
        item_number = len(items)
        compartment1 = set(items[:(item_number//2)])
        compartment2 = set(items[(item_number//2):])
        in_common = compartment1.intersection(compartment2).pop()
        priority_sum += get_priority(in_common)
    return priority_sum

def part_2():
    priority_sum = 0
    for group_start_index in range(0, len(rucksack_items)-2, 3):
        group1, group2, group3 = [set(items) for items in rucksack_items[group_start_index:group_start_index + 3]]
        in_common = group1.intersection(group2).intersection(group3).pop()
        priority_sum += get_priority(in_common)
    return priority_sum

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
