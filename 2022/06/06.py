with open("inputs/6.txt") as file:
    input_chars = list(file.read().strip())

def get_unique_sequence_end_position(sequence_length):
    for i in range(len(input_chars)):
        if len(set(input_chars[i:i+sequence_length])) == sequence_length:
            return i + sequence_length

def part_1():
    return get_unique_sequence_end_position(4)

def part_2():
    return get_unique_sequence_end_position(14)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
