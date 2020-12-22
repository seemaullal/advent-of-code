expressions = [expression.strip() for expression in open('day18_input.txt').readlines()]

def evaluate_operator(left, operator, right):
    if operator == '+':
        return left + right
    return left * right

def evaluate(line, is_part_two, inMultiply=False):
    left = 0
    operator = '+'
    right = 0
    while line:
        char, line = line[0], line[1:]
        if char in '0123456789':
            right = right * 10 + int(char)
            continue
        if char == ' ':
            continue
        if is_part_two:
            if inMultiply and char in '*)':
                line = char + line
                break
            if char == '*':
                temp, line = evaluate(line, is_part_two, True)
                left = (left + right) * temp
                right = 0
                continue
        if char in '+*':
            left = evaluate_operator(left, operator, right)
            operator = char
            right = 0
            continue
        if char == '(':
            right, line = evaluate(line, is_part_two)
        if char == ')':
            break
    return evaluate_operator(left, operator, right), line

# part 1
print('part 1', sum([evaluate(expression, False)[0] for expression in expressions]))
print('part 2', sum([evaluate(expression, True)[0] for expression in expressions]))