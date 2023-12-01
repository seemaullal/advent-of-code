with open("../inputs/2.txt") as file:
    moves = [turn.strip().split(" ") for turn in file]

scores = { 'X': 1, 'Y': 2, 'Z': 3 }
wins = { 'C': 'X', 'B': 'Z', 'A': 'Y' }
loses = { 'C': 'Y', 'B': 'X', 'A': 'Z' }
matches = { 'A': 'X', 'B': 'Y', 'C': 'Z' }

def part_1():
    score = 0
    for player1, player2 in moves:
        score += scores[player2]
        if wins[player1] == player2:
            score += 6
        elif matches[player1] == player2:
            score += 3
    return score


def part_2():
    score = 0
    for player1, instruction in moves:
        if instruction == 'X':
            player2 = loses[player1]
        elif instruction == 'Y':
            player2 = matches[player1]
            score += 3
        else:
            player2 = wins[player1]
            score += 6
        score += scores[player2]
    return score

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
