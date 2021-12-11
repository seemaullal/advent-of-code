import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/10.txt"
with open(input_file) as file:
    chunks = [list(chunk.strip()) for chunk in file.readlines()]


PAIRS = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}

PART_1_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

PART_2_SCORES = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

OPENING = {k for k in PAIRS.keys()}


def solve_both_parts():
    error_score = 0
    autocomplete_scores = []
    for line in chunks:
        seen = []
        bad = False
        for chunk in line:
            if chunk in OPENING:
                seen.append(chunk)
            elif PAIRS[seen[-1]] != chunk:
                error_score += PART_1_SCORES[chunk]
                bad = True
                break
            else:
                seen.pop()
        if not bad:
            current_score = 0
            for char in reversed(seen):
                current_score = (current_score * 5) + PART_2_SCORES[char]
            autocomplete_scores.append(current_score)
    return error_score, sorted(autocomplete_scores)[len(autocomplete_scores) // 2]


def part_1():
    return solve_both_parts()[0]


def part_2():
    return solve_both_parts()[1]


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
