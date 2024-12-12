import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/25.txt"

with open(input_file) as file:
    card, door = map(lambda n: int(n.strip()), file.readlines())

def calculate_loop_size(num):
    value = 1
    loop_size = 0
    while value != num:
        value = value * 7
        value = value % 20201227
        loop_size += 1
    return loop_size

def part_1():
    card_loop_size = calculate_loop_size(card)
    value = 1
    while card_loop_size:
        value = value * door
        value = value % 20201227
        card_loop_size -= 1
    return value

def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
