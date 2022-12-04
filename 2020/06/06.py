with open("inputs/6.txt") as file:
    groups = [group.split("\n") for group in file.read().split("\n\n")]


def part_1():
    yes_count = 0
    for group_answers in groups:
        answers = set()
        for answer in group_answers:
            for question in answer:
                answers.add(question)
        yes_count += len(answers)
    return yes_count


def part_2():
    all_in_group_yes_count = 0
    for group_answers in groups:
        yes_answers = set(list(group_answers[0]))
        for answer in group_answers:
            to_remove = set()
            for question in yes_answers:
                if question not in answer:
                    to_remove.add(question)
            yes_answers = yes_answers - to_remove
        all_in_group_yes_count += len(yes_answers)
    return all_in_group_yes_count


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
