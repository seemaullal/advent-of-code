numbers = [int(line.strip()) for line in open("day9_input.txt").readlines()]

# part 1
current_index = 26
previous_twenty_five = numbers[:25]
while current_index < len(numbers) - 25:
    nums_found = False
    numbers_to_search = set(previous_twenty_five)
    for num in numbers_to_search:
        if (numbers[current_index] - num) in numbers_to_search:
            nums_found = True
            break
    if not nums_found:
        part1_answer = numbers[current_index]
        break
    previous_twenty_five = previous_twenty_five[1:] + [numbers[current_index]]
    current_index += 1
print('part 1', part1_answer)

def part_2(target_sum):
    for start_index in range(len(numbers)):
        for end_index in range(start_index + 1, len(numbers)):
            current_numbers = numbers[start_index : end_index + 1]
            sum_of_current = sum(current_numbers)
            if sum_of_current == target_sum:
                return min(current_numbers) + max(current_numbers)
print('part2', part_2(part1_answer))
