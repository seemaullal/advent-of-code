import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/day8.txt"
patterns = []
with open(input_file) as file:
    for line in file.readlines():
        first, second = line.strip().split(" | ")
        patterns.append([first.split(), second.split()])

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
    one_signal, four_signal, seven_signal = None, None, None
    sorted_signals = [sort_string(signal) for signal in signals]
    for signal in sorted_signals:
        if len(signal) == 2:
            mapping[signal] = 1
            one_signal = signal
        elif len(signal) == 4:
            mapping[signal] = 4
            four_signal = signal
        elif len(signal) == 3:
            mapping[signal] = 7
            seven_signal = signal
        elif len(signal) == 7:
            mapping[signal] = 8
    for signal in sorted_signals:
        if len(signal) == 6:
            if all([letter in signal for letter in one_signal]):
                if len([letter for letter in four_signal if letter in signal]) == 4:
                    mapping[signal] = 9
                else:
                    mapping[signal] = 0
            else:
                mapping[signal] = 6
        elif len(signal) == 5:
            if all([letter in signal for letter in seven_signal]):
                mapping[signal] = 3
            else:
                if len([letter for letter in four_signal if letter in signal]) == 3:
                    mapping[signal] = 5
                else:
                    mapping[signal] = 2
    return mapping


def part_1():
    total = 0
    for _signals, output in patterns:
        for combination in output:
            if len(combination) in (2, 4, 3, 7):
                total += 1
    return total


def part_2():
    total = 0
    for signals, output in patterns:
        mapping = get_number_mapping(signals)
        current = ""
        for combination in output:
            current += str(mapping[sort_string(combination)])
        total += int(current)
    return total


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
