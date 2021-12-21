import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/21.txt"
with open(input_file) as file:
    p1_pos, p2_pos = [int(line.strip()[line.find(": ") + 1 :]) for line in file.readlines()]


def part_1():
    current_p1_pos, current_p2_pos = p1_pos, p2_pos
    p1_score, p2_score = 0, 0
    die_roll = 0
    while p1_score < 1000 and p2_score < 1000:
        roll = die_roll + 1 + die_roll + 2 + die_roll + 3
        die_roll += 3
        new_position = current_p1_pos + roll
        while new_position > 10:
            new_position -= 10
        p1_score += new_position
        current_p1_pos = new_position
        # swap positions and scores to switch turns
        p1_score, p2_score = p2_score, p1_score
        current_p1_pos, current_p2_pos = current_p2_pos, current_p1_pos
    return min(p1_score, p2_score) * die_roll


def part_2():
    calculated_already = {}

    def calculate_wins(p1_pos, p1_score, p2_pos, p2_score):
        if p1_score >= 21:
            return (1, 0)
        if p2_score >= 21:
            return (0, 1)
        # memoize to avoid repeated calculations
        if (p1_pos, p1_score, p2_pos, p2_score) in calculated_already:
            return calculated_already[(p1_pos, p1_score, p2_pos, p2_score)]
        win_totals = (0, 0)
        for die1 in (1, 2, 3):
            for die2 in (1, 2, 3):
                for die3 in (1, 2, 3):
                    new_p1_pos = p1_pos + die1 + die2 + die3
                    while new_p1_pos > 10:
                        new_p1_pos -= 10
                    new_p1_score = p1_score + new_p1_pos
                    # swap the players
                    new_p2_score, updated_p1 = calculate_wins(p2_pos, p2_score, new_p1_pos, new_p1_score)
                    win_totals = (win_totals[0] + updated_p1, win_totals[1] + new_p2_score)

        calculated_already[(p1_pos, p1_score, p2_pos, p2_score)] = win_totals
        return win_totals

    return max(calculate_wins(p1_pos, 0, p2_pos, 0))


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
