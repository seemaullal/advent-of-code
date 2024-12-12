part_1 = 0
part_2 = 0

with open("inputs/09.txt", "r") as file:
    sequence = list(file.read().strip())
blocks = []
is_free_space = False

id = 0
for char in sequence:
    if is_free_space:
        for _ in range(int(char)):
            blocks.append(".")
    else:
        for _ in range(int(char)):
            blocks.append(str(id))
        id += 1
    is_free_space = not is_free_space
current_free_space_index = 0
right_index = len(blocks) -1
while current_free_space_index < right_index:
    while blocks[right_index] == ".":
        right_index -= 1
    while blocks[current_free_space_index] != ".":
        current_free_space_index += 1
    if current_free_space_index < right_index:
        blocks[current_free_space_index] = blocks[right_index]
        blocks[right_index] = "."

for index, char in enumerate(blocks):
    if char == ".":
        break
    part_1 += index * int(char)

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
