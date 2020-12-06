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