import sys
from collections import Counter

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/14.txt"
with open(input_file) as file:
    sequence = file.readline().strip()
    file.readline()
    rules = dict([line.strip().split(" -> ") for line in file.readlines()])


def part_1():
    current_sequence = sequence
    for _ in range(10):
        new_sequence = ""
        for first, second in zip(current_sequence, current_sequence[1:]):
            new_sequence += first + rules[first + second]
        # the final letter was not added so add it to the sequence
        current_sequence = new_sequence + second
    sorted_counts = Counter(current_sequence).most_common()
    return sorted_counts[0][1] - sorted_counts[-1][1]


def part_2():
    pair_counts = Counter()
    for first, second in zip(sequence, sequence[1:]):
        pair_counts[first + second] += 1
    for _ in range(40):
        updated_double_counts = Counter()
        for current, count in pair_counts.items():
            updated_double_counts[current[0] + rules[current]] += count
            updated_double_counts[rules[current] + current[1]] += count
        pair_counts = updated_double_counts
    single_letter_counter = Counter()
    for pattern, count in pair_counts.items():
        single_letter_counter[pattern[0]] += count
    # the final letter was not counted so add 1 to its count
    single_letter_counter[sequence[-1]] += 1
    sorted_counts = single_letter_counter.most_common()
    return sorted_counts[0][1] - sorted_counts[-1][1]


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
