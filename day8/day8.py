commands = [command.strip().split() for command in open("day8_input.txt").readlines()]
def loop_until_repeated_command(command_list):
    seen_command_indices = set()
    current_command_index = 0
    acc = 0
    while current_command_index not in seen_command_indices and current_command_index < len(command_list):
        seen_command_indices.add(current_command_index)
        # print(command_list[current_command_index])
        current_command, num = command_list[current_command_index]
        num = int(num)
        if current_command == 'acc':
            acc += num
            current_command_index += 1
        elif current_command == 'jmp':
            current_command_index += num
        else:
            current_command_index += 1
    return (acc, current_command_index)

# part 1
print('part 1', loop_until_repeated_command(commands)[0])

# part 2
command_index = -1
while command_index < len(commands) -1:
    command_index += 1
    current_command, num = commands[command_index]
    if current_command == 'jmp':
        swapped_command = 'nop'
    elif current_command == 'nop':
        swapped_command = 'jmp'
    else:
        continue
    commands_with_swap = commands[:]
    commands_with_swap[command_index] =[swapped_command, num]
    acc, last_command_index = loop_until_repeated_command(commands_with_swap)
    if last_command_index == len(commands):
        print('part 2', acc)
        break