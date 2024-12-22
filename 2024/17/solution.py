reg_a = 41644071
reg_b = 0
reg_c = 0
program = [int(num) for num in "2,4,1,2,7,5,1,7,4,4,0,3,5,5,3,0".split(",")]


def get_combo(operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return reg_a
    elif operand == 5:
        return reg_b
    elif operand == 6:
        return reg_c

current_index = 0
part_1 = []
part_2 = 0
while current_index < len(program):
    no_jump = True
    opcode = program[current_index]
    operand = program[current_index + 1]
    if opcode == 0:
        reg_a = reg_a // 2**get_combo(operand)
    elif opcode == 1:
        reg_b = reg_b ^ operand
    elif opcode == 2:
        reg_b = get_combo(operand) % 8
    elif opcode == 3 and reg_a != 0:
        no_jump = False
        current_index = operand
    elif opcode == 4:
        reg_b = reg_b ^ reg_c
    elif opcode == 5:
        part_1.append(get_combo(operand) % 8)
    elif opcode == 6:
        reg_b = reg_a // 2**get_combo(operand)
    elif opcode == 7:
        reg_c = reg_a //  2**get_combo(operand)

    if no_jump:
        current_index += 2


print(f"Part 1: {','.join(map(str, part_1))}")
print(f"Part 2: {part_2}")
