with open("inputs/input.txt", "r") as file:
    sequence = list(file.read().strip())


def calculate(is_part_1):
    A = []
    free_space = []
    file_id = 0
    results = []
    position = 0
    for index, character in enumerate(sequence):
        if index % 2 == 0:
            if not is_part_1:
                A.append((position, int(character), file_id))
            for _ in range(int(character)):
                results.append(file_id)
                if is_part_1:
                    A.append((position, 1, file_id))
                position += 1
            file_id += 1
        else:
            free_space.append((position, int(character)))
            for i in range(int(character)):
                results.append(None)
                position += 1

    for position, size, file_id in reversed(A):
        for space_index, (space_position, space_size) in enumerate(free_space):
            if space_position < position and size <= space_size:
                for index in range(size):
                    results[position + index] = None
                    results[space_position + index] = file_id

                free_space[space_index] = (space_position + size, space_size - size)
                break

    return sum(index * value for index, value in enumerate(results) if value is not None)


print(f"Part 1: {calculate(True)}")
print(f"Part 2: {calculate(False)}")
