# Needed for both parts
file = open('day6_input.txt')
groups = [group.split('\n') for group in file.read().split('\n\n')]

# part 1 
yes_count = 0
for group_answers in groups:
    answers = set()
    for answer in group_answers:
        for question in answer:
            answers.add(question)
    yes_count += len(answers)
print('part 1:', yes_count)

# part 2
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
print('part 2:', all_in_group_yes_count)