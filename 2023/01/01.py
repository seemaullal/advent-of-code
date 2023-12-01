def part_1():
    with open("../inputs/1.txt") as file:
        calibration_values = []
        for line in file:
            value = []
            for character in line:
                if character.isdigit():
                    value.append(character)
            calibration_values.append(int(f"{value[0]}{value[-1]}"))
    return sum(calibration_values)


WORD_TO_NUM = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part_2():
    with open("../inputs/1.txt") as file:
        calibration_values = []
        for line in file:
            value = []
            for index, character in enumerate(line):
                if character.isdigit():
                    value.append(character)
                else:
                    for word in WORD_TO_NUM:
                        word_length = len(word)
                        if line[index : index + word_length] == word:
                            value.append(WORD_TO_NUM[word])
            calibration_values.append(int(f"{value[0]}{value[-1]}"))
    return sum(calibration_values)


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
