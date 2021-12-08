import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/day8.txt"
signals = []
outputs = []
with open(input_file) as file:
    for line in file.readlines():
        first, second = line.strip().split(" | ")
        signals.append(first.split())
        outputs.append(second.split())

# DIGITS = {
#     0: "abcefg",  # 6
#     1: "cf",  # 2
#     2: "acdeg",  # 5
#     3: "acdfg",  # 5
#     4: "bcdf",  # 4
#     5: "abdfg",  # 5
#     6: "abdefg",  # 6
#     7: "acf",  # 3
#     8: "abcdefg",  # 7
#     9: "abcdfg",  # 6
# }


def sort_string(str):
    """Returns a string containing the same letters as the input argument
    but in sorted order

    Example: "dmfje" would return "defjm"
    """

    return "".join(sorted(str))


def get_number_mapping(signals):
    mapping = {}
    sorted_signals = [sort_string(signal) for signal in signals]
    for signal in sorted_signals:
        if len(signal) == 2:
            mapping[signal] = 1
            letters_in_one = set(signal)
        elif len(signal) == 4:
            mapping[signal] = 4
            letters_in_four = set(signal)
        elif len(signal) == 3:
            mapping[signal] = 7
            letters_in_seven = set(signal)
        elif len(signal) == 7:
            mapping[signal] = 8
    for signal in sorted_signals:
        if len(signal) == 6:
            if (letters_in_one & set(signal)) == letters_in_one:
                if len(letters_in_four & set(signal)) == 4:
                    mapping[signal] = 9
                else:
                    mapping[signal] = 0
            else:
                mapping[signal] = 6
        elif len(signal) == 5:
            if (letters_in_seven & set(signal)) == letters_in_seven:
                mapping[signal] = 3
            elif len(letters_in_four & set(signal)) == 3:
                mapping[signal] = 5
            else:
                mapping[signal] = 2
    return mapping


def part_1():
    return len([number for output in outputs for number in output if len(number) in (2, 4, 3, 7)])


def part_2():
    total = 0
    for current_signals, current_outputs in zip(signals, outputs):
        mapping = get_number_mapping(current_signals)
        current = ""
        for combination in current_outputs:
            current += str(mapping[sort_string(combination)])
        total += int(current)
    return total


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
