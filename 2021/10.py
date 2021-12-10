import sys
from collections import deque

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/10.txt"
with open(input_file) as file:
    chunks = [list(chunk.strip()) for chunk in file.readlines()]


PAIRS = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}

SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

OPENING = {k for k in PAIRS.keys()}


def part_1():
    error_score = 0
    for line in chunks:
        seen = []
        for chunk in line:
            if chunk in OPENING:
                seen.append(chunk)
            elif PAIRS[seen[-1]] != chunk:
                error_score += SCORE[chunk]
                break
            else:
                seen.pop()
    return error_score


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
