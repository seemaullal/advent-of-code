import sys

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/21.txt"
with open(input_file) as file:
    p1_pos, p2_pos = [int(line.strip()[line.find(": ") + 1 :]) for line in file.readlines()]


def part_1():
    current_p1_pos = p1_pos
    current_p2_pos = p2_pos
    current_die_start = 1
    p1_score, p2_score = 0, 0
    player_1_turn = True
    die_roll = 0
    while p1_score < 1000 and p2_score < 1000:
        roll = current_die_start + current_die_start + 1 + current_die_start + 2
        die_roll += 3
        if player_1_turn:
            new_position = current_p1_pos + roll
            while new_position > 10:
                new_position -= 10
            p1_score += new_position
            current_p1_pos = new_position
            player_1_turn = False
        else:
            new_position = current_p2_pos + roll
            while new_position > 10:
                new_position -= 10
            p2_score += new_position
            current_p2_pos = new_position
            player_1_turn = True
        current_die_start += 3
    return min(p1_score, p2_score) * die_roll


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
