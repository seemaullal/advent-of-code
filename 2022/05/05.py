with open("inputs/5.txt") as file:
    stack_input, moves = open("inputs/5.txt").read().split("\n\n")

STACK_NUMBER = int(stack_input[-1])
stack_input = stack_input.split("\n")[:-1][::-1]

stacks_part_1 = [[] for _ in range(STACK_NUMBER)]
stacks_part_2 = [[] for _ in range(STACK_NUMBER)]

for line in stack_input:
    stack_number = 0
    for i in range(1, len(line), 4):
        if line[i] != " ":
            stacks_part_1[stack_number].append(line[i])
            stacks_part_2[stack_number].append(line[i])
        stack_number += 1

for move in moves.split("\n"):
    num_moves, from_stack, to_stack = [
        int(value) for value in move.split(" ") if value.isnumeric()
    ]
    for _ in range(num_moves):
        stacks_part_1[to_stack - 1].append(stacks_part_1[from_stack - 1].pop(-1))
    stacks_part_2[to_stack - 1].extend(stacks_part_2[from_stack - 1][-num_moves:])
    stacks_part_2[from_stack - 1] = stacks_part_2[from_stack - 1][:-num_moves]

part_1 = "".join([stack[-1] for stack in stacks_part_1])
part_2 = "".join([stack[-1] for stack in stacks_part_2])


print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
